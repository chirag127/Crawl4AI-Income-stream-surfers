---
url: https://docs.expo.dev/eas/workflows/examples
title: https://docs.expo.dev/eas/workflows/examples
date: 2025-04-30T17:13:38.633056
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Example CI/CD workflows
Common CI/CD workflows that are useful for your project.
The following workflows are examples of how you can use EAS Workflows to automate your development and release processes. They can help you and your team develop, review each other's PRs, and release changes to your users.
## Development builds workflow
[Development builds](https://docs.expo.dev/develop/development-builds/introduction) are specialized builds of your project that include Expo's developer tools. These types of builds include all native dependencies inside your project, enabling you to run a production-like build of your project on a simulator, emulator, or a physical device.
Prerequisites
2 requirements
1.
Set up your environment
To get started, you'll need to configure your project and devices to build and run development builds. Learn how to set up your environment for development builds with the following guides:
[Android device setupGet your project ready for development builds.](https://docs.expo.dev/get-started/set-up-your-environment?mode=development-build&platform=android&device=physical)[Android Emulator setupGet your project ready for development builds.](https://docs.expo.dev/get-started/set-up-your-environment?mode=development-build&platform=android&device=simulated)[iOS device setupGet your project ready for development builds.](https://docs.expo.dev/get-started/set-up-your-environment?mode=development-build&platform=ios&device=physical)[iOS Simulator setupGet your project ready for development builds.](https://docs.expo.dev/get-started/set-up-your-environment?mode=development-build&platform=ios&device=simulated)
2.
Create build profiles
After you've configured your project and devices, add the following build profiles to your eas.json file.
eas.json
Copy
```
{
 "build": {
  "development": {
   "developmentClient": true,
   "distribution": "internal"
  },
  "development-simulator": {
   "developmentClient": true,
   "distribution": "internal",
   "ios": {
    "simulator": true
   }
  }
 }
}

```

The following workflow creates a build for each platform and for both physical devices, Android emulators, and iOS simulators. They all will run in parallel.
.eas/workflows/create-development-builds.yml
Copy
```
name: Create development builds
jobs:
 android_development_build:
  name: Build Android
  type: build
  params:
   platform: android
   profile: development
 ios_device_development_build:
  name: Build iOS device
  type: build
  params:
   platform: ios
   profile: development
 ios_simulator_development_build:
  name: Build iOS simulator
  type: build
  params:
   platform: ios
   profile: development-simulator

Show More

```

Run the above workflow with:
Terminal
Copy
`- ``eas workflow:run .eas/workflows/create-development-builds.yml`
## Preview updates workflow
Once you've made changes to your project, you can share a preview of your changes with your team by publishing a [preview update](https://docs.expo.dev/review/share-previews-with-your-team).
You can access preview updates in the development build UI and through scannable QR codes on the Expo dashboard. When publishing a preview on every commit, your team can review changes without pulling the latest changes and running them locally.
Prerequisites
2 requirements
1.
Set up EAS Update
Your project needs to have [EAS Update](https://docs.expo.dev/eas-update/introduction) setup to publish preview updates. You can set up your project with:
Terminal
Copy
`- ``eas update:configure`
2.
Create new development builds
After you've configured your project, create new [development builds](https://docs.expo.dev/develop/development-builds/create-a-build) for each platform.
The following workflow publishes a preview update for every commit on every branch.
.eas/workflows/publish-preview-update.yml
Copy
```
name: Publish preview update
on:
 push:
  branches: ['*']
jobs:
 publish_preview_update:
  name: Publish preview update
  type: update
  params:
   branch: ${{ github.ref_name || 'test' }}

```

## Deploy to production workflow
When you're ready to deliver changes to your users, you can build and submit to the app stores or you can send an over-the-air update. The following workflow detects if you need new builds, and if so, it sends them to the app stores. If new builds are not required, it will send an over-the-air update.
Prerequisites
3 requirements
1.
Set up EAS Build
To set up EAS Build, follow this guide:
[EAS Build prerequisitesGet your project ready for EAS Build.](https://docs.expo.dev/build/setup)
2.
Set up EAS Submit
To set up EAS Submit, follow the Google Play Store and Apple App Store submissions guides:
[Google Play Store CI/CD submission guideGet your project ready for Google Play Store submissions.](https://docs.expo.dev/submit/android#submitting-your-app-using-cicd-services)[Apple App Store CI/CD submission guideGet your project ready for Apple App Store submissions.](https://docs.expo.dev/submit/ios#submitting-your-app-using-cicd-services)
3.
Set up EAS Update
And finally, you'll need to set up EAS Update, which you can do with:
Terminal
Copy
`- ``eas update:configure`
The following workflow runs on each push to the `main` branch and performs the following:
  * Takes a hash of the native characteristics of the project using [Expo Fingerprint](https://docs.expo.dev/versions/latest/sdk/fingerprint).
  * Checks if a build already exists for the fingerprint.
  * If a build does not exist, it will build the project and submit it to the app stores.
  * If a build exists, it will send an over-the-air update.


.eas/workflows/deploy-to-production.yml
Copy
```
name: Deploy to production
on:
 push:
  branches: ['main']
jobs:
 fingerprint:
  name: Fingerprint
  type: fingerprint
 get_android_build:
  name: Check for existing android build
  needs: [fingerprint]
  type: get-build
  params:
   fingerprint_hash: ${{ needs.fingerprint.outputs.android_fingerprint_hash }}
   profile: production
 get_ios_build:
  name: Check for existing ios build
  needs: [fingerprint]
  type: get-build
  params:
   fingerprint_hash: ${{ needs.fingerprint.outputs.ios_fingerprint_hash }}
   profile: production
 build_android:
  name: Build Android
  needs: [get_android_build]
  if: ${{ !needs.get_android_build.outputs.build_id }}
  type: build
  params:
   platform: android
   profile: production
 build_ios:
  name: Build iOS
  needs: [get_ios_build]
  if: ${{ !needs.get_ios_build.outputs.build_id }}
  type: build
  params:
   platform: ios
   profile: production
 submit_android_build:
  name: Submit Android Build
  needs: [build_android]
  type: submit
  params:
   build_id: ${{ needs.build_android.outputs.build_id }}
 submit_ios_build:
  name: Submit iOS Build
  needs: [build_ios]
  type: submit
  params:
   build_id: ${{ needs.build_ios.outputs.build_id }}
 publish_android_update:
  name: Publish Android update
  needs: [get_android_build]
  if: ${{ needs.get_android_build.outputs.build_id }}
  type: update
  params:
   branch: production
   platform: android
 publish_ios_update:
  name: Publish iOS update
  needs: [get_ios_build]
  if: ${{ needs.get_ios_build.outputs.build_id }}
  type: update
  params:
   branch: production
   platform: ios

Show More

```


