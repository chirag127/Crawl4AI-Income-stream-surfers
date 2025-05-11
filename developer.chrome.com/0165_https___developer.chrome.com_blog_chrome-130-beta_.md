---
url: https://developer.chrome.com/blog/chrome-130-beta?hl=en
title: https://developer.chrome.com/blog/chrome-130-beta?hl=en
date: 2025-05-11T16:54:16.933141
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/chrome-130-beta?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/chrome-130-beta?hl=es-419)




  * On this page
  * [CSS](https://developer.chrome.com/blog/chrome-130-beta?hl=en#css)
    * [CSS Container Queries flat tree lookup](https://developer.chrome.com/blog/chrome-130-beta?hl=en#css_container_queries_flat_tree_lookup)
    * [CSS Nesting: The nested declarations rule](https://developer.chrome.com/blog/chrome-130-beta?hl=en#css_nesting_the_nested_declarations_rule)
    * [Full and unprefixed box-decoration-break support](https://developer.chrome.com/blog/chrome-130-beta?hl=en#full_and_unprefixed_box-decoration-break_support)
    * [Allow more pseudo-elements and pseudo-classes after ::part()](https://developer.chrome.com/blog/chrome-130-beta?hl=en#allow_more_pseudo-elements_and_pseudo-classes_after_part)
  * [Web APIs](https://developer.chrome.com/blog/chrome-130-beta?hl=en#web_apis)
    * [Attribution Reporting API feature (Attribution Scopes)](https://developer.chrome.com/blog/chrome-130-beta?hl=en#attribution_reporting_api_feature_attribution_scopes)
    * [Attribution Reporting API feature (debug key privacy improvement)](https://developer.chrome.com/blog/chrome-130-beta?hl=en#attribution_reporting_api_feature_debug_key_privacy_improvement)
    * [Compression dictionary transport with shared Brotli and shared Zstandard](https://developer.chrome.com/blog/chrome-130-beta?hl=en#compression_dictionary_transport_with_shared_brotli_and_shared_zstandard)
    * [Concurrent smooth scrollIntoView()](https://developer.chrome.com/blog/chrome-130-beta?hl=en#concurrent_smooth_scrollintoview)
    * [Document picture-in-picture: add option to ignore window bounds cache](https://developer.chrome.com/blog/chrome-130-beta?hl=en#document_picture-in-picture_add_option_to_ignore_window_bounds_cache)
    * [Improved error reporting in IndexedDB for large value read failures](https://developer.chrome.com/blog/chrome-130-beta?hl=en#improved_error_reporting_in_indexeddb_for_large_value_read_failures)
    * [Keyboard focusable scroll containers](https://developer.chrome.com/blog/chrome-130-beta?hl=en#keyboard_focusable_scroll_containers)
    * [Protected Audience Bidding and Auction Services](https://developer.chrome.com/blog/chrome-130-beta?hl=en#protected_audience_bidding_and_auction_services)
    * [Support non-special scheme URLs](https://developer.chrome.com/blog/chrome-130-beta?hl=en#support_non-special_scheme_urls)
    * [WebAssembly JavaScript String Builtins](https://developer.chrome.com/blog/chrome-130-beta?hl=en#webassembly_javascript_string_builtins)
    * [WebGPU: Dual source blending](https://developer.chrome.com/blog/chrome-130-beta?hl=en#webgpu_dual_source_blending)
    * [Web Serial: connected attribute and RFCOMM connection events](https://developer.chrome.com/blog/chrome-130-beta?hl=en#web_serial_connected_attribute_and_rfcomm_connection_events)
  * [Origin trials in progress](https://developer.chrome.com/blog/chrome-130-beta?hl=en#origin_trials_in_progress)
    * [Language Detector API](https://developer.chrome.com/blog/chrome-130-beta?hl=en#language_detector_api)
    * [WebAuthn attestationFormats](https://developer.chrome.com/blog/chrome-130-beta?hl=en#webauthn_attestationformats)
  * [Deprecations and removals](https://developer.chrome.com/blog/chrome-130-beta?hl=en#deprecations_and_removals)
    * [Remove expectedImprovement in DelegatedInkTrailPresenter](https://developer.chrome.com/blog/chrome-130-beta?hl=en#remove_expectedimprovement_in_delegatedinktrailpresenter)
    * [Deprecate non-standard GPUAdapter requestAdapterInfo() method](https://developer.chrome.com/blog/chrome-130-beta?hl=en#deprecate_non-standard_gpuadapter_requestadapterinfo_method)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  Chrome 130 beta 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [CSS](https://developer.chrome.com/blog/chrome-130-beta?hl=en#css)
    * [CSS Container Queries flat tree lookup](https://developer.chrome.com/blog/chrome-130-beta?hl=en#css_container_queries_flat_tree_lookup)
    * [CSS Nesting: The nested declarations rule](https://developer.chrome.com/blog/chrome-130-beta?hl=en#css_nesting_the_nested_declarations_rule)
    * [Full and unprefixed box-decoration-break support](https://developer.chrome.com/blog/chrome-130-beta?hl=en#full_and_unprefixed_box-decoration-break_support)
    * [Allow more pseudo-elements and pseudo-classes after ::part()](https://developer.chrome.com/blog/chrome-130-beta?hl=en#allow_more_pseudo-elements_and_pseudo-classes_after_part)
  * [Web APIs](https://developer.chrome.com/blog/chrome-130-beta?hl=en#web_apis)
    * [Attribution Reporting API feature (Attribution Scopes)](https://developer.chrome.com/blog/chrome-130-beta?hl=en#attribution_reporting_api_feature_attribution_scopes)
    * [Attribution Reporting API feature (debug key privacy improvement)](https://developer.chrome.com/blog/chrome-130-beta?hl=en#attribution_reporting_api_feature_debug_key_privacy_improvement)
    * [Compression dictionary transport with shared Brotli and shared Zstandard](https://developer.chrome.com/blog/chrome-130-beta?hl=en#compression_dictionary_transport_with_shared_brotli_and_shared_zstandard)
    * [Concurrent smooth scrollIntoView()](https://developer.chrome.com/blog/chrome-130-beta?hl=en#concurrent_smooth_scrollintoview)
    * [Document picture-in-picture: add option to ignore window bounds cache](https://developer.chrome.com/blog/chrome-130-beta?hl=en#document_picture-in-picture_add_option_to_ignore_window_bounds_cache)
    * [Improved error reporting in IndexedDB for large value read failures](https://developer.chrome.com/blog/chrome-130-beta?hl=en#improved_error_reporting_in_indexeddb_for_large_value_read_failures)
    * [Keyboard focusable scroll containers](https://developer.chrome.com/blog/chrome-130-beta?hl=en#keyboard_focusable_scroll_containers)
    * [Protected Audience Bidding and Auction Services](https://developer.chrome.com/blog/chrome-130-beta?hl=en#protected_audience_bidding_and_auction_services)
    * [Support non-special scheme URLs](https://developer.chrome.com/blog/chrome-130-beta?hl=en#support_non-special_scheme_urls)
    * [WebAssembly JavaScript String Builtins](https://developer.chrome.com/blog/chrome-130-beta?hl=en#webassembly_javascript_string_builtins)
    * [WebGPU: Dual source blending](https://developer.chrome.com/blog/chrome-130-beta?hl=en#webgpu_dual_source_blending)
    * [Web Serial: connected attribute and RFCOMM connection events](https://developer.chrome.com/blog/chrome-130-beta?hl=en#web_serial_connected_attribute_and_rfcomm_connection_events)
  * [Origin trials in progress](https://developer.chrome.com/blog/chrome-130-beta?hl=en#origin_trials_in_progress)
    * [Language Detector API](https://developer.chrome.com/blog/chrome-130-beta?hl=en#language_detector_api)
    * [WebAuthn attestationFormats](https://developer.chrome.com/blog/chrome-130-beta?hl=en#webauthn_attestationformats)
  * [Deprecations and removals](https://developer.chrome.com/blog/chrome-130-beta?hl=en#deprecations_and_removals)
    * [Remove expectedImprovement in DelegatedInkTrailPresenter](https://developer.chrome.com/blog/chrome-130-beta?hl=en#remove_expectedimprovement_in_delegatedinktrailpresenter)
    * [Deprecate non-standard GPUAdapter requestAdapterInfo() method](https://developer.chrome.com/blog/chrome-130-beta?hl=en#deprecate_non-standard_gpuadapter_requestadapterinfo_method)


Rachel Andrew 
[ GitHub ](https://github.com/rachelandrew) [ LinkedIn ](https://www.linkedin.com/in/rachelandrew) [ Mastodon ](https://front-end.social/@rachelandrew) [ Bluesky ](https://bsky.app/profile/rachelandrew.bsky.social) [ Homepage ](https://rachelandrew.co.uk)
Published: September 18, 2024 
Unless otherwise noted, the following changes apply to the newest Chrome beta channel release for Android, ChromeOS, Linux, macOS, and Windows. Learn more about the features listed here through the provided links or from the list on ChromeStatus.com. Chrome 130 is beta as of September 18, 2024. You can download the latest on [Google.com](https://www.google.com/chrome/beta/) for desktop or on Google Play Store on Android.
## CSS
This release adds four new CSS features.
### CSS Container Queries flat tree lookup
The specification for container queries changed to look up flat tree ancestors. This change is only relevant for shadow DOM where an element will now be able to see non-named containers inside shadow trees into which the element or one of its ancestors are slotted, even if the CSS rule does not use `::part()` or `::slotted()`.
### CSS Nesting: The nested declarations rule
Keeps bare declarations following a nested rule in their place, by wrapping those declarations in `CSSNestedDeclarations` rules during parsing.
### Full and unprefixed box-decoration-break support
Adds support for `box-decoration-break: clone` both for inline fragmentation (line layout) and block fragmentation (pagination for printing and multicol).
Previously in Chrome, only `box-decoration-break:slice` (the initial value) was supported for block fragmentation, whereas for inline fragmentation,`box-decoration-break:clone` was also supported, but only when using the prefixed `-webkit-box-decoration-break` property.
### Allow more pseudo-elements and pseudo-classes after `::part()`
CSS selectors that use the `::part()` pseudo-element are allowed to have other CSS pseudo-elements (except `::part()`) and many types of other CSS pseudo-classes after them. Combinators are still not allowed after `::part()`, and pseudo-classes that depend on tree structure are not allowed.
Previously Chrome only allowed a limited set of pseudo-classes and pseudo-elements after `::part()`. This change allows all of the pseudo-classes and pseudo-elements that should be allowed. It means selectors such as `::part(part-name):enabled` and `::part(part-name)::marker` are now allowed.
## Web APIs
### Attribution Reporting API feature (Attribution Scopes)
This change is based on ad tech feedback and the need for more fine grained filtering controls before the attribution process takes place. It lets API callers specify a field called "attribution scopes" which will be used for filtering before starting the regular attribution flow. This allows API callers more fine grained control over the attribution granularity and the ability to receive proper attribution reports when there are multiple different advertisers or campaigns that all convert on the same destination site.
### Attribution Reporting API feature (debug key privacy improvement)
This change helps to mitigate a potential privacy gap with debug keys.
Currently the API allows a source debug key or a trigger debug key to be specified if third-party cookies are available and can be set by API callers. If either a source or trigger debug key is specified then it will be included in the attribution report. This may lead to a privacy leak if third-party cookies are only allowed on either the publisher or the advertiser site but not both.
This change mitigates this issue by enforcing that source debug keys and trigger debug keys are only included in the attribution report if they're present on both the source and trigger, which would mean that third-party cookies were available on both the publisher and advertiser site. This change will apply to both event-level reports and aggregatable reports.
### Compression dictionary transport with shared Brotli and shared Zstandard
This feature adds support for using designated previous responses, as an external dictionary for content encoding compressing responses with Brotli or Zstandard.
Enterprises might experience potential compatibility issues with enterprise network infrastructure that intercepts HTTPS traffic and is sensitive to unknown content encodings. The enterprise policy `CompressionDictionaryTransportEnabled` is available to turn off the compression dictionary transport feature.
### Concurrent smooth `scrollIntoView()`
The [`scrollIntoView()`](https://developer.mozilla.org/docs/Web/API/Element/scrollIntoView) method with `behavior: "smooth"` lets developers create scroll containers that scroll to their descendants with a gentle scroll animation. This feature fixes Chrome's implementation of the API so that ongoing `scrollIntoView` animations are not canceled by unrelated scrolls on other scroll containers.
The feature also fixes cases where Chrome fails to scroll to a page's fragment anchor because of a competing `scrollIntoView` that is invoked when the page loads.
### Document picture-in-picture: add option to ignore window bounds cache
This adds a new parameter (`preferInitialWindowPlacement`) to the document picture-in-picture API that, when set to true, hints to the user agent that it shouldn't try to reuse the position or size of the previous document picture-in-picture from this site when opening this one.
Often, a document picture-in-picture window will close and re-open multiple times for the same site, such as moving a video conference to and from PiP. The user agent is free to re-open the PiP window at its most recent size and location, so that it stays where the user last moved it and provides continuity between the PiP windows. However, if the new window is semantically unrelated to the previous window, such as if it is a new video call, then the developer can use this parameter to provide a hint to the user agent that this window might be better opened in its default position and size instead.
Learn about how to [open the window in its default position and size](https://developer.chrome.com/docs/web-platform/document-picture-in-picture#open_the_picture-in-picture_window_in_its_default_position_and_size).
### Improved error reporting in IndexedDB for large value read failures
Change to reporting for certain error cases that were previously reported with a `DOMException` and the message "Failed to read large IndexedDB value".
Chrome will now raise a `DOMException` with the name `"NotFoundError"` when the file containing the data being read by an IDBRequest is missing from the disk so that sites can take the appropriate corrective action when an unrecoverable failure occurs. Corrective actions could include deleting the entry from the DB, notifying the user, or re-fetching the data from servers.
### Keyboard focusable scroll containers
This feature makes scrollers without focusable children keyboard-focusable by default.
This is an important improvement to help make scrollers and contents within scrollers more accessible to all users. You can read more about its benefits in [Keyboard focusable scrollers](https://developer.chrome.com/blog/keyboard-focusable-scrollers). Keyboard focusable scrollers will be enabled by default starting in Chrome 130. If websites need time to adjust to this new feature, there are a few options:
  * The [ Keyboard focusable scrollers opt out deprecation trial](https://developer.chrome.com/origintrials#/view_trial/2455024746870341633) can be used to opt back out of the feature for a limited time on a given site. This can be used through Chrome 132, ending March 18, 2025.
  * The [`KeyboardFocusableScrollersEnabled enterprise policy`](https://chromeenterprise.google/policies/#KeyboardFocusableScrollersEnabled) available from Chrome 127 can be used for the same purpose.


### Protected Audience Bidding and Auction Services
The Protected Audience API (formerly known as FLEDGE) is a Privacy Sandbox proposal to serve remarketing and custom audience use cases, designed so third parties cannot track user browsing behavior across sites.
This feature, Protected Audience Bidding and Auction Services, outlines a way to allow Protected Audience computation to take place on cloud servers in a trusted execution environment, rather than running locally on a user's device. Moving computations to cloud servers can help optimize the Protected Audience auction, to free up computational cycles and network bandwidth for a device.
### Support non-special scheme URLs
Previously, Chrome's URL parser didn't support non-special URLs. The parser parses non-special URLs as if they had an "opaque path", which is not aligned with the URL Standard. Now, Chromium's URL parser parses non-special URLs correctly, following the URL Standard.
See [bit.ly/url-non-special](http://bit.ly/url-non-special) for more details.
### WebAssembly JavaScript String Builtins
This feature exposes common JavaScript string operations for import into WebAssembly. This lets you create and manipulate JavaScript strings from WebAssembly without support within WebAssembly. This still allows for a similar performance as supported string references.
### WebGPU: Dual source blending
Adds the optional GPU feature "dual-source-blending" that enables combining two fragment shader outputs into a single framebuffer. This technique is particularly useful for applications that require complex blending operations, such as those based on Porter-Duff blend modes. By reducing the need for frequent pipeline state object changes, dual source blending can enhance performance and flexibility.
### Web Serial: `connected` attribute and RFCOMM connection events
This feature adds a boolean `SerialPort.connected` attribute. The attribute returns `true` if the serial port is logically connected. For wired serial ports, a port is logically connected if the port is physically attached to the system. For wireless serial ports, a port is logically connected if the device hosting the port has any open connections to the host.
Previously, only wired serial ports dispatched connect and disconnect events. With this feature, Bluetooth RFCOMM serial ports will dispatch these events when the port becomes logically connected or disconnected.
This feature is intended to allow applications to detect when a Bluetooth RFCOMM serial port is available without opening the port.
Learn more in [Bluetooth RFCOMM updates in Web Serial](https://developer.chrome.com/blog/bluetooth-rfcomm-updates-web-serial).
## Origin trials in progress
In Chrome 130 you can opt into the following new [origin trials](https://developer.chrome.com/docs/web-platform/origin-trials).
### Language Detector API
A JavaScript API for [detecting the language of text](https://developer.chrome.com/blog/august2024-language-detection), with confidence levels.
### WebAuthn attestationFormats
Support the `attestationFormats` field from WebAuthn level 3.
WebAuthn Level 3 supports a site expressing an ordered preference for credential attestation formats in the new `attestationFormats` field. This feature enables support for this on Android, where multiple formats can be supported by passkey providers.
[Register for the WebAuthn attestationFormats trial.](https://developer.chrome.com/origintrials#/view_trial/1428204031829868545)
## Deprecations and removals
This version of Chrome introduces the following deprecations and removals. Visit [ChromeStatus.com](https://chromestatus.com) for lists of planned deprecations, current deprecations and previous removals.
This release of Chrome removes one feature.
### Remove `expectedImprovement` in `DelegatedInkTrailPresenter`
The `expectedImprovement` attribute tells web developers how much improvement the DelegatedInkTrails API will provide to their current ink latency. However, this attribute is not worth the increase to fingerprinting entropy.
This release of Chrome deprecates one feature.
### Deprecate non-standard GPUAdapter `requestAdapterInfo()` method
The `requestAdapterInfo()` asynchronous method in WebGPU is redundant because developers can already get `GPUAdapterInfo` synchronously using the `GPUAdapter` `info` attribute.
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-09-18 UTC.

