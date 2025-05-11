---
url: https://developer.chrome.com/blog/new-in-chrome-134?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-134?hl=en
date: 2025-05-11T16:57:33.473008
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-134?hl=en#main-content)
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


#  New in Chrome 134 
Stay organized with collections  Save and categorize content based on your preferences. 
Rachel Andrew 
[ GitHub ](https://github.com/rachelandrew) [ LinkedIn ](https://www.linkedin.com/in/rachelandrew) [ Mastodon ](https://front-end.social/@rachelandrew) [ Bluesky ](https://bsky.app/profile/rachelandrew.bsky.social) [ Homepage ](https://rachelandrew.co.uk)
Published: March 4, 2025 
Here's what you need to know:
  * [The light-dismiss behavior from popover comes to `<dialog>`](https://developer.chrome.com/blog/new-in-chrome-134?hl=en#dialog).
  * [The Web Locks API is now supported in shared storage](https://developer.chrome.com/blog/new-in-chrome-134?hl=en#weblocks).
  * [The `imageSmoothingQuality` attribute is now supported on paint canvas ](https://developer.chrome.com/blog/new-in-chrome-134?hl=en#paintcanvas).
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-134?hl=en#more).


## The light-dismiss behavior from popover comes to `<dialog>`
One of the nice features of the Popover API is its light dismiss behavior. This behavior is now part of `<dialog>`, with a new `closedby` attribute controlling the behavior:
  * `<dialog closedby="none">`: No user-triggered closing of dialogs at all.
  * `<dialog closedby="closerequest">`: Pressing `ESC` (or other close trigger) closes the dialog
  * `<dialog closedby="any">`: Clicking outside the dialog, or pressing `ESC`, closes the dialog. Akin to `popover="auto"` behavior.


## The Web Locks API is now supported in shared storage
Integrates the Web Locks API into Shared Storage. This prevents scenarios such as where cross-site reach measurement can result in duplicate reporting, due to the potential race conditions within the `get()` and `set()` logic.
This change:
  * Introduces `navigator.locks.request` to the worklet environment.
  * Introduces `{ withLock: <resource>}` option to all modifier methods.
  * Introduces a batch modify method: `sharedStorage.batchUpdate(methods,options)`. This method, with the `withLock` option, allows multiple modifier methods to be executed atomically, enabling use cases where a website needs to maintain consistency while updating data organized across multiple keys.


## The `imageSmoothingQuality` attribute is now supported on paint canvas
Add support for the `imageSmoothingQuality` attribute on paint canvas. This lets you choose the quality or performance tradeoff when scaling images. There are three options in total for `imageSmoothingQuality`: `low`, `medium` and `high`.
## And more!
Of course there's plenty more.
  * Chrome makes it easier to move between the browser and installed web apps with user Link capturing on PWAs.
  * You can now customize `<select>` menus with images and more.


See the full [Chrome 134 release notes](https://developer.chrome.com/release-notes/134) for details of these and many other features that are New in Chrome!
## Further reading
This covers only some key highlights. Check the following links for additional changes in Chrome 134.
  * [Release notes for Chrome 134](https://developer.chrome.com/release-notes/134).
  * [What's new in Chrome DevTools (134)](https://developer.chrome.com/blog/new-in-devtools-134).
  * [ChromeStatus.com updates for Chrome 133](https://chromestatus.com/features#milestone%3D134).
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule).


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
As soon as Chrome 134 is released, we'll be right here to tell you what's new in Chrome!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-03-04 UTC.

