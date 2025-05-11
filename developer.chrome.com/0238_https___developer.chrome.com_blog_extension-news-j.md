---
url: https://developer.chrome.com/blog/extension-news-january-2025?hl=en
title: https://developer.chrome.com/blog/extension-news-january-2025?hl=en
date: 2025-05-11T16:55:46.412973
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/extension-news-january-2025?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/extension-news-january-2025?hl=es-419)




  * On this page
  * [Highlights](https://developer.chrome.com/blog/extension-news-january-2025?hl=en#highlights)
    * [Chrome built-in AI APIs and Hackathon](https://developer.chrome.com/blog/extension-news-january-2025?hl=en#chrome_built-in_ai_apis_and_hackathon)
    * [New Extensions Menu](https://developer.chrome.com/blog/extension-news-january-2025?hl=en#new_extensions_menu)
    * [Extensions storage viewer](https://developer.chrome.com/blog/extension-news-january-2025?hl=en#extensions_storage_viewer)
    * [userScripts.execute() in Canary](https://developer.chrome.com/blog/extension-news-january-2025?hl=en#userscriptsexecute_in_canary)
  * [Platform updates](https://developer.chrome.com/blog/extension-news-january-2025?hl=en#platform_updates)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  What's happening in Chrome Extensions, January 2025 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Highlights](https://developer.chrome.com/blog/extension-news-january-2025?hl=en#highlights)
    * [Chrome built-in AI APIs and Hackathon](https://developer.chrome.com/blog/extension-news-january-2025?hl=en#chrome_built-in_ai_apis_and_hackathon)
    * [New Extensions Menu](https://developer.chrome.com/blog/extension-news-january-2025?hl=en#new_extensions_menu)
    * [Extensions storage viewer](https://developer.chrome.com/blog/extension-news-january-2025?hl=en#extensions_storage_viewer)
    * [userScripts.execute() in Canary](https://developer.chrome.com/blog/extension-news-january-2025?hl=en#userscriptsexecute_in_canary)
  * [Platform updates](https://developer.chrome.com/blog/extension-news-january-2025?hl=en#platform_updates)


Sebastian Benz 
[ GitHub ](https://github.com/sebastianbenz) [ Mastodon ](https://mastodon.cloud/@sebabenz) [ Bluesky ](https://bsky.app/profile/sebabenz.bsky.social)
Published: January 29, 2025 
A few very exciting features landed in the Chrome Web Store and the Chrome Extensions platform over the past quarter. Let's take a look!
## Highlights
### Chrome built-in AI APIs and Hackathon
The [Prompt API](https://developer.chrome.com/docs/extensions/ai/prompt-api) is now available exclusively for Chrome Extensions in an origin trial. You can now build Chrome Extensions that use Gemini Nano, our most efficient language model, in the browser. While you're at it, take a look at the origin trials for the [Translator](https://developer.chrome.com/docs/ai/translator-api), [Summarizer](https://developer.chrome.com/docs/ai/summarizer-api) and [Language Detector](https://developer.chrome.com/docs/ai/language-detection) APIs which are now available as origin trials as well.
To kick off the origin trial for the new Built-in AI API, the Chrome team launched the Chrome Built-in AI Challenge. Developers had two months to create innovative web applications and Chrome Extensions using Chrome's integrated AI models and APIs. This week, we announced the [winners](https://www.youtube.com/watch?v=5LHDdtXe5yA&pp=ygUYZ2RnIG1hZHJpZCBleHRlbnNpb25zIGFp). It was amazing to see how many teams decided to build an extension as the majority of submissions were Chrome Extensions! It seems like we're not the only ones being excited about the combination of Chrome Extensions and the new Built-in AI APIs. Stay tuned for more!
### New Extensions Menu
At Google I/O 2024, we shared some early designs for upcoming changes to the extensions menu, which give users more control over the sites extensions can access. If you're an extension developer, we recommend checking out the newly introduced [chrome.permissions.addHostAccessRequest()](https://developer.chrome.com/docs/extensions/reference/api/permissions#method-addHostAccessRequest) API which gives you a way to ask users for access to a specific website. We'll start testing these changes in Canary over the next few months. Read our [blog post](https://developer.chrome.com/blog/new-extensions-menu-testing) for all the details about what's changing (and what's not).
### Extensions storage viewer
You can now view and edit extension storage in DevTools! This was one of the most requested DevTools features and had become one of the most starred DevTools issues in the issue tracker. [Oliver](https://bsky.app/profile/oliverdunk.com) took this on and contributed the new extension storage viewer to Chrome DevTools. [Read the announcement for more details](https://groups.google.com/a/chromium.org/g/chromium-extensions/c/ehw8_hM6pyg/m/-LwxB-1iAgAJ).
### `userScripts.execute()` in Canary
Another update we're really excited about: [userScripts.execute()](https://github.com/w3c/webextensions/issues/477) will land in Chrome 134. The change is currently in Canary behind the `ApiUserScriptsExecute` flag (launch Chrome with `--enable-features=ApiUserScriptsExecute` to test). This API will let you programmatically inject user scripts at runtime. Again, this is a feature that many developers have been asking for and we're really happy that it will launch soon!
## Platform updates
Here are a few more updates to the extensions platform:
  * Chrome 130: We enabled [support for the `use_dynamic_url` property](https://groups.google.com/a/chromium.org/g/chromium-extensions/c/Nr3QNKFv74c/m/PYLvA7dOAAAJ) on entries under the `[web_accessible_resources](/docs/extensions/reference/manifest/web-accessible-resources#manifest_declaration)` key in the manifest.
  * Chrome 132: The [frozen](https://developer.chrome.com/docs/extensions/reference/api/tabs#property-Tab-frozen) property in the Tabs API indicates if a tab has been frozen by the browser. Messages sent to frozen tabs will be queued and handled when the tab is unfrozen.
  * Chrome 133: Unpacked extensions loaded from the `chrome://extensions` page will only be enabled if the developer mode switch is turned on. When the switch is turned off, these extensions will be disabled.
  * Chrome 134: Declarative Net Request rules will apply to main frame requests for web resources initiated by extensions ([read more](https://groups.google.com/a/chromium.org/g/chromium-extensions/c/TW2Bm46E09s/m/sJhCloQcCgAJ)).


## New videos
Patrick from the Chrome Extensions Developer Relations team sat down with Chrome Extensions product manager David Li to answer your top questions about the Chrome Web Store.
Oliver did a presentation at the [Wey Wey Web conference](https://www.weyweyweb.com/) in Malaga, Spain. His talk is a great introduction to what's possible with Chrome Extensions.
## What's next?
Cancel review is coming! The ability to cancel a review on the Web Store is in the final stages of testing and will roll out to users soon! Beyond that, the Chrome Web Store team is working on more features to make the store more secure—stay tuned.
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-01-29 UTC.

