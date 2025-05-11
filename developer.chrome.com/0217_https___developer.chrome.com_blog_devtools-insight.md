---
url: https://developer.chrome.com/blog/devtools-insights-sidebar?hl=en
title: https://developer.chrome.com/blog/devtools-insights-sidebar?hl=en
date: 2025-05-11T16:55:21.006086
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/devtools-insights-sidebar?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/devtools-insights-sidebar?hl=es-419)

Sign in


  * On this page
  * [Using the Insights sidebar](https://developer.chrome.com/blog/devtools-insights-sidebar?hl=en#using_the_insights_sidebar)
  * [Insights for page load](https://developer.chrome.com/blog/devtools-insights-sidebar?hl=en#insights_for_page_load)
    * [Page load insights beyond LCP](https://developer.chrome.com/blog/devtools-insights-sidebar?hl=en#page_load_insights_beyond_lcp)
  * [Insights for responsiveness](https://developer.chrome.com/blog/devtools-insights-sidebar?hl=en#insights_for_responsiveness)
  * [Insights for layout stability](https://developer.chrome.com/blog/devtools-insights-sidebar?hl=en#insights_for_layout_stability)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  Insights sidebar in the DevTools Performance panel 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Using the Insights sidebar](https://developer.chrome.com/blog/devtools-insights-sidebar?hl=en#using_the_insights_sidebar)
  * [Insights for page load](https://developer.chrome.com/blog/devtools-insights-sidebar?hl=en#insights_for_page_load)
    * [Page load insights beyond LCP](https://developer.chrome.com/blog/devtools-insights-sidebar?hl=en#page_load_insights_beyond_lcp)
  * [Insights for responsiveness](https://developer.chrome.com/blog/devtools-insights-sidebar?hl=en#insights_for_responsiveness)
  * [Insights for layout stability](https://developer.chrome.com/blog/devtools-insights-sidebar?hl=en#insights_for_layout_stability)


Brendan Kenny 
[ GitHub ](https://github.com/brendankenny) [ Bluesky ](https://bsky.app/profile/brendankenny.bsky.social)
Published: April 02, 2025 
The **Performance** panel in Chrome DevTools is incredibly powerful, containing data for almost any possible problem in your site's runtime behavior. That wealth of data can be overwhelming, though: it can be difficult for many developers to know where to start, and even experts can have trouble isolating a particular issue within a complex page load.
Tools like Lighthouse were developed to address this, analyzing performance traces and reporting a concise list of potential issues and how you might address them. But this has a tradeoff as well: disconnected from the details, it can be difficult to see when in the timeline that issues occur relative to each other. And, if you want to understand the context within the full trace, you have to start from scratch in the Performance panel.
The new **Insights** sidebar is bridging the gap by bringing Lighthouse insights directly into the **Performance** panel. Recommendations are now right in the panel when looking at a trace, but, more importantly, the integration allows insights to highlight events and overlay explanations directly in the performance timeline. Hover over an insight to zoom in and highlight the relevant parts of the trace, visualize critical paths, or flag performance bottlenecks within their full context.
The DevTools Performance panel with the Insights sidebar on the left
## Using the Insights sidebar
You may have already noticed the new sidebar, which was added in Chrome 131 with some initial insights and has gained more insights in each new Chrome release since.
To see it, hit radio_button_checked **Record** in the Performance panel, load a URL or interact with a page, and then stop the recording. The sidebar may be collapsed to the left-hand side of the Performance panel if you've closed it in the past. To reveal it, click the left_panel_open button, and there will be a list of insights to serve as entry points to investigating performance issues.
Similar to a Lighthouse report, the sidebar will list a set of insights for the recording you just took, identifying performance or UX issues, or providing data to help you filter and diagnose issues yourself. At the bottom is a collapsed **Passed insights** section, which has insights that weren't identified as problematic for this recording, whether because a particular performance issue didn't occur, or the insight just wasn't applicable at all (for example, if you took a trace of interactions with the page and didn't navigate).
Screen recording of navigating the Insights sidebar
Finally, if the trace you recorded includes navigations to multiple pages, each page will get its own set of insights that you can flip through to investigate each navigation separately. Click the center_focus_weak icon next to the URL and the timeline view will zoom into the part of the trace which occurred while on that page.
## Insights for page load
A fast page load is essential for a good user experience, and [Largest Contentful Paint (LCP)](https://web.dev/articles/lcp) is the Core Web Vital focused on measuring page load. The Insights sidebar offers dedicated insights for improving LCP, as well as insights for aspects of page load beyond LCP.
### LCP insights
For understanding and improving LCP, a good place to start is with LCP phases, an [approach to breaking down the time to LCP into four subparts and addressing them separately](https://web.dev/articles/optimize-lcp#lcp-breakdown).
Click **LCP by phase** in the Insights tab on the left, and the breakdown of time spent in each subpart is shown in the Insights tab. Hovering or clicking on each subpart in the Insights tab will highlight or zoom into each subpart in the performance timeline, to investigate events within that period. If you have [Field data enabled](https://developer.chrome.com/docs/devtools/performance/overview#compare) and [image LCP load data is available for your site](https://developer.chrome.com/blog/crux-2025-02#lcp_image_subparts), the 75th percentile values for the subparts will also be included in the insight.
Screen recording of the LCP by phase insight
**LCP request discovery** will suggest improvements in how to load the LCP resource, one of the [most common issues affecting LCP](https://web.dev/blog/common-misconceptions-lcp) across the web. It overlays the timeline with annotations that mark when the image could have been loaded, and the estimated loading time that could have been saved.
Screenshot of the LCP request discovery insight
Further insights help identify issues within LCP subparts. **Document request latency** highlights potential optimizations in the navigation request to the server. **Render blocking requests** points out requests that will block the initial render of the page until they are complete, even if content (like LCP) is ready to be displayed.
### Page load insights beyond LCP
Additional insights help identify potential issues impacting overall page load performance beyond LCP.
One of the biggest challenges is the performance of third party resources. Often they're necessary for business reasons, but web developers have little direct control over their performance. The **3rd parties** insight categorizes resources and CPU activity by first and third-party entities, showing which entities consumed the most time and resources. Hovering over each entity will highlight their activity within the performance and network timelines. This insight works in tandem with the ["Dim 3rd parties" checkbox and the new 1st/3rd party entries in the Summary tab](https://developer.chrome.com/blog/devtools-navigate-and-filter#dim_3rd-party_scripts).
Screenshot of the 3rd parties insight
**Font display** will list fonts that could have used `font-display: swap` or `optional` to not prevent text from being shown during font loads.
Screenshot of the Font display insight
**Network dependency tree** identifies long chains of dependencies within your page load, where resource A loads resource B loads resource C, and C is important for the look or functionality of the page. Each dependent request can add significant latency to loading the full chain, especially for users on worse connections.
Screenshot of the Network dependency tree insight
And finally, for image resources, **Improve image delivery** identifies images that could be significantly optimized, potentially wasting significant download time fetching unnecessary extra bytes.
Screenshot of the Improve image delivery insight
## Insights for responsiveness
[Interaction to Next Paint (INP)](https://web.dev/articles/inp) can be [broken down into subparts](https://web.dev/articles/optimize-inp#optimize_interactions), similar to LCP. The **INP by phase** insight will add overlays to the performance timeline to highlight these subparts, helping you see their direct relation to main thread activity.
Screenshot of the INP by phase insight
Interactions that update the page often spend significant time recalculating styles and layout. One of the best predictors for how long style and layout will take is the size of the DOM, both in the total number of nodes and the depth of the tree. **Optimize DOM size** reports the page's DOM size, and highlights events that were likely made worse by the large DOM size.
Screenshot of the Optimize DOM size insight
**Forced reflow** alerts on a common threat to responsiveness: interleaved reads and writes to the DOM that require the browser to do layout, for example adding new elements to the DOM then calling a DOM function that reads the size of some element on screen. Even if you know that two parts of the DOM don't affect each other's layout, without explicit [content containment](https://developer.mozilla.org/docs/Web/CSS/content-visibility), the browser may still be forced to re-layout the full page due to unknown dependencies between the two.
Screenshot of the Forced reflow insight
Most pages on the web now set an explicit [mobile viewport](https://developer.mozilla.org/docs/Web/HTML/Viewport_meta_tag), but if they don't, they [risk spending hundreds of extra milliseconds on every click](https://developer.chrome.com/blog/300ms-tap-delay-gone-away) while the browser waits for possible additional input. The **Optimize viewport for mobile** insight alerts when the viewport isn't set correctly.
Screenshot of the Optimize viewport for mobile insight
Finally, if the **Enable CSS Selector stats (slow)** option is selected, the **CSS selector costs** insight will appear, providing an overview of [style recalculation performance](https://developer.chrome.com/docs/devtools/performance/selector-stats). Note that the **Enable CSS selector stats (slow)** option that needs to be enabled for this insight will slow down page performance significantly.
## Insights for layout stability
[Cumulative Layout Shift (CLS)](https://web.dev/articles/cls) gets its own **Layout shifts** track within the timeline, showing individual shifts [grouped into windows (clusters) of up to five seconds](https://web.dev/articles/cls#what-is-cls), which are used to calculate the CLS score.
The **Layout shift culprits** insight highlights the worst CLS cluster, and lists the individual layout shifts within it. Hovering over each shift in the list or the track will show a screenshot of the page, visualizing the shift with an animated overlay.
Screen recording of the Layout shift culprits insight
## Conclusion
Insights aim to bring the power of Lighthouse into the full context of the **Performance** panel, making traces easier to understand and making insights connected to the data they come from.
We are actively improving the current insights and more are on the way. Try out the Insights sidebar and [let us know](https://crbug.com/371170842) all the ways they could be improved or what other insights you'd love to see.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-04-02 UTC.

