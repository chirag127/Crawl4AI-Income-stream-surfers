---
url: https://developer.chrome.com/blog/new-in-chrome-125?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-125?hl=en
date: 2025-05-11T16:57:27.078243
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-125?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-chrome-125?hl=es-419)

Sign in


  * On this page
  * [CSS Anchor Positioning.](https://developer.chrome.com/blog/new-in-chrome-125?hl=en#anchor-positioning)
  * [Compute Pressure API.](https://developer.chrome.com/blog/new-in-chrome-125?hl=en#compute-pressure-api)
  * [Storage Access API (SAA) extended to non-cookie storage.](https://developer.chrome.com/blog/new-in-chrome-125?hl=en#storage-access-api)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  New in Chrome 125 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [CSS Anchor Positioning.](https://developer.chrome.com/blog/new-in-chrome-125?hl=en#anchor-positioning)
  * [Compute Pressure API.](https://developer.chrome.com/blog/new-in-chrome-125?hl=en#compute-pressure-api)
  * [Storage Access API (SAA) extended to non-cookie storage.](https://developer.chrome.com/blog/new-in-chrome-125?hl=en#storage-access-api)


Adriana Jara 
[ GitHub ](https://github.com/tropicadri) [ LinkedIn ](https://www.linkedin.com/in/adrianajara) [ Mastodon ](https://hachyderm.io/@tropicadri)
Here's what you need to know:
  * Anchoring elements is easier than ever with [CSS Anchor Positioning](https://developer.chrome.com/blog/new-in-chrome-125?hl=en#anchor-positioning).
  * The [Compute Pressure API](https://developer.chrome.com/blog/new-in-chrome-125?hl=en#compute-pressure-api) helps to optimize the available computer power.
  * [Storage Access API](https://developer.chrome.com/blog/new-in-chrome-125?hl=en#storage-access-api) is expanded for more than cookie storage.
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-125?hl=en#more).


I'm Adriana Jara. Let's dive in and see what's new for developers in Chrome 125.
## CSS Anchor Positioning.
Displaying an element anchored to another element lets you create UI patterns like using a popover as a tooltip and attaching it to the element that invokes it.
With [CSS Anchor Positioning](https://developer.chrome.com/blog/anchor-positioning-api) you can tether an absolutely positioned element to one or more elements on the page in a declarative way. It doesn't require JavaScript and works performantly when the anchors are scrollable.
The anchor positioning feature consists of a large number of CSS properties. A few of the key properties are as follows:
  * `anchor-name`: Sets up an element to be an anchor for other elements.
  * `position-anchor`: Describes the "default" anchor that an anchored element should use for anchor positioning.
  * The `anchor()` function: Refers to the position of the anchor element, in positioning the anchored element.
  * `inset-area`: A shorthand for positioning, for common relative positions.


## Compute Pressure API.
The Compute Pressure API offers high-level states that represent the CPU load on the system.
When optimizing for a balanced use of computer power the API uses the right underlying hardware metrics to ensure that users can take advantage of all the processing power available as long as the system is not under unmanageable stress.
Intel led the design and implementation work for this API, which will let video conferencing apps dynamically balance features and performance.
Visit [Compute Pressure API](https://developer.chrome.com/docs/web-platform/compute-pressure) for samples and more information.
## Storage Access API (SAA) extended to non-cookie storage.
The [Storage Access API](https://developer.mozilla.org/docs/Web/API/Storage_Access_API) is a JavaScript API that was created as an alternative to cross site cookies, for embeds that depend on loading cross-site resources, to request access permission from the user, on an as-needed basis.
This version includes an extension to use the API beyond cookies. With the extension you can access unpartitioned cookies and non-cookie storage in a third-party context, for example for indexedDB and localstorage. The following code shows an example to request access to indexedDB.
```
// Request a new storage handle via rSA (this may prompt the user)
lethandle=awaitdocument.requestStorageAccess({indexedDB:true});
// Open or create an indexedDB that is shared with the 1P context
letmessageDB=handle.indexedDB.open("messages");

```

## And more!
Of course there's plenty more.
  * There's an [origin trial](https://developer.chrome.com/origintrials#/view_trial/4188910603407982593) for the [Device Posture API and the Viewport Segments Enumeration API](https://developer.chrome.com/blog/foldable-apis-ot). These APIs are designed to help developers target foldable devices.
  * The CSS stepped-value functions [`round()`](https://developer.mozilla.org/docs/Web/CSS/round), [`mod()`](https://developer.mozilla.org/docs/Web/CSS/mod), and [`rem()`](https://developer.mozilla.org/docs/Web/CSS/rem) have been added, making these features Baseline Newly Available
  * The [Shared Storage API](https://developer.mozilla.org/docs/Web/API/Shared_Storage_API) now supports running cross origin worklets without having to create an iframe.


[Read the full release notes](https://developer.chrome.com/release-notes/125).
## Further reading
This covers only some key highlights. Check the following links for additional changes in Chrome 125.
  * [What's new in Chrome DevTools (125)](https://developer.chrome.com/blog/new-in-devtools-125)
  * [ChromeStatus.com updates for Chrome 125](https://chromestatus.com/features#milestone%3D125)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/124.0.6367.178..125.0.6422.44)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
Yo soy Adriana Jara, and as soon as Chrome 126 is released, I'll be right here to tell you what's new in Chrome!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-05-14 UTC.

