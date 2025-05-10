---
url: https://expo.dev/changelog/2023-12-19-eas-build-xcode-15.1-image
title: https://expo.dev/changelog/2023-12-19-eas-build-xcode-15.1-image
date: 2025-04-30T17:18:58.348606
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [Xcode 15.1 image is now available on EAS Build](https://expo.dev/changelog/2023-12-19-eas-build-xcode-15.1-image)
Dec 19, 2023 by
Szymon Dziedzic
Xcode 15.1 is now available on EAS Build. You can start using it today by setting your [iOS image](https://docs.expo.dev/eas/json/#image-1) in **eas.json** to `"image": "latest"` or `"image": "macos-ventura-13.6-xcode-15.1"`.
Note that `"latest"` is an alias that points to the most recently added image. If you are reading this post long after the publication date, it may point to a different image.
[Refer to the build image documentation for more information](https://docs.expo.dev/build-reference/infrastructure/).
The primary focus of this update is on bug fixes. To learn more about the changes introduced in Xcode 15.1 check [Apple’s official release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-15_1-release-notes).
If you want to check the full specification of the new image visit [our infrastructure docs](https://docs.expo.dev/build-reference/infrastructure/#macos-ventura-136-xcode-151-latest) or check the logs of the `Spin up build environment` build phase when running a build using the new image.

