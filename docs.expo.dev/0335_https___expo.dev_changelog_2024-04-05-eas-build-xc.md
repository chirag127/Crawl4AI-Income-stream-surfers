---
url: https://expo.dev/changelog/2024-04-05-eas-build-xcode-15.3-image
title: https://expo.dev/changelog/2024-04-05-eas-build-xcode-15.3-image
date: 2025-04-30T17:18:58.328125
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [Xcode 15.3 image is now available on EAS Build](https://expo.dev/changelog/2024-04-05-eas-build-xcode-15.3-image)
Apr 5, 2024 by
Szymon Dziedzic
Xcode 15.3 is now available on EAS Build. You can start using it today by setting your [iOS image](https://docs.expo.dev/eas/json/#image-1) in **eas.json** to `"image": "latest"` or `"image": "macos-sonoma-14.3-xcode-15.3"`.
Note that `"latest"` is an alias that points to the most recently added image. If you are reading this post long after the publication date, it may point to a different image.
[Refer to the build image documentation for more information.](https://docs.expo.dev/build-reference/infrastructure/)
Updated **eas.json** file that explicitly opts into using Xcode 15.3.
Xcode 15.3 includes SDKs for iOS 17.4, iPadOS 17.4, tvOS 17.4, watchOS 10.4, macOS Sonoma 14.4, and visionOS 1.1. To learn more about the changes introduced in Xcode 15.3 check [Apple’s official release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-15_3-release-notes).
If you want to check the full specification of the new image visit [our infrastructure docs](https://docs.expo.dev/build-reference/infrastructure/#macos-sonoma-144-xcode-153-latest) or check the logs of the `Spin up build environment` build phase when running a build using the new image.

