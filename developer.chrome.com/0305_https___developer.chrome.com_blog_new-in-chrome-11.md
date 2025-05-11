---
url: https://developer.chrome.com/blog/new-in-chrome-119?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-119?hl=en
date: 2025-05-11T16:57:17.069138
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-119?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-chrome-119?hl=es-419)




  * On this page
  * [Cookies expiration date.](https://developer.chrome.com/blog/new-in-chrome-119?hl=en#cookies-expiration)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  New in Chrome 119 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Cookies expiration date.](https://developer.chrome.com/blog/new-in-chrome-119?hl=en#cookies-expiration)


Adriana Jara 
[ GitHub ](https://github.com/tropicadri) [ LinkedIn ](https://www.linkedin.com/in/adrianajara) [ Mastodon ](https://hachyderm.io/@tropicadri)
Here's what you need to know:
  * There’s an [update to the expiration date](https://developer.chrome.com/blog/new-in-chrome-119?hl=en#cookies-expiration) upper limit for cookies already in storage.
  * [CSS has new pseudo-classes](https://developer.chrome.com/blog/new-in-chrome-119?hl=en#css-updates), relative color syntax and more.
  * [Fenced Frames added improvements](https://developer.chrome.com/blog/new-in-chrome-119?hl=en#fenced-frames-improvements) like ad size macros and others.
  * And there’s plenty [more](https://developer.chrome.com/blog/new-in-chrome-119?hl=en#more).


I’m Adriana Jara. Let’s dive in and see what’s new for developers in Chrome 119.
## Cookies expiration date.
Since Chrome 104 newly created cookies or those updated with an expiration date have had that date capped at no more than 400 days in the future. This same limit will now be retroactively applied to cookies already in storage.
The expiration dates of these cookies will be capped at no more than 400 days after the first time Chrome 119+ starts up and does a one time database migration. The impact of this change will not be felt by users until at least 400 days after Chrome 119 is released, and then only for existing cookies that have not been updated in that period.
You can read more about [the expiration date recommendation](https://httpwg.org/http-extensions/draft-ietf-httpbis-rfc6265bis.html#name-the-expires-attribute) and here is a friendly reminder that third party cookies will be deprecated [in the near future](https://privacysandbox.com/news/the-next-stages-of-privacy-sandbox-general-availability) and [a guide to prepare for the deprecation](https://developers.google.com/privacy-sandbox/3pcd).
## CSS updates
For CSS we have three updates:
Number one: the new [`:user-invalid`](https://developer.mozilla.org/docs/Web/CSS/:user-invalid) and [`:user-valid`](https://developer.mozilla.org/docs/Web/CSS/:user-valid) pseudo-classes that represent an element with incorrect or correct input, respectively, but only after the user has significantly interacted with it. They are similar to the `:valid` and `:invalid`, pseudo-classes but with the added constraint that the new pseudo-classes only match after the user has interacted with the element.
Number two: the [relative color syntax](https://developer.chrome.com/blog/css-relative-color-syntax) allows developers to define colors by modifying the parameters of other colors.
For example: `oklab(from magenta calc(l * 0.8) a b);` results in an Oklab magenta that is 80% lighter.
And number three: `clip-path` now supports more values.
The [`clip-path`](https://developer.mozilla.org/docs/Web/CSS/clip-path) property creates a clipping region that sets what part of an element should be shown. Parts that are inside the region are shown, while those outside are hidden.
Now you can use [`<geometry-box>`](https://developer.mozilla.org/docs/Web/CSS/clip-path#geometry-box) values to control the clip's reference box, making `clip-path` easier to use. These box values can be used alongside basic shapes (for example, `clip-path: circle(50%) margin-box`), or they can be used alone to clip to the specified box (for example,`clip-path: content-box`).
You can also use the functions [`xywh()`](https://developer.mozilla.org/docs/Web/CSS/basic-shape/xywh) and [`rect()`](https://developer.mozilla.org/docs/Web/CSS/basic-shape/rect) that make it easier to specify rectangular or rounded-rectangular clips.
_Correction: A previous version of this article referred to improvements for Fenced Frames. These changes are now shipping in Chrome 120._
## And more!
Of course there’s plenty more.
  * [`WebSQL` is fully removed](https://developer.chrome.com/blog/deprecating-web-sql) as of Chrome 119. A reverse origin trial allows developers to continue to use WebSQL until Chrome 123.
  * Now the [`monitorTypeSurfaces`](https://developer.chrome.com/docs/web-platform/screen-sharing-controls#monitorTypeSurfaces) option can be used to prevent the user from sharing an entire screen, with [`getDisplayMedia()`](https://developer.mozilla.org/docs/Web/API/MediaDevices/getDisplayMedia)
  * There’s [an origin trial](https://developer.chrome.com/origintrials#/view_trial/106960491150049281) that adds a `fullscreen` windowFeatures parameter to the `window.open()` JavaScript API to allow the caller to open a popup directly to full-screen.


## Further reading
This covers only some key highlights. Check the links below for additional changes in Chrome 119.
  * [What's new in Chrome DevTools (119)](https://developer.chrome.com/blog/new-in-devtools-119)
  * [Chrome 119 deprecations and removals](https://developer.chrome.com/blog/deps-rems-119)
  * [ChromeStatus.com updates for Chrome 119](https://chromestatus.com/features#milestone%3D119)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/118.0.5993.116..119.0.6045.63)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
Yo soy Adriana Jara, and as soon as Chrome 120 is released, I'll be right here to tell you what's new in Chrome!
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2023-10-31 UTC.

