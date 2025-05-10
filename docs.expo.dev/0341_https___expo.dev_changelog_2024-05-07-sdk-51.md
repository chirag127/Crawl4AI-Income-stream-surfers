---
url: https://expo.dev/changelog/2024-05-07-sdk-51
title: https://expo.dev/changelog/2024-05-07-sdk-51
date: 2025-04-30T17:18:58.356371
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [Expo SDK 51](https://expo.dev/changelog/2024-05-07-sdk-51)
May 7, 2024 by
Brent Vatne
Today we're announcing the release of Expo SDK 51. SDK 51 includes React Native 0.74. Thank you to everyone who helped with beta testing.
## [New Architecture is rolling out in 2024! ](https://expo.dev/changelog/2024-05-07-sdk-51#new-architecture-is-rolling-out-in-2024)
SDK 51 and React Native 0.74 represent a huge step forward in rolling out the long-awaited New Architecture for React Native.
  * We have added support for ["bridgeless"](https://github.com/reactwg/react-native-new-architecture/discussions/154), one of the pillars of the New Architecture, to nearly all Expo modules and the Expo Modules API.
  * We worked in close collaboration with the React Native team at Meta and developers in the React Native ecosystem to ensure there would be support for the New Architecture in many of the most commonly used packages on EAS Build.

### [Testing your app with the New Architecture ](https://expo.dev/changelog/2024-05-07-sdk-51#testing-your-app-with-the-new-architecture)
There is still work to do, but we've made some incredible progress so far this year and we think SDK 51 and React Native 0.74 is the time to test your apps with the New Architecture. With your help, we can enable the New Architecture by default in SDK 52.
That said, most apps will run into some issues when testing with the New Architecture today, but [we encourage you to try](https://docs.expo.dev/guides/new-architecture/#can-i-still-try-the-new-architecture) and [report your experience](https://github.com/reactwg/react-native-new-architecture/discussions/177). Improvements will be arriving rapidly during the SDK 51 and React Native 0.74 cycle, so if your initial attempt isn't successful, you might want to create a branch that you can retry every couple weeks with the latest versions of every package.
  * [Read about the known issues with the New Architecture](https://docs.expo.dev/guides/new-architecture/#troubleshooting) to get an idea of what to expect.
  * [Learn more about enabling the New Architecture in your app](https://docs.expo.dev/guides/new-architecture/). It is **not** enabled by default yet, you can opt in to try it.

### [New default project template and "Getting Started" flow ](https://expo.dev/changelog/2024-05-07-sdk-51#new-default-project-template-and-getting-started-flow)
When you create a new project with `npx create-expo-app`, you will see our ✨renovated new project template✨! It includes common dependencies and configuration that most projects need, so you can hit the ground running.
That's a lot of code to delete if you don't need it! That's why you can run `npm run reset-project` to remove all of the boilerplate code and start fresh.
We've also updated the "Getting Started" flow to make it easier to get started with Expo, whether you are dipping your toes in with Expo Go or diving in with development builds. We hope that these changes will make it easier for you to get started with Expo and to understand the different options available to you.
Choose your own adventure, we'll explain exactly how to get started.
## ["Next" Camera and SQLite APIs are now the defaults ](https://expo.dev/changelog/2024-05-07-sdk-51#next-camera-and-sqlite-apis-are-now-the-defaults)
`expo-camera/next` is now exported from `expo-camera` ([learn more](https://docs.expo.dev/versions/v51.0.0/sdk/camera/)), and `expo-sqlite/next` is now exported from `expo-sqlite` ([learn more](https://docs.expo.dev/versions/v51.0.0/sdk/sqlite/)). You can find the old versions at `expo-camera/legacy` and `expo-sqlite/legacy` during SDK 51, and they will be removed in SDK 52.
Please note that these are complete rewrites, and the APIs have changed significantly. So, if you want to first upgrade to SDK 51 and then migrate to the new API, you can start by updating your imports to the legacy imports.
Code
Copy
```

// New APIs (SDK 50)
import{CameraView}from'expo-camera/next';
import*asSQLitefrom'expo-sqlite/next';
// New APIs (SDK 51): if you import the next packages in your app, update the
// imports to the following:
import{CameraView}from'expo-camera';
import*asSQLitefrom'expo-sqlite';
// Legacy APIs (SDK 50)
import{Camera}from'expo-camera';
import*asSQLitefrom'expo-sqlite';
// Legacy APIs (SDK 51): if you import the legacy packages in your app, update
// the imports to the following:
import{Camera}from'expo-camera/legacy';
import*asSQLitefrom'expo-sqlite/legacy';

```

  * To migrate to the new APIs, refer to the respective docs. While many of the props and function names remain the same, there are also a number of changes. For example, `onBarCodeScanned` is now named `onBarcodeScanned` in the new Camera API. Using TypeScript will also help you to catch these.
  * You can learn more about the motivation behind the new `expo-camera` API in the ["expo-camera/next is ready for a close up" blog post](https://expo.dev/blog/expo-camera-next).
  * The new Expo SQLite API is a complete re-write of our SQLite library, aimed to modernize the API and bring it towards parity with the mature equivalents that exist for web and Node.js. The API is built on SQLite 3.45.3, includes both **sync and async methods** , makes it easy to [import existing databases](https://docs.expo.dev/versions/v51.0.0/sdk/sqlite/#import-an-existing-database), adds support for **prepared statements** , **update callbacks** , the **Blob data type** , and providing **custom build flags** for SQLite, among other features. [Learn more](https://docs.expo.dev/versions/v51.0.0/sdk/sqlite/)


**Thank you** to everybody who used these APIs during SDK 50 and gave us feedback!
## [Introducing `expo-symbols` ](https://expo.dev/changelog/2024-05-07-sdk-51#introducing-)
`expo-symbols` is currently an iOS-only package that provides access to the [SF Symbols library](https://developer.apple.com/sf-symbols/), a collection of over 5000 icons with multiple weights, scales, and support for animations. [Learn more](https://docs.expo.dev/versions/v51.0.0/sdk/symbols/).
Autocompletion with TypeScript makes it easy to find the right symbol for [expo-symbols](https://docs.expo.dev/versions/v51.0.0/sdk/symbols/).
## [Fingerprint runtime version policy promoted from experimental to beta ](https://expo.dev/changelog/2024-05-07-sdk-51#fingerprint-runtime-version-policy-promoted-from-experimental-to-beta)
By using the `"runtimeVersion": { "policy": "fingerprint" }` field in your **app.json** , you can be confident that your updates will always target compatible native runtimes. This makes `@expo/fingerprint` integration with EAS Build and Update seamless — you will notice, for example, that there is now a "Calculate expo-updates runtime version" step on builds for projects that use updates. [Learn more about how this helps you to achieve Continuous Deployment](https://docs.expo.dev/eas-update/continuous-deployment/), and [learn about how](https://expo.dev/blog/fingerprint-your-native-runtime) [`@expo/fingerprint`](https://expo.dev/blog/fingerprint-your-native-runtime) [works](https://expo.dev/blog/fingerprint-your-native-runtime).
## [Expo Router v3.5 ](https://expo.dev/changelog/2024-05-07-sdk-51#expo-router-v35)
Most of the user-facing changes in the latest release of Expo Router are bug fixes and improvements based on feedback from the community. We'll be sharing more in-depth blog posts about the new features and improvements in Expo Router v3.5 in the coming weeks. Some notable changes include:
  * Support for the # segment in URLs with `const { "#": hash } = useLocalSearchParams()`.
  * Added new router functions for dismissing routes `router.dismiss()`, `.dismissAll()` and `.canDismiss()`.
  * Removed `ExpoRequest` and `ExpoResponse` objects in favor of built-in WinterCG-compliant Request/Response objects.
  * Support for platform specific extensions for routes and `_layout` files (a platform agnostic version is still required).
  * Support to handle rewriting deeplinked URLs.
  * Improvements to Typed Routes.
  * `Href` in typed routes is no longer generic.
  * Fixes issues for `experiments.baseUrl` support on web.


Be sure to catch our talks at [React Conf](https://conf.react.dev/) and [App.js Conf](https://appjs.co/) for more information about what we have been working on in Expo Router!
## [Apple Privacy Manifests ](https://expo.dev/changelog/2024-05-07-sdk-51#apple-privacy-manifests)
Starting on May 1, Apple requires that apps using any "restricted reason" APIs include a [privacy manifest](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files). To make this easy for you to comply with, we have added support for the privacy manifest to the Expo config. [Learn more](https://docs.expo.dev/guides/apple-privacy/).
app.json
Copy
```

"expo":{
"ios":{
"privacyManifests":{
"NSPrivacyAccessedAPITypes":[
"NSPrivacyAccessedAPIType":"NSPrivacyAccessedAPICategoryUserDefaults",
"NSPrivacyAccessedAPITypeReasons":["CA92.1"]

```

We also [contributed a feature to React Native](https://github.com/facebook/react-native/pull/44214) that adds support for automatically aggregating privacy manifests from CocoaPods resource bundles. This feature is available in React Native 0.74.1, but there are some edge cases that are not yet supported, so we have temporarily disabled it by default in SDK 51 projects.
For now, we recommend [using the Expo config](https://docs.expo.dev/guides/apple-privacy/) to add privacy manifest configuration for your dependencies. Once a new React Native release is available with fixes for the edge cases, we will enable the aggregation feature by default. If you'd like to try it now, you can opt-in by setting `ios.privacyManifestAggregationEnabled` to `true` in the [expo-build-properties config plugin](https://docs.expo.dev/versions/v51.0.0/sdk/build-properties/#pluginconfigtypeios). Bare projects can set this value directly in the **Podfile**.
## [EAS Update: rollout web UI and new preview page ](https://expo.dev/changelog/2024-05-07-sdk-51#eas-update-rollout-web-ui-and-new-preview-page)
In SDK 50, we released support for "rollouts": this allows you to gradually roll out updates to a percentage of your users, in order to minimize the impact of accidentally introducing a bug to your production environment. This was previously only available in EAS CLI, and we've now released an intuitive web UI to create and manage rollouts more easily.
Select a deployment from the deployments page for your project (in the left sidebar), and from there you can create a new rollout or manage existing rollouts. In this case, we're rolling out the "preview" branch to 10% of users. We can come back and adjust it later if it all goes well, or delete the rollout if it doesn't.
We've also revamped our web UI for opening and sharing updates with your team. Press the "Preview" button on the top right of an Update details page to open the preview modal.
Notice the integration with [Orbit](https://expo.dev/orbit), and the list of compatible development builds. When you scroll down, you will find a shareable URL you can copy to send to your team.
## [🧹 Expo Go: Dropped SDK 49 and 50 ](https://expo.dev/changelog/2024-05-07-sdk-51#-expo-go-dropped-sdk-49-and-50)
The Play Store / App Store versions of Expo Go now only support SDK 51. If you have a project that uses SDK 49 or 50, you can still use Expo CLI or [expo.dev/go](https://expo.dev/go) to install the appropriate version of Expo Go for your project.
### [Single SDK version in Expo Go ](https://expo.dev/changelog/2024-05-07-sdk-51#single-sdk-version-in-expo-go)
[As announced in SDK 50](https://expo.dev/changelog/2024/01-18-sdk-50#a-single-sdk-version-per-release-of-the-expo-go-app:-looking-ahead-to-sdk-51), starting with SDK 51, Expo Go will only support a single SDK version at a time. This means that when the new Expo Go version supporting SDK 51 is released to the App Store and Play Store, it will only support SDK 51. It will not support SDK 50 or below. The Expo Go app will continue to be a great sandbox to get started quickly and experiment with ideas, but we encourage adopting [development builds](https://docs.expo.dev/develop/development-builds/introduction/) for a flexible and powerful development environment suitable for real-world applications at scale.
To make it as easy as possible to install a specific version of Expo Go, created [expo.dev/go](https://expo.dev/go), a website that makes it as easy as possible to install a compatible version of Expo Go on your target platform. This works on Android devices/emulators and iOS simulators, but due to limitations of the iOS platform, you will only be able to use the latest version of Expo Go on physical iOS devices.
[expo.dev/go](https://expo.dev/go) makes it easy to install a compatible version of Expo Go on your target platform. The error message that you see when you try to open a project with an unsupported SDK version in Expo Go links directly to this website with the appropriate version and platform selected.
## [Other Highlights ](https://expo.dev/changelog/2024-05-07-sdk-51#other-highlights)
  * **Beta release of new expo-video library**. Following the success of the "next" Camera and SQLite APIs, we are releasing a new video library that incorporates our learnings from maintaining `expo-av` over the years. This library is a complete rewrite of the Video functionality from `expo-av`, and it's designed to be more reliable and easier to use. We expect to update this library frequently during the SDK 51 cycle, and so it will not yet be available in Expo Go (yet another reason to use [Development Builds](https://docs.expo.dev/develop/development-builds/introduction/)). [Learn more](https://docs.expo.dev/versions/v51.0.0/sdk/video/).
  * **`eslint-config-expo`****and** **`npx expo lint`****command** : You can now run `npx expo lint` in your project to generate an ESLint config file that extends from [`eslint-config-expo`](https://github.com/expo/expo/tree/main/packages/eslint-config-expo). The philosophy of this config is to focus on code correctness and avoid stylistic rules that can be subjective. More documentation is coming soon, until then you can [read the rules in the source code](https://github.com/expo/expo/tree/main/packages/eslint-config-expo/utils).


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

  * **expo-asset config plugin makes it easy to link assets as native resources**. This is useful for linking assets that need to be accessed by native code that expect resource names, or to include assets without needing to modify the Metro configuration. [Learn more](https://docs.expo.dev/versions/v51.0.0/sdk/asset/#configuration-in-appjsonappconfigjs).
  * **Modernized library build.gradle**. If you maintain an Expo module, you don't need to change anything; but, if you want to clean your module up a bit, you can apply the changes from [this diff](https://gist.github.com/brentvatne/88e27545243b828554bb376a7e6dd08d). [Learn more about the changes in](https://github.com/expo/expo/pull/28083) [**expo/expo#28083**](https://github.com/expo/expo/pull/28083).
  * **Bundler speed improvements** : `EXPO_USE_FAST_RESOLVER=1` can be set to enable up to 6x faster Metro resolution. We've also fully removed ["exotic" bundling](https://blog.expo.dev/drastically-faster-bundling-in-react-native-a54f268e0ed1) in favor of the default `expo/metro-config` which has fully integrated stable speed improvements. [Learn more](https://twitter.com/Baconbrix/status/1785364741751214529)
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

  * **Create Expo (App) now supports all mainstream package managers and versions**. Whether you're using Yarn, pnpm, Bun, or npm, `create-expo`/`create-expo-app` will initialize a project with the required configuration to ensure that it will work with your package manager of choice.


Code
Copy
```

🗄️ npx create-expo-app@latest
🌭 bunx create-expo-app
📦 pnpm create expo-app
🧶 yarn create expo-app

```

  * **Expo Orbit for Windows is available in beta**. One click to download, install, and run your apps, now for Windows too! Try it out and give us feedback. [Learn more](https://expo.dev/blog/expo-orbit-now-available-as-a-preview-for-windows).
  * **EAS Build default worker image for iOS builds now uses macOS 14.4 and Xcode 15.3** [Learn more](https://docs.expo.dev/build-reference/infrastructure/).
  * **React Native 0.74 and React 18.2.0 (unchanged from SDK 50)**. There were many improvements in this release, so refer to the [React Native CHANGELOG](https://github.com/facebook/react-native/blob/main/CHANGELOG.md), and [Release Notes](https://reactnative.dev/blog/2024/04/22/release-0.74). One change that many folks will be excited about is that [Yoga has been upgraded to 3.0](https://yogalayout.dev/blog/announcing-yoga-3.0), which improves layout correctness and adds support for two additional layout properties. You may also be able to drop a few polyfills: `TextEncoder`, `btoa`, `atob` are now globally available in Hermes.

## [Deprecations, renamings, and removals ](https://expo.dev/changelog/2024-05-07-sdk-51#deprecations-renamings-and-removals)
  * **expo-camera imports have changed** : if you want to continue using the legacy implementation, update your imports from `expo-camera` to `expo-camera/legacy`. If you were already using the "next" implementation, then update the imports from `expo-camera/next` to `expo-camera`. The legacy implementation will be available until SDK 52.
  * **expo-sqlite imports have changed** : if you want to continue using the legacy implementation, update your imports from `expo-sqlite` to `expo-sqlite/legacy`. If you were already using the "next" implementation, then update the imports from `expo-sqlite/next` to `expo-sqlite`. The legacy implementation will be available until SDK 52.
  * **Fingerprint runtime version policy has been renamed** : `"runtimeVersion": { "policy": "fingerprintExperimental" }` → `"runtimeVersion": { "policy": "fingerprint" }` in your **app.json**.
  * **The** **`hooks`****field has been removed from app.json** : this was previously used for the [Classic Updates](https://blog.expo.dev/sunsetting-expo-publish-and-classic-updates-6cb9cd295378) and `sentry-expo`, which was deprecated in SDK 50 in favor of [`@sentry/react-native`](https://docs.expo.dev/guides/using-sentry/). You should remove the `hooks` field from your app config.
  * **sentry-expo is no longer supported, use** **`@sentry/react-native`****instead**. In SDK 50, `sentry-expo` was deprecated in favor of `@sentry/react-native`, which we worked closely with the Sentry team on to ensure first-class support for Expo projects. [Learn more](https://docs.expo.dev/guides/using-sentry/).
  * **Expo Go only supports a single SDK version as of SDK 51.** [Learn more](https://expo.dev/changelog/2024/05-07-sdk-51#single-sdk-version-in-expo-go).
  * **Google Maps is no longer supported in Expo Go for iOS.** You can use Apple Maps in Expo Go instead (remove the prop `provider={PROVIDER_GOOGLE}` from your `<MapView />` components) or switch to a development build (recommended). If you have already configured Google Maps for your production releases, no additional configuration will be necessary. [Learn how to set up a development build](https://docs.expo.dev/get-started/set-up-your-environment/?mode=development-build).
  * **Foreground location service is no longer supported in Expo Go for Android.** You can use it in a development build, enable the `isAndroidForegroundServiceEnabled` option in the [config plugin](https://docs.expo.dev/versions/latest/sdk/location/#configuration-in-appjsonappconfigjs).
  * **Notifications entitlement is no longer always added to iOS projects during prebuild** : No changes are required if you use `expo-notifications`. If your project uses push notifications but does not use the `expo-notifications` package, you may need to add the `aps-environment` entitlement to your app config:


app.json
Copy
```

"expo":{
"ios":{
"entitlements":{
"aps-environment":"development"

```

### [Known issues ](https://expo.dev/changelog/2024-05-07-sdk-51#known-issues)
  * **Resolved in Expo Go v2.31.5.** ~Expo Router may crash in SDK 51 when switching tabs ([related issue](https://github.com/software-mansion/react-native-reanimated/issues/5968))...~
  * **Resolved in expo-updates@0.25.14.** ~If you have `expo-updates` installed in your app, [you will need to have](https://docs.expo.dev/eas-update/runtime-versions/#setting-runtimeversion) [`runtimeVersion`](https://docs.expo.dev/eas-update/runtime-versions/#setting-runtimeversion) [configured](https://docs.expo.dev/eas-update/runtime-versions/#setting-runtimeversion) to load it in a development build.~
  * **react-native-dotenv is not compatible with expo-router**. If you are using the `react-native-dotenv` Babel plugin, it will overwrite `expo-router` configuration environment variables and you'll see the empty state "Welcome to Expo" screen. We are tracking the incomptibility in [expo/expo#28933](https://github.com/expo/expo/issues/28933), but we recommend removing the library and Babel plugin, and instead using Expo CLI's built-in support for **.env** files ([learn more](https://docs.expo.dev/guides/environment-variables/)).
  * Found an issue? [Report a regression](https://github.com/expo/expo/issues/new?assignees=&amp;labels=needs+review&amp;template=bug_report.yml).

## [➡️ Upgrading your app ](https://expo.dev/changelog/2024-05-07-sdk-51#️-upgrading-your-app)
Here's how to upgrade your app to Expo SDK 51 from 50:
  * **Update to the latest version of EAS CLI** (if you use it):


Terminal
Copy
`npm i -g eas-cli`
  * **Upgrade all dependencies to match SDK 51** :


Terminal
Copy
`npx expo install expo@^51.0.0 --fix`
  * **If you have any** **`resolutions`/`overrides`** **in your package.json, verify that they are still needed.** For example, you should remove `metro` and `metro-resolver` overrides if you added them for `expo-router` in a previous SDK release.
  * **Check for any possible known issues** :


Terminal
Copy
`npx expo-doctor@latest`
  * **Refer to the** [**"Deprecations, renamings, and removals"**](https://expo.dev/changelog/2024/05-07-sdk-51#deprecations-renamings-and-removals) **section** above for breaking changes that are most likely to impact your app.
  * **Make sure to check the** [**changelog**](https://github.com/expo/expo/blob/main/CHANGELOG.md) **for all other breaking changes!**
  * **Upgrade Xcode if needed** : Xcode 15 is needed to compile the native iOS project. We recommend Xcode 15.3 for SDK 51. For EAS Build, projects without any specified `image` will default to Xcode 15.3.
  * **If you don't use** [**Continuous Native Generation**](https://docs.expo.dev/workflow/continuous-native-generation/):
    * Run `npx pod-install` if you have an `ios` directory.
    * Apply any relevant changes from the [Native project upgrade helper](https://docs.expo.dev/bare/upgrade/).
    * Alternatively, you could consider [adopting prebuild](https://docs.expo.dev/guides/adopting-prebuild/) for easier upgrades in the future.
  * **If you maintain any Expo Modules** : it is optional, but you may want to modernize your library **build.gradle** by applying the changes from [this diff](https://gist.github.com/brentvatne/88e27545243b828554bb376a7e6dd08d). [Learn more about the changes in](https://github.com/expo/expo/pull/28083) [**expo/expo#28083**](https://github.com/expo/expo/pull/28083).
  * **If you use Expo Go** : Update the Expo Go app on your phones from app stores. Expo CLI will automatically update your apps in simulators. You can also download the iOS simulator build or the APK from [expo.dev/go](https://expo.dev/go).
  * **If you use** [**development builds with expo-dev-client**](https://docs.expo.dev/development/introduction/): Create a new development build after upgrading.
  * **Questions?** Join our weekly office hours on Wednesdays at 12:00PM Pacific. [Register for Expo Office Hours](https://us02web.zoom.us/meeting/register/tZcvceivqj0oHdGVOjEeKY0dRxCRPb0HzaAK#/registration).

## [📺 Tune in to upcoming conferences for more news! ](https://expo.dev/changelog/2024-05-07-sdk-51#-tune-in-to-upcoming-conferences-for-more-news)
  * **React Conf** : the official React Conference from Meta, May 15-16. Expo team members [Evan Bacon](https://twitter.com/baconbrix/) and [Kadi Kraman](https://twitter.com/kadikraman) will be speaking, alongside many other great speakers. [Learn more](https://conf.react.dev/).
  * **App.js Conf** : a React Native & Expo conference organized by our friends and colleagues at Software Mansion, May 22-24. In all but name, it's the official Expo conference. [Learn more](https://appjs.co/).

## [Thanks to everyone who contributed to the release! ](https://expo.dev/changelog/2024-05-07-sdk-51#thanks-to-everyone-who-contributed-to-the-release)
**The team:** [everyone](https://expo.dev/about) contributed one way or another, with special mentions to the engineers most directly involved in this release: [Łukasz Kosmaty](https://github.com/lukmccall), [Kudo Chien](https://github.com/kudo), and [Tomasz Sapeta](https://github.com/tsapeta) for leading all SDK work. Also, [Alan Hughes](https://github.com/alanjhughes), [Aleksander Mikucki](https://github.com/aleqsio), [Gabriel Donadel](https://twitter.com/donadeldev), [Kadi Kraman](https://github.com/kadikraman), [Aman Mittal](https://github.com/amandeepmittal), [Bartosz Kaszubowski](https://github.com/Simek), [Cedric van Putten](https://github.com/bycedric), [Doug Lowder](https://github.com/douglowder), [Evan Bacon](https://github.com/EvanBacon), [Keith Kurak](https://github.com/keith-kurak), [Kim Brandwijk](https://github.com/kbrandwijk), [Quin Jung](https://github.com/quinlanj), [Will Schurman](https://github.com/wschurman), [Wojciech Dróżdż](https://github.com/behenate), [Mark Lawlor](https://github.com/marklawlor), and [Phil Pluckthun](https://github.com/kitten)!
**External contributors:** [Adrian Drummond](https://github.com/uamcloudadrian), [Adrien Jacquier Bret](https://github.com/ajacquierbret), [Albert Schilling](https://github.com/albert-schilling), [Alejandro Paredes Alva](https://github.com/aparedes), [Alex Fournier](https://github.com/alex-fournier), [Alex Ownejazayeri](https://github.com/alexownejazayeri), [Alexander Pataridze](https://github.com/alexandrius), [Alperen Gözüm](https://github.com/Alperengozum), [Alpheus](https://github.com/alpheustangs), [Amir Angel](https://github.com/17Amir17), [Andreas K](https://github.com/megacherry), [Andrew McCallum](https://github.com/stretch0), [Angel S. Moreno](https://github.com/angelxmoreno), [Aprilia](https://github.com/useEffects), [ArianHamdi](https://github.com/ArianHamdi), [Aroyan](https://github.com/aroyan), [Baraa Bilal](https://github.com/Baraa-bi), [Benny Neugebauer](https://github.com/bennycode), [Brandon Orther](https://github.com/orther), [Brandon Pelton-Cox](https://github.com/bpeltonc), [C. L. Jones](https://github.com/cjones26), [Charles Kornoelje](https://github.com/charkour), [Christian](https://github.com/christianbauer1), [Colton Schlosser](https://github.com/cltnschlosser), [Cyril Bonaccini](https://github.com/cyrilbo), [Daniel Lindenkreuz](https://github.com/dlindenkreuz), [Daniel O'Neill](https://github.com/byudaniel), [Dat Nguyen](https://github.com/imtiendat0311), [David Jebing](https://github.com/davidjbng), [David Storm](https://github.com/david-storm94), [Derek Guenther](https://github.com/dguenther), [Divy Srivastava](https://github.com/littledivy), [Dmitry Litsman](https://github.com/dlitsman), [Dominic Go](https://github.com/dominicstop), [Dylan](https://github.com/dylancom), [Fabrizio Codello](https://github.com/Fabryz), [Frank Calise](https://github.com/frankcalise), [GaelCO](https://github.com/GaelCO), [Hailey](https://github.com/haileyok), [Harsh Mangalam](https://github.com/harshmangalam), [Hichem Fantar](https://github.com/hichemfantar), [Hirbod](https://github.com/hirbod), [Howard Dean Watts](https://github.com/hdwatts), [Humberto](https://github.com/HumbertoL), [Ian Felix](https://github.com/ianfelix), [Ibukun Olofin](https://github.com/cardiscardis), [Jacek Pudysz](https://github.com/jpudysz), [Jackson Ludwig](https://github.com/jludwiggreenaction), [Jake Zhao](https://github.com/jakeinater), [Jakov Glavina](https://github.com/fobos531), [Jakub T. Jankiewicz](https://github.com/jcubic), [James Sigurdarson](https://github.com/jamiees2), [Jamie Birch](https://github.com/shirakaba), [Jan Richter](https://github.com/falnyr), [Jarren San Jose](https://github.com/jarrensj), [Jens Tschirpig](https://github.com/jens1101), [Jonathan Walker](https://github.com/walker-style), [JongHan Leem](https://github.com/jleem99), [Jorens Merenjanu](https://github.com/JorensM), [Josh](https://github.com/Haru-hue), [Jover](https://github.com/JoverZhang), [Jun Matsushita](https://github.com/jmatsushita), [Kamil Owczarz](https://github.com/kowczarz), [Kevin J Gao](https://github.com/gaokevin1), [Kryštof Woldřich](https://github.com/krystofwoldrich), [Leon](https://github.com/leonhh), [Lukas](https://github.com/WookieFPV), [Manoel Aranda Neto](https://github.com/marandaneto), [Mark Rickert](https://github.com/markrickert), [Markus Kurzmann](https://github.com/maks-io), [Mathieu Acthernoene](https://github.com/zoontek), [Mathieu Post](https://github.com/mathieupost), [Maximilian Vitzthum](https://github.com/maximilian-V), [Med Daifi](https://github.com/mdaifi1337), [Mike Hamilton](https://github.com/gorbypark), [Mike Kruk](https://github.com/tamagokun), [Muhammad Bilal](https://github.com/bilal1031), [Nathan Ahn](https://github.com/nahn20), [Nikita Dudin](https://github.com/NikitaDudin), [Otto Bretz](https://github.com/ottob), [Patrick Weisensee](https://github.com/pweisensee), [Pavlos Vinieratos](https://github.com/pvinis), [Peter Jozsa](https://github.com/peter-jozsa), [René Klomp](https://github.com/rklomp), [Riza Hassan](https://github.com/rizahassan), [Rodolfo Perottoni](https://github.com/rodperottoni), [Roman Kubiv](https://github.com/Balibaloo), [Rui Ying](https://github.com/robertying), [Sam Carlton](https://github.com/ThatGuySam), [Seth Lachman](https://github.com/stlachman), [SeungRyeol Lee](https://github.com/toy0605), [Stefano Martella](https://github.com/StefanoMartella), [Stephen Kempin](https://github.com/SKempin), [TN531](https://github.com/tn531), [Thibault Malbranche](https://github.com/Titozzz), [TomOConnor95](https://github.com/TomOConnor95), [Utyfua](https://github.com/utyfua), [Vojtech Novak](https://github.com/vonovak), [Yousef Abu Shanab](https://github.com/youzarsiph), [benjamin](https://github.com/benschac), [dan](https://github.com/gaearon), [ericKuang](https://github.com/eric183), [gabimoncha](https://github.com/gabimoncha), [gkasdorf](https://github.com/gkasdorf), [jack](https://github.com/jackholden), [jay shah](https://github.com/jayshah123), [katayama8000](https://github.com/katayama8000), [lukben2000](https://github.com/lukben2000), [mkhoussid](https://github.com/mkhoussid), [nishan](https://github.com/intergalacticspacehighway), [p16w](https://github.com/msp5382), [pga32ah](https://github.com/pga32ah), [ppichier](https://github.com/ppichier), [raph](https://github.com/raphaelrk), [scottwoodall](https://github.com/scottwoodall), [tess-dev-main](https://github.com/tess-dev-main), [ts-candide](https://github.com/ts-candide), [waiscodes](https://github.com/waiscodes), and [風魔小次郎](https://github.com/XHFkindergarten).
**Beta testers:** [Michał Rusinek](https://github.com/marelix2), [Oscar Landmark](https://github.com/oscklm), [RRaideRR](https://github.com/RRaideRR), [Kryspin Ziemski](https://github.com/kziemski), [Costas Ioannou](https://github.com/killerchip), [nam-aalto](https://github.com/nam-aalto), [FightFarewellFearless](https://github.com/FightFarewellFearless), [contactsimonwilson](https://github.com/contactsimonwilson), [NadeemKhanFh](https://github.com/NadeemKhanFh), [Nathan Bird](https://github.com/nathansbird), [Mike Hamilton](https://github.com/gorbypark), and [Austin Harris](https://github.com/austin43).

