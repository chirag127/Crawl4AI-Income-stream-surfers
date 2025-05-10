---
url: https://expo.dev/changelog/2025-01-21-react-native-0.77
title: https://expo.dev/changelog/2025-01-21-react-native-0.77
date: 2025-04-30T17:19:25.275727
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [React Native 0.77 is now available with Expo SDK 52](https://expo.dev/changelog/2025-01-21-react-native-0.77)
Jan 21, 2025 by
Vojtech Novak
Today, [React Native 0.77 was released](https://reactnative.dev/blog/2025/01/21/version-0.77), and Expo SDK 52 now supports both React Native 0.76 and 0.77. Typically, an Expo SDK version is tied to a specific React Native version. For example, Expo SDK 50 was only tested against and expected to be compatible with React Native 0.73, and tools such as Expo CLI and Doctor will validate that you are using the expected version. We've decided that this isn't necessary for React Native 0.77. As a result, this should be an even quicker upgrade than usual – if you choose to upgrade.
React Native 0.77 was released, and Expo SDK 52 now supports both React Native 0.76 and 0.77.
## [Why no full SDK release for React Native 0.77? ](https://expo.dev/changelog/2025-01-21-react-native-0.77#why-no-full-sdk-release-for-react-native-077)
The 0.77 release includes a number of bug fixes and improvements, but React Native engineers at Meta consider it to be a relatively small release.
To minimize the disruption of SDK releases, we opted for adding support for both 0.76 and 0.77 to the same SDK release. Previously, we have taken this approach with React Native 0.74 and 0.75 with SDK 51.
## [How to use React Native 0.77 with Expo SDK 52 ](https://expo.dev/changelog/2025-01-21-react-native-0.77#how-to-use-react-native-077-with-expo-sdk-52)
Expo Go stays on React Native 0.76, and it does not support React Native 0.77. Create a [development build](https://docs.expo.dev/develop/development-builds/create-a-build/) if you want to use React Native 0.77.
The default React Native version for Expo SDK 52 will continue to be 0.76. You can opt in to use version 0.77 by following these steps:
### [1. Exclude packages from version validations ](https://expo.dev/changelog/2025-01-21-react-native-0.77#1-exclude-packages-from-version-validations)
All Expo packages will work with both 0.76 and 0.77 versions. However, some other popular libraries that we include in the Expo SDK and validate against do not have releases that are compatible with both versions simultaneously. For example, `react-native-reanimated@3.16.1 `does not support React Native 0.77, you will need to use `react-native-reanimated@~3.16.7`.
To avoid warnings about incompatible versions, you can exclude packages from version validations. This is done by adding the `expo.install.exclude` property to your **package.json** file. For example:
package.json
Copy
```

"expo":{
"install":{
"exclude":[
"react-native@~0.76.6",
"react-native-reanimated@~3.16.1",
"react-native-gesture-handler@~2.20.0",
"react-native-screens@~4.4.0",
"react-native-safe-area-context@~4.12.0",
"react-native-webview@~13.12.5"

```

This will ensure that Expo tools will not warn you about incompatible versions of `react-native` and `react-native-reanimated`, as long as the Expo SDK that you are using is recommending the specified versions. So, when you update to SDK 52, these exclusions will no longer apply because the recommended versions will have changed.
### [2. Install updated packages ](https://expo.dev/changelog/2025-01-21-react-native-0.77#2-install-updated-packages)
Firstly, update `expo` to at least version `52.0.27`. Then, install dependencies compatible with React Native 0.77:
Terminal
Copy
`npx expo install react-native@~0.77.1 react-native-reanimated@~3.16.7 react-native-gesture-handler@~2.22.0 react-native-screens@~4.8.0 react-native-safe-area-context@~5.1.0 react-native-webview@~13.13.1`
### [3. Update your native projects ](https://expo.dev/changelog/2025-01-21-react-native-0.77#3-update-your-native-projects)
  * If you use [CNG](https://docs.expo.dev/workflow/continuous-native-generation/) and have run prebuild locally, you will need to run `npx expo prebuild --clean` again to re-generate the native projects to pull in changes that make the app compatible with React Native 0.77.
  * If you do not use CNG, you will need to bump Kotlin and NDK versions in your Android project, for more details refer to the [Native Project Upgrade Helper](https://docs.expo.dev/bare/upgrade/?fromSdk=52&toSdk=unversioned).

## [What's next? ](https://expo.dev/changelog/2025-01-21-react-native-0.77#whats-next)
We'll continue working on improving Expo and bringing in support for React Native 0.78 later this year. If you run into any issues with React Native 0.77 and Expo SDK 52, [please file an issue](https://github.com/expo/expo/issues).

