---
url: https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks
title: https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks
date: 2025-05-10T21:34:49.455632
depth: 2
---

[Skip to main content](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
Today we're releasing React Native 0.73! This release adds improvements to debugging with Hermes, stable symlink support, Android 14 support, and new experimental features. We are also deprecating legacy debugging features, and are releasing the next pillar of the New Architecture: Bridgeless Mode!
### Highlights[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#highlights "Direct link to Highlights")
  * [Debugging Improvements](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#debugging-improvements)
  * [Stable Symlink Support in Metro](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#stable-symlink-support-in-metro)
  * [Kotlin Template on Android](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#kotlin-template-on-android)
  * [New Architecture Updates](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#new-architecture-updates)
  * [Deprecated Debugging Features](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#deprecated-debugging-features)


### Breaking Changes[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#breaking-changes "Direct link to Breaking Changes")
  * [Babel Package Renames](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#babel-package-renames)
  * [Other Breaking Changes](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#other-breaking-changes)
  * [React Native CLI Changes](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#react-native-cli-changes)
  * [Deprecated @types/react-native](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#deprecated-typesreact-native)


## Highlights[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#highlights-1 "Direct link to Highlights")
### Debugging Improvements[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#debugging-improvements "Direct link to Debugging Improvements")
The React Native and Hermes teams are committed to improving the debugging experience in React Native. In 0.73, we're happy to share some initial progress out of this ongoing investment.
#### Console Log History in Hermes[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#console-log-history-in-hermes "Direct link to Console Log History in Hermes")
`console.log()` is an ever popular way for developers to quickly debug their JavaScript code. In previous releases, console logs in React Native apps would not be recorded until a debugger was connected. This made it hard to observe logs that occur early during app load.
In React Native 0.73 we've addressed this issue. Hermes now captures all `console.log()` calls in the background, which will be sent to the Console tab when a debugger is first connected — matching the debugging experience in web browsers. This new behaviour works across Flipper, Chrome DevTools connected to Hermes, and the experimental New Debugger.
#### Updated Debugging Docs[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#updated-debugging-docs "Direct link to Updated Debugging Docs")
We've refreshed the [Debugging](https://reactnative.dev/docs/debugging) section of our docs, which now includes up-to-date information on how to connect all supported debuggers, more info on React DevTools, and refreshed visuals.
#### Experimental New Debugger[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#experimental-new-debugger "Direct link to Experimental New Debugger")
The React Native team is working on a new JavaScript debugger experience, intended to replace Flipper, with a Technical Preview available as of React Native 0.73. The new debugger opens immediately, and features a stripped-back Chrome DevTools UI customized for debugging React Native with Hermes.
note
The new debugger is **experimental** and has some [known issues](https://github.com/react-native-community/discussions-and-proposals/discussions/733) we are actively working to solve in a future release of React Native. If you are trying it out, please use the [same discussion thread](https://github.com/react-native-community/discussions-and-proposals/discussions/733) to report feedback.
Learn more about enabling this experience [in the docs](https://reactnative.dev/docs/next/debugging?js-debugger=new-debugger#opening-the-debugger).
### Stable Symlink Support in Metro[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#stable-symlink-support-in-metro "Direct link to Stable Symlink Support in Metro")
Support for resolving symlinks in Metro is now **enabled by default**. Symlink support enables React Native to work with monorepo setups when containing directories are configured with [`watchFolders`](https://metrobundler.dev/docs/configuration/#watchfolders).
Symlinks are deeply represented in Metro's internals, meaning they work with features such as [Fast Refresh](https://reactnative.dev/docs/fast-refresh), and incur little performance overhead during bundling. Symlinks are supported on all desktop platforms, with and without Watchman.
info
#### Monorepo workarounds[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#monorepo-workarounds "Direct link to Monorepo workarounds")
We are aware there are still edge cases when using React Native in a monorepo layout. We have planned work to address some of these, which didn't quite make it into 0.73 — but which we aim to ship as soon as possible.
**For React Native template projects (`npx react-native init`)**, you will need to configure any [`watchFolders`](https://metrobundler.dev/docs/configuration/#watchfolders) outside of the project root in order for Metro to discover them ([more info](https://metrobundler.dev/docs/configuration/#unstable_enablesymlinks-experimental)). You may also need to update file paths if your `react-native` dependency is installed to a folder at a different level.
**For Expo apps** , support for Yarn (Classic) workspaces is configured out of the box. See also the [Work with monorepos](https://docs.expo.dev/guides/monorepos/) guide in the Expo docs.
### Kotlin Template on Android[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#kotlin-template-on-android "Direct link to Kotlin Template on Android")
We're excited to announce that, starting from 0.73, Kotlin is now the **recommended language** for Android apps built with React Native. This follows the direction that the Android ecosystem has been moving in for several years and allows you to write your app using a modern language.
We've updated React Native's template on Android to use Kotlin instead of Java. The new `MainActivity.kt` and `MainApplication.kt` files are 36% smaller in size.
The [Upgrade Helper](https://react-native-community.github.io/upgrade-helper/) has also been updated to make it easier to migrate your `.java` files to `.kt` files. If you've previously modified the Java files in your project and you need support migrating them to Kotlin, you can use the `Code > Convert Java file to Kotlin File` utility of Android Studio (also accessible with the shortcut `Cmd ⌘` + `Shift ⇧` + `Option ⌥` + `K`).
### Android 14 Support[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#android-14-support "Direct link to Android 14 Support")
We've updated React Native to fully support Android 14. Starting from 0.73, React Native developers can now target the latest Android SDK version, [API Level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element?hl=en#ApiLevels) (_Upside Down Cake_).
#### Java 17 and Android Gradle Plugin upgrade[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#java-17-and-android-gradle-plugin-upgrade "Direct link to Java 17 and Android Gradle Plugin upgrade")
In order to support Android 14, we've updated the version of Android Gradle Plugin (AGP) used to build Android apps from `7.4.x` to `8.1.x`.
This major version bump of AGP comes with a series of breaking changes that are available in the release notes from Google ([8.0.0](https://developer.android.com/build/releases/past-releases/agp-8-0-0-release-notes) and [8.1.0](https://developer.android.com/build/releases/past-releases/agp-8-1-0-release-notes)).
Most importantly, **Java 17** is now a requirement to build Android apps. You can update your Java version to 17 by running:
```
brew install--cask zulu@17
```

and by updating your `JAVA_HOME` as documented in the [Getting Started guide](https://reactnative.dev/docs/environment-setup).
If you're a library developer, your libraries should work with React Native 0.73 without changes. Earlier this year, [we published a note](https://github.com/react-native-community/discussions-and-proposals/issues/671) with a clarification on what the AGP bump means for you as a library author.
#### Grant partial access to photos and videos[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#grant-partial-access-to-photos-and-videos "Direct link to Grant partial access to photos and videos")
[Selected Photos Access](https://developer.android.com/about/versions/14/changes/partial-photo-video-access) allows Android 14 users to grant apps access to specific items in their media library, rather than access to all media. In 0.73, React Native apps now support this capability, by using the `READ_MEDIA_VISUAL_USER_SELECTED` permission in the [`PermissionsAndroid`](https://reactnative.dev/docs/permissionsandroid) API.
#### Min SDK bump[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#min-sdk-bump "Direct link to Min SDK bump")
React Native 0.73 will be the final version which supports Android 5.0 (API Level 21). The next version of React Native will have a minimum SDK version of 23 (Android 6.0). Read more about the upcoming changes to min SDK bump [here](https://github.com/react-native-community/discussions-and-proposals/discussions/740).
### New Architecture Updates[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#new-architecture-updates "Direct link to New Architecture Updates")
We continue the rollout of React Native's New Architecture, to make it available to everyone in the Open Source community.
Since React Native 0.68, both the New Renderer (Fabric) and the New Native Module System (TurboModules) were available to users to experiment and evaluate. We want to thank the community for the feedback we've received so far.
Today we're releasing another piece of the New Architecture: [**Bridgeless Mode**](https://github.com/reactwg/react-native-new-architecture/discussions/154). Up until now, when you enable the New Architecture in your app, the Bridge would still be available to support backward compatibility with older components and modules. However, our vision is to fully sunset the bridge. Starting from React Native 0.73, you can enable Bridgeless Mode which will disable the creation of the bridge entirely.
Together with Bridgeless Mode, we're shipping a Native Module Interop Layer, that will allow you to reuse your old modules when in Bridgeless Mode. The [Renderer Interop Layer](https://github.com/reactwg/react-native-new-architecture/discussions/135) introduced in React Native 0.72 has also been adapted to work with Bridgeless Mode.
As with the rest of the New Architecture, Bridgeless Mode is initially experimental. We invite interested users to enable it and report any problems and incompatibilities you face in the [New Architecture working group](https://github.com/reactwg/react-native-new-architecture/discussions).
### Deprecated Debugging Features[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#deprecated-debugging-features "Direct link to Deprecated Debugging Features")
#### Flipper ↔ React Native integration[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#flipper--react-native-integration "Direct link to Flipper ↔ React Native integration")
We are gradually moving away from Flipper as the default tool for debugging React Native apps. In 0.73, this begins by deprecating the native Flipper integration included with React Native (bootstrap code which wires up Flipper's core plugins). We will be removing this integration and dependency in the next release — meaning parts of Flipper such as the Network plugin will cease to work.
**Unchanged** : Flipper as a standalone product for native app debugging will continue to exist. Even after its removal from new React Native projects in the future, developers will be able to [manually add Flipper to their app](https://fbflipper.com/docs/getting-started/android-native/) if they wish.
For more information on why we are moving away from Flipper, [view the RFC](https://github.com/react-native-community/discussions-and-proposals/blob/main/proposals/0641-decoupling-flipper-from-react-native-core.md).
#### Remote JavaScript Debugging[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#remote-javascript-debugging "Direct link to Remote JavaScript Debugging")
Remote JavaScript Debugging is a legacy debugging mode that connects an external web browser (Chrome) to your app and runs your JavaScript code inside a web page, i.e. `http://localhost:8081/debugger-ui`. This model could lead to inconsistent app behaviour while debugging, and is incompatible with native modules under the New Architecture.
In 0.73, [Remote JavaScript Debugging is deprecated](https://github.com/react-native-community/discussions-and-proposals/discussions/734) and has been removed from the Dev Menu. Enabling the remote debugger must now be done manually via the `NativeDevSettings` API. Doing this is covered in the [Other Debugging Methods docs](https://reactnative.dev/docs/next/other-debugging-methods#remote-js-debugging).
info
Remote JavaScript Debugging was previously the default debugging experience for apps using JavaScriptCore (JSC). We recommend [Safari Developer Tools (direct JSC debugging)](https://reactnative.dev/docs/next/other-debugging-methods#safari-developer-tools-direct-jsc-debugging) instead, for iOS apps.
We recommend using [Hermes](https://reactnative.dev/docs/hermes) for a consistent debugging experience on all platforms.
## Breaking Changes[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#breaking-changes-1 "Direct link to Breaking Changes")
### Babel Package Renames[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#babel-package-renames "Direct link to Babel Package Renames")
We've relocated two Babel-related packages out of Metro and into React Native's repository and versioning scheme, enabling us to simplify maintenance and upgrades. The new versions of these packages support New Architecture features in 0.73, meaning these dependencies must be updated.
Please follow the [Upgrade Helper](https://react-native-community.github.io/upgrade-helper/) when upgrading, to ensure you have updated these dependencies. Some packages have been renamed:
Old Package Name| New Package Name  
---|---  
`metro-react-native-babel-preset`| `@react-native/babel-preset`  
`metro-react-native-babel-transformer`| `@react-native/metro-babel-transformer`  
info
`@react-native/babel-preset` now includes `@react-native/babel-plugin-codegen`, this no longer needs to be specified separately in your Babel config file.
### Other Breaking Changes[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#other-breaking-changes "Direct link to Other Breaking Changes")
These are some of the key breaking changes in 0.73. Please consult the [full changelog](https://github.com/facebook/react-native/blob/main/CHANGELOG.md) for the complete list of breaking changes.
  * Raise minimum Node.js requirement to 18.x ([#37709](https://github.com/facebook/react-native/pull/37709)) (see also [Node.js 16 EOL](https://nodejs.org/en/blog/announcements/nodejs16-eol)).
  * The template now uses TypeScript 5.0 ([#36862](https://github.com/facebook/react-native/pull/36862)). 
    * React Native types continue working on TypeScript 4.8.
  * **Android** : Java 17 is now a requirement to build Android apps ([see above](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#java-17-and-android-gradle-plugin-upgrade)).
  * **Android** : Major bump of Fresco to 3.0 ([#38275](https://github.com/facebook/react-native/pull/38275)).
  * **iOS** : Raise minimum iOS version to 13.4 ([#36795](https://github.com/facebook/react-native/pull/36795)).
  * **iOS** : Metro will no longer be automatically started when running builds via Xcode ([#38242](https://github.com/facebook/react-native/pull/38242)).


For library authors:
  * **Android** : Bump to AGP 8.1.1 ([discussion](https://github.com/react-native-community/discussions-and-proposals/issues/671))


### React Native CLI Changes[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#react-native-cli-changes "Direct link to React Native CLI Changes")
#### Highlighted breaking changes[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#highlighted-breaking-changes "Direct link to Highlighted breaking changes")
  * Change default task prefix in `build-android` command. From now on, when you run `build-android`, the `bundle` task will be run instead of `assemble` ([#1913](https://github.com/react-native-community/cli/pull/1913)).
  * Remove fallback flow for Metro config defaults ([#1972](https://github.com/react-native-community/cli/pull/1972)). 
    * The [updated `metro.config.js` format](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#new-metroconfigjs-setup) from 0.72 is now required in 0.73, as we have removed the fallback copy of these defaults from CLI.
  * Remove `--configuration` option from `run-ios` (replaced with `--mode`) ([#2028](https://github.com/react-native-community/cli/pull/2028)).
  * Remove `--variant` option from `build-android` command (replaced with `--mode`) ([#2026](https://github.com/react-native-community/cli/pull/2026)).


[See full changelog for v12.0.0](https://github.com/react-native-community/cli/releases/tag/v12.0.0).
### Deprecated `@types/react-native`[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#deprecated-typesreact-native "Direct link to deprecated-typesreact-native")
As mentioned in [First-class Support for TypeScript](https://reactnative.dev/blog/2023/01/03/typescript-first#declarations-shipped-with-react-native), we have shipped TypeScript types with `react-native` since 0.71 and we are now deprecating `@types/react-native` for 0.73.
We will not ship any future patches for existing versions. The guidance is to migrate away from `@types/react-native`. See instructions on [how to migrate](https://reactnative.dev/blog/2023/01/03/typescript-first#how-to-migrate).
## Acknowledgements[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#acknowledgements "Direct link to Acknowledgements")
React Native 0.73 contains over [2259 commits](https://github.com/facebook/react-native/compare/v0.72.7...v0.73.0) from 68 contributors. Thanks for all your hard work!
## Upgrade to 0.73[​](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#upgrade-to-073 "Direct link to Upgrade to 0.73")
Please use the [React Native Upgrade Helper](https://react-native-community.github.io/upgrade-helper/) to view code changes between React Native versions for existing projects, in addition to the [Upgrading docs](https://reactnative.dev/docs/upgrading). You can also create a new project with `npx react-native@latest init MyProject`.
If you use Expo, React Native 0.73 will be supported in the Expo SDK 50 release.
info
0.73 is now the latest stable version of React Native and **0.70.x now moves to unsupported**. For more information see [React Native’s support policy](https://github.com/reactwg/react-native-releases#releases-support-policy).
  * [Breaking Changes](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#breaking-changes)
  * [Highlights](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#highlights-1)
    * [Debugging Improvements](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#debugging-improvements)
    * [Stable Symlink Support in Metro](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#stable-symlink-support-in-metro)
    * [Kotlin Template on Android](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#kotlin-template-on-android)
    * [Android 14 Support](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#android-14-support)
    * [New Architecture Updates](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#new-architecture-updates)
    * [Deprecated Debugging Features](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#deprecated-debugging-features)
  * [Breaking Changes](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#breaking-changes-1)
    * [Babel Package Renames](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#babel-package-renames)
    * [Other Breaking Changes](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#other-breaking-changes)
    * [React Native CLI Changes](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#react-native-cli-changes)
    * [Deprecated `@types/react-native`](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#deprecated-typesreact-native)
  * [Acknowledgements](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#acknowledgements)
  * [Upgrade to 0.73](https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks#upgrade-to-073)



