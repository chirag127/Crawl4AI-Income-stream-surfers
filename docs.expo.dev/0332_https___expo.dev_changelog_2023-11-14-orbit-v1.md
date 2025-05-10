---
url: https://expo.dev/changelog/2023-11-14-orbit-v1
title: https://expo.dev/changelog/2023-11-14-orbit-v1
date: 2025-04-30T17:18:38.876446
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [Expo Orbit v1: launcher app launched into orbit](https://expo.dev/changelog/2023-11-14-orbit-v1)
Nov 14, 2023 by
Gabriel Donadel
Expo Orbit for macOS makes it faster and easier to install and run builds from EAS or elsewhere, and to run Snack projects on simulators and physical devices.
The current process for installing builds from EAS (Android device/emulator, iOS simulator, iOS device) and running Snack projects on simulators is more manual than it needs to be. You can use `eas build:run` and select a build for Android devices/emulators or iOS simulators, or you can download the archive, extract it, and drag and drop it to the simulator/emulator. For [Snack projects](https://snack.expo.dev/), additional steps include [installing Expo Go](https://docs.expo.dev/get-started/expo-go/) in the simulator through the CLI, logging in, and selecting the Snack from a list.
To improve this, [in August 2023 we released Orbit](https://expo.dev/changelog/2023/08-09-orbit) as an experiment intended to speed up development builds and Snack projects. The goal was to make these steps as seamless as possible, aligning with the user-friendly experience that Expo offers. The community feedback was very positive and we decided to move forward with this project.
## [What is Expo Orbit v1 and what are the benefits? ](https://expo.dev/changelog/2023-11-14-orbit-v1#what-is-expo-orbit-v1-and-what-are-the-benefits)
Expo Orbit v1 is a macOS menu bar app designed to make your development workflow even faster, allowing you to:
  * List and launch simulators, including the ability to run Android emulators without audio


  * Install and launch [builds from EAS](https://docs.expo.dev/build/introduction/) to your simulators and real devices with just one click


  * Launch Snack projects in your simulators by clicking a button


  * Install and launch apps from local files using Finder or just drag and drop a file into the menu bar app. Orbit supports any Android apk, simulator compatible .app, or ad-hoc signed apps


  * See pinned projects and quickly launch your latest builds

## [Get started with Expo Orbit ](https://expo.dev/changelog/2023-11-14-orbit-v1#get-started-with-expo-orbit)
You can download Orbit via Homebrew or directly through [GitHub](https://github.com/expo/orbit/releases).
Terminal
Copy
`brew install expo-orbit`
At this point in time, Orbit is compatible only with macOS but we have exciting plans to integrate it further into the Expo ecosystem and add even more features.
Try out Expo Orbit now, explore its capabilities, and share your feedback. Your input will shape the future of this tool and guide us on where to take it next.

