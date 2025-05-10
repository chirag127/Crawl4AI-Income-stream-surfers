---
url: https://docs.expo.dev/guides/facebook-authentication
title: https://docs.expo.dev/guides/facebook-authentication
date: 2025-04-30T17:14:04.160880
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Using Facebook authentication
A guide on using react-native-fbsdk-next library to integrate Facebook authentication in your Expo project.
The [`react-native-fbsdk-next`](https://github.com/thebergamo/react-native-fbsdk-next/) library provides a wrapper around Facebook's Android and iOS SDKs. It allows integrating Facebook authentication into your Expo project and provide access to native components.
This guide provides additional information on configuring the library with Expo for Android.
## Prerequisites
The `react-native-fbsdk-next` library can't be used in the Expo Go app because it requires custom native code. Learn more about [adding custom native code to your app](https://docs.expo.dev/workflow/customizing).
## Installation
See `react-native-fbsdk-next` documentation for instructions on how to install and configure the library:
[React Native FBSDK Next: Expo installation instructions](https://github.com/thebergamo/react-native-fbsdk-next/#expo-installation)
## Configuration for Android
Adding Android as a platform in your Facebook project requires you to have your app approved by Google Play Store so that it has a valid Play Store URL, and the [`package`](https://docs.expo.dev/versions/latest/config/app#package) name associated with your app. Otherwise, you'll run into the following error:
See the following guides for more information on how to build your project for app stores:
[Build your project for app stores](https://docs.expo.dev/deploy/build-project) [Manually upload Android app for the first time](https://expo.fyi/first-android-submission)
Once you have uploaded the app to the Play Store you can submit your app review. When it is approved the Facebook project will be able to access it at a Play Store URL.
After that, go to your Facebook project's Settings > Basic and add the Android platform. You'll need to provide the Key hash, Package name and Class name.
  * To add Key hash, go to your Play Store Console to obtain the SHA-1 certificate fingerprint from Release > Setup > App Integrity > App signing key certificate. Then, [convert the value of the Hex value of the certificate to Base64](https://base64.guru/converter/encode/hex) and add it under the Android > Key hashes in your Facebook project.
  * You can find the Package name in your [app config](https://docs.expo.dev/versions/latest/config/app) under the [`android.package`](https://docs.expo.dev/versions/latest/config/app#package) field.
  * The Class name is `MainActivity` by default, and you can use `package.MainActivity` where `package` is the `android.package` in your project's app config. For example, `com.myapp.example.MainActivity`, where `com.myapp.example` is the `package` name of your app.
  * Then, click Save changes to save the configuration.


Now, you can use your Facebook project for development or release builds and production apps.

