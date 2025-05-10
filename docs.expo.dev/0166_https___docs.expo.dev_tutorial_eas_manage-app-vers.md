---
url: https://docs.expo.dev/tutorial/eas/manage-app-versions
title: https://docs.expo.dev/tutorial/eas/manage-app-versions
date: 2025-04-30T17:14:54.112355
depth: 2
---

Search
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Manage different app versions
Learn about developer-facing and user-facing app versions and how EAS Build automatically manages developer-facing versions.
In this chapter, we'll learn how EAS Build automatically manages the developer-facing app version for Android and iOS. Learning about it will be useful before we dive into production build in the next two chapters.
[Watch: Automating app version code](https://www.youtube.com/watch?v=C8x4N9UmzS8)
## Understanding developer-facing and user-facing app versions
An app version is composed of two values:
  * Developer-facing value: Represented by [`versionCode`](https://docs.expo.dev/versions/latest/config/app#versioncode) for Android and [`buildNumber`](https://docs.expo.dev/versions/latest/config/app#buildnumber) for iOS.
  * User-facing value: Represented by [`version`](https://docs.expo.dev/versions/latest/config/app#version) app.config.js.


Both Google Play Store and Apple App Store rely on developer-facing values to identify each unique build. For example, if we upload an app with the app version `1.0.0 (1)` (which is a combination of user-facing and developer-facing values), we cannot submit another build to the app stores with the same app version. Submitting builds with duplicate app version numbers results in a failed submission.
An example demonstration of manually managing developer-facing values is shown below by `android.versionCode` and `ios.buildNumber` in app.config.js. We don't have to add or manage these values manually since EAS Build automates this for us.
app.config.js
Copy
```
{
 ios: {
  buildNumber: 1
  %%placeholder-start%%... %%placeholder-end%%
 },
 android: {
  versionCode: 1
 }
 %%placeholder-start%%... %%placeholder-end%%
}

```

> Note: The [user-facing version number](https://docs.expo.dev/build-reference/app-versions#user-facing-version) is not handled by EAS. Instead, we define that in the app store developer portals before submitting our production app for review.
## Automatic app version management with EAS Build
By default, EAS Build assists in automating developer-facing values. It utilizes the [remote version source](https://docs.expo.dev/build-reference/app-versions#remote-version-source) to automatically increment developer-facing values whenever a new production release is made.
When we initialized the project with `eas init` command, the EAS CLI automatically added the following properties in eas.json:
  * `cli.appVersionSource` which is set to `remote`
  * [`build.production.autoIncrement`](https://docs.expo.dev/eas/json#autoincrement-1) which is set to `true`


You can view them in your project's eas.json:
eas.json
Copy
```
{
 "cli": {
  %%placeholder-start%%... %%placeholder-end%%
  "appVersionSource": "remote"
 },
 "build": {
  "production": {
   "autoIncrement": true
  }
 }
 %%placeholder-start%%... %%placeholder-end%%
}

```

When we create a new production build in the next two chapters, the `versionCode` for Android and `buildNumber` for iOS will increment automatically.
Syncing developer-facing app versions for already published apps to EAS
If your app is already published in the app stores, the developer-facing app versions are already set. When migrating this app to use EAS Build, follow the steps below to sync those app versions:
  * In the terminal window, run the `eas build:version:set` command:


Terminal
Copy
`- ``eas build:version:set`
  * Select the platform (Android or iOS) when prompted.
  * When prompted Do you want to set app version source to remote now?, select yes. This will set the `cli.appVersionSource` to `remote` in eas.json.
  * When prompted What version would you like to initialize it with?, enter the last version number that you have set in the app stores.


After these steps, the app versions will be synced to EAS Build remotely. You can set `build.production.autoIncrement` to `true` in eas.json. When you create a new production build, the `versionCode` and `buildNumber` will be automatically incremented from now on.
## Summary
Chapter 7: Manage different app versions
We successfully explored app versioning differences, addressed the importance of unique app versions to prevent store rejections, and enabled automated version updates in eas.json for production builds.
Mark this chapter as read
In the next chapter, learn about the process of creating a production build for Android.
[Next: Create a production build for Android](https://docs.expo.dev/tutorial/eas/android-production-build)

