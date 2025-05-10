---
url: https://expo.dev/changelog/2024-03-29-eas-build-upcoming-ios-images-updates
title: https://expo.dev/changelog/2024-03-29-eas-build-upcoming-ios-images-updates
date: 2025-04-30T17:19:00.762839
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [EAS Build: Upcoming iOS images updates](https://expo.dev/changelog/2024-03-29-eas-build-upcoming-ios-images-updates)
Mar 29, 2024 by
Szymon Dziedzic
[Starting on April 29th, 2024, apps uploaded to App Store Connect must be built with Xcode 15 for iOS 17, iPadOS 17, tvOS 17, or watchOS 10](https://developer.apple.com/news/?id=fxu2qp7b). To ensure that your builds are compatible with the upcoming requirements, you can opt-in to use the Xcode 15 for your iOS builds by specifying [`"image": "macos-sonoma-14.4-xcode-15.3"`](https://docs.expo.dev/build-reference/infrastructure/#macos-sonoma-144-xcode-153-latest) or [`"image": "latest"`](https://docs.expo.dev/build-reference/infrastructure/#configuring-build-environment) in your [**eas.json**](https://docs.expo.dev/eas/json/#image-1) [configuration file](https://docs.expo.dev/eas/json/#image-1).
Note that `"latest"` is an alias that points to the most recently added image. If you are reading this post long after the publication date, it may point to a different image.
[Refer to the build image documentation for more information.](https://docs.expo.dev/build-reference/infrastructure/)
Following Apple's announcement we are planning to drop the support for all of the iOS images with Xcode < 15 a month after the required Xcode version changes on Apple's side. This means that starting on May 29th, 2024, we will no longer provide the following images:
  * `macos-monterey-12.1-xcode-13.2`
  * `macos-monterey-12.3-xcode-13.3`
  * `macos-monterey-12.4-xcode-13.4`
  * `macos-monterey-12.6-xcode-14.0`
  * `macos-monterey-12.6-xcode-14.1`
  * `macos-monterey-12.6-xcode-14.2`
  * `macos-ventura-13.3-xcode-14.3`
  * `macos-ventura-13.4-xcode-14.3.1`


If you are using one of the images listed above, we recommend updating your configuration to use Xcode 15 as soon as possible to avoid any disruptions in your build process.

