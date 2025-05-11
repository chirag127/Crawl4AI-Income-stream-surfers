---
url: https://developer.chrome.com/blog/loaf-has-shipped?hl=en
title: https://developer.chrome.com/blog/loaf-has-shipped?hl=en
date: 2025-05-11T16:56:47.735909
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/loaf-has-shipped?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/loaf-has-shipped?hl=es-419)




  * On this page
  * [LoAF is available in web-vitals JavaScript library](https://developer.chrome.com/blog/loaf-has-shipped?hl=en#web-vitals)
  * [LoAF is available in Web Vitals Extension](https://developer.chrome.com/blog/loaf-has-shipped?hl=en#web-vitals-extension)
  * [Updated guidance on using LoAF](https://developer.chrome.com/blog/loaf-has-shipped?hl=en#loaf-guidance)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  The Long Animation Frame API has now shipped 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [LoAF is available in web-vitals JavaScript library](https://developer.chrome.com/blog/loaf-has-shipped?hl=en#web-vitals)
  * [LoAF is available in Web Vitals Extension](https://developer.chrome.com/blog/loaf-has-shipped?hl=en#web-vitals-extension)
  * [Updated guidance on using LoAF](https://developer.chrome.com/blog/loaf-has-shipped?hl=en#loaf-guidance)


Barry Pollard 
[ GitHub ](https://github.com/tunetheweb) [ Mastodon ](https://webperf.social/@tunetheweb) [ Bluesky ](https://bsky.app/profile/tunetheweb.com) [ Homepage ](https://www.tunetheweb.com)
Browser Support
  * 123 
  * 123 


[Source](https://developer.mozilla.org/docs/Web/API/PerformanceLongAnimationFrameTiming)
The Long Animation Frame API (LoAF-pronounced Lo-Af) has shipped from Chrome 123 and we've now also updated our tooling and guidance to help you make the most of this new API.
## LoAF is available in `web-vitals` JavaScript library
Version 4 of [the web-vitals JavaScript library](https://github.com/GoogleChrome/web-vitals) includes the long animation frame (or frames) related to the INP interaction as documented in the _Find slow interactions in the field_ guide [to include information on how to take advantage of LoAF](https://web.dev/articles/find-slow-interactions-in-the-field#the_long_animation_frame_api_loaf).
At Google I/O 2024, we presented this information in the [New field insights for debugging INP](https://www.youtube.com/watch?v=xfjumh8ySRY) talk, including [leveraging LoAF](https://www.youtube.com/watch?v=xfjumh8ySRY&t=390s) to identify other scripts slowing down your INP interactions.
Integrating the API directly in the library allows RUM partners using this API to expose this data, including the likes of [RUMVision](https://www.rumvision.com/blog/long-animation-frames/), and [DebugBear](https://www.debugbear.com/blog/long-animation-frames). This also provides an open-source reference implementation for other RUM providers looking to add it to their own product.
## LoAF is available in Web Vitals Extension
The [Web Vitals Extension](https://chromewebstore.google.com/detail/web-vitals/ahfhijdlegdabablpippeagghigmibma) has been updated to include long animation frame data to help you debug INP interactions:
Web Vitals Extension console logging surfaces LoAF data.
This is useful to see what other scripts are running at the time of your interaction, which are often the cause of delays (particularly input delays) but until now were difficult to diagnose when using the extension.
## Updated guidance on using LoAF
We have also [updated our guidance in our main Long Animation Frames API documentation](https://developer.chrome.com/docs/web-platform/long-animation-frames#use-loaf) to help you make the most of this API.
A page may have many LoAFs, one of which is related to the INP interaction.
This guidance is based on how we have seen this API used in the field, for example [in this case study from Taboola](https://web.dev/case-studies/taboola-inp). We are working on a number of other case studies and look forward to publishing more examples like this in the future.
In addition we have also [documented the API on MDN](https://developer.mozilla.org/docs/Web/API/Performance_API/Long_animation_frame_timing).
## Conclusion
The Long Animation Frames API is an exciting addition to the web platform and we have already seen a number of sites using this API to improve their sites even during its trial phase. We look forward to a wider adoption of the API in tooling and improved responsiveness on websites thanks to this API.
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-06-24 UTC.

