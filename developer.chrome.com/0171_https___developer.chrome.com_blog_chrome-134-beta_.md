---
url: https://developer.chrome.com/blog/chrome-134-beta?hl=en
title: https://developer.chrome.com/blog/chrome-134-beta?hl=en
date: 2025-05-11T16:54:24.602526
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/chrome-134-beta?hl=en#main-content)
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


#  Chrome 134 beta 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Rachel Andrew 
[ GitHub ](https://github.com/rachelandrew) [ LinkedIn ](https://www.linkedin.com/in/rachelandrew) [ Mastodon ](https://front-end.social/@rachelandrew) [ Bluesky ](https://bsky.app/profile/rachelandrew.bsky.social) [ Homepage ](https://rachelandrew.co.uk)
Published: February 5, 2025 
Unless otherwise noted, the following changes apply to the newest Chrome beta channel release for Android, ChromeOS, Linux, macOS, and Windows. Learn more about the features listed here through the provided links or from the list on ChromeStatus.com. Chrome 134 is beta as of 5 February, 2025. You can download the latest on [Google.com](https://www.google.com/chrome/beta/) for desktop or on Google Play Store on Android.
## CSS
This release adds five new CSS and UI features.
### CSS dynamic-range-limit property
Enables a page to limit the maximum brightness of HDR content.
### Customizable `<select>` element
Add the ability to customize HTML `<select>` elements, by opting into the new behavior with the `base-select` value of `appearance`. After opting in you can add rich content including images, and also style the options.
### Dialog light dismiss
One of the nice features of the Popover API is its light dismiss behavior. This feature brings the same capability to `<dialog>`. A new `closedby` attribute controls behavior:
  * `<dialog closedby=none>`: No user-triggered closing of dialogs at all. 
  * `<dialog closedby=closerequest>`: Pressing `ESC` (or other close trigger) closes the dialog.
  * `<dialog closedby=any>`: Clicking outside the dialog, or pressing ESC, closes the dialog. The same as `popover=auto` behavior.


### CSS highlight inheritance
With CSS highlight inheritance, the CSS highlight pseudo-classes, such as `::selection` and `::highlight`, inherit their properties through the pseudo highlight chain, rather than the element chain. The result is a more intuitive model for inheritance of properties in highlights.
To learn more, read the blog post [Inheritance changes for CSS selection styling ](https://developer.chrome.com/blog/selection-styling) written by Stephen Chenney from Igalia.
## `:has-slotted` pseudo-class
The `:has-slotted` pseudo-class represents a slot element with slotted content, such as a text node or element. This can be used to style elements based on whether or not they are using slot fallback content.
## Web APIs
### Attribution Reporting Feature: Remove Aggregatable report limit when trigger context ID is non-null
This change is based on API caller feedback and the need for being able to measure a higher number of conversion events for certain user flows.
Currently the API has a limit that allows up to 20 aggregatable reports to be generated per source registration which is restrictive for use cases where a user may have a longer user journey. This change removes the aggregatable report limit when a trigger context ID is provided as part of the registration. The removal of this limit is restricted to only when the trigger context ID is specified, because when it is specified the API applies a higher rate of null reports which helps to protect against cross-site information leaking through report counts.
Additionally, aggregatable reports will still be bound by other limits that restrict the total amount of information that can be measured, such as the L1 contribution budget (65,536) per source and the attribution rate limit.
### Blob URL Partitioning: Fetching/Navigation
As a continuation of Storage Partitioning, implements partitioning of Blob URL access by Storage Key (top-level site, frame origin, and the has-cross-site-ancestor boolean), with the exception of top-level navigations which will remain partitioned only by frame origin. This behavior is similar to what's currently implemented by both Firefox and Safari, and aligns Blob URL usage with the partitioning scheme used by other storage APIs as part of Storage Partitioning. In addition, Chrome will enforce noopener on renderer-initiated top-level navigations to Blob URLs where the corresponding site is cross-site to the top-level site performing the navigation. This aligns Chrome with similar behavior in Safari, and the relevant specs have been updated to reflect these changes.
This change can be temporarily reverted by setting the `PartitionedBlobURLUsage` policy. The policy will be deprecated when the other storage partitioning related enterprise policies are deprecated.
### Document-Policy: `expect-no-linked-resources`
The `expect-no-linked-resources` configuration point in Document-Policy lets a document hint to the user agent to better optimize its loading sequence, such as not using the default speculative parsing behavior (also known as the [preload scanner](https://developer.chrome.com/articles/preload-scanner)).
User Agents have implemented speculative parsing of HTML to speculatively fetch resources that are present in the HTML markup, to speed up page loading. For the vast majority of pages on the Web that have resources declared in the HTML markup, the optimization is beneficial and the cost paid in determining such resources is a sound tradeoff. However, the following scenarios might result in a sub-optimal performance tradeoff versus the explicit time spent parsing HTML for determining sub resources to fetch:
  * Pages that don't have any resources declared in the HTML.
  * Large HTML pages with minimal or no resource loads that could explicitly control preloading resources using other preload mechanisms available.


The `expect-no-linked-resources` Document-Policy hints the User Agent that it may choose to optimize out the time spent in such sub-resource determination.
### Explicit resource management (async and sync)
These features address a common pattern in software development regarding the lifetime and management of various resources (for example memory and I/O). This pattern generally includes the allocation of a resource and the ability to explicitly release critical resources.
### Extend the `console.timeStamp` API to support measurements and presentation options
This feature extends the `console.timeStamp()` API, in a backwards-compatible manner, to provide a high-performance method for instrumenting applications and surfacing timing data to the Performance panel in DevTools.
Timing entries added with the API can have a custom timestamp, duration and presentation options (track, swimlane, and color).
### `OffscreenCanvas` `getContextAttributes`
Adds the `getContextAttributes` interface from `CanvasRenderingContext2D` to `OffscreenCanvasRenderingContext2D`.
### Private Aggregation API: per-context contribution limits for Shared Storage callers
Enables Shared Storage callers to customize the number of contributions per Private Aggregation report.
This feature enables Shared Storage callers to configure per-context contribution limits with a new field, `maxContributions`. Callers set this field to override the default number of contributions per report—larger and smaller numbers will both be permitted. Chrome will accept values of `maxContributions` between 1 and 1000 inclusive; larger values will be interpreted as 1000.
Due to padding, the size of each report's payload will be roughly proportional to the chosen number of contributions per report. We expect that opting into larger reports will increase the cost of operating the Aggregation Service.
Protected Audience callers won't be affected by this feature. However, we are planning to add support for customizing the number of contributions for Protected Audience reports in future features.
### Support `ImageSmoothingQuality` in `PaintCanvas`
Add support for the `imageSmoothingQuality` attribute on Paint Canvas. It allows a web developer to choose the quality over performance tradeoff when scaling images. There are three valid options for `imageSmoothingQuality`: `low`, `medium` and `high`.
### WebGPU Subgroups
Adds subgroup functionality to WebGPU. Subgroup operations perform SIMT operations to provide efficient communication and data sharing among groups of invocations. These operations can be used to accelerate applications by reducing memory overheads incurred by inter-invocation communication.
## New origin trials
In Chrome 134 you can opt into the following new [origin trials](https://developer.chrome.com/docs/web-platform/origin-trials).
### Digital Credential API
Websites can and do get credentials from mobile wallet apps through a variety of mechanisms today, for example, custom URL handlers and QR code scanning. This feature lets sites request identity information from wallets using Android's `IdentityCredential` `CredMan` system. It is extensible to support multiple credential formats (for example, ISO mDoc and W3C verifiable credential) and allows multiple wallet apps to be used. Mechanisms are being added to help reduce the risk of ecosystem-scale abuse of real-world identity.
The origin trial starting in Chrome 134 adds support for this API on desktop platform, where Chrome on Desktop will securely communicate with the digital wallet on the Android phone to fetch the requested credentials.
## Deprecations and removals
This version of Chrome introduces the deprecations and removals listed below. Visit ChromeStatus.com for lists of planned deprecations, current deprecations and previous removals.
This release of Chrome removes one feature.
### Remove nonstandard getUserMedia audio constraints
Blink supports a number of nonstandard `goog`-prefixed constraints for `getUserMedia` from some time before constraints were properly standardized.
Usage has gone down significantly to between 0.000001% and 0.0009% (depending on the constraint) and some of them don't even have an effect due to changes in the Chromium audio-capture stack. Soon none of them will have any effect due to other upcoming changes.
We don't expect any major regressions due to this change. Applications using these constraints will continue to work, but will get audio with default settings (as if no constraints were passed). They can opt to migrate to standard constraints.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-02-05 UTC.

