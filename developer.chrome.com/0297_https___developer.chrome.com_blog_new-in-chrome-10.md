---
url: https://developer.chrome.com/blog/new-in-chrome-109?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-109?hl=en
date: 2025-05-11T16:57:02.766283
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-109?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-chrome-109?hl=es-419)




  * On this page
  * [OPFS on Android](https://developer.chrome.com/blog/new-in-chrome-109?hl=en#opfs)
  * [MathML Core support.](https://developer.chrome.com/blog/new-in-chrome-109?hl=en#math-ml-core)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  New in Chrome 109 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [OPFS on Android](https://developer.chrome.com/blog/new-in-chrome-109?hl=en#opfs)
  * [MathML Core support.](https://developer.chrome.com/blog/new-in-chrome-109?hl=en#math-ml-core)


Adriana Jara 
[ GitHub ](https://github.com/tropicadri) [ LinkedIn ](https://www.linkedin.com/in/adrianajara) [ Mastodon ](https://hachyderm.io/@tropicadri)
Here's what you need to know:
  * The Origin Private File System API is [now available](https://developer.chrome.com/blog/new-in-chrome-109?hl=en#opfs) for Android.
  * There is a set of [new properties in CSS](https://developer.chrome.com/blog/new-in-chrome-109?hl=en#css-updates).
  * You can easily add math notations in your HTML with the [support for MathML Core](https://developer.chrome.com/blog/new-in-chrome-109?hl=en#math-ml-core).
  * And there’s plenty [more](https://developer.chrome.com/blog/new-in-chrome-109?hl=en#more).


I’m Adriana Jara. Let’s dive in and see what’s new for developers in Chrome 109.
## OPFS on Android
The Origin Private File System (OPFS) is part of the [File System Access API](https://developer.mozilla.org/docs/Web/API/File_System_Access_API), it is a storage endpoint private to the origin of the page.
It was launched on desktop on Chrome 102, Chrome 109 increases its compatibility by making it available on Android.
With a couple of exceptions, it includes all of the File System Access API surfaces, to seamlessly manage files directly from the local file system. The `show*Picker()` methods and the [Drag-and-Drop API integration](https://developer.chrome.com/articles/file-system-access#drag-and-drop-integration) are not available yet.
With the File System Access API on OPFS, sites can access their per-origin, private file system and are able to perform file operations via `FileSystemSyncAccessHandle` which provides improved performance.
Check out [this article](https://developer.chrome.com/articles/file-system-access) to learn how to implement smooth file system access across platforms.
## New in CSS.
Now a few new CSS features, starting with a new length unit: `lh`.
The `lh` CSS unit is equal to the computed value of the line-height property on the element on which it is used. This allows a `textarea` to be given a height that is the same as the number of lines of expected text.
Also the CSS Working Group added a new value of `auto` for the descriptors: `font-weight`, `font-style`, and `font-stretch` inside the `@font-face` rule. `auto` is now the initial value. These descriptors in [variable fonts](https://web.dev/articles/variable-fonts) provide users the ability to choose how heavy or slanted or wide the typeface should be.
To provide better control over web typography, the [`hyphenate-limit-chars`](https://developer.mozilla.org/docs/Web/CSS/hyphenate-limit-chars#:%7E:text=The%20hyphenate%2Dlimit%2Dchars%20CSS,control%20over%20hyphenation%20in%20text.) property specifies the minimum number of characters in a hyphenated word.
## MathML Core support.
If you ever tried to add math formulas to your web page in a styleable and accessible way you’ll be happy to hear that [MathML Core](https://www.w3.org/TR/mathml-core/) is now supported in Chrome.
MathML is a language for describing mathematical notation in a way that can be included in HTML and SVG. It is rendered in a CSS-compatible way with OpenType MATH and exposed via platform accessibility APIs.
MathML styling is enabled by CSS features including those dedicated to math layout. Some examples are the `math-depth`, `math-shift` and `math-style` properties, and the `math` value for the `display` property and more.
Check out [the documentation](https://developer.mozilla.org/docs/Web/MathML) for details and examples to up your mathematical notation game!
## And more!
Of course there’s plenty more.
  * You can use the property `suppressLocalAudioPlayback` in [`MediaTrackSupportedConstraints`](https://developer.mozilla.org/docs/Web/API/MediaTrackSupportedConstraints) to better control audio playback when using external speakers.
  * [Conditional Focus](https://developer.chrome.com/docs/web-platform/conditional-focus) is now available when calling `getDisplayMedia()`.
  * [Secure Payment Confirmation](https://developer.chrome.com/blog/spc-on-android) is available for Chrome on Android.


## Further reading
This covers only some key highlights. Check the links below for additional changes in Chrome 109.
  * [What's new in Chrome DevTools (109)](https://developer.chrome.com/blog/new-in-devtools-109)
  * [Chrome 109 deprecations and removals](https://developer.chrome.com/blog/chrome-109-beta#deprecations_and_removals)
  * [ChromeStatus.com updates for Chrome 109](https://www.chromestatus.com/features#milestone%3D109)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/108.0.5359.70..109.0.5414.91)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
I’m Adriana Jara, and as soon as Chrome 110 is released, I'll be right here to tell you what's new in Chrome!
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2023-01-10 UTC.

