---
url: https://developer.chrome.com/blog/extension-news-july-2023?hl=en
title: https://developer.chrome.com/blog/extension-news-july-2023?hl=en
date: 2025-05-11T16:55:46.418734
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/extension-news-july-2023?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/extension-news-july-2023?hl=es-419)




  * On this page
  * [New extension APIs and features](https://developer.chrome.com/blog/extension-news-july-2023?hl=en#new-apis)
    * [More API launches](https://developer.chrome.com/blog/extension-news-july-2023?hl=en#apis-others)
  * [Documentation upgrades and more Manifest V3 guidance](https://developer.chrome.com/blog/extension-news-july-2023?hl=en#new-docs)
  * [💡 Did you know?](https://developer.chrome.com/blog/extension-news-july-2023?hl=en#tips)
  * [Let's connect! 🙌](https://developer.chrome.com/blog/extension-news-july-2023?hl=en#connecting)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  What's happening in Chrome Extensions? 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [New extension APIs and features](https://developer.chrome.com/blog/extension-news-july-2023?hl=en#new-apis)
    * [More API launches](https://developer.chrome.com/blog/extension-news-july-2023?hl=en#apis-others)
  * [Documentation upgrades and more Manifest V3 guidance](https://developer.chrome.com/blog/extension-news-july-2023?hl=en#new-docs)
  * [💡 Did you know?](https://developer.chrome.com/blog/extension-news-july-2023?hl=en#tips)
  * [Let's connect! 🙌](https://developer.chrome.com/blog/extension-news-july-2023?hl=en#connecting)


Amy Steam 
[ GitHub ](https://github.com/amysteam) [ LinkedIn ](https://www.linkedin.com/in/amysteam)
So far, 2023 has been a busy year in the world of Chrome extensions. Your valuable feedback has allowed us to improve the extension platform and our documentation. We also continue collaborating with other browser vendors in the [WebExtensions Community Group](https://github.com/w3c/webextensions/issues) so that extension APIs work more consistently across browsers.
In this post, we’ll share with you a few changes that the Chrome extension team has worked on during the first half of this year and what upcoming features will be released later this quarter. Let's get started!
## New extension APIs and features
In this section, I want to highlight some significant API launches, briefly review other API improvements, and share upcoming API releases.
### Highlights
#### Offscreen documents
The [Offscreen API](https://developer.chrome.com/docs/extensions/reference/offscreen) was introduced in Chrome 109. It allows Manifest V3 extensions to handle use cases that need interaction with the DOM or window, which cannot be performed in the extension service worker. Also, Chrome 114 introduced two additional offscreen reasons: `'WORKERS'` for instances when your document needs to spawn a worker and `'LOCAL_STORAGE'` to help migrate data from `window.localStorage` to the [`chrome.storage` API](https://developer.chrome.com/docs/extensions/migrating/to-service-workers#convert-localstorage). 
Starting in Chrome 115, you can provide multiple reasons when creating an offscreen document. This allows you to perform two related tasks in the same document.
#### New Side Panel API 🎉
In the past, the only way to create sidebars in extensions was by injecting a new element with content scripts on every page. In Chrome 114, the [Side Panel API](https://developer.chrome.com/docs/extensions/reference/api/sidePanel) was launched. Now you can develop a companion sidebar experience for users in a much more straightforward way. Read more about how the [Side Panel API allows you to design a superior user experience](https://developer.chrome.com/blog/extension-side-panel-launch).
Side panel dictionary extension. See the [code](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/functional-samples/sample.sidepanel-dictionary) in the chrome-extensions-samples repository. 
#### More robust Service Workers
All extension events now restart the extension service worker's idle timer. In Chrome 110, the hard five-minute maximum lifetime was removed for extension service workers. Also, messages to [native applications](https://developer.chrome.com/docs/extensions/mv3/nativeMessaging) and [messages within the extension](https://developer.chrome.com/docs/extensions/mv3/messaging) restart the idle timer. Read more about it in [The extension service worker lifecycle](https://developer.chrome.com/docs/extensions/mv3/service_workers/service-worker-lifecycle#timeouts) article.
### More API launches
  * **Action API** : Starting Chrome 110, you can customize the badge text with [`setBadgeTextColor`()](https://developer.chrome.com/docs/extensions/reference/action#method-setBadgeTextColor) and [`getBadgeTextColor()`](https://developer.chrome.com/docs/extensions/reference/action#method-getBadgeTextColor). Also, [`isEnabled()`](https://developer.chrome.com/docs/extensions/reference/action#method-isEnabled) allows you to check if the action is enabled for the current tab.
  * **Commands API** : The bug where extension shortcuts, declared in the manifest under [`"commands._execute_action"`](https://developer.chrome.com/docs/extensions/reference/commands#action-commands), would not persist during conversion to MV3, was fixed in [Chrome 111](https://chromiumdash.appspot.com/commit/a98898b9615f2e454ec02917c720f479f29e673f).
  * **Downloads API** : The default downloads UI in Chrome has moved from a shelf at the bottom to the right side of the omnibox. To disable this behavior, you can use [`downloads.setUiOptions()`](https://developer.chrome.com/docs/extensions/reference/downloads#method-setUiOptions) which replaces `setShelfEnabled()`.
  * **History API** : [`chrome.history.getVisits()`](https://developer.chrome.com/docs/extensions/reference/history#method-getVisits) and [`chrome.history.search()`](https://developer.chrome.com/docs/extensions/reference/history#method-search) also return data from other devices that have been synced to the local history database. This may result in more history entries and higher visit counts. `isLocal` was added to [`VisitItem`](https://developer.chrome.com/docs/extensions/reference/history#type-VisitItem) in Chrome 115 (expected in stable later this month) to be able to filter by local visits only.
  * **Identity API** : The authentication window now appears as a popup, instead of occupying a full application window. To grant more control during the process of JavaScript redirects, we have added two new options: [`abortOnLoadForNonInteractive`](https://developer.chrome.com/docs/extensions/reference/identity#property-WebAuthFlowDetails-abortOnLoadForNonInteractive) and [`timeoutMsForNonInteractive`](https://developer.chrome.com/docs/extensions/reference/identity#property-WebAuthFlowDetails-timeoutMsForNonInteractive).
  * **Storage API** : In Chrome 112 the [`chrome.session`](https://developer.chrome.com/docs/extensions/reference/storage#property-session) storage size was increased to 10MB. Then [`chrome.local`](https://developer.chrome.com/docs/extensions/reference/storage#property-local) storage size was changed to match in Chrome 114.


### Coming soon...
Upcoming Chrome versions will introduce many features to make it easier for extensions to migrate to Manifest V3. For a list of upcoming MV3 migration-related changes, check out our [known issues page](https://developer.chrome.com/docs/extensions/migrating/known-issues#closing-the-platform-gap). Additionally, we plan to add the following features:
  * **DeclarativeNetRequest API** : The default value for the [isUrlFilterCaseSensitive](https://developer.chrome.com/docs/extensions/reference/declarativeNetRequest#property-RuleCondition-isUrlFilterCaseSensitive) property will change to `false`. See the [WECG](https://github.com/w3c/webextensions/issues/269) thread.
  * The **File Handling API** will allow ChromeOS extensions to open files with specified MIME types and file extensions. This feature is currently [behind a flag](https://developer.chrome.com/docs/extensions/whatsnew#the-file-handling-api-comes-to-chromeos).
  * **Runtime API** : We are releasing [`runtime.getContexts()`](https://developer.chrome.com/docs/extensions/reference/runtime#method-getContexts) to replace `extension.getViews()`, which is deprecated. This will allow extensions to determine if an extension page like the side panel or offscreen document is open. See the [WECG](https://github.com/w3c/webextensions/blob/main/proposals/runtime_get_contexts.md) proposal.
  * **Service workers** : We're adding strong keep-alives to Chrome APIs that display a user prompt: [`permissions.request()`](https://developer.chrome.com/docs/extensions/reference/permissions#method-request), [`desktopCapture.chooseDesktopMedia()`](https://developer.chrome.com/docs/extensions/reference/desktopCapture#method-chooseDesktopMedia), [`identity.launchWebAuthFlow()`](https://developer.chrome.com/docs/extensions/reference/identity#method-launchWebAuthFlow), and [`management.uninstall()`](https://developer.chrome.com/docs/extensions/reference/management#method-uninstall).
  * **Side Panel API** : We're launching [`sidepanel.open()`](https://developer.chrome.com/docs/extensions/reference/sidepanel#method-open), which will open the extension side panel programmatically in response to a user gesture, such as a context menu click.
  * **TabCapture API** : We're adding the ability to call `getMediaStreamId()` from the extension service worker and obtain a MediaStream from a stream ID in an offscreen document. See [Audio recording and screen capture](https://developer.chrome.com/docs/extensions/mv3/screen_capture) for examples.


Stay tuned to the [What's new in extensions](https://developer.chrome.com/docs/extensions/whatsnew) page for these announcements as soon as they are made available in [Chrome Beta](https://chromestatus.com/roadmap).
## Documentation upgrades and more Manifest V3 guidance
We've also been working hard to improve the developer's learning experience. Big thanks to all of you who took the time to ask questions on the [chromium-group](https://groups.google.com/a/chromium.org/g/chromium-extensions) and report documentation issues on [developer.chrome.com](https://github.com/GoogleChrome/developer.chrome.com/issues).
### Highlights
  * The new [MV3 Migration](https://developer.chrome.com/docs/extensions#migrate-from-manifest-v2-to-manifest-v3) section provides practical ways to convert Manifest V2 extensions to Manifest V3.
  * The [Extension service workers](https://developer.chrome.com/docs/extensions#service-workers) guide provides detailed information on extension service workers topics. These include how they are registered and updated, what the lifecycle looks like, how imports work, and more.
  * The [Handle events with service workers](https://developer.chrome.com/docs/extensions/mv3/getstarted/tut-quick-reference) tutorial teaches the basics of extension service workers. It builds an omnibox extension that gives you quick access to extension API reference pages.


### More updates
  * [Using Google Analytics 4](https://developer.chrome.com/docs/extensions/mv3/tut_analytics) demonstrates how to track the usage of your extension popup and service worker events.
  * [Using geolocation](https://developer.chrome.com/docs/extensions/mv3/geolocation) shows how to obtain the geographical location of the extension using the Offscreen API.
  * [Audio recording and screen capture](https://developer.chrome.com/docs/extensions/mv3/screen_capture) teaches how to capture audio and video from tabs, windows, or screens using `chrome.tabCapture` and `navigator.mediaDevices.getDisplayMedia()` APIs.
  * We've added new debugging tips to the [Debugging extensions](https://developer.chrome.com/docs/extensions/mv3/tut_debugging) guide.
  * We've updated the [Permission warnings guidelines](https://developer.chrome.com/docs/extensions/mv3/permission_warnings) to make it easier to understand how permission warnings work and how you can provide a better user experience. Also, there are practical ways to check what warnings the user will see.
  * Our team and contributors have also added new Manifest V3 extension samples: [WASM in extensions](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/functional-samples), [Scripting API demo](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/api-samples/scripting), [Side Panel API cookbooks](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/functional-samples), and [DeclarativeNetRequest API samples](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/api-samples/declarativeNetRequest). You can explore other extension samples in our [GitHub samples repo](https://github.com/GoogleChrome/chrome-extensions-samples).


### Coming soon...
  * How to migrate remote hosted code to Manifest V3.
  * How to run automated tests for Chrome extensions.
  * Improved Declarative Net Request guidance.
  * Improvements to the content script explainer.


## 💡 Did you know?
Before we wrap up, we wanted to share a couple of useful tools and insights:
  * Chrome started work on supporting [WebHID](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/functional-samples/sample.co2meter); you can play around with the API starting Chrome 115 (but be aware that it's still a work in progress).
  * [Puppeteer](https://pptr.dev/guides/chrome-extensions) now supports testing in headless mode using `--headless=new` . Read more about it on [Chrome's headless mode upgrade](https://developer.chrome.com/articles/new-headless) blog post.
  * With the [Extension Update Testing Tool](https://github.com/GoogleChromeLabs/extension-update-testing-tool), you can check what warnings are triggered when permissions change in the manifest. This way, you can experience the update process as a user would. This is important because some permissions might disable the extension until the user grants access again.


## Let's connect! 🙌
This year, the extension team was happy to meet extension developers in person during [Google I/O Connect](https://youtu.be/634qUJ0rJ8I) events. We are working on creating new spaces to connect with you, such as launching focus groups and meetup events.
In the meantime, please continue to ask questions on the [chromium-groups](https://groups.google.com/a/chromium.org/g/chromium-extensions), consider participating on the [WECG](https://github.com/w3c/webextensions/issues), and report any documentation issues on the [developer.chrome.com GitHub repo](https://github.com/GoogleChrome/developer.chrome.com/issues).
Thanks again for being a part of the extension developer community!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2023-07-13 UTC.

