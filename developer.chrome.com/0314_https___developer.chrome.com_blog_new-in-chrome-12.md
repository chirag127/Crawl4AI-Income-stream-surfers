---
url: https://developer.chrome.com/blog/new-in-chrome-128?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-128?hl=en
date: 2025-05-11T16:57:27.070907
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-128?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-chrome-128?hl=es-419)




  * On this page
  * [Line breakable <ruby>](https://developer.chrome.com/blog/new-in-chrome-128?hl=en#ruby-line-breaks)
  * [PointerEvent.deviceProperties for multi-pen inking](https://developer.chrome.com/blog/new-in-chrome-128?hl=en#multi-pen-pointer)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  New in Chrome 128 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Line breakable <ruby>](https://developer.chrome.com/blog/new-in-chrome-128?hl=en#ruby-line-breaks)
  * [PointerEvent.deviceProperties for multi-pen inking](https://developer.chrome.com/blog/new-in-chrome-128?hl=en#multi-pen-pointer)


Adriana Jara 
[ GitHub ](https://github.com/tropicadri) [ LinkedIn ](https://www.linkedin.com/in/adrianajara) [ Mastodon ](https://hachyderm.io/@tropicadri)
Here's what you need to know:
  * Displaying `<ruby>` elements is better with [line breaks](https://developer.chrome.com/blog/new-in-chrome-128?hl=en#ruby-line-breaks).
  * [Promise.try](https://developer.chrome.com/blog/new-in-chrome-128?hl=en#promise-try) makes it easier to chain Promises.
  * PointerEvent is extended to uniquely identify [multiple pens](https://developer.chrome.com/blog/new-in-chrome-128?hl=en#multi-pen-pointer).
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-128?hl=en#more).


I'm Adriana Jara. Let's dive in and see what's new for developers in Chrome 128.
## Line breakable `<ruby>`
The `<ruby>` element enhances text presentation, especially for East Asian languages. It lets you display phonetic annotations or other supplemental information above or beside base text.
A ruby element consists of two main parts, ruby base which is the main text and ruby text which is the annotation text, marked up with the element.
Previously if a ruby-base or a ruby-text was longer than a whole line, they were wrapped individually creating layout challenges.
Now line-breakable ruby, places wrapped ruby annotation text over wrapped base text achieving ideal text rendering.
Visit [Line-breakable `<ruby>` and CSS ruby-align property](https://developer.chrome.com/blog/line-breakable-ruby) for examples and more information.
## Promise.try
`Promise.try` makes it easier to handle errors with Promises. There's a pattern where you have a function, `f`. This function may be async, and return a Promise, or it may not. To use Promise semantics to handle errors in both cases, you wrap the function in a Promise.
One way to achieve this is with `Promise.resolve().then(f)`, but in this case `f` would be run needlessly asynchronously on the next tick.
To avoid this problem you need to use `new Promise(resolve => resolve(f()))` which is not ergonomic at all.
`Promise.try`, is the simple, straightforward way to accomplish the same. It lets you start a Promise chain that catches all errors in `.catch` handlers instead of having to handle both synchronous and asynchronous exception flows.
To learn more check out the [`Promise.try` documentation](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise/try).
## PointerEvent.deviceProperties for multi-pen inking
Developers didn't have a way to distinguish between two individual pens on an ink-enabled digitizer. The existing [PointerEvent.pointerId](https://developer.mozilla.org/docs/Web/API/PointerEvent/pointerId) attribute is implemented in different ways and does not always persist for each ink stroke or interaction with the screen.
The `PointerEvent` interface is now extended to include a new attribute: `deviceProperties`. It contains the attribute `uniqueId`, that represents a session-persistent, document isolated, unique identifier that a developer can reliably use to identify individual pens interacting with the page.
With this change you can, for example, set specific colors or pen shapes for each device interacting with the digitizer.
Read about getting started with pointer events in [Pointing the way forward](https://developer.chrome.com/blog/pointer-events).
## And more!
Of course there's plenty more.
  * The CSS [`zoom`](https://developer.mozilla.org/docs/Web/CSS/zoom) property is now aligned with the latest standard.
  * [`AudioContext`](https://developer.mozilla.org/docs/Web/API/AudioContext) creation and audio rendering errors are now reported through `AudioContext.onerror`.
  * The [DevTools](https://developer.chrome.com/blog/new-in-devtools-128) Animations panel now captures animations and you can edit `@keyframes` live.


[Read the full release notes](https://developer.chrome.com/release-notes/128).
## Further reading
This covers only some key highlights. Check the following links for additional changes in Chrome 128.
  * [What's new in Chrome DevTools (128)](https://developer.chrome.com/blog/new-in-devtools-128)
  * [ChromeStatus.com updates for Chrome 128](https://chromestatus.com/features#milestone%3D128)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/127.0.6533.133..128.0.6613.62)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
Yo soy Adriana Jara, and as soon as Chrome 128 is released, I'll be right here to tell you what's new in Chrome!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-08-20 UTC.

