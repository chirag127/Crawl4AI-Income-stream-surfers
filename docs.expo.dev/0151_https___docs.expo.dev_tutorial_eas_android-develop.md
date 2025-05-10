---
url: https://docs.expo.dev/tutorial/eas/android-development-build
title: https://docs.expo.dev/tutorial/eas/android-development-build
date: 2025-04-30T17:14:44.714711
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Create and run a cloud build for Android
Learn how to configure a development build for Android devices and emulators using EAS Build.
In this chapter, we'll create a development build that can run on Android with EAS Build.
The process for creating and running a build on Android devices or emulators is identical, with differences only in the installation of the development build.
[Watch: How to create and run a cloud build for Android](https://www.youtube.com/watch?v=D612BUtvvl8)
## Create a build for the development profile
For Android, the development build must be in the .apk. While the default Android format is .aab, which is ideal for Google Play Store distribution, it cannot be installed on devices or emulators.
To create a .apk:
  * In eas.json, make sure that `developmentClient` is set to `true` under `build.development` profile.
  * Then, run the `eas build` command with `android` as the platform and `development` as the build profile:
Terminal
Copy
`- ``eas build --platform android --profile development`
> Tip: Next time you run `eas build` command, you can also use `-p` to specify the platform. It is short for `--platform`.


This command prompts us with the following questions:
  * What would you like your Android application id to be? Press `return` to select the default value provided for this prompt. This will add [`android.package`](https://docs.expo.dev/versions/latest/config/app#package) in app.json.
  * Generate a new Android Keystore? Press `Y`.


After responding, the build will queue up, and we can track its progress via a provided link by the EAS CLI in the Expo dashboard:
What information does a build details page contain?
The build details page displays the build type, profile, Expo SDK version, app version, version code, last commit hash, and the identity of the developer or account owner who initiated the build.
In the above image, the current status of the Build artifact shows that the build is in progress. Upon completion, this section will offer an option to download the build. The Logs outlines every step taken during the Android build process on EAS Build. For the sake of brevity, we won't explore each step in detail here. To learn more, see [Android build process](https://docs.expo.dev/build-reference/android-builds).
What is an Android application ID?
Also known as the package name of our Android app, it stores the value in DNS reverse notation format (`com.owner.appname`). Each component of this notation should start with a lowercase letter.
For example, our example app has `com.owner.stickersmash` where `com.owner` is the domain and `stickersmash` is our app name.
## Android device
1
### Install development build
Once the build finishes, the Build artifact section gets updated, indicating that the build is complete:
This section provides the methods available for running the development build on an Android device: Expo Orbit and Install button.
[Expo Orbit](https://expo.dev/orbit) allows for seamless installation of the development build on an Android device. To use this method:
  * Connect our Android device to our local machine using USB.
  * Open the Orbit menu bar app.
  * Select the Device in the Orbit app.


  * On the Expo dashboard, under Build artifact, click the Open with Orbit.


After the build is installed, the Orbit app launches the development build on the device.
Alternate: Use the Install button and QR code
The Install button in the Build artifact generates a QR code for installation:
  * Click Install to display a popup with the QR code.


  * Scan the QR code with our Android device's camera to open the build link in the default web browser.
  * Tap the Install button on the webpage to download the .apk file.
  * Once downloaded, open the .apk to start the installation process.
  * If an Unsafe app blocked message appears, select Install anyway. This warning can safely be ignored as the source of the .apk (which we generated) is trusted.


2
### Run development build
Start the development server by running `npx expo start` from the project directory. Once the server is running, press `a` in the terminal window to open the project:
Terminal
Copy
`- ``npx expo start`
## Android Emulator
1
### Install the development build
In the terminal, once the build finishes, EAS CLI prompts us by asking whether we want to run the build on an Android Emulator. Press `Y`.
Alternate: Use Expo Orbit
Alternatively, [Expo Orbit](https://docs.expo.dev/build/orbit) can be used for installation. From Build artifact on the Expo dashboard, click Open with Expo Orbit to install the development build on the Android Emulator.
2
### Run the development build
Start the development server by running `npx expo start` from the project directory. Once the server is running, press `a` in the terminal window to open the project:
Terminal
Copy
`- ``npx expo start`
## Summary
Chapter 2: Create and run a cloud build for Android
We successfully used EAS Build to create and run development builds on Android devices and emulators, and learned about .apk and .aab file formats.
Mark this chapter as read
In the next chapter, learn how to configure a development build for iOS Simulators using EAS Build and get it running.
[Next: Create and run a cloud build for iOS Simulator](https://docs.expo.dev/tutorial/eas/ios-development-build-for-simulators)

