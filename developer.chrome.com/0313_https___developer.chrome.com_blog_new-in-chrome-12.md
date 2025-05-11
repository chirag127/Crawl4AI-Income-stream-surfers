---
url: https://developer.chrome.com/blog/new-in-chrome-126?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-126?hl=en
date: 2025-05-11T16:57:27.068915
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-126?hl=en#main-content)


  * On this page
  * [Cross-document view transitions for same-origin navigations](https://developer.chrome.com/blog/new-in-chrome-126?hl=en#cross-document-transitions)
  * [CloseWatcher API re-enabled](https://developer.chrome.com/blog/new-in-chrome-126?hl=en#close-watcher-api)
  * [Gamepad API trigger-rumble extension](https://developer.chrome.com/blog/new-in-chrome-126?hl=en#trigger-rumble)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  New in Chrome 126 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Cross-document view transitions for same-origin navigations](https://developer.chrome.com/blog/new-in-chrome-126?hl=en#cross-document-transitions)
  * [CloseWatcher API re-enabled](https://developer.chrome.com/blog/new-in-chrome-126?hl=en#close-watcher-api)
  * [Gamepad API trigger-rumble extension](https://developer.chrome.com/blog/new-in-chrome-126?hl=en#trigger-rumble)


Adriana Jara 
[ GitHub ](https://github.com/tropicadri) [ LinkedIn ](https://www.linkedin.com/in/adrianajara) [ Mastodon ](https://hachyderm.io/@tropicadri)
Here's what you need to know:
  * [Cross-document transitions](https://developer.chrome.com/blog/new-in-chrome-126?hl=en#cross-document-transitions) are newly supported in the View Transitions API.
  * The [CloseWatcher API](https://developer.chrome.com/blog/new-in-chrome-126?hl=en#close-watcher-api) is available once again.
  * The Gamepad API now includes [trigger-rumble](https://developer.chrome.com/blog/new-in-chrome-126?hl=en#trigger-rumble).
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-126?hl=en#more).


I'm Adriana Jara. Let's dive in and see what's new for developers in Chrome 126.
## Cross-document view transitions for same-origin navigations
The [View Transitions API](https://developer.mozilla.org/docs/Web/API/View_Transitions_API) gives you the power to create seamless visual transitions between different views and now it is available by default for same-origin navigations. Previously it was only available for single page application architectures.
To implement a cross-document view transition, both ends need to opt-in. To do this, use the view-transition at-rule and set the navigation descriptor to auto.
Cross-document view transitions use the same building blocks and principles as same-document view transitions.
```
@view-transition{
navigation:auto;
}

```

Visit [Smooth transitions with the View Transition API](https://developer.chrome.com/docs/web-platform/view-transitions) for details, samples are more.
## CloseWatcher API re-enabled
For `<dialog>` and `popover=""` elements, the CloseWatcher API makes it easier to handle close requests, like the ESC key on desktop platforms or the back gesture on Android.
This feature was originally shipped in [Chrome 120](https://developer.chrome.com/blog/new-in-chrome-120#close-watcher), but was disabled because of an unexpected interaction with the dialog element. It has been re enabled in Chrome 126 after improvements to minimize the previous problems.
To learn how to use CloseWatcher visit [its demo](https://close-watcher-demo.glitch.me/).
## Gamepad API trigger-rumble extension
The trigger-rumble capability is now part of the [Gamepad API](https://developer.mozilla.org/docs/Web/API/Gamepad_API). It enhances gaming experiences on the web for compatible controllers.
`trigger-rumble` extends the [`GamepadHapticActuator`](https://developer.mozilla.org/docs/Web/API/GamepadHapticActuator), which is an interface that represents hardware in the controller designed to provide haptic feedback to the user (if available). `trigger-rumble` allows web applications that use the Gamepad API to also vibrate the triggers of those gamepad devices.
With the following code you can check if the functionality is supported in the browser and how to trigger— pun intended —`trigger-rumble`
```
// This assumes a `Gamepad` as the value of the `gamepad` variable.
consttriggerRumble=(gamepad,delay=0,duration=100,weak=1.0,strong=1.0)=>{
if(!('vibrationActuator'ingamepad)){
return;
}
// Feature detection.
if(!('effects'ingamepad.vibrationActuator)||!gamepad.vibrationActuator.effects.includes('trigger-rumble')){
return;
}
gamepad.vibrationActuator.playEffect('trigger-rumble',{
// Duration in ms.
duration:duration,
// The left trigger (between 0 and 1).
leftTrigger:leftTrigger,
// The right trigger (between 0 and 1).
rightTrigger:rightTrigger,
});
};

```

Check out [Play the Chrome dino game with your gamepad](https://web.dev/articles/gamepad) for more information to make the most of the Gamepad API.
## And more!
Of course there's plenty more.
  * [`GeolocationCoordinates`](https://developer.mozilla.org/docs/Web/API/GeolocationCoordinates) and [`GeolocationPosition`](https://developer.mozilla.org/docs/Web/API/GeolocationPosition) now include a `.toJSON()` method.
  * In [DevTools updates](https://developer.chrome.com/blog/new-in-devtools-126), you can inspect storage buckets in a dedicated tree in the **Application** > **Storage** section.
  * ChromeOS now supports [tabbed mode for web apps](https://developer.chrome.com/docs/capabilities/tabbed-application-mode).


[Read the full release notes](https://developer.chrome.com/release-notes/126).
## Further reading
This covers only some key highlights. Check the following links for additional changes in Chrome 126.
  * [What's new in Chrome DevTools (126)](https://developer.chrome.com/blog/new-in-devtools-126)
  * [ChromeStatus.com updates for Chrome 126](https://chromestatus.com/features#milestone%3D126)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/125.0.6422.168..126.0.6478.41)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
Yo soy Adriana Jara, and as soon as Chrome 127 is released, I'll be right here to tell you what's new in Chrome!
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-06-11 UTC.

