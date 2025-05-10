---
url: https://docs.expo.dev/tutorial/eas/introduction
title: https://docs.expo.dev/tutorial/eas/introduction
date: 2025-04-30T17:12:06.358434
depth: 1
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# EAS Tutorial: Introduction
An introduction to the tutorial for building apps for Android and iOS using Expo Application Services (EAS) that covers the Build, Update, and Submit workflows.
## About this tutorial
This tutorial will give you proficiency with [Expo Application Services (EAS)](https://expo.dev/eas) core services: [Build](https://docs.expo.dev/build/introduction), [Submit](https://docs.expo.dev/submit/introduction), and [Update](https://docs.expo.dev/eas-update/introduction). When you complete the tutorial, you will know how to set up a professional mobile Continuous Integration (CI)/Continuous Development (CD) pipeline for your individual and team projects.
This tutorial covers the following topics:
  * Use EAS Build to create and install a development build, then run it on a device, emulator, or simulator.
  * Experience the benefits of using a development build instead of Expo Go.
  * Implement workflows for sharing development builds with a team or external stakeholders.
  * Automatically increment app build versions.
  * Simultaneously install different app variants, like development and preview, on one device.
  * Utilize EAS Update to create and deploy updates swiftly during the development phase.
  * Automate build processes by integrating with a GitHub repository.


These topics will give us the foundation needed to use EAS effectively and to approach more advanced topics when needed.
## Prerequisites
This tutorial is hands-on and designed to be completed in about two hours. You will need an existing Expo project to follow along and set it up locally on your machine. Options include:
  * Continuing with the Sticker Smash app from our previous tutorial. If new, download it from [GitHub](https://github.com/expo/examples/tree/master/stickersmash).
  * Starting a new project with [`npx create-expo-app`](https://docs.expo.dev/get-started/create-a-project).
  * Using a bare React Native project. Ensure the `expo` package is installed, which you can do [automatically](https://docs.expo.dev/bare/installing-expo-modules) or [manually](https://docs.expo.dev/bare/installing-expo-modules#manual-installation).


## Tools
[Expo Orbit](https://expo.dev/orbit) to manage and launch builds with one click on macOS and Windows.
If you want to install and run the build locally on your machine simultaneously, you can use Android Emulator or iOS Simulator. To set them up, see the following:
  * [Android Emulator](https://docs.expo.dev/workflow/android-studio-emulator)
  * [iOS Simulator](https://docs.expo.dev/workflow/ios-simulator) (available only on macOS)


## Next step
We're ready for this journey after setting up an Expo project locally. In the next chapter, let's learn how to create your first build with EAS Build.
[StartLet's start by configuring a development build.](https://docs.expo.dev/tutorial/eas/configure-development-build)

