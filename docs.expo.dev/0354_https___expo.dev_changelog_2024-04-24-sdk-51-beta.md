---
url: https://expo.dev/changelog/2024-04-24-sdk-51-beta
title: https://expo.dev/changelog/2024-04-24-sdk-51-beta
date: 2025-04-30T17:19:00.796390
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [Expo SDK 51 beta is now available](https://expo.dev/changelog/2024-04-24-sdk-51-beta)
Apr 24, 2024 by
Brent Vatne
**The SDK 51 beta period begins today and will last approximately one week.** The beta is an opportunity for developers to test out the SDK and ensure that the new release does not introduce any regressions for their particular systems and app configurations. We’re also hosting [office hours](https://us02web.zoom.us/meeting/register/tZcvceivqj0oHdGVOjEeKY0dRxCRPb0HzaAK) for those of you interested in helping test the release!
SDK 51 beta includes React Native 0.74. The full release notes for SDK 51 won't be available until the stable release, but you can browse the changes in the [expo/expo CHANGELOG](https://github.com/expo/expo/blob/main/CHANGELOG.md) to learn more about the scope of the release and any breaking changes.
### [New default project template ](https://expo.dev/changelog/2024-04-24-sdk-51-beta#new-default-project-template)
When you create a new project with `npx create-expo-app --template default@beta`, you will see our ✨renovated new project template✨! It includes common dependencies and configuration that most projects need, so you can hit the ground running.
That's a lot of code to delete if you don't need it! That's why you can run `npm run reset-project` to remove all of the boilerplate code and start fresh.
### [Highlights ](https://expo.dev/changelog/2024-04-24-sdk-51-beta#highlights)
  * **"Next" Camera and SQLite APIs are now the default.** `expo-camera/next` is now exported from `expo-camera` ([learn more](https://docs.expo.dev/versions/v51.0.0/sdk/camera/)), and `expo-sqlite/next` is now exported from `expo-sqlite` ([learn more](https://docs.expo.dev/versions/v51.0.0/sdk/sqlite/)). You can find the old versions at `expo-camera/legacy` and `expo-sqlite/legacy` during SDK 51, and they will be removed in SDK 52. **Thank you** to everybody who used these APIs during SDK 50 and gave us feedback!
  * **Beta release of new expo-video library**. Following the success of the "next" Camera and SQLite APIs, we are releasing a new video library that incorporates our learnings from maintaining `expo-av` over the years. This library is a complete rewrite of the Video functionality from `expo-av`, and it's designed to be more reliable and easier to use. We expect to update this library frequently during the SDK 51 cycle, and so it will not yet be available in Expo Go (yet another reason to use [Development Builds](https://docs.expo.dev/develop/development-builds/introduction/)). [Learn more](https://docs.expo.dev/versions/v51.0.0/sdk/video/).
  * **iOS Privacy manifest config field** : beginning on May 1, Apple will require that apps using any "restricted reason" APIs include a privacy manifest. To make this easy for you to comply with, we have added support for the privacy manifest to the Expo config. [Learn more](https://docs.expo.dev/guides/apple-privacy/).


Code
Copy
```

"expo":{
"ios":{
"privacyManifests":{
"NSPrivacyAccessedAPITypes":[
"NSPrivacyAccessedAPIType":"NSPrivacyAccessedAPICategoryUserDefaults",
"NSPrivacyAccessedAPITypeReasons":["CA92.1"]

```

  * **New expo-symbols library provides access to the iOS SF Symbols library**. This package provides a way to use the [SF Symbols](https://developer.apple.com/sf-symbols/), a collection of over 5000 icons with multiple weights, scales, and support for animations. [Learn more](https://docs.expo.dev/versions/v51.0.0/sdk/symbols/)


Autocompletion with TypeScript makes it easy to find the right symbol for [expo-symbols](https://docs.expo.dev/versions/v51.0.0/sdk/symbols/).
  * **Fingerprint runtime version policy promoted from experimental to beta** : by using the `"runtimeVersion": { "policy": "fingerprint" }` field in your **app.json** , you can be confident that your updates will always target compatible native runtimes. This makes `@expo/fingerprint` integration with EAS Build and Update seamless. [Learn more about how this helps you to achieve Continuous Deployment](https://docs.expo.dev/eas-update/continuous-deployment/), and [learn about how @expo/fingerprint works](https://expo.dev/blog/fingerprint-your-native-runtime).
  * **ESLint config and** **`npx expo lint`****command** : You can now run `npx expo lint` in your project to generate an ESLint config file that extends from [`eslint-config-expo`](https://github.com/expo/expo/tree/main/packages/eslint-config-expo). The philosophy of this config is to focus on code correctness and avoid stylistic rules that can be subjective. More documentation is coming soon, until then you can [read the rules in the source code](https://github.com/expo/expo/tree/main/packages/eslint-config-expo/utils).


Code
Copy
```

# When ESLint is not configured yet
npx expo lint
? No ESLint config found. Install and configure ESLint in this project? › (Y/n)
# After ESLint has been configured
npx expo lint
>yarn eslint .
$ /app/node_modules/.bin/eslint .
/app/components/HelloWave.tsx
22:6 warning React Hook useEffect has a missing dependency: 'rotateAnimation'. Either include it or remove the dependency array react-hooks/exhaustive-deps
✖ 1 problem (0 errors, 1 warning)

```

  * **Modernized library build.gradle**. If you maintain an Expo module, you don't need to change anything; but, if you want to clean your module up a bit, you can apply the changes from [this diff](https://gist.github.com/brentvatne/88e27545243b828554bb376a7e6dd08d). [Learn more about the changes in](https://github.com/expo/expo/pull/28083) [**expo/expo#28083**](https://github.com/expo/expo/pull/28083).
  * **Bundler speed improvements** : `EXPO_USE_FAST_RESOLVER=1` can be set to enable up to 6x faster Metro resolution. We've also fully removed ["exotic" bundling](https://blog.expo.dev/drastically-faster-bundling-in-react-native-a54f268e0ed1) in favor of the default expo/metro-config which has fully integrated stable speed improvements.
  * **Expo CLI supports running on iOS devices over the network and for Vision Pro simulators**. Use `npx expo run:ios --device` to pick a device from the list of available devices on your network, in the same way you would from the device selection window in Xcode.


Code
Copy
```

npx expo run:ios --device
? Select a device ›
❯  🌐 Brent iPhone (17.4.1)
  🌐 Apple Vision Pro (1.1.1)
  iPhone 15(17.4)
  iPhone 15 Plus (17.4)
 ↓ iPad Pro (12.9-inch)(6th generation)(17.4)

```

  * **Expo Orbit for Windows is available in beta**. One click to download, install, and run your apps, now for Windows too! Try it out and give us feedback. [Learn more](https://expo.dev/blog/expo-orbit-now-available-as-a-preview-for-windows).
  * **EAS Build default worker image for iOS builds now uses macOS 14.4 and Xcode 15.3** [Learn more](https://docs.expo.dev/build-reference/infrastructure/).
  * **React Native 0.74 and React 18.2.0 (unchanged from SDK 50)**. There were many improvements in this release, so refer to the [React Native CHANGELOG](https://github.com/facebook/react-native/blob/main/CHANGELOG.md), and [Release Notes](https://reactnative.dev/blog/2024/04/22/release-0.74). One change that many folks will be excited about is that [Yoga has been upgraded to 3.0](https://yogalayout.dev/blog/announcing-yoga-3.0), which improves layout correctness and adds support for two additional layout properties. You may also be able to drop a few polyfills: `TextEncoder`, `btoa`, `atob` are now globally available in Hermes.

### [Notable breaking changes ](https://expo.dev/changelog/2024-04-24-sdk-51-beta#notable-breaking-changes)
  * **expo-camera imports have changed** : if you want to continue using the legacy implementation, update your imports from `expo-camera` to `expo-camera/legacy`. If you were already using the "next" implementation, then update the imports from `expo-camera/next` to `expo-camera`. The legacy implementation will be available until SDK 52.
  * **expo-sqlite imports have changed** : if you want to continue using the legacy implementation, update your imports from `expo-sqlite` to `expo-sqlite/legacy`. If you were already using the "next" implementation, then update the imports from `expo-sqlite/next` to `expo-sqlite`. The legacy implementation will be available until SDK 52.
  * **Fingerprint runtime version policy has been renamed** : `"runtimeVersion": { "policy": "fingerprintExperimental" }` → `"runtimeVersion": { "policy": "fingerprint" }` in your **app.json**.
  * **The** **`hooks`****field has been removed from app.json** : this was previously used for the [Classic Updates](https://blog.expo.dev/sunsetting-expo-publish-and-classic-updates-6cb9cd295378) and `sentry-expo`, which was deprecated in SDK 50 in favor of [`@sentry/react-native`](https://docs.expo.dev/guides/using-sentry/). You should remove the `hooks` field from your app config.
  * **sentry-expo is no longer supported, use @sentry/react-native instead**. In SDK 50, `sentry-expo` was deprecated in favor of `@sentry/react-native`, which we worked closely with the Sentry team on to ensure first-class support for Expo projects. [Learn more](https://docs.expo.dev/guides/using-sentry/).
  * **Expo Go only supports a single SDK version as of SDK 51.** [Learn more](https://expo.dev/changelog/2024/04-24-sdk-51-beta#single-sdk-version-in-expo-go).

### [New Architecture is rolling out in 2024! ](https://expo.dev/changelog/2024-04-24-sdk-51-beta#new-architecture-is-rolling-out-in-2024)
SDK 51 and React Native 0.74 represent a huge step forward in rolling out the long-awaited New Architecture for React Native.
  * We have added support for ["bridgeless"](https://github.com/reactwg/react-native-new-architecture/discussions/154), one of the pillars of the New Architecture, to nearly all Expo modules and the Expo Modules API.
  * We worked in close collaboration with the React Native team at Meta and developers in the React Native ecosystem to ensure there would be support for the New Architecture in many of the most commonly used packages on EAS Build.

#### [Testing your app with the New Architecture ](https://expo.dev/changelog/2024-04-24-sdk-51-beta#testing-your-app-with-the-new-architecture)
There is still work to do, but we've made some incredible progress so far this year and we think SDK 51 and React Native 0.74 is the time to test your apps with the New Architecture. With your help, we can enable the New Architecture by default in SDK 52.
That said, most apps will run into some issues when testing with the New Architecture today, but [we encourage you to try](https://docs.expo.dev/guides/new-architecture/#can-i-still-try-the-new-architecture) and [report your experience](https://github.com/reactwg/react-native-new-architecture/discussions/177). Improvements will be arriving rapidly during the SDK 51 and React Native 0.74 cycle, so if your initial attempt isn't successful, you might want to create a branch that you can retry every couple weeks with the latest versions of every package.
  * [Read about the known issues](https://docs.expo.dev/guides/new-architecture/#troubleshooting) to get an idea of what to expect.
  * [Learn more enabling the New Architecture in your app](https://docs.expo.dev/guides/new-architecture/).

### [Single SDK version in Expo Go ](https://expo.dev/changelog/2024-04-24-sdk-51-beta#single-sdk-version-in-expo-go)
[As announced in SDK 50](https://expo.dev/changelog/2024/01-18-sdk-50#a-single-sdk-version-per-release-of-the-expo-go-app:-looking-ahead-to-sdk-51), starting with SDK 51, Expo Go will only support a single SDK version at a time. This means that when the new Expo Go version supporting SDK 51 is released to the App Store and Play Store, it will only support SDK 51. It will not support SDK 50 or below. The Expo Go app will continue to be a great sandbox to get started quickly and experiment with ideas, but we encourage adopting [development builds](https://docs.expo.dev/develop/development-builds/introduction/) for a flexible and powerful development environment suitable for real-world applications at scale.
To make it as easy as possible to install a specific version of Expo Go, created [expo.dev/go](https://expo.dev/go), a website that makes it as easy as possible to install a compatible version of Expo Go on your target platform. This works on Android devices/emulators and iOS simulators, but due to limitations of the iOS platform, you will only be able to use the latest version of Expo Go on physical iOS devices.
[expo.dev/go](https://expo.dev/go) makes it easy to install a compatible version of Expo Go on your target platform. The error message that you see when you try to open a project with an unsupported SDK version in Expo Go links directly to this website with the appropriate version and platform selected.
### [Expo Router v3.5 ](https://expo.dev/changelog/2024-04-24-sdk-51-beta#expo-router-v35)
Most of the user-facing changes in the latest release of Expo Router are bug fixes and improvements based on feedback from the community. Some notable changes include:
  * Support for the # segment in URLs with `const { "#": hash } = useLocalSearchParams()`.
  * Added new router functions for dismissing routes `router.dismiss()`, `.dismissAll()` and `.canDismiss()`
  * Removed `ExpoRequest` and `ExpoResponse` objects in favor of built-in WinterCG-compliant Request/Response objects.
  * Support for platform specific extensions for routes and `_layout` files (a platform agnostic version is still required).
  * Support to handle rewriting deeplinked URLs.
  * Improvements to Typed Routes.
  * Href in typed routes is no longer generic.
  * Fixes issues for `experiments.baseUrl` support on web.

### [Known issues ](https://expo.dev/changelog/2024-04-24-sdk-51-beta#known-issues)
  * **Alerts rendered incorrectly after system UI windows for biometric authentication, and perhaps others**. This will be fixed in an upcoming React Native patch release by [facebook/react-native#44167](https://github.com/facebook/react-native/pull/44167)

### [Known regressions ](https://expo.dev/changelog/2024-04-24-sdk-51-beta#known-regressions)
  * Found an issue? [Report a regression](https://github.com/expo/expo/issues/new?assignees=&amp;labels=needs+review&amp;template=bug_report.yml).

### [How to try out the beta release ](https://expo.dev/changelog/2024-04-24-sdk-51-beta#how-to-try-out-the-beta-release)
  * **Initialize a new project with SDK 51 beta:**
    * **npm:** `npx create-expo-app@latest --template default@beta`
    * **bun:** `bun create expo-app --template default@beta`
    * **pnpm** : create expo-app --template default@beta
    * **yarn:** `yarn create expo-app --template default@beta`
    * **Note:** `create-expo-app` will install dependencies with the package manager that you are using. For example, with npm when `npx` is used and yarn when `yarn create` used.
  * **Upgrade an existing project:**
    * Upgrade all dependencies to match SDK 51: `npx expo install expo@next --fix`
  * **Install the latest Expo Go for iOS to your physical device:**
    * Use this [TestFlight open beta link](https://testflight.apple.com/join/GZJxxfUU) and follow the instructions.
  * **Install the latest Expo Go for iOS simulators or Android emulators/physical devices:**
    * Launch your project through Expo CLI (press the `i` or `a` keyboard shortcut after running `npx expo start`) and the updated version of Expo Go will be automatically installed.
  * **SDK 51 beta is not yet available on Snack.**
  * [**Read the documentation**](https://docs.expo.dev/versions/v51.0.0) by selecting it from the version selector in the API reference section.

### [What to test ](https://expo.dev/changelog/2024-04-24-sdk-51-beta#what-to-test)
  * Upgrade your app with `npm install expo@next` or `yarn add expo@next`, then run `npx expo install --fix` and consult the [Native project upgrade helper](https://docs.expo.dev/bare/upgrade/) and [report any issues you encounter](https://github.com/expo/expo/issues/new?assignees=&amp;labels=needs+review&amp;template=bug_report.yml).
  * Build your app with EAS Build, and/or if you have Xcode installed and up to date on your machine and/or Android Studio, try prebuilding your app and running it: `npx expo prebuild --clean` and `npm run ios` and `npm run android`. Alternatively, try out `npx expo run`. Any new issues? [Please report them](https://github.com/expo/expo/issues/new?assignees=&amp;labels=needs+review&amp;template=bug_report.yml).
  * Did we miss updating the documentation somewhere? [Let us know](https://github.com/expo/expo/issues/new?assignees=&amp;labels=docs&amp;template=documentation.yml&amp;title=%5Bdocs%5D+).

### [How to report issues ](https://expo.dev/changelog/2024-04-24-sdk-51-beta#how-to-report-issues)
  * Create an issue on <https://github.com/expo/expo/issues> and be sure to fill out the appropriate template (and include a [minimal reproducible example](https://stackoverflow.com/help/minimal-reproducible-example), please!).
  * Figuring out the underlying causes of issues is super helpful.
  * Let us know that you are using the SDK 51 beta so we can prioritize the issue.
  * The most helpful beta testers will be listed in the final release notes (and possibly even provided with some [Discord](https://chat.expo.dev/) flair — you can [link your Discord and GitHub accounts to your Expo account](https://expo.dev/settings#connections)).


Thank you for helping us with testing the release — we look forward to shipping it soon! 🚀

