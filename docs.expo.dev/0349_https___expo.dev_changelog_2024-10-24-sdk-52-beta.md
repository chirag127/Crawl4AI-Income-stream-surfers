---
url: https://expo.dev/changelog/2024-10-24-sdk-52-beta
title: https://expo.dev/changelog/2024-10-24-sdk-52-beta
date: 2025-04-30T17:19:00.775137
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [Expo SDK 52 beta is now available](https://expo.dev/changelog/2024-10-24-sdk-52-beta)
Oct 24, 2024 by
Brent Vatne
**The SDK 52 beta period begins today and will last approximately two weeks.** The beta is an opportunity for developers to test out the SDK and ensure that the new release does not introduce any regressions for their particular systems and app configurations. We will be continuously releasing fixes and improvements during the beta period, some of these may include breaking changes.
SDK 52 beta includes React Native 0.76.0. The full release notes for SDK 52 won't be available until the stable release, but you can browse the changelogs in the [expo/expo repo](https://github.com/expo/expo) to learn more about the scope of the release and any breaking changes. We'll merge all changelogs into the root **CHANGELOG.md** when the beta is complete.
We're also [hosting office hours on Discord](https://chat.expo.dev/) for those of you interested in helping test the release!
### [The New Architecture rollout is happening now! ](https://expo.dev/changelog/2024-10-24-sdk-52-beta#the-new-architecture-rollout-is-happening-now)
After a year of working on a number of varied initiatives at Expo and across the React Native ecosystem, in close collaboration with Meta, Software Mansion, and many other developers in the community, we are excited to be rolling out the New Architecture by default for all newly created projects from SDK 52 onward.
Not familiar with React Native's "New Architecture"? Read ["New Architecture is here" on the React Native blog](https://docs.expo.dev/guides/new-architecture/), and/or [join our livestream with Nicola Corti and Riccardo Cipolleschi from Meta on October 29th](https://www.youtube.com/live/VqFwrEoni40).
#### [What the rollout will look like ](https://expo.dev/changelog/2024-10-24-sdk-52-beta#what-the-rollout-will-look-like)
  * **The New Architecture is now enabled by default for all new projects**. Starting with SDK 52, when you create a new project with `npx create-expo-app --template default@beta`, you will see that `newArchEnabled` is set to `true` in your **app.json**.
  * **Projects that are upgrading from a previous SDK release can opt in to the New Architecture** , it's not required and it will not be automatically enabled for existing projects in SDK 52. We recommend enabling it after upgrading successfully using the old architecture. In SDK 53, we will likely enable the New Architecture by default and you will have to opt out. In a future release in 2025, we may remove the ability to use the old architecture.
  * **Expo Go for SDK 52 and higher will only support the New Architecture**. All Expo SDK packages support the New Architecture, and any of the third party libraries that we include in Expo Go are also supported. This should not impact your experience of using Expo Go. If it does, you can still opt out of using the New Architecture in your project by explicitly disabling it by setting `newArchEnabled` set to `false` in your **app.json** and creating a [development build](https://docs.expo.dev/develop/development-builds/introduction/).

#### [Testing your app with the New Architecture ](https://expo.dev/changelog/2024-10-24-sdk-52-beta#testing-your-app-with-the-new-architecture)
  * Ensure that you use the latest version of all third-party native libraries.
  * Run `npx expo-doctor@latest` in your SDK 52 project to find any library incompatibilities that may cause issues when migrating. Doctor will validate your dependencies against [React Native Directory](https://reactnative.directory/) and let you know if any libraries are known to be incompatible with the New Architecture, or if their compatibility status is unknown. In some cases you will want to migrate to alternative libraries that are compatible with the New Architecture. If a library doesn't support the New Architecture yet, there is a good chance that it is not actively maintained.
  * [Read about the known issues](https://docs.expo.dev/guides/new-architecture/#troubleshooting) to get an idea of what to expect.
  * [Learn more enabling the New Architecture in your app](https://docs.expo.dev/guides/new-architecture/).

### [Highlights ](https://expo.dev/changelog/2024-10-24-sdk-52-beta#highlights)
  * **iOS deployment target bumped** (minimum supported version) from 13.4 to iOS 15.1. This mirrors the minimum version of iOS that is required by React Native 0.76.
  * **Android** **`minSdkVersion`****and** **`compileSdkVersion`****bumped** from 23 to 24 and 34 to 35 respectively. This mirrors changes from React Native.
  * **EAS Build default worker image for iOS builds updated** to macOS 14.6 and Xcode 16.0. [Learn more](https://docs.expo.dev/build-reference/infrastructure/).
  * **Stable release of new** **`expo-video`****library**. We released the beta for `expo-video` in SDK 51 and received a lot of great feedback. We spent the last SDK cycle incorporating that feedback and making other improvements to the library, and now we're ready to call it stable! We recommend migrating to it from `expo-av` now. It is more reliable, easier to use, more performant, and more powerful than `Video` component from `expo-av`. We've also added a utility to `expo-video` for generating video thumbnails, which may replace `expo-video-thumbnails` in the future. [Learn more about expo-video](https://docs.expo.dev/versions/v52.0.0/sdk/video/).


`expo-video` now includes lock screen controls and support for Picture-in-Picture on both Android and iOS, among many other features. [Learn more](https://docs.expo.dev/versions/v52.0.0/sdk/video/).
  * **Beta release of new** **`expo-audio`****library**. Similar to our rewrites over other libraries, like expo-video and [expo-camera](https://expo.dev/blog/expo-camera-next), we are focused on providing a modern, stable, and easy to use API that works great for the vast majority of apps. It may not handle certain niche use cases that requires more control, since this is often requires trading off stability and ease of use even in common cases. The `expo-audio` library is now in beta, and we're excited to get your feedback! We think it's easier than ever now to add audio to your apps. [Learn more about expo-audio](https://docs.expo.dev/versions/v52.0.0/sdk/audio/).
  * **Beta release of** **`expo-file-system/next`**. We rebuilt the`expo-file-system` library with a new API designed for ease of use and developer experience, based on Expo Modules. This enables synchronous read/write operations, using `SharedObjects` to represent files and directories and advanced features like stateful file handles. The `expo-file-system/next` library is now in beta (fully backwards compatible if you decide to partially adopt it), with plenty more of improvements and integrations planned! [Learn more about expo-file-system/next](https://docs.expo.dev/versions/v52.0.0/sdk/filesystem-next/).
  * **Many improvements to** **`expo-camera`**. After promoting it out of the`expo-camera/next` namespace in SDK 51, we've followed up with a bunch of fixes and improvements based on feedback from the community. It's now more robust for a wider range of use cases. We've also switched over to using Swift Concurrency, which improves the camera configuration setup reliability compared to using dispatch queues. Refer to the [expo-camera changelog](https://github.com/expo/expo/blob/main/packages/expo-camera/CHANGELOG.md) for more information.
  * **New** **`expo-live-photo`****library**. This library is currently iOS-only, and it allows you to play back iOS Live Photos. We've also added support to `expo-image-picker` for picking live photos from the photo library. [Learn more](https://docs.expo.dev/versions/v52.0.0/sdk/live-photo).
  * **Improvements in affordances for edge-to-edge layouts on Android**. We worked with [@zoontek](https://github.com/zoontek) to help ship [react-native-edge-to-edge](https://github.com/zoontek/react-native-edge-to-edge), a library that 'effortlessly enables [edge-to-edge](https://developer.android.com/develop/ui/views/layout/edge-to-edge) display in React Native, allowing your Android app content to flow seamlessly beneath the system bars.' [Learn more](https://x.com/zoontek/status/1844814034710696371).
  * **`expo-image`****v2 introduces a powerful new API for loading images** : the [`useImage`](https://docs.expo.dev/versions/v52.0.0/sdk/image/#useimagesource-options-dependencies) hook lets you preload the image into memory, providing its size and metadata before the image is rendered. The result of this hook is a [shared reference](https://docs.expo.dev/versions/v52.0.0/sdk/expo/#sharedref-1) to a native image instance ([Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) on Android and [UIImage](https://developer.apple.com/documentation/uikit/uiimage) on iOS) that can be passed as a source to render the image immediately, without any additional network requests and I/O operations. We've also added `onDisplay` event that is called once the image is displayed on the screen.


Code
Copy
```

import{ useImage,Image}from'expo-image';
import{Text}from'react-native';
exportdefaultfunctionMyImage(){
const image =useImage('https://picsum.photos/1000/800',{
  maxWidth:800,
onError(error, retry){
console.error('Loading failed:', error.message);
});
if(!image){
return<Text>Image is loading...</Text>;
return(
<Image
source={image}
style={{ width: image.width/2, height: image.height/2}}
/>
);

```

  * **`expo-image-manipulator`****now offers a** [**new object-oriented, contextual API**](https://docs.expo.dev/versions/v52.0.0/sdk/imagemanipulator/#manipulateuri) that is more performant, more flexible, and provides better developer experience. Images returned from this API can be efficiently passed as a source to the `Image` component from `expo-image` v2. [See a usage example](https://github.com/expo/expo/blob/d32a975316f9c3aeb6affe733739beb3f532d362/apps/native-component-list/src/screens/ImageManipulatorScreen.tsx).
  * **New** **`expo-sqlite/async-storage`****API provides convenient key/value storage, built on top of** **`expo-sqlite`**. It implements the same API as`@react-native-async-storage/async-storage` , but it also adds synchronous APIs (for example, you can call `getItemSync` instead of `getItem` to make it synchronous). [Learn more about expo-sqlite/async-storage](https://docs.expo.dev/versions/v52.0.0/sdk/sqlite/#asyncstorage).
  * **`expo-sqlite`****now supports SQLCipher**. You can enable it with the [`expo-sqlite`](https://docs.expo.dev/versions/v52.0.0/sdk/sqlite/#configuration-in-appjsonappconfigjs) [config plugin](https://docs.expo.dev/versions/v52.0.0/sdk/sqlite/#configuration-in-appjsonappconfigjs). While building support for this, we also resolved an [issue](https://github.com/expo/expo/issues/30546) that would occasionally make `expo-updates` incompatible with other libraries that use SQLite.
  * **`expo-sqlite`****now supports saving SQLite databases to shared containers on iOS** , and any other available directory. This allows an app extension (eg: widget, share extension) to share a database with the main application, or across other app extensions. Thanks to [@IgorKhramtsov](https://github.com/IgorKhramtsov) for a great [PR](https://github.com/expo/expo/pull/31278) implementing this.
  * **Expo DevTools Plugins now support binary payloads** , such as `Uint8Array`. This was built in order to support advanced use cases for an upcoming state management library, which we will talk about in our upcoming [Launch Party](https://expo.dev/launch-party) starting November 18th.
  * **expo-notifications improvements** : over the SDK 51 cycle, we've rolled out many bugfixes and improvements to the library, including but not limited to better support for FCMv1. You can expect a lot of improvements to `expo-notifications` as we continue investing in it.
  * **Support for iOS 18 tinted icons**. With the introduction of the controversial iOS 18 tinted icons, it's now possible to provide [a version of your icon that works well when tinted by iOS](https://developer.apple.com/design/human-interface-guidelines/app-icons#Platform-considerations), rather than letting iOS attempt to tint your standard icon. Thank you to [@fobos531](https://github.com/fobos531) for the [excellent pull request](https://github.com/expo/expo/pull/30247). [Learn how to configure a tinted icon in your app config](https://docs.expo.dev/versions/v52.0.0/config/app/#icon-2).
  * **Fixed an issue with environment variables and embedded** **`expoConfig`**:`expo-constants` now properly sources `@expo/env` to ensure your **.env** files are loaded when generating the embedded `Constants.expoConfig` data. This was also backported to SDK 51. Thanks to [ChromeQ](https://github.com/chromeq) for working with us to narrow down the issue.
  * [**Calendar form sheets**](https://docs.expo.dev/versions/v52.0.0/sdk/calendar/#launching-system-provided-calendar-dialogs) **now launchable from** **`expo-calendar`**. Shout out to the guy at App.js Conf who asked me about this. Be sure to attend[App.js 2025](https://appjs.co/) and tell [Brent](https://x.com/notbrent) what you'd like to see in the Expo SDK!
  * **React Native DevTools** replaces the JavaScript debugger introduced in SDK 47. It's very similar, so you don't have to worry about learning a new tool (they were both built on on Chrome DevTools and the Chrome DevTools Protocol). [Learn more about React Native DevTools](https://reactnative.dev/blog/2024/10/23/release-0.76-new-architecture#react-native-devtools).
  * **React Native 0.76** is a big release, we've mentioned some of its features here but you can learn more about it in the [React Native 0.76 release notes](https://reactnative.dev/blog/2024/10/23/release-0.76-new-architecture).

### [DOM Components ](https://expo.dev/changelog/2024-10-24-sdk-52-beta#dom-components)
DOM Components make it easier than ever to incrementally migrate from web to native. They also provide a useful escape hatch that makes it easy to integrate any web library into your native app, even if it's just for a single view.
To use DOM Components, create a React DOM component file (using `<div>`, `<span>`, even `<marquee>` if you want) and then add the `"use dom"` directive to the top of the file. You will now be able to import that DOM component from a React Native component. The DOM component will be rendered inside of a webview, but you can mostly use it like a normal component via props (with a slightly different pattern required for non-serializable props, in particular functions).
You can use any web library that you like within your DOM components. [Thor used DOM components for custom Protomaps tiles](https://supabase.com/blog/self-host-maps-storage-protomaps). [Raphaël used DOM components to quickly add a spherical photo viewer](https://x.com/rphlmr/status/1845771295872426227). And of course, [Evan Bacon](https://twitter.com/baconbrix) has shared [a lot](https://x.com/Baconbrix/status/1827762941581799849) [of](https://x.com/Baconbrix/status/1823366398405415176) [examples](https://x.com/rphlmr/status/1845771295872426227). In each case, you may want to migrate to a native equivalent eventually for the best experience, but DOM components are a great starting point - in particular if you already have a web app that you want to migrate to native, or you already have a library that does what you want but is not yet available for native Android or iOS.
Check out Evan Bacon's recent ["Introducing DOM components" talk](https://www.youtube.com/watch?v=JUOxTLu8ZsM), and get started by reading the [DOM Components guide](https://docs.expo.dev/guides/dom-components/).
### [Expo CLI ](https://expo.dev/changelog/2024-10-24-sdk-52-beta#expo-cli)
  * **Experimental universal Tree Shaking support**. Automatically remove unused ESM imports and exports from your app to improve OTA and web performance. [Learn more](https://docs.expo.dev/guides/tree-shaking/).
  * **Experimental support for React Compiler** : enable it with `"experiments": { "reactCompiler": true }` in your app config. [Learn more](https://docs.expo.dev/preview/react-compiler/).
  * **Fast resolving by default across all platforms.** Up to 15x faster resolution. This was merged into Metro, so it's now enabled for all React Native projects as of React Native 0.76.
  * **New flag to pass app to launch to iOS run command** : `npx expo run:ios --binary /path/to/bin`.
  * **Eager builds with Android/iOS run commands** : with `npx expo run --eager`, Expo CLI will bundle your app with Metro before compiling it. This is helpful when you are creating a release build and want to ensure that your JavaScript bundles correctly before proceeding to the relatively more time consuming native build step.
  * **New flag to improve debugging of missing modules** : `EXPO_USE_METRO_REQUIRE=1`.
  * **Support for** **`resolver.requireCycleIgnorePatterns`****in Metro server bundles**.
  * **`EXPO_USE_METRO_WORKSPACE_ROOT`****is now enabled by default**. The monorepo root is considered to "contain all content", the workspace root adds something called "server root" besides the "project root". This fixes a couple of things related to: resolution to workspaces in the monorepo, splitting the Metro cache for near-identical apps in the same monorepo, using the correct entry point resolution in various cases.
  * **Metro will now be automatically configured to support pnpm monorepos**. [Learn more](https://docs.expo.dev/guides/monorepos/#automatic-configuration).
  * **CSS modules can now import other CSS modules.** So you can put CSS modules in your CSS modules while you write CSS modules ([remember 2008?](https://knowyourmeme.com/memes/xzibit-yo-dawg)).
  * **Web assets now use strings / ImageSource for easier interop with web ecosystem.**
  * **Added** **`ios.appleTeamId`****field to app config** , which sets the `DEVELOPMENT_TEAM` in all PBX projects when defined. This improves affordances for multi-target iOS apps.
  * **Reduced size of Expo CLI by removing dependency RNC CLI.** Expo projects use `expo-modules-autolinking` to discover both Expo Modules and modules built with the React Native module API (such as Turbo Modules). You can opt in to `@react-native-community/cli` autolinking by setting the environment variable `EXPO_USE_COMMUNITY_AUTOLINKING=1` and running `pod install` again.

### [Expo Modules API ](https://expo.dev/changelog/2024-10-24-sdk-52-beta#expo-modules-api)
  * **Better support for sharing SharedRef between packages**. During the conversion process, the inner reference type is now validated to ensure the conversion is possible. Additionally, developers can check the type of SharedRef in the JavaScript.
  * **Enhanced support for** **`SharedObject`**, introducing new memory pressure handling for more effective garbage collection of native objects with significant data.
  * **`CMTime`****(iOS) and** **`Duration`****(Android) are now supported as convertible types** , making it easier to handle time-based media in native modules.
  * **Added** **`customizeRootView`****to** **`ExpoAppDelegateSubscriberProtocol`**. This enables developers to customize the root view in their applications through[AppDelegate subscribers](https://docs.expo.dev/modules/appdelegate-subscribers/), providing more control over the app's initial layout and setup.
  * **Added** **`OnUserLeavesActivity`****event to** [**Android lifecycle listeners**](https://docs.expo.dev/modules/android-lifecycle-listeners/). This is triggered when the user leaves the app, e.g., pressing the Home button.
  * **New event APIs** **`useEvent`****and** **`useEventListener`**provide simpler event management and reduce the need for you to write boilerplate event code yourself in each module.
  * **Migrated EventEmitter to C++ implementation**. The new EventEmitter in C++ replaces the legacy JS version. This migration paves the way for potential improvements in performance and reliability in event handling within Expo modules.
  * **Extended Expo Module config to simplify wrapping third-party AARs**. Use `android.gradleAarProjects` in your **expo-module.config.json** to wrap third-party AARs. [Learn more](https://docs.expo.dev/modules/third-party-library/#are-you-trying-to-use-a-aar).
  * **Exposed a new way to define type-safe web modules with events** : `registerWebModule`.

### [Expo Router ](https://expo.dev/changelog/2024-10-24-sdk-52-beta#expo-router)
  * **Early preview of Server Components and Server Actions**. [As demonstrated at React Conf 2024](https://www.youtube.com/watch?v=djhEgxQf3Kw), we've been working on support for React Server Components. We're incredibly excited about the potential this offers for new patterns in app development. This preview is meant to help libraries (such as `react-native`) adopt React Server Components support, and not intended for production yet. A dedicated blog post is coming soon, for now you can [learn more in the docs](https://docs.expo.io/guides/server-components).
  * **Now uses React Navigation v7**. During the beta period, we're using the RC release. The final v7 release is coming soon. [Learn more](https://reactnavigation.org/blog/2024/06/27/react-navigation-7.0-rc)
  * **New** **`expo-router/ui`****API for tabs**. The new "headless" `<Tabs />` component provides Radix-like API for un-styled `<Tab />` layouts, which makes it easier to build these layouts for web.
  * **New** **`expo-router/link`****export**. Better alignment for upcoming `package.json` exports support and server components support.
  * **Added** **`legacy_subscribe`****for broader compatibility**. This API was added to `+native-intent` as a fallback for projects using services like Branch, which support React Navigation via `Linking.subscribe` but do not native support Expo Router yet. [Learn more](https://docs.expo.dev/router/advanced/native-intent/#legacy_subscribe).
  * **Added** **`sitemap`****Config Plugin option to disable the built-in route**. You can now disable the default `/_sitemap` route by passing `sitemap: false` to the `expo-router` Config Plugin.

### [Deprecations ](https://expo.dev/changelog/2024-10-24-sdk-52-beta#deprecations)
  * **Push notifications (remote notifications) will no longer be supported in Expo Go for Android in SDK 53**. In SDK 52, you will be warned when using push notifications-related features from `expo-notifications` in Expo Go. The reason for this change is that we (1) want to make transition from Expo Go to development builds smoother, and (2) make push notifications and their setup more transparent. Push notifications are deeply integrated with the native app which they are delivered to. Expo Go made some necessary integration steps in order to support push notifications - but the integration was somewhat opaque and would become invalid once users transitioned from Expo Go to development build. With this change, we instead ask developers to create a development build when they would like to use push notifications and configure them right away. Learn how to set up push notifications: [docs](https://docs.expo.dev/versions/latest/sdk/notifications/#configuration), [video](https://youtu.be/BCCjGtKtBjE?si=dy9UwwKPpVJwv-x5).
  * **Google Maps will no longer be supported in Expo Go for Android in SDK 53**. In SDK 52, you will be warned when using `react-native-maps` in Expo Go for Android. On iOS, Expo Go only supports Apple Maps. [You can use Google Maps in development builds](https://docs.expo.dev/versions/v52.0.0/sdk/map-view/#deploy-app-with-google-maps). Similar to the remote notifications change, this ensures that the setup of Google Maps is transparent and it is clear to developers that they will need to configure it before they are able to use the API in production.
  * **CRSQLite support in expo-sqlite has been deprecated**. This was a fun experiment for us, but CRSQLite library is not currently under active development and so we've decided to remove it for now.
  * **`expo-av`****Video API is deprecated** , use `expo-video` instead.

### [Notable breaking changes ](https://expo.dev/changelog/2024-10-24-sdk-52-beta#notable-breaking-changes)
  * **Expo Go now uses the New Architecture for all apps**. Because of this change, **JSC is no longer supported in Expo Go** , you will need to use Hermes. If you are still using JSC, reach out to us at secure@expo.dev and let us know why!
  * **`expo-camera/legacy`****has been removed** : migrate to `expo-camera` from `expo-camera/legacy`.
  * **`expo-sqlite/legacy`****has been removed** : migrate to `expo-sqlite` from `expo-sqlite/legacy`.
  * **`expo-barcode-scanner`****has been removed** : it was deprecated in SDK 50 and slated for removal in SDK 51. The barcode scanning functionality provided by `expo-camera` is a better alternative (and it also supports the iOS 16+ [`DataScannerViewController`](https://developer.apple.com/documentation/visionkit/scanning-data-with-the-camera)). [Learn more](https://docs.expo.dev/versions/v52.0.0/sdk/camera/#launchscanneroptions).
  * **Unused** **`privacy`****field from app.json has been removed**. This field was previously used when the Expo website had optional public-facing pages for projects, which we no longer provide.
  * **create-react-native-app is no longer supported**. Use `npx create-expo-app` instead, it's pretty much the same thing! We're consolidating CLIs for clarity in the ecosystem.
  * **`expo-notifications`****trigger types changed** : we simplified calendar trigger input types in response to feedback that the old approach was difficult to use and error prone. [Learn more](https://github.com/expo/expo/pull/31598).
  * **`expo-router`****type changes** : removed generic from `Href` type and navigation hooks/APIs, eg: `Href<T> -> Href` / `router.push<T>()` -> `router.push()`. The purpose is to simplify passing `Href` as a props, avoiding the need to creating generic typed components, and preserving typing with `forwardRef`.
  * **`expo-router`****Typed Routes no longer generate types for partial group** **`Href`s**. Previously `/(hello)/(world)/page` could be typed as `/(world)/page`. This will now show a TypeScript error. The href is still valid, if you have this edge case you will need to cast to `href`. You can revert to the old behaviour by setting `partialRouteTypes` in the Expo Router config plugin.
  * When using the New Architecture, React state `set` functions will no longer execute synchronously (due to [automatic batching](https://reactnative.dev/blog/2024/10/23/the-new-architecture-is-here#automatic-batching)). If you have any code that assumes state setters execute synchronously, you may encounter subtle issues.

### [Known issues ](https://expo.dev/changelog/2024-10-24-sdk-52-beta#known-issues)
  * If you use npm, you may encounter installation issues related to peer dependencies, eg: "ERESOLVE could not resolve" / "Could not resolve dependency". This is due to libraries having peer dependencies such as `"expo": ">= 51.0.0"`, which will not match `"expo@52.0.0-preview"` (due to [this quirk of npm](https://github.com/npm/npm/issues/8854)). You can work around this using `--legacy-peer-deps` and/or setting that option in your **.npmrc** file, or switching to another package manager.
  * Expo Go for iOS is not yet available on TestFlight External Beta. Use the Simulator build, installable through Expo CLI, or a development build.
  * Expo Go for Android and iOS aren't able to launch into React Native DevTools. A fix is coming soon. Use a development build instead.
  * Developer preview of React Server Components are not meant for production use yet.
  * When launching React DevTools, you will see multiple inspectable JavaScript targets when using development builds or Expo Go. One of these corresponds to your app, and others will be the apps that power the development UI. We're working on a fix to hide the extra targets related to the development UI.
  * DOM components are not yet updatable with `expo-updates`, but we are working on it.
  * Snack is not yet supported for SDK 52.

### [Known regressions ](https://expo.dev/changelog/2024-10-24-sdk-52-beta#known-regressions)
  * Found an issue? [Report a regression](https://github.com/expo/expo/issues/new?assignees=&amp;labels=needs+review&amp;template=bug_report.yml).

### [How to try out the beta release ](https://expo.dev/changelog/2024-10-24-sdk-52-beta#how-to-try-out-the-beta-release)
  * **Initialize a new project with SDK 52 beta:**


Terminal
`# npm``npx create-expo-app@latest --template default@beta``# bun``bun create expo-app --template default@beta``# pnpm``pnpm create expo-app --template default@beta``# yarn``yarn create expo-app --template default@beta`
**Note:** `create-expo-app` will install dependencies with the package manager that you are using. For example, with npm when `npx` is used and yarn when `yarn create` used.
  * **Upgrade an existing project:**
    * Upgrade all dependencies to match SDK 52:


Terminal
Copy
`npx expo@next install --fix`
  * ~**Install the latest Expo Go for iOS to your physical device:** ~ (TestFlight External Beta link coming soon, use a development build or run Expo Go in a simulator instead, for now).
  * **Install the latest Expo Go for Android emulators/physical devices or iOS simulators:**
    * Launch your project through Expo CLI (press the a or i keyboard shortcut after running `npx expo start`) and the updated version of Expo Go will be automatically installed.
  * [**Read the documentation**](https://docs.expo.dev/versions/v52.0.0) by selecting it from the version selector in the API reference section.

### [What to test ](https://expo.dev/changelog/2024-10-24-sdk-52-beta#what-to-test)
  * Upgrade your app with `npm install expo@next` or `yarn add expo@next`, then run `npx expo install --fix` and consult the [Native project upgrade helper](https://docs.expo.dev/bare/upgrade/) and [report any issues you encounter](https://github.com/expo/expo/issues/new?assignees=&amp;labels=needs+review&amp;template=bug_report.yml).
  * Build your app with EAS Build, and/or if you have Xcode installed and up to date on your machine and/or Android Studio, try prebuilding your app and running it: `npx expo prebuild --clean` and `npm run ios` and `npm run android`. Alternatively, try out `npx expo run`. Any new issues? [Please report them](https://github.com/expo/expo/issues/new?assignees=&amp;labels=needs+review&amp;template=bug_report.yml).
  * Did we miss updating the documentation somewhere? [Let us know](https://github.com/expo/expo/issues/new?assignees=&amp;labels=docs&amp;template=documentation.yml&amp;title=%5Bdocs%5D+).

### [How to report issues ](https://expo.dev/changelog/2024-10-24-sdk-52-beta#how-to-report-issues)
  * Create an issue on <https://github.com/expo/expo/issues> and be sure to fill out the appropriate template (and include a [minimal reproducible example](https://stackoverflow.com/help/minimal-reproducible-example), please!).
  * Figuring out the underlying causes of issues is super helpful.
  * Let us know that you are using the SDK 52 beta so we can prioritize the issue.
  * The most helpful beta testers will be listed in the final release notes (and possibly even provided with some [Discord](https://chat.expo.dev/) flair — you can [link your Discord and GitHub accounts to your Expo account](https://expo.dev/settings#connections)).


Thank you for helping us with testing the release — we look forward to shipping it soon! 🚀

