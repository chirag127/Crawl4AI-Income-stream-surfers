---
url: https://developer.chrome.com/blog/new-in-chrome-100?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-100?hl=en
date: 2025-05-11T16:56:56.962911
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-100?hl=en#main-content)
Sign in


  * On this page
  * [100 Cool Web Moments](https://developer.chrome.com/blog/new-in-chrome-100?hl=en#100coolwebmoments)
  * [Reduced User-Agent string](https://developer.chrome.com/blog/new-in-chrome-100?hl=en#reduced-ua)
  * [Multi-screen window placement API](https://developer.chrome.com/blog/new-in-chrome-100?hl=en#multi-screen-window-placement)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  New in Chrome 100 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [100 Cool Web Moments](https://developer.chrome.com/blog/new-in-chrome-100?hl=en#100coolwebmoments)
  * [Reduced User-Agent string](https://developer.chrome.com/blog/new-in-chrome-100?hl=en#reduced-ua)
  * [Multi-screen window placement API](https://developer.chrome.com/blog/new-in-chrome-100?hl=en#multi-screen-window-placement)


Pete LePage 
[ GitHub ](https://github.com/petele) [ Glitch ](https://glitch.com/@petele) [ Mastodon ](https://techhub.social/@petele) [ Homepage ](https://petelepage.com/)
Here's what you need to know:
  * Chrome 100 has a [three digit version](https://developer.chrome.com/blog/new-in-chrome-100?hl=en#chrome100) number
  * Take a stroll down memory lane and celebrate [#100CoolWebMoments](https://developer.chrome.com/blog/new-in-chrome-100?hl=en#100coolwebmoments) since Chrome's first release.
  * There are some important changes to the [user agent string](https://developer.chrome.com/blog/new-in-chrome-100?hl=en#reduced-ua).
  * The [Multi-Screen Window Placement API](https://developer.chrome.com/blog/new-in-chrome-100?hl=en#multi-screen-window-placement) makes it possible to enumerate the displays connected to a user's machine, and place windows on specific screens.
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-100?hl=en#more).


I'm [Pete LePage](https://petelepage.com). Let's dive in and see what's new for developers in Chrome 100.
## Chrome 100
When browsers first reached version 10, there were a few issues as the major version number went from one digit to two. Hopefully, we learned a few things that'll ease the transition from two digits to three.
Chrome 100 is available now, and Firefox 100 ships very soon. These three digit version numbers have the potential to cause issues on sites that rely on identifying the browser version in some way. Over the last few months, the Firefox team, and the Chrome team, ran experiments in which the browser reported version number 100, even though it wasn't.
This led to a few reported issues, many of which have already been fixed. But, we still need your help.
  * If you are a website maintainer, test your website with Chrome and Firefox 100.
  * If you develop a User-Agent parsing library, add tests to parse versions greater than and equal to 100.


Check out [Chrome and Firefox soon to reach major version 100](https://web.dev/chrome-firefox-100/) on [web.dev](https://web.dev/) for more details.
## 100 Cool Web Moments
It's been exciting to watch the web grow, and see all the amazing stuff you've built over the last 100 Chrome releases. We thought it would be fun to take a stroll down memory lane and celebrate [#100CoolWebMoments](https://developer.chrome.com/100) that have happened in the last 14 years.
Tell us which moments you loved the most. If we've missed anything (and we're sure we have), tweet us [@Chromiumdev](https://twitter.com/ChromiumDev) with [#100CoolWebMoments](https://twitter.com/hashtag/100CoolWebMoments). Enjoy!
## Reduced User-Agent string
Speaking of the user agent, Chrome 100 will be the last version to support an unreduced User-Agent string by default. This is part of a strategy to replace use of the User-Agent string, with the new [User-Agent Client Hints API](https://web.dev/user-agent-client-hints/).
Starting in Chrome 101, the user agent will be gradually reduced.
Check out [User Agent Reduction Origin Trial and Dates](https://blog.chromium.org/2021/09/user-agent-reduction-origin-trial-and-dates.html) on the [Chromium blog][crblog], to learn more about what will be removed, and when.
## Multi-screen window placement API
For some apps, opening new windows and putting them in specific places, or specific displays is an important feature. For example, when using Slides to present, I want the slides to appear full screen on the primary display, and my speaker notes to appear on the other display.
The Multi-Screen Window Placement API makes it possible to enumerate the displays connected to the user's machine, and place windows on specific screens.
You can quickly check if there's more than one screen connected to the device with `window.screen.isExtended`.
```
constisExtended=window.screen.isExtended;
// returns true/false

```

But, the key functionality is in `window.getScreenDetails()`, which provides details about the attached displays.
```
constx=awaitwindow.getScreenDetails();
// returns
// {
//  currentScreen: {...}
//  oncurrentscreenchange: null
//  onscreenschange: null
//  screens: [{...}, {...}]
// }

```

For example, you can determine the primary screen, then use `requestFullscreen()` to make an element full screen on that display.
```
try{
constscreens=awaitwindow.getScreenDetails();
constprimary=screens
.filter((screen)=>screen.primary)[0]
awaitelem.requestFullscreen({screen:primary});
}catch(err){
console.error(err);
}

```

And it provides a way to listen for changes, for example if a new display is plugged in or removed, the resolution changes, and so on.
```
constscreens=awaitwindow.getScreenDetails();
letnumScreens=screens.screens.length;
screens.addEventListener('screenschange',(event)=>{
if(screens.screens.length!==numScreens){
console.log('Screen count changed');
numScreens=screens.screens.length;
}
});

```

Check out Tom's updated article [Managing several displays with the Multi-Screen Window Placement API](https://web.dev/multi-screen-window-placement/) on [web.dev](https://web.dev/) for a deeper dive.
## And more!
Of course there's plenty more.
There's a new `forget()` method for HID Devices that allow you to revoke a permission to an HID Device that was granted by a user.
```
// Request an HID device.
const[device]=awaitnavigator.hid.requestDevice(opts);

// Then later, revoke permission to the device.
awaitdevice.forget();

```

And for WebNFC, the `makeReadOnly()` method allows you to make NFC tags permanently read-only.
```
constndef=newNDEFReader();
awaitndef.makeReadOnly();

```

## Further reading
This covers only some of the key highlights. Check the links below for additional changes in Chrome 100.
  * [What's new in Chrome DevTools (100)](https://developer.chrome.com/blog/new-in-devtools-100)
  * [Chrome 100 deprecations and removals](https://developer.chrome.com/blog/deps-rems-100)
  * [ChromeStatus.com updates for Chrome 100](https://www.chromestatus.com/features#milestone%3D100)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/99.0.4844.48..100.0.4896.63.48)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
I'm Pete LePage, and as soon as Chrome 101 is released, I'll be right here to tell you what's new in Chrome!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2022-03-29 UTC.

