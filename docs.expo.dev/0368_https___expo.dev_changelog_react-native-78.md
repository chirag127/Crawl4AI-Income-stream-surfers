---
url: https://expo.dev/changelog/react-native-78
title: https://expo.dev/changelog/react-native-78
date: 2025-04-30T17:19:25.225176
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [Expo support for React Native 0.78](https://expo.dev/changelog/react-native-78)
Feb 19, 2025 by
Brent Vatne
React Native 0.78 is supported in a canary release of the Expo SDK, instructions available in this post. Expo SDK 53 will be released in the spring and will likely support React Native 0.79.
> 💡 **Note** : as of March 20, 2025, `canary` uses React Native 0.79. Depending on when you are reading this post, `canary` may even point to another version - it will always use the latest version that is on the [expo/expo main branch](https://github.com/expo/expo). The last canary version to use React Native 0.78 is: `53.0.0-canary-20250306-d9d3e02`. Use this in place of the `canary` tag when creating a project or installing the `expo` package to install that specific version; however, we recommend using the latest.
Expo SDK 52 currently supports React Native [0.76 (default)](https://expo.dev/changelog/2025/01-21-react-native-0.77), released October 23, 2024, and [0.77 (opt-in)](https://expo.dev/changelog/2025/01-21-react-native-0.77), released January 21, 2025.
React Native 0.78 support is available in a canary release of the Expo SDK, to allow early adopters to use it right away. _This is not intended to be a stable release_ , but if you are particularly adventurous and have a good motivation to use it today, you certainly can (provided that other non-Expo libraries you depend on are also compatible).
## [**Support is available on the Expo canary channel** ](https://expo.dev/changelog/react-native-78#support-is-available-on-the-expo-canary-channel)
> Canary releases represent a snapshot of the state of the `main` branch at the time they are published. Canary package versions include `-canary` in the name, along with the date and commit hash, such as `51.0.0-canary-20240418-8d74597`. ([Source](https://docs.expo.dev/versions/latest/#using-pre-release-versions))
  * **Create a new project with the canary release** : `npx create-expo-app my-app --template blank@canary`
  * **Install a canary release in an existing project** : `npx expo install expo@canary --fix`
  * **If you use npm, add an override for React 19 to your project:** [example](https://github.com/expo/expo/pull/35331).


_When using a canary release, you should be aware that:_
  * It is not stable and may contain bugs
  * It may have breaking changes
  * It should only be used for testing and evaluation
  * It may not have all features fully implemented
  * It could have compatibility issues with some third-party libraries
  * It will not support Expo Go

## [**Why not add support for 0.78 to the existing Expo SDK 52?** ](https://expo.dev/changelog/react-native-78#why-not-add-support-for-078-to-the-existing-expo-sdk-52)
React Native 0.78 includes a number of changes that would make supporting it in Expo SDK 52 unfeasible. The most significant of these is the React version: React Native 0.78 bumps React to 19, while 0.76 and 0.77 use 18.
## [**Why will there be no dedicated stable Expo SDK release for 0.78?** ](https://expo.dev/changelog/react-native-78#why-will-there-be-no-dedicated-stable-expo-sdk-release-for-078)
> New Expo SDK versions are released three times each year. Between these releases, we publish pre-release versions of the `expo` package and all of the Expo SDK packages. Pre-releases are not considered stable and should only be used if you are comfortable with the risk of encountering bugs or other issues. ([Source](https://docs.expo.dev/versions/latest/#using-pre-release-versions))
At Expo, we have found that releasing three major version provides a good balance of stability and innovation for developers depending on our open source tools. Following this schedule, the timing that works out better for releasing SDK 53 coincides with the time when React Native 0.79 is likely to be released.
Expo and Meta work closely together on releases, and we will keep improving our processes to get the latest Expo and React Native features to you as quickly as possible. With the current release cadences, ideally there will be a dedicated Expo SDK release for each second React Native release, with the in between version being supported by the previous Expo SDK release.
## [**Spring 2025: Expo SDK 53** ](https://expo.dev/changelog/react-native-78#spring-2025-expo-sdk-53)
Expo SDK 53 is intended for release this spring, in advance of [App.js Conf](https://appjs.co/) (get your ticket now if you haven't already!). It is intended to support React Native 0.79. Keep an eye out for a beta release in late March or April.

