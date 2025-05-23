---
url: https://developer.chrome.com/blog/new-in-chrome-113?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-113?hl=en
date: 2025-05-11T16:57:07.906455
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-113?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-chrome-113?hl=es-419)




  * On this page
  * [WebGPU is here.](https://developer.chrome.com/blog/new-in-chrome-113?hl=en#webgpu)
  * [Devtools response headers override.](https://developer.chrome.com/blog/new-in-chrome-113?hl=en#override-headers)
  * [First-Party Sets is rolling out.](https://developer.chrome.com/blog/new-in-chrome-113?hl=en#first-party-sets)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  New in Chrome 113 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [WebGPU is here.](https://developer.chrome.com/blog/new-in-chrome-113?hl=en#webgpu)
  * [Devtools response headers override.](https://developer.chrome.com/blog/new-in-chrome-113?hl=en#override-headers)
  * [First-Party Sets is rolling out.](https://developer.chrome.com/blog/new-in-chrome-113?hl=en#first-party-sets)


Adriana Jara 
[ GitHub ](https://github.com/tropicadri) [ LinkedIn ](https://www.linkedin.com/in/adrianajara) [ Mastodon ](https://hachyderm.io/@tropicadri)
Here's what you need to know:
  * [WebGPU](https://developer.chrome.com/blog/new-in-chrome-113?hl=en#webgpu) is here, it allows high-performance 3D graphics and data-parallel computation on the web.
  * Devtools can now override network [response headers](https://developer.chrome.com/blog/new-in-chrome-113?hl=en#override-headers).
  * [First Party Sets](https://developer.chrome.com/blog/new-in-chrome-113?hl=en#first-party-sets), part of the [Privacy Sandbox](https://privacysandbox.com/), that allows organizations to declare related sites is starting to roll out.
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-113?hl=en#more).


I'm Adriana Jara. Let's dive in and see what's new for developers in Chrome 113.
## WebGPU is here.
[WebGPU is a new API](https://developer.chrome.com/blog/webgpu-release) for the web, which exposes modern hardware capabilities and allows rendering and computation operations on a GPU, similar to [Direct3D 12](https://learn.microsoft.com/en-us/windows/win32/direct3d12/what-is-directx-12-), [Metal](https://developer.apple.com/metal/), and [Vulkan](https://developer.nvidia.com/vulkan).
Unlike the [WebGL](https://www.khronos.org/webgl/wiki/Getting_Started) family of APIs, WebGPU offers access to more advanced GPU features and provides first-class support for general computations on the GPU.
The API is designed with the web platform in mind. It features: An idiomatic JavaScript API. Integration with promises. Support for importing videos. A polished developer experience with great error messages.
Many widely used WebGL libraries are already working on implementing WebGPU support or have already done so. This means that using WebGPU may only require making a single line change, for example:
  * **Babylon.js:** Has full WebGPU support already.
  * **PlayCanvas:** Has announced initial WebGPU support.
  * **TensorFlow.js:** Supports WebGPU-optimized versions of most operators.
  * **Three.js:** WebGPU support is under development.


Check out [WebGPU's documentation](https://developer.mozilla.org/docs/Web/API/WebGPU_API) on MDN for all the details.
## Devtools response headers override.
In DevTools you can now override response headers in the **Network** panel.
Previously, you needed access to the web server to experiment with HTTP response headers.
With response header overrides, you can locally prototype fixes for various headers, including but not limited to:
  * [Cross-Origin Resource Sharing (CORS) Headers](https://developer.mozilla.org/docs/Web/HTTP/CORS)
  * [Permissions-Policy Headers](https://developer.mozilla.org/docs/Web/HTTP/Headers/Permissions-Policy)
  * [Cross-Origin Isolation Headers](https://web.dev/articles/coop-coep)


To override a header, navigate to **Network** > **Headers** > **Response Headers** , hover over a header's value, click **Edit** and edit it.
You can also add a new header:
And edit all overrides in a single place.
Check out [this article](https://developer.chrome.com/blog/new-in-devtools-113) for instructions on how to use this feature and other updates in DevTools
## First-Party Sets is rolling out.
[First-Party Sets (FPS)](https://developer.chrome.com/docs/privacy-sandbox/first-party-sets) is starting to roll out to stable. First Party Sets is part of the [Privacy Sandbox](https://privacysandbox.com/). It is a way for organizations to declare relationships among sites, so that browsers allow limited third-party cookie access for specific purposes.
As part of the work on First-Party Sets, Chrome is implementing and extending the Storage Access API allowing a site to request access to their cookies in a third-party context. With it, organizations with related sites (for example, using different domain names, or country-specific domains) can still provide services like single sign-on or shared sessions. Remember! This API will be rolled out slowly to users over a number of weeks to enable testing and evaluation.
## And more!
Of course there's plenty more.
  * The unprefixed [image-set](https://developer.mozilla.org/docs/Web/CSS/image/image-set) type is now available so authors don't need to use `-webkit-image-set` and it is up to date to the current spec.
  * The [`overflow-inline`](https://developer.mozilla.org/docs/Web/CSS/@media/overflow-inline) and [`overflow-block`](https://developer.mozilla.org/docs/Web/CSS/@media/overflow-block) media features are now supported.
  * There is an origin trial for [WebGPU WebCodecs integration](https://developer.chrome.com/origintrials#/view_trial/1705738358866575361).


## Further reading
This covers only some key highlights. Check the links below for additional changes in Chrome 113.
  * [What's new in Chrome DevTools (113)](https://developer.chrome.com/blog/new-in-devtools-113)
  * [Chrome 113 deprecations and removals](https://developer.chrome.com/blog/deps-rems-113)
  * [ChromeStatus.com updates for Chrome 113](https://www.chromestatus.com/features#milestone%3D113)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/112.0.5615.170..113.0.5672.58)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
I'm Adriana Jara, and as soon as Chrome 114 is released, I'll be right here to tell you what's new in Chrome!
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2023-05-03 UTC.

