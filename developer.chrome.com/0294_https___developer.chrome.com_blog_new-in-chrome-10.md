---
url: https://developer.chrome.com/blog/new-in-chrome-107?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-107?hl=en
date: 2025-05-11T16:57:01.034996
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-107?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-chrome-107?hl=es-419)




  * On this page
  * [New properties in Screen Capture API](https://developer.chrome.com/blog/new-in-chrome-107?hl=en#new-screen-capture)
  * [Identify render blocking resources](https://developer.chrome.com/blog/new-in-chrome-107?hl=en#render-blocking-status)
  * [PendingBeacon API origin trial](https://developer.chrome.com/blog/new-in-chrome-107?hl=en#pending-beacon)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  New in Chrome 107 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [New properties in Screen Capture API](https://developer.chrome.com/blog/new-in-chrome-107?hl=en#new-screen-capture)
  * [Identify render blocking resources](https://developer.chrome.com/blog/new-in-chrome-107?hl=en#render-blocking-status)
  * [PendingBeacon API origin trial](https://developer.chrome.com/blog/new-in-chrome-107?hl=en#pending-beacon)


Adriana Jara 
[ GitHub ](https://github.com/tropicadri) [ LinkedIn ](https://www.linkedin.com/in/adrianajara) [ Mastodon ](https://hachyderm.io/@tropicadri)
Here's what you need to know:
  * There are [new properties in the Screen Capture API](https://developer.chrome.com/blog/new-in-chrome-107?hl=en#new-screen-capture) to improve the screen sharing experiences.
  * You can now precisely identify whether a resource on your page is [render blocking or not](https://developer.chrome.com/blog/new-in-chrome-107?hl=en#render-blocking-status).
  * There is a new way to send data to a backend server with the declarative [PendingBeacon API](https://developer.chrome.com/blog/new-in-chrome-107?hl=en#pending-beacon) in origin trial. And there’s plenty more.
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-107?hl=en#more).


I'm [Adriana Jara](https://twitter.com/tropicadri). Let's dive in and see what's new for developers in Chrome 107.
## New properties in Screen Capture API
In this version the Screen Capture API adds new properties to improve the screen sharing experiences.
The `DisplayMediaStreamOptions` added the `selfBrowserSurface` property. With this hint the application can tell the browser that when calling `getDisplayMedia()` the current tab should be excluded.
```
// Exclude the streaming tab
constoptions={
selfBrowserSurface:'exclude',
};
conststream=awaitnavigator
.mediaDevices
.getDisplayMedia(options);

```

It helps prevent accidental self capture and avoids the “Hall of Mirrors” effect we’ve seen in video conferences.
`DisplayMediaStreamOptions`now also has the `surfaceSwitching` property. This property adds an option to programmatically control whether Chrome shows a button for switching tabs while screen sharing. These options will be passed to`getDisplayMedia()`. The `Share this tab instead` button allows users to switch to a new tab without going back to the video-conferencing tab or selecting from a long list of tabs, but the behavior is exposed conditionally in case the web application doesn’t handle it.
```
// Show the switch to this tab button
constoptions={
surfaceSwitching:'include',
};
conststream=awaitnavigator
.mediaDevices
.getDisplayMedia(options);

```

Also `MediaTrackConstraintSet` adds the property `displaySurface`. When `getDisplayMedia()` is called the browser offers the user a choice of display surfaces: tabs, windows or monitors. Using the `displaySurface` constraint, the web app may now hint to the browser if it prefers one of the surface types to be offered more prominently.
For example, it can help [prevent oversharing](https://developer.chrome.com/blog/avoiding-oversharing-when-screen-sharing) by accident since sharing a single tab can be the default. 
## Identify render blocking resources
Reliable insights into a page’s performance are critical for developers to build fast user experiences, so far developers have relied on complex heuristics to determine whether a resource is render blocking or not.
Now the Performance API includes the renderBlockingStatus property which provides a direct signal from the browser that identifies the resources that prevent your page from displaying, until they are downloaded.
The code snippet here, shows how to get a list of all your resources and use the new renderBlockingStatus property to list all of those that are render blocking.
```
// Get all resources
constres=window.performance.getEntriesByType('resource');
// Filter to get only the blocking ones
constblocking=res.filter(({renderBlockingStatus})=>
renderBlockingStatus==='blocking');

```

Optimizing how you load your resources helps with [Core Web Vitals](https://web.dev/articles/vitals) and with providing a better user experience, Check out the MDN documentation to learn more about the [Performance API](https://developer.mozilla.org/docs/Web/API/Performance_API), look for those render blocking resources and optimize away.
## PendingBeacon API origin trial
The declarative [PendingBeacon API](https://github.com/WICG/pending-beacon) lets the browser control when beacons are sent.
A beacon is a bundle of data sent to a backend server, without expecting a particular response.
Applications often want to send these beacons at the end of a user's visit, but there's no good time for that "send" call to be made. This API delegates the sending to the browser itself, so it can support beacons on `page unload` or on `page hide`, without the developer having to implement send calls at exactly the right times.
[Sign up for the origin trial](https://developer.chrome.com/docs/web-platform/origin-trials), give the API a try and please send feedback our way to improve the use cases.
## And more!
Of course there’s plenty more.
  * The `expect-ct` http header is deprecated.
  * The `rel` attribute is now supported on `<form>` elements.
  * Last time I mentioned [`grid-template` interpolation](https://web.dev/articles/css-animated-grid-layouts), this time it should be included.


## Further reading
This covers only some key highlights. Check the links below for additional changes in Chrome 107.
  * [What's new in Chrome DevTools (107)](https://developer.chrome.com/blog/new-in-devtools-107)
  * [Chrome 107 deprecations and removals](https://developer.chrome.com/blog/deps-rems-107)
  * [ChromeStatus.com updates for Chrome 107](https://www.chromestatus.com/features#milestone%3D107)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/106.0.5249.68..107.0.5304.71)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
I’m Adriana Jara, and as soon as Chrome 108 is released, I'll be right here to tell you what's new in Chrome!
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2022-10-25 UTC.

