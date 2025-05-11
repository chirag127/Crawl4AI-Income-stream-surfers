---
url: https://developer.chrome.com/blog/new-in-chrome-122?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-122?hl=en
date: 2025-05-11T16:57:19.236285
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-122?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-chrome-122?hl=es-419)

Sign in


  * On this page
  * [Storage Buckets API.](https://developer.chrome.com/blog/new-in-chrome-122?hl=en#storage-buckets-api)
  * [DevTools improvements in the Performance Panel](https://developer.chrome.com/blog/new-in-chrome-122?hl=en#performance-panel-improvements)
  * [Async Clipboard API unsanitized option](https://developer.chrome.com/blog/new-in-chrome-122?hl=en#read-unsanitized-html)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  New in Chrome 122 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Storage Buckets API.](https://developer.chrome.com/blog/new-in-chrome-122?hl=en#storage-buckets-api)
  * [DevTools improvements in the Performance Panel](https://developer.chrome.com/blog/new-in-chrome-122?hl=en#performance-panel-improvements)
  * [Async Clipboard API unsanitized option](https://developer.chrome.com/blog/new-in-chrome-122?hl=en#read-unsanitized-html)


Adriana Jara 
[ GitHub ](https://github.com/tropicadri) [ LinkedIn ](https://www.linkedin.com/in/adrianajara) [ Mastodon ](https://hachyderm.io/@tropicadri)
Here's what you need to know:
  * Improve storage management with the [Storage Buckets API](https://developer.chrome.com/blog/new-in-chrome-122?hl=en#storage-buckets-api).
  * There are DevTools [improvements in the Performance Panel](https://developer.chrome.com/blog/new-in-chrome-122?hl=en#performance-panel-improvements).
  * Choose to preserve accuracy when copying and pasting HTML using the new Async Clipboard API [`unsanitized` option](https://developer.chrome.com/blog/new-in-chrome-122/read-unsanitized-html).
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-122?hl=en#more).


I'm Adriana Jara. Let's dive in and see what's new for developers in Chrome 122.
## Storage Buckets API.
The [Storage Buckets API](https://wicg.github.io/storage-buckets/explainer) provides more granularity to better manage persistent storage.
Traditionally, as the user runs out of storage space on their device, the data stored with APIs like IndexedDB or `localStorage` gets lost without the user being able to intervene. One way to make storage persistent is using the [`persist()`](https://developer.mozilla.org/docs/Web/API/StorageManager/persist) method of the StorageManager interface. However, this method of requesting for storage to be persistent is all or nothing
The core idea of the Storage Buckets API is granting sites the ability to create multiple storage buckets, where the browser may choose to delete each bucket independently of other buckets. So you can specify eviction prioritization to make sure the most valuable data isn't deleted.Each storage bucket can contain data associated with established storage APIs such as IndexedDB and CacheStorage.
Visit [not all storage is created equal: introducing Storage Buckets](https://developer.chrome.com/docs/web-platform/storage-buckets) for more details and code samples to start using Storage Buckets.
## DevTools improvements in the Performance Panel
In Chrome 122 DevTools include the following improvements in the **Performance** panel.
First, the **Timeline** at the top of the **Performance** panel now lets you set breadcrumbs and jump between them. To set a breadcrumb, select a range on the **Timeline** , hover over it, and click the corresponding **N ms** zoom_in button. You can create several nested breadcrumbs in succession. To jump between zoom levels, click the corresponding breadcrumb in the chain on top of the **Timeline**. Watch the next video to see breadcrumbs in action.
Also, there are now event initiators in the **Main** track. The **Performance** > **Main** track by default shows arrows connecting initiators and the following events they caused.
  * Style or layout invalidation -> **Recalculate styles** or **Layout**
  * **Request Animation Frame** -> **Animation Frame Fired**
  * **Request Idle Callback** -> **Fire Idle Callback**
  * **Install Timer** -> **Timer Fired**
  * **Create WebSocket** -> **Send...** and **Receive WebSocket Handshake** or **Destroy WebSocket**


To see the arrows, find such an event in the trace and click it.
Find more DevTools updates in [What's new in Devtools 122](https://developer.chrome.com/blog/new-in-devtools-122).
## Async Clipboard API `unsanitized` option
When copying and pasting using the Async Clipboard API the [`unsanitized`](https://developer.mozilla.org/docs/Web/API/Clipboard/read#unsanitized) option for the `read()` method allows apps and websites to get unsanitized HTML. Unless sites include this property, reading HTML from the clipboard will be sanitized.
By default, when reading `text/html` MIME types using the async API, the sanitizer is invoked to strip out contents from the HTML markup due to security concerns, and styles are inlined in the resulting HTML. This leads to a large HTML payload and loss of fidelity of HTML content when read by web developers or mobile apps.
You can see the difference in the output in the following example.
Input:
```
<style>p { color: blue; }</style><p>Hello, World!</p>'

```

Sanitized (default):
```
<p style='color: blue; font-size: medium; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'>Hello, World!</p>

```

With `unsanitized` option:
```
<html><head><style>p { color: blue; }</style></head><body><p>Hello, World!</p></body></html>

```

Visit [Unblocking clipboard access](https://web.dev/articles/async-clipboard) to learn the basics of the Clipboard API.
## And more!
Of course there's plenty more.
  * In CSS, container queries with unsupported features never match. For example, the following query will never match due to the unknown feature:

```
@container(width0px)or(unknown){}

```

  * [dataTransfer.clearData()](https://developer.mozilla.org/docs/Web/API/DataTransfer/clearData) does not affect File objects, it only deletes text type objects.
  * With WebGL's [`drawingBufferStorage`](https://developer.chrome.com/blog/chrome-122-beta#webgl_drawingbufferstorage) you can avoid an extra copy when converting rendering to the default drawing buffer pixel format and draw content that has more than 8 bits of precision.


## Further reading
This covers only some key highlights. Check the following links for additional changes in Chrome 122.
  * [What's new in Chrome DevTools (122)](https://developer.chrome.com/blog/new-in-devtools-122)
  * [Chrome 122 deprecations and removals](https://developer.chrome.com/blog/deps-rems-122)
  * [ChromeStatus.com updates for Chrome 122](https://chromestatus.com/features#milestone%3D122)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/121.0.6167.205..122.0.6261.52)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
Yo soy Adriana Jara, and as soon as Chrome 123 is released, I'll be right here to tell you what's new in Chrome!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-02-20 UTC.

