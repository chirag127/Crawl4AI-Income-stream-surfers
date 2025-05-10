---
url: https://reactnative.dev/blog/tags/announcement
title: https://reactnative.dev/blog/tags/announcement
date: 2025-05-10T21:34:57.395808
depth: 2
---

[Skip to main content](https://reactnative.dev/blog/tags/announcement#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
React Native 0.76 with the New Architecture by default is now available on npm!
In the [0.76 release blog post](https://reactnative.dev/blog/2024/10/23/release-0.76-new-architecture), we shared a list of significant changes included in this version. In this post, we provide an overview of the New Architecture and how it shapes the future of React Native.
The New Architecture adds full support for modern React features, including [Suspense](https://react.dev/blog/2022/03/29/react-v18#new-suspense-features), [Transitions](https://react.dev/blog/2022/03/29/react-v18#new-feature-transitions), [automatic batching](https://react.dev/blog/2022/03/29/react-v18#new-feature-automatic-batching), and [`useLayoutEffect`](https://react.dev/reference/react/useLayoutEffect). The New Architecture also includes new [Native Module](https://reactnative.dev/docs/next/turbo-native-modules-introduction) and [Native Component](https://reactnative.dev/docs/next/fabric-native-components-introduction) systems that let you write type-safe code with direct access to native interfaces without a bridge.
This release is the result of a ground-up rewrite of React Native we’ve been working on since 2018, and we’ve taken extra care to make the New Architecture a gradual migration for most apps. In 2021, we created [the New Architecture Working Group](https://github.com/reactwg/react-native-new-architecture/) to collaborate with the community on ensuring a smooth upgrade experience for the entire React ecosystem.
Most apps will be able to adopt React Native 0.76 with the same level of effort as any other release. The most popular React Native libraries already support the New Architecture. The New Architecture also includes an automatic interoperability layer to enable backward compatibility with libraries targeting the old architecture.
Today we are excited to release React Native 0.76!
This is a major milestone for React Native, as we’re enabling the New Architecture by default, and we’re introducing React Native DevTools. This has been the culmination of 6 years of hard work from our team, together with the support of our incredible community of developers.
### Highlights[​](https://reactnative.dev/blog/tags/announcement#highlights "Direct link to Highlights")
  * [React Native New Architecture by default](https://reactnative.dev/blog/2024/10/23/release-0.76-new-architecture#react-native-new-architecture-by-default)
  * [React Native DevTools](https://reactnative.dev/blog/2024/10/23/release-0.76-new-architecture#react-native-devtools)
  * [Faster Metro resolution](https://reactnative.dev/blog/tags/announcement#faster-metro-resolution)
  * [Box Shadow and Filter style props](https://reactnative.dev/blog/2024/10/23/release-0.76-new-architecture#box-shadow-and-filter-style-props)


### Breaking Changes[​](https://reactnative.dev/blog/tags/announcement#breaking-changes "Direct link to Breaking Changes")
  * [Removed the dependency on the react-native-community/cli](https://reactnative.dev/blog/2024/10/23/release-0.76-new-architecture#removed-the-dependency-on-the-react-native-communitycli)
  * [Android Apps are ~3.8Mb smaller thanks to Native Library merging](https://reactnative.dev/blog/2024/10/23/release-0.76-new-architecture#android-apps-are-38mb-smaller-thanks-to-native-library-merging)
  * [Updates to Minimum iOS and Android SDK requirements](https://reactnative.dev/blog/2024/10/23/release-0.76-new-architecture#updates-to-minimum-ios-and-android-sdk-requirements)


At [React Conf](https://www.youtube.com/live/0ckOUBiuxVY?si=pU4qP4eB5iWfY0IG&t=2320), we updated our guidance on the best tool to get started building React Native apps: a **React Native framework** - a toolbox with all the necessary APIs to let you build production-ready apps.
Using React Native frameworks, such as Expo, is now the **recommended** approach to create new apps.
In this blogpost we want to walk you through what they are in detail and what they mean for you as a React Native developer starting a new project.
Today we're releasing React Native 0.74! This release adds Yoga 3.0, Bridgeless by default under the New Architecture, batched `onLayout` updates (New Architecture), and Yarn 3 as the default package manager for new projects.
We are also removing deprecated APIs, with the removal of `PropTypes` and breaking changes to `PushNotificationIOS`. On Android, SDK 23 (Android 6.0) is now the minimum supported version.
### Highlights[​](https://reactnative.dev/blog/tags/announcement#highlights "Direct link to Highlights")
  * [New Architecture: Bridgeless by Default](https://reactnative.dev/blog/2024/04/22/release-0.74#new-architecture-bridgeless-by-default)
  * [New Architecture: Batched `onLayout` Updates](https://reactnative.dev/blog/2024/04/22/release-0.74#new-architecture-batched-onlayout-updates)
  * [Yarn 3 for New Projects](https://reactnative.dev/blog/2024/04/22/release-0.74#yarn-3-for-new-projects)


### Breaking Changes[​](https://reactnative.dev/blog/tags/announcement#breaking-changes "Direct link to Breaking Changes")
  * [Android Minimum SDK Bump (Android 6.0)](https://reactnative.dev/blog/2024/04/22/release-0.74#android-minimum-sdk-bump-android-60)
  * [API Changes to PushNotificationIOS (Deprecated)](https://reactnative.dev/blog/2024/04/22/release-0.74#api-changes-to-pushnotificationios-deprecated)
  * [Removal of Deprecated `PropTypes`](https://reactnative.dev/blog/2024/04/22/release-0.74#removal-of-deprecated-proptypes)
  * [Removal of Flipper React Native Plugin](https://reactnative.dev/blog/2024/04/22/release-0.74#removal-of-flipper-react-native-plugin)
  * [Other Breaking Changes](https://reactnative.dev/blog/2024/04/22/release-0.74#other-breaking-changes)


Today we're releasing React Native 0.73! This release adds improvements to debugging with Hermes, stable symlink support, Android 14 support, and new experimental features. We are also deprecating legacy debugging features, and are releasing the next pillar of the New Architecture: Bridgeless Mode!
### Highlights[​](https://reactnative.dev/blog/tags/announcement#highlights "Direct link to Highlights")
  * [Debugging Improvements](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#debugging-improvements)
  * [Stable Symlink Support in Metro](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#stable-symlink-support-in-metro)
  * [Kotlin Template on Android](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#kotlin-template-on-android)
  * [New Architecture Updates](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#new-architecture-updates)
  * [Deprecated Debugging Features](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#deprecated-debugging-features)


### Breaking Changes[​](https://reactnative.dev/blog/tags/announcement#breaking-changes "Direct link to Breaking Changes")
  * [Babel Package Renames](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#babel-package-renames)
  * [Other Breaking Changes](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#other-breaking-changes)
  * [React Native CLI Changes](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#react-native-cli-changes)
  * [Deprecated @types/react-native](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#deprecated-typesreact-native)


Today we’re releasing 0.72!
This release adds highly requested features for Metro, better error handling, and other developer experience improvements. So much of this work was prioritized from your feedback on the [2022 community survey](https://github.com/react-native-community/discussions-and-proposals/discussions/528) -- thank you to all those that participated!
### Highlights[​](https://reactnative.dev/blog/tags/announcement#highlights "Direct link to Highlights")
  * [Developer Experience Improvements](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#developer-experience-improvements)
  * [Moving New Architecture Updates](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#moving-new-architecture-updates)


### Breaking Changes[​](https://reactnative.dev/blog/tags/announcement#breaking-changes "Direct link to Breaking Changes")
  * [Deprecated Component Removals](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#deprecated-component-removals)


With the release of [React Native 0.72](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks), Metro — our JavaScript build tool — now includes beta support for the `package.json` [`"exports"`](https://nodejs.org/docs/latest-v18.x/api/packages.html#exports) field. When [enabled](https://reactnative.dev/blog/2023/06/21/package-exports-support#enabling-package-exports-beta), it adds the following functionality:
  * [React Native projects will work with more npm packages out-of-the-box](https://reactnative.dev/blog/2023/06/21/package-exports-support#for-app-developers)
  * [New capabilities for packages to define their API and target React Native](https://reactnative.dev/blog/2023/06/21/package-exports-support#for-package-maintainers-preview)
  * [Some breaking changes to package resolution (in edge cases)](https://reactnative.dev/blog/2023/06/21/package-exports-support#breaking-changes)


In this post we'll cover how Package Exports works, and what these changes mean for you as a React Native app developer or package maintainer.
Today we’re releasing React Native version 0.71! This is a feature-packed release including:
  * [TypeScript by default](https://reactnative.dev/blog/2023/01/12/version-071#typescript-by-default)
  * [Simplifying layouts with Flexbox Gap](https://reactnative.dev/blog/2023/01/12/version-071#simplifying-layouts-with-flexbox-gap)
  * [Web-inspired props for accessibility, styles, and events](https://reactnative.dev/blog/2023/01/12/version-071#web-inspired-props-for-accessibility-styles-and-events)
  * [Restoring PropTypes](https://reactnative.dev/blog/2023/01/12/version-071#restoring-proptypes)
  * [Developer Experience Improvements](https://reactnative.dev/blog/2023/01/12/version-071#developer-experience-improvements)
  * [New Architecture Updates](https://reactnative.dev/blog/2023/01/12/version-071#new-architecture)


In this post we’ll cover some of the highlights of 0.71.
Today we are sharing an experimental cross-platform pointer API for React Native. We’ll go over motivations, how it works, and its benefits to React Native users. There are instructions on how to enable and we’re excited to hear your feedback!
It’s been over a year since we shared [our many platform vision](https://reactnative.dev/blog/2021/08/26/many-platform-vision) on the wins of building beyond mobile and how it sets a higher bar for all platforms. During this time, we've increased our investments in React Native for VR, Desktop, and Web. With differences in hardware and interactions on these platforms, it raised the question of how React Native should holistically handle input.
After years of pandemic and online-only events, we really felt it was time to bring the Core Contributors of React Native together!
That’s why at the beginning of September, we gathered some of the active core contributors of React Native, library maintainers, and the Meta’s React Native and Metro teams to the **Core Contributor Summit 2022**. [Callstack](https://www.callstack.com/) hosted the Summit in their HQ in Wrocław, Poland, as a part of the [React Native EU](https://www.react-native.eu/) conference happening at the same time.
Together with the React Native core team, we devised a series of **workshops** in which the attendees could participate. The topics were:
  * ​​React Native Codegen & TypeScript Support
  * ​​React Native New Architecture Library Migration
  * ​​React Native Monorepo
  * Metro Web and Ecosystem Alignment
  * Metro Simplified Release Workflow


We were impressed by the amount of knowledge-sharing and collaboration over those two days. In this blog post, we’d like to give you a sneak peek of the results of this gathering.

