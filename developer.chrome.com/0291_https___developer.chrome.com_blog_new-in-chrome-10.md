---
url: https://developer.chrome.com/blog/new-in-chrome-101?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-101?hl=en
date: 2025-05-11T16:56:57.082274
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-101?hl=en#main-content)
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


#  New in Chrome 101 
Stay organized with collections  Save and categorize content based on your preferences. 
Rachel Andrew 
[ GitHub ](https://github.com/rachelandrew) [ LinkedIn ](https://www.linkedin.com/in/rachelandrew) [ Mastodon ](https://front-end.social/@rachelandrew) [ Bluesky ](https://bsky.app/profile/rachelandrew.bsky.social) [ Homepage ](https://rachelandrew.co.uk)
Here's what you need to know:
  * [The `hwb()` color notation](https://developer.chrome.com/blog/new-in-chrome-101?hl=en#hwb) gives you a new way to specify color according to hue, whiteness, and blackness.
  * [Fetch Priority](https://developer.chrome.com/blog/new-in-chrome-101?hl=en#priority-hints) give you a way to hint to the browser in which order resources should be downloaded.
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-101?hl=en#also_in_this_release).


Let's take a look at what's available in Chrome 101.
## `hwb()` color notation
Described [in an article by Stefan Judis](https://www.stefanjudis.com/blog/hwb-a-color-notation-for-humans/) as a "color notation for humans", [`hwb()`](https://developer.mozilla.org/docs/Web/CSS/color_value/hwb) specifies color according to hue, whiteness, and blackness. As with other color notations, an optional alpha component specifies opacity.
```
h1{
color:hwb(1940%0%/.5)/* #00c3ff with 50% opacity */
}

```

This method of specifying color is now well-supported, with Firefox supporting it from version 96, and Safari from version 15.
## Fetch Priority
Fetch Priority gives you a way to hint to the browser which order resources should be downloaded in, by using the `fetchpriority` attribute. This accepts values of `"high"`, `"low"`, and `"auto"`.
  * `"high"`: You consider the resource a high priority and want the browser to prioritize it as long as the browser's heuristics don't prevent that from happening.
  * `"low"`: You consider the resource a low priority and want the browser to deprioritize it if its heuristics permit.
  * `"auto"`: This is the default value that lets the browser decide the appropriate priority.


In the example below, a low priority image is indicated with `fetchpriority="low"`.
```
<img src="/images/in_viewport_but_not_important.svg" fetchpriority="low" alt="I'm an unimportant image!">

```

Read more about the various use cases in [Optimize resource loading with the Fetch Priority API](https://web.dev/articles/fetch-priority).
### Also in this release
There is a new method of [`forget()`](https://web.dev/articles/usb#revoke_access) for [`USBDevice`](https://developer.mozilla.org/docs/Web/API/USBDevice) objects. This enables the forgetting of a device that previously had permission granted. For example, if this is an application used on a shared computer with many devices.
Also for Web USB, a fix to support [`SameObject`] for related attributes within `USBDevice`. The specification change can be found [in a PR to the draft spec](https://github.com/WICG/webusb/pull/212).
Dedicated workers loaded from a secure (HTTPS) origin, yet instantiated by insecure (non-HTTPS) contexts, are no longer considered secure. This means that inside such worker contexts: - `self.isSecureContext` is now `false`. - `self.caches` and `self.storageFoundation` are no longer available.
The [`popup`](https://developer.mozilla.org/docs/Web/API/Window/open#popup) argument for `window.open()` now evaluates to `true`, following a recent change to the spec for parsing this argument. Previously, when `popup` was set equal to true, `window.open()` was interpreted to mean `false`. This change makes boolean features easier to use and understand.
## Further reading
This covers only some key highlights. Check the links below for additional changes to Chrome 101.
  * [What's new in Chrome DevTools (101)](https://developer.chrome.com/blog/new-in-devtools-101)
  * [Chrome 101 deprecations and removals](https://developer.chrome.com/blog/deps-rems-101)
  * [ChromeStatus.com updates for Chrome 101](https://www.chromestatus.com/features#milestone%3D101)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/refs/tags/101.0.4951.49)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2022-05-03 UTC.

