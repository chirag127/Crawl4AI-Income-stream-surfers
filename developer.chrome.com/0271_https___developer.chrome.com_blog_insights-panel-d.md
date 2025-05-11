---
url: https://developer.chrome.com/blog/insights-panel-deprecation?hl=en
title: https://developer.chrome.com/blog/insights-panel-deprecation?hl=en
date: 2025-05-11T16:56:30.302361
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/insights-panel-deprecation?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/insights-panel-deprecation?hl=es-419)




  * On this page
  * [Give us feedback](https://developer.chrome.com/blog/insights-panel-deprecation?hl=en#give_us_feedback)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  Deprecation of the Performance Insights panel 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Give us feedback](https://developer.chrome.com/blog/insights-panel-deprecation?hl=en#give_us_feedback)


Brendan Kenny 
[ GitHub ](https://github.com/brendankenny) [ Bluesky ](https://bsky.app/profile/brendankenny.bsky.social)
As [announced earlier this year](https://developer.chrome.com/blog/perf-tooling-2024#the_experimental_performance_insights_panel_will_be_deprecated), the Chrome 131 release officially deprecates the experimental Performance Insights panel. It will be removed from DevTools completely in the next Chrome release, early in 2025.
The [Performance panel](https://developer.chrome.com/docs/devtools/performance/overview) contains so much information, it could be difficult to know where to even begin. The Performance _Insights_ panel [was an experiment](https://developer.chrome.com/docs/devtools/performance-insights#why_a_new_panel) on ways to automatically isolate and focus on the relevant parts of that information for debugging of specific performance and user experience issues, especially [Core Web Vitals](https://web.dev/articles/vitals).
The best of those experiments are now being folded back into the Performance panel, combined with the Lighthouse audit engine, and appear as new insights within the Performance panel itself. A sidebar and additional data overlaying the timeline will provide insights into how a page loads and runs, and give advice on improving performance and the user experience.
If you're looking to improve your site, the insights can give a great list of where to start. If you're diving deep into a specific performance or architectural issue, the insights can provide entry points, as well as context for when you're immersed in the minutiae of a trace, aiming to help you keep an eye on the bigger picture.
## Give us feedback
Many of these insights may seem familiar from the Performance Insights panel and Lighthouse, but in a brand new context within the Performance panel. Try them out and [let us know](https://crbug.com/371170842) all the ways they could be improved or what other insights you'd love to see.
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-11-26 UTC.

