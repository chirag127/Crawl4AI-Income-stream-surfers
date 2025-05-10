---
url: https://docs.expo.dev/distribution/app-stores
title: https://docs.expo.dev/distribution/app-stores
date: 2025-04-30T17:13:11.514887
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# App stores best practices
Learn about the best practices when submitting an app to the app stores.
This guide offers best practices for submitting your app to the app stores. To learn how to generate native binaries for submission, see [Create your first build](https://docs.expo.dev/build/setup).
> Disclaimer: Review guidelines and rules are updated frequently, and enforcement of various rules can sometimes be inconsistent. There is no guarantee that your particular project will be accepted by either platform, and you are ultimately responsible for your app's behavior. That said, you can re-submit your app as needed to address feedback from reviews.
[Versioning your appLearn how to configure native runtime versions for your apps.](https://docs.expo.dev/build-reference/app-versions) [App Store presenceManage your Apple App Store metadata from the command line.](https://docs.expo.dev/eas/metadata) [PermissionsRefine native permissions and system dialog messages by using app config.](https://docs.expo.dev/guides/permissions) [App iconsApp stores have strict rules for home screen icons.](https://docs.expo.dev/develop/user-interface/splash-screen-and-app-icon) [Splash screenCreate a seamless loading experience using the splash screen API.](https://docs.expo.dev/develop/user-interface/splash-screen-and-app-icon) [App store assetsLearn how to create screenshots and previews for your app's store pages.](https://docs.expo.dev/guides/store-assets) [Localizing your appPrepare versions of your app for different languages and regions.](https://docs.expo.dev/guides/localization) [Apple: Review guidelinesOfficial Apple guide on preparing your app for App Store review.](https://developer.apple.com/distribute/app-review/)
## Responsive design
It's a good idea to test your app on a device or simulator with a small screen (for example, an iPhone SE) and a large screen (for example, an iPhone X). Ensure your components render the way you expect, no buttons are blocked, and all text fields are accessible.
Try your app on tablets in addition to handsets. Even if you have `ios.supportsTablet: false` configured, your app will still render at phone resolution on iPads and must be usable.
> Apple may reject your app if elements don't render properly on an iPad, even if your app doesn't target the iPad form factor. Be sure and test your app on an iPad (or iPad simulator).
## Privacy policy
Starting October 3, 2018, all new iOS apps and app updates will be required to have a privacy policy to pass the App Store Review Guidelines.
### App privacy questions
Beginning December 8, 2020, new app submissions and updates are required to provide information about their privacy practices in App Store Connect. See [App privacy details on the App Store](https://developer.apple.com/app-store/app-privacy-details/) for more information.
Apple will ask you a series of questions when you submit the app. Depending on which libraries you use, your answers may vary. For example, if you use `expo-updates`, you will need to say Yes, we collect data from this app and then you will want to select Crash Data.

