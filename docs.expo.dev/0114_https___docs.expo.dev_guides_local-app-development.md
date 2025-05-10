---
url: https://docs.expo.dev/guides/local-app-development
title: https://docs.expo.dev/guides/local-app-development
date: 2025-04-30T17:14:04.138702
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Local app development
Learn how to compile and build your Expo app locally.
To build your project into an app locally using your machine, you have to manually generate native code before testing the debug build or creating a production build for it to submit to the app store. There are two ways you can build your app locally. This guide provides a brief introduction to both methods and references to other guides that are necessary to create this workflow.
## Prerequisites
You need to install and set up Android Studio and Xcode to compile and run Android and iOS projects on your local machine. See the following on how to set up these tools:


## Local app compilation
To build your project locally you can use compile commands from Expo CLI which generates the android and ios directories:
Terminal
`# Build native Android project`
`- ``npx expo run:android`
`# Build native iOS project`
`- ``npx expo run:ios`
The above commands compile your project, using your locally installed Android SDK or Xcode, into a debug build of your app.
  * These compilation commands initially run `npx expo prebuild` to generate native directories (android and ios) before building, if they do not exist yet. If they already exist, this will be skipped.
  * You can also add the `--device` flag to select a device to run the app on — you can select a physically connected device or emulator/simulator.
  * You can pass in `--variant release` (Android) or `--configuration Release` (iOS) to build a [production build of your app](https://docs.expo.dev/deploy/build-project#production-builds-locally). Note that these builds are not signed and you cannot submit them to app stores. To sign your production build, see [Local app production](https://docs.expo.dev/guides/local-app-production).


To modify your project's configuration or native code after the first build, you will have to rebuild your project. Running `npx expo prebuild` again layers the changes on top of existing files. It may also produce different results after the build.
To avoid this, add native directories to the project's .gitignore and use `npx expo prebuild --clean` command. This ensures that the project is always managed, and the [`--clean` flag](https://docs.expo.dev/workflow/prebuild#clean) will delete existing directories before regenerating them. You can use [app config](https://docs.expo.dev/workflow/configuration) or create a [config plugin](https://docs.expo.dev/config-plugins/introduction) to modify your project's configuration or code inside the native directories.
To learn more about how compilation and prebuild works, see the following guides:
[Compiling with Expo CLILearn how Expo CLI uses `run` commands to compile your app locally, arguments you can pass to the CLI and more.](https://docs.expo.dev/more/expo-cli#compiling) [PrebuildLearn how Expo CLI generates native code of your project before compiling it.](https://docs.expo.dev/workflow/prebuild)
## Local builds with `expo-dev-client`
If you install [`expo-dev-client`](https://docs.expo.dev/develop/development-builds/introduction#what-is-expo-dev-client) to your project, then a debug build of your project will include the `expo-dev-client` UI and tooling, and we call these development builds.
Terminal
Copy
`- ``npx expo install expo-dev-client`
To create a development build, you can use [local app compilation](https://docs.expo.dev/guides/local-app-development#local-app-compilation) commands (`npx expo run:[android|ios]`) which will create a debug build and start the development server.
## Local builds using Android product flavors
> This feature is only available for SDK 52 and above.
If you have a custom Android project with multiple product flavors using different application IDs, you can configure `npx expo run:android` to use the correct flavor and build type. Expo supports both `--variant` and `--app-id` to customize the build and launch behavior.
The `--variant` flag can switch the Android build type from debug to release. This flag can also configure a product flavor and build type, when formatted in camelCase. For example, if you have both [free and paid product flavors](https://developer.android.com/build/build-variants#change-app-id), you can build a development version of your app with:
Terminal
`- ``npx expo run:android --variant freeDebug`
`- ``npx expo run:android --variant paidDebug`
The `--app-id` flag can be used to launch the app after building using a customized application id. For example, if your product flavor free is using `applicationIdSuffix ".free"` or `applicationId "dev.expo.myapp.free"` you can run build and launch the app with:
Terminal
Copy
`- ``npx expo run:android --variant freeDebug --app-id dev.expo.myapp.free`
> Customizing the Android build type is also possible, but that would break Expo's assumption that the build type release is used for production. You might build unoptimized code in your app using a different build type instead of release.
## Local builds with EAS
[Run builds on your infrastructureLearn how to run EAS Build on your custom infrastructure or locally on your machine with the `--local` flag.](https://docs.expo.dev/build-reference/local-builds)

