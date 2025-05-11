---
url: https://developer.chrome.com/blog/chrome-133-beta?hl=en
title: https://developer.chrome.com/blog/chrome-133-beta?hl=en
date: 2025-05-11T16:54:24.605042
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/chrome-133-beta?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/chrome-133-beta?hl=es-419)




  * On this page
  * [CSS and UI](https://developer.chrome.com/blog/chrome-133-beta?hl=en#css_and_ui)
    * [CSS advanced attr() function](https://developer.chrome.com/blog/chrome-133-beta?hl=en#css_advanced_attr_function)
    * [CSS :open pseudo-class](https://developer.chrome.com/blog/chrome-133-beta?hl=en#css_open_pseudo-class)
    * [CSS scroll state container queries](https://developer.chrome.com/blog/chrome-133-beta?hl=en#css_scroll_state_container_queries)
    * [CSS text-box, text-box-trim, and text-box-edge](https://developer.chrome.com/blog/chrome-133-beta?hl=en#css_text-box_text-box-trim_and_text-box-edge)
    * [The hint value of the popover attribute](https://developer.chrome.com/blog/chrome-133-beta?hl=en#the_hint_value_of_the_popover_attribute)
    * [Popover invoker and anchor positioning improvements](https://developer.chrome.com/blog/chrome-133-beta?hl=en#popover_invoker_and_anchor_positioning_improvements)
    * [Popover nested inside invoker shouldn't re-invoke it](https://developer.chrome.com/blog/chrome-133-beta?hl=en#popover_nested_inside_invoker_shouldnt_re-invoke_it)
  * [Web APIs](https://developer.chrome.com/blog/chrome-133-beta?hl=en#web_apis)
    * [Animation.overallProgress](https://developer.chrome.com/blog/chrome-133-beta?hl=en#animationoverallprogress)
    * [The pause() method of the Atomics object](https://developer.chrome.com/blog/chrome-133-beta?hl=en#the_pause_method_of_the_atomics_object)
    * [CSP hash reporting for scripts](https://developer.chrome.com/blog/chrome-133-beta?hl=en#csp_hash_reporting_for_scripts)
    * [DOM state-preserving move](https://developer.chrome.com/blog/chrome-133-beta?hl=en#dom_state-preserving_move)
    * [Expose attributionsrc attribute on <area>](https://developer.chrome.com/blog/chrome-133-beta?hl=en#expose_attributionsrc_attribute_on_area)
    * [Expose coarsened cross-origin renderTime in element timing and LCP (regardless of Timing-Allow-Origin)](https://developer.chrome.com/blog/chrome-133-beta?hl=en#expose_coarsened_cross-origin_rendertime_in_element_timing_and_lcp_regardless_of_timing-allow-origin)
    * [Revert responseStart and introduce firstResponseHeadersStart](https://developer.chrome.com/blog/chrome-133-beta?hl=en#revert_responsestart_and_introduce_firstresponseheadersstart)
    * [The FileSystemObserver interface](https://developer.chrome.com/blog/chrome-133-beta?hl=en#the_filesystemobserver_interface)
    * [Freezing on Energy Saver](https://developer.chrome.com/blog/chrome-133-beta?hl=en#freezing_on_energy_saver)
    * [Multiple import maps](https://developer.chrome.com/blog/chrome-133-beta?hl=en#multiple_import_maps)
    * [Storage Access Headers](https://developer.chrome.com/blog/chrome-133-beta?hl=en#storage_access_headers)
    * [Support creating ClipboardItem with Promise<DOMString>](https://developer.chrome.com/blog/chrome-133-beta?hl=en#support_creating_clipboarditem_with_promisedomstring)
    * [WebAssembly Memory64](https://developer.chrome.com/blog/chrome-133-beta?hl=en#webassembly_memory64)
    * [​​Web Authentication API: PublicKeyCredential getClientCapabilities() method](https://developer.chrome.com/blog/chrome-133-beta?hl=en#​​web_authentication_api_publickeycredential_getclientcapabilities_method)
    * [WebGPU: 1-component vertex formats (and unorm8x4-bgra)](https://developer.chrome.com/blog/chrome-133-beta?hl=en#webgpu_1-component_vertex_formats_and_unorm8x4-bgra)
    * [X25519 algorithm of the Web Cryptography API](https://developer.chrome.com/blog/chrome-133-beta?hl=en#x25519_algorithm_of_the_web_cryptography_api)
  * [New origin trials](https://developer.chrome.com/blog/chrome-133-beta?hl=en#new_origin_trials)
    * [Opt out of freezing on Energy Saver](https://developer.chrome.com/blog/chrome-133-beta?hl=en#opt_out_of_freezing_on_energy_saver)
  * [Deprecations and removals](https://developer.chrome.com/blog/chrome-133-beta?hl=en#deprecations_and_removals)
    * [Deprecate the WebGPU maxInterStageShaderComponents limit](https://developer.chrome.com/blog/chrome-133-beta?hl=en#deprecate_the_webgpu_maxinterstageshadercomponents_limit)
    * [Remove <link rel=prefetch> five-minute rule](https://developer.chrome.com/blog/chrome-133-beta?hl=en#remove_link_relprefetch_five-minute_rule)
    * [Remove Chrome Welcome page triggering with initial prefs first run tabs](https://developer.chrome.com/blog/chrome-133-beta?hl=en#remove_chrome_welcome_page_triggering_with_initial_prefs_first_run_tabs)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  Chrome 133 beta 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [CSS and UI](https://developer.chrome.com/blog/chrome-133-beta?hl=en#css_and_ui)
    * [CSS advanced attr() function](https://developer.chrome.com/blog/chrome-133-beta?hl=en#css_advanced_attr_function)
    * [CSS :open pseudo-class](https://developer.chrome.com/blog/chrome-133-beta?hl=en#css_open_pseudo-class)
    * [CSS scroll state container queries](https://developer.chrome.com/blog/chrome-133-beta?hl=en#css_scroll_state_container_queries)
    * [CSS text-box, text-box-trim, and text-box-edge](https://developer.chrome.com/blog/chrome-133-beta?hl=en#css_text-box_text-box-trim_and_text-box-edge)
    * [The hint value of the popover attribute](https://developer.chrome.com/blog/chrome-133-beta?hl=en#the_hint_value_of_the_popover_attribute)
    * [Popover invoker and anchor positioning improvements](https://developer.chrome.com/blog/chrome-133-beta?hl=en#popover_invoker_and_anchor_positioning_improvements)
    * [Popover nested inside invoker shouldn't re-invoke it](https://developer.chrome.com/blog/chrome-133-beta?hl=en#popover_nested_inside_invoker_shouldnt_re-invoke_it)
  * [Web APIs](https://developer.chrome.com/blog/chrome-133-beta?hl=en#web_apis)
    * [Animation.overallProgress](https://developer.chrome.com/blog/chrome-133-beta?hl=en#animationoverallprogress)
    * [The pause() method of the Atomics object](https://developer.chrome.com/blog/chrome-133-beta?hl=en#the_pause_method_of_the_atomics_object)
    * [CSP hash reporting for scripts](https://developer.chrome.com/blog/chrome-133-beta?hl=en#csp_hash_reporting_for_scripts)
    * [DOM state-preserving move](https://developer.chrome.com/blog/chrome-133-beta?hl=en#dom_state-preserving_move)
    * [Expose attributionsrc attribute on <area>](https://developer.chrome.com/blog/chrome-133-beta?hl=en#expose_attributionsrc_attribute_on_area)
    * [Expose coarsened cross-origin renderTime in element timing and LCP (regardless of Timing-Allow-Origin)](https://developer.chrome.com/blog/chrome-133-beta?hl=en#expose_coarsened_cross-origin_rendertime_in_element_timing_and_lcp_regardless_of_timing-allow-origin)
    * [Revert responseStart and introduce firstResponseHeadersStart](https://developer.chrome.com/blog/chrome-133-beta?hl=en#revert_responsestart_and_introduce_firstresponseheadersstart)
    * [The FileSystemObserver interface](https://developer.chrome.com/blog/chrome-133-beta?hl=en#the_filesystemobserver_interface)
    * [Freezing on Energy Saver](https://developer.chrome.com/blog/chrome-133-beta?hl=en#freezing_on_energy_saver)
    * [Multiple import maps](https://developer.chrome.com/blog/chrome-133-beta?hl=en#multiple_import_maps)
    * [Storage Access Headers](https://developer.chrome.com/blog/chrome-133-beta?hl=en#storage_access_headers)
    * [Support creating ClipboardItem with Promise<DOMString>](https://developer.chrome.com/blog/chrome-133-beta?hl=en#support_creating_clipboarditem_with_promisedomstring)
    * [WebAssembly Memory64](https://developer.chrome.com/blog/chrome-133-beta?hl=en#webassembly_memory64)
    * [​​Web Authentication API: PublicKeyCredential getClientCapabilities() method](https://developer.chrome.com/blog/chrome-133-beta?hl=en#​​web_authentication_api_publickeycredential_getclientcapabilities_method)
    * [WebGPU: 1-component vertex formats (and unorm8x4-bgra)](https://developer.chrome.com/blog/chrome-133-beta?hl=en#webgpu_1-component_vertex_formats_and_unorm8x4-bgra)
    * [X25519 algorithm of the Web Cryptography API](https://developer.chrome.com/blog/chrome-133-beta?hl=en#x25519_algorithm_of_the_web_cryptography_api)
  * [New origin trials](https://developer.chrome.com/blog/chrome-133-beta?hl=en#new_origin_trials)
    * [Opt out of freezing on Energy Saver](https://developer.chrome.com/blog/chrome-133-beta?hl=en#opt_out_of_freezing_on_energy_saver)
  * [Deprecations and removals](https://developer.chrome.com/blog/chrome-133-beta?hl=en#deprecations_and_removals)
    * [Deprecate the WebGPU maxInterStageShaderComponents limit](https://developer.chrome.com/blog/chrome-133-beta?hl=en#deprecate_the_webgpu_maxinterstageshadercomponents_limit)
    * [Remove <link rel=prefetch> five-minute rule](https://developer.chrome.com/blog/chrome-133-beta?hl=en#remove_link_relprefetch_five-minute_rule)
    * [Remove Chrome Welcome page triggering with initial prefs first run tabs](https://developer.chrome.com/blog/chrome-133-beta?hl=en#remove_chrome_welcome_page_triggering_with_initial_prefs_first_run_tabs)


Rachel Andrew 
[ GitHub ](https://github.com/rachelandrew) [ LinkedIn ](https://www.linkedin.com/in/rachelandrew) [ Mastodon ](https://front-end.social/@rachelandrew) [ Bluesky ](https://bsky.app/profile/rachelandrew.bsky.social) [ Homepage ](https://rachelandrew.co.uk)
Published: January 15, 2024 
Unless otherwise noted, the following changes apply to the newest Chrome beta channel release for Android, ChromeOS, Linux, macOS, and Windows. Learn more about the features listed here through the provided links or from the list on ChromeStatus.com. Chrome 133 is beta as of January 15, 2024. You can download the latest on [Google.com](https://www.google.com/chrome/beta/) for desktop or on Google Play Store on Android.
## CSS and UI
This release adds seven new CSS and UI features.
### CSS advanced `attr()` function
Implements the augmentation to `attr()` specified in CSS Level 5, which allows types besides `<string>` and use in all CSS properties (in addition to the existing support for the pseudo-element `content`).
Find out more in [CSS `attr()` gets an upgrade](https://developer.chrome.com/blog/advanced-attr).
### CSS `:open` pseudo-class
The `:open` pseudo-class matches `<dialog>` and `<details>` when they are in their open state, and matches `<select>` and `<input>` when they are in modes which have a picker and the picker is showing.
### CSS scroll state container queries
Use container queries to style descendants of containers based on their scroll state.
The query container is either a scroll container, or an element affected by the scroll position of a scroll container. The following states can be queried:
  * `stuck`: A sticky positioned container is stuck to one of the edges of the scroll box.
  * `snapped`: A scroll snap aligned container is currently snapped horizontally or vertically.
  * `scrollable`: Whether a scroll container can be scrolled in a queried direction.


A new `container-type: scroll-state` lets containers be queried.
```
#sticky{
position:sticky;
container-type:scroll-state;
}
@containerscroll-state(stuck:top){
#sticky-child{
font-size:75%;
}
}

```

Learn more in [CSS `scroll-state()`](https://developer.chrome.com/blog/css-scroll-state-queries).
### CSS `text-box`, `text-box-trim`, and `text-box-edge`
To achieve optimal balance of text content, the `text-box-trim` and `text-box-edge` properties, along with the `text-box` shorthand property, make finer control of vertical alignment of text possible.
The `text-box-trim` property specifies the sides to trim, above or below, and the `text-box-edge` property specifies how the edge should be trimmed.
These properties let you control vertical spacing precisely by using the font metrics. Find out more in [CSS text-box-trim](https://developer.chrome.com/blog/css-text-box-trim).
### The `hint` value of the `popover` attribute
The Popover API specifies the behavior for two values of the `popover` attribute: `auto` and `manual`. This feature describes a third value, `popover=hint`. Hints, which are most often associated with "tooltip" type behaviors, have slightly different behaviors. Primarily, the difference is that a `hint` is subordinate to `auto` when opening nested stacks of popovers. So it is possible to open an unrelated `hint` popover while an existing stack of `auto` popovers stays open.
The canonical example is that a `<select>` picker is open (`popover=auto`) and a hover-triggered tooltip (`popover=hint`) is shown. That action does not close the `<select>` picker.
### Popover invoker and anchor positioning improvements
Adds an imperative way to set invoker relationships between popovers with `popover.showPopover({source})`. Enables invoker relationships to create implicit anchor element references.
### Popover nested inside invoker shouldn't re-invoke it
In the following case clicking the button properly activates the popover, however, clicking on the popover itself after that should not close the popover.
```
<button popovertarget=foo>Activate
 <div popover id=foo>Clicking me shouldn't close me</div>
</button>

```

Previously this happened, because the popover click bubbles to the `<button>` and activates the invoker, which toggles the popover closed. This has now been changed to the expected behavior.
## Web APIs
### `Animation.overallProgress`
Provides developers with a convenient and consistent representation of how far along an animation has advanced across its iterations and regardless of the nature of its timeline. Without the `overallProgress` property, you need to manually compute how far an animation has advanced, factoring in the number of iterations of the animation and whether the `currentTime` of the animation is a percentage of total time (as in the case of scroll-driven animations) or an absolute time quantity (as in the case of time-driven animations).
### The `pause()` method of the `Atomics` object
Adds the `pause()` method to the `Atomics` namespace object, to hint the CPU that the current code is executing a spinlock.
### CSP hash reporting for scripts
Complex web applications often need to keep track of the subresources that they download, for security purposes.
In particular, upcoming industry standards and best practices (for example, PCI-DSS v4) require that web applications keep an inventory of all the scripts they download and execute.
This feature builds on CSP and the Reporting API to report the URLs and hashes (for CORS/same-origin) of all the script resources that the document loads.
### DOM state-preserving move
Adds a DOM primitive (`Node.prototype.moveBefore`) that lets you move elements around a DOM tree, without resetting the element's state.
When moving instead of removing and inserting, following state such as the following is preserved:
  * `<iframe>` elements remain loaded.
  * The active element remains focus.
  * Popovers, fullscreen, and modal dialogs remain open.
  * CSS transitions and animations continue.


### Expose `attributionsrc` attribute on `<area>`
Aligns exposure of the `attributionsrc` attribute on `<area>` with the existing processing behavior of the attribute, even when it wasn't exposed.
Additionally, it makes sense to support the attribute on `<area>`, as that element is a first-class navigation surface, and Chrome already supports this on the other surfaces of `<a>` and `window.open`
### Expose coarsened cross-origin `renderTime` in element timing and LCP (regardless of `Timing-Allow-Origin`)
Element timing and LCP entries have a `renderTime` attribute, aligned with the first frame in which an image or text was painted.
This attribute is currently guarded for cross-origin images by requiring a `Timing-Allow-Origin` header on the image resource. However, that restriction is easy to work around (for example, by displaying a same-origin and cross-origin image in the same frame).
Since this has been a source of confusion, we instead plan to remove this restriction, and instead coarsen all render times by 4 ms when the document is not cross-origin-isolated. This is seemingly coarse enough to avoid leaking any useful decoding-time information about cross-origin images.
### Revert `responseStart` and introduce `firstResponseHeadersStart`
With [103 Early Hints](https://developer.chrome.com/docs/web-platform/early-hints) enabled, responses have two timestamps:
  * When the Early Hints arrive (103)
  * When the final headers arrive (e.g. 200)


When Chrome 115 shipped [`firstInterimResponseStart`](https://chromestatus.com/feature/5086730938482688) to allow measuring of these two timestamps, we also changed the meaning of `responseStart` (used by [Time to First Byte (TTFB)](https://web.dev/articles/ttfb)) to mean "the final headers". This created a web compatibility issue with browsers and tools that did not make a similar change for this commonly used metric.
Chrome 133 reverts this `responseStart` change to resolve this compatibility issue and instead introduces `firstResponseHeadersStart` to allow sites to measure the time to the final headers, while retaining the original definition of TTFB.
### The `FileSystemObserver` interface
The [`FileSystemObserver` interface](https://developer.chrome.com/blog/file-system-observer) notifies websites of changes to the file system. Sites observe changes to files and directories, to which the user has previously granted permission, in the user's local device, or in the Bucket File System (also known as the Origin Private File System), and are notified of basic change info, such as the change type.
### Freezing on Energy Saver
When Energy Saver is active, Chrome will freeze a "browsing context group" that has been hidden and silent for over five minutes if any subgroup of same-origin frames within it exceeds a CPU usage threshold, unless it:
  * Provides audio- or video-conferencing functionality (detected by identifying microphone, camera or screen/window/tab capture or an RTCPeerConnection with an 'open' RTCDataChannel or a 'live' MediaStreamTrack).
  * Controls an external device (detected with use of WebUSB, Web Bluetooth, WebHID, or Web Serial).
  * Holds a Web Lock or an IndexedDB connection that blocks a version update or a transaction on a different connection.


Freezing consists of pausing execution. It is formally defined in the Page Lifecycle API.
The CPU usage threshold will be calibrated to freeze approximately 10% of background tabs when Energy Saver is active.
### Multiple import maps
Import maps currently have to load before any ES module and there can only be a single import map per document. That makes them fragile and potentially slow to use in real-life scenarios: Any module that loads before them breaks the entire app, and in apps with many modules they become a large blocking resource, as the entire map for all possible modules needs to load first.
This feature enables multiple import maps per document, by merging them in a consistent and deterministic way.
### Storage Access Headers
Offers an alternate way for authenticated embeds to opt in for unpartitioned cookies. These headers indicate whether unpartitioned cookies are (or can be) included in a given network request, and allow servers to activate 'storage-access' permissions they have already been granted. Giving an alternative way to activate the 'storage-access' permission allows usage by non-iframe resources, and can reduce latency for authenticated embeds.
### Support creating `ClipboardItem` with `Promise<DOMString>`
The `ClipboardItem`, which is the input to the async clipboard `write()` method, now accepts string values in addition to Blobs in its constructor. `ClipboardItemData` can be a Blob, a string, or a Promise that resolves to either a Blob or a string.
### WebAssembly Memory64
The [memory64 proposal](https://github.com/WebAssembly/memory64/blob/main/proposals/memory64/Overview.md) adds support for linear WebAssembly memories with size larger than 2^32 bits. It provides no new instructions, but instead extends the existing instructions to allow 64-bit indexes for memories and tables.
### ​​Web Authentication API: PublicKeyCredential `getClientCapabilities()` method
The PublicKeyCredential `getClientCapabilities()` method lets you determine which WebAuthn features are supported by the user's client. The method returns a list of supported capabilities, allowing developers to tailor authentication experiences and workflows based on the client's specific functionality.
### WebGPU: 1-component vertex formats (and unorm8x4-bgra)
Adds additional vertex formats not present in the initial release of WebGPU due to lack of support or old macOS versions (which are no longer supported by any browser). The 1-component vertex formats let applications request only the necessary data when previously they had to request at least two times more for 8 and 16-bit data types. The unorm8x4-bgra format makes it slightly more convenient to load BGRA-encoded vertex colors while keeping the same shader.
### X25519 algorithm of the Web Cryptography API
The "X25519" algorithm provides tools to perform key agreement using the X25519 function specified in [RFC7748]. The "X25519" algorithm identifier can be used in the SubtleCrypto interface to access the implemented operations: generateKey, importKey, exportKey, deriveKey and deriveBits.
## New origin trials
In Chrome 133 you can opt into the following new [origin trials](https://developer.chrome.com/docs/web-platform/origin-trials).
### Opt out of freezing on Energy Saver
This opt out trial lets sites opt out from the freezing on Energy Saver behavior that ships in Chrome 133.
## Deprecations and removals
This version of Chrome introduces the deprecations and removals listed below. Visit ChromeStatus.com for lists of planned deprecations, current deprecations and previous removals.
This release of Chrome deprecates one feature.
### Deprecate the WebGPU `maxInterStageShaderComponents` limit
The `maxInterStageShaderComponents limit` is deprecated due to a combination of factors. The intended removal date in Chrome 135.
  * Redundancy with `maxInterStageShaderVariables`: This limit already serves a similar purpose, controlling the amount of data passed between shader stages.
  * Minor discrepancies: While there are slight differences in how the two limits are calculated, these differences are minor and can be effectively managed within the `maxInterStageShaderVariables` limit.
  * Simplification: Removing `maxInterStageShaderComponents` streamlines the shader interface and reduces complexity for developers. Instead of managing two separate limits with subtle differences, they can focus on the more appropriately named and comprehensive `maxInterStageShaderVariables`.


This release of Chrome removes two features.
### Remove `<link rel=prefetch>` five-minute rule
Previously, when a resource was prefetched using `<link rel=prefetch>`, Chrome ignored its cache semantics (namely `max-age` and `no-cache`) for the first use within five minutes, to avoid refetching. Now, Chrome removes this special case and uses normal HTTP cache semantics.
This means web developers need to include appropriate caching headers (Cache-Control or Expires) to see benefits from `<link rel=prefetch>`.
This also affects the nonstandard `<link rel=prerender>`.
### Remove Chrome Welcome page triggering with initial prefs first run tabs
Including `chrome://welcome` in the `first_run_tabs` property of the `initial_preferences` file will now have no effect. This is removed because that page is redundant with the First Run Experience that triggers on desktop platforms.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-01-15 UTC.

