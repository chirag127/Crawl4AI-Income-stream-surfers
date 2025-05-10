---
url: https://expo.dev/blog/apple-sdk-minimum-requirements
title: https://expo.dev/blog/apple-sdk-minimum-requirements
date: 2025-04-30T17:18:15.267166
depth: 2
---

[All Posts](https://expo.dev/blog)
Share this post
# Apple SDK minimum requirements
Product•April 25, 2025•1 minute read
Beto Moedano
Engineering
As of April 24, 2025, Apple requires that applications uploaded to App Store Connect be built with Xcode 16 or later using the iOS 18 SDK
## [What does this mean? ](https://expo.dev/blog/apple-sdk-minimum-requirements#what-does-this-mean)
If you build your Expo app with Xcode version lower than 16.0, Apple will not allow you to submit your application to the store. You'll receive an email like this:
> **ITMS-90725: SDK version issue** This app was built with the iOS 17.2 SDK. Starting April 24, 2025, all iOS and iPadOS apps must be built with the iOS 18 SDK or later, included in Xcode 16 or later, in order to be uploaded to App Store Connect or submitted for distribution.
## [Solution ](https://expo.dev/blog/apple-sdk-minimum-requirements#solution)
Use Xcode version 16 or later to build your app. Expo apps using SDKs 50, 51, 52, and 53 (latest) can be built with Xcode 16 or later.
**Note:** If you’re using SDK 52 or later, no action is needed—EAS Build will default to Xcode 16. If you’re using SDK 51 or earlier, we strongly recommend upgrading to SDK 52 or higher.
### [Using Xcode 16 with EAS Build ](https://expo.dev/blog/apple-sdk-minimum-requirements#using-xcode-16-with-eas-build)
To use Xcode 16 or later to build your app, set the [build image](https://docs.expo.dev/eas/json/#image-1) in your [build profile](https://docs.expo.dev/build/eas-json/#build-profiles) to use an [iOS server image](https://docs.expo.dev/build-reference/infrastructure/#ios-server-images) with Xcode version 16 or later. See [Xcode versions supported by EAS Build](https://docs.expo.dev/build-reference/infrastructure/#ios-server-images) for a full list of supported Xcode versions.
eas.json
Copy
```

"cli":{
"version":">= 7.3.0"
},
"build":{
"production":{
"ios":{
"image":"macos-sequoia-15.3-xcode-16.2"

```

#### Table of Contents
[What does this mean?](https://expo.dev/blog/apple-sdk-minimum-requirements#what-does-this-mean)[Solution](https://expo.dev/blog/apple-sdk-minimum-requirements#solution)[Using Xcode 16 with EAS Build](https://expo.dev/blog/apple-sdk-minimum-requirements#using-xcode-16-with-eas-build)
Share this post
### Sign up for the Expo Newsletter
Sign up to receive a summary of new features, capabilities, content, and news about Expo and the React Native community.
### Dive in, and create your first Expo project
[Learn More](https://docs.expo.dev)

