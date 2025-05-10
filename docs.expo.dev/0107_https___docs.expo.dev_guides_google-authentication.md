---
url: https://docs.expo.dev/guides/google-authentication
title: https://docs.expo.dev/guides/google-authentication
date: 2025-04-30T17:14:01.068925
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Using Google authentication
A guide on using @react-native-google-signin/google-signin library to integrate Google authentication in your Expo project.
The [`@react-native-google-signin/google-signin`](https://github.com/react-native-google-signin/google-signin) library provides a way integrate Google authentication in your Expo app. It also provides native sign-in buttons and supports authenticating the user as well as obtaining their authorization to use Google APIs. You can use the library in your project by adding the [config plugin](https://docs.expo.dev/config-plugins/introduction) in the [app config](https://docs.expo.dev/versions/latest/config/app).
This guide provides information on how to configure the library for your project.
## Prerequisites
The `@react-native-google-signin/google-signin` library can't be used in the Expo Go app because it requires custom native code. Learn more about [adding custom native code to your app](https://docs.expo.dev/workflow/customizing).
## Installation
See `@react-native-google-signin/google-signin` documentation for instructions on how to install and configure the library:
[React Native Google Sign In: Expo installation instructions](https://react-native-google-signin.github.io/docs/setting-up/expo)
## Configure Google project for Android and iOS
Below are instructions on how to configure your Google project for Android and iOS.
### Upload app to Google Play Store
We recommend uploading the app to the Google Play Store if your app intends to run in production. You can submit your app to the stores for testing even if your project is still in development. This allows you to test Google Sign In when your app is signed by EAS for testing, and when it is signed by [Google Play App Signing](https://support.google.com/googleplay/android-developer/answer/9842756?hl=en) for store deployment. To learn more about the app submission process, see the guides below in the order they are specified:
[Create your first EAS Build](https://docs.expo.dev/build/setup) [Build your project for app stores](https://docs.expo.dev/deploy/build-project) [Manually upload Android app for the first time](https://expo.fyi/first-android-submission)
### Configure your Firebase or Google Cloud Console project
> Refer to the [library's documentation](https://react-native-google-signin.github.io/docs/setting-up/get-config-file) for a more in-depth configuration guide.
For Android, once you have uploaded your app, you need to provide the SHA-1 certificate fingerprint values when asked while configuring the project in Firebase or Google Cloud Console. There are two types of values that you can provide:
  * Fingerprint of the .apk you built (on your machine or using EAS Build). You can find the SHA-1 certificate fingerprint in the Google Play Console under Release > Setup > App Integrity > Upload key certificate.
  * Fingerprint(s) of a production app downloaded from the play store. You can find the SHA-1 certificate fingerprint(s) in the Google Play Console under Release > Setup > App Integrity > App signing key certificate.


### With Firebase
For more instructions on how to configure your project for Android and iOS with Firebase:
[Firebase](https://react-native-google-signin.github.io/docs/setting-up/expo#expo-and-firebase-authentication)
#### Upload google-services.json and GoogleService-Info.plist to EAS
If you use the Firebase method for Android and iOS (as shared in sections above), you'll need to make sure google-services.json and GoogleService-Info.plist are available in EAS for building the app. You can check them into your repository because the files should not contain sensitive values, or you can treat the files as secrets, add them to .gitignore and use the guide below to make them available in EAS.
[Upload a secret file to EAS and use in the app config](https://docs.expo.dev/eas/environment-variables?redirected#use-environment-variables-with-eas-build)
### With Google Cloud Console
This is an alternate method to configure a Google project when you are not using [Firebase](https://docs.expo.dev/guides/google-authentication#with-firebase).
For more instructions on how to configure your Google project Android and iOS with Google Cloud Console:
[Expo without Firebase](https://react-native-google-signin.github.io/docs/setting-up/expo#expo-without-firebase)

