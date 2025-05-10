---
url: https://docs.expo.dev/workflow/upgrading-expo-sdk-walkthrough
title: https://docs.expo.dev/workflow/upgrading-expo-sdk-walkthrough
date: 2025-04-30T17:18:15.261190
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Upgrade Expo SDK
Learn how to incrementally upgrade the Expo SDK version in your project.
> We recommend upgrading SDK versions incrementally, one at a time. Doing so will help you pinpoint breakages and issues that arise during the upgrade process.
With a new SDK release, the latest version enters the current release status. This applies to Expo Go as it only supports the latest SDK version and previous versions are no longer supported. We recommend using [development builds](https://docs.expo.dev/develop/development-builds/introduction) for production apps as the backwards compatibility for older SDK versions on EAS services tends to be much longer, but not forever.
If you are looking to install a specific version of Expo Go, visit [expo.dev/go](https://expo.dev/go). It supports downloads for Android devices/emulators and iOS simulators. However, due to iOS platform restrictions, only the latest version of Expo Go is available for installation on physical iOS devices.
## How to upgrade to the latest SDK version
1
### Upgrade the Expo SDK
Install the new version of the Expo package:
npm
Yarn
Terminal
`# Install latest`
`- ``npx expo install expo@latest`
`# Install a specific SDK version (for example, SDK 52)`
`- ``npx expo install expo@^52.0.0`
Terminal
`# Install latest`
`- ``yarn expo install expo@latest`
`# Install a specific SDK version (for example, SDK 52)`
`- ``yarn expo install expo@^52.0.0`
2
### Upgrade dependencies
Upgrade all dependencies to match the installed SDK version.
Terminal
Copy
`- ``npx expo install --fix`
3
### Update native projects
  * If you use [Continuous Native Generation](https://docs.expo.dev/workflow/continuous-native-generation): Delete the android and ios directories if you generated them for a previous SDK version in your local project directory. They'll be re-generated next time you run a build, either with `npx expo run:ios`, `npx expo prebuild`, or with EAS Build.
  * If you don't use [Continuous Native Generation](https://docs.expo.dev/workflow/continuous-native-generation): Run `npx pod-install` if you have an `ios` directory. Apply any relevant changes from the [Native project upgrade helper](https://docs.expo.dev/bare/upgrade). Alternatively, you could consider [adopting prebuild](https://docs.expo.dev/guides/adopting-prebuild) for easier upgrades in the future.


4
### Follow the release notes for any other instructions
Read the [SDK changelogs](https://docs.expo.dev/workflow/upgrading-expo-sdk-walkthrough#sdk-changelogs) for the SDK version you are upgrading to. They contain important information about breaking changes, deprecations, and other changes that may affect your app. Refer to tue "Upgrading your app" section at the bottom of the release notes page for any additional instructions.
## SDK Changelogs
Each SDK announcement release notes post contains information deprecations, breaking changes, and anything else that might be unique to that particular SDK version. When upgrading, be sure to check these out to make sure you don't miss anything.
  * SDK 52: [Release notes](https://expo.dev/changelog/2024/11-12-sdk-52)
    * React Native 0.77 is available with Expo SDK 52. To upgrade, see these [Release notes](https://expo.dev/changelog/2025/01-21-react-native-0.77).
  * SDK 51: [Release notes](https://expo.dev/changelog/2024/05-07-sdk-51)
  * SDK 50: [Release notes](https://expo.dev/changelog/2024/01-18-sdk-50)


### Deprecated SDK Version Changelogs
The following blog posts may included outdated information, but they are still useful for reference if you happen to fall far behind on SDK upgrades.
See a full list of deprecated SDK release changelogs
  * SDK 49: [Release notes](https://blog.expo.dev/expo-sdk-49-c6d398cdf740)
  * SDK 48: [Release notes](https://blog.expo.dev/expo-sdk-48-ccb8302e231)
  * SDK 47: [Release notes](https://blog.expo.dev/expo-sdk-47-a0f6f5c038af)
  * SDK 46: [Release notes](https://blog.expo.dev/expo-sdk-46-c2a1655f63f7)
  * SDK 45: [Release notes](https://blog.expo.dev/expo-sdk-45-f4e332954a68)
  * SDK 44: [Release notes](https://blog.expo.dev/expo-sdk-44-4c4b8306584a)
  * SDK 43: [Release notes](https://blog.expo.dev/expo-sdk-43-aa9b3c7d5541)
  * SDK 42: [Release notes](https://blog.expo.dev/expo-sdk-42-579aee2348b6)
  * SDK 41: [Release notes](https://blog.expo.dev/expo-sdk-41-12cc5232f2ef)
  * SDK 40: [Release notes](https://dev.to/expo/expo-sdk-40-is-now-available-1in0)
  * SDK 39: [Release notes](https://dev.to/expo/expo-sdk-39-is-now-available-1lm8)
  * SDK 38: [Release notes](https://dev.to/expo/expo-sdk-38-is-now-available-5aa0)
  * SDK 37: [Release notes](https://dev.to/expo/expo-sdk-37-is-now-available-69g)
  * SDK 36: [Release notes](https://blog.expo.dev/expo-sdk-36-is-now-available-b91897b437fe)
  * SDK 35: [Release notes](https://blog.expo.dev/expo-sdk-35-is-now-available-beee0dfafbf4)



