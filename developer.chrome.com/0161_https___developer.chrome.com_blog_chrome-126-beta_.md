---
url: https://developer.chrome.com/blog/chrome-126-beta?hl=en
title: https://developer.chrome.com/blog/chrome-126-beta?hl=en
date: 2025-05-11T16:54:12.889741
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/chrome-126-beta?hl=en#main-content)
Sign in


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  Chrome 126 beta 
Stay organized with collections  Save and categorize content based on your preferences. 
Unless otherwise noted, the following changes apply to the newest Chrome beta channel release for Android, ChromeOS, Linux, macOS, and Windows. Learn more about the features listed here through the provided links or from the list on [ChromeStatus.com](https://chromestatus.com/). Chrome 126 is beta as of 15 May 2024. You can download the latest on [Google.com](https://www.google.com/chrome/beta/) for desktop or on Google Play Store on Android.
## CSS
This release adds one new CSS feature.
### Cross-document view transitions for same-origin navigations
Previously you had to rearchitect your website to an SPA to use the View Transitions API. This is no longer the case. View transitions are now available for same-origin navigations. You can create a view transition between two different documents that are the same-origin.
To enable a cross-document view transition, both ends need to opt-in. To do this, use the `@view-transition` at-rule and set the `navigation` descriptor to `auto`.
```
@view-transition{
navigation:auto;
}

```

Cross-document view transitions use the same building blocks and principles as same-document view transitions. Elements that have a `view-transition-name` applied are captured, and you can customize the animations using CSS animations.
Learn more in the [View Transitions API documentation](https://developer.chrome.com/docs/web-platform/view-transitions).
## Web APIs
_This post originally included the Automatic fullscreen content setting feature, which has now been moved to land in Chrome 127._
### Gamepad API trigger-rumble extension
Extends the `GamepadHapticActuator` interface to expose the [trigger-rumble capability](https://web.dev/articles/gamepad#trigger_rumble) on the Web for compatible gamepads. This extension will allow web applications that take advantage of the Gamepad API to also vibrate the triggers of gamepad devices that come equipped with this functionality.
### OpusEncoderConfig `signal` and `application` parameters
The `OpusEncoderConfig.signal` and `OpusEncoderConfig.application` parameters are mapped directly to implementation specific encoder knobs. These allow web authors to provide hints as to what type of data is being encoded, and in which context the data is being used.
`signal` can be one of `"auto"`, `"music"`, `"voice"`. It configures the encoder for the best performance in encoding the specified type of data. `application` can be one of `"voip"`, `"audio"`, `"lowdelay"`. It configures the encoder to favor speech intelligibility, faithful reproduction of the original input, or minimal latency.
### PointerEvent.deviceId for multi-pen inking
As devices with advanced pen input capabilities are becoming increasingly prevalent, it is important that the web platform continues to evolve to fully support these advanced features in order to unlock rich experiences for both end users and developers. One such advancement is the ability for a device's digitizer to recognize more than one pen device interacting with it simultaneously.
This feature is an extension to the `PointerEvent` interface to include a new attribute, `deviceId`, that represents a session-persistent, document isolated, unique identifier that a developer can reliably use to identify individual pens interacting with the page.
### ChromeOS tabbed web apps
PWAs in a standalone window can only have one page open at a time. Some apps expect users to have many pages open at once. Tabbed mode adds a tab strip to standalone web apps in ChromeOS that allows multiple tabs to be open at once.
The feature adds a new display mode of `"tabbed"` and a new manifest field to allow customizations to the tab strip.
### `toJSON()` method for `GeolocationCoordinates` and `GeolocationPosition`
Adds `.toJSON()` methods to the `GeolocationCoordinates` and `GeolocationPosition` interfaces. This enables serialization of these objects with `JSON.stringify()`.
### `visualViewport` `onscrollend` support
The `scrollend` JavaScript event fires to signal that a scrolling operation has come to an end.
The `visualViewport` interface includes an `onscrollend` event handler that should be invoked when a scrolling operation on the `visualViewport` has ended. Chrome already supports adding a scrollend event listener through `visualViewport.addEventListener("scrollend")`. This just makes it possible to also add an event listener using `visualViewport.onscrollend`.
### WebGLObject Web IDL superinterface
This feature exposes the `WebGLObject` type in the same contexts where the WebGL API is exposed—on the main thread and workers.
### WebRTC encoded transform: Modify Metadata functions
Some WebRTC Encoded Transform use cases involve manipulation of not only the payload of encoded video or audio frames but also its metadata. For example:
Altering the timestamp of a frame to introduce a delay. Changing the mime type of the frame if the transform changes the type of the payload. Forwarding of media to a new peer connection set up to use different metadata values.
The feature lets the WebRTC Encoded Transform API manipulate audio and video frame metadata.
### SVG support for the Async Clipboard API
Switch to UTF-8 on Windows while writing `image/svg+xml` format to the clipboard. HTML format already uses UTF-* on Windows and this will allow copying and pasting SVG images from the clipboard.
On all other supported platforms, `image/svg+xml` is serialized into UTF-8 before it gets written to the clipboard.
Read more in [SVG support for the Async Clipboard API](https://developer.chrome.com/blog/svg-support-for-async-clipboard-api).
### Re-enabling the `CloseWatcher` API and close requests for `<dialog>` and `popover=""`
The `CloseWatcher` API allows handling close requests, like the `ESC` key on desktop platforms or the back gesture or button on Android, in a uniform way. This feature was originally shipped [in Chrome 120](https://developer.chrome.com/blog/new-in-chrome-120), but was disabled due to [an unexpected interaction with `<dialog>`](https://issues.chromium.org/issues/41484805). It has been reenabled in Chrome 126 after some improvements to its behavior to minimize the problems seen there.
### Support for the UI Automation Accessibility Framework on Windows
Microsoft has worked with the Chrome team to support the UI Automation (UIA) framework on Windows directly, making it easier for accessibility tools to communicate with the browser. A gradual rollout to stable, starts in Chrome version 126. This enables Voice Access to function in all Chromium-based browsers and will enhance the user experience for all UIA-based accessibility tools, such as Narrator and Magnifier. This work will also eliminate the Windows UIA emulation layer, which has been the source of many performance issues in Chromium on Windows.
Learn more in [Introducing UIA support on Windows](https://developer.chrome.com/blog/windows-uia-support).
## New origin trials
In Chrome 126 you can opt into the following new [origin trials](https://developer.chrome.com/docs/web-platform/origin-trials).
### FedCM as a trust signal for the Storage Access API
Reconciles the FedCM and Storage Access APIs by making a prior FedCM grant a valid reason to automatically approve a storage access request.
When a user grants permission for using their identity with a third-party Identity Provider (IdP) on a Relying Party (RP), many IdPs require third-party cookies to function correctly and securely. This proposal aims to satisfy that requirement in a private and secure manner by updating the Storage Access API (SAA) permission checks to not only accept the permission grant that is given by a storage access prompt, but also the permission grant that is given by a FedCM prompt.
A key property of this mechanism is limiting the grant to cases explicitly allowed by the RP through the FedCM permissions policy, enforcing a per-frame control for the RP and preventing passive surveillance by the IdP beyond the capabilities that FedCM already grants.
[Register for FedCM as a trust signal for the Storage Access API origin trial](https://developer.chrome.com/origintrials#/view_trial/4008766618313162753).
### Media previews opt-out
This reverse origin trial excludes sites from the launch of Media Previews.
Chrome will provide real-time previews of camera and microphone input at the time camera and microphone permissions are requested by websites. These will also be available from the site's pageinfo.
In addition, users with multiple devices will be able to select a camera and microphone at the time permissions are requested, unless the site has requested a specific device through `getUserMedia()`.
To exclude your site from media previews register for the [media previews opt-out origin trial](https://developer.chrome.com/origintrials#/register_trial/3270176279424401409).
### FedCM: Continuation API, Parameters API, Fields API, Multiple configURLs, Custom Account Labels
Developers can start taking part in an origin trial for a bundle of desktop FedCM features that can include authorization. The bundle consists of FedCM Continuation API, Parameter API, Fields API, Multiple configURLs and Custom Account Labels. This enables an OAuth authorization flow-like experience involving an IdP-provided permission dialog.
### Keyboard focusable scroll containers deprecation trial
This feature introduces the following changes:
  * Scrollers are click-focusable and programmatically-focusable by default.
  * Scrollers without focusable children are keyboard-focusable by default.


This is an important improvement to help make scrollers and contents within scrollers more accessible to all users. You can read more about its benefits in the post [Keyboard focusable scrollers](https://developer.chrome.com/blog/keyboard-focusable-scrollers).
We attempted to ship these changes, and found that a limited number of sites had broken expectations around some of their components. As a result, we had to unship the feature to avoid this breakage. Given the benefits, we are shipping this feature again. To allow more time for the affected sites to migrate their components, we are starting a deprecation trial. When enabled, this will disable the `KeyboardFocusableScrollers` feature.
## Deprecations and removals
There are no new deprecations or removals in this version of Chrome. However, this is the last Chrome release that supports mutation events. They will be removed in Chrome 127. Read [Mutation events will be removed from Chrome](https://developer.chrome.com/blog/mutation-events-deprecation) to learn more and prepare for this removal.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-05-16 UTC.

