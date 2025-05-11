---
url: https://developer.chrome.com/blog/edge-to-edge?hl=en
title: https://developer.chrome.com/blog/edge-to-edge?hl=en
date: 2025-05-11T16:55:43.066550
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/edge-to-edge?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/edge-to-edge?hl=es-419)




  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  Prepare for Chrome on Android going edge-to-edge 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Bramus 
[ GitHub ](https://github.com/bramus) [ Mastodon ](https://front-end.social/@bramus) [ Bluesky ](https://bsky.app/profile/bram.us) [ Homepage ](https://www.bram.us/)
Published: Feb 28, 2025 
Edge-to-edge is [an Android feature](https://developer.android.com/develop/ui/views/layout/edge-to-edge) that lets applications span the entire width and height of the display by drawing behind the [Android system bars](https://developer.android.com/design/ui/mobile/guides/foundations/system-bars).
Before Chrome 135 Chrome on Android didn't draw edge-to-edge. However, from Chrome 135, Chrome on Android can draw web content up to the bottom device edge by extending the viewport into the gesture navigation bar area.
Visualizations of the viewport in Chrome that is not edge-to-edge and is edge-to-edge.
Chrome 135 on Android features a bottom bar called "the chin" that automatically goes out of the way as you scroll. This means that in most cases you won't need to do anything special when developing your site. However, in some cases content might get obstructed by the gesture navigation bar.
To ease the adoption of edge-to-edge we have prepared [a guide](https://developer.chrome.com/docs/css-ui/edge-to-edge) explaining the effect this change has on websites and what you can do to embrace this change.
[Chrome on Android edge-to-edge migration guide.](https://developer.chrome.com/docs/css-ui/edge-to-edge)
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-02-28 UTC.

