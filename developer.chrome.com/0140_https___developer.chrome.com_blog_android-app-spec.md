---
url: https://developer.chrome.com/blog/android-app-specific-history?hl=en
title: https://developer.chrome.com/blog/android-app-specific-history?hl=en
date: 2025-05-11T16:53:48.708124
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/android-app-specific-history?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/android-app-specific-history?hl=es-419)




  * On this page
  * [Benefits for users](https://developer.chrome.com/blog/android-app-specific-history?hl=en#benefits_for_users)
  * [Good for developers, too](https://developer.chrome.com/blog/android-app-specific-history?hl=en#good_for_developers_too)
  * [Get started with App-specific history today](https://developer.chrome.com/blog/android-app-specific-history?hl=en#get_started_with_app-specific_history_today)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  Deepen user engagement with App-specific history in Chrome Custom Tabs 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Benefits for users](https://developer.chrome.com/blog/android-app-specific-history?hl=en#benefits_for_users)
  * [Good for developers, too](https://developer.chrome.com/blog/android-app-specific-history?hl=en#good_for_developers_too)
  * [Get started with App-specific history today](https://developer.chrome.com/blog/android-app-specific-history?hl=en#get_started_with_app-specific_history_today)


From Chrome 126, a new feature in Chrome Custom Tabs on Android enhances the web experience for users and developers alike. With App-specific history, Android users can see browsing history specific to an app and act upon it in both the custom tab as well as Chrome.
For users, this makes finding and returning to content simpler than ever. They can continue to act on the inspiration originating from an app whether it be unanswered questions, incomplete shopping journeys, and more complex tasks that keep users coming back to Chrome and your app.
In order for this to work, though, developers need to opt-in. Specifically, you'll need to share your app package name with Chrome. Read more to find out the benefits of opting in for both you and your app's users.
## How it works
App-specific history provides an entry point for users to view links opened in an app's custom tab. It lets Chrome users resume their browsing session from inside the Chrome app. Links from the originating app are grouped in Chrome's history, making it easier for users to find and return to a previously visited page.
App-specific history is enabled by using [setShareIdentityEnabled](https://developer.android.com/reference/android/app/ActivityOptions#setShareIdentityEnabled\(boolean\)). When used on a CustomTabsIntent, the API grants Chrome access to the host app's package name. This lets Chrome identify the Chrome Custom Tabs session and tag history entries.
## Benefits for users
On mobile, users often have trouble returning to the content they have previously viewed. Browsers like Chrome maintain history, but many apps have embedded web experiences as well, making the history harder to scan and find. Existing solutions, like bookmarks, only go so far.
With App-specific history, users can quickly find and return to web content. This lets them continue their journey if they have already associated that product detail page or news article seen in content from your app. They'll be able to better filter down and understand the origins of the links in their history and see links reflected in both Chrome and the host app. Over time, users begin to rely on the seamless journeys between app and Chrome that make the two a helpful destination for those multi-session complex tasks.
**Figure 1.** Chrome History. **Figure 2.** In-App Custom Tab Overflow Menu.
## Good for developers, too
App-specific history is a win for you as an app developer helping you to grow traffic and engagement within your app. Adding history and seamless transitions to Chrome discourages app abandonment and cases where users attempt to open custom tab content outside the app in a standalone browser.
Within the app, you get a free surface and launchpad into previous intent, campaigns and other high-quality interactions from most engaged users that go deeper on the content. Within Chrome, apps get branding and visibility that helps users revisit dormant tasks that require them to revisit your app.
App-specific history provides robust experiences and increases users' investment and productivity within the apps. Those who choose to opt-in are certain to see a benefit from an enhanced user experience.
## Get started with App-specific history today
To get started with App-specific history, additional documentation and code can be found in the [Android Browser Helper](https://github.com/GoogleChrome/android-browser-helper) library. The API is specific to devices running Chrome and Android 14+.
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-01-31 UTC.

