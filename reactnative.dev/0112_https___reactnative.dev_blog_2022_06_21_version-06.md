---
url: https://reactnative.dev/blog/2022/06/21/version-069
title: https://reactnative.dev/blog/2022/06/21/version-069
date: 2025-05-10T21:34:19.454568
depth: 2
---

[Skip to main content](https://reactnative.dev/blog/2022/06/21/version-069#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
We are excited to release a new version of React Native, 0.69.0. This version comes with several improvements for the New Architecture of React Native and new features: React 18 support & bundled Hermes. Read on to learn more!
### Sections[​](https://reactnative.dev/blog/2022/06/21/version-069#sections "Direct link to Sections")
  * [Highlights of 0.69](https://reactnative.dev/blog/2022/06/21/version-069#highlights-of-069)


## React 18[​](https://reactnative.dev/blog/2022/06/21/version-069#react-18 "Direct link to React 18")
We are delighted to share with you that React Native 0.69 is the first release to support React 18. React 18 has brought [lots of improvements](https://reactjs.org/blog/2022/03/29/react-v18.html), like new hooks such as `useId`. Additionally, React 18 includes new concurrency features such as `useTransition` or full Suspense support.
On React Native 0.69, React 18 is enabled by default. However, if you have not migrated to the New Architecture, you will only be able to leverage the features that don't use concurrent rendering and concurrent features. The New Architecture has been built with concurrent rendering in mind but we cannot add that support for the old architecture.
You can learn more about the React 18 support in React Native [here](https://reactnative.dev/docs/0.69/react-18-and-react-native).
## Bundled Hermes[​](https://reactnative.dev/blog/2022/06/21/version-069#bundled-hermes "Direct link to Bundled Hermes")
Before this release, Hermes and React Native were released separately. That led to confusion on which version of Hermes is compatible with which version of React Native. To remedy this issue, starting with React Native 0.69 we will be shipping a compatible version of Hermes alongside React Native. Making this change will make using Hermes in React Native much more stable.
Using the proper version of Hermes is handled by React Native, however, make sure to follow the steps in the [upgrade helper](https://react-native-community.github.io/upgrade-helper/?from=0.68.2&to=0.69.0) to ensure the integration works as intended. If you don't have Hermes enabled already, you can follow the steps [here](https://reactnative.dev/docs/hermes) to do so. While we will continue supporting other JavaScript engines, we recommend everyone to migrate to Hermes to have the best experience and to make sure we can support you better.
Note that users on the New Architecture on Android will need to **build Hermes from source**. For building Hermes from source, Windows users will need to additionally follow [these steps](https://reactnative.dev/architecture/bundled-hermes#android-users-on-new-architecture-building-on-windows).
If you are interested to learn more about how React Native bundles Hermes works under the hood, you can check out the deep-dive documentation [here](https://reactnative.dev/architecture/bundled-hermes).
## New Architecture[​](https://reactnative.dev/blog/2022/06/21/version-069#new-architecture "Direct link to New Architecture")
We are continuing the roll-out of the New Architecture for both Android and iOS. If you have not migrated your app or library, yet, follow the steps [here](https://github.com/reactwg/react-native-new-architecture#guides). You can also read the [latest update](https://reactnative.dev/blog/2022/06/16/resources-migrating-your-react-native-library-to-the-new-architecture) on tools and resources for the New Architecture to learn more.
## Highlights of 0.69[​](https://reactnative.dev/blog/2022/06/21/version-069#highlights-of-069 "Direct link to Highlights of 0.69")
As mentioned above, the most important improvements in this release are centered around React 18 support and bundled Hermes. However, there have been other notable changes, including:
  * [Deprecating support](https://github.com/facebook/react-native/commit/982ca30de079d7e80bd0b50365d58b9048fb628f) for iOS/tvOS SDK 11.0, version 12.4+ is now required
  * [Better support](https://github.com/facebook/react-native/commit/c5babd993a2bed2994ecc4710fa9e424b3e6cfc2) for M1 users developing for Android
  * [Addition](https://github.com/facebook/react-native/commit/0480f56c5b5478b6ebe5ad88e347cad2810bfb17) of the new `.xcode.env` configuration file for more deterministically sourcing the node executable
  * [React Native now uses](https://github.com/facebook/react-native/commit/50c8e973f067d4ef1fc3c2eddd360a0709828968) the latest status bar API from Android 11
  * [New](https://github.com/facebook/react-native/commit/1a1a304ed2023d60547aef65b1a7bf56467edf08) `hotkeysEnabled` option in the iOS debug menu


### Breaking changes[​](https://reactnative.dev/blog/2022/06/21/version-069#breaking-changes "Direct link to Breaking changes")
There have also been a few breaking changes:
  * React Native CLI has been bumped to a new major version of [8.0](https://github.com/react-native-community/cli/releases/tag/v8.0.0): 
    * `link` and `unlink` commands have been removed in the favour of autolinking
    * Deprecated `initCompat` has been removed, use `init` command instead
    * Removed deprecated `run-android` properties
    * Removed `install` and `uninstall` commands
    * Removed assets and hooks from `react-native.config.js` – you'll need to remove these properties from your config
    * `podspecPath` was removed from the iOS dependency config
    * Removed `--project-path` option from a `run-ios`
    * Changed iOS source directory detection from looking for an Xcode project to looking for a Podfile
  * Support for `console.disableYellowBox` [has been dropped](https://github.com/facebook/react-native/commit/b633cc130533f0731b2577123282c4530e4f0abe)
  * Already deprecated prop types have been removed ([cdfddb4dad](https://github.com/facebook/react-native/commit/cdfddb4dad7c69904850d7e5f089a32a1d3445d1), [3e229f27bc](https://github.com/facebook/react-native/commit/3e229f27bc9c7556876ff776abf70147289d544b), [10199b1581](https://github.com/facebook/react-native/commit/10199b158138b8645550b5579df87e654213fe42))
  * `removeListener`, deprecated since RN 0.65, [was removed](https://github.com/facebook/react-native/commit/8dfbed786b40082a7a222e00dc0a621c0695697d) from Appearance
  * If you were using `SegmentedComponentIOS`, you will now need to replace it with the third-party library, for example [segmented-control](https://github.com/react-native-segmented-control/segmented-control) ([235f168574](https://github.com/facebook/react-native/commit/235f1685748442553e53f8ec6d904bc0314a8ae6))


### Upgrades[​](https://reactnative.dev/blog/2022/06/21/version-069#upgrades "Direct link to Upgrades")
And we upgraded some of our dependencies:
  * Bump [of AGP to 7.1.1](https://github.com/facebook/react-native/commit/200488e87cf4bc355e03c78cd814b97b23452117) - we recommend sticking to this version in your apps
  * `boost` for Android was updated to 1.76 [to align with iOS](https://github.com/facebook/react-native/commit/5cd6367f0b86543274a15bb6d0e53a8545fed845)
  * Ruby [was bumped to 2.7.5](https://github.com/facebook/react-native/commit/2c87b7466e098c5cd230e02b279fc7bc7a357615)
  * Direct metro dependencies [have been upgraded](https://github.com/facebook/react-native/commit/b74e964e705c40834acad7020562e870cdad9db1) to 0.70.1


You can check out the full list of changes [in the changelog](https://github.com/facebook/react-native/blob/main/CHANGELOG.md#0690).
### Acknowledgements[​](https://reactnative.dev/blog/2022/06/21/version-069#acknowledgements "Direct link to Acknowledgements")
80 contributors with their 629 commits have helped to make this release possible - thanks everyone!
We are also thankful to the release testers, supporters, and everyone else who gave their feedback to ensure this release will be as stable as possible.
  * [Bundled Hermes](https://reactnative.dev/blog/2022/06/21/version-069#bundled-hermes)
  * [New Architecture](https://reactnative.dev/blog/2022/06/21/version-069#new-architecture)
  * [Highlights of 0.69](https://reactnative.dev/blog/2022/06/21/version-069#highlights-of-069)
    * [Breaking changes](https://reactnative.dev/blog/2022/06/21/version-069#breaking-changes)
    * [Acknowledgements](https://reactnative.dev/blog/2022/06/21/version-069#acknowledgements)



