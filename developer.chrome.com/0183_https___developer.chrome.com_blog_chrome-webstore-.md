---
url: https://developer.chrome.com/blog/chrome-webstore-rollback?hl=en
title: https://developer.chrome.com/blog/chrome-webstore-rollback?hl=en
date: 2025-05-11T16:54:35.872438
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/chrome-webstore-rollback?hl=en#main-content)
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


#  Version rollbacks in the Chrome Web Store Developer Dashboard 
Stay organized with collections  Save and categorize content based on your preferences. 
Zach Warneke 
This week we're excited to launch a new feature that lets developers roll back their extensions to the previous published version in the Chrome Web Store. Our goal is to give developers increased peace-of-mind when publishing updates, especially with the transition to Manifest V3.
## My extension has a live bug, what now?
From today, you don't need to submit a new version of your extension with a bug fix and wait for it to pass review. Instead, you can initiate a rollback through the **more** menu or the package page for your item.
A rollback requires a new version number under which the previous version of your extension will be re-published and a reason for the rollback. After filling in the required information, confirm the rollback.
Once the rollback is finished, the rolled-back package will be pushed to users through the normal Chrome auto-update process. You can verify that the rollback was successful on the package page or status page.
Refer to the [rollback documentation](https://developer.chrome.com/docs/webstore/rollback) for more information, including how we handle rollbacks in certain special cases. The version rollback feature is live now, and the Chrome Web Store team is looking forward to continuing to improve the rollout management process for developers.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-04-09 UTC.

