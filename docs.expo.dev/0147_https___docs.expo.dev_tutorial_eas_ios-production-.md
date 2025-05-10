---
url: https://docs.expo.dev/tutorial/eas/ios-production-build
title: https://docs.expo.dev/tutorial/eas/ios-production-build
date: 2025-04-30T17:14:37.430437
depth: 2
---

Search
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Create a production build for iOS
Learn about the process of creating a production build for iOS and automating the release process.
In this chapter, we'll create our example app's production version and submit it for testing using TestFlight. After that, we'll submit them for App Store review to get it on the App Store.
[Watch: Creating and releasing a production build for iOS](https://www.youtube.com/watch?v=VZL_e0cEwo8)
## Prerequisites
To publish and distribute an app on the Apple Play Store, we need:
  * Apple Developer account: To create one, see [Apple Developer Portal](https://developer.apple.com/account/).
  * Production build profile: Ensure that a `production` build profile is present in your eas.json, which is added by default.


## Production build for iOS
A [production iOS build](https://docs.expo.dev/build/eas-json#production-builds) is optimized for Apple's App Store Connect, which allows distributing builds to testers with TestFlight and public end users through the App Store. This build type cannot be side-loaded on a simulator or device and can only be distributed through App Store Connect.
1
## Create a distribution provisioning profile
Run the `eas credentials` command in the terminal and then answer the following prompts by EAS CLI:
  * Select platform iOS.
  * Which build profile do you want to configure? Select production.
  * Do you want to log in to your Apple account? Press `Y`. This will log in to our Apple Developer account.
  * What do you want to do? Select Build credentials and choose All: Set up all the required credentials to build your project.
  * Now, it will prompt whether we want to re-use the previous Distribution Certificate. Press `Y`.
  * Generate a new Apple Provisioning Profile? Press `Y`. This will be the provisioning profile for the production app.
  * Once the profiles are created, press any `ctrl` + `c` to exit the EAS CLI.


2
## Create a production build
To create an iOS production build using the default `production` profile, open your terminal and execute the following command. Since `production` is set as the default profile in the EAS configuration, there is no need to specify it explicitly with the `--profile` flag.
Terminal
Copy
`- ``eas build --platform ios`
The command will queue the build. Notice on the Expo dashboard that the Build Number is auto-incremented.
3
## Submit the app binary to the App Store
To submit the app binary created from our latest EAS Build, run the [`eas submit`](https://docs.expo.dev/submit/introduction) command:
Terminal
Copy
`- ``eas submit --platform ios`
After running this command, we need to:
  * Select a build from EAS. Let's select the latest build ID.
  * Follow the prompt to log in to our Apple account. When it asks for Reuse this App Store Connect API Key? Press `Y`.


This will trigger the submission process.
4
## Release an internal testing version
After the submission process is complete, we'll need to log in to the Apple Developer account from the web browser.
  * Click and see the app icon.
  * Click the app name, and from the navigation tab menu, click TestFlight. If the build was just submitted, it may take a few minutes for Apple to process the build before it is available to distribute with TestFlight.
  * Click on the Manage Compliance link. Since our app doesn't use any encryption, select None of the algorithms mentioned above.


> Tip: Next time when creating an app, skip this compliance by adding [`ios.config.usesNonExemptEncryption`](https://docs.expo.dev/versions/latest/config/app#usesnonexemptencryption) in app config and set it to `false` if the app doesn't use any encryption.
  * In App Store Connect, under Internal Testing, and create a test group. This will allow us to invite test users.


  * Once the group is created, an email will be sent to all the test users.


  * In the email, click View in TestFlight, accept the invite, and then tap Install.


After that, the app will download on our device so that we can test it.
> Note: Similar to internal testing, we can also create a group for inviting external testers using TestFlight. Where internal testing has a limit of 100 users, TestFlight allows sharing a test release version externally with up to 10,000 testers and provides a publicly shareable link. For brevity, we are not going to cover those steps in this tutorial.
5
## Submit the app to the Apple App Store
To prepare our app for App Store submission, go to the App Store tab:
  * Provide metadata details, provide screenshots as per Apple's guidelines and also fill details under General.


  * Then, manually select the build.


> Complete App Store listing: To prepare the app for store listing, see [Create app store assets](https://docs.expo.dev/guides/store-assets) on how to create screenshots and previews.
  * Once our app is ready, click on Submit to App Review. After that, Apple will review our app, and if approved, the app will be available on the App Store.


6
## Automated submissions
For future releases, we can streamline the process by combining build creation and App Store submission into a single step by using the [`--auto-submit`](https://docs.expo.dev/build/automate-submissions) flag with `eas build`:
Terminal
Copy
`- ``eas build --platform ios --auto-submit`
## Summary
Chapter 9: Create a production build for iOS
We successfully created a production-ready iOS build, discussed distribution using TestFlight and Apple App Store using `eas submit`, and automated the release process with the `--auto-submit`.
Mark this chapter as read
In the next chapter, learn how to use the EAS Update to send OTA updates and share previews with our team.
[Next: Share previews with your team](https://docs.expo.dev/tutorial/eas/team-development)

