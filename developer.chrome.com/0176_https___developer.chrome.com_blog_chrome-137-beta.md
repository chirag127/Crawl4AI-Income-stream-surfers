---
url: https://developer.chrome.com/blog/chrome-137-beta
title: https://developer.chrome.com/blog/chrome-137-beta
date: 2025-05-11T16:54:26.629697
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/chrome-137-beta#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/chrome-137-beta?hl=es-419)




  * On this page
  * [CSS and UI](https://developer.chrome.com/blog/chrome-137-beta#css_and_ui)
    * [The if() function](https://developer.chrome.com/blog/chrome-137-beta#the_if_function)
    * [The reading-flow and reading-order properties](https://developer.chrome.com/blog/chrome-137-beta#the_reading-flow_and_reading-order_properties)
    * [offset-path: shape()](https://developer.chrome.com/blog/chrome-137-beta#offset-path_shape)
    * [Support transform attribute on SVGSVGElement](https://developer.chrome.com/blog/chrome-137-beta#support_transform_attribute_on_svgsvgelement)
    * [Allow <use> to reference an external document's root element by omitting the fragment.](https://developer.chrome.com/blog/chrome-137-beta#allow_use_to_reference_an_external_documents_root_element_by_omitting_the_fragment)
    * [System accent color for accent-color property expanded to Windows and ChromeOS](https://developer.chrome.com/blog/chrome-137-beta#system_accent_color_for_accent-color_property_expanded_to_windows_and_chromeos)
    * [view-transition-name: match-element](https://developer.chrome.com/blog/chrome-137-beta#view-transition-name_match-element)
  * [Web APIs](https://developer.chrome.com/blog/chrome-137-beta#web_apis)
    * [Align error type thrown for 'payment' WebAuthn credential creation](https://developer.chrome.com/blog/chrome-137-beta#align_error_type_thrown_for_payment_webauthn_credential_creation)
    * [Blob URL Partitioning: Fetching/Navigation](https://developer.chrome.com/blog/chrome-137-beta#blob_url_partitioning_fetchingnavigation)
    * [Call stacks in crash reports from unresponsive web pages](https://developer.chrome.com/blog/chrome-137-beta#call_stacks_in_crash_reports_from_unresponsive_web_pages)
    * [Canvas Floating Point Color Types](https://developer.chrome.com/blog/chrome-137-beta#canvas_floating_point_color_types)
    * [Disallow non-trustworthy plaintext HTTP prerendering](https://developer.chrome.com/blog/chrome-137-beta#disallow_non-trustworthy_plaintext_http_prerendering)
    * [Document-Isolation-Policy](https://developer.chrome.com/blog/chrome-137-beta#document-isolation-policy)
    * [Ed25519 in Web Cryptography](https://developer.chrome.com/blog/chrome-137-beta#ed25519_in_web_cryptography)
    * [IP address logging and reporting](https://developer.chrome.com/blog/chrome-137-beta#ip_address_logging_and_reporting)
    * [JavaScript Promise Integration](https://developer.chrome.com/blog/chrome-137-beta#javascript_promise_integration)
    * [Language Detector API](https://developer.chrome.com/blog/chrome-137-beta#language_detector_api)
    * [Restrict float attributes and arguments on SVGMatrix, SVGRect, and SVGPoint](https://developer.chrome.com/blog/chrome-137-beta#restrict_float_attributes_and_arguments_on_svgmatrix_svgrect_and_svgpoint)
    * [Selection API getComposedRanges and direction](https://developer.chrome.com/blog/chrome-137-beta#selection_api_getcomposedranges_and_direction)
    * [Web app scope extensions](https://developer.chrome.com/blog/chrome-137-beta#web_app_scope_extensions)
    * [WebAssembly Branch Hints](https://developer.chrome.com/blog/chrome-137-beta#webassembly_branch_hints)
    * [WebGPU: GPUTextureView for externalTexture binding](https://developer.chrome.com/blog/chrome-137-beta#webgpu_gputextureview_for_externaltexture_binding)
    * [WebGPU: copyBufferToBuffer overload](https://developer.chrome.com/blog/chrome-137-beta#webgpu_copybuffertobuffer_overload)
  * [New origin trials](https://developer.chrome.com/blog/chrome-137-beta#new_origin_trials)
    * [Full frame rate render blocking attribute](https://developer.chrome.com/blog/chrome-137-beta#full_frame_rate_render_blocking_attribute)
    * [Pause media playback on not-rendered iframes](https://developer.chrome.com/blog/chrome-137-beta#pause_media_playback_on_not-rendered_iframes)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  Chrome 137 beta 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [CSS and UI](https://developer.chrome.com/blog/chrome-137-beta#css_and_ui)
    * [The if() function](https://developer.chrome.com/blog/chrome-137-beta#the_if_function)
    * [The reading-flow and reading-order properties](https://developer.chrome.com/blog/chrome-137-beta#the_reading-flow_and_reading-order_properties)
    * [offset-path: shape()](https://developer.chrome.com/blog/chrome-137-beta#offset-path_shape)
    * [Support transform attribute on SVGSVGElement](https://developer.chrome.com/blog/chrome-137-beta#support_transform_attribute_on_svgsvgelement)
    * [Allow <use> to reference an external document's root element by omitting the fragment.](https://developer.chrome.com/blog/chrome-137-beta#allow_use_to_reference_an_external_documents_root_element_by_omitting_the_fragment)
    * [System accent color for accent-color property expanded to Windows and ChromeOS](https://developer.chrome.com/blog/chrome-137-beta#system_accent_color_for_accent-color_property_expanded_to_windows_and_chromeos)
    * [view-transition-name: match-element](https://developer.chrome.com/blog/chrome-137-beta#view-transition-name_match-element)
  * [Web APIs](https://developer.chrome.com/blog/chrome-137-beta#web_apis)
    * [Align error type thrown for 'payment' WebAuthn credential creation](https://developer.chrome.com/blog/chrome-137-beta#align_error_type_thrown_for_payment_webauthn_credential_creation)
    * [Blob URL Partitioning: Fetching/Navigation](https://developer.chrome.com/blog/chrome-137-beta#blob_url_partitioning_fetchingnavigation)
    * [Call stacks in crash reports from unresponsive web pages](https://developer.chrome.com/blog/chrome-137-beta#call_stacks_in_crash_reports_from_unresponsive_web_pages)
    * [Canvas Floating Point Color Types](https://developer.chrome.com/blog/chrome-137-beta#canvas_floating_point_color_types)
    * [Disallow non-trustworthy plaintext HTTP prerendering](https://developer.chrome.com/blog/chrome-137-beta#disallow_non-trustworthy_plaintext_http_prerendering)
    * [Document-Isolation-Policy](https://developer.chrome.com/blog/chrome-137-beta#document-isolation-policy)
    * [Ed25519 in Web Cryptography](https://developer.chrome.com/blog/chrome-137-beta#ed25519_in_web_cryptography)
    * [IP address logging and reporting](https://developer.chrome.com/blog/chrome-137-beta#ip_address_logging_and_reporting)
    * [JavaScript Promise Integration](https://developer.chrome.com/blog/chrome-137-beta#javascript_promise_integration)
    * [Language Detector API](https://developer.chrome.com/blog/chrome-137-beta#language_detector_api)
    * [Restrict float attributes and arguments on SVGMatrix, SVGRect, and SVGPoint](https://developer.chrome.com/blog/chrome-137-beta#restrict_float_attributes_and_arguments_on_svgmatrix_svgrect_and_svgpoint)
    * [Selection API getComposedRanges and direction](https://developer.chrome.com/blog/chrome-137-beta#selection_api_getcomposedranges_and_direction)
    * [Web app scope extensions](https://developer.chrome.com/blog/chrome-137-beta#web_app_scope_extensions)
    * [WebAssembly Branch Hints](https://developer.chrome.com/blog/chrome-137-beta#webassembly_branch_hints)
    * [WebGPU: GPUTextureView for externalTexture binding](https://developer.chrome.com/blog/chrome-137-beta#webgpu_gputextureview_for_externaltexture_binding)
    * [WebGPU: copyBufferToBuffer overload](https://developer.chrome.com/blog/chrome-137-beta#webgpu_copybuffertobuffer_overload)
  * [New origin trials](https://developer.chrome.com/blog/chrome-137-beta#new_origin_trials)
    * [Full frame rate render blocking attribute](https://developer.chrome.com/blog/chrome-137-beta#full_frame_rate_render_blocking_attribute)
    * [Pause media playback on not-rendered iframes](https://developer.chrome.com/blog/chrome-137-beta#pause_media_playback_on_not-rendered_iframes)


Rachel Andrew 
[ GitHub ](https://github.com/rachelandrew) [ LinkedIn ](https://www.linkedin.com/in/rachelandrew) [ Mastodon ](https://front-end.social/@rachelandrew) [ Bluesky ](https://bsky.app/profile/rachelandrew.bsky.social) [ Homepage ](https://rachelandrew.co.uk)
Published: May 1, 2025 
Unless otherwise noted, the following changes apply to the newest Chrome beta channel release for Android, ChromeOS, Linux, macOS, and Windows. Learn more about the features listed here through the provided links or from the list on ChromeStatus.com. Chrome 130 is beta as of 30 April, 2025. You can download the latest on [Google.com](https://www.google.com/chrome/beta/) for desktop or on Google Play Store on Android.
## CSS and UI
This release adds seven new CSS and UI features.
### The `if()` function
The CSS `if()` function provides a concise way to express conditional values. It accepts a series of condition-value pairs, delimited by semicolons. The function evaluates each condition sequentially and returns the value associated with the first true condition. If none of the conditions evaluate to true, the function returns an empty token stream. This lets you express complex conditional logic in a simple and concise way. Example:
```
div{
color:var(--color);
background-color:if(style(--color:white):black;else:white);
}
.dark{
--color:black;
}
.light{
--color:white;
}

```
```
<div class="dark">dark</div>
<div class="light">light</div>

```

### The `reading-flow` and `reading-order` properties
The `reading-flow` CSS property controls the order in which elements in a flex, grid, or block layout are exposed to accessibility tools and focused using tab keyboard focus navigation. It takes one of the following keyword values:
  * `normal`
  * `flex-visual`
  * `flex-flow`
  * `grid-rows`
  * `grid-columns`
  * `grid-order`
  * `source-order`


The `reading-order` CSS property lets you manually-override the order within a reading flow container. It is an integer with default value of 0.
To learn more read [Use CSS reading-flow for logical sequential focus navigation](https://developer.chrome.com/blog/reading-flow) and try out some [examples of reading flow](https://chrome.dev/reading-flow-examples/).
### `offset-path: shape()`
The `shape()` function is already supported in `clip-path`, and allows responsive clipping. Enabling it also for `offset-path` closes a small gap where the same kind of shape can be used for that property.
### Support transform attribute on `SVGSVGElement`
This feature enables the application of transformation properties—such as scaling, rotation, translation, and skewing—directly to the `<svg>` root element using its transform attribute. This enhancement lets you manipulate the entire SVG coordinate system or its contents as a whole, providing greater flexibility in creating dynamic, responsive, and interactive vector graphics. By supporting this attribute, the SVG element can be transformed without requiring additional wrapper elements or complex CSS workarounds, streamlining the process of building scalable and animated web graphics.
### Allow `<use>` to reference an external document's root element by omitting the fragment.
In this feature, we are streamlining the SVG `<use>` element by loosening referencing requirements. Currently, you need to explicitly reference fragments within the SVG document. If no fragment ID is given, `<use>` won't be able to resolve the target and nothing will be rendered or referred.
With this feature, omitting fragments or just giving the external SVG file name will automatically reference the root element, eliminating the need for you to alter the referenced document just to assign an ID to the root. This enhancement simplifies this manual editing process and improves efficiency.
### System accent color for `accent-color` property expanded to Windows and ChromeOS
This lets you use the operating system's accent color for form elements. By using the `accent-color` CSS property, you can ensure that form elements such as checkboxes, radio buttons, and progress bars automatically adopt the accent color defined by the user's operating system. This has been supported on macOS since 2021, and is now supported on Windows and ChromeOS.
### `view-transition-name: match-element`
The `match-element` value for the `view-transition` property generates a unique ID based on the element's identity and remains the same for this element. This is used in Single Page App cases where the element is being moved around and you want to animate it with a view transition.
## Web APIs
### Align error type thrown for 'payment' WebAuthn credential creation
Corrects the error type thrown during WebAuthn credential creation for `payment` credentials. Due to a historic specification mismatch, creating a `payment` credential in a cross-origin iframe without a user activation would throw a `SecurityError` instead of a `NotAllowedError`, which is what is thrown for non-payment credentials. This is a breaking change. Code that previously detected the type of error thrown (for example, `e instanceof SecurityError`) would be affected. Code that just generally handles errors during credential creation (for example, `catch (e)`) will continue to function correctly.
### Blob URL Partitioning: Fetching/Navigation
As a continuation of Storage Partitioning, this implements partitioning of Blob URL access by Storage Key (top-level site, frame origin, and the `has-cross-site-ancestor` boolean), with the exception of top-level navigations which will remain partitioned only by frame origin.
This change can be temporarily reverted by setting the `PartitionedBlobURLUsage` policy. The policy will be deprecated when the other storage partitioning related enterprise policies are deprecated.
### Call stacks in crash reports from unresponsive web pages
This feature captures the JavaScript call stack when a web page becomes unresponsive due to JavaScript code running an infinite loop or other very long computation. This helps developers to identify the cause of the unresponsiveness and fix it more easily. The JavaScript call stack is included in the crash reporting API when the reason is unresponsive.
### Canvas Floating Point Color Types
Introduces the ability to use floating point pixel formats (as opposed to 8-bit fixed point) with `CanvasRenderingContext2D`, `OffscreenCanvasRenderingContext2D`, and `ImageData`. This is necessary for high precision applications (for example, medical visualization), high dynamic range content, and linear working color spaces.
### Disallow non-trustworthy plaintext HTTP prerendering
Currently prerender is permitted over HTTP and HTTPS, while prefetch only works over HTTPS. Restrict prerender to be consistent with prefetch.
### Document-Isolation-Policy
`Document-Isolation-Policy` lets a document enable `crossOriginIsolation` for itself, without having to deploy COOP or COEP, and regardless of the `crossOriginIsolation` status of the page. The policy is backed by process isolation. Additionally, the document non-CORS cross-origin subresources will either be loaded without credentials or will need to have a CORP header.
Learn more in [Document Isolation Policy: Enable powerful web features with ease](https://developer.chrome.com/blog/document-isolation-policy).
### Ed25519 in Web Cryptography
This feature adds support for Curve25519 algorithms in the Web Cryptography API, namely the signature algorithm Ed25519
### IP address logging and reporting
Chrome Enterprise is enhancing security monitoring and incident response capabilities by collecting and reporting local and remote IP addresses and sending those IP addresses to the Security Investigation Logs (SIT). In addition, Chrome Enterprise will allow admins to optionally send the IP addresses to 1P and 3P SIEM providers using the Chrome Enterprise Reporting connector. This will be available for Chrome Enterprise Core customers.
### JavaScript Promise Integration
[JavaScript Promise Integration](https://v8.dev/blog/jspi) (JSPI) is an API that lets WebAssembly applications integrate with JavaScript Promises. It allows a WebAssembly program to act as the generator of a Promise, and it allows the WebAssembly program to interact with Promise-bearing APIs. In particular, when an application uses JSPI to call a Promise-bearing (JavaScript) API, the WebAssembly code is suspended; and the original caller to the WebAssembly program is given a Promise that will be fulfilled when the WebAssembly program finally completes.
### Language Detector API
The [Language Detector API](https://developer.chrome.com/docs/ai/language-detection) is a JavaScript API that identifies the language of a provided string. This API is backed by an underlying model that is fine-tuned to perform language detection tasks.
Given a string, the Language Detector API returns an ordered list of the detected languages, along with a confidence score for each result.
Optionally, developers can pass in a list of expected input languages when creating a Language Detector instance to help optimize for use cases where detection is expected to be performed on certain languages.
### Restrict float attributes and arguments on `SVGMatrix`, `SVGRect`, and `SVGPoint`
When setting float attributes or arguments on `SVGMatrix`, `SVGRect` and `SVGPoint`, you now can't set them as `Infinity` or `Nan`. A JavaScript exception is thrown if you attempt to set it, as defined in the SVG specification.
### Selection API `getComposedRanges` and `direction`
This feature ships two new API methods for the Selection API:
  * `Selection.direction` which returns the selection's direction as either `"none"`, `"forward"` or `"backward"`
  * `Selection.getComposedRanges()` which returns a list of 0 or 1 "composed" `StaticRange`


A "composed" `StaticRange` is allowed to cross shadow boundaries, which normal Ranges cannot.
For example:
```
constrange=getSelection().getComposedRanges({shadowRoots:[root]});

```

If the selection crosses a shadow root boundary that isn't provided in the `shadowRoots` list, then the endpoints of the `StaticRange` will be "rescoped" to be outside that tree. This makes sure we don't expose unknown shadow trees.
### Web app scope extensions
Adds a `scope_extensions` web app manifest field that lets web apps extend their scope to other origins.
Example:
```
{
"name":"Example",
"display":"standalone",
"start_url":"/index.html",
"scope_extensions":[
{"type":"type","origin":"https://example.com"}
]
}

```

This allows sites that control multiple subdomains and top level domains to be presented as a single web app.
Requires listed origins to confirm association with the web app using a `.well-known/web-app-origin-association` configuration file.
```
{
"https://sample-app.com/":{
"scope":"/"
}
}

```

### WebAssembly Branch Hints
Improves the performance of compiled WebAssembly code by informing the engine that a particular branch instruction is very likely to take a specific path. This allows the engine to make better decisions for code layout (improving instruction cache hits) and register allocation.
### WebGPU: `GPUTextureView` for `externalTexture` binding
A `GPUTextureView` is now allowed to be used for an `externalTexture` binding when creating a `GPUBindGroup`.
### WebGPU: `copyBufferToBuffer` overload
The `GPUCommandEncoder` `copyBufferToBuffer()` method now includes a simpler way to copy entire buffers using a new overload with optional offsets and size parameters.
## New origin trials
In Chrome 137 you can opt into the following new [origin trials](https://developer.chrome.com/docs/web-platform/origin-trials).
### Full frame rate render blocking attribute
Adds a new render blocking token full-frame-rate to the blocking attributes. When the renderer is blocked with the full-frame-rate token, the renderer will work at a lower frame rate so as to reserve more resources for loading.
### Pause media playback on not-rendered iframes
Adds a `"media-playback-while-not-rendered"` permission policy to allow embedder websites to pause media playback of embedded iframes which aren't rendered—that is, have their "display" property set to "none". This should allow developers to build more user-friendly experiences and to also improve the performance by letting the browser handle the playback of content that is not visible to users.
### Rewriter API
The Rewriter API transforms and rephrases input text in requested ways, backed by an on-device AI language model. Developers may use this API to remove redundancies within a text in order to fit into a word limit, rephrase messages to suit the intended audience or to be more constructive if a message is found to use toxic language, rephrasing a post or article to use simpler words and concepts and more.
### Writer API
The Writer API can be used for writing new material given a writing task prompt, backed by an on-device AI language model. Developers will be able to use this API to generate textual explanations of structured data, composing a post about a product based on reviews or product description, expanding on pro and con lists into full views and more.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-05-01 UTC.

