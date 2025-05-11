---
url: https://developer.chrome.com/blog/devtools-realtime-cwv?hl=en
title: https://developer.chrome.com/blog/devtools-realtime-cwv?hl=en
date: 2025-05-11T16:55:27.444245
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/devtools-realtime-cwv?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/devtools-realtime-cwv?hl=es-419)

Sign in


  * On this page
  * [Real-time local Core Web Vitals performance](https://developer.chrome.com/blog/devtools-realtime-cwv?hl=en#local-metrics)
  * [Real-user experience data](https://developer.chrome.com/blog/devtools-realtime-cwv?hl=en#field-data)
  * [Recommendations to configure your local environment](https://developer.chrome.com/blog/devtools-realtime-cwv?hl=en#config)
  * [Information to help you reproduce issues](https://developer.chrome.com/blog/devtools-realtime-cwv?hl=en#repro)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  Monitor your local and real-user Core Web Vitals performance in DevTools 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Real-time local Core Web Vitals performance](https://developer.chrome.com/blog/devtools-realtime-cwv?hl=en#local-metrics)
  * [Real-user experience data](https://developer.chrome.com/blog/devtools-realtime-cwv?hl=en#field-data)
  * [Recommendations to configure your local environment](https://developer.chrome.com/blog/devtools-realtime-cwv?hl=en#config)
  * [Information to help you reproduce issues](https://developer.chrome.com/blog/devtools-realtime-cwv?hl=en#repro)


Rick Viscomi 
[ GitHub ](https://github.com/rviscomi) [ Bluesky ](https://bsky.app/profile/rviscomi.dev) [ Homepage ](https://developer.chrome.com/rviscomi.dev/)
Published: September 17, 2024 
In the previous post, we looked at three new features to help you [customize your performance workflows](https://developer.chrome.com/blog/devtools-customization) in DevTools. These ergonomic improvements were just the start of our [multi-year effort](https://developer.chrome.com/blog/perf-tooling-2024) to make DevTools even easier and more capable for optimizing Core Web Vitals. Today, we're launching of the next batch of features: **a completely redesigned Performance panel landing page featuring a live view of your local Core Web Vitals performance**.
Local and field metrics in the DevTools Performance panel
In this post we'll take a closer look at each of the new features:
  * [Real-time local Core Web Vitals performance](https://developer.chrome.com/blog/devtools-realtime-cwv?hl=en#local-metrics)
  * [Real-user experience data](https://developer.chrome.com/blog/devtools-realtime-cwv?hl=en#field-data)
  * [Recommendations to configure your local environment](https://developer.chrome.com/blog/devtools-realtime-cwv?hl=en#config)
  * [Information to help you reproduce issues](https://developer.chrome.com/blog/devtools-realtime-cwv?hl=en#repro)


## Real-time local Core Web Vitals performance
The ability to measure how your local experience performs is a critical part of any Core Web Vitals debugging workflow. It can make the difference between reproducing real-user issues or not. However, measuring your local performance wasn't always this easy.
The trace view in the DevTools Performance panel
Historically, the Performance panel in DevTools shows a detailed timeline of network requests and CPU activity which is a very useful tool for performance debugging. However, it can be difficult to reproduce performance issues because you don't know if the performance is poor until after the recording finishes. As we've learned from the [Web Vitals extension](https://web.dev/articles/debug-cwvs-with-web-vitals-extension), having access to your local Core Web Vitals performance in DevTools is a game-changer. So we've taken everything we've learned from the extension and decided to build these features directly into the Performance panel.
For the first time, all of your Core Web Vitals metrics are available in the Performance panel. Open up the Performance panel and you'll immediately see how your local experience performs—no recording necessary. In fact, you don't even need to have DevTools open; the metrics are gathered in the background and available whenever you need it. This comes in handy all of those times when you may not be actively trying to debug a specific issue, but something feels slow, and you want to understand why.
Local Core Web Vitals metrics
The **Local metrics** section of the panel features a live view of your local Core Web Vitals metrics: Largest Contentful Paint, Cumulative Layout Shift, and Interaction to Next Paint. As you load and interact with the page, these metrics will update in real time. They're also color-coded according to their respective [thresholds](https://web.dev/articles/vitals#core-web-vitals) for good and poor performance, making it easier to spot performance issues as they happen.
## Real-user experience data
Optimizing performance issues that most users never experience may not be the best use of your time. Likewise, if your local experience is unrealistically fast, you're probably overlooking some real-world issues. So to make a more informed decision about how to invest your time, you should be comparing your local performance to real-user experience data from the field.
Local and field-based Core Web Vitals metrics side by side
The Performance panel now gives you a way to see your real-user data right next to your local experiences. The data is powered by the public [CrUX API](https://developer.chrome.com/docs/crux/api), which is a 28-day aggregation of real-user experiences on a given web page and origin. To enable it, click **Set up** in the **Field data** section and follow the directions in the configuration dialog.
Note that individual URLs and origins (entire websites) must meet certain [eligibility criteria](https://developer.chrome.com/docs/crux/methodology#eligibility) to be included in the CrUX dataset. User experiences are also aggregated by desktop and mobile device types when there's sufficient data. DevTools will do its best to automatically show the most relevant data to your local experience, defaulting to the same URL and device type when available. If there's insufficient desktop or mobile-level data, it will attempt to show data aggregated over all device types.
Comparison of local and field-based LCP
In addition to the 75th percentile value, you can hover over any metric to see the proportions of real-user experiences within each rating. In this example, the local Largest Contentful Paint experience is atypically slow, similar to only 12% of real-user experiences.
Equipped with this data, you'll have a much clearer picture of how representative your local experience is and you'll be able to [fine tune it](https://developer.chrome.com/blog/devtools-realtime-cwv?hl=en#config) to more closely emulate a typical user experience.
## Recommendations to configure your local environment
There are many [differences between lab and field data](https://web.dev/articles/lab-and-field-data-differences), which are compounded by all the ways one can access and interact with a page. You can account for some of these differences and make your local experience more representative by configuring your environment.
CPU and network settings
When field data is enabled and available, the **Recording settings** section will suggest emulating the most common device type used by real users. By enabling [device mode](https://developer.chrome.com/docs/devtools/device-mode) you can emulate a mobile device's viewport size. Responsive interfaces might change which element is attributed to the Largest Contentful Paint and have very different performance characteristics. The mobile layout might also reveal certain elements, like a navigation menu that only mobile users can interact with, or incur unique kinds of layout shifts not otherwise experienced on larger viewports.
This section may also recommend a specific network throttling configuration, like **Slow 4G**. Network recommendations are based on the 75th percentile [round trip time](https://developer.chrome.com/docs/crux/methodology/metrics#round-trip-time-metric) metric, aggregated from real-user experiences on that page or website. Slower network speeds can make the loading performance characteristics of the page more realistic—for real-world desktop and mobile users alike—which can make it easier to spot opportunities for improvement. Also consider that layout shifts only count towards the Cumulative Layout Shift metric if they don't occur within 500 ms of an interaction. If a [user-initiated layout shift](https://web.dev/articles/cls#user-initiated_layout_shifts) is the result of a network request, throttling the network may be the only way to expose it locally.
Throttling your CPU is another way to make your local device perform more like real users. CPU throttling better emulates the relatively slower way that mobile devices tend to perform, with faster machines requiring even more throttling. DevTools recently added the ability to [throttle your CPU by 20x](https://developer.chrome.com/blog/new-in-devtools-126#throttle-20x), which is especially useful for the performant desktop machines that developers often use. A throttled CPU will cause scripts to run more slowly, making them more likely to become [long tasks](https://web.dev/articles/optimize-long-tasks) that lead to Interaction to Next Paint issues. For the same reason, the other Core Web Vitals metrics can also be affected by slower script execution, especially if it blocks the rendering of the largest piece of content or elements that shift the layout.
Configuring your local environment with more realistic viewport, network, and CPU settings should bring more performance issues to the surface that you might not have otherwise known about. And with recommendations powered by real-user data taking the guesswork out of it, you can focus more on finding and fixing those issues.
## Information to help you reproduce issues
Your local performance is heavily dependent on how your environment is configured and how you interact with the page. For example, on a typical web page, the Largest Contentful Paint element is [less likely to be an image](https://almanac.httparchive.org/en/2022/performance#lcp-content-types) at mobile viewport sizes. Typing a single character into a text field may be fast, but typing many of them in quick succession may cause poor Interaction to Next Paint. To help make sense of this and have more reproducible experiences, additional information about the metrics is available.
Highlighting the LCP element and viewing it in the Elements panel
The **LCP Element** associated with the Largest Contentful Paint metric shows a link to the element itself. Hovering over the link highlights the element on the page. Clicking the link takes you to the Elements panel, so you can see the element in the full context of the document.
The interaction log with one slow interaction
The **Interactions** section is a real time log of [all eligible interactions](https://web.dev/articles/inp#whats_in_an_interaction) that occur while DevTools is open. As you type, tap, or click, each interaction is added to the log with additional information to help you better understand what happened and how to reproduce it.
In addition to the interaction type, which is either a pointer or keyboard event, you'll see a reference to the interaction target. Similar to the **LCP element** , the interaction target itself is interactive and you can hover over it to highlight it on the page or click it to see it in the Elements panel. The interaction latency is also shown, using the same color-coding per the Interaction to Next Paint metric thresholds, making it easier to spot the slowest ones.
Performance profile recording options
When you're able to reproduce the performance issue you're trying to debug, you're ready to [start profiling](https://developer.chrome.com/docs/devtools/performance/reference#record). Under the **Next steps** section, use the **Record and reload** button to debug loading performance issues, like Largest Contentful Paint and [load-time](https://web.dev/articles/optimize-cls#identifying-load-cls-issues) Cumulative Layout Shift. To debug issues that happen as a result of user interactions, use the **Record** button to profile the page while manually reproducing slow interactions or [post-load layout shifts](https://web.dev/articles/optimize-cls#identifying-post-load-cls-issues).
## What's next
Grounding your performance workflows in real-time local data and real-user data from the field can help you decide whether to invest more or less effort in debugging and optimizing a metric. You should use this data to adjust your local environment to more realistically emulate your users' device types, CPU speeds, or network configurations to better reproduce their performance issues.
For any users of the Web Vitals extension, you'll probably recognize many of these features and so you might be wondering what this means for the extension. We'll be sharing more information in the coming weeks about how these changes impact the extension.
We're still just getting started with all of our Performance panel improvements, and there's so much more yet to come. We'll post here again with another update soon, but until then we encourage you to try out all of these new features in the Performance panel and let us know what you think. If you have any feedback, we'd love to read your comments in the [public issue](https://crbug.com/329541444).
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-09-17 UTC.

