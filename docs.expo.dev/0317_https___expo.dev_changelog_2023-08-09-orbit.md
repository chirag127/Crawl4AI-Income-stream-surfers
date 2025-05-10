---
url: https://expo.dev/changelog/2023-08-09-orbit
title: https://expo.dev/changelog/2023-08-09-orbit
date: 2025-04-30T17:18:38.397707
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [Expo Orbit: Download and launch builds](https://expo.dev/changelog/2023-08-09-orbit)
Aug 9, 2023 by
Gabriel Donadel
To make your development workflow even faster, we are experimenting with a menu bar app that can launch builds and run Snack projects on your devices and simulators. It's called Expo Orbit. It's a macOS menu bar app that allows you to:
  * Install and launch builds from EAS with just one click
  * Launch Snack projects in your simulators with a link
  * List and launch Android emulators and iOS simulators
  * Install and launch apps from local files


[Download Orbit](https://github.com/expo/orbit/releases) and enable the Orbit experiment by going to [settings](https://expo.dev/settings) and turning on the "Expo Orbit" experiment under the **Experiments** section. Note: Orbit relies on `xcrun` and the Android SDK for device management, which requires having both Android Studio and Xcode set up.
We can't wait for you to try Orbit, explore its capabilities, and hear your feedback (orbit@expo.dev). Your input will shape the future of this tool and guide us on where to take it next.
A big part of the inspiration for this project came from the fantastic work of Shopify, with their internal tool "Tophat". We learned about it through [this post](https://shopify.engineering/shopify-tophat-mobile-developer-testing) in their blog, and the team was kind enough to jump on a call and chat with us about how they built it.
Another great open source macOS menu bar utility for launching iOS/Android simulators/emulators in a similar way to Tophat/Orbit is [MiniSim](https://github.com/okwasniewski/MiniSim) from [Oskar Kwaśniewski](https://twitter.com/o_kwasniewski).

