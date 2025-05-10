---
url: https://expo.dev/changelog/sdk-53-beta
title: https://expo.dev/changelog/sdk-53-beta
date: 2025-04-30T17:19:25.085177
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [Expo SDK 53 beta is now available](https://expo.dev/changelog/sdk-53-beta)
Apr 12, 2025 by
Brent Vatne
**The SDK 53 beta period begins today and will last approximately two weeks.** The beta is an opportunity for developers to test out the SDK and ensure that the new release does not introduce any regressions for their particular systems and app configurations. We will be continuously releasing fixes and improvements during the beta period — some of these may include breaking changes.
SDK 53 beta includes React Native 0.79.0 and React 19.0.0. The full release notes for SDK 53 won't be available until the stable release, but you can browse the changelogs in the [expo/expo repository](https://github.com/expo/expo) to learn more about the scope of the release and any breaking changes. We'll merge all changelogs into the root [**CHANGELOG.md**](https://github.com/expo/expo/blob/main/CHANGELOG.md) when the beta is complete.
We're also [hosting office hours on Discord](https://chat.expo.dev/) for those of you interested in helping test the release!
## [The New Architecture is now also default for existing projects ](https://expo.dev/changelog/sdk-53-beta#the-new-architecture-is-now-also-default-for-existing-projects)
In SDK 52, we enabled the New Architecture in all new projects, but it remained opt-in for existing projects. **In SDK 53, the New Architecture is enabled by default in all projects, and you must explicitly opt out if you aren’t ready to adopt it yet**. [Learn how to opt out](https://docs.expo.dev/guides/new-architecture/#disable-the-new-architecture-in-an-existing-project).
If you use `react-native-maps`, instead of using the currently recommended 1.20.0 version, [try installing the the latest 1.21.0 release](https://github.com/react-native-maps/react-native-maps/releases/tag/v1.21.0) (`npx expo install react-native-maps@1.21.0` , [exclude it from version validation](https://docs.expo.dev/versions/latest/config/package-json/#installexclude), and [apply this change to the config plugin](https://github.com/expo/expo/pull/35848)). This version includes full support for the New Architecture, and it could benefit from additional testing from the broader community before it is recommended as a default version for Expo SDK 53. Additionally, if your app depends heavily on this open source, community maintained library, consider joining us in sponsoring the project to support its ongoing maintenance. For apps that require maps and that are able to enforce a minimum version of iOS 17 (or don't support iOS), then you could consider the new Swift UI and Jetpack Compose based [expo-maps](https://docs.expo.dev/versions/latest/sdk/maps/) as an alternative.
If you use `@stripe/stripe-react-native`, note that it does not yet support the New Architecture — but [it is coming soon](https://github.com/stripe/stripe-react-native/issues/1275#issuecomment-2695944483).
If there are any issues blocking you from migrating to the New Architecture, [create an issue on expo/expo](https://github.com/expo/expo/issues/new?template=bug_report.yml), and [opt out](https://docs.expo.dev/guides/new-architecture/#disable-the-new-architecture-in-an-existing-project) until the issue is resolved.
## [Rolling out edge-to-edge by default for new Android projects ](https://expo.dev/changelog/sdk-53-beta#rolling-out-edge-to-edge-by-default-for-new-android-projects)
In SDK 52, we shared that we were working with [@zoontek](https://github.com/zoontek) to help ship [react-native-edge-to-edge](https://github.com/zoontek/react-native-edge-to-edge), a library that 'effortlessly enables [edge-to-edge](https://developer.android.com/develop/ui/views/layout/edge-to-edge) display in React Native, allowing your Android app content to flow seamlessly beneath the system bars.' This has become increasingly important, because Google has announced that [**opting out of edge-to-edge will no longer be possible in Android 16**](https://developer.android.com/about/versions/16/behavior-changes-16#edge-to-edge), coming in June.
> [Android 15 enforced edge-to-edge](https://developer.android.com/about/versions/15/behavior-changes-15#edge-to-edge) for apps targeting Android 15 (API level 35), but your app could opt-out by setting [`R.attr#windowOptOutEdgeToEdgeEnforcement`](https://developer.android.com/reference/android/R.attr#windowOptOutEdgeToEdgeEnforcement) to `true`. For apps targeting Android 16 (API level 36), `R.attr#windowOptOutEdgeToEdgeEnforcement` is deprecated and disabled, and your app can't opt-out of going edge-to-edge.
In SDK 53, edge-to-edge on Android is now:
  * **enabled by default in the Expo Go app** , with no opt-out.
  * **enabled by default in all new projects** , with opt-out available outside of Expo Go.
  * **disabled by default in all existing projects** outside of Expo Go, with opt-in available and encouraged.


Looking to the future, in SDK 54, edge-to-edge will be the default for new and existing projects. A guide that goes more in depth will be coming in time for the proper SDK 53 release. Until then, refer to the [“Considerations” section of the react-native-edge-to-edge README](https://github.com/zoontek/react-native-edge-to-edge?tab=readme-ov-file#considerations).
## [Improved Swift UI and Jetpack Compose integration, powering an experimental new Expo UI package ](https://expo.dev/changelog/sdk-53-beta#improved-swift-ui-and-jetpack-compose-integration-powering-an-experimental-new-expo-ui-package)
Building this interface should take a couple minutes in your Expo iOS app, and we hope it will be soon with Expo UI. [Source code](https://github.com/expo/expo/blob/d5061581c76017af7d7db0bbf2410b296aa039e6/apps/native-component-list/src/screens/UI/SwiftUIContainerScreen.tsx).
[Expo UI](https://docs.expo.dev/versions/v53.0.0/sdk/ui/) aims to give developers easy access to native UI components from Jetpack Compose and SwiftUI. It will include essential platform primitives—like toggles, sliders, context menus, pickers, and lists—to complement existing community libraries built around Android Views and iOS UIKit.
**This library is experimental, it’s very rough, and it’s changing quickly.** APIs that you are using today may change tomorrow! Swift UI and Jetpack Compose are not yet widely used in the React Native ecosystem, and we’ve been exploring some unique approaches to integrating with these tools. **You will find issues and limitations** , and we encourage you to [report them](https://github.com/expo/expo/issues)!
This is not the first attempt at doing something like this in the ecosystem, and getting it off of the ground has been a joint effort — with contributions from folks like Andrew Levy, Janic Duplessis, Andrew Prifer, Emanuel Quimper, Benjamin Komen, Fernando Rojo, and the mysterious “Pflaumenbaum”. If this is a problem that you are interested in, we encourage you to contribute.
More information will be coming soon about the improved Swift UI and Jetpack Compose integration, you can [learn more about Expo UI in the API reference](https://docs.expo.dev/versions/unversioned/sdk/ui/), and [see examples on GitHub](https://github.com/expo/expo/tree/main/apps/native-component-list/src/screens/UI).
## [Added experimental support for caching local builds ](https://expo.dev/changelog/sdk-53-beta#added-experimental-support-for-caching-local-builds)
When you set `experiments.remoteBuildCache.provider` to `eas` in your app config, running `npx expo run:[ios|android]` will look for a build with a matching [fingerprint](https://expo.dev/blog/understanding-and-comparing-fingerprints-in-expo-apps) on EAS, and if one exists it will download and launch it rather than compiling the app again. If there is no matching build, then it will continue to compile locally as usual for the `run` command, then upload the archive once it is completed. On subsequent runs, you and your teammates will download the new build automatically and save a few minutes each time.
This video demonstrates what this flow looks like in action. Most of the cold cache build time was cut from the video, nobody needs to see that.
If you have been using `eas build:dev` , you might wonder what the difference is — the main distinction is that this `remoteBuildCache` approach will compile your app locally when there is a cache miss, rather than build on EAS. Additionally, during the beta we will add support for alternative remote cache provider implementations, so you will be able to host your own cache on GitHub or wherever you prefer.
During this initial experiment period, we’ve limited the number of cached builds with the EAS provider to 10 on the free and on demand plans, 50 with the production plan, and 100 with the enterprise plan (per billing cycle). We’ll adjust this as the feature moves towards a stable release. The cache is built on top of `eas upload` and `eas build:download` commands, which we built for the [Radon IDE](https://ide.swmansion.com/) team for this same use case — so you can expect to see similar behavior for Expo projects using the IDE in the near future.
[Let us know](https://bsky.app/profile/expo.dev) if this is useful for you and your team, and any other thoughts you have about similar tools we can build to help improve the speed of your development workflow.
## [Highlights ](https://expo.dev/changelog/sdk-53-beta#highlights)
  * **React Native 0.79** **with React 19 and React Native Web 0.20.0**. Refer to the release notes for [React Native 0.79](https://reactnative.dev/blog/2025/04/08/react-native-0.79) and [React 19](https://react.dev/blog/2024/12/05/react-19) release notes for detailed information. There are some great features in React 19 — such as `Suspense` for loading states and `use` for contexts and promises, so be sure to read up on it! Also, learn more about the [Expo SDK policy for tracking React Native versions.](https://docs.expo.dev/versions/v53.0.0#expo-sdk-policy-for-tracking-react-native)
  * **Stable release of new expo-audio library**. We released the beta for `expo-audio` in SDK 52 and received a lot of great feedback. We spent the last SDK cycle incorporating that feedback and making other improvements to the library, and now we're ready to call it stable! We recommend migrating to it from `expo-av` now. It is more reliable, easier to use, more performant, and more powerful than `Audio` component from `expo-av`. [Learn more about expo-audio](https://docs.expo.dev/versions/v53.0.0/sdk/audio/).
  * **New expo-maps package alpha release**. This library aims to provide wrappers for the platform standard APIs for maps — Google Maps on Android and Apple Maps for iOS. It is built on top of the modern Jetpack Compose and Swift UI APIs for each component. Keep in mind that _the minimum iOS version required to use the library is currently iOS 17, and s_ upport for older versions likely won’t be possible, due to limitations of the Swift UI API. We also do not intend to support Google Maps on iOS in this library. We’re excited about `expo-maps` because, like with our [Camera](https://docs.expo.dev/versions/v53.0.0/sdk/camera/), [Video](https://docs.expo.dev/versions/v53.0.0/sdk/video/), and [Audio](https://docs.expo.dev/versions/v53.0.0/sdk/audio/) libraries, it will be built with our philosophy of providing a stable, consistent, and reliable interface to the most common use cases that most apps will need. Other maps libraries in the ecosystem can focus on filling in more specific and uncommon use cases that a smaller set of app developers may need. [Learn more](https://docs.expo.dev/versions/v53.0.0/sdk/maps/).
  * **Improve Android build times with prebuilt Expo Modules.** Build time significantly impacts daily development. Recently, we announced that we’ve improved the iOS build time by upgrading our hardware — now it's time for Android. By precompiling some of our Expo Modules for Android in this SDK, you will experience up to a 25% reduction in build time locally (depending on your hardware). The improvements are currently more modest on EAS, but they enable us to build a more robust caching mechanism for EAS and further improve build times.By default, this feature is enabled when using a new project template. As always, you can opt out by passing `buildFromSource` to Expo Autolinking in the **package.json:**


package.json
Copy
```

"name":"opt-out-example",
"dependencies":{},
"expo":{
"autolinking":{
"android":{
"buildFromSource":[".*"]

```

  * **expo-updates** now allows you to override headers at runtime with `Updates.setUpdateURLAndRequestHeadersOverride()` , giving you full control over updates on the client side ([use it with caution](https://docs.expo.dev/eas-update/override/#security-considerations)). The `expo-updates` library was intentionally built with guardrails to minimize the risk of accidentally bricking your app, but there are sometimes cases where you would prefer to trade off these protections in favor of control, for example to enable the ability to allow a client to switch between updates (such as in a preview build for internal employees). [Learn more](https://docs.expo.dev/eas-update/override/).
  * **React Server Functions support is now in beta.** You can now deploy React Server Functions to production with EAS Hosting and the new `EXPO_UNSTABLE_DEPLOY_SERVER` environment variable, along with setting `experiments.reactServerFunctions` to `true` in your app config. [Learn more](https://docs.expo.dev/guides/server-components/).
  * **Improved background tasks -** our new module `expo-background-task` uses the latest APIs on Android and iOS and deprecates the `expo-background-fetch` module, which was based on now deprecated platform APIs. The new package supports running deferrable tasks in the background in a way that optimizes power usage on the end user’s device. Expo Background Task uses the [`WorkManager`](https://developer.android.com/topic/libraries/architecture/workmanager) API on Android and the [`BGTaskScheduler`](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler) API on iOS. Using this package, you can run tasks when your app is in the background and perform operations like downloading data, _running Expo Updates to check for and download new versions_ (you should do this!), or perform routine operations like cleaning up your database or uploading local data at regular intervals. [Learn more](https://docs.expo.dev/versions/latest/sdk/background-task/).
  * **Development builds can now be deployed to TestFlight.** More information available in [facebook/react-native#49154](https://github.com/facebook/react-native/pull/49154). This can be a good alternative to using ad hoc distribution, which requires registering every device by UDID to distribute development builds. Try it out with the new `npx testflight` package if you use EAS — set `"distribution": "store"` on your `development` profile and add `"development": {}` as a submit profile in **eas.json** , then then run `npx testflight --profile development` .
  * **Expo Modules for TV and macOS improvements:** the primary platforms supported by Expo are currently Android, iOS, and web, and we also invest in tvOS and Android TV through the [react-native-tvos](https://github.com/react-native-tvos/react-native-tvos) project. In Expo Orbit, we target macOS with the [react-native-macos](https://github.com/microsoft/react-native-macos) project and we have built support this platform into parts of the Expo SDK and Expo Modules APIs as needed for our development and maintenance of Orbit. In SDK 53, we added support for macOS AppDelegate subscribers and users can now extend directly from ExpoAppDelegate for an easier setup. [Learn more about Expo Module TV and macOS platform support](https://docs.expo.dev/modules/additional-platform-support/).
  * **expo-file-system/next** now integrates with [`expo/fetch`](https://docs.expo.dev/versions/latest/sdk/expo/#expofetch-api) for file uploads with `file.blob()`. [Learn more](https://docs.expo.dev/versions/v53.0.0/sdk/filesystem-next/).
  * **expo-sqlite now includes experimental support for web**. It uses a WebAssembly build of SQLite based on [wa-sqlite](https://github.com/rhashimoto/wa-sqlite), [with a few additions](https://github.com/expo/wa-sqlite). To learn more about other details of the implementation, see [expo#35207.](https://github.com/expo/expo/pull/35207) To learn how to use it, [refer to the documentation](https://docs.expo.dev/versions/v53.0.0/sdk/sqlite/#web-setup).
  * **expo-sqlite now supports libsql** , and in collaboration with Turso we’ve shipped support for their [Offline Sync Public Beta](https://turso.tech/blog/turso-offline-sync-public-beta). Give it a try and provide feedback to the Turso team to help the product grow! Learn more in this [example repository](https://github.com/betomoedano/notes-app) and its [accompanying YouTube video](https://www.youtube.com/watch?v=SBv32tmyb3k).
  * **expo-notifications improvements** : Following the deprecation of support for push notifications in Expo Go for Android in SDK 52, the feature is no longer supported in Expo Go for Android in SDK 53. Expo Go for iOS continues to work, along with all other environments. We recommend you [migrate to a development build](https://docs.expo.dev/develop/development-builds/introduction/#how-to-convert-from-expo-go-to-a-development-build) if you were using push notifications in Expo Go for Android. We added support for custom images and icons to the Expo Push Service for Android. The iOS implementation has been almost entirely converted to Swift and Expo modules API, making it easier to navigate and further improve — please verify that your notifications features work as expected during the beta, and report any regressions you might find. Breaking changes were introduced [here](https://github.com/expo/expo/pull/35295) and [here](https://github.com/expo/expo/pull/36361). Additionally, there was a number of bug fixes across both Android and iOS.
  * **Add import.meta transform plugin**. This is an experimental opt-in feature, you can turn it on with the `unstable_transformImportMeta` option in the `babel-preset-expo` configuration ([example](https://gist.github.com/Kudo/39041f31f3a055442f9200540e8da649)). This was added in order to improve ESM integration and specifically to better support [LiveStore](https://github.com/livestorejs/livestore).
  * **AppDelegate has moved from Objective-C to Swift**. Config Plugins that modify the AppDelegate source code will need to be updated to make Swift modifications rather than Objective-C.
  * **Bumped the recommend TypeScript version** to `~5.8.3`. We also now use this version in the [expo repository](https://github.com/expo/expo).
  * **Experimental opt-in React 19.1 support with improved errors available** : you can try it out by toggling `experiments.reactCanary` to `true` in your app config.

## [Expo CLI ](https://expo.dev/changelog/sdk-53-beta#expo-cli)
  * **Flat config support in eslint-config-expo**. `npx expo lint` now supports [flat config](https://eslint.org/blog/2022/08/new-config-system-part-2/). [Learn how to migrate](https://docs.expo.dev/guides/using-eslint/#migration-to-flat-config).
  * **package.json exports and imports now enabled by default.** This change comes from Metro bundler. This is a breaking change, see “**Notable breaking changes** ” below for additional information.
  * **Expo Atlas has been promoted from experimental to stable**. You can enable it with `EXPO_ATLAS=1 npx expo` to investigate your JavaScript bundle and improve the app size.
  * **Added experimental support for web workers on web.** This is used in `expo-sqlite` for multi-threaded web support. Native apps can still use native modules and Reanimated worklets to run JavaScript off the main thread. [Learn more](https://docs.expo.dev/versions/v53.0.0/config/metro/#web-workers).
  * **Added experimental EAS Update support to Expo DOM components**. You can now update your DOM components with `eas update` — be sure to test this in a staging build before updating your DOM components in production, and [report any issues to us](https://github.com/expo/expo/issues/new).
  * **Improved error messages.** React errors will now print symbolicated stack traces in the Expo CLI logs. This makes it easier to ⌘+click into a file and jump directly to the related line of code.


Code
Copy
```

Error: Couldn't find the bottom tab bar height. Are you inside a screenin Bottom Tab Navigator?
This error is located at:
20|
21|export default function ParallaxScrollView({
>22|  children,
|
23|  headerImage,
24|  headerBackgroundColor,
25|}: Props){
Call Stack
 ParallaxScrollView (components/ParallaxScrollView.tsx:22:11)
 HomeScreen(./(tabs)/index.tsx)(<anonymous>)
 Suspense (<anonymous>)
 RCTView (<anonymous>)
 RCTView (<anonymous>)
 RNSScreen (<anonymous>)
 Suspense (<anonymous>)
 RNSScreenNavigationContainer (<anonymous>)
 RCTView (<anonymous>)
 TabLayout (app/(tabs)/_layout.tsx:12:37)

```

## [Expo Router ](https://expo.dev/changelog/sdk-53-beta#expo-router)
  * **Added build-time redirects and rewrites**. These can be used for customizing the URL and routing behavior of your app and website. This is especially useful for migrating existing projects to Expo Router. [Learn more](https://docs.expo.dev/router/reference/redirects/).
  * **Make authentication and other flows using an initial redirect easier to build**. Apps are now wrapped in a virtual root navigator to ensure all navigation events can be processed.
  * **Improved Fast Refresh and error stack traces in Expo Router to improve development**.
  * **Improved documentation.** We're happy to share our much improved new Expo Router documentation. For example, check out the ["Router 101" section](https://docs.expo.dev/router/basics/core-concepts/) to shore up your foundational router knowledge.

## [Deprecations ](https://expo.dev/changelog/sdk-53-beta#deprecations)
  * **expo-av** : the Video component was replaced by [`expo-video`](https://docs.expo.dev/versions/v53.0.0/sdk/video/) in SDK 52 and the Audio API is replaced by [`expo-audio`](https://docs.expo.dev/versions/v53.0.0/sdk/audio/) in SDK 53. The [`expo-av`](https://docs.expo.dev/versions/v53.0.0/sdk/video-av/) package will no longer be maintained and we will not publish any new versions for SDK 54 and beyond.
  * **expo-background-fetch** : this has been replaced by [`expo-background-task`](https://docs.expo.dev/versions/v53.0.0/sdk/background-task/), which uses modern platform APIs.

## [Notable breaking changes ](https://expo.dev/changelog/sdk-53-beta#notable-breaking-changes)
  * **React 19** comes with some breaking changes, which you can learn more about in the [React 19 upgrade guide](https://react.dev/blog/2024/04/25/react-19-upgrade-guide) — note that you may skip over the web-specific instructions in the guide.
  * **Internal imports in React Native were updated to`export` syntax.** [Refer to the examples from the React Native 0.79 blog post to more](https://reactnative.dev/blog/2025/04/08/react-native-0.79#internal-modules-updated-to-export-syntax)**.**
  * **Updated default AppTheme.** New native Android projects and projects generated with CNG is now use the `DayNight` theme, see: <https://github.com/expo/expo/pull/33964>. This change was made in order to facilitate the rollout of edge-to-edge layout, for compatibility with [react-native-edge-to-edge](https://github.com/zoontek/react-native-edge-to-edge).
  * **Deprecated`setImmediate` polyfill has been removed from the runtime**.
  * **expo-status-bar and expo-navigation-bar are more limited when edge-to-edge is enabled.** Only the `StatusBar` component can be used, none of the imperative methods are available on either module. For now, you can control the navigation bar through the `SystemBars` API in `react-native-edge-to-edge`, and we will likely expose that through `expo-navigation-bar` as well.
  * **The package.json exports field is now enabled by default in Metro bundler.** You can opt out of this in your app by specifying `unstable_enablePackageExports: false` if you run into related issues ([source](https://github.com/facebook/metro/pull/1448)). If libraries that you depend on are incompatible with this change, it may manifest in subtle ways in your app caused by what’s known as the [dual package hazard](https://nodejs.org/docs/latest-v19.x/api/packages.html#dual-package-hazard) — your app may end up importing both the ESM and CommonJS versions of a library, and if that library is stateful then you will have two independent copies of it. One way is to [analyze your bundle with Expo Atlas](https://docs.expo.dev/guides/analyzing-bundles/). In the following screenshot, there are `commonjs` _and_ `module` copies of `@react-navigation` packages (the issue has already resolved in this particular case, this is only included here as an example). You will be able to identify the dual package hazard in your app by looking for this pattern. Additionally, If you are a library author and use [react-native-builder-bob](https://github.com/callstack/react-native-builder-bob), we recommend following [their guide to adapt to this change](https://github.com/callstack/react-native-builder-bob/releases/tag/react-native-builder-bob%400.40.0).


Exploring an app bundle using Expo Atlas, we can see the same source files are included multiple times for a single package, both under “commonjs” and “module”.
## [Known issues ](https://expo.dev/changelog/sdk-53-beta#known-issues)
  * **If you use npm, you may encounter installation issues related to peer dependencies** , eg: "ERESOLVE could not resolve" / "Could not resolve dependency". This is due to libraries having peer dependencies such as `"expo": ">= 52.0.0"`, which will not match `"expo@53.0.0-preview"` (due to [this quirk of npm](https://github.com/npm/npm/issues/8854)). You can work around this using `-legacy-peer-deps` and/or setting that option in your **.npmrc** file, or switching to another package manager.
  * **React 18 peer dependencies can lead to multiple`react` installations**. Many libraries have peer dependencies on React 18 — even though they are likely compatible with React 19. To prevent npm from installing multiple copies of `react`, which will cause runtime errors, [you may need to add `overrides` to your **package.json**](https://github.com/expo/expo/blob/b5d33e69cc81d16c53baf048b9847ec1fb0224fe/templates/expo-template-default/package.json#L45-L47) to ensure every library uses the same single version of React.

## [**Known regressions** ](https://expo.dev/changelog/sdk-53-beta#known-regressions)
  * Found an issue? [Report a regression](https://github.com/expo/expo/issues/new?assignees=&labels=needs+review&template=bug_report.yml).

### [How to try out the beta release ](https://expo.dev/changelog/sdk-53-beta#how-to-try-out-the-beta-release)#### [Initialize a new project with SDK 53 beta ](https://expo.dev/changelog/sdk-53-beta#initialize-a-new-project-with-sdk-53-beta)
Terminal
`# npm`
`- ``npx create-expo-app@latest --template default@sdk-53`
`# bun`
`- ``bun create expo-app --template default@sdk-53`
`# pnpm`
`- ``pnpm create expo-app --template default@sdk-53`
`# yarn`
`- ``yarn create expo-app --template default@sdk-53`
**Note:** `create-expo-app` will install dependencies with the package manager that you are using. For example, with npm when `npx` is used and yarn when `yarn create` used.
#### [Upgrade an existing project ](https://expo.dev/changelog/sdk-53-beta#upgrade-an-existing-project)
  * **Upgrade all dependencies to match SDK 53** :


Terminal
Copy
`- ``npx expo@next install --fix`
  * **Install the latest Expo Go for Android emulators/physical devices or iOS simulators:**
    * Launch your project through Expo CLI (press the a or i keyboard shortcut after running `npx expo start`) and the updated version of Expo Go will be automatically installed.
  * **Install the latest Expo Go for iOS to your physical device:**[Join the TestFlight External Beta](https://testflight.apple.com/join/GZJxxfUU).
  * [**Read the documentation**](https://docs.expo.dev/versions/v53.0.0) by selecting it from the version selector in the API reference section.

### [What to test ](https://expo.dev/changelog/sdk-53-beta#what-to-test)
  * Upgrade your app with `npm install expo@next` or `yarn add expo@next`, then run `npx expo install --fix` and consult the [Native project upgrade helper](https://docs.expo.dev/bare/upgrade/?fromSdk=52&toSdk=53) and [report any issues you encounter](https://github.com/expo/expo/issues/new?assignees=&amp;labels=needs+review&amp;template=bug_report.yml).
  * Build your app with EAS Build, and/or if you have Xcode installed and up to date on your machine and/or Android Studio, try prebuilding your app and running it: `npx expo prebuild --clean` and `npm run ios` and `npm run android`. Alternatively, try out `npx expo run`. Any new issues? [Please report them](https://github.com/expo/expo/issues/new?assignees=&amp;labels=needs+review&amp;template=bug_report.yml).
  * Did we miss updating the documentation somewhere? [Let us know](https://github.com/expo/expo/issues/new?assignees=&amp;labels=docs&amp;template=documentation.yml&amp;title=%5Bdocs%5D+).

### [How to report issues ](https://expo.dev/changelog/sdk-53-beta#how-to-report-issues)
  * [Create an issue](https://github.com/expo/expo/issues) and be sure to fill out the appropriate template (and include a [minimal reproducible example](https://stackoverflow.com/help/minimal-reproducible-example)).
  * Figuring out the underlying causes of issues is always super helpful, and it'll help expedite a solution.
  * Let us know that you are using the SDK 53 beta so we can prioritize the issue.
  * The most helpful beta testers will be listed in the final release notes (and possibly even provided with some [Discord](https://chat.expo.dev/) flair — you can [link your Discord and GitHub accounts to your Expo account](https://expo.dev/settings#connections)).


Thank you for helping us with testing the release — we look forward to shipping it soon! 🚀

