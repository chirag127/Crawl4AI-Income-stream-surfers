---
url: https://expo.dev/changelog/2023-09-28-new-xcode-ios
title: https://expo.dev/changelog/2023-09-28-new-xcode-ios
date: 2025-04-30T17:18:38.419387
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [Xcode 15 and iOS 17](https://expo.dev/changelog/2023-09-28-new-xcode-ios)
Sep 28, 2023 by
Brent Vatne
Xcode 15 and iOS 17 were released on Monday, September 18th. Since then, we've released the following improvements to our tools and services in order to fully support these new versions.
## [Added Xcode 15 image on EAS Build ](https://expo.dev/changelog/2023-09-28-new-xcode-ios#added-xcode-15-image-on-eas-build)
Use Xcode 15 on EAS Build by setting the `ios.image` field on your build profile to [`macos-ventura-13.6-xcode-15.0`](https://docs.expo.dev/build-reference/infrastructure/#ios-server-images). Alternatively, use the alias that currently points to it: `latest`. [Learn more](https://docs.expo.dev/build-reference/infrastructure/#ios-server-images).
The default Xcode version for currently released SDK versions (Xcode 14.3 for SDK 49) will remain unchanged in order to ensure a reliable and consistent build experience.
eas.json
Copy
```

"build":{
"production":{
"ios":{
"image":"latest"

```

## [New recommended React Native version for SDK 49 ](https://expo.dev/changelog/2023-09-28-new-xcode-ios#new-recommended-react-native-version-for-sdk-49)
[React Native 0.72.5](https://github.com/facebook/react-native/releases/tag/v0.72.5) is now recommended for SDK 49 (the previously recommended version was 0.72.4). This patch release includes support for Xcode 15. If you are using SDK 49, we recommend upgrading to this version if you build locally and have Xcode 15 installed, or if you would like to use Xcode 15 on EAS Build. You can install it with `npx expo install --fix`.
**Note:** We will be updating the recommended React Native patch version for SDK 47 and 48 when new versions are released with support for Xcode 15.
## [Added "Tap to Pay on iPhone" entitlement support ](https://expo.dev/changelog/2023-09-28-new-xcode-ios#added-tap-to-pay-on-iphone-entitlement-support)
EAS Build will [automatically sync the newly added "Tap to Pay on iPhone" (`com.apple.developer.proximity-reader.payment.acceptance`) capability](https://docs.expo.dev/build-reference/ios-capabilities/) when the entitlement is set in your app config under [`ios.entitlements`](https://docs.expo.dev/versions/latest/config/app/#entitlements). Note that you must [request access to this entitlement from Apple](https://developer.apple.com/contact/request/tap-to-pay-on-iphone/) in order to use it.
## [Updated expo-calendar on SDK 49 for iOS 17 changes ](https://expo.dev/changelog/2023-09-28-new-xcode-ios#updated-expo-calendar-on-sdk-49-for-ios-17-changes)
Install the latest version with `npx expo install expo-calendar` and re-build your app with Xcode 15. The improvements are availabile in `expo-calendar@~1.3.2`. We recommend updating if you use `expo-calendar` in your app. The following is a technical outline of the changes to the calendar API that were made in order to support iOS 17.
  * iOS 17 introduces a new permissions model in `EventKit`. Previously, you could request access and you would be either granted full access or none at all. In iOS 17 this has been changed. You can now request (1) `write-only` access, (2) `full-access`, or (3) present the new `EventKitEditViewController`, which requires no user permissions.
  * **This change means all apps linked against iOS 17 must adopt this new model now — all uses of the older APIs on iOS 17 will fail**. We have implemented the necessary changes in `expo-calendar` in [expo/expo#24545](https://github.com/expo/expo/pull/24545)
  * The method `requestAccess(to:)` has been replaced with two new APIs that must be used in iOS 17: `requestFullAccessToReminders` and `requestFullAccessToEvents`. Calling the `requestAccess(to:)` API on iOS 17 is now a no-op. We have added support for both of the new APIs in `expo-calendar`.
  * This change also required two new keys to be added to the **Info.plist**. `NSRemindersFullAccessUsageDescription` and `NSCalendarsFullAccessUsageDescription`. [Changes were made to the config plugin](https://github.com/expo/expo/pull/24545/files#diff-a930b52365b3519d47ac5f2ffd91b31d48b0bd8e9b60dfc8aba8d29b20cf1834) to support this and provide defaults for both of these properties.
  * The current solution will build on both Xcode 14 and 15, but for the devices running iOS 17, the app will need to have been built with Xcode 15.
  * The fix we have in place maintains the previous behavior. We will be evaluating the new changes and adding support for presenting `EventKitEditViewController` and requesting `write-only` access, likely coming in SDK 50.



