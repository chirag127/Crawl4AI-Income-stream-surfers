---
url: https://developer.chrome.com/blog/extension-news-october-2023?hl=en
title: https://developer.chrome.com/blog/extension-news-october-2023?hl=en
date: 2025-05-11T16:55:56.056200
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/extension-news-october-2023?hl=en#main-content)
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


#  What's happening in Chrome Extensions? 
Stay organized with collections  Save and categorize content based on your preferences. 
Amy Steam 
[ GitHub ](https://github.com/amysteam) [ LinkedIn ](https://www.linkedin.com/in/amysteam)
Back in July, we launched [a new blog series](https://developer.chrome.com/blog/extension-news-july-2023) to keep you up-to-date on extension developments. Thanks to your valuable feedback and our ongoing collaboration with fellow browser vendors in the WebExtensions Community Group, we continue to enhance extension APIs and work towards greater consistency across browsers.
Welcome to the October edition! In this post, we'll look at some of the changes the Chrome extension team has made in the past few months, as well as some new features that'll come out later this year. Let's get started!
## New extension APIs and features
In this section, we share some significant API launches, briefly review other API improvements, and share upcoming releases. All launches are currently available in the latest Beta release. See the [chromium release schedule](https://chromiumdash.appspot.com/schedule) for details.
### Highlights
#### Resolved known issues
The extension team has been actively working to resolve Manifest V3 stability issues. [Chrome 116 launched many improvements](https://developer.chrome.com/blog/chrome-116-beta-whats-new-for-extensions) that helped us make significant progress toward closing the feature gap between Manifest V2 and V3. In Chrome 120, we will have finished addressing all our prioritized platform gaps and closed all critical bugs that are documented on the [known issues page](https://developer.chrome.com/docs/extensions/migrating/known-issues). All features are currently available in Chrome 120 Canary, except fileHandler support for ChromeOS Lacros, and the userScripts API which will land later this month. Check out the updated [known issues page](https://developer.chrome.com/docs/extensions/migrating/known-issues) for more details.
#### Improved Service Worker stability
Service worker-related stability issues have been resolved. In Chrome 116, we added strong keep-alives to extension APIs that [display a user prompt](https://developer.chrome.com/blog/chrome-116-beta-whats-new-for-extensions#sw-keepalive) and improved support for WebSockets (see the [Using WebSockets in extensions](https://developer.chrome.com/docs/extensions/mv3/tut_websockets) tutorial). From Chrome 118 onward, a service worker will stay alive during an [active Debugger API session](https://developer.chrome.com/docs/extensions/reference/debugger).
Check out our updated [Service Worker guidance](https://developer.chrome.com/docs/extensions/mv3/service_workers/service-worker-lifecycle#timeouts) for more details. If your users still encounter service worker-related stability issues in Chrome versions after 119, [please let us know](https://developer.chrome.com/docs/extensions/support-feedback). 
#### Increased security
Previously, navigating to some `chrome://` URLs using [`tabs.update()`](https://developer.chrome.com/docs/extensions/reference/tabs#method-update), [`tabs.create`](https://developer.chrome.com/docs/extensions/reference/tabs#method-create), and [`windows.create()`](https://developer.chrome.com/docs/extensions/reference/windows#method-create) emitted an error or would crash Chrome. Also, [`tabs.update()`](https://developer.chrome.com/docs/extensions/reference/tabs#method-update) couldn't open a Javascript URL. In Chrome 117, we expanded the number of supported `chrome://` URLs, and the Javascript URL blocking now also applies to all extension API methods.
In Chrome 117, users will receive proactive notifications on the Chrome Extensions page if an extension they've installed is no longer available on the Chrome Web Store. This can happen if the developer unpublishes the extension, it's taken down for policy violations, or it's identified as malware. For a deep dive, see [Bringing Safety Check to the chrome://extensions page](https://developer.chrome.com/en/blog/extension-safety-hub).
In Chrome 118, extensions will not be allowed to navigate to `file://` URLs using the `chrome.tabs` and `chrome.windows` APIs unless the “Allow access to file URLs” option is enabled on the extension’s details page. See the [WECG discussion](https://github.com/w3c/webextensions/issues/426).
### More API launches
  * **Runtime API:** Starting in Chrome 116, you can use [`runtime.getContexts()`](https://developer.chrome.com/docs/extensions/reference/runtime#method-getContexts) to retrieve information about active contexts. For example, you can check if there's an [active offscreen document](https://developer.chrome.com/docs/extensions/reference/offscreen#example-maintaining-the-lifecycle-of-an-offscreen-document).
  * **Side Panel API** In [Chrome 116](https://chromiumdash.appspot.com/commit/8e7430446eaa0b80964b0ab1fd816ac6f33fd4cd) you can use [`sidepanel.open()`](https://developer.chrome.com/docs/extensions/reference/api/sidePanel#user-interaction) to open the extension side panel programmatically in response to a user gesture, such as a context menu click.
  * **TabCapture API** Added the ability to call `getMediaStreamId()` from the extension service worker and obtain a [`MediaStream`](https://developer.mozilla.org/docs/Web/API/MediaStream) object from a stream ID in an offscreen document in Chrome 116. See [Audio recording and screen capture](https://developer.chrome.com/docs/extensions/mv3/screen_capture) for examples.
  * **DeclarativeNetRequest API:** The default value for the [`isUrlFilterCaseSensitive`](https://developer.chrome.com/docs/extensions/reference/declarativeNetRequest#property-RuleCondition-isUrlFilterCaseSensitive) property was changed to `false` in [Chrome 118](https://chromiumdash.appspot.com/commit/d90e6a56d0e77ce5d278a5b070098c5d8f7081fd).


### Coming soon...
We plan to address all remaining items on the [known issues page](https://developer.chrome.com/docs/extensions/migrating/known-issues#closing-the-platform-gap) with the release of Chrome 120. Additionally, we plan to add the following features:
  * The **UserScripts API** will allow user script managers to coordinate how and when to inject a collection of user scripts into web pages. See the [WECG proposal](https://github.com/w3c/webextensions/blob/main/proposals/user-scripts-api.md) for details.
  * The **ReadingList API** will allow developers to create, read, update, and delete metadata located in the Reading List panel of the side panel. Watch [What's new in Chrome extensions](https://developer.chrome.com/docs/extensions/whatsnew) for the announcement.
  * Following [feedback](https://github.com/w3c/webextensions/issues/318) in the Web Extensions Community Group, we are **significantly increasing the limit on enabled static rulesets from 10 to 50**. Additionally, we are **increasing the total number of allowed static rulesets from 50 to 100**. This is currently available in Canary.
  * The **File Handling API:** will be available for ChromeOS extensions starting in ChromeOS 120, which lets extensions open files with specified MIME types and file extensions in a similar manner to web platform file handling.
  * Extensions will be able to use the web [Push API](https://developer.mozilla.org/docs/Web/API/Push_API) via [`self.registration.pushManager.subscribe()`](https://developer.mozilla.org/docs/Web/API/PushManager/subscribe) without showing a user-visible notification by setting `userVisibleOnly` to `false`. This will make push notifications a more seamless alternative to WebSockets in service workers (MV3) for asynchronous client-server communication. See [Chromium bug](https://bugs.chromium.org/p/chromium/issues/detail?id=1319986) and [WECG discussion](https://github.com/w3c/webextensions/issues/208) for details.


Stay tuned to the [What's new in extensions](https://developer.chrome.com/docs/extensions/whats-new) page for announcements as soon as these features are available in [Chrome Beta](https://chromestatus.com/roadmap).
## Documentation upgrades
We've also been improving and adding to our documentation. Please continue to ask questions on the [chromium-group](https://groups.google.com/a/chromium.org/g/chromium-extensions) and [report documentation issues](https://developer.chrome.com/docs/extensions/support-feedback/file-a-bug).
### Highlights
  * We've revamped the [Samples landing page](https://developer.chrome.com/docs/extensions/samples). You can now filter by API, permission, and type, making it easier to locate specific samples. This enhancement was a collaborative effort with our Summer of Code intern, Xuezhou Dai. Read about his experience in [this blog post](https://developer.chrome.com/blog/google-summer-of-code-and-chrome-extensions).
  * [Using your Google Analytics account with the Chrome Web Store](https://developer.chrome.com/docs/webstore/google-analytics) describes how to view Google Analytics 4 for your Chrome Web Store listing, complementing the data provided by the Developer Dashboard. This guide provides steps to opt into Google Analytics, monitor ad performance, track conversions, and grant other accounts access to Google Analytics data.
  * We published a new guide on [how cookies and web storage APIs](https://developer.chrome.com/docs/extensions/mv3/storage-and-cookies) work in Chrome extensions. It includes all you need to know about [Privacy Sandbox](https://developer.chrome.com/docs/privacy-sandbox) as an extension developer. 
  * We launched new articles on how to integrate testing in your extension projects: [Unit testing Chrome extensions](https://developer.chrome.com/docs/extensions/mv3/unit-testing) and [End-to-end testing for extensions](https://developer.chrome.com/docs/extensions/mv3/end-to-end-testing) covers general guidance and best practices across a number of popular frameworks. For a practical tutorial, see [Testing Chrome Extensions with Puppeteer](https://developer.chrome.com/docs/extensions/mv3/tut_puppeteer-testing).


### More updates
  * We've rewritten the [Declarative Net Request API](https://developer.chrome.com/docs/extensions/reference/declarativeNetRequest) guidance in a way that paints a clearer picture of how to implement declarative rulesets.
  * We added more guidance for [migrating remotely hosted code to Manifest V3](https://developer.chrome.com/docs/extensions/migrating/improve-security). Plus, to minimize the risk of encountering issues during the release, we offer strategies for [Publishing your Manifest V3 extension](https://developer.chrome.com/docs/extensions/migrating/publish-mv3) in stages.
  * Learn how to connect to a [WebSocket in your extension's service worker](https://developer.chrome.com/docs/extensions/mv3/tut_websockets).
  * We expanded our [Get Help guide](https://developer.chrome.com/docs/extensions/support-feedback) to include more detailed instructions on how to file a bug, keep track of existing issues, request new features, and more. 


### Coming soon...
  * User Scripts API reference and tutorial.
  * Firebase tutorial and samples.
  * ReadingList API reference.


## Redesigning the Chrome Web store 🌈
.  The new Chrome Web Store home page 
Earlier this month, we announced an early preview of the revamped Chrome Web Store, as we hinted at Google I/O. Check it out for yourself! <https://chromewebstore.google.com/>. A few noteworthy changes are:
  * Increased the list of categories from a list of eleven to a new list of [seventeen in three](https://developer.chrome.com/docs/webstore/best-practices#category-revisions) category groups.
  * Improved autocomplete in the search.
  * Screenshots are now being displayed at significantly higher quality. If you haven't already, you can upload 1280x800 screenshots.
  * Replies to questions on the Support tab now show newlines.
  * When replying to user reviews and support questions, your response will now include a “Developer” badge beside your name.
  * You can provide users with a direct link to the reviews page by adding "/reviews" at the end of your store item URL For example: `https://chromewebstore.google.com/detail/_EXTENSION_ID_/reviews`.


Thanks for everyone's input so far on the [chromium-google group](https://groups.google.com/a/chromium.org/g/chromium-extensions/c/9lc7Prf9vLk/m/3trCFBWYAQAJ). Feel free to join in the discussion or send your feedback directly to the CWS team using the **Give feedback** menu item:
Giving feedback on the Chrome Web Store page 
Additionally, you can [submit a self-nomination form](https://docs.google.com/forms/d/e/1FAIpQLSf4goBOeJDSVwp7xGCZw5vORovPOBhCv_kWM-VXWDhSA0NUQg/viewform) to be featured in the Editors’ Picks collection. Stay tuned for improvements coming soon to the developer dashboard as well!
## 💡 Did you know?
  * There's a new video on Debugging Chrome extensions. It covers many topics you may already be familiar with, but it also shares a few neat tricks for using DevTools in extensions. 
  * You are now required to provide a privacy policy for each extension. Previously, you could only add one privacy policy per developer account, but it was awkward if you had a few extensions under one developer account. This new interface is available in the **Privacy Tab** of your item in the developer dashboard. This means that account-level privacy policies are no longer supported.  Screenshot of the privacy policy box 


## Reaching out 🙌
We've continued reaching out to the extension developer community through 1:1's, launching new programs, and attending summits. Here are a few highlights: 
  * The extensions [Google Developer Experts program](https://developers.google.com/community/experts) was launched in August. We have over a dozen new Chrome extension-focused GDEs from around the world providing us with great feedback. It's a very exciting time for the program! 
  * We attended [TPAC](https://www.w3.org/2023/09/TPAC/) (W3C's annual conference) as part of the [Web Extensions Community Group](https://github.com/w3c/webextensions) and met with representatives from Firefox and Safari along with several members of the community. We made significant progress on several topics, including moving towards more consistent extension APIs, working on a specification, and building on top of Web Platform Tests to create a new testing suite. Read the full minutes in the [WECG repository](https://github.com/w3c/webextensions).
  * Last week, the extension team participated in the [Ad-Filtering Dev Summit](https://adfilteringdevsummit.com/) in Amsterdam. They met several of you at a coffee chat they hosted before the summit week and the open office hours on Friday.  Extension team in Ad-filtering Dev Summit 


Even if you were unable to attend any of these events, you can continue getting involved by asking questions on the [chromium-extensions](https://groups.google.com/a/chromium.org/g/chromium-extensions) Google group, following browser partner discussions on the [WECG](https://github.com/w3c/webextensions/issues), and reporting any documentation issues.
Thanks again for being a part of the extension developer community!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2023-10-17 UTC.

