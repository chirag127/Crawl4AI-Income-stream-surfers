---
url: https://docs.expo.dev/review/with-orbit
title: https://docs.expo.dev/review/with-orbit
date: 2025-04-30T17:12:06.577521
depth: 1
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# How to launch an update using Expo Orbit
Learn how to open updates with Expo Orbit as part of a review workflow.
[Expo Orbit](https://expo.dev/orbit) is a macOS and Windows app designed to speed up installing and running builds from EAS. It makes running your builds and updates as easy as pressing Open in Orbit.
How does automatic installation and launching of updates work?
When you launch an update, Orbit will look for the latest development build that matches the runtime version and target platform of the update. If a compatible build is found, the update will install automatically on the target device and launch with a deep link that points to the update.
If you don't have any development builds available, either because they have all expired, you haven't created one, you don't use EAS Build, or you are [building your app locally](https://docs.expo.dev/guides/local-app-development), then Orbit will prompt you on how to proceed. Click Launch with deep link in the prompt to open the update if you already have a compatible development build installed on your target device.
## Prerequisites
  * Install the Orbit app before following the steps in this guide. You can download it directly from [GitHub releases](https://github.com/expo/orbit/releases) or see the [alternative method](https://docs.expo.dev/build/orbit#installation) to install it.
  * After installing the app, sign in to your Expo account from Settings.


## Preview an update with Expo Orbit
Expo Orbit launching an update directly from Expo dashboard to an iOS Simulator.
Previewing with Expo Orbit requires you to have an update published. If you haven't published an update, see [Publish an update](https://docs.expo.dev/eas-update/getting-started#publish-an-update) before following the steps in the next section.
### Install and launch the update
> Note: Launching updates using Expo Orbit is not supported on physical iOS devices. It is supported on Android devices/emulators or iOS Simulators.
After the update is published, follow these steps to open it on an Android Emulator or iOS Simulator:
  * Navigate your project's Updates tab.
  * Select the update you want to preview.
  * Click Preview. This will open the Preview dialog.
  * Under Open with Orbit, select a platform to launch the update.
  * Orbit will install and launch the update on the selected Android Emulator or iOS Simulator.


You can now seamlessly launch and review updates using Expo Orbit.

