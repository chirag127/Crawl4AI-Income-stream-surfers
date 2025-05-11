---
url: https://developer.chrome.com/blog/extension-news-october-2024?hl=en
title: https://developer.chrome.com/blog/extension-news-october-2024?hl=en
date: 2025-05-11T16:56:01.623264
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/extension-news-october-2024?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/extension-news-october-2024?hl=es-419)

Sign in


  * On this page
  * [Extensions and AI](https://developer.chrome.com/blog/extension-news-october-2024?hl=en#extensions_and_ai)
  * [Extensions on tour](https://developer.chrome.com/blog/extension-news-october-2024?hl=en#extensions_on_tour)
  * [Chrome Web Store policy updates](https://developer.chrome.com/blog/extension-news-october-2024?hl=en#chrome_web_store_policy_updates)
  * [New extension APIs](https://developer.chrome.com/blog/extension-news-october-2024?hl=en#new_extension_apis)
  * [Upcoming features](https://developer.chrome.com/blog/extension-news-october-2024?hl=en#upcoming_features)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  What's happening in Chrome Extensions, October 2024 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Extensions and AI](https://developer.chrome.com/blog/extension-news-october-2024?hl=en#extensions_and_ai)
  * [Extensions on tour](https://developer.chrome.com/blog/extension-news-october-2024?hl=en#extensions_on_tour)
  * [Chrome Web Store policy updates](https://developer.chrome.com/blog/extension-news-october-2024?hl=en#chrome_web_store_policy_updates)
  * [New extension APIs](https://developer.chrome.com/blog/extension-news-october-2024?hl=en#new_extension_apis)
  * [Upcoming features](https://developer.chrome.com/blog/extension-news-october-2024?hl=en#upcoming_features)


Milica Mihajlija 
[ GitHub ](https://github.com/mihajlija) [ Homepage ](https://mihajlija.github.io/)
It's time for another round up of what's happening in Chrome Extensions: read on for exciting updates on AI integration, new APIs, events and videos.
## Extensions and AI
Extensions enable you to enhance your browsing experience by controlling web content and customizing the browser. With AI you can take this to the next level! We have published resources built for understanding how to effectively use [AI in Chrome extensions](https://developer.chrome.com/docs/extensions/ai). Make sure to check out the examples that demonstrate [what's possible with Gemini in Chrome extensions](https://developer.chrome.com/docs/extensions/ai#ai-powered-extensions-in-action)!
Chrome has also launched the Built-in AI Challenge: You are invited to create innovative web applications and Chrome Extensions, using [Chrome's integrated AI models and APIs](https://developer.chrome.com/docs/ai/built-in), and have a chance to win prizes which total $65,000 USD.
Sign up and get more information on the [Built-in AI Challenge website](https://goo.gle/ChromeAIChallenge). We can't wait to see what you create when you infuse the web with AI!
## Extensions on tour
Want to learn more about browser extensions and connect with the team that builds them? Come find us at these upcoming events!
**DevFest London:** Oliver will be at [DevFest London](https://devfestlondon.com/) on November 16th, 2024, showcasing the latest updates on Chrome extension development. Come learn about new APIs, best practices, and get inspired to build amazing extension projects.
**Ad Filtering Summit Berlin:** Join us at the [Ad Filtering Summit in Berlin](https://adfilteringdevsummit.com/sessions/public/-NXuG6IckpLeVt7jyeIm) on 24 and 25 October, 2024, where we'll be discussing the future of ad filtering and how extensions play a crucial role in creating a better web experience for users. Registration for this event is free.
**TPAC summit:** As part of our involvement in the WebExtensions Community Group, the team has recently attended TPAC, the W3C's annual conference filled with engaging discussions about the future of the web. We collaborated with other browser vendors and developers from the community on important web standards and initiatives that will shape how extensions are built and used. To name just a couple–adding to the Web Platform Tests project to make extension APIs more consistent across browsers and looking at upcoming internationalization standards that we may be able to support in the chrome.i18n API.
TPAC summit.
## Chrome Web Store policy updates
The Chrome Web Store team has published a series of updates to the [Developer Program Policies](https://developer.chrome.com/docs/webstore/program-policies) page designed to encourage the development of high quality products, prevent deceptive behavior, and ensure informed user consent. Rebecca Soares, the Chrome Web Store policy manager, has summarized all the updates in [Chrome Extensions: Important policy updates blog post](https://developer.chrome.com/blog/cws-policy-updates-2024).
## New extension APIs
Starting in Chrome 128, we have added support for response header matching in the Declarative Net Request API. We've updated our API reference to include the new [`responseHeaders`](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest#property-RuleCondition-responseHeaders) and [`excludedResponseHeaders`](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest#property-RuleCondition-excludedResponseHeaders) fields. As part of this update, we've also added a new [rule evaluation](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest#implementation-matching-algorithm) section to our documentation which explains how rules are matched.
Starting in Chrome 130, the [`getKeys()`](https://developer.chrome.com/docs/extensions/reference/api/storage#method-StorageArea-getKeys) method is available on the StorageArea interface used by the chrome.storage API. This follows a [proposal](https://github.com/w3c/webextensions/issues/601) in the WebExtensions Community Group.
Starting in Chrome 130, the [`action.onUserSettingsChanged`](https://developer.chrome.com/docs/extensions/reference/api/action#event-onUserSettingsChanged) event is available. This follows a [proposal](https://github.com/w3c/webextensions/blob/main/proposals/action-on-user-settings-changed-api.md) in the WebExtensions Community Group. Thanks to Microsoft for the contribution to Chromium.
The `minimum_chrome_version` field in the manifest now supports non-major versions. These can be helpful if you need to target a specific Chrome release.
## Upcoming features
View extension storage in DevTools: One of the most requested features in our bug tracker is the ability to view extension storage in DevTools, in the same way we already support for web storage APIs. We hear you, and we're working on this! Expect more details on how to try this experiment out before the end of the year.
Starting in Chrome 130, we will [enable support for the `use_dynamic_url` property](https://groups.google.com/a/chromium.org/g/chromium-extensions/c/Nr3QNKFv74c/m/PYLvA7dOAAAJ) on entries under the [`web_accessible_resources`](https://developer.chrome.com/docs/extensions/reference/manifest/web-accessible-resources#manifest_declaration) key in the manifest.
Following the discussion in the WebExtensions Community Group during TPAC, starting in Chrome 131, `$schema` and `browser_specific_settings` in manifest will no longer cause warnings, as these keys are widely adopted and are understood to not have special behavior in Chrome.
## 🗃️ New videos
Join Oliver on an adventure to add a custom cursor to Chrome, with a guest appearance from Chrome dino!
Don't stop there, learn about content scripts in Chrome Extensions, including how to register CSS and JavaScript to run on a particular page. [Check out the full video on YouTube](https://www.youtube.com/watch?v=ezhJezGX5ak).
Subscribe to our [YouTube channel](https://www.youtube.com/@ChromeDevs) to not miss the upcoming interview with David Li, Extensions Product Manager at Google.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-10-11 UTC.

