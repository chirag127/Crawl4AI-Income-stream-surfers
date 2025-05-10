---
url: https://reactnative.dev/blog
title: https://reactnative.dev/blog
date: 2025-05-10T20:52:17.662011
depth: 1
---

[Skip to main content](https://reactnative.dev/blog#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
Today we are excited to release React Native 0.79!
This release ships with performance improvements on various fronts, as well as several bugfixes. First, Metro is now faster to start thanks to deferred hashing, and has stable support for package exports. Startup time in Android will also be improved thanks to changes in the JS bundle compressions and much more.
### Highlights[​](https://reactnative.dev/blog#highlights "Direct link to Highlights")
  * [JSC moving to a Community Package](https://reactnative.dev/blog/2025/04/08/react-native-0.79#jsc-moving-to-community-package)
  * [iOS: Swift-Compatible Native Modules registration](https://reactnative.dev/blog/2025/04/08/react-native-0.79#ios-swift-compatible-native-modules-registration)
  * [Android: Faster App Startup](https://reactnative.dev/blog/2025/04/08/react-native-0.79#android-faster-app-startup)
  * [Removal of Remote JS Debugging](https://reactnative.dev/blog/2025/04/08/react-native-0.79#removal-of-remote-js-debugging)


Today we are excited to release React Native 0.78!
This release ships React 19 in React Native and some other relevant features like native support for Android Vector drawables and better brownfield integration for iOS.
### Highlights[​](https://reactnative.dev/blog#highlights "Direct link to Highlights")
  * [Towards smaller and faster releases](https://reactnative.dev/blog/2025/02/19/react-native-0.78#towards-smaller-and-faster-releases)
  * [Opt-in for JavaScript logs in Metro](https://reactnative.dev/blog/2025/02/19/react-native-0.78#opt-in-for-javascript-logs-in-metro)
  * [Added support for Android XML drawables](https://reactnative.dev/blog/2025/02/19/react-native-0.78#added-support-for-android-xml-drawables)
  * [ReactNativeFactory on iOS](https://reactnative.dev/blog/2025/02/19/react-native-0.78#reactnativefactory-on-ios)


Every year, the core contributors in the React Native Community get together with the React Native team to collaboratively shape the direction of this project.
Last year was no different—with small exception. We usually meet a day before [React Universe Conf](https://www.reactuniverseconf.com) (formerly React Native EU) at [Callstack](https://www.callstack.com/open-source) HQ in Wrocław. In 2024, learning from past experiences, we hosted the Summit for two consecutive days, so that we can have more unstructured time together.
Today we are excited to release React Native 0.77!
This release ships several features: new styling capabilities such as support for `display: contents`, `boxSizing`, `mixBlendMode`, and `outline`-related properties to provide a more powerful layout options; Android 16KB page support to be compatible with the newer Android devices. We are also modernizing the community template by migrating it to Swift, while continuing to support and maintain compatibility with Objective-C for developers who prefer it.
React Native 0.76 with the New Architecture by default is now available on npm!
In the [0.76 release blog post](https://reactnative.dev/blog/2024/10/23/release-0.76-new-architecture), we shared a list of significant changes included in this version. In this post, we provide an overview of the New Architecture and how it shapes the future of React Native.
The New Architecture adds full support for modern React features, including [Suspense](https://react.dev/blog/2022/03/29/react-v18#new-suspense-features), [Transitions](https://react.dev/blog/2022/03/29/react-v18#new-feature-transitions), [automatic batching](https://react.dev/blog/2022/03/29/react-v18#new-feature-automatic-batching), and [`useLayoutEffect`](https://react.dev/reference/react/useLayoutEffect). The New Architecture also includes new [Native Module](https://reactnative.dev/docs/next/turbo-native-modules-introduction) and [Native Component](https://reactnative.dev/docs/next/fabric-native-components-introduction) systems that let you write type-safe code with direct access to native interfaces without a bridge.
This release is the result of a ground-up rewrite of React Native we’ve been working on since 2018, and we’ve taken extra care to make the New Architecture a gradual migration for most apps. In 2021, we created [the New Architecture Working Group](https://github.com/reactwg/react-native-new-architecture/) to collaborate with the community on ensuring a smooth upgrade experience for the entire React ecosystem.
Most apps will be able to adopt React Native 0.76 with the same level of effort as any other release. The most popular React Native libraries already support the New Architecture. The New Architecture also includes an automatic interoperability layer to enable backward compatibility with libraries targeting the old architecture.
Today we are excited to release React Native 0.76!
This is a major milestone for React Native, as we’re enabling the New Architecture by default, and we’re introducing React Native DevTools. This has been the culmination of 6 years of hard work from our team, together with the support of our incredible community of developers.
### Highlights[​](https://reactnative.dev/blog#highlights "Direct link to Highlights")
  * [React Native New Architecture by default](https://reactnative.dev/blog/2024/10/23/release-0.76-new-architecture#react-native-new-architecture-by-default)
  * [React Native DevTools](https://reactnative.dev/blog/2024/10/23/release-0.76-new-architecture#react-native-devtools)
  * [Faster Metro resolution](https://reactnative.dev/blog#faster-metro-resolution)
  * [Box Shadow and Filter style props](https://reactnative.dev/blog/2024/10/23/release-0.76-new-architecture#box-shadow-and-filter-style-props)


### Breaking Changes[​](https://reactnative.dev/blog#breaking-changes "Direct link to Breaking Changes")
  * [Removed the dependency on the react-native-community/cli](https://reactnative.dev/blog/2024/10/23/release-0.76-new-architecture#removed-the-dependency-on-the-react-native-communitycli)
  * [Android Apps are ~3.8Mb smaller thanks to Native Library merging](https://reactnative.dev/blog/2024/10/23/release-0.76-new-architecture#android-apps-are-38mb-smaller-thanks-to-native-library-merging)
  * [Updates to Minimum iOS and Android SDK requirements](https://reactnative.dev/blog/2024/10/23/release-0.76-new-architecture#updates-to-minimum-ios-and-android-sdk-requirements)


Today we are excited to release React Native 0.75!
This release ships several features, such as Yoga 3.1 with support for `%` values, several stabilization fixes for the New Architecture, and the introduction of the recommendation for users to use a React Native Framework.
### Highlights[​](https://reactnative.dev/blog#highlights "Direct link to Highlights")
  * [Yoga 3.1 and Layout Improvements](https://reactnative.dev/blog/2024/08/12/release-0.75#yoga-31-and-layout-improvements)
  * [New Architecture Stabilization](https://reactnative.dev/blog/2024/08/12/release-0.75#new-architecture-stabilization)


### Breaking Changes[​](https://reactnative.dev/blog#breaking-changes "Direct link to Breaking Changes")
  * [Touchables in TypeScript can’t be used as types in Generic expressions anymore](https://reactnative.dev/blog/2024/08/12/release-0.75#touchables-in-typescript-cant-be-used-as-types-in-generic-expressions-anymore)
  * [Last version supporting minSdk 23 and minIOSVersion 13.4](https://reactnative.dev/blog/2024/08/12/release-0.75#last-version-supporting-minsdk-23-and-miniosversion-134)
  * [Android: JSIModule has been deleted](https://reactnative.dev/blog/2024/08/12/release-0.75#android-jsimodule-has-been-deleted)
  * [Android: PopUp Menu removed from core](https://reactnative.dev/blog/2024/08/12/release-0.75#android-popup-menu-moved-to-separate-package)
  * [iOS: Finalized Push Notifications deprecation work](https://reactnative.dev/blog/2024/08/12/release-0.75#ios-finalized-pushnotificationios-deprecation-work)
  * [Community CLI: Removal of ram-bundle and profile-hermes commands](https://reactnative.dev/blog/2024/08/12/release-0.75#community-cli-removal-of-ram-bundle-and-profile-hermes-commands)


At [React Conf](https://www.youtube.com/live/0ckOUBiuxVY?si=pU4qP4eB5iWfY0IG&t=2320), we updated our guidance on the best tool to get started building React Native apps: a **React Native framework** - a toolbox with all the necessary APIs to let you build production-ready apps.
Using React Native frameworks, such as Expo, is now the **recommended** approach to create new apps.
In this blogpost we want to walk you through what they are in detail and what they mean for you as a React Native developer starting a new project.
Today we're releasing React Native 0.74! This release adds Yoga 3.0, Bridgeless by default under the New Architecture, batched `onLayout` updates (New Architecture), and Yarn 3 as the default package manager for new projects.
We are also removing deprecated APIs, with the removal of `PropTypes` and breaking changes to `PushNotificationIOS`. On Android, SDK 23 (Android 6.0) is now the minimum supported version.
### Highlights[​](https://reactnative.dev/blog#highlights "Direct link to Highlights")
  * [New Architecture: Bridgeless by Default](https://reactnative.dev/blog/2024/04/22/release-0.74#new-architecture-bridgeless-by-default)
  * [New Architecture: Batched `onLayout` Updates](https://reactnative.dev/blog/2024/04/22/release-0.74#new-architecture-batched-onlayout-updates)
  * [Yarn 3 for New Projects](https://reactnative.dev/blog/2024/04/22/release-0.74#yarn-3-for-new-projects)


### Breaking Changes[​](https://reactnative.dev/blog#breaking-changes "Direct link to Breaking Changes")
  * [Android Minimum SDK Bump (Android 6.0)](https://reactnative.dev/blog/2024/04/22/release-0.74#android-minimum-sdk-bump-android-60)
  * [API Changes to PushNotificationIOS (Deprecated)](https://reactnative.dev/blog/2024/04/22/release-0.74#api-changes-to-pushnotificationios-deprecated)
  * [Removal of Deprecated `PropTypes`](https://reactnative.dev/blog/2024/04/22/release-0.74#removal-of-deprecated-proptypes)
  * [Removal of Flipper React Native Plugin](https://reactnative.dev/blog/2024/04/22/release-0.74#removal-of-flipper-react-native-plugin)
  * [Other Breaking Changes](https://reactnative.dev/blog/2024/04/22/release-0.74#other-breaking-changes)


Today we're releasing React Native 0.73! This release adds improvements to debugging with Hermes, stable symlink support, Android 14 support, and new experimental features. We are also deprecating legacy debugging features, and are releasing the next pillar of the New Architecture: Bridgeless Mode!
### Highlights[​](https://reactnative.dev/blog#highlights "Direct link to Highlights")
  * [Debugging Improvements](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#debugging-improvements)
  * [Stable Symlink Support in Metro](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#stable-symlink-support-in-metro)
  * [Kotlin Template on Android](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#kotlin-template-on-android)
  * [New Architecture Updates](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#new-architecture-updates)
  * [Deprecated Debugging Features](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#deprecated-debugging-features)


### Breaking Changes[​](https://reactnative.dev/blog#breaking-changes "Direct link to Breaking Changes")
  * [Babel Package Renames](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#babel-package-renames)
  * [Other Breaking Changes](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#other-breaking-changes)
  * [React Native CLI Changes](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#react-native-cli-changes)
  * [Deprecated @types/react-native](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#deprecated-typesreact-native)



