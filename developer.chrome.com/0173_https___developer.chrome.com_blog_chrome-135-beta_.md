---
url: https://developer.chrome.com/blog/chrome-135-beta?hl=en
title: https://developer.chrome.com/blog/chrome-135-beta?hl=en
date: 2025-05-11T16:54:24.611451
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/chrome-135-beta?hl=en#main-content)
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


#  Chrome 135 beta 
Stay organized with collections  Save and categorize content based on your preferences. 
Rachel Andrew 
[ GitHub ](https://github.com/rachelandrew) [ LinkedIn ](https://www.linkedin.com/in/rachelandrew) [ Mastodon ](https://front-end.social/@rachelandrew) [ Bluesky ](https://bsky.app/profile/rachelandrew.bsky.social) [ Homepage ](https://rachelandrew.co.uk)
Published: March 05, 2025 
Unless otherwise noted, the following changes apply to the newest Chrome beta channel release for Android, ChromeOS, Linux, macOS, and Windows. Learn more about the features listed here through the provided links or from the list on ChromeStatus.com. Chrome 135 is beta as of 5 March 2025. You can download the latest on [Google.com](https://www.google.com/chrome/beta/) for desktop or on Google Play Store on Android.
## CSS and UI
This release adds thirteen new CSS and UI features.
### Anchor positioning remembered scroll offset
Add support for the concept of [_remembered scroll offset_](https://drafts.csswg.org/css-anchor-position-1/#scroll). When a positioned element has a default anchor, and is tethered to this anchor at one edge, and against the original containing block at the other edge, the scroll offset will be taken into account when it comes to sizing the element. This means you can use all visible space (using `position-area`) for the anchored element when the document is scrolled at a given scroll offset. In order to avoid layout (resizing the element) every time the document is scrolled, the browser uses the _remembered scroll offset_ , rather than always using the current scroll offset. The remembered scroll offset is updated at an _anchor recalculation point_ , which is either the position where the positioned element is initially displayed, or, when a different position option (`position-try-fallbacks`) is chosen.
### CSS Inertness
Making an element inert affects whether it can be focused, edited, selected, and searchable by find-in-page. It also affects whether it is visible in the accessibility tree. The `interactivity` property specifies whether an element and its flat tree descendants (including text runs) are inert or not. The `interactivity` property accepts one of two values: `auto` or `inert`.
### Logical overflow properties
The `overflow-inline` and `overflow-block` CSS properties let you set overflow in inline and block direction relative to the writing-mode. In a horizontal writing-mode `overflow-inline` maps to `overflow-x`, while in a vertical writing-mode it maps to `overflow-y`.
### Sign-related functions: `abs()` and `sign()`
### The `dynamic-range-limit` property
Lets a page limit the maximum brightness of HDR content.
### The `shape()` function
The `shape()` function allows responsive free-form shapes in the `clip-path` property. It lets you define a series of commands, equivalent to the commands in `path()`. However, the commands accept responsive units (for example, `%` or `vw`), as well as any CSS values such as custom properties.
### The `::column` pseudo-element
A `::column` pseudo-element, which allows applying a limited set of styles to the generated fragments. Specifically, this is limited to styles which do not affect the layout, and thus can be applied post-layout.
### `::scroll-button()` pseudo-elements
Allow the creation of interactive scroll buttons as pseudo-elements. For example:
```
.scroller{
overflow:auto;
}
.scroller::scroll-button(inline-start){
content:"<";
}
.scroller::scroll-button(inline-end){
content:">";
}

```

These should be focusable, behaving as a button (including their UA styles). When activated, a scroll should be performed in the direction by some amount. When it is not possible to scroll in that direction, they should be disabled (and styled with `:disabled`), otherwise they are enabled (and styled with `:enabled`). The selector lets you define buttons in four logical directions: `block-start`, `block-end`, `inline-start`, `inline-end`; as well as four physical directions: `up`, `down`, `left`, `right`.
### `::scroll-marker` and `::scroll-marker-group`
Adds the `::scroll-marker` and `::scroll-marker-group` for scrolling containers. These pseudo-elements let you create a set of focusable markers for all of the associated items within the scrolling container.
### Nested pseudo elements styling
Enables styling of pseudo-elements that are nested inside other pseudo-elements. So far, support is defined for: `::before::marker` and `::after::marker` with `::column::scroll-marker` being supported in the future.
### Partitioning `:visited` links history
To eliminate user browsing history leaks, anchor elements are styled as `:visited` only if they have been clicked from this top-level site and frame origin before. By only styling links that have been clicked on this site and frame before, the many side-channel attacks that have been developed to obtain `:visited` links styling information are now obsolete, as they no longer provide sites with new information about users.
There is an exception for _self-links_ , where links to a site's own pages can be styled as `:visited` even if they have not been clicked on in this exact top-level site and frame origin before. This exemption is only enabled in top-level frames or subframes which are the same-origin with the top-level frame. The privacy benefits are still achieved because sites already know which of its subpages a user has visited, so no new information is exposed. This was a community-requested exception which improves user experience.
### Interpolation progress functional notation: CSS `*progress()` function
### `safe-area-max-inset-`* variables
In addition to the `safe-area-inset` environment variables, Chrome now also supports `max-area-safe-inset-`* variants of these variables. Unlike the dynamic insets, the max insets do not change and represent the maximum possible safe area inset.
These values are necessary when building performant edge-to-edge web experiences.
## Web APIs
### Add `MediaStreamTrack` support to the Web Speech API
Add `MediaStreamTrack` support to the Web Speech API. The Web Speech API is a web standard API that allows developers to incorporate speech recognition and synthesis into their web pages. Currently, the Web Speech API uses the user's default microphone as the audio input. MediaStreamTrack support allows websites to use the Web Speech API to caption other sources of audio including remote audio tracks.
### Blob URL Partitioning: Fetching and navigation
As a continuation of Storage Partitioning, this feature implements partitioning of Blob URL access by Storage Key (top-level site, frame origin, and the has-cross-site-ancestor boolean), with the exception of top-level navigations which will remain partitioned only by frame origin.
### CSP `require-sri-for` for scripts
The `require-sri-for` directive gives you the ability to assert that every resource of a given type needs to be integrity checked. If a resource of that type is attempted to be loaded without integrity metadata, that attempt will fail and trigger a CSP violation report. This intent covers the `"script"` value of this directive.
### Create service worker client and inherit service worker controller for `srcdoc` iframe
Srcdoc context documents are currently not service worker clients and not covered by their parent's service worker. That results in some discrepancies (for example, Resource Timing reports the URLs that these documents load, but service worker doesn't intercept them). This aims to fix the discrepancies by creating service worker clients for `srcdoc` iframes and make them inherit their parent's service worker controller.
### Dispatching click events to captured pointer
If a pointer is captured while the `pointerup` event is being dispatched, the `click` event will be dispatched to the captured target instead of the nearest common ancestor of `pointerdown` and `pointerup` events as per the UI Event spec. For uncaptured pointers, the `click` target remains unchanged.
### Float16Array
Adds the `Float16Array` typed array. Number values are rounded to IEEE fp16 when writing into `Float16Array` instances.
### Incorporating navigation initiator into the HTTP cache partition key
Chrome's HTTP cache keying scheme has been updated to include an `is-cross-site-main-frame-navigation` boolean to mitigate cross-site leak attacks involving top-level navigation. Specifically, this will prevent cross-site attacks in which an attacker can initiate a top-level navigation to a given page and then navigate to a resource known to be loaded by the page in order to infer sensitive information via load timing. This change also improves privacy by preventing a malicious site from using navigations to infer whether a user has visited a given site previously.
### HSTS tracking prevention
Mitigates user tracking by third-parties via the HSTS cache.
This feature only allows HSTS upgrades for top-level navigations and blocks HSTS upgrades for sub-resource requests. Doing so makes it infeasible for third-party sites to use the HSTS cache to track users across the web.
### Invoker Commands: the `command` and `commandfor` attributes
The `command` and `commandfor` attributes on `<button>` elements let you assign behaviour to buttons in a more accessible and declarative way, while reducing bugs and simplifying the amount of JavaScript needed for interactivity. Buttons with `commandfor` and `command` attributes will—when clicked, touched, or enacted with keypress—dispatch a `CommandEvent` on the element referenced by `commandfor`, with some default behaviours such as opening dialogs and popovers.
### Link `rel="facilitated-payment"` to support push payments
Adds support for `<link rel="facilitated-payment" href="...">` as a hint that the browser should notify registered payment clients about a pending push payment.
### The `NavigateEvent` `sourceElement` property
When a navigation is initiated by an Element (that is, a link click or a form submission), the `sourceElement` property on the `NavigateEvent` will return the initiating element.
### NotRestoredReasons API reason name change
The `NotRestoredReasons` API is changing some of the reason texts to align to the standardized names. Developers monitoring these reasons may notice a change in reason texts.
### On-device Web Speech API
### Service Worker client URL ignore `history.pushState` changes
Modifies the service worker `Client.url` property to ignore document URL changes using `history.pushState()` and other similar history APIs. The `Client.url` property is intended to be the creation URL of the HTML document which ignores such changes.
### Support `rel` and `relList` attributes for `SVGAElement`
The SVGAElement interface in SVG 2.0 allows manipulation of `<a>` elements similar to HTML anchor elements. Supporting the `rel` and `relList` attributes enhances security and privacy for developers. This alignment with HTML anchor elements ensures consistency and ease of use across web technologies.
### Timestamps for RTC Encoded Frames
This feature consists in exposing to the Web some timestamps that are present in WebRTC encoded frames transmitted via RTCPeerConnection. The timestamps in question are:
  * Capture timestamp: the timestamp when a frame was originally captured
  * Receive timestamp: the timestamp when a frame was received


### Update `ProgressEvent` to use double type for 'loaded' and 'total'
The `ProgressEvent` has attributes `loaded` and `total` indicating the progress, and their type is `unsigned long long` now. With this feature, the type for these two attributes is changed to `double` instead, which gives the developer more control over the value. For example, the developers can now create a ProgressEvent with the `total` of 1 and the `loaded` increasing from 0 to 1 gradually. This is aligned with the default behavior of the `<progress>` HTML element if the max attribute is omitted.
### The `fetchLater` API
The `fetchLater()` API is a JavaScript API to request a deferred fetch, especially useful for more reliable beaconing at the end of a page's lifetime. Once called in a document, a deferred request is queued by the browser in the PENDING state, and will be invoked by the earliest of the following conditions:
The document is destroyed. After a user-specified time. For privacy reasons, all pending requests will be flushed when the document enters bfcache no matter how much time is left. The browser decides it's time to send it.
The API returns a `FetchLaterResult` that contains a boolean field `activated` that may be updated to tell whether the deferred request has been sent out or not. On successful sending, the whole response will be ignored by the browser, including body and headers.
Note that from the point of view of the API user, the exact send time is unknown.
## New origin trials
In Chrome 135 you can opt into the following new [origin trials](https://developer.chrome.com/docs/web-platform/origin-trials).
### Interest Invokers
This feature adds an `interesttarget` attribute to `<button>` and `<a>` elements. The `interesttarget` attribute adds "interest" behaviors to the element, such that when the user "shows interest" in the element, actions are triggered on the target element. Actions can include things like showing a popover. The user agent will handle detecting when the user "shows interest" in the element, using methods such as hovering the element with a mouse, hitting special hotkeys on the keyboard, or long-pressing the element on touchscreens. When interest is shown or lost, an `InterestEvent` is fired on the target, which have default actions in the case of popovers—showing and hiding the popover.
### Signature-based Integrity
This feature provides web developers with a mechanism to verify the provenance of resources they depend upon, creating a technical foundation for trust in a site's dependencies. In short: servers can sign responses with a Ed25519 key pair, and web developers can require the user agent to verify the signature using a specific public key. This offers a helpful addition to URL-based checks offered by Content Security Policy on the one hand, and Subresource Integrity's content-based checks on the other.
## Deprecations and removals
This version of Chrome introduces the deprecations and removals listed below. Visit ChromeStatus.com for lists of planned deprecations, current deprecations and previous removals.
This release of Chrome deprecates one feature.
### Deprecate getters of Intl Locale Info
The Intl Locale Info API is a Stage 3 ECMAScript TC39 proposal to enhance the `Intl.Locale` object by exposing Locale information, such as week data (first day in a week, weekend start day, weekend end day, minimum day in the first week), and text direction hour cycle used in the locale. Chrome landed an implementation in Chrome 99, however the proposal changed to move several getters to functions. We need to remove the deprecated getters and relaunch the renamed functions.
This release of Chrome removes three features.
### Remove deprecated `navigator.xr.supportsSession` method
`navigator.xr.supportsSession` was replaced in the WebXR spec by the `navigator.xr.isSessionSupported` method in September of 2019 after receiving feedback on the API shape from the TAG. It has been marked as deprecated in Chrome since then, producing a console warning redirecting developers to the updated API. Usage of the call is very low, and all major frameworks that are used to build WebXR content have been confirmed to have been updated to use the newer call.
### Remove `NavigateEvent` `canTransition` property
In Chrome 108, the `NavigateEvent`'s `transitionWhile()` method and `canTransition` property were replaced with the new `intercept()` method and `canIntercept` property. At that time, the `transitionWhile()` method was removed. However, we forgot to remove the `canTransition` property: instead, we left it around as an alias for `canIntercept`. In Chrome 135, we're fixing that and removing `canTransition`. Any uses of `canTransition`can be replaced with `canIntercept`, with no change in behavior.
### Remove WebGPU limit maxInterStageShaderComponents
The `maxInterStageShaderComponents` limit is being removed due to a combination of factors:
  * Redundancy with `maxInterStageShaderVariables`: This limit already serves a similar purpose, controlling the amount of data passed between shader stages.
  * Minor Discrepancies: While there are slight differences in how the two limits are calculated, these differences are minor and can be effectively managed within the `maxInterStageShaderVariables limit`.
  * Simplification: Removing `maxInterStageShaderComponents` streamlines the shader interface and reduces complexity for developers. Instead of managing two separate limits (that both apply simultaneously but with subtle differences), they can focus on the more appropriately named and comprehensive `maxInterStageShaderVariables`.


Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-03-05 UTC.

