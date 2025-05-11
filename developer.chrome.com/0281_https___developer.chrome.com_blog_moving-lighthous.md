---
url: https://developer.chrome.com/blog/moving-lighthouse-to-insights?hl=en
title: https://developer.chrome.com/blog/moving-lighthouse-to-insights?hl=en
date: 2025-05-11T16:56:47.742908
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/moving-lighthouse-to-insights?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/moving-lighthouse-to-insights?hl=es-419)




  * On this page
  * [Renamed and consolidated audits](https://developer.chrome.com/blog/moving-lighthouse-to-insights?hl=en#renamed_and_consolidated_audits)
  * [Migrate to the new insights audits](https://developer.chrome.com/blog/moving-lighthouse-to-insights?hl=en#migrate_to_the_new_insights_audits)
  * [Documentation for the new insights audits](https://developer.chrome.com/blog/moving-lighthouse-to-insights?hl=en#documentation_for_the_new_insights_audits)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  Lighthouse is moving to performance insight audits 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Renamed and consolidated audits](https://developer.chrome.com/blog/moving-lighthouse-to-insights?hl=en#renamed_and_consolidated_audits)
  * [Migrate to the new insights audits](https://developer.chrome.com/blog/moving-lighthouse-to-insights?hl=en#migrate_to_the_new_insights_audits)
  * [Documentation for the new insights audits](https://developer.chrome.com/blog/moving-lighthouse-to-insights?hl=en#documentation_for_the_new_insights_audits)


Barry Pollard 
[ GitHub ](https://github.com/tunetheweb) [ Mastodon ](https://webperf.social/@tunetheweb) [ Bluesky ](https://bsky.app/profile/tunetheweb.com) [ Homepage ](https://www.tunetheweb.com)
Published: April 28, 2025 
Over a year ago, we [announced our intention to evolve our performance tooling](https://developer.chrome.com/blog/perf-tooling-2024) including bringing "the power of Lighthouse, in[to] the Performance panel". The intent was to bring our many performance tooling surfaces together.
On the Performance Panel side, we have made great progress on that goal, and the [Insights sidebar now provides Lighthouse-like information that works with the trace](https://developer.chrome.com/blog/devtools-insights-sidebar). As part of this work, we have made a number of changes to the performance advice that Lighthouse users are familiar with: in some cases advice from many audits is consolidated into a single insight, and we have retired some advice.
Staying with our aim to consolidate our tooling surfaces, we want to bring those Insights back to Lighthouse. Both for consistency, and also so that Lighthouse users can benefit from the improvements we've made to these audits—plus any future improvements!
Unfortunately this does mean some breaking changes for Lighthouse users, especially the API users that may be used to certain audit names or result formats. For this reason we will wait for the next major release of Lighthouse (13) before we make this switch—which we're aiming for in October 2025. After this time, the old audit data will no longer be available.
## Renamed and consolidated audits
The following audits have been renamed and in some cases are consolidated from more than one Lighthouse audit:
New insight audit id | Replacing audit id(s)  
---|---  
`cls-culprits-insight` |  `layout-shifts` `non-composited-animations[](https://developer.chrome.com/docs/lighthouse/performance/non-composited-animations)` `unsized-images`  
`document-latency-insight` |  `uses-text-compression[](https://developer.chrome.com/docs/lighthouse/performance/uses-text-compression)`  
`dom-size-insight` |   
`duplicated-javascript-insight` | `duplicated-javascript`  
`font-display-insight` |   
`image-delivery-insight` |  `uses-optimized-images[](https://developer.chrome.com/docs/lighthouse/performance/uses-optimized-images)` `efficient-animated-content[](https://developer.chrome.com/docs/lighthouse/performance/efficient-animated-content)` `uses-responsive-images[](https://developer.chrome.com/docs/lighthouse/performance/uses-responsive-images)`  
`interaction-to-next-paint-insight` | `work-during-interaction`  
`lcp-discovery-insight` |  `prioritize-lcp-image` `lcp-lazy-loaded`  
`lcp-phases-insight` | `largest-contentful-paint-element`  
`legacy-javascript-insight` | `legacy-javascript`  
`modern-http-insight` |   
`network-dependency-tree-insight` |  `critical-request-chains[](https://developer.chrome.com/docs/lighthouse/performance/critical-request-chains)`  
`render-blocking-insight` | `render-blocking-resources[](https://developer.chrome.com/docs/lighthouse/performance/render-blocking-resources)`  
`third-parties-insight` |   
`use-cache-insight` |   
`viewport-insight` |   
Renamed and consolidated audits
## Removed audits
The following audits have been removed as it was felt these no longer served useful purposes:
**Removed audits** | **Reason for removal**  
---|---  
`first-meaningful-paint[](https://developer.chrome.com/docs/lighthouse/performance/first-meaningful-paint)` | Older metric that is no longer recommended (replaced by LCP)  
| Rarely an issue in first-party scripts these days, and it is inactionable for third-party scripts that use this.  
| Offscreen images are already deprioritized by the browser so while lazy loading helps reduce bandwidth, it is unlikely to have an impact on what Lighthouse measures.  
`uses-passive-event-listeners[](https://developer.chrome.com/docs/lighthouse/best-practices/uses-passive-event-listeners)` | Rarely an issue in first-party scripts these days, and it is inactionable for third-party scripts that use this.  
| Not enabled due to risks of over recommending.  
| This audit covers limited facades and some developers expressed concern using non-affiliated third-party facades. Ultimately, we would prefer the third-parties improve their offerings rather than work around them.  
Removed audits
## Other audits
The other Performance audits not included in the previous tables won't be affected by this change. Similarly, the audits for [Accessibility](https://developer.chrome.com/docs/lighthouse/accessibility), [SEO](https://developer.chrome.com/docs/lighthouse/seo), and [Best Practices](https://developer.chrome.com/docs/lighthouse/best-practices) also won't be affected by this change.
## Migrate to the new insights audits
To facilitate the migration, we've already made the new insights available in the Lighthouse JSON. Consumers of the API and the Lighthouse JSON can start migrating now to prepare for the eventual removal of the old audits in Lighthouse 13.
Lighthouse 12.6 (included in Chrome 137) will also show a visible toggle to allow users of the report to toggle between the two different views:
Trying insights in Lighthouse.
The new insights-based audits will show under an **Insights** heading, while the unchanged audits will continue to show under a **Diagnostics** heading.
At the moment, the default is to continue to show the old audits, but in a June 2025 Lighthouse release (likely 12.7), we plan to switch the default to the newer insights audits. This change will also be rolled out to PageSpeed Insights and DevTools Lighthouse reports in Chrome 139. Users will still be able to toggle back to the old audits for a limited period of time until Lighthouse 13.
## Documentation for the new insights audits
We'll be documenting the new audits on [developer.chrome.com](https://developer.chrome.com/) before the cutover date. The old documentation will be kept around for the foreseeable future so prior versions of Lighthouse can still link to them.
## Feedback
If you have any concerns or questions on this move, then we'd love to hear them on [this GitHub discussion](https://github.com/GoogleChrome/lighthouse/discussions/16462).
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-04-28 UTC.

