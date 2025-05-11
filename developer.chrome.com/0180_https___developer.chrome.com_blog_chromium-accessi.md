---
url: https://developer.chrome.com/blog/chromium-accessibility-performance?hl=en
title: https://developer.chrome.com/blog/chromium-accessibility-performance?hl=en
date: 2025-05-11T16:54:35.616718
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/chromium-accessibility-performance?hl=en#main-content)
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Nederlands
  * Português – Brasil
  * Tiếng Việt
  * Русский
  * العربيّة
  * ภาษาไทย
  * 中文 – 简体
  * 中文 – 繁體

Sign in


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  Improving the performance of Chromium accessibility 
Stay organized with collections  Save and categorize content based on your preferences. 
This post is from Chromium contributor ​​Ahmed Elwasefi, sharing how he became a contributor through the Google Summer of Code, and the accessibility performance issues he has identified and fixed.
Ahmed Elwasefi 
[ GitHub ](https://github.com/Ahmad45123) [ LinkedIn ](https://www.linkedin.com/in/ahmad45123)
As I approached my final year in computer engineering at the German University in Cairo, I decided to explore opportunities to contribute to open source. I began exploring Chromium's list of beginner-friendly issues and found myself particularly drawn to accessibility. My search for guidance led me to Aaron Leventhal, whose expertise and willingness to help inspired me to team up with him for a project. This collaboration became my [Google Summer of Code](https://summerofcode.withgoogle.com/) experience, where I was accepted to work with the Chromium Accessibility Team.
After successfully completing Google Summer of Code, I continued to address an unresolved scrolling issue, driven by the desire to improve performance. Thanks to two grants from Google's OpenCollective program, I was able to keep working on this project while also taking on additional tasks focused on streamlining code for better performance.
This blog post shares my journey with Chromium over the last year and a half, detailing the technical improvements we've made, particularly in the area of performance.
## How accessibility code impacts performance in Chrome
Chrome's accessibility code helps assistive technologies like screen readers access the web. However, when enabled, it can impact loading times, performance, and battery life. Therefore, if not needed, this code remains inactive to avoid slowing down performance. Approximately 5-10% of users have accessibility code enabled, often due to tools like password managers and antivirus software that use platform accessibility APIs. These tools rely on these APIs to interact with and modify page content, such as locating password fields for password managers and form fillers.
The total degradation in core metrics is not yet known, but a recent experiment called Auto Disable Accessibility (turning off accessibility when it is not used), shows it's quite high. The problem occurs because of the massive amounts of computation and communication in two main areas of Chrome's accessibility codebase: the renderer and the browser. The renderer gathers information about web contents and changes to content, computing accessibility properties for a tree of nodes. Any dirty nodes are then serialized and sent through a pipe to the browser process' main UI thread. This thread receives and deserializes this information into the identical tree of nodes and then finally converts it to a suitable form for third party assistive technologies such as screen readers.
## Improvements to Chromium accessibility
The following projects were completed during Summer of Code and then afterward, funded by the Google OpenCollective program.
### Cache improvement
In Chrome, there's a special data structure called the _accessibility tree_ that mirrors the DOM tree. It's used to help assistive technologies access web content. Sometimes, when a device needs information from this tree, it might not be ready, so the browser has to schedule those requests for later.
Previously, this scheduling was handled using a method called closures, which involved placing callbacks into a queue. This approach added extra work because of how closures are processed.
To improve this, we switched to a system using enums. Each task is assigned a specific enum value, and once the accessibility tree is ready, the correct method for that task is called. This change made the code easier to understand and improved performance by over _20%_.
A graph of runtimes of several performance tests where there's a visible drop of about 20% across all of them.
### Finding and fixing scroll performance issues
Next, I explored how performance improves when we turn off bounding box serialization. _Bounding boxes_ are the positions and sizes of elements on a web page, including details like width, height, and their position relative to their parent element.
To test this, we temporarily removed the code that handles bounding boxes and ran performance tests to see the impact. One test, _focus-links.html_ showed a huge improvement of about 1618%. This discovery became the foundation for further work.
#### Investigating the slow test
I started investigating why that specific test was slow with bounding boxes. All the test did was place focus on several links one after the other. Therefore, the main issue must be either focusing on elements or the scrolling that happened with focus action. To test this, I added `{preventScroll: true}` to the `focus()` call in the performance test, stopping the scrolling.
With scrolling disabled, the test time dropped to 1.2 milliseconds when bounding box calculations were active. This showed that scrolling was the real problem.
Focus-links test runtime drops from 20 ms to 1.1 ms when scrolling is disabled or bounding box serialization is removed.
I created a new test called _scroll-in-page.html_ to replicate the _focus-links_ test, but instead of using focus, it scrolls through elements with `scrollIntoView()`. I tested both smooth and instant scrolling, with and without bounding box calculations.
Time taken to process scrolls in instant scrolling is 65 ms while smooth scrolling takes 123 ms.
The results showed that with instant scrolling and bounding boxes, the process took about 66ms. Smooth scrolling was even slower at around 124ms. When we turned off bounding boxes, it took no time at all because no events were triggered.
#### We knew the case, but why was it happening?
We'd now learned that scrolling is the source of a lot of slowness in accessibility serialization, but we still had to find out why. To analyze this, Two tools called _perf_ and _pprof_ were used to break down the work done in the browser process. These tools are often used in C++ for profiling. The following graphs shows a snippet of the interesting part.
A graph generated from profiling of scrolling tests. Shows that time is mostly spent in calls to a function called Unserialize as well as another called IsChildOfLeaf.
After investigating, we found that the issue wasn't the deserialization code itself, but the frequency of calls to it. To understand this, we need to look at how accessibility updates work in Chromium. Updates aren't sent individually; instead, there's a central location called `AXObjectCache` that stores all properties. When a node changes, various methods notify the cache to mark that node as _dirty_ for later serialization. Then, all properties of dirty notes, including unchanged properties, are serialized and sent to the browser. While this design simplifies the code and reduces complexity by having a single update path, it becomes slow when there are rapid "mark as dirty" events, such as those from scrolling. The only thing that changes is the `scrollX` and `scrollY` values; yet, we serialize the rest of the properties with them every time. The rate of updates here reached over twenty times per second!
Bounding box serialization addresses this issue by using a faster serialization path that only sends the bounding box details, allowing quick updates without affecting other properties. This method efficiently handles bounding box changes.
#### Scrolling fix
The solution was clear: include the current scroll offsets with bounding box serialization. This ensures that scrolling updates are processed through the fast path, enhancing performance without unnecessary delays. By packing scroll offsets with bounding box data, we optimize the process for smoother and more efficient updates, creating a less janky experience for users with accessibility turned on. The improvement after the implementation of the fix is _up to 825%_ in scrolling tests.
### Code simplifications
In this period, I focused on code quality as part of a project called Onion Soup, which simplifies the code by reducing or removing unnecessarily spreading code across layers.
The [first project](https://chromium-review.googlesource.com/c/chromium/src/+/5321720) aimed to streamline the way accessibility data is serialized from the renderer to the browser. Previously, the data had to pass through an extra layer before reaching its destination, which added unnecessary complexity. We simplified this process by allowing the data to be sent directly, cutting out the middleman.
Additionally, we identified and removed some outdated events that were causing unnecessary work in the system, like one that triggered when a layout was complete. We replaced these with a more efficient solution.
There were also other small improvements made. Unfortunately, performance improvements were not recorded for these, but we're proud to share that the code is a lot clearer and self documenting than it was. This helps a lot to pave the way for future performance improvements. You may check the actual changes over in my [gerrit profile](https://chromium-review.googlesource.com/q/owner:a.m.elwasefi@chromium.org).
## Conclusion
Working with the Chromium Accessibility Team has been a rewarding journey. Through tackling various challenges, from optimizing scrolling performance to simplifying the codebase, I've gained a deeper understanding of development in such a large scale project as well as learning important tools for profiling. In addition, I've learned how crucial accessibility is for creating a web that's inclusive for everyone. The improvements we've made not only enhance the user experience for those relying on assistive technologies but also contribute to the overall performance and efficiency of the browser.
The performance results have been impressive. For example, the switch to using enums for scheduling tasks improved performance by _over 20%_. Additionally, our scrolling fix resulted in up to an _825%_ reduction in scrolling tests. Code simplifications changes have not only made the code clearer and more maintainable, but also paved the way for future enhancements.
I would like to express my gratitude to Stefan Zager, Chris Harrelson, and Mason Freed for their support and guidance throughout the year, and especially to Aaron Leventhal, without whom this opportunity wouldn't have been possible. I'd also like to thank Tab Atkins-Bittner and the GSoC team for their support.
For those looking to contribute to a meaningful project and develop their skills, I highly recommend getting involved with Chromium. It's a great way to learn, and programs like Google Summer of Code offer an excellent starting point for your journey.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-08-20 UTC.

