---
url: https://expo.dev/changelog/2023-12-12-sdk-50-beta
title: https://expo.dev/changelog/2023-12-12-sdk-50-beta
date: 2025-04-30T17:19:00.781439
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [Expo SDK 50 beta is now available](https://expo.dev/changelog/2023-12-12-sdk-50-beta)
Dec 12, 2023 by
Brent Vatne
**The SDK 50 beta period begins today and will last approximately one month.** The beta is an opportunity for developers to test out to SDK and ensure that the new release does not introduce any regressions for their particular systems and app configurations. We’re also [hosting office hours](https://us02web.zoom.us/meeting/register/tZcvceivqj0oHdGVOjEeKY0dRxCRPb0HzaAK) for those of you interested in helping test the release!
SDK 50 beta includes React Native 0.73. The full release notes for SDK 50 won’t be available until its generally available, but you can browse the changes in the [expo/expo CHANGELOG](https://github.com/expo/expo/blob/main/CHANGELOG.md) to learn more about the scope of the release and any breaking changes.
### [New features to try ](https://expo.dev/changelog/2023-12-12-sdk-50-beta#new-features-to-try)
  * **Expo Dev Tools Plugin API.** [First discussed in August 2023](https://expo.dev/changelog/2023/08-10-dev-tools-plugins), this API provides a foundation for library authors (and adventurous app developers) to build browser-based plugins to debug and interact with aspects of their library / app. To validate and demonstrate the API, we also built a few plugins for popular tools: Apollo Client, TanStack Query, TinyBase, and React Navigation — and you can find them in the [expo/dev-plugins repository](https://github.com/expo/dev-plugins).


This example app and the plugins used in it are available in: <https://github.com/expo/dev-plugins>
  * `expo-sqlite/next`: a complete re-write of our SQLite library, aimed to modernize the API and bring it towards parity with the mature equivalents that exist for web and Node.js. The API includes both **sync and async methods,** adds support for **prepared statements** , **update callbacks** , and the **Blob data type** , among other features! We’ve also updated the SQLite version to 3.42.0 on both platforms, rather than depending on the versions bundled with the operating system. This makes it possible to add support for SQLite extensions, such as [CR-SQLite](https://expo.dev/changelog/2023/08-10-cr-sqlite). We've also built a [Knex dialect for expo-sqlite](https://github.com/expo/knex-expo-sqlite-dialect), for folks who like using query builders. SQLite is already an important building block and we believe that it will become increasingly more essential as patterns like [local-first application architecture](https://www.youtube.com/watch?v=qHSI5rxTp_Q) continue to grow, and we’ll continue to invest in this library accordingly. [Learn more about the new API](https://docs.expo.dev/versions/unversioned/sdk/sqlite-next/).
  * `expo-camera/next`: accessing the device camera is a fundamental capability of many mobile apps, and we believe that this should be both simple to do and reliable. So, we’ve taken one of our older and most popular libraries and brought it up to date with native platform best practices. For most use cases, we expect `expo-camera/next` to fit like a glove. For more advanced use cases (such as [frame processors](https://react-native-vision-camera.com/docs/guides/frame-processors)), [react-native-vision-camera](https://react-native-vision-camera.com/) is a fantastic option. Documentation coming soon, for now you can [learn more about the new API in the type definition](https://github.com/expo/expo/blob/0519010004cba9093f1f07cc2eb884e2dc951afe/packages/expo-camera/src/next/Camera.types.ts).


Code
Copy
```

import{CameraView}from'expo-camera/next';
// Minimal example of using the new API, refer to types for more information on props
exportdefaultfunctionCamera(){
return(
<CameraView
   style={{ flex:1}}
/>
);

```

  * `@expo/fingerprint` **and integration into** `expo-github-action`: the `@expo/fingerprint` library is our answer to a common question for React Native developers: “ _how do I know if an app JavaScript bundle is compatible with a particular build of my app?_ ”. We do this by generating a fingerprint that represents the unique native characteristics of a project, and if that fingerprint changes, then JavaScript that targeted the older fingerprint may be incompatible. Try it out through the CLI: `npx @expo/fingerprint path/to/your/project` and [learn more in the README](https://github.com/expo/expo/blob/main/packages/%40expo/fingerprint/README.md), and in [the expo-github-actions README](https://github.com/expo/expo-github-action/tree/main/fingerprint). First class integration into EAS services will be coming in the future! [Learn more](https://github.com/expo/expo/blob/main/packages/%40expo/fingerprint/README.md#cli-usage).


After you generate a fingerprint, try changing your project in a way that impacts your native runtime and use the CLI to compare it to find what changed. [Learn more](https://github.com/expo/expo/blob/main/packages/%40expo/fingerprint/README.md#cli-usage).
  * **Expo Router v3 Release Candidate:** The next major release for universal file-based routing and advanced web support. Many bugfixes and stability improvements, better documentation, web support, testing, and types. Most notably, Expo Router v3 now has experimental support for building universal server endpoints with [API Routes](https://docs.expo.dev/router/reference/api-routes/). Learn more about the [Expo Router v3 beta](https://blog.expo.dev/expo-router-v3-beta-is-now-available-eab52baf1e3e).
  * `expo-font` **config plugin now supports natively adding fonts to your app** : it can be useful to load fonts at runtime with `Font.loadAsync` or `useFonts` to avoid rebuilding your app binary, but fonts in an app typically don’t change very much and so embedding the font into the native project with a config plugin can help you to clean up some of the async loading code from your app startup when you’re ready to do a build. [Learn more](https://docs.expo.dev/develop/user-interface/fonts/#use-a-custom-font).
  * `expo-secure-store` **gets a handful of new improvements**. By popular demand, we’ve introduced synchronous `getItem` and `setItem` functions! We’ve also unified the behavior as much as possible across Android and iOS — other than different types of exceptions resulting from different native implementations, all of the functions now behave the same. This introduces a small breaking change — when fetching a value which doesn’t exist in a keychain `expo-secure-store` will now always return `null`. Previously, Android would throw an exception and iOS would return `null`. [Learn more about other changes in the changelog](https://github.com/expo/expo/blob/main/CHANGELOG.md).
  * `expo-dev-client` **now defaults to loading the most recently opened project** when you boot up a development build. If the development server isn’t available, then it falls back to the launch screen. We’ve heard that this is what people typically want when they boot a development build, but if this isn’t your preference, then you can change this behavior with the config plugin:`"launchModeExperimental": "launcher”`. [Learn more](https://github.com/expo/expo/blob/25f1fd82b55f02f1774c056ba445bef30ecf8aa4/packages/expo-dev-launcher/plugin/src/pluginConfig.ts#L24-L39).
  * `expo-updates` **hook API**. We’ve included the new `useUpdates()` hook ([teased during the August launch week](https://expo.dev/changelog/2023/08-08-use-updates-api)) in the `expo-updates` package to make it easy to track state and interact with the updates API. This API should give you ergonomic access to anything you’d like to know about the state of updates in your project — see the [return type](https://docs.expo.dev/versions/unversioned/sdk/updates/#useupdatesreturntype) and the [`useUpdates()`](https://docs.expo.dev/versions/unversioned/sdk/updates/#useupdates) [docs](https://docs.expo.dev/versions/unversioned/sdk/updates/#useupdates) for more information.


Code
Copy
```

import{ useUpdates }from'expo-updates';
exportdefaultfunctionApp(){
const{
  currentlyRunning,
  availableUpdate,
  isUpdateAvailable,
  isUpdatePending,
// and so on!
}=useUpdates();
// etc..

```

  * **EAS Update rollbacks:** It is now possible to instruct your production apps to roll back to their embedded update the next time they check for updates. This helps in cases where you accidentally deployed a regression as a first update to a new build, and you want to revert to the embedded working state rather than trying to deploy an update fix on top. [Learn more](https://docs.expo.dev/eas-update/rollbacks/).
  * **EAS Update rollouts:** You can now gradually roll out updates to a percentage of your users, in order to minimize the risk of introducing bugs or other issues to your production environment. [Learn more](https://docs.expo.dev/eas-update/rollouts/).


[First announced during our summer launch week](https://expo.dev/changelog/2023/08-08-rollouts-eas-update), rollouts are now generally available for production use.
  * **Added** `npx expo run` **command.** Expo CLI will now prompt you to select a target platform if it’s not explicitly named in the command. This is a small quality of life improvement that aligns the `npx expo run` UX with that of `eas build:run`. You can also use `npx expo run android` or `npx expo run ios` as alternatives to `run:android` and `run:ios`.


Terminal
Copy
`- ``npx expo run`
`? Select the platform to run › - Use arrow-keys. Return to submit.``❯  Android``  iOS`
  * `npx expo install --fix` **now upgrades the** `expo` **package to the latest patch version.** We have found that developers often keep up to date with Expo SDK patch versions released through an SDK cycle by running `npx expo install --fix`, with the exception of the `expo` package, which was not automatically updated with this command. We encourage developers to stay up to date with our latest patches, and so we now also update the `expo` package with the `--fix` flag.
  * **Native project update tool now available.** If you use [CNG](https://docs.expo.dev/workflow/continuous-native-generation/), this doesn’t apply to you — although you may be curious to look at what is changing under the hood between releases. The [React Native Upgrade Helper](https://react-native-community.github.io/upgrade-helper/) is a great tool for developers that are building projects on top of the React Native Community CLI template, but the native projects in this template are quite different from projects that use Expo Modules. To make upgrading bare native projects with Expo Modules easier, we’ve built a similar tool to the community upgrade helper and it’s now part of our docs: see the “[Native project upgrade helper](https://docs.expo.dev/bare/upgrade/)”.


  * **Web bundle splitting with Metro, enabled by default.** Yes, bundle splitting, with Metro! More information coming soon, for now, [check out the related async routes documentation](https://docs.expo.dev/router/reference/async-routes/#static-rendering).
  * **Improved error messages and code removal.** Expo CLI now provides full stack traces for component-based errors, tree shakes all unused platform-specific code, and transforms faster when bundling for Hermes. Static website exports are now over 2x faster!
  * **The** `URL` **and** `URLSearchParams` **standards are built-in**. It was previously necessary to polyfill the web standard `URL` API (usually with the excellent [`react-native-url-polyfill`](https://www.npmjs.com/package/react-native-url-polyfill) library) in order to use many cross-platform libraries available on npm, where developers tend to assume that the `URL` API is available. We believe that `URL` is an important enough primitive that it deserves to be built in to the Expo core runtime, and so we now ship our own implementation in the `expo` package. [Learn more](https://docs.expo.dev/versions/unversioned/sdk/url/).
  * **Improved isolated modules support**. You can now use `pnpm` or `npm --install-mode=isolated` for local development builds. For other scenarios, we're working through a few remaining blocking issues and hope to have an update soon.
  * **React Native 0.73 (latest at the time of writing) and React 18.2.0 (unchanged from SDK 49).** There were many improvements in this release, refer to the [React Native CHANGELOG](https://github.com/facebook/react-native/blob/main/CHANGELOG.md), [Release Notes](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks), and [React CHANGELOG](https://github.com/facebook/react/blob/main/CHANGELOG.md) for a complete account.
  * **Preview available of the experimental React Native JS debugger UI.** We worked with Meta to unify the debugging experience in React Native as a whole, and the infrastructure that powers this new debugger UI is the same foundation as the [JS debugger built into Expo CLI](https://docs.expo.dev/debugging/tools/) . The approaches are slightly different, and we’ll talk about that more in the future. The upcoming React Native 0.73.1 release will also include connection stabilization fixes.


You can try this debugger by setting `EXPO_USE_UNSTABLE_DEBUGGER=1` when running `npx expo start` or `npx expo run`, and then launching the debugger from the CLI with j.
### [Other notable changes ](https://expo.dev/changelog/2023-12-12-sdk-50-beta#other-notable-changes)
  * **EAS Build default worker image now uses Xcode 15 for iOS and JDK 17 for Android.** [Learn more](https://docs.expo.dev/build-reference/infrastructure/).
  * `sentry-expo` **will be deprecated in favor of** **`@sentry/react-native`.** The `sentry-expo` package will continue to work in SDK 50, but it will be deprecated and we recommend moving to `@sentry/react-native`. This change allows us to deduplicate efforts and ensure a better, always up to date experience for folks that use Sentry in their projects. We’ll update this post with information about how to migrate soon.
  * `@expo/webpack-config` **is deprecated in favor of Expo CLI’s Metro web.** We’ll update the documentation throughout the SDK beta period. Learn more in [migrating from Expo Webpack.](https://docs.expo.dev/router/migrate/from-expo-webpack/)
  * **CSS is enabled by default with Metro web**. CSS is not supported on Android and iOS, but on web you can use all CSS features by importing CSS files. [Learn more](https://docs.expo.dev/versions/latest/config/metro/#css).
  * `tsconfigPaths` **is now enabled in** `@expo/metro-config` **by default:** this means that all you need to do to add path aliases is configure the `paths` property in your **tsconfig.json**. For example, `"@/*": ["src/*"]` will allow you to write code like `import Button from '@/components/Button';` anywhere in your codebase and have it resolve to the correct location within `src`. [Learn more](https://docs.expo.dev/guides/typescript/#path-aliases).
  * **Babel configuration changes in** `babel-preset-expo`: we made a variety of small quality of life improvements in our Babel preset: we removed transforms that aren’t necessary when targeting Hermes, we no longer alias `react-native-vector-icons` to `@expo/vector-icons` in the Babel preset (it’s now done in the Metro resolver instead), and we now add the Reanimated plugin by default when it’s installed (you don’t need to remove it from your **babel.config.js** , but you may want to).
  * **Bundler no longer started automatically when running the app from Xcode.** This aligns with the same change made in the React Native Community CLI template. Prior to running a build in Xcode (or afterwards, if you forget to do it before), run `npx expo start` to run the Expo dev server.
  * **Most** `expo-updates` JavaScript APIs are no longer available in Expo Go or development builds using `expo-dev-client`. The majority of the APIs exposed through the [`expo-updates`](https://docs.expo.dev/versions/latest/sdk/updates/) JavaScript interface (for example, `checkForUpdateAsync`, `fetchUpdateAsync`, etc.) are designed to be used in production builds. In development builds, Expo Go and `expo-dev-client` control how updates are loaded in those environments.
  * `npx expo prebuild` **no longer executes** **`[npm|yarn|pnpm|bun] install`****on each run by default.** If no changes are made to the dependencies in the **package.json** (default when using the standard template) then the Node module installation step will be skipped. The only changes outside of the native directories will likely only be the **package.json** scripts now.

### [Notable breaking changes ](https://expo.dev/changelog/2023-12-12-sdk-50-beta#notable-breaking-changes)
  * **Android SDK 34, AGP 8, and Java 17.** If you build your project locally, you will need to install JDK 17. [Learn more](https://docs.expo.dev/guides/local-app-development/#android).
  * **Android minimum supported version bumped to Android 6 (API 23).**
  * **iOS minimum deployment target bumped to 13.4**.
  * **Expo CLI and React Native now require Node 18+.** We also [bumped the default Node version on EAS Build to Node 18 on November 27th](https://expo.dev/changelog/2023/11-03-node-default).
  * **Classic updates is no longer supported.** As announced in February, 2023, projects using Expo SDK 50 do not support classic updates. We recommend [EAS Update](https://docs.expo.dev/eas-update/migrate-from-classic-updates/) instead. [Learn more](https://blog.expo.dev/sunsetting-expo-publish-and-classic-updates-6cb9cd295378).
  * **`@expo/vector-icons`****has been updated to use** **`react-native-vector-icons@10.0.0`**: this adds support for FontAwesome6 and also changes to Ionicons and MaterialIcons. Most notably, the`ios-` and `md-` prefixed icon names in Ionicons have now dropped those prefixes. If you use TypeScript, you will be warned about any icon names that have changed when you update. Otherwise, be sure to verify that your icons are correct.
  * React Native 0.73 changed from Java to Kotlin for Android `Main*` classes: **MainApplication.java** /**MainActivity.java** are now **MainApplication.kt** /**MainActivity.kt**. If you depend on any config plugins that use dangerous modifications to change these files, they may need to be updated for SDK 50 support.
  * The `ProgressBarAndroid` and `ProgressViewIOS` components from React Native have been removed in 0.73, after a long period of deprecation.
  * Refer to the [**Breaking Changes**](https://blog.expo.dev/expo-router-v3-beta-is-now-available-eab52baf1e3e) [section of the Expo Router v3 beta post](https://blog.expo.dev/expo-router-v3-beta-is-now-available-eab52baf1e3e) if you use it in your project.

### [Looking ahead to SDK 51 (Spring 2024): A single SDK version per release of the Expo Go app ](https://expo.dev/changelog/2023-12-12-sdk-50-beta#looking-ahead-to-sdk-51-spring-2024-a-single-sdk-version-per-release-of-the-expo-go-app)
For years, Expo Go has supported multiple SDK versions in a single installation of the app (for example, Expo Go for SDK 49 supports SDK 47, 48, and 49 projects). We even have a patent for this approach: [US Patent #11467854](https://patents.justia.com/patent/11467854): _“Method and apparatus for loading multiple differing versions of a native library into a native environment”_. As you might imagine, there is a fair amount of work that goes into this for each SDK release — I’d go as far as to say that this is the single most tedious and difficult part of the release process.
At a time when development with Expo tooling was largely focused around Expo Go, this made a lot of sense for us to invest in. Expo Go was a stepping stone for us in our journey to building [the Expo workflow as people know it today](https://docs.expo.dev/workflow/overview/). The Expo Go app will continue to be a great sandbox to get started quickly and experiment with ideas, but we encourage adopting [development builds](https://docs.expo.dev/workflow/overview/#development-builds) for a flexible and powerful development environment suitable for real-world applications at scale.
We expect that including a single version of the Expo SDK in Expo Go will not have a large impact on most developers using Expo tools: Expo CLI will continue to install the appropriate version of Expo Go for the SDK that your project uses to any connected Android device/emulator or iOS simulator.
Let us know what you think about this upcoming change, and if you have any concerns about it: **brent@expo.dev**.
### [Known issues ](https://expo.dev/changelog/2023-12-12-sdk-50-beta#known-issues)
  * Source maps aren’t working correctly in Expo Go for iOS.
  * “Open JS Debugger” in the dev menu in Expo Go doesn't currently launch the debugger.

### [Known regressions ](https://expo.dev/changelog/2023-12-12-sdk-50-beta#known-regressions)
  * Found an issue? [Report a regression](https://github.com/expo/expo/issues/new?assignees=&amp;labels=needs+review&amp;template=bug_report.yml).

### [How to try out the beta release ](https://expo.dev/changelog/2023-12-12-sdk-50-beta#how-to-try-out-the-beta-release)
  * **Initialize a new project with SDK 50 beta:**
    * **bun:** `bun create expo-app --template blank@beta`
    * **npm:** `npx create-expo-app --template blank@beta`
    * **yarn:** `yarn create expo-app --template blank@beta`
    * **Note:** `create-expo-app` will install dependencies with the package manager that you are using. For example, with npm when `npx` is used and yarn when `yarn create` used.
  * **Upgrade an existing project:**
    * Install the beta version of the Expo package: `npm install expo@next` or `yarn add expo@next`
    * Upgrade all dependencies to match SDK 50: `npx expo install --fix`
  * **Install the latest Expo Go for iOS to your physical device:**
    * Use this [TestFlight open beta link](https://testflight.apple.com/join/GZJxxfUU) and follow the instructions.
  * **Install the latest Expo Go for iOS simulators or Android emulators/physical devices:**
    * Launch your project through Expo CLI (press the `i` or `a` keyboard shortcut after running `npx expo start`) and the updated version of Expo Go will be automatically installed.
  * **SDK 50 beta is not yet available on Snack.**
  * [**Read the documentation**](https://docs.expo.dev/versions/v50.0.0) by selecting it from the version selector in the API reference section.

### [What to test ](https://expo.dev/changelog/2023-12-12-sdk-50-beta#what-to-test)
  * Upgrade your app with `npm install expo@next` or `yarn add expo@next`, then run `npx expo install --fix` and consult the [Native project upgrade helper](https://docs.expo.dev/bare/upgrade/) and [report any issues you encounter](https://github.com/expo/expo/issues/new?assignees=&amp;labels=needs+review&amp;template=bug_report.yml).
  * Build your app with EAS Build, and/or if you have Xcode installed and up to date on your machine and/or Android Studio, try prebuilding your app and running it: `npx expo prebuild --clean` and `npm run ios` and `npm run android`. Alternatively, try out `npx expo run`. Any new issues? [Please report them](https://github.com/expo/expo/issues/new?assignees=&amp;labels=needs+review&amp;template=bug_report.yml).
  * Did we miss updating the documentation somewhere? [Let us know](https://github.com/expo/expo/issues/new?assignees=&amp;labels=docs&amp;template=documentation.yml&amp;title=%5Bdocs%5D+).

### [How to report issues ](https://expo.dev/changelog/2023-12-12-sdk-50-beta#how-to-report-issues)
  * Create an issue on <https://github.com/expo/expo/issues> and be sure to fill out the appropriate template (and include a [minimal reproducible example](https://stackoverflow.com/help/minimal-reproducible-example), please!).
  * Figuring out the underlying causes of issues is super helpful.
  * Let us know that you are using the SDK 50 beta so we can prioritize the issue.
  * The most helpful beta testers will be listed in the final release notes (and possibly even provided with some [Discord](https://chat.expo.dev/) flair — you can [link your Discord and GitHub accounts to your Expo account](https://expo.dev/settings#connections)).


Thank you for helping us with testing the release — we look forward to shipping it soon! 🚀

