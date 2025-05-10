---
url: https://expo.dev/changelog/2024-01-18-eas-build-xcode-15.2-image
title: https://expo.dev/changelog/2024-01-18-eas-build-xcode-15.2-image
date: 2025-04-30T17:19:00.739551
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [Xcode 15.2 image is now available on EAS Build](https://expo.dev/changelog/2024-01-18-eas-build-xcode-15.2-image)
Jan 18, 2024 by
Szymon Dziedzic
Xcode 15.2 is now available on EAS Build. You can start using it today by setting your [iOS image](https://docs.expo.dev/eas/json/#image-1) in **eas.json** to `"image": "latest"` or `"image": "macos-ventura-13.6-xcode-15.2"`.
Note that `"latest"` is an alias that points to the most recently added image. If you are reading this post long after the publication date, it may point to a different image.
[Refer to the build image documentation for more information](https://docs.expo.dev/build-reference/infrastructure/).
Xcode 15.2 includes SDKs for iOS 17.2, iPadOS 17.2, tvOS 17.2, watchOS 10.2, macOS Sonoma 14.2, and visionOS. The primary focus of this update is on bug fixes. To learn more about the changes introduced in Xcode 15.2 check [Apple’s official release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-15_2-release-notes).
If you want to check the full specification of the new image visit [our infrastructure docs](https://docs.expo.dev/build-reference/infrastructure/#macos-ventura-136-xcode-152-latest) or check the logs of the `Spin up build environment` build phase when running a build using the new image.

