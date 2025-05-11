---
url: https://developer.chrome.com/blog/new-in-chrome-108?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-108?hl=en
date: 2025-05-11T16:57:01.046296
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-108?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-chrome-108?hl=es-419)




  * On this page
  * [New viewport size units](https://developer.chrome.com/blog/new-in-chrome-108?hl=en#viewport-units)
  * [Variable fonts now supported in COLRv1.](https://developer.chrome.com/blog/new-in-chrome-108?hl=en#colrv1-support)
  * [FileSystemSyncAccessHandle methods are now synchronous.](https://developer.chrome.com/blog/new-in-chrome-108?hl=en#sync-filehandle)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  New in Chrome 108 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [New viewport size units](https://developer.chrome.com/blog/new-in-chrome-108?hl=en#viewport-units)
  * [Variable fonts now supported in COLRv1.](https://developer.chrome.com/blog/new-in-chrome-108?hl=en#colrv1-support)
  * [FileSystemSyncAccessHandle methods are now synchronous.](https://developer.chrome.com/blog/new-in-chrome-108?hl=en#sync-filehandle)


Adriana Jara 
[ GitHub ](https://github.com/tropicadri) [ LinkedIn ](https://www.linkedin.com/in/adrianajara) [ Mastodon ](https://hachyderm.io/@tropicadri)
Here's what you need to know:
  * It is easier to create adaptive UIs with new [viewport size units](https://developer.chrome.com/blog/new-in-chrome-108?hl=en#viewport-units).
  * Color vector fonts now include support for [variable fonts](https://developer.chrome.com/blog/new-in-chrome-108?hl=en#colrv1-support).
  * The methods in the interface `FileSystemSyncAccessHandle`, part of the File System Access API, are now [synchronous](https://developer.chrome.com/blog/new-in-chrome-108?hl=en#sync-filehandle).
  * And there’s plenty [more](https://developer.chrome.com/blog/new-in-chrome-108?hl=en#more)


I’m Adriana Jara. Let’s dive in and see what’s new for developers in Chrome 108.
## New viewport size units
The new viewport units give you more control to create adaptive UIs.
These units measure the viewport area differently, as they take into account UI elements in the browser that can be expanded or collapsed. For example, the address bar.
The `large` units provide the viewport size assuming that those user agent interfaces are collapsed.
On the other hand the `small` units provide viewport size assuming the interfaces are expanded.
And with `dynamic` units the viewport size will automatically adjust itself in response to browser interface elements being shown or not.
The value will be anything within the limits of the large unit (the maximum) and small units (the minimum).
Check out [this article](https://web.dev/blog/viewport-units) for more details. Also checkout the change on [Android viewport resizing behavior](https://developer.chrome.com/blog/viewport-resize-behavior) to handle your viewport appropriately .
## Variable fonts now supported in COLRv1.
[COLRv1 color vector fonts](https://developer.chrome.com/blog/colrv1-fonts) have been supported since Chrome 98, but the initial release supported only static functionality of the COLRv1 table.
But COLRv1 specification also includes OpenType Variations, which means allowing changes to font properties by changing variable axis values. Such variations are supported now.
This release also includes the `font-tech()` and `font-format()` condition extensions to CSS `@supports` .
With these conditions the developer can detect when the font features are available to give the user the latest experience and also create a fallback if the support is not available.
Play with the demo [here](https://roettsch.es/var_colrv1.html) and add impact to your words with variable fonts.
## FileSystemSyncAccessHandle methods are now synchronous.
The origin private file system provides access to a special kind of file that is highly optimized for performance, developers can get access to such files by calling `createSyncAccessHandle()`, which is a method exposed on `FileSystemFileHandle` objects.
This call results in a `FileSystemSyncAccessHandle`.
The methods `truncate(newSize)`, `getSize()`, `flush()`, and `close()` in that access handle, used to be asynchronous, but they are synchronous as of Chrome 108.
There is a good reason for the change, it makes `FileSystemSyncAccessHandle` match the synchronous, POSIX-like file API that Wasm-based applications expect; making the API more ergonomic while bringing substantial performance gains.
This is a potentially breaking change, if you are using the methods above, any use of `Promise.then()` will break. If you chain a `then()` call on the result of any of the previously asynchronous and now synchronous methods, you need to change your code.
```
// ⛔️ This will break, and you need to restructure your code:
accessHandle.flush().then(/* Follow-up code */);
// ✅ Correct:
accessHandle.flush();
/* Follow-up code */

```

For more detailed instructions visit this [article](https://developer.chrome.com/blog/sync-methods-for-accesshandles)
## And more!
Of course there’s plenty more.
  * A change [in the behavior for `overflow`](https://developer.chrome.com/blog/overflow-replaced-elements) on replaced elements is being rolled out.
  * If you are an identity provider check out the [Federated Credential Management API](https://developer.chrome.com/docs/privacy-sandbox/fedcm).
  * The [Media Source Extensions API](https://web.dev/articles/media-mse-basics) is now available in the worker context.


## Further reading
This covers only some key highlights. Check the links below for additional changes in Chrome 108.
  * [What's new in Chrome DevTools (108)](https://developer.chrome.com/blog/new-in-devtools-108)
  * [Chrome 108 deprecations and removals](https://developer.chrome.com/blog/deps-rems-108)
  * [ChromeStatus.com updates for Chrome 108](https://www.chromestatus.com/features#milestone%3D108)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/107.0.5304.124..108.0.5359.70)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
I’m Adriana Jara, and as soon as Chrome 109 is released, I'll be right here to tell you what's new in Chrome!
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2022-11-29 UTC.

