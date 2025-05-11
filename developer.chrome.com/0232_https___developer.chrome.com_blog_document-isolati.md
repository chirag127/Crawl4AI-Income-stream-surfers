---
url: https://developer.chrome.com/blog/document-isolation-policy?hl=en
title: https://developer.chrome.com/blog/document-isolation-policy?hl=en
date: 2025-05-11T16:55:43.062191
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/document-isolation-policy?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/document-isolation-policy?hl=es-419)

Sign in


  * On this page
  * [What is cross-origin isolation?](https://developer.chrome.com/blog/document-isolation-policy?hl=en#what_is_cross-origin_isolation)
  * [What is Document Isolation Policy?](https://developer.chrome.com/blog/document-isolation-policy?hl=en#what_is_document_isolation_policy)
  * [How Document Isolation Policy works](https://developer.chrome.com/blog/document-isolation-policy?hl=en#how_document_isolation_policy_works)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  Document Isolation Policy: Enable powerful web features with ease 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [What is cross-origin isolation?](https://developer.chrome.com/blog/document-isolation-policy?hl=en#what_is_cross-origin_isolation)
  * [What is Document Isolation Policy?](https://developer.chrome.com/blog/document-isolation-policy?hl=en#what_is_document_isolation_policy)
  * [How Document Isolation Policy works](https://developer.chrome.com/blog/document-isolation-policy?hl=en#how_document_isolation_policy_works)


Camille Lamy 
Published: May 1, 2025 
From Chrome 137 Document Isolation Policy is a new feature that makes [crossOriginIsolation](https://developer.mozilla.org/docs/Web/API/Window/crossOriginIsolated) adoption easier. Unlike COEP ([Cross-Origin-Embedder-Policy](https://developer.mozilla.org/docs/Web/HTTP/Reference/Headers/Cross-Origin-Embedder-Policy)), Document Isolation Policy applies per frame and makes no requirements of subframes. By enabling `crossOriginIsolation`, Document Isolation Policy unlocks access to powerful web functionalities like [SharedArrayBuffers](https://developer.mozilla.org/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer) or [WebAssembly threads](https://web.dev/articles/webassembly-threads).
## What is cross-origin isolation?
Cross-origin isolation draws a firm boundary around a document and its same-origin relatives within the browser's process. It prevents the document from being grouped and potentially sharing resources or information with documents from different origins. Cross-origin isolation achieves this by ensuring the origin can be loaded in its own process, regardless of the status of the underlying browser engine's support for site isolation or cross-origin isolation by default. This helps [protect against speculative execution attacks](https://chromium.googlesource.com/chromium/src/+/master/docs/security/side-channel-threat-model.md), such as [Spectre](https://spectreattack.com/).
## What is Document Isolation Policy?
Document Isolation Policy provides a more straightforward way to implement [crossOriginIsolation](https://developer.mozilla.org/docs/Web/API/Window/crossOriginIsolated), when compared to COOP ([Cross-Origin-Opener-Policy](https://developer.mozilla.org/docs/Web/HTTP/Reference/Headers/Cross-Origin-Opener-Policy)) and COEP ([Cross-Origin-Embedder-Policy](https://developer.mozilla.org/docs/Web/HTTP/Reference/Headers/Cross-Origin-Embedder-Policy)). It allows for isolation on a per-frame basis, eliminating the need for embedded iframes to support COEP.
## How Document Isolation Policy works
Document Isolation Policy lets you isolate specific frames within their web applications. By sending a Document-Isolation-Policy header with your document, the document gains access to powerful features like [SharedArrayBuffers](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer), which are otherwise restricted due to security concerns. Unlike [COOP](https://developer.mozilla.org/docs/Web/HTTP/Reference/Headers/Cross-Origin-Opener-Policy) and [COEP](https://developer.mozilla.org/docs/Web/HTTP/Reference/Headers/Cross-Origin-Embedder-Policy), Document Isolation Policy doesn't impose restrictions on pages with which the document can communicate or on child frames it can embed. Documents with Document Isolation Policy can open cross-origin popups and communicate with them. They can also embed any iframe normally.
Document Isolation Policy, similar to [COEP](https://developer.mozilla.org/docs/Web/HTTP/Reference/Headers/Cross-Origin-Embedder-Policy), has two modes: `isolate-and-require-corp` and `isolate-and-credentialless`. These modes govern how cross-origin subresources loaded without [Cross-Origin Resource Sharing](https://developer.mozilla.org/docs/Web/HTTP/Guides/CORS) (CORS) are handled. In `isolate-and-require-corp` mode, cross-origin resources must explicitly declare their cross-origin resource policy using the [`Cross-Origin-Resource-Policy`](https://developer.mozilla.org/docs/Web/HTTP/Reference/Headers/Cross-Origin-Resource-Policy) header; if not, they are blocked. This ensures that resources are intentionally shared. Conversely, `isolate-and-credentialless` mode allows cross-origin resources to be loaded without [CORS](https://developer.mozilla.org/docs/Web/HTTP/Guides/CORS) headers but strips any credentials (like cookies or HTTP authentication) from the request, effectively treating the resource as if it were anonymous. This mode provides a less restrictive but still secure way to handle non-CORS resources.
Iframes isolated with Document Isolation Policy don't have synchronous DOM access to same-origin iframes that are not isolated. However, these isolated iframes can still communicate with non-isolated frames using cross-origin [Window](https://developer.mozilla.org/docs/Web/API/Window) methods like [postMessage](https://developer.mozilla.org/docs/Web/API/Window/postMessage). Additionally, they retain full access to storage APIs, allowing for data persistence and sharing within the same origin, even with isolation enabled.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-05-01 UTC.

