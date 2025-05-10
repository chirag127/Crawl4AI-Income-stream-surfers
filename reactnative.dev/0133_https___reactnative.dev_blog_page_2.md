---
url: https://reactnative.dev/blog/page/2
title: https://reactnative.dev/blog/page/2
date: 2025-05-10T21:34:54.758332
depth: 2
---

[Skip to main content](https://reactnative.dev/blog/page/2#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
Today we’re releasing 0.72!
This release adds highly requested features for Metro, better error handling, and other developer experience improvements. So much of this work was prioritized from your feedback on the [2022 community survey](https://github.com/react-native-community/discussions-and-proposals/discussions/528) -- thank you to all those that participated!
### Highlights[​](https://reactnative.dev/blog/page/2#highlights "Direct link to Highlights")
  * [Developer Experience Improvements](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#developer-experience-improvements)
  * [Moving New Architecture Updates](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#moving-new-architecture-updates)


### Breaking Changes[​](https://reactnative.dev/blog/page/2#breaking-changes "Direct link to Breaking Changes")
  * [Deprecated Component Removals](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#deprecated-component-removals)


With the release of [React Native 0.72](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks), Metro — our JavaScript build tool — now includes beta support for the `package.json` [`"exports"`](https://nodejs.org/docs/latest-v18.x/api/packages.html#exports) field. When [enabled](https://reactnative.dev/blog/2023/06/21/package-exports-support#enabling-package-exports-beta), it adds the following functionality:
  * [React Native projects will work with more npm packages out-of-the-box](https://reactnative.dev/blog/2023/06/21/package-exports-support#for-app-developers)
  * [New capabilities for packages to define their API and target React Native](https://reactnative.dev/blog/2023/06/21/package-exports-support#for-package-maintainers-preview)
  * [Some breaking changes to package resolution (in edge cases)](https://reactnative.dev/blog/2023/06/21/package-exports-support#breaking-changes)


In this post we'll cover how Package Exports works, and what these changes mean for you as a React Native app developer or package maintainer.
Now that 0.71 is [available](https://reactnative.dev/blog/2023/01/12/version-071), we want to share some key information about the incident that broke Android builds for all React Native versions while releasing the first 0.71 release candidate for React Native & Expo Android builds on November 4th, 2022.
The contributors who helped tackle the incident recently attended a post-mortem meeting to discuss in detail what happened, what we all learned from it, and what actions we are going to take to avoid similar outages in the future.
Today we’re releasing React Native version 0.71! This is a feature-packed release including:
  * [TypeScript by default](https://reactnative.dev/blog/2023/01/12/version-071#typescript-by-default)
  * [Simplifying layouts with Flexbox Gap](https://reactnative.dev/blog/2023/01/12/version-071#simplifying-layouts-with-flexbox-gap)
  * [Web-inspired props for accessibility, styles, and events](https://reactnative.dev/blog/2023/01/12/version-071#web-inspired-props-for-accessibility-styles-and-events)
  * [Restoring PropTypes](https://reactnative.dev/blog/2023/01/12/version-071#restoring-proptypes)
  * [Developer Experience Improvements](https://reactnative.dev/blog/2023/01/12/version-071#developer-experience-improvements)
  * [New Architecture Updates](https://reactnative.dev/blog/2023/01/12/version-071#new-architecture)


In this post we’ll cover some of the highlights of 0.71.
With the release of 0.71, React Native is investing in the TypeScript experience with the following changes:
  * [New app template is TypeScript by default](https://reactnative.dev/blog/2023/01/03/typescript-first#new-app-template-is-typescript-by-default)
  * [TypeScript declarations shipped with React Native](https://reactnative.dev/blog/2023/01/03/typescript-first#declarations-shipped-with-react-native)
  * [React Native documentation is TypeScript First](https://reactnative.dev/blog/2023/01/03/typescript-first#documentation-is-typescript-first)


In this post we’ll cover what these changes mean for you as a TypeScript or Flow user.
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
We are excited to release a new version of React Native, 0.70.0. This version comes with several improvements like a new unified configuration for Codegen, Hermes as default engine, and full CMake support for Android builds along with a refresh of the documentation for the New Architecture. Read on to learn more!
### Sections[​](https://reactnative.dev/blog/page/2#sections "Direct link to Sections")
  * [New Architecture’s New Documentation](https://reactnative.dev/blog/2022/09/05/version-070#new-architectures-new-documentation)
  * [Hermes as default engine](https://reactnative.dev/blog/2022/09/05/version-070#hermes-as-default-engine)
  * [A new unified configuration for Codegen](https://reactnative.dev/blog/2022/09/05/version-070#a-new-unified-configuration-for-codegen)
  * [Android Auto-linking for New Architecture libraries](https://reactnative.dev/blog/2022/09/05/version-070#android-auto-linking-for-new-architecture-libraries)
  * [Full CMake support for Android builds](https://reactnative.dev/blog/2022/09/05/version-070#full-cmake-support-for-android-builds)
  * [Highlights of 0.70](https://reactnative.dev/blog/2022/09/05/version-070#highlights-of-070)


Last October, we [announced](https://reactnative.dev/blog/2021/10/26/toward-hermes-being-the-default) that we had started work towards **making** **Hermes the default engine for all React Native apps**.
Hermes has provided a lot of value to React Native inside of Meta, and we believe the open-source community will benefit as well. Hermes is designed for resource constrained devices and optimizes for start up, app size, and memory consumption. One key difference between Hermes and other JS engines is its ability to compile JavaScript source code to bytecode ahead of time. This precompiled bytecode is bundled inside the binary, and saves the interpreter from having to perform this expensive step during app startup.
Since the announcement, a lot of work has gone into making Hermes better, and today, we are excited to share that **React Native 0.70 will ship with Hermes as the default engine.** This means that all new projects starting on v0.70 will have Hermes enabled by default. With the rollout coming up in July, we want to work closely with the community and make sure the transition is smooth and brings value to all users. This blogpost will go over what you can expect from the change, performance benchmarks, new features, and more. Note that you don’t need to wait for React Native 0.70 to start using Hermes - you can **follow[these instructions](https://reactnative.dev/docs/hermes#enabling-hermes) to enable Hermes on your existing React Native app**.
Note that while Hermes will be enabled by default in new React Native projects, support for other engines will continue.
We are excited to release a new version of React Native, 0.69.0. This version comes with several improvements for the New Architecture of React Native and new features: React 18 support & bundled Hermes. Read on to learn more!
### Sections[​](https://reactnative.dev/blog/page/2#sections "Direct link to Sections")
  * [Highlights of 0.69](https://reactnative.dev/blog/2022/06/21/version-069#highlights-of-069)



