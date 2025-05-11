---
url: https://developer.chrome.com/blog/freezing-on-energy-saver?hl=en
title: https://developer.chrome.com/blog/freezing-on-energy-saver?hl=en
date: 2025-05-11T16:56:06.360914
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/freezing-on-energy-saver?hl=en#main-content)
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


#  Freezing on Energy Saver 
Stay organized with collections  Save and categorize content based on your preferences. 
François Doray 
Published: January 20, 2025 
From Chrome 133 (February 2025), eligible CPU-intensive background tabs will be frozen when Energy Saver mode is active. This aims to reduce battery consumption for users who rely on Energy Saver and for whom every percentage point of battery life counts. To minimize disruption, only background tabs that meet specific criteria and exhibit high CPU usage will be frozen.
## What is freezing?
Freezing suspends task execution on a web page. This includes:
  * Event handlers (for example, input, network, and sensor)
  * Timers
  * Promise resolvers


Freezing is different from discarding, where a tab is unloaded from memory. When a frozen tab is brought back into focus, it's automatically unfrozen, and any queued tasks are executed without loss of state.
The freeze and resume events are dispatched when a page is frozen or resumed (see the [Page Lifecycle API documentation](https://developer.chrome.com/docs/web-platform/page-lifecycle-api)). These events allow the page to release unused resources, notify a server that the page is paused, or record metrics.
## What pages can be frozen?
Freezing will operate on _[browsing context groups](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-group)_. Typically, a browsing context group consists of a single tab. However, multiple tabs can belong to the same group when using APIs like `window.open()`.
With Energy Saver enabled, a browsing context group will be frozen if it meets the following conditions:
  * All pages within the group have been hidden and silent for more than five minutes.
  * Any subgroup of same-origin frames within the group is "CPU-intensive."
  * The group does **not** : 
    * Provide audio or video conferencing functionality (detected using microphone, camera, screen/window/tab capture, or an RTCPeerConnection with an 'open' RTCDataChannel or a 'live' MediaStreamTrack).
    * Control an external device (detected using Web USB, Web Bluetooth, Web HID, or Web Serial).
    * Hold a Web Lock or an IndexedDB connection that blocks operations outside the group.


The definition of "CPU-intensive" may evolve, but the intention is to exclude efficiently implemented email or chat clients, or calendar applications that generate notifications.
Freezing simultaneously all tabs within the same browsing context group minimizes disruption for apps that use popups, such as those for composing messages or entering credentials.
## How can I prepare my site?
If your site doesn't have background functionality (for example notifications, file uploads, or content refresh), it likely won't be affected by freezing.
If your site does have background functionality, minimize its CPU usage in the background to avoid being considered CPU-intensive and thus frozen. Here are some tips:
  * Avoid timers for periodic state change checks. 
    * Use [IntersectionObserver](https://developer.mozilla.org/docs/Web/API/Intersection_Observer_API) to detect when an element enters the viewport.
    * Use [ResizeObserver](https://web.dev/articles/resize-observer) to detect element size changes.
    * Use [MutationObserver](https://developer.mozilla.org/docs/Web/API/MutationObserver) or [custom element lifecycle callbacks](https://developer.mozilla.org/docs/Web/Web_Components/Using_custom_elements) for DOM changes.
  * Consider [web sockets](https://developer.mozilla.org/docs/Web/API/WebSockets_API), [server-sent events](https://developer.mozilla.org/docs/Web/API/EventSource), [push messages](https://developer.mozilla.org/docs/Web/API/Push_API), or [fetch streams](https://web.dev/articles/fetch-upload-streaming#previously_on_the_exciting_adventures_of_fetch_streams) instead of a polling server.
  * [Use events like timeupdate and ended](https://html.spec.whatwg.org/multipage/media.html#mediaevents) for audio or video changes.


We also recommend migrating background functionality to a service worker so that it's not affected by freezing. In addition to not being affected by freezing, a service worker requires less browser resources. Consider using:
  * [Push API for notifications](https://web.dev/articles/push-notifications-overview)
  * [Background Synchronization API](https://developer.mozilla.org/docs/Web/API/Background_Synchronization_API) or [Web Periodic Background Synchronization API](https://web.dev/patterns/web-apps/periodic-background-sync) for fetching updates.


Sites can opt out of freezing by participating in the [BackgroundPageFreezeOptOut origin trial](https://developer.chrome.com/origintrials#/view_trial/4254212798004854785). This trial will be discontinued once new APIs for declaring important background work are released (for example the [Progress Notification API](https://github.com/explainers-by-googlers/progress-notification)).
You can check a tab's eligibility for freezing at `chrome://discards`. Note that even if a tab is eligible for freezing, Chrome 133 will only freeze it if it's CPU-intensive and Energy Saver is active.
## What's next?
Background tab freezing conserves power, which is crucial for users with Energy Saver enabled.
It also improves foreground tab performance and helps avoid background tab termination, especially on resource-constrained devices, by reducing CPU usage and memory access. Chrome will therefore expand tab freezing to more situations (changes will be announced on [blink-dev@chromium.org](https://groups.google.com/a/chromium.org/g/blink-dev)). To do this with minimal disruption to background use cases, new APIs like the [Progress Notification API](https://github.com/explainers-by-googlers/progress-notification) will allow pages to declare important background work and prevent freezing.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-01-20 UTC.

