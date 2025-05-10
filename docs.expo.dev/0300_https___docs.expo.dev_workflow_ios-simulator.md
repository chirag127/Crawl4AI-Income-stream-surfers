---
url: https://docs.expo.dev/workflow/ios-simulator
title: https://docs.expo.dev/workflow/ios-simulator
date: 2025-04-30T17:18:15.249145
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# iOS Simulator
Learn how you can install the iOS Simulator on your Mac and use it to develop your app.
Developing your app directly on a computer can be more convenient than constantly interacting with an iPhone or iPad, especially when network conditions are slow or when a [tunnel connection](https://docs.expo.dev/more/expo-cli#tunneling) is required due to LAN limitations.
This guide explains how to install the iOS Simulator on your Mac for app development. Note that the iOS Simulator can only be installed on macOS. If you are developing an iOS app from a Windows or a Linux machine, you will need a physical iOS device.
## Setup Xcode and Watchman
1
### Install Xcode
Open up the Mac App Store, search for [Xcode](https://apps.apple.com/us/app/xcode/id497799835), and click Install (or Update if you have it already).
2
### Install Xcode Command Line Tools
Open Xcode, choose Settings... from the Xcode menu (or press `cmd ⌘` + `,`). Go to the Locations and install the tools by selecting the most recent version in the Command Line Tools dropdown.
3
### Install an iOS Simulator in Xcode
To install an iOS Simulator, open Xcode > Settings... > Components, and under Platform Support > iOS ..., click Get.
4
### Install Watchman
[Watchman](https://facebook.github.io/watchman/docs/install#macos) is a tool for watching changes in the filesystem. Installing it will result in better performance. You can install it with:
Terminal
Copy
`- ``brew update`
`- ``brew install watchman`
4
### Try it out
Run your app with `npx expo start` and press `i` from the command line.
You may get a warning about needing to accept the Xcode license. Run the command that it suggests. Open your app again to see if it was successful. If not, check the [troubleshooting](https://docs.expo.dev/workflow/ios-simulator#troubleshooting) tips below.
You can also press `shift` + `i` in the Expo CLI to interactively select a simulator to open.
## Expo Orbit
You can use the Expo Orbit app which allows launching builds and simulator management with one click from the menu bar on macOS.
[Use Expo OrbitLearn more about how to use Expo Orbit.](https://docs.expo.dev/build/orbit)
## Limitations
Although the iOS Simulator is great for rapid development, it does come with a few limitations. We'll list out a few of the main differences that affect Expo APIs below. However, see [Apple's documentation](https://help.apple.com/simulator/mac/current/#/devb0244142d) for more details.
The following hardware is unavailable in the Simulator:
  * Audio Input
  * Barometer
  * Camera
  * Motion Support (accelerometer and gyroscope)


The Simulator also suspends background apps and processes on iOS 11 and later.
## Troubleshooting
### The CLI seems to be stuck when opening a Simulator
Sometimes the iOS Simulator doesn't respond to the open command. If it seems stuck on this prompt, you can open the iOS Simulator manually (`open -a Simulator`) and then in the macOS toolbar, choose File > Open Simulator, and select an iOS version and device that you'd like to open.
You can use this menu to open any version of the simulator. You can also open multiple simulators at the same time, however, Expo CLI will always target the most recently opened simulator.
### Simulator opened but the Expo Go app isn't opening inside of it
The first time you install the app in the simulator, iOS will ask if you'd like to open the Expo Go app. You may need to interact with the simulator (click around, drag something) for this prompt to show up, then press OK.
### How do I force an update to the latest version?
Create a project with the desired SDK version and open it in a simulator to install a particular version of Expo Go.
Terminal
`# Bootstrap an SDK 51 project`
`- ``npx create-expo-app --template blank@51`
`# Open the app on a simulator to install the required Expo Go app`
`- ``npx expo start --ios`
### Expo CLI is printing an error message about `xcrun`, what do I do?
For miscellaneous errors, try the following:
  * Manually uninstall Expo Go on your simulator and reinstall by pressing `shift` + `i` in the Expo CLI Terminal UI and selecting the desired simulator.
  * If that doesn't help, focus the simulator window and in the Mac toolbar choose Device > Erase All Content and Settings... This will reinitialize your simulator from a blank image. This is sometimes useful for cases where your computer is low on memory and the simulator fails to store some internal files, leaving the device in a corrupt state.



