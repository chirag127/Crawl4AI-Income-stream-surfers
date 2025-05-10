---
url: https://docs.expo.dev/build/orbit
title: https://docs.expo.dev/build/orbit
date: 2025-04-30T17:12:52.005104
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo Orbit
Accelerate your development workflow with one-click build and update launches and simulator management.
[Expo Orbit](https://expo.dev/orbit) for macOS and Windows enables faster to install and launch builds or updates from EAS, local files, or run Snack projects, on simulators and physical devices.
## Why Orbit
Before Orbit, installing builds or updates from EAS (on Android and iOS physical devices or emulator/simulator) or running Snack projects on simulators was manual. You had to run `eas build:run` command and select a build for your chosen device or download the archive and then drag and drop it to the simulator (in the case of iOS). Also, for Snack projects, additional steps included installing Expo Go on the virtual device, logging in, and then selecting the Snack from the list. Orbit makes all of these steps as seamless as possible.
## Highlights
  * List and launch simulators, including running Android emulators without audio.
  * Install and launch builds from EAS on simulators and real devices in one click.
  * [Install and open updates from EAS](https://docs.expo.dev/review/with-orbit) on Android Emulators or iOS Simulators.
  * Launch Snack projects in your simulators in one click.
  * Install and launch apps from local files using Finder or drag and drop a file into the menu bar app. Orbit supports any Android .apk, iOS Simulator compatible .app, or ad hoc signed apps.
  * See pinned projects from your [EAS dashboard](https://expo.dev) and quickly launch your latest builds.


## Installation
> Orbit relies on the Android SDK on both macOS and Windows and `xcrun` for device management only on macOS, which requires setting up both [Android Studio](https://docs.expo.dev/workflow/android-studio-emulator) and [Xcode](https://docs.expo.dev/workflow/ios-simulator).
macOS
Windows
You can download Orbit with Homebrew for macOS, or directly from the [GitHub releases](https://github.com/expo/orbit/releases).
Terminal
Copy
`- ``brew install expo-orbit`
If you want Orbit to start when you log in automatically, click on the Orbit icon in the menu bar, then Settings and select the Launch on Login option.
> Note: Orbit for Windows is in preview and is only compatible with x64 and x86 machines. Compatibility for other architectures will be added in the future.
You can download Orbit for Windows directly from the [GitHub releases](https://github.com/expo/orbit/releases).

