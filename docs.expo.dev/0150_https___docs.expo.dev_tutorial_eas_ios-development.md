---
url: https://docs.expo.dev/tutorial/eas/ios-development-build-for-simulators
title: https://docs.expo.dev/tutorial/eas/ios-development-build-for-simulators
date: 2025-04-30T17:14:44.712541
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Create and run a cloud build for iOS Simulator
Learn how to configure a development build for iOS Simulators using EAS Build.
In this chapter, we'll create a development build that can run on an iOS Simulator with EAS Build.
Development builds for iOS Simulators are generated in the .app format which is different from iOS devices.
[Watch: Creating a development build for iOS Simulator](https://www.youtube.com/watch?v=SgL97PFZctg)
## Create a simulator build profile in eas.json
In eas.json, add a new build profile called `ios-simulator` with the property [`ios.simulator`](https://docs.expo.dev/eas/json#simulator) property. Set its value `true`:
eas.json
Copy
```
{
 "build": {
  "development": {
   %%placeholder-start%%... %%placeholder-end%%
  },
  "ios-simulator": {
   "ios": {
    "simulator": true
   }
  }
 }
}

```

For a development build, it's necessary to have the `developmentClient` and `distribution` properties defined in the profile. To avoid redundancy, we can extend the `development` profile properties:
eas.json
Copy
```
{
 "ios-simulator": {
  "extends": "development",
  "ios": {
   "simulator": true
  }
 }
}

```

## Development build for iOS Simulator
1
### Create
Run the `eas build` command with `ios` as a platform and `ios-simulator` as the build profile:
Terminal
Copy
`- ``eas build --platform ios --profile ios-simulator`
This command prompts us with the following questions when we create the build for the first time:
  * What would you like your iOS bundle identifier to be? Press `return` to select the default value provided for this prompt. This will add [`ios.bundleIdentifier`](https://docs.expo.dev/versions/latest/config/app#package) in app.json.


After responding to the prompts, our EAS Build is queued, and the EAS CLI provides a link to view build details and track progress on the Expo dashboard:
What does a build details page contain?
The build details page displays the build type, profile, Expo SDK version, app version, build number, last commit hash, and the identity of the developer or account owner who initiated the build.
In the above image, the current status of the Build artifact shows that the build is in progress. Upon completion, this section will offer an option to download the build. The Logs outlines every step taken during the iOS build process on EAS Build. For the sake of brevity, we won't explore each step in detail here. To learn more, see [iOS build process](https://docs.expo.dev/build-reference/ios-builds).
What is iOS bundle identifier?
The `ios.bundleIdentifier` is a unique name of our app. If we publish our app right now, the Apple App Store will use this property and its value to identify our app on the store.
This notation is defined as `host.owner.app-name`. For example, our example app has `com.owner.stickersmash` where `com.owner` is the domain and `stickersmash` is our app name.
2
### Install
In the terminal, once the build finishes, EAS CLI prompts us by asking whether we want to run the build on an iOS Simulator. Press `Y`.
Alternate: Use Expo Orbit
You can use [Expo Orbit](https://expo.dev/orbit) to install the development build. From Build artifact on the Expo dashboard, click Open with Expo Orbit to install the development build on the iOS Simulator.
3
### Run
Start the development server by running the `npx expo start` command from the project directory:
Terminal
Copy
`- ``npx expo start`
Press `i` in the terminal window to open the project on the iOS Simulator.
## Summary
Chapter 3: Create and run a cloud build for iOS Simulator
We successfully used EAS Build to create and run development builds on iOS Simulators.
Mark this chapter as read
In the next chapter, let's create a development build for iOS, install it on a device, and get it running.
[Next: Create and run a cloud build for iOS device](https://docs.expo.dev/tutorial/eas/ios-development-build-for-devices)

