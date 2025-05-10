---
url: https://expo.dev/changelog/2024-01-18-sdk-50
title: https://expo.dev/changelog/2024-01-18-sdk-50
date: 2025-04-30T17:19:00.739551
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [Expo SDK 50](https://expo.dev/changelog/2024-01-18-sdk-50)
Jan 18, 2024 by
Brent Vatne
Today we're announcing the release of Expo SDK 50. SDK 50 includes React Native 0.73. Thank you to everyone who helped with beta testing.
## [Introducing Expo Dev Tools Plugins ](https://expo.dev/changelog/2024-01-18-sdk-50#introducing-expo-dev-tools-plugins)
This API provides a foundation for library authors (and adventurous app developers) to build browser-based plugins to debug and interact with aspects of their library / app. To validate and demonstrate the API, we also built a few plugins for popular tools: Apollo Client, TanStack Query, TinyBase, React Native Async Storage, and React Navigation — and you can find them in the [expo/dev-plugins repository](https://github.com/expo/dev-plugins). [Learn more](https://docs.expo.dev/debugging/devtools-plugins/).
This example app and the plugins used in it are available in: <https://github.com/expo/dev-plugins>
Thank you to everyone who provided feedback since our [proof of concept release in August](https://expo.dev/changelog/2023/08-10-dev-tools-plugins)!
## [New and improved SQLite and Camera APIs ](https://expo.dev/changelog/2024-01-18-sdk-50#new-and-improved-sqlite-and-camera-apis)
  * [`expo-sqlite/next`](https://docs.expo.dev/versions/v50.0.0/sdk/sqlite-next/): a complete re-write of [our SQLite library](https://docs.expo.dev/versions/latest/sdk/sqlite/), aimed to modernize the API and bring it towards parity with the mature equivalents that exist for web and Node.js. The API includes both **sync and async methods,** adds support for **prepared statements** , **update callbacks** , and the **Blob data type** , among other features! We've also updated the SQLite version to 3.42.0 on both platforms, rather than depending on the versions bundled with the operating system. This makes it possible to add support for SQLite extensions, such as [CR-SQLite](https://expo.dev/changelog/2023/08-10-cr-sqlite). We've also built a [Knex dialect for expo-sqlite](https://github.com/expo/knex-expo-sqlite-dialect), for folks who like using query builders. SQLite is already an important building block and we believe that it will become increasingly more essential as patterns like [local-first application architecture](https://www.youtube.com/watch?v=qHSI5rxTp_Q) continue to grow, and we'll continue to invest in this library accordingly. [Learn more about the new SQLite API](https://docs.expo.dev/versions/unversioned/sdk/sqlite-next/).
  * [`expo-camera/next`](https://docs.expo.dev/versions/v50.0.0/sdk/camera-next/): accessing the device camera is a fundamental capability of many mobile apps, and we believe that this should be both simple to do and reliable. So, we've taken one of our older and most popular libraries and brought it up to date with native platform best practices. For most use cases, we expect `expo-camera/next` to fit like a glove. For more advanced use cases (such as [frame processors](https://react-native-vision-camera.com/docs/guides/frame-processors)), [react-native-vision-camera](https://react-native-vision-camera.com/) is a fantastic option. [Learn more about the new Camera API](https://docs.expo.dev/versions/v50.0.0/sdk/camera-next/).


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

## [Introducing`@expo/fingerprint` ](https://expo.dev/changelog/2024-01-18-sdk-50#introducing)
This is our answer to a common question for React Native developers: “ _how do I know if an app JavaScript bundle is compatible with a particular build of my app?_ ”.
The [`@expo/fingerprint`](https://github.com/expo/expo/tree/main/packages/%40expo/fingerprint) CLI or API generates a fingerprint that represents the unique native characteristics of a project, and if that fingerprint changes, then you know that the JavaScript app that targeted the older fingerprint may be incompatible.
Try it out through the CLI: `npx @expo/fingerprint path/to/your/project` and [learn more in the README](https://github.com/expo/expo/blob/main/packages/%40expo/fingerprint/README.md), and in [the expo-github-actions README](https://github.com/expo/expo-github-action/tree/main/fingerprint). First class integration into EAS services will be coming in the future!
After you generate a fingerprint, try changing your project in a way that impacts your native runtime and use the CLI to compare it to find what changed. [Learn more](https://github.com/expo/expo/blob/main/packages/%40expo/fingerprint/README.md#cli-usage).
## [Expo Router v3 ](https://expo.dev/changelog/2024-01-18-sdk-50#expo-router-v3)
This is the next major release for universal file-based routing and advanced web support. Expo Router v3 includes many bugfixes and stability improvements, better documentation, web support, testing, and types. Most notably, Expo Router v3 now has experimental support for building universal server endpoints with [API Routes](https://docs.expo.dev/router/reference/api-routes/). [Learn more in "Expo Router v3: API Routes, bundle splitting, speed improvements, and more"](https://expo.dev/changelog/2024/01-23-router-3).
## [EAS Build ](https://expo.dev/changelog/2024-01-18-sdk-50#eas-build)
We continuously deploy improvements to [EAS Build](https://docs.expo.dev/build/introduction/). Here are some of the highlights since the last SDK release:
  * **Xcode 15.2 is now the default for macOS workers**. [Learn more](https://expo.dev/changelog/2024/01-18-eas-build-xcode-15.2-image).
  * **JDK 17 and Ubuntu 20 are now the default for Linux workers**. [Learn more](https://docs.expo.dev/build-reference/infrastructure/).
  * **Node 18 is now the default**. The default Node version on EAS Build tracks the current maintenance LTS, and on November 27th, 2023 we changed the default version from Node 16 to 18. [Learn more](https://expo.dev/changelog/2023/11-03-node-default).
  * **Improved warnings and errors**. "Build annotations" can make you feel like you have an experienced engineer looking over your shoulder to help you understand why you are seeing particular warnings and errors in your build, and what to do about them. [Learn more](https://expo.dev/changelog/2023/12-01-build-annotations).
  * **Pre-warmed CocoaPods cache for faster builds**. All of your iOS builds will be a bit faster, without any changes needed on your end. [Learn more](https://expo.dev/changelog/2023/12-07-cocoapods-cache).
  * **Expo Orbit v1 released** : Orbit for macOS makes it faster and easier to install and run builds from EAS. [Learn more](https://expo.dev/changelog/2023/11-14-orbit-v1).
  * ...we also [added support for Bun](https://expo.dev/changelog/2023/09-25-eas-bun-support), EAS CLI will now read **.nvmrc** files to set your Node version for your builds (unless explicitly specified in your build profile), `eas build:run` now accepts the `--profile` flag to filter builds, we added the `eas build:delete` command by request to support certain automation workflows, and we have continued improving the [fully customizable builds preview](https://expo.dev/changelog/2023/08-10-custom-builds) which we hope to make GA in the coming months.

## [EAS Update ](https://expo.dev/changelog/2024-01-18-sdk-50#eas-update)
  * **New, easy to use JavaScript API** : we now include the new `useUpdates()` hook ([teased during the August launch week](https://expo.dev/changelog/2023/08-08-use-updates-api)) in the `expo-updates` package to make it easy to track state and interact with the updates API. This API should give you ergonomic access to anything you'd like to know about the state of updates in your project — see the [return type](https://docs.expo.dev/versions/v50.0.0/sdk/updates/#useupdatesreturntype), the [`useUpdates()`](https://docs.expo.dev/versions/v50.0.0/sdk/updates/#useupdates) [docs](https://docs.expo.dev/versions/v50.0.0/sdk/updates/#useupdates), and the [expo/UpdatesAPIDemo repository](https://github.com/expo/UpdatesAPIDemo) for more information.


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

  * **New dashboard UI features:** Recently we released some updates to the dashboard that allow you to: create new channels, remove them, republish updates, and remove them. [Learn more](https://expo.dev/changelog/2023/12-13-eas-update-ui)
  * **Rollbacks:** It is now possible to instruct your production apps to roll back to their embedded update (the JavaScript app generated at build time) the next time they check for updates. This helps in cases where you accidentally deployed a regression as a first update to a new build, and you want to revert to the embedded working state rather than trying to deploy an update fix on top. [Learn more](https://docs.expo.dev/eas-update/rollbacks/).
  * **Rollouts:** You can now gradually roll out updates to a percentage of your users, in order to minimize the impact of accidentally introducing a bug to your production environment. [Learn more](https://docs.expo.dev/eas-update/rollouts/).


[See the announcement](https://expo.dev/changelog/2023/08-08-rollouts-eas-update).
## [Basic Expo Modules support for tvOS and macOS ](https://expo.dev/changelog/2024-01-18-sdk-50#basic-expo-modules-support-for-tvos-and-macos)
You can now use the [Expo Modules API](https://docs.expo.dev/modules/overview/) to build native modules for [tvOS](https://github.com/react-native-tvos/react-native-tvos) and [macOS](https://github.com/microsoft/react-native-macos).
  * The `use_expo_modules!` method that autolinks Expo modules can now be used on `tvOS` and `macOS` targets in the **Podfile**. It automatically installs only these modules that [declare support for the target platform in their podspec](https://github.com/expo/expo/blob/2dc48d7130d14d475c8aa79be22bf83c2593a385/packages/expo-image/ios/ExpoImage.podspec#L13).
  * The packages supporting tvOS platform in SDK 50: `expo-application`, `expo-av`, `expo-constants`, `expo-device`, `expo-file-system`, `expo-font`, `expo-image`, `expo-keep-awake`, `expo-localization`, `expo-splash-screen`, `expo-updates`, `@expo/cli`. [Learn more in the "Build Expo apps for TV" guide](https://docs.expo.dev/guides/building-for-tv), and [let us know](https://x.com/expo) which packages you are most interested in seeing supported in the future!
  * The packages supporting macOS platform in SDK 50: `expo-constants`, `expo-file-system`, `expo-keep-awake` (no-op). More packages will be adapted after the SDK release, and we'll also add support for `@expo/cli` so that you can use `npx expo start` to run your dev server. [Let us know](https://x.com/tsapeta) which packages you are most interested in!


Refer to the [PR that installs Expo modules in Expo Orbit](https://github.com/expo/orbit/pull/130) and the [PR that migrates one of its native modules to Expo Modules API](https://github.com/expo/orbit/pull/132) for examples. Documentation will be coming soon.
## [First-class Expo support in Sentry ](https://expo.dev/changelog/2024-01-18-sdk-50#first-class-expo-support-in-sentry)
`sentry-expo` has been merged into [`@sentry/react-native@5.16.0`](https://github.com/getsentry/sentry-react-native/releases/tag/5.16.0), and `sentry-expo` is now deprecated. The `sentry-expo` package will continue to work in SDK 50, but we recommend moving to `@sentry/react-native`. This change allows us to deduplicate efforts and ensure a better, always up to date experience for folks that use Sentry in their projects. A big thank you goes out to [Krystof Woldrich](https://github.com/krystofwoldrich) from Sentry for his work on this!
While collaborating on this work, one of our goals was to improve the integration between Sentry and [EAS Update](https://docs.expo.dev/eas-update/introduction/). It is now as easy as `eas update --branch <branch> && npx sentry-expo-upload-sourcemaps dist` to publish an update and upload the corresponding sourcemaps.
  * [Learn how to migrate from](https://expo.fyi/sentry-expo-migration) [`sentry-expo`](https://expo.fyi/sentry-expo-migration) [to](https://expo.fyi/sentry-expo-migration) [`@sentry/react-native`](https://expo.fyi/sentry-expo-migration).
  * [Read the "Use Sentry" guide on the Expo documentation](https://docs.expo.dev/guides/using-sentry/).
  * [Read Sentry's documentation](https://docs.sentry.io/platforms/react-native/manual-setup/expo/).

## [Other Highlights ](https://expo.dev/changelog/2024-01-18-sdk-50#other-highlights)
  * **React Native 0.73 (latest at the time of writing) and React 18.2.0 (unchanged from SDK 49).** There were many improvements in this release, refer to the [React Native CHANGELOG](https://github.com/facebook/react-native/blob/main/CHANGELOG.md), [Release Notes](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks), and [React CHANGELOG](https://github.com/facebook/react/blob/main/CHANGELOG.md) for a complete account.
  * `expo-font` **config plugin now supports natively adding fonts to your app**. It can be useful to load fonts at runtime with `Font.loadAsync` or `useFonts` to avoid rebuilding your app binary, but fonts in an app typically don't change very much and so embedding the font into the native project with a config plugin can help you to clean up some of the async loading code from your app startup when you're ready to do a build. [Learn more](https://docs.expo.dev/develop/user-interface/fonts/#use-a-custom-font).
  * `expo-secure-store` **gets a handful of new improvements**. By popular demand, we've introduced synchronous `getItem` and `setItem` functions! We've also unified the behavior as much as possible across Android and iOS — other than different types of exceptions resulting from different native implementations, all of the functions now behave the same. This introduces a small breaking change — when fetching a value which doesn't exist in a keychain `expo-secure-store` will now always return `null`. Previously, Android would throw an exception and iOS would return `null`. [Learn more about other changes in the changelog](https://github.com/expo/expo/blob/main/CHANGELOG.md).
  * `expo-dev-client` **now defaults to loading the most recently opened project** when you boot up a development build. If the development server isn't available, then it falls back to the launch screen. We've heard that this is what people typically want when they boot a development build, but if this isn't your preference, then you can change this behavior with the config plugin:`"launchModeExperimental": "launcher”`. [Learn more](https://github.com/expo/expo/blob/25f1fd82b55f02f1774c056ba445bef30ecf8aa4/packages/expo-dev-launcher/plugin/src/pluginConfig.ts#L24-L39).
  * **Added** `npx expo run` **command.** Expo CLI will now prompt you to select a target platform if it's not explicitly named in the command. This is a small quality of life improvement that aligns the `npx expo run` UX with that of `eas build:run`. You can also use `npx expo run android` or `npx expo run ios` as alternatives to `run:android` and `run:ios`.


Terminal
Copy
`- npx expo run``? Select the platform to run › - Use arrow-keys. Return to submit.``❯  Android``  iOS`
  * `npx expo install --fix` **now upgrades the** `expo` **package to the latest patch version.** We have found that developers often keep up to date with Expo SDK patch versions released through an SDK cycle by running `npx expo install --fix`, with the exception of the `expo` package, which was not automatically updated with this command. We encourage developers to stay up to date with our latest patches, and so, after the initial upgrade to SDK 50, the `--fix` flag will update all of your Expo SDK packages, including the `expo` package.
  * **Native project update tool now available.** If you use [CNG](https://docs.expo.dev/workflow/continuous-native-generation/), this doesn't apply to you — although you may be curious to look at what is changing under the hood between releases. The [React Native Upgrade Helper](https://react-native-community.github.io/upgrade-helper/) is a great tool for developers that are building projects on top of the React Native Community CLI template, but there are some differences in native projects that use this template as compared to projects that use Expo Modules. To make upgrading bare native projects with Expo Modules easier, we've built a similar tool to the community upgrade helper and it's now part of our docs: see the “[Native project upgrade helper](https://docs.expo.dev/bare/upgrade/)”.


  * **Web bundle splitting with Metro, enabled by default.** Yes, bundle splitting, with Metro! More information coming soon, for now, [check out the related async routes documentation](https://docs.expo.dev/router/reference/async-routes/#static-rendering).
  * **Improved error messages and code removal.** Expo CLI now provides full stack traces for component-based errors, tree shakes all unused platform-specific code, and transforms faster when bundling for Hermes. Static website exports are now over 2x faster!
  * **The** `URL` **and** `URLSearchParams` **standards are built-in**. It was previously necessary to polyfill the web standard `URL` API (usually with the excellent [`react-native-url-polyfill`](https://www.npmjs.com/package/react-native-url-polyfill) library) in order to use many cross-platform libraries available on npm, where developers tend to assume that the `URL` API is available. We believe that `URL` is an important enough primitive that it deserves to be built in to the Expo core runtime, and so we now ship our own implementation in the `expo` package. [Learn more](https://docs.expo.dev/versions/unversioned/sdk/url/).
  * **Improved isolated modules support**. You can now use `pnpm` or `npm --install-mode=isolated` for local development builds. For other scenarios, we're working through a few remaining blocking issues and hope to have an update soon.
  * **Preview available of the experimental React Native JS debugger UI.** We worked with Meta to unify the debugging experience in React Native as a whole, and the infrastructure that powers this new debugger UI is the same foundation as the [JS debugger built into Expo CLI](https://docs.expo.dev/debugging/tools/). The approaches are slightly different, and we'll talk about that more in the future.


  * `@expo/webpack-config` **is deprecated in favor of Expo CLI's Metro web.** This means it that Webpack support will continue to work in SDK 50, but it will not be actively developed, and it will be removed in a future release. Read the ["Webpack support in Expo CLI is now deprecated" blog](https://blog.expo.dev/webpack-support-in-expo-cli-is-now-deprecated-e9831d7eb631) for the full story, and [learn about migrating away from Webpack to Metro](https://docs.expo.dev/router/migrate/from-expo-webpack/).
  * **CSS is enabled by default with Metro web**. CSS is not supported on Android and iOS, but on web you can use all CSS features by importing CSS files. [Learn more](https://docs.expo.dev/versions/latest/config/metro/#css).
  * `tsconfigPaths` **is now enabled in** `@expo/metro-config` **by default:** this means that all you need to do to add path aliases is configure the `paths` property in your **tsconfig.json**. For example, `"@/*": ["src/*"]` will allow you to write code like `import Button from '@/components/Button';` anywhere in your codebase and have it resolve to the correct location within `src`. [Learn more](https://docs.expo.dev/guides/typescript/#path-aliases).
  * **Babel configuration changes in** `babel-preset-expo`: we made a variety of small quality of life improvements in our Babel preset: we removed transforms that aren't necessary when targeting Hermes, we no longer alias `react-native-vector-icons` to `@expo/vector-icons` in the Babel preset (it's now done in the Metro resolver instead), and we now add the [Reanimated](https://docs.swmansion.com/react-native-reanimated/) plugin by default when it's installed (you don't need to remove it from your **babel.config.js** , but you may want to).
  * **Bundler no longer starts automatically when running the app from Xcode.** This aligns with the same change made in the React Native Community CLI template. Prior to running a build in Xcode (or afterwards, if you forget to do it before), run `npx expo start` to run the Expo dev server.


`npx expo prebuild` **no longer executes** **`[npm|yarn|pnpm|bun] install`****on each run by default.** If no changes are made to the dependencies in the **package.json** (default when using the standard template) then the Node module installation step will be skipped. The only changes outside of the native directories will likely be the **package.json** scripts now.
## [Notable breaking changes ](https://expo.dev/changelog/2024-01-18-sdk-50#notable-breaking-changes)
  * **Android SDK 34, AGP 8, and Java 17.** If you build your project locally, you will need to install JDK 17. [Learn more](https://docs.expo.dev/guides/local-app-development/#android).
  * **Android minimum supported version bumped to Android 6 (API 23).**
  * **iOS minimum deployment target bumped to 13.4**.
  * **Expo CLI and React Native now require Node 18+.** We also [bumped the default Node version on EAS Build to Node 18 on November 27th](https://expo.dev/changelog/2023/11-03-node-default).
  * **Classic updates is no longer supported.** As announced in February, 2023, projects using Expo SDK 50 do not support classic updates. We recommend [EAS Update](https://docs.expo.dev/eas-update/migrate-from-classic-updates/) instead. [Learn more](https://blog.expo.dev/sunsetting-expo-publish-and-classic-updates-6cb9cd295378).
  * **`@expo/vector-icons`****has been updated to use** **`react-native-vector-icons@10.0.0`**: this adds support for FontAwesome6 and also changes to Ionicons and MaterialIcons. Most notably, the`ios-` and `md-` prefixed icon names in Ionicons have now dropped those prefixes. If you use TypeScript, you will be warned about any icon names that have changed when you update. Otherwise, be sure to verify that your icons are correct.
  * Most `expo-updates` JavaScript APIs are no longer available in Expo Go or development builds using `expo-dev-client`. The majority of the APIs exposed through the [`expo-updates`](https://docs.expo.dev/versions/latest/sdk/updates/) JavaScript interface (for example, `checkForUpdateAsync`, `fetchUpdateAsync`, etc.) are designed to be used in production builds. In development builds, Expo Go and `expo-dev-client` control how updates are loaded in those environments.
  * React Native 0.73 changed from Java to Kotlin for Android `Main*` classes: **MainApplication.java** /**MainActivity.java** are now **MainApplication.kt** /**MainActivity.kt**. If you depend on any config plugins that use dangerous modifications to change these files, they may need to be updated for SDK 50 support.
  * The `ProgressBarAndroid` and `ProgressViewIOS` components from React Native have been removed in 0.73, after a long period of deprecation.
  * Refer to the [**Breaking Changes**](https://expo.dev/changelog/2024/01-23-router-3) [section of the Expo Router v3 post](https://expo.dev/changelog/2024/01-23-router-3) if you use it in your project.

## [🧹 Expo Go: Dropped SDK 47 and 48 ](https://expo.dev/changelog/2024-01-18-sdk-50#-expo-go-dropped-sdk-47-and-48)
We routinely drop SDK versions that have low usage in order to reduce the number of versions we need to support in Expo Go. This means that SDK 47 and 48 projects will no longer work within the latest version of Expo Go — and they will continue to work as expected otherwise. You can install older versions of Expo Go for Android device/emulators or iOS simulators, [learn more](https://docs.expo.dev/get-started/expo-go/#sdk-versions).
### [A single SDK version per release of the Expo Go app: looking ahead to SDK 51 ](https://expo.dev/changelog/2024-01-18-sdk-50#a-single-sdk-version-per-release-of-the-expo-go-app-looking-ahead-to-sdk-51)
For years, Expo Go has supported multiple SDK versions in a single installation of the app (for example, Expo Go for SDK 49 supports SDK 47, 48, and 49 projects). We even have a patent for this approach: [US Patent #11467854](https://patents.justia.com/patent/11467854): _“Method and apparatus for loading multiple differing versions of a native library into a native environment”_. As you might imagine, there is a fair amount of work that goes into this for each SDK release — I'd go as far as to say that this is the single most tedious and difficult part of the release process.
At a time when development with Expo tooling was largely focused around Expo Go, this made a lot of sense for us to invest in. Expo Go was a stepping stone for us in our journey to building [the Expo workflow as people know it today](https://docs.expo.dev/workflow/overview/). The Expo Go app will continue to be a great sandbox to get started quickly and experiment with ideas, but we encourage adopting [development builds](https://docs.expo.dev/workflow/overview/#development-builds) for a flexible and powerful development environment suitable for real-world applications at scale.
We expect that including a single version of the Expo SDK in Expo Go will not have a large impact on most developers using Expo tools: Expo CLI will continue to install the appropriate version of Expo Go for the SDK that your project uses to any connected Android device/emulator or iOS simulator.
Let us know what you think about this upcoming change, and if you have any concerns about it: **brent@expo.dev**.
## [Known issues ](https://expo.dev/changelog/2024-01-18-sdk-50#known-issues)
  * [Snack](https://snack.expo.dev/) support for SDK 50 is not yet available, it will be coming soon.
  * Expo Go for iOS: source maps aren't working correctly in this context, and [the JavaScript debugger doesn't connect](https://github.com/expo/expo/issues/26044#issuecomment-1879722559). These issues are not present in development builds.
  * Found an issue? [Report a regression](https://github.com/expo/expo/issues/new?assignees=&amp;labels=needs+review&amp;template=bug_report.yml).

## [➡️ Upgrading your app ](https://expo.dev/changelog/2024-01-18-sdk-50)
Here's how to upgrade your app to Expo SDK 50 from 49:
  * **Update to the latest version of EAS CLI** (if you use it):


Terminal
Copy
`npm i -g eas-cli`
  * **Install the new version of the Expo package** :


Terminal
Copy
`npm install expo@^50.0.0`
  * **Upgrade all dependencies to match SDK 50** :


Terminal
Copy
`npx expo install --fix`
  * **If you have any** **`resolutions`/`overrides`** **in your package.json, verify that they are still needed.** For example, you should remove `metro` and `metro-resolver` overrides if you added them for `expo-router` in a previous SDK release.
  * **Check for any possible known issues** :


Terminal
Copy
`npx expo-doctor@latest`
  * **Refer to the "Deprecations, renamings, and removals" section** above for breaking changes that are most likely to impact your app.
  * **Make sure to check the** [**changelog**](https://github.com/expo/expo/blob/main/CHANGELOG.md) **for all other breaking changes!**
  * **Upgrade Xcode if needed** : Xcode 15 is needed to compile the native iOS project. We recommend Xcode 15.2 for SDK 50. For EAS Build, projects without any specified `image` will default to Xcode 15.2.
  * **If you use Expo Router** : refer to the [breaking changes in v3](https://blog.expo.dev/expo-router-v3-beta-is-now-available-eab52baf1e3e#aed2) and update your app accordingly.
  * **If you don't use** [**Continuous Native Generation**](https://docs.expo.dev/workflow/continuous-native-generation/):
    * Run `npx pod-install` if you have an `ios` directory.
    * Apply any relevant changes from the [Native project upgrade helper](https://docs.expo.dev/bare/upgrade/).
    * Alternatively, you could consider [adopting prebuild](https://docs.expo.dev/guides/adopting-prebuild/) for easier upgrades in the future.
  * **If you maintain any Expo Modules** :
    * For Android: update your library **build.gradle** to match the changes in [this diff](https://gist.github.com/brentvatne/61cd1a938fb4ba8869bc490647aa52e8). You may also now remove the JVM target version configuration, [as explained in this FYI page](https://expo.fyi/expo-modules-gradle8-migration#error-task-current-target-is-17-and-compilereleasekotlin-task-current-target-is-11-jvm-target-compatibility-should-be-set-to-the-same-java-version).
    * For iOS: update the platform deployment target field from `'13.0'` to `'13.4'`, matching the changes in [this diff](https://gist.github.com/brentvatne/87ac1b2c402be415972231a73ba3a695).
  * **If you maintain any config plugins** :
    * Note that **MainActivity.java** and **MainApplication.java** were migrated to Kotlin. If you use any config plugins that modify these files, they may need to be updated for SDK 50 support (for example, [this config plugin](https://github.com/morrowdigital/watermelondb-expo-plugin/blob/b5d5802e0490e79219253073e5cb5574dc8b730c/src/withWatermelon.ts#L20-L43)).
  * **If you use Expo Go** : Update the Expo Go app on your phones from app stores. Expo CLI will automatically update your apps in simulators. You can also download the iOS simulator build or the APK from [expo.dev/tools](https://expo.dev/tools).
  * **If you use** [**development builds with expo-dev-client**](https://docs.expo.dev/development/introduction/): Create a new development build after upgrading.
  * **Questions?** We'll be hosting an SDK 50 launch live-stream on January 31st, [join us on YouTube](https://www.youtube.com/watch?v=cKFSVUo3AnI).

## [Thanks to everyone who contributed to the release! ](https://expo.dev/changelog/2024-01-18-sdk-50#thanks-to-everyone-who-contributed-to-the-release)
**The team:** [everyone](https://expo.dev/about) contributed one way or another, with special mentions to the engineers most directly involved in this release: [Łukasz Kosmaty](https://github.com/lukmccall), [Kudo Chien](https://github.com/kudo), and [Tomasz Sapeta](https://github.com/tsapeta) for leading all SDK work. Also, [Alan Hughes](https://github.com/alanjhughes), [Aleksander Mikucki](https://github.com/aleqsio), [Gabriel Donadel](https://twitter.com/donadeldev), [Aman Mittal](https://github.com/amandeepmittal), [Bartosz Kaszubowski](https://github.com/Simek), [Cedric van Putten](https://github.com/bycedric), [Doug Lowder](https://github.com/douglowder), [Evan Bacon](https://github.com/EvanBacon), [Keith Kurak](https://github.com/keith-kurak), [Kim Brandwijk](https://github.com/kbrandwijk), [Quin Jung](https://github.com/quinlanj), [Will Schurman](https://github.com/wschurman), [Wojciech Dróżdż](https://github.com/behenate), and [Mark Lawlor](https://github.com/marklawlor). Welcome to the team, [Kadi Kraman](https://github.com/kadikraman) and [Phil Pluckthun](https://github.com/kitten)!
**External contributors:** [Adnan Karšić](https://github.com/adokce), [Ahmed Ali](https://github.com/ahmedali5530), [Alexander Pataridze](https://github.com/alexandrius), [Alfonso Curbelo](https://github.com/alfonsocj), [Ammar](https://github.com/ammar-madni), [Amr Hassaballah](https://github.com/amrhassab), [Andrew Enyeart](https://github.com/aenyeart), [Andrew X. Shah](https://github.com/drewxs), [Andy Matuschak](https://github.com/andymatuschak), [Anthony Mittaz](https://github.com/sync), [Antonio Dal Sie](https://github.com/exodusanto), [Archimedes Trajano](https://github.com/trajano), [Avi Avinav](https://github.com/AviAvinav), [Ayrton-Taede Tromp](https://github.com/BeBoRE), [Bartosz Boruta](https://github.com/bartoszboruta), [Ben](https://github.com/bensaine), [Ben Limmer](https://github.com/blimmer), [Benny Neugebauer](https://github.com/bennycode), [Brad Cooley](https://github.com/Bradley-Cooley), [Brad Jones](https://github.com/bradjones1), [Brandon Austin](https://github.com/branaust), [Brian Sharon](https://github.com/floatplane), [Chee Kit](https://github.com/thespacemanatee), [Cho Chi Him](https://github.com/chochihim), [Claude](https://github.com/claudesortwell), [Colin McDonnell](https://github.com/colinhacks), [Craig Malton](https://github.com/notlamc), [César Guadarrama](https://github.com/cesargdm), [Daniel](https://github.com/donni106), [Daniel Friyia](https://github.com/friyiajr), [Daniel Reichhart](https://github.com/reichhartd), [David Leuliette](https://github.com/flexbox), [Debabrata Batabyal](https://github.com/Kite2002), [Derek W. Stavis](https://github.com/derekstavis), [Felix Schindler](https://github.com/fschindler), [Francis](https://github.com/francisleigh), [Frank Calise](https://github.com/frankcalise), [Frederick Ros](https://github.com/sleeper), [Gabriel Porto](https://github.com/gsporto), [Gavin](https://github.com/gkasdorf), [Gennadiy](https://github.com/GennadiyK), [Greg Westneat](https://github.com/leggomuhgreggo), [Guilherme Oenning](https://github.com/goenning), [Göksenin Güngör](https://github.com/dopplerDistortion), [Hirbod](https://github.com/hirbod), [Ian Felix](https://github.com/ianfelix), [Ian Martorell](https://github.com/ianmartorell), [Igor Adrov](https://github.com/nucleartux), [Isaac Way](https://github.com/iway1), [J. Lewis](https://github.com/lewxdev), [Jabed Zaman](https://github.com/jabedzaman), [Jacob Marshall](https://github.com/jacobhq), [James Edmonston](https://github.com/jamesedmonston), [Janic Duplessis](https://github.com/janicduplessis), [Joel](https://github.com/jgarplind), [Johan Holm](https://github.com/johanholm), [Jonatan E. Salas](https://github.com/JonatanSalas), [Jonathan Ehwald](https://github.com/DoctorJohn), [Joon Shakya](https://github.com/joonshakya), [Josh Kramer](https://github.com/jkjustjoshing), [Joshua Joseph Myers](https://github.com/JoshBot-Debug), [Jun Matsushita](https://github.com/jmatsushita), [Justin Kaufman](https://github.com/jkaufman), [Justin Parker](https://github.com/jparkrr), [KIM WOORAM](https://github.com/nararalab), [Kacper Kapuściak](https://github.com/kacperkapusciak), [Kelvin Choi](https://github.com/tszheichoi), [Kesha Antonov](https://github.com/kesha-antonov), [Krzysztof Piaskowy](https://github.com/piaskowyk), [Liam Jones](https://github.com/liamjones), [Linus Unnebäck](https://github.com/LinusU), [Logan Rosen](https://github.com/loganrosen), [Lucas Fronza](https://github.com/lucasfronza), [Luiz Henrique Souza](https://github.com/souzaluiz), [M.H.Pousti](https://github.com/Mhp23), [Marek Lewandowski](https://github.com/mlewand), [Marius](https://github.com/MariuzM), [Marius Gaciu](https://github.com/mariusgaciu), [Mateus Craveiro](https://github.com/mccraveiro), [Matin Zadeh Dolatabad](https://github.com/matinzd), [Matt Polky](https://github.com/mdpolky), [Mehrdad Moradi](https://github.com/thegreatzeus), [Michael Hueter](https://github.com/hueter), [Mo Javad](https://github.com/mojavad), [Mohit Yadav](https://github.com/Just-Moh-it), [Mustafa Shabib](https://github.com/mustafashabib), [Nelson Sousa](https://github.com/nelsonprsousa), [Nikhil](https://github.com/qwertynik), [Niklas Haug](https://github.com/niklashaug), [Omer Sabah](https://github.com/Omerrj), [Ossi Siipola](https://github.com/Hiipivahalko), [Pavlo Hromov](https://github.com/hromovp), [Peter Ferguson](https://github.com/peterferguson), [Peter Hasza](https://github.com/phasza), [Peter Hägg](https://github.com/pehagg), [Pierre Zimmermann](https://github.com/pierrezimmermannbam), [Pieter De Baets](https://github.com/javache), [Piotr Szeremeta](https://github.com/khamilowicz), [Pranjal soni](https://github.com/sonipranjal), [RRaideRR](https://github.com/RRaideRR), [Randall71](https://github.com/Randall71), [Robert](https://github.com/robertn702), [Robert Trevethan](https://github.com/mmmguitar), [Rodolfo](https://github.com/RodolfoGS), [Rohit Kumar Saini](https://github.com/rockingrohit9639), [Rui Ying](https://github.com/robertying), [Sebastian Biallas](https://github.com/sebastianbiallas), [Sergey Pashkevich](https://github.com/siarheipashkevich), [Siarhei Haikou](https://github.com/haikov), [Simen Bekkhus](https://github.com/SimenB), [Spencer Chang](https://github.com/spencerc99), [Suvin Nimnaka](https://github.com/Suvink), [TJ Couch](https://github.com/tjcouch1), [Tag Howard](https://github.com/jthoward64), [Tarun Chauhan](https://github.com/tarunrajput), [Thomas Mollard](https://github.com/Thomas-Mollard), [Thor 雷神 Schaeff](https://github.com/thorwebdev), [Tim Etler](https://github.com/etler), [Tomas Ravinskas](https://github.com/OzymandiasTheGreat), [Tomek Zawadzki](https://github.com/tomekzaw), [Trivikram Kamat](https://github.com/trivikr), [Valentin Vetter](https://github.com/BeLi4L), [Vojtech Novak](https://github.com/vonovak), [Wanderson Alves](https://github.com/wandersonalwes), [Weykon](https://github.com/weykon), [William](https://github.com/darnfish), [Youssouf EL AZIZI](https://github.com/yjose), [Zach Nugent](https://github.com/mrzachnugent), [Zayyan Faizal](https://github.com/zfaizal2), [bja34](https://github.com/bja34), [ebrahimhassan121](https://github.com/ebrahimhassan121), [italocoura87](https://github.com/italocoura87), [jingpeng](https://github.com/jingpeng), [jleprinc](https://github.com/jleprinc), [kapobajza](https://github.com/kapobajza), [la55u](https://github.com/la55u), [noman](https://github.com/noman-land), [owen-duncan-snobel](https://github.com/owen-duncan-snobel), [rieg-ec](https://github.com/rieg-ec), [safesecurely](https://github.com/safesecurely), and [sak2](https://github.com/sak2).
**Beta testers:** [Gamote](https://github.com/Gamote), [Alex Fournier](https://github.com/alex-fournier), [Justin Parker](https://github.com/jparkrr), [SmashBoy](https://github.com/smashboy), [Justin](https://github.com/juskek), [Valerii Smirnov](https://github.com/XantreGodlike), [Rodrigo Figueroa](https://github.com/bidah), [Dimo Portenko](https://github.com/dimaportenko), [Matthieu Gicquel](https://github.com/matthieugicquel), [Muhammad Usman](https://github.com/uxxman), [Achmad Kurnianto](https://github.com/achmadk), [Liam Malloy](https://github.com/palmerhyde), [Rifaldhi AW](https://github.com/rifaldhiaw), [Kief](https://github.com/Kief5555), [Tomasz Żelawski](https://github.com/tjzel), [Mo Javad](https://github.com/mojavad), [Peter Ferguson](https://github.com/peterferguson), [Shannon](https://github.com/revolution42), [evelant](https://github.com/evelant), [Alexander Nanberg](https://github.com/alexandernanberg), [Andrzej Hanusek](https://github.com/ahanusek), [Sergei Vronskii](https://github.com/SVronskiy), [Chanphirom Sok](https://github.com/chanphiromsok), [Kenneth Stark](https://github.com/kennethstarkrl), [Tony Chen](https://github.com/zhiqingchen), [Benjamin Komen](https://github.com/benjaminkomen), and [Chris Zubak-Skees](https://github.com/chriszs).

