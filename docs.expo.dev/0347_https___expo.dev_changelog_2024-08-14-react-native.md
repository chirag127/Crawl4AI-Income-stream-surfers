---
url: https://expo.dev/changelog/2024-08-14-react-native-0.75
title: https://expo.dev/changelog/2024-08-14-react-native-0.75
date: 2025-04-30T17:19:00.767515
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [React Native 0.75 is now available with Expo SDK 51](https://expo.dev/changelog/2024-08-14-react-native-0.75)
Aug 14, 2024 by
Gabriel Donadel
Today, [React Native 0.75 was released](https://reactnative.dev/blog/2024/08/12/release-0.75), and Expo SDK 51 now supports both React Native 0.74 and 0.75. Typically, an Expo SDK version is tied to a specific React Native version. For example, Expo SDK 50 is only tested against and expected to be compatible with React Native 0.73, and tools such as Expo CLI and Doctor will validate that you are using the expected version. We've decided that this isn't necessary for React Native 0.75. As a result, this should be an even quicker upgrade than usual, should you choose to upgrade.
## [Why no full SDK release for React Native 0.75? ](https://expo.dev/changelog/2024-08-14-react-native-0.75#why-no-full-sdk-release-for-react-native-075)
The 0.75 release includes a number of bug fixes and improvements, but React Native engineers at Meta consider it to be a relatively small release compared to the upcoming 0.76 release in the fall.
In order to continue with [rolling out the New Architecture](https://docs.expo.dev/guides/new-architecture/), there will be a shorter-than-usual period between 0.75 and 0.76. So, to minimize the thrash of SDK releases, we opted for adding support for both 0.74 and 0.75 to the same SDK release.
## [How to use React Native 0.75 with Expo SDK 51 ](https://expo.dev/changelog/2024-08-14-react-native-0.75#how-to-use-react-native-075-with-expo-sdk-51)
The default React Native version for Expo SDK 51 will continue to be 0.74. You can opt in to using the 0.75 with the following steps.
### [1. Exclude packages from version validations ](https://expo.dev/changelog/2024-08-14-react-native-0.75#1-exclude-packages-from-version-validations)
All Expo packages will work with both 0.74 and 0.75 versions. However, some other popular libraries that we include in the Expo SDK and validate against do not have releases that are compatible with both versions simultaneously. For example, `react-native-reanimated@~3.10.0` does not support React Native 0.75, you will need to use `react-native-reanimated@~3.15.0`.
To avoid warnings about incompatible versions, you can exclude packages from version validations. This is done by adding the `expo.install.exclude` property to your **package.json** file. For example:
Code
Copy
```

"expo":{
"install":{
"exclude":[
"react-native@~0.74.0",
"react-native-reanimated@~3.10.0",
"react-native-gesture-handler@~2.16.1",
"react-native-screens@~3.31.1"

```

This will ensure that Expo tools will not warn you about incompatible versions of react-native and react-native-reanimated, as long as the Expo SDK that you are using is recommending the specified versions. So, when you update to SDK 52, these exclusions will no longer apply because the recommended versions will have changed.
### [2. Install updated packages ](https://expo.dev/changelog/2024-08-14-react-native-0.75#2-install-updated-packages)
Terminal
Copy
`npx expo install react-native@~0.75.0 react-native-reanimated@~3.15.0 react-native-gesture-handler@~2.18.1 react-native-screens@~3.34.0`
### [3. Update your Android native project ](https://expo.dev/changelog/2024-08-14-react-native-0.75#3-update-your-android-native-project)
  * If you use [CNG](https://docs.expo.dev/workflow/continuous-native-generation/) and have run prebuild locally, you will need to run `npx expo prebuild --clean -p android` again to re-generate the native projects to pull in changes that make the app compatible with both React Native 0.74 and 0.75.
  * If you do not use CNG, you will need to update your **settings.gradle** , **app/build.gradle** , and **gradle/wrapper/gradle-wrapper.properties**. Refer to the [Native Project Upgrade Helper](https://docs.expo.dev/bare/upgrade/?fromSdk=50&amp;toSdk=51) for details on those specific files. Note that this tool will show you the diff between SDK 50 and 51, but in this case you may just be migrating from SDK 51 (without React Native 0.75 support) to SDK 51 (with React Native 0.74 and 0.75 support), so the diff is less instructive than the actual content of the files. Also note that you should keep Jetifier enabled — disabling it may cause issues with `expo-camera` due to the legacy camera implementation that will be dropped in SDK 52.

### [4. Optional: Try out autolinking speed improvements ](https://expo.dev/changelog/2024-08-14-react-native-0.75#4-optional-try-out-autolinking-speed-improvements)
With Expo SDK 51 and React Native 0.75, **the autolinking step for React Native libraries (which are not Expo modules) is now faster — up to ~6.5x faster on Android and ~1.5x faster on iOS.**
When installing CocoaPods for your iOS project or running an Android build, you typically wouldn't notice the impact of autolinking configuration resolution speed because those tasks are relatively long running. However, for tasks that execute in seconds, such as generating a project fingerprint with `@expo/fingerprint`, autolinking can represent a significant portion of the execution time and any improvements will be noticeable. If we can run `@expo/fingerprint` often without interrupting the development process, we can start to leverage fingerprints for different purposes in the future.
In an upcoming version of React Native, the React Native Community CLI and autolinking packages will be removed from React Native and our new implementation of autolinking will become the default. Try it out today and let us know if you notice any improvements or run into any issues. Set `EXPO_UNSTABLE_CORE_AUTOLINKING=1` to try it with the latest version of Expo SDK 51 and React Native 0.75. [Learn more](https://github.com/react-native-community/discussions-and-proposals/discussions/814)
## [What's next? ](https://expo.dev/changelog/2024-08-14-react-native-0.75#whats-next)
We'll continue working on SDK 52 and React Native 0.76, and we hope to have them ready early in the fall. If you run into any issues with React Native 0.75 and Expo SDK 51, [please file an issue](https://github.com/expo/expo/issues).

