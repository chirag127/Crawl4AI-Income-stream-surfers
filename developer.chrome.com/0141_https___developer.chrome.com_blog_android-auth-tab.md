---
url: https://developer.chrome.com/blog/android-auth-tab?hl=en
title: https://developer.chrome.com/blog/android-auth-tab?hl=en
date: 2025-05-11T16:53:48.719732
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/android-auth-tab?hl=en#main-content)


  * On this page
  * [Auth Tab versus Custom Tabs](https://developer.chrome.com/blog/android-auth-tab?hl=en#auth_tab_versus_custom_tabs)
  * [Migrate to Auth Tab](https://developer.chrome.com/blog/android-auth-tab?hl=en#migrate_to_auth_tab)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  Improve your web-based sign-in flow with Auth Tab for Android 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Auth Tab versus Custom Tabs](https://developer.chrome.com/blog/android-auth-tab?hl=en#auth_tab_versus_custom_tabs)
  * [Migrate to Auth Tab](https://developer.chrome.com/blog/android-auth-tab?hl=en#migrate_to_auth_tab)


Streamline your web-based sign-in flow on Android with the new Auth Tab, available from Chrome 132. Auth Tabs optimize the [Custom Tab](https://developer.chrome.com/docs/android/custom-tabs) experience for tasks, such as authentication, requiring minimal UI and offer a more secure callback mechanism.
Auth Tab is a specialized Custom Tab that is purpose-built to handle authentication. It provides all the core benefits of Custom Tabs tailored for app developer integrations that want a stripped-down browser experience focused on web content. It uses idiomatic Android APIs and provides enhanced security for your applications. In addition, Auth Tab has the ability to automatically fall back to standard Custom Tabs when it is not available on a user's device.
If you're using Custom Tabs to handle browser-based authentication, upgrading to Auth Tab is straightforward. Auth Tabs are available starting with Chrome 132 and they'll automatically fall back to the default Custom Tabs experience for earlier versions of Chrome. If you are developing a new authentication process, Auth Tab is the way to go.
## Auth Tab versus Custom Tabs
Custom Tabs provides a dedicated, in-app browser experience that can help increase and focus user engagement and greatly simplify implementation details for the Android developer. Authentication strategies built on Custom Tabs offer a vast improvement from prior solutions, but challenges still remain:
  * Communication between the browser tab and the app relies on [Activity intents](https://developer.android.com/guide/components/intents-filters), which can expose your app to potential interference to your intent
  * Using Activity intents to manage information transfer from the tab is less idiomatic than using Android APIs


Auth Tab solves these problems. A dedicated callback adds a layer of security and eliminates the need for Activity intents. The browser interface, meanwhile, eliminates some Chrome features such as the minimize button to create a more authentic authorization experience for users.
**Figure 1.** Custom Tab full featured. **Figure 2.** Auth Tab with minimal capabilities.
## Migrate to Auth Tab
Auth Tab was introduced in Chrome 132 and requires the [AndroidX](https://developer.android.com/jetpack/androidx/releases/browser) browser auth library.
Migrate your existing Custom Tabs authentication strategy into Auth Tab by changing only a few lines of code. A complete developer's guide is available in [Chrome Custom Tabs documentation](https://developer.chrome.com/docs/android/custom-tabs).
A working Auth Tab demo, complete with a fallback to standard Custom Tabs authentication, can be found in the [Android Browser Helper](https://github.com/GoogleChrome/android-browser-helper/tree/main/demos) library.
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-01-31 UTC.

