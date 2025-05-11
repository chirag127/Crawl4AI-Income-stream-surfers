---
url: https://developer.chrome.com/blog/extension-safety-hub?hl=en
title: https://developer.chrome.com/blog/extension-safety-hub?hl=en
date: 2025-05-11T16:56:01.641493
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/extension-safety-hub?hl=en#main-content)
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


#  Bringing Safety check to the chrome://extensions page 
Stay organized with collections  Save and categorize content based on your preferences. 
Oliver Dunk 
[ GitHub ](https://github.com/oliverdunk) [ Bluesky ](https://bsky.app/profile/oliverdunk.com) [ Homepage ](https://oliverdunk.com)
Starting in Chrome 117, Chrome will proactively highlight to users when an extension they have installed is no longer in the Chrome Web Store. This is limited to three specific cases:
  * The extension has been unpublished by the developer.
  * The extension has been taken down for violating Chrome Web Store policy.
  * The item was marked as malware.


We have designed this change to keep the ecosystem safe for users while limiting the chances that this will impact genuine extensions. If an issue is resolved, the notification is automatically cleared. The notification will not be displayed for an extension when the developer has been [notified of a possible violation](https://developer.chrome.com/docs/webstore/review-process/#warning) and has been given time to address the issue or appeal.
Users are most likely to encounter this feature in the "Privacy and security" section of the settings page.
Chrome will highlight these extensions in the "Privacy and security" settings. 
When a user clicks "Review", they will be taken to their extensions and given the choice to either remove the extension or hide the warning if they wish to keep the extension installed. As in previous versions of Chrome, extensions marked as malware are automatically disabled.
Two extensions that are no longer present in the Chrome Web Store show on the chrome://extensions page. 
As mentioned, we hope this change will help to keep the ecosystem safe without impacting genuine extensions.
If you have any feedback, we'd love to hear. Consider posting in the [chromium-extensions](https://groups.google.com/a/chromium.org/g/chromium-extensions) mailing list where we'll be looking out for your thoughts.
_Photo by[Nicolás Flor](https://unsplash.com/@nicolassflorr?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/photos/hOWxbQAuC00?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)_
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2023-08-16 UTC.

