---
url: https://docs.expo.dev/archive/glossary
title: https://docs.expo.dev/archive/glossary
date: 2025-04-30T17:12:45.543729
depth: 2
---

[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Glossary of terms
> The following page consists of definitions for some of the deprecated terms, technologies and tools.
### detach
The term "detach" was previously used in Expo to mean [ejecting](https://docs.expo.dev/archive/glossary#eject) your app to use [ExpoKit](https://docs.expo.dev/archive/glossary#expokit).
### eject
The term "eject" was popularized by [create-react-app](https://github.com/facebook/create-react-app), and it is used in Expo to describe leaving the cozy comfort of the standard Expo development environment, where you do not have to deal with build configuration or native code. When you "eject" from Expo, you have two choices:
  * _Eject to bare workflow_ , where you jump between [workflows](https://docs.expo.dev/archive/managed-vs-bare) and move into the bare workflow, where you can continue to use Expo APIs but have access and full control over your native Android and iOS projects.
  * _Eject to ExpoKit_ , where you get the native projects along with [ExpoKit](https://docs.expo.dev/archive/glossary#expokit). This option is deprecated and support for ExpoKit was removed after SDK 38.


### ExpoKit
ExpoKit is an Objective-C and Java library that allows you to use the [Expo SDK](https://docs.expo.dev/more/glossary-of-terms#expo-sdk) and platform and your existing Expo project as part of a larger standard native project — one that you would normally create using Xcode, Android Studio, or `react-native init`. For more information, see [Ejecting to ExpoKit](https://docs.expo.dev/archive/expokit/eject).
Support for ExpoKit ended after SDK 38. Expo modules can implement support for custom native configuration, and projects that need even more custom native code can [expose their Android Studio and Xcode projects with `npx expo prebuild`](https://docs.expo.dev/workflow/customizing).
### Shell app
Another term we occasionally use for [Standalone app](https://docs.expo.dev/more/glossary-of-terms#standalone-app).
### XDE
XDE was a desktop tool with a graphical user interface (GUI) for working with Expo projects. It's been replaced by [Expo CLI](https://docs.expo.dev/more/expo-cli), which now provides both command line and web interfaces.

