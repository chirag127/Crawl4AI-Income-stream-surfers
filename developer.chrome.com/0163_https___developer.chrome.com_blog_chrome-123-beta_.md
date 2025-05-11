---
url: https://developer.chrome.com/blog/chrome-123-beta?hl=en
title: https://developer.chrome.com/blog/chrome-123-beta?hl=en
date: 2025-05-11T16:54:12.925998
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/chrome-123-beta?hl=en#main-content)
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


#  Chrome 123 beta 
Stay organized with collections  Save and categorize content based on your preferences. 
Unless otherwise noted, the following changes apply to the newest Chrome beta channel release for Android, ChromeOS, Linux, macOS, and Windows. Learn more about the features listed here through the provided links or from the list on [ChromeStatus.com](https://chromestatus.com). Chrome 123 is beta as of 21 February 2024. You can download the latest on [Google.com](https://www.google.com/chrome/beta/) for desktop or on Google Play Store on Android.
## CSS
This release adds five new CSS features.
### CSS `light-dark()` color function
The `light-dark()` function in CSS lets developers more easily adapt color-scheme to a user's preference for light or dark mode.
Use `light-dark()` to specify two different color values within a single CSS property. The browser (or device) will automatically choose the appropriate color based on the element's computed `color-scheme` value. For example, with the following CSS:
  * If the user has selected a light theme, the `.target` element will have a lime background.
  * If the user has selected a dark theme, the `.target` element will have a green background.

```
html{
color-scheme:lightdark;
}
.target{
background-color:light-dark(lime,green);
}

```

### CSS picture-in-picture display mode
Adds support to the CSS [`display-mode`](https://developer.mozilla.org/docs/Web/CSS/@media/display-mode) media feature for the `picture-in-picture` value. This allows web developers to write specific CSS rules that are only applied when (part of the) the web app is shown in picture-in-picture mode.
Learn more about this media feature, in the [picture-in-picture documentation](https://developer.chrome.com/docs/web-platform/document-picture-in-picture#css_picture-in-picture_display_mode).
### align-content CSS property for blocks
The `align-content` CSS property is now supported on block containers and table cells. Previously, this property was supported only on grid and flex items. For example, `display: block`, `display: list-item`, and `display: table-cell` can now be aligned using `align-content`.
Learn more in [Support for `align-content` in block and table layouts](https://developer.chrome.com/blog/align-content).
### The `field-sizing` CSS property
Using the `field-sizing` property, developers can disable fixed default sizes of form controls, and make their size depend on their content. This provides a way to create automatically-growing text fields.
### The CSS `text-spacing-trim` property
This property applies the kerning to Chinese, Japanese, and Korean (CJK) punctuation characters to produce the visually pleasing typography as defined by JLREQ (Requirements for Japanese Text Layout) and CLREQ (Requirements for Chinese Text Layout).
Many CJK punctuation characters include glyph-internal spacing. For example, the CJK full stop and the CJK close parenthesis usually have glyph-internal spacings on the right half of their glyph spaces, to give them a constant advance as other ideographic characters. But when they appear in a row, the glyph-internal spacings become excessive. This feature adjusts such excessive spacing.
The `text-spacing-trim` property accepts one of the following four values: `normal`, `trim-start`, `space-all`, and `space-first`. Learn more in [Introducing four new international features in CSS](https://developer.chrome.com/blog/css-i18n-features#cjk_punctuation_kerning_text-spacing-trim).
## Web APIs
### Allow for WebAuthn credential creation in a cross-origin iframe
This feature allows web developers to create WebAuthn credentials (that is, "publickey" credentials, known as passkeys) in cross-origin iframes. Two conditions are required for this new ability:
  * The iframe has a `publickey-credentials-create-feature` permission policy.
  * The iframe has transient user activation.


This will allow developers to create passkeys in embedded scenarios, such as after an identity step-up flow where the Relying Party is providing a federated identity experience.
### Attribution reporting feature bundle
Chrome 123 adds trigger data customization and aggregatable value filters to the Attribution Reporting API focused on:
  * Additional API configurability for event-level reporting by supporting customization for trigger data cardinality and values.
  * Additional API configurability for summary reports by supporting filters in aggregatable values.


### Cross App and Web Attribution Measurement
Extends the Attribution Reporting API to allow attributing conversions that happen on the web to events that happen off the browser, within other applications.
The proposal here takes advantage of OS-level support for attribution. In particular, it gives the developer an option to allow events on the mobile web to be joinable with events in Android's Privacy Sandbox, although support for other platforms could also be implemented.
### `blocking=render` on inline module scripts
This is a small change that removes an artificial limitation from `<script blocking="render">`. Prior to this change, `<script blocking="render"type="module">` requires a `src` attribute, even if this `src` is a data URI. This is an unnecessary constraint, as inline module scripts that import other scripts should still be able to render-block.
The motivation for this is that cross-document view transitions often rely on render-blocking scripts for customization, so making render-blocking scripts easier to author would support this feature.
### Document picture-in-picture: allow the `focus()` API to focus the opener
You can now use [`opener.focus()`](https://developer.chrome.com/docs/web-platform/document-picture-in-picture#focus_the_opener_window) from a document picture-in-picture window to bring system-level focus to the tab that owns the document picture-in-picture window.
This allows developers to bring the original tab back to the foreground when necessary. For example, when the user needs to access a UI experience that doesn't fit in the smaller picture-in-picture window.
### Import attributes `with` syntax
Import attributes are a JavaScript feature to allow annotating import declarations, for example `import xxx from "mod" with { type: "json" }`. Chrome originally shipped a previous version of the proposal (in Chrome 91) using `assert` as the keyword. This version has then been updated to use `with` due to some changes needed while integrating it with HTML for JSON and CSS modules.
### jitterBufferTarget
The `jitterBufferTarget` attribute allows applications to specify a target duration of time in milliseconds of media for the `RTCRtpReceiver` jitter buffer to hold. This influences the amount of buffering done by the user agent, which in turn affects retransmissions and packet loss recovery. Altering the target value allows applications to control the tradeoff between playout delay and the risk of running out of audio or video frames due to network jitter.
### Long Animation Frame Timing
The [Long Animation Frames API](https://developer.chrome.com/docs/web-platform/long-animation-frames) is an extension of the [Long Tasks API](https://developer.mozilla.org/docs/Web/API/PerformanceLongTaskTiming). It measures the task together with its subsequent rendering update, adding information such as long running scripts, rendering time, and time spent in forced layout and style, known as [_layout thrashing_](https://web.dev/articles/avoid-large-complex-layouts-and-layout-thrashing).
Developers can use this as a diagnostic for "sluggishness", which is measured by [INP](https://web.dev/articles/inp), by finding the causes for main-thread congestion which is often the cause for bad INP.
### NavigationActivation
The NavigationActivation interface adds `navigation.activation`. This stores state about when the current Document was activated (for example, when it was initialized, or restored from the back/forward cache).
This means that developers can offer customized pages based on where the user navigated from. For example run a different animation if they came from the home page.
### pagereveal event
The `pagereveal` event is fired on a Document's window object at the first render opportunity after a Document is: initially loaded, restored from the back-forward cache, or activated from a prerender.
It can be used by a page author to set up a page entry experience—such as a view transition from a previous state.
### PointerEvent.deviceId for Multi-Pen Inking
As devices with advanced pen input capabilities are becoming increasingly prevalent, it is important that the web platform continues to evolve to fully support these advanced features in order to unlock rich experiences for both end users and developers. One such advancement is the ability for a device's digitizer to recognize more than one pen device interacting with it simultaneously. This feature is an extension to the `PointerEvent` interface to include a new attribute, `deviceId`, that represents a session-persistent, document isolated, unique identifier that a developer can reliably use to identify individual pens interacting with the page.
### Private network access checks for navigation requests: warning-only mode
Before website A navigates to another site B in the user's private network, this feature does the following:
  1. Checks whether the request has been initiated from a secure context.
  2. Sends a preflight request, and checks whether B responds with a header that allows private network access.


There are already features for subresources and workers, but this addition is specifically for navigation requests.
These checks are made to protect the user's private network. Since this feature is the "warning-only" mode, it won't fail the requests if any of the checks fails. Instead, a warning will be shown in DevTools, to help developers prepare for the coming enforcement.
### Sec-CH-UA-Form-Factor client hint
This hint indicates the "form-factor" of the user-agent or device, so that the site can tailor its response.
### Service Worker Static Routing API
This API allows developers to configure the routing, and allows them to offload simple things service workers do. If the condition matches, the navigation happens without starting service workers or executing JavaScript, which allows web pages to avoid performance penalties due to service worker interceptions. For more information, see [the previous blog post on this API](https://developer.chrome.com/blog/service-worker-static-routing-api-origin-trial).
### Shared Storage update
This update supports running cross origin worklets without having to create an iframe.
### zstd Content-Encoding
Zstandard, or zstd, is a data compression mechanism described in RFC8878. It is a fast lossless compression algorithm, targeting real-time compression scenarios at zlib-level and better compression ratios. The `zstd` token was added as an IANA-registered Content-Encoding token.
Adding support for `zstd` as a Content-Encoding will help load pages faster and use less bandwidth, and spend less time, CPU, and power on compression on our servers, resulting in reduced server costs.
## New origin trials
In Chrome 123 you can opt into the following new [origin trials](https://developer.chrome.com/docs/web-platform/origin-trials).
### WebAssembly JavaScript promise integration
In order to support responsive applications written using WebAssembly it is necessary to provide features that allow WebAssembly programs to be suspended and resumed.
The primary initial use case for [promise integration](https://v8.dev/blog/jspi) is to allow WebAssembly programs whose source relies on synchronous APIs to use asynchronous APIs that are increasingly common on the Web platform.
[Register for the promise integration origin trial](https://developer.chrome.com/origintrials#/view_trial/1603844417297317889).
## Removals
Chrome 123 removes the following feature.
### The `window-placement` alias for permission and permission policy `window-management`
In Chrome 111, [`window-management` was added](https://developer.chrome.com/docs/capabilities/web-apis/window-management#the_window-management_permission) as an alias for `window-placement` permission and permission-policy strings. This was part of a larger effort to rename the strings by eventually deprecating and removing `window-placement`. The terminology change improves the longevity of the descriptor as the Window Management API evolves over time.
Deprecation warnings for the `window-placement` alias began in Chrome 113, and it will now be removed.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-02-21 UTC.

