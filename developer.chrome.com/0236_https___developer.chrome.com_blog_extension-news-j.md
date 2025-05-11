---
url: https://developer.chrome.com/blog/extension-news-january-2024?hl=en
title: https://developer.chrome.com/blog/extension-news-january-2024?hl=en
date: 2025-05-11T16:55:46.405447
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/extension-news-january-2024?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/extension-news-january-2024?hl=es-419)




  * On this page
  * [User Scripts API](https://developer.chrome.com/blog/extension-news-january-2024?hl=en#user_scripts_api)
  * [Reading List API](https://developer.chrome.com/blog/extension-news-january-2024?hl=en#reading_list_api)
  * [Declarative Net Request API safe rules](https://developer.chrome.com/blog/extension-news-january-2024?hl=en#declarative_net_request_api_safe_rules)
  * [Other API launches](https://developer.chrome.com/blog/extension-news-january-2024?hl=en#other_api_launches)
    * [File Handling API](https://developer.chrome.com/blog/extension-news-january-2024?hl=en#file_handling_api)
    * [Cross-browser compatibility enhancements](https://developer.chrome.com/blog/extension-news-january-2024?hl=en#cross-browser_compatibility_enhancements)
  * [Upcoming features...](https://developer.chrome.com/blog/extension-news-january-2024?hl=en#upcoming_features)
  * [Documentation updates](https://developer.chrome.com/blog/extension-news-january-2024?hl=en#documentation_updates)
    * [New video: exploring the platform evolution with Simeon](https://developer.chrome.com/blog/extension-news-january-2024?hl=en#new_video_exploring_the_platform_evolution_with_simeon)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  What's happening in Chrome Extensions? 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [User Scripts API](https://developer.chrome.com/blog/extension-news-january-2024?hl=en#user_scripts_api)
  * [Reading List API](https://developer.chrome.com/blog/extension-news-january-2024?hl=en#reading_list_api)
  * [Declarative Net Request API safe rules](https://developer.chrome.com/blog/extension-news-january-2024?hl=en#declarative_net_request_api_safe_rules)
  * [Other API launches](https://developer.chrome.com/blog/extension-news-january-2024?hl=en#other_api_launches)
    * [File Handling API](https://developer.chrome.com/blog/extension-news-january-2024?hl=en#file_handling_api)
    * [Cross-browser compatibility enhancements](https://developer.chrome.com/blog/extension-news-january-2024?hl=en#cross-browser_compatibility_enhancements)
  * [Upcoming features...](https://developer.chrome.com/blog/extension-news-january-2024?hl=en#upcoming_features)
  * [Documentation updates](https://developer.chrome.com/blog/extension-news-january-2024?hl=en#documentation_updates)
    * [New video: exploring the platform evolution with Simeon](https://developer.chrome.com/blog/extension-news-january-2024?hl=en#new_video_exploring_the_platform_evolution_with_simeon)


Amy Steam 
[ GitHub ](https://github.com/amysteam) [ LinkedIn ](https://www.linkedin.com/in/amysteam)
Happy New Year from the extension team! Hope you had a fantastic end of the year, whether you spent it relaxing or exploring some of the new features we announced in the [October 2023 blog post](https://developer.chrome.com/blog/extension-news-october-2023). We also want to take a moment to thank you for all your feedback and for being part of the extension community.
Let's dive into the features launched in the last quarter of 2023 and take a sneak peek at some new features coming in early 2024.
## User Scripts API
Starting with Chrome 120, Manifest V3 extensions can use the [User Scripts API](https://developer.chrome.com/docs/extensions/reference/api/userScripts) to manage the collection of user scripts and determine when and how to inject them on web pages. For a quick start, check out the [User Scripts API sample](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/api-samples/userScripts).
## Reading List API
The [Reading List API](https://developer.chrome.com/docs/extensions/reference/api/readingList), also launched in Chrome 120, allows developers to create, read, update, and delete metadata located in the Reading List side panel. Check out the [Reading List API demo](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/api-samples/readingList).
## Declarative Net Request API safe rules
Based on your [feedback](https://github.com/w3c/webextensions/issues/318), we significantly increased the limit on enabled static rulesets from 10 to 50. Additionally, we doubled the total number of allowed static rulesets from 50 to 100. Check out [Improving content filtering in Manifest V3](https://developer.chrome.com/blog/improvements-to-content-filtering-in-manifest-v3) for more details.
## Other API launches
### Cookies API
In Chrome 119, the [Cookies API](https://developer.chrome.com/docs/extensions/reference/api/cookies) was updated with support for [partitioning](https://developers.google.com/privacy-sandbox/3pcd/chips). You can now specify the [`partitionKey`](https://developer.chrome.com/docs/extensions/reference/api/cookies#property-Cookie-partitionKey) attribute to specify the partition to perform an operation on.
### File Handling API
The [File Handling API](https://developer.chrome.com/docs/extensions/how-to/web-platform/file-handling-chromeos) is now available for ChromeOS 120, allowing extensions to open files with specified MIME types and file extensions similar to web platform file handling. 
### Push API
Starting Chrome 121, extensions can use the [Push API](https://developer.mozilla.org/docs/Web/API/Push_API) to receive messages from a server without showing notifications. This means WebSockets aren't the only method for server-to-extension communication anymore. It's worth noting that the Push API has been optimized to function seamlessly with extension service workers. This includes the ability to activate a service worker when a message is received. Try the [Push API sample](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/functional-samples/cookbook.push).
### Cross-browser compatibility enhancements
We continue to work with other browser vendors to enhance cross-browser compatibility. In response to your [feedback](https://github.com/w3c/webextensions/issues/282#issuecomment-1443396585) in the WECG starting Chrome 121 when you include the background.scripts, background.page, or background.persistent to the manifest in your MV3 extension, it will only trigger a warning instead of an error (see [issue 1418934](https://crbug.com/1418934)). The [tabs.Tab.lastAccessed](https://developer.chrome.com/docs/extensions/reference/api/tabs#property-Tab-lastAccessed) property was also added to make extensions more compatible with Firefox (see [issue 1419613](https://bugs.chromium.org/p/chromium/issues/detail?id=1419613)).
## Upcoming features...
  * [WebAuthn API](https://developer.mozilla.org/docs/Web/API/Web_Authentication_API): Extensions will be able to assert RP IDs for websites where they have host permissions. See [this email](https://lists.w3.org/Archives/Public/public-webauthn/2023Dec/0078.html) for context.
  * All asynchronous **Chrome API methods will support promises** for easier use unless the function signature isn't compatible with promises, like `chrome.desktopCapture.chooseDesktopMedia()`. Callbacks will still work for backward compatibility.


## Documentation updates
A major goal for us last year was improving the Chrome Extensions documentation. This included adding more getting started guidance, how-to guides, and publishing a new MV3 migration guide. At the end of last year we took the next big step: we've started reorganizing to better serve the needs of users.
Here's an overview of what's new:
  * Streamlined navigation and improved structure for easy access to extension and Chrome web store articles.
  * Added sidebar filter for quick topic access. For example, on the [Reference API](https://developer.chrome.com/docs/extensions/reference/api) page you can filter by "tab" to see all tabs-related APIs.

Filtering API reference by name
  * A friendlier learning journey for new extension developers.

Getting started page
  * One-click code snippet copying.

Copying code
  * Support of dark mode for a better viewing experience in low-light settings.

Dark mode toggle on documentation
  * Added collections so that you can quickly find frequently used reference pages.

Expanded collection drop-down
This is the first step in improving documentation. We plan to add new reference content, conceptual articles, and tutorials, as well as updating outdated content. [Let us know](https://issuetracker.google.com/issues/new?component=1400036&template=1897236) what you think so we can continue improving.
### Upcoming guides
  * User Scripts API tutorial.
  * New Real-time updates guidance exploring different ways of handling notifications from server-side events.
  * New additions to the [How to](https://developer.chrome.com/docs/extensions/how-to) section.


### New video: exploring the platform evolution with Simeon
Simeon Vincent, co-chair of the Web Extensions Community Group (WECG) sat down together with our DevRel team to discuss the intricacies and future of web extensions.
The conversation focused on:
  * Standardizing extension behaviors across browsers.
  * Tackling the development challenges of transitioning to Manifest V3.
  * How extensions are integrating AI into extensions.


### More updates
  * Learn to use the [WebHID](https://developer.chrome.com/docs/extensions/how-to/web-platform/webhid) API in extensions, to connect to standard devices like keyboards and unique ones like gaming gloves or eye-tracking devices.
  * Learn to use the [WebUSB](https://developer.chrome.com/docs/extensions/how-to/web-platform/webusb) API in extensions to connect to USB devices like flash drives, barcode scanners, robotics controllers, and USB microscopes.
  * Migrating your extension to Manifest Version 3 means your extension cannot use JavaScript code from an external server. Check out the [remotely hosted code guide](https://developer.chrome.com/docs/extensions/develop/migrate/remote-hosted-code) that provides guidance for remote code alternatives, preventing your extension from receiving a [Blue Argon](https://developer.chrome.com/docs/webstore/troubleshooting#additional-requirements-for-manifest-v3) Chrome Web Store rejection.


Thank you once again for your dedication to the extension developer community. In 2024, your insights and feedback will be crucial in shaping and enhancing the extension ecosystem. We're looking forward to another year of progress with your support.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-01-23 UTC.

