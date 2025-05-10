---
url: https://docs.expo.dev/distribution/introduction
title: https://docs.expo.dev/distribution/introduction
date: 2025-04-30T17:13:13.155600
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Distribution: Overview
An overview of submitting an app to the app stores or with the internal distribution.
Get your app into the hands of users by submitting it to the app stores or with [Internal Distribution](https://docs.expo.dev/build/internal-distribution).
Terminal
Copy
`# Install the CLI`
`- ``npm i -g eas-cli`
`# Build and submit your app`
`- ``eas build --auto-submit`
`# OR -- Submit existing binaries`
`- ``eas submit`
You can run `eas build --auto-submit` with [EAS CLI](https://docs.expo.dev/eas) to build your app and automatically upload the binary for distribution on the Google Play Store and Apple App Store.
This automatically manages all native code signing for Android and iOS for any React Native app. Advanced features such as payments, notifications, universal links, and iCloud can be automatically enabled based on your [config plugins](https://docs.expo.dev/config-plugins/introduction) or native entitlements, meaning no more wrestling with slow portals to get libraries set up correctly.
### Get started
[Submit to the Google Play StoreLearn how to submit an Android app to the Google Play Store.](https://docs.expo.dev/submit/android) [Submit to the Apple App StoreLearn how to submit an iOS or an iPadOS app to the Apple App Store from any operating system.](https://docs.expo.dev/submit/ios) [Internal DistributionShare your mobile app internally with testers using AdHoc builds.](https://docs.expo.dev/build/internal-distribution) [Publish websitesExport your website and upload to any web host.](https://docs.expo.dev/guides/publishing-websites) [OTA updatesSend over-the-air updates to your users instantly.](https://docs.expo.dev/eas-update/introduction)

