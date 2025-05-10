---
url: https://docs.expo.dev/eas-update/expo-dev-client
title: https://docs.expo.dev/eas-update/expo-dev-client
date: 2025-04-30T17:13:13.143277
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Preview updates in development builds
Learn how to use the expo-dev-client library to preview a published EAS Update inside a development build.
[`expo-dev-client`](https://docs.expo.dev/develop/development-builds/introduction) library allows launching different versions of a project by creating a development build. Any compatible EAS Update can be previewed in a development build.
This guide walks through the steps required to load and preview a published update inside a development build using the Extensions tab or constructing a specific Update URL.
## Prerequisites
  * [Create a development build and install it](https://docs.expo.dev/develop/development-builds/create-a-build) on your device or Android Emulator or iOS Simulator.
  * Make sure your development build has the [`expo-updates` library installed](https://docs.expo.dev/eas-update/getting-started#configure-your-project).


## What is an Extensions tab
When using the `expo-updates` library inside a development build, the Extensions tab provides the ability to load and preview a published update automatically.
### Preview an update using the Extensions tab
1
Make non-native changes locally in your project and then [publish them using `eas update`](https://docs.expo.dev/eas-update/getting-started#publish-an-update). The update will be published on a branch.
2
After publishing the update, open your development build, go to Extensions, and tap Login to log in to your Expo account within the development build. This step is required for the Extensions tab to load any published updates associated with the project under your Expo account.
3
After logging in, an EAS Update section will appear inside the Extensions tab with one or more of the latest published updates. Tap Open next to the update you want to preview.
In the Extensions tab, you can view the list of all published updates for a branch. Tap the branch name in the Extensions tab.
## Preview an update using the Expo dashboard
You can also preview an update using the Expo dashboard by following the steps below:
  * Click the published updated link in the CLI after running the command to publish an update. This will open the update's details on the Updates page in the Expo dashboard.
  * Click Preview. This will open the Preview dialog.
  * To preview the update, you can either scan the QR code with your device's camera or select a platform to [launch the update under Open with Orbit](https://docs.expo.dev/review/with-orbit).


## Construct an update URL
As an alternative to the methods described in the previous sections, you can construct a specific URL to open your EAS Update in the development build. The URL will look like the following:
```
[slug]://expo-development-client/?url=[https://u.expo.dev/project-id]/group/[group-id]
# Example
my-app://expo-development-client/?url=https://u.expo.dev/675cb1f0-fa3c-11e8-ac99-6374d9643cb2/group/47839bf2-9e01-467b-9378-4a978604ab11

```

Let's break this URL to understand what each part does:
Part of URL| Description  
---|---  
`slug`| The project's [slug](https://docs.expo.dev/versions/latest/config/app#slug) found in the app config.  
`://expo-development-client/`| Necessary for the deep link to work with the [`expo-dev-client`](https://docs.expo.dev/versions/latest/sdk/dev-client) library.  
`?url=`| Defines a `url` query parameter.  
`https://u.expo.dev/675cb1f0-fa3c-11e8-ac99-6374d9643cb2`| This is the updates URL, which is inside the project's app config under [`updates.url`](https://docs.expo.dev/versions/latest/config/app#url).  
`/group/47839bf2-9e01-467b-9378-4a978604ab11`| The group ID of the update.  
Once you've constructed the URL, copy and paste it directly into the development build's launcher screen under Enter URL Manually.
Alternatively, you can [create a QR code for the URL](https://docs.expo.dev/more/qr-codes) and scan it using your device's camera. When scanned, the URL will open up the development build to the specified channel.
## Example
[See a working exampleSee a working example of using `expo-dev-client` with EAS Update.](https://github.com/jonsamp/test-expo-dev-client-eas-update)

