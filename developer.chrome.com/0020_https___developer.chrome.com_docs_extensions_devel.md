---
url: https://developer.chrome.com/docs/extensions/develop/concepts/service-workers
title: https://developer.chrome.com/docs/extensions/develop/concepts/service-workers
date: 2025-05-11T16:51:45.021064
depth: 1
---

[ Skip to main content ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=es-419)






#  About extension service workers 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
This section explains what you need to know to use service workers in extensions. You should read this section whether you're familiar with service workers or not. Extension service workers are an extension's central event handler. That makes them just different enough from web service workers that the mountains of service worker articles around the web may or may not be useful.
Extension service workers have a few things in common with their web counterparts. An extension service worker is loaded when it is needed, and unloaded when it goes dormant. Once loaded, an extension service worker generally runs as long as it is actively receiving events, though it [can shut down](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers/lifecycle#idle-shutdown). Like its web counterpart, an extension service worker cannot access the DOM, though you can use it if needed with [offscreen documents](https://developer.chrome.com/docs/extensions/reference/api/offscreen).
Extension service workers are more than network proxies (as web service workers are often described). In addition to the [standard service worker events](https://developer.mozilla.org/docs/Web/API/ServiceWorkerGlobalScope#events), they also respond to extension events such as navigating to a new page, clicking a notification, or closing a tab. They're also registered and updated differently from web service workers.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2023-05-03 UTC.

