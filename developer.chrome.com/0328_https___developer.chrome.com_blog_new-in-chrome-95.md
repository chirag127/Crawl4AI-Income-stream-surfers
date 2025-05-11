---
url: https://developer.chrome.com/blog/new-in-chrome-95?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-95?hl=en
date: 2025-05-11T16:57:43.105141
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-95?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-chrome-95?hl=es-419)




  * On this page
  * [Routing with URLPattern](https://developer.chrome.com/blog/new-in-chrome-95?hl=en#urlpattern)
  * [Picking colors with the Eye Dropper API](https://developer.chrome.com/blog/new-in-chrome-95?hl=en#eyedropper)
  * [User-agent reduction origin trial](https://developer.chrome.com/blog/new-in-chrome-95?hl=en#reduced-ua-ot)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  New in Chrome 95 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Routing with URLPattern](https://developer.chrome.com/blog/new-in-chrome-95?hl=en#urlpattern)
  * [Picking colors with the Eye Dropper API](https://developer.chrome.com/blog/new-in-chrome-95?hl=en#eyedropper)
  * [User-agent reduction origin trial](https://developer.chrome.com/blog/new-in-chrome-95?hl=en#reduced-ua-ot)


Pete LePage 
[ GitHub ](https://github.com/petele) [ Glitch ](https://glitch.com/@petele) [ Mastodon ](https://techhub.social/@petele) [ Homepage ](https://petelepage.com/)
Here's what you need to know:
  * Routing gets easier with [`URLPattern`](https://developer.chrome.com/blog/new-in-chrome-95?hl=en#urlpattern) baked into the browser.
  * The [Eye Dropper API](https://developer.chrome.com/blog/new-in-chrome-95?hl=en#eyedropper) provides a built in tool for selecting colors.
  * There's a new origin trial that allows you to opt into receiving the [reduced UA string](https://developer.chrome.com/blog/new-in-chrome-95?hl=en#reduced-ua-ot) now.
  * The [PWA Summit](https://developer.chrome.com/blog/new-in-chrome-95?hl=en#pwa-summit) videos are all online.
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-95?hl=en#more).


I'm [Pete LePage](https://petelepage.com), working, and shooting from home, let's dive in and see what's new for developers in Chrome 95.
## Routing with `URLPattern`
Nearly all web apps depend on routing in some way whether it's code running on a server that maps a path to files on disk or logic in a single-page app that updates the DOM when the URL changes. `URLPattern` is a new web platform API that standardizes routing pattern syntax.
It builds on the foundation of existing frameworks, making it easier to perform common routing tasks. For example, matching against full URLs, or a URL pathname, then returning information about the token and group matches.
If you're already familiar with the routing syntax used in [Express](https://expressjs.com/en/guide/routing.html), Ruby on Rails, or [path-to-regexp](https://www.npmjs.com/package/path-to-regexp), this will probably look familiar.
To use it, create a new `URLPattern()` and provide the details you want to pattern match against. Patterns can contain wildcards, named token groups, regular expression groups, and group modifiers.
```
constp=newURLPattern({
protocol:'https',
hostname:'example.com',
pathname:'/:folder/*/:fileName.jpg',
search:'*',
hash:'*',
});

```

For example, let's look at the `URLPattern` that might be used by Google Docs. We'll specify the `kind` of file, the file `ID`, and what `mode` to open it in. Then to use the pattern, we can call either `test()`, or `exec()`.
```
consturl='https://docs.google.com/document/d/1s...5c/edit#heading=h.8...c';
constpattern=newURLPattern({
pathname:'/:kind/d/:fileID/:mode',
hash:'*',
});
constr=pattern.exec(url);
// {
//  "pathname": {"groups": {
//   "fileID": "1s...5c",
//   "kind": "document",
//   "mode": "edit"
//  }, ...},
//  "hash": {"groups": {"0":"heading=h.8...c"}, ...},
//  ...
// }

```

`URLPattern` is enabled by default in Chrome and Edge version 95 and above. And for browsers or environments like Node, that don't support it yet, you can use the [urlpattern-polyfill](https://github.com/kenchris/urlpattern-polyfill) library.
Check out Jeff's article [URLPattern brings routing to the web platform](https://web.dev/urlpattern/) for complete details!
## Picking colors with the Eye Dropper API
Almost every design app I've ever used has an eye dropper tool, making it easy to figure out what color something is. Some browsers have eyedropper capability built into `<input type=color>`, but it's not ideal.
The eye dropper API, implemented by some of the folks at Microsoft brings that functionality to the web. To use it, create a new `EyeDropper()` instance, then call `open()` on it.
```
consteyeDropper=newEyeDropper();
constresult=awaiteyeDropper.open();
// result = {sRGBHex: '#160731'}

```

Like many other modern web APIs, it works asynchronously, so that it doesn't block the main thread. When the user clicks on the color they want, it'll resolve with the color they clicked on.
You can try out a quick [demo](https://eyedropper-sample.glitch.me/), and see the [code](https://glitch.com/edit/#!/eyedropper-sample?path=script.js) on Glitch.
## PWA Summit
Did you catch the PWA Summit earlier this month?
It was great to see so many folks talking about PWAs and sharing their experiences. If you missed it, the videos are all up, so be sure to check it out at [PWASummit.org](https://pwasummit.org) or the [PWA Summit YouTube channel](https://www.youtube.com/channel/UC1j3gvdVISAEO1_2MwA5oQw/videos).
## User-agent reduction origin trial
[User-Agent Reduction](https://blog.chromium.org/2021/09/user-agent-reduction-origin-trial-and-dates.html) is an effort to reduce passive finger-printing surfaces, by reducing the information in the User-Agent string to only the browser's brand and significant version, its desktop or mobile distinction, and the platform it's running on.
Starting in Chrome 95, there's a new [origin trial](https://developer.chrome.com/blog/user-agent-reduction-origin-trial/) that allows you to opt into receiving the reduced UA string now. This will enable you to discover and fix problems before the reduced UA becomes the default behavior in Chrome.
The changes will be applied incrementally over a number of releases, but everything you need to prepare and test is ready right now.
All of the details and timeline are in the [User-Agent Reduction origin trial](https://developer.chrome.com/blog/user-agent-reduction-origin-trial/) post on [developer.chrome.com](https://developer.chrome.com/blog).
## And more!
Of course there's plenty more.
  * If you've been following the [Storage Foundation API](https://chromestatus.com/feature/5670244905385984) work, there's a new [origin trial for Access Handles](https://developer.chrome.com/origintrials/#/view_trial/3378825620434714625).
  * WebAssembly now provides [exception handling support](https://developer.chrome.com/origintrials/#/view_trial/2393663201947418625), which allows code to break control flow when an exception is thrown.
  * Chrome _100_ is coming next year. Which means it's time to make sure your code can handle more than **two** digits!


## Further reading
This covers only some of the key highlights. Check the links below for additional changes in Chrome 95.
  * [What's new in Chrome DevTools (95)](https://developer.chrome.com/blog/new-in-devtools-95)
  * [Chrome 95 deprecations & removals](https://developer.chrome.com/blog/deps-rems-95)
  * [ChromeStatus.com updates for Chrome 95](https://www.chromestatus.com/features#milestone%3D95)
  * [What's new in JavaScript in Chrome 95](https://v8.dev/blog/v8-release-95)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/94.0.4606.56..95.0.4638.56)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
I'm Pete LePage, and as soon as Chrome 96 is released, I'll be right here to tell you what's new in Chrome!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2021-10-19 UTC.

