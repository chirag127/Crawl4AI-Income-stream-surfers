---
url: https://expo.dev/changelog/2024-07-12-eas-build-upcoming-android-images-updates
title: https://expo.dev/changelog/2024-07-12-eas-build-upcoming-android-images-updates
date: 2025-04-30T17:19:00.779339
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [EAS Build: Upcoming Android images updates](https://expo.dev/changelog/2024-07-12-eas-build-upcoming-android-images-updates)
Jul 12, 2024 by
Szymon Dziedzic
The EAS Build team is continuing image-related maintenance efforts to ensure that the builder VM images are up-to-date and secure. Recently, a new [`ubuntu-22.04-jdk-17-ndk-26b`](https://docs.expo.dev/build-reference/infrastructure/#ubuntu-2204-jdk-17-ndk-r26b-latest-sdk-51) image was added to better support builds using SDK 51.
Additionally, we are dropping support for old Android images running Ubuntu 20.04 or using Java 8. Starting September 1st, 2024, these will no longer be available:
  * `ubuntu-20.04-jdk-8-ndk-r19c`
  * `ubuntu-20.04-jdk-11-ndk-r19c`
  * `ubuntu-20.04-jdk-8-ndk-r21e`
  * `ubuntu-20.04-jdk-11-ndk-r21e`
  * `ubuntu-20.04-jdk-11-ndk-r23b`
  * `ubuntu-22.04-jdk-8-ndk-r21e`


If you are using one of the images listed above in your [**eas.json**](https://docs.expo.dev/eas/json/#image) [configuration file](https://docs.expo.dev/eas/json/#image), we recommend updating your configuration to use [`latest`](https://docs.expo.dev/build-reference/infrastructure/#configuring-build-environment) [and](https://docs.expo.dev/build-reference/infrastructure/#configuring-build-environment) [`auto`](https://docs.expo.dev/build-reference/infrastructure/#configuring-build-environment) tags or [some of the images with newer JDK and Ubuntu versions](https://docs.expo.dev/build-reference/infrastructure/#android-server-images) as soon as possible to avoid any disruptions in your build process.
The `ubuntu-20.04-jdk-8-ndk-r19c` and `ubuntu-20.04-jdk-11-ndk-r19c` images were used by our default [`auto`](https://docs.expo.dev/build-reference/infrastructure/#configuring-build-environment) image resolution logic for Expo SDKs below version 46. The `ubuntu-20.04-jdk-11-ndk-r21e` and `ubuntu-20.04-jdk-8-ndk-r21e` were used for SDKs 46 and 47. All of these resolutions will be updated to use the `ubuntu-22.04-jdk-11-ndk-r21e` image. The resolution logic for newer SDKs will remain unchanged.

