---
url: https://developer.chrome.com/blog/extension-news-april-2024?hl=en
title: https://developer.chrome.com/blog/extension-news-april-2024?hl=en
date: 2025-05-11T16:55:46.409902
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/extension-news-april-2024?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/extension-news-april-2024?hl=es-419)




  * On this page
  * [Chrome Web Store version rollback](https://developer.chrome.com/blog/extension-news-april-2024?hl=en#chrome_web_store_version_rollback)
  * [Firebase Auth SDK now supports extensions](https://developer.chrome.com/blog/extension-news-april-2024?hl=en#firebase_auth_sdk_now_supports_extensions)
  * [Other API launches](https://developer.chrome.com/blog/extension-news-april-2024?hl=en#other_api_launches)
  * [Upcoming features](https://developer.chrome.com/blog/extension-news-april-2024?hl=en#upcoming_features)
  * [Documentation updates](https://developer.chrome.com/blog/extension-news-april-2024?hl=en#documentation_updates)
  * [WECG March meet-up update](https://developer.chrome.com/blog/extension-news-april-2024?hl=en#wecg_march_meet-up_update)
  * [🗃️ Unpacking the Chrome Extension Review](https://developer.chrome.com/blog/extension-news-april-2024?hl=en#🗃️_unpacking_the_chrome_extension_review)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  What's happening in Chrome Extensions? 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Chrome Web Store version rollback](https://developer.chrome.com/blog/extension-news-april-2024?hl=en#chrome_web_store_version_rollback)
  * [Firebase Auth SDK now supports extensions](https://developer.chrome.com/blog/extension-news-april-2024?hl=en#firebase_auth_sdk_now_supports_extensions)
  * [Other API launches](https://developer.chrome.com/blog/extension-news-april-2024?hl=en#other_api_launches)
  * [Upcoming features](https://developer.chrome.com/blog/extension-news-april-2024?hl=en#upcoming_features)
  * [Documentation updates](https://developer.chrome.com/blog/extension-news-april-2024?hl=en#documentation_updates)
  * [WECG March meet-up update](https://developer.chrome.com/blog/extension-news-april-2024?hl=en#wecg_march_meet-up_update)
  * [🗃️ Unpacking the Chrome Extension Review](https://developer.chrome.com/blog/extension-news-april-2024?hl=en#🗃️_unpacking_the_chrome_extension_review)


Amy Steam 
[ GitHub ](https://github.com/amysteam) [ LinkedIn ](https://www.linkedin.com/in/amysteam)
The first three months of the year have been productive for the extensions team. We've rolled out several significant updates and new features that we're excited to share with you. But one particular Chrome Web Store addition has been hugely anticipated—a feature that will improve your publishing experience.
## Chrome Web Store version rollback
Last week, the Chrome Web Store added a new feature that lets you go back to an older version of your extension more quickly. If your latest update didn't go as planned and you want to fix it fast, provide a new version number for the previous version and a reason why. We'll publish the previous version in minutes—no need to wait for your item to be reviewed. This way, your user can get a working version right away.
Modal requesting details for a version rollback.
Want to know more about how version rollback works? Check out our [blog post](https://developer.chrome.com/blog/chrome-webstore-rollback) and the [step-by-step guide](https://developer.chrome.com/docs/webstore/rollback) on reverting to a previous version.
## Firebase Auth SDK now supports extensions
In February, the Firebase team rolled out the first-ever Web Extensions entry point in the [JS SDK v10.8.0](https://firebase.google.com/support/release-notes/js#version_1080_-_february_1_2024) release. It addresses a longstanding issue that has led to some extensions being rejected from the Chrome Web Store due to using [remotely hosted code](https://developer.chrome.com/docs/extensions/develop/migrate/remote-hosted-code) for Firebase Auth.
The new Web Extensions version of the Firebase SDK bundles all required code, eliminating the need for remote hosting. This solves the policy compliance challenge that extension developers have faced. This change applies specifically to Firebase Auth, but it sets the stage for addressing other extension-specific issues.
The Firebase team has [worked closely with the extension developer community](https://github.com/firebase/firebase-js-sdk/issues/7617#issuecomment-1740008013) to deliver this much-needed solution. They are dedicated to ongoing collaboration and welcome [feedback](https://github.com/firebase/firebase-js-sdk/issues) from extension developers on ways the Firebase SDK can be further optimized for extensions. For more details, see the [PSA announcement in the Extension's Google Group post](https://groups.google.com/a/chromium.org/g/chromium-extensions/c/7TVc58ARcVE/m/O-CbmCsGAQAJ).
## Other API launches
  * From Chrome 124, service workers support WebGPU. This improves the implementation experience for developers interested in building AI extensions. For a quick start, check out the [WebGPU extension sample](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/functional-samples/sample.webgpu/).
  * In Chrome 123, alarms set using the Alarms API are no longer delayed [when a device goes to sleep](https://developer.chrome.com/docs/extensions/reference/api/alarms#device_sleep). When the device wakes up, the alarm will fire once, no matter how many alarms are missed.
  * If you rely on a port remaining open throughout the lifetime of a page, you may need to make changes to reconnect when a page is restored. Learn more about the changes made to the bfcache behavior in Chrome 123 in the [Changes to BFCache](https://developer.chrome.com/blog/bfcache-extension-messaging-changes) blog post.
  * CIDR Block Filtering in [Events API](https://developer.chrome.com/docs/extensions/reference/api/events): In Chrome 123, developers can now use Classless Inter-Domain Routing (CIDR) blocks for more efficient event filtering. This update eliminates the need for the tedious task of creating individual filter rules for each IP address within a range. By adopting CIDR notation, you can succinctly specify a range of IP addresses, allowing for streamlined management of event triggers by IP ranges.
  * In Chrome 123 the [tabs.Tab](https://developer.chrome.com/docs/extensions/reference/api/tabs#type-Tab)'s property [`windowId`](https://developer.chrome.com/docs/extensions/reference/api/tabs#property-Tab-windowId) can have a value of -1 to indicate that the tab does not belong to a browser window. This is often the case for pre-rendered tabs, which are loaded in the background to speed up browsing but are not yet visible in any window.
  * [WebAuthn API](https://developer.mozilla.org/docs/Web/API/Web_Authentication_API): Extensions are now able to assert RP IDs for websites where they have host permissions. See [the email](https://lists.w3.org/Archives/Public/public-webauthn/2023Dec/0078.html) for context.
  * All asynchronous Chrome API methods support promises for easier use unless the function signature isn't compatible with promises, like `chrome.desktopCapture.chooseDesktopMedia()`. Callbacks will still work for backward compatibility.


## Upcoming features
Future plans include adding more features to the UserScripts API. Learn about `userScripts.execute()` in this [WECG proposal](https://github.com/w3c/webextensions/blob/main/proposals/user-scripts-execute-api.md).
## Documentation updates
  * The [Web Push guide](https://developer.chrome.com/docs/extensions/how-to/integrate/web-push) describes how you can add push notifications and send messages from your server to your extension service worker using any Push provider.
  * [Test service worker termination with Puppeteer](https://developer.chrome.com/docs/extensions/how-to/test/test-serviceworker-termination-with-puppeteer): In this guide, you'll learn how to test the service worker of a Chrome extension using Puppeteer. You'll set up a test suite, write tests to validate service worker messaging, handle unexpected service worker termination, and learn best practices for building robust service worker code.
  * The [Chrome Web Store Publish API](https://developer.chrome.com/docs/webstore/using-api) documentation has been updated! This API lets you programmatically create, update, and publish extensions in the Chrome Web Store. The new documentation covers obtaining access tokens, making HTTP requests with the OAuth 2.0 Playground, and more. Check it out to streamline your Chrome Web Store publishing workflow.
  * The [documentScan API](https://developer.chrome.com/docs/extensions/reference/api/documentScan) reference page was recently updated to include [advanced scanning](https://developer.chrome.com/docs/extensions/reference/api/documentScan#complex_scanning) use cases for ChromeOS extensions.


## WECG March meet-up update
In March, the team met with representatives from Safari, Firefox, and Edge as well as a number of major extensions in the inaugural Web Extensions Community Group summit. Hosted by the Apple team in San Diego California, the WECG covered how to improve platform inconsistencies, nuanced aspects of permission systems, aiming to strike a balance between user privacy and developer needs. We couldn't be happier with how this event went, and our team is excited to reconvene this September in Anaheim, California, for TPAC 2024.
## Syntax podcast
Oliver from our team recently appeared as a guest on the Syntax podcast. Tune in to hear about the changes in Manifest V3, review in the Chrome Web Store and more.
## 🗃️ Unpacking the Chrome Extension Review
We met with the Chrome Web Store review team in person to film a video about the intricacies of the review process. We collected all the questions and feedback you shared on this [extensions forum post](https://groups.google.com/a/chromium.org/g/chromium-extensions/c/wFRf2dBKvwM) and used it on the day. The session will be featured on the [Chrome for Developers Youtube Channel](https://www.youtube.com/channel/UCnUYZLuoy1rq1aVMwx4aTzw).
Thanks again for being part of the extensions community, and continue to be awesome! ❤️
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-04-16 UTC.

