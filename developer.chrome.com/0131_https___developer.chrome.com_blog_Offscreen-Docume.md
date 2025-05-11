---
url: https://developer.chrome.com/blog/Offscreen-Documents-in-Manifest-v3?hl=en
title: https://developer.chrome.com/blog/Offscreen-Documents-in-Manifest-v3?hl=en
date: 2025-05-11T16:53:33.453304
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/Offscreen-Documents-in-Manifest-v3?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/Offscreen-Documents-in-Manifest-v3?hl=es-419)




  * On this page
  * [Feature Information](https://developer.chrome.com/blog/Offscreen-Documents-in-Manifest-v3?hl=en#feature_information)
  * [Reasons, and requiring a purpose](https://developer.chrome.com/blog/Offscreen-Documents-in-Manifest-v3?hl=en#reasons_and_requiring_a_purpose)
  * [Into the future](https://developer.chrome.com/blog/Offscreen-Documents-in-Manifest-v3?hl=en#into_the_future)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  Offscreen Documents in Manifest V3 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Feature Information](https://developer.chrome.com/blog/Offscreen-Documents-in-Manifest-v3?hl=en#feature_information)
  * [Reasons, and requiring a purpose](https://developer.chrome.com/blog/Offscreen-Documents-in-Manifest-v3?hl=en#reasons_and_requiring_a_purpose)
  * [Into the future](https://developer.chrome.com/blog/Offscreen-Documents-in-Manifest-v3?hl=en#into_the_future)


Ian Stanion 
To replace functionality in the transition from background pages to extension service workers, developers can use the [`chrome.offscreen`](https://developer.chrome.com/docs/extensions/reference/offscreen) API and manifest permission starting in Chrome 109. Requesting this permission allows for the creation of off-screen documents to use DOM APIs without obtrusively opening new windows or tabs that interrupt the user experience. The `chrome.offscreen` API is now available in chrome extensions. 
In Chromium, Manifest V3 extensions are service worker-based, but service workers don't provide support for the same APIs and mechanisms that full document-based pages (which include background and event pages) do. Additionally, using content scripts to access DOM APIs on web pages leaves the extension at the mercy of different content security policies on a page-to-page basis. To help solve this, we're introducing Offscreen Documents to support DOM-related features and APIs by allowing Manifest V3 extensions to open minimal, scoped, and relatively un-permissioned offscreen documents at runtime through a dedicated API. 
## Feature Information
Since offscreen documents are specifically designed to handle use cases that are not supported in service workers (for example, audio playback), the lifetime of this page, and the permissions it will be granted are separate from that of the extension service worker. The page will have a lifetime mechanism similar to event pages in Manifest V2, in that it will be torn down when it stops performing actions. Additionally, the user agent may place further restrictions on the lifetime specific to the purpose specified. Offscreen documents are designed to fill gaps from APIs that are only accessible to DOM APIs; because of this, extension APIs don't need to be exposed directly in this context. To reduce the likelihood of extensions using these as a "background page replacement", only the [`chrome.runtime` messaging APIs](https://developer.chrome.com/docs/extensions/mv3/messaging) are exposed to the offscreen document. (Developers may also use web messaging by claiming the offscreen document as a [Client](https://developer.mozilla.org/docs/Web/API/Client) via their service worker.) Because some use cases - in particular, site scraping - require access to cross-origin frames, we allow these documents to embed cross-origin frames following the same rules that extension pages have today. In offscreen documents, content scripts specified by the extension are able to run in these frames in order to scrape any necessary content, as they would for any normal web page. 
## Reasons, and requiring a purpose
Creating an offscreen document requires stated reasons and further justification. These reasons are listed in the API reference documentation, and handle the document’s lifetime in different ways. For example, a document opened for audio playback currently has different rules applied to its lifetime than a document opened for clipboard management. You can also add further detail on the offscreen document’s purpose in the justification, which is a developer-written string, and not a parameter with effects on the document. Further reasons may be added to the API over time as developers share their feedback and use cases.
## Into the future
For implementation ease, the first version of this API only supports a single page per-extension, per-profile at a time. In future versions, we may relax this to support multiple pages. Currently, if the extension is running in split mode with an active incognito profile, both the normal and incognito profiles can each have one offscreen document. It is also planned to give the extension worker DOM functionality at a later point. You can “future-proof” your extensions by pairing functions that use the offscreen API with an equivalent commented function in the service worker for swapping at a later date. 
```
// Solution 1 - Service workers cannot directly interact with
// the system clipboard. To work around this, we'll create an offscreen
// document and pass the data we want to write to the clipboard.
asyncfunctionaddToClipboard(value){
awaitchrome.offscreen.createDocument({
url:'offscreen.html',
reasons:[chrome.offscreen.Reason.CLIPBOARD],
justification:'Write text to the clipboard.',
});
}

// Solution 2 – Once extension service workers can use the Clipboard API,
// replace the offscreen document based implementation with something like this
asyncfunctionaddToClipboardV2(value){
navigator.clipboard.writeText(value);
}

```

Additionally, as DOM functionality and APIs are added to the service worker, the list of [reasons](https://developer.chrome.com/docs/extensions/reference/offscreen#reasons) to create a document will be added to or reduced depending on the current state of the service worker, and reasons to use offscreen documents. 
### Conclusion
Offscreen Documents allow extensions that require DOM or window interaction access that cannot be achieved in service workers currently. It also provides a flexible approach, where new use cases can be added and future-solved use cases can be removed. Extensions should employ the proposed offscreen document API for specific use cases, and the primary background context of the extension should remain the service worker specified in the manifest. The offscreen document should not be the place to store primary extension logic because it has limited API access. The lifetime of an offscreen document is independent of the service worker that created it. Service worker lifetime considerations and use cases related to service worker lifetime in extensions will be covered in a separate blog post. The reasons to use offscreen documents will fluctuate over time as features and APIs are added to the service worker itself. We are eager to hear developer feedback as this unfolds.
Photo by [Kari Shea](https://unsplash.com/@karishea?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/wallpapers/desktop/laptop?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2023-01-25 UTC.

