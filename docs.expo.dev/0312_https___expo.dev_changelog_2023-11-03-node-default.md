---
url: https://expo.dev/changelog/2023-11-03-node-default
title: https://expo.dev/changelog/2023-11-03-node-default
date: 2025-04-30T17:18:29.980517
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [EAS Build: Upgrading default Node.js version from 16 to 18 on November 27th, 2023](https://expo.dev/changelog/2023-11-03-node-default)
Nov 3, 2023 by
Brent Vatne
One month ago, on September 11th, Node 16 reached end-of-life and it no longer receives any form of support. For that reason, **effective** **November 27th, 2023** , we will migrate the default Node version from 16 to 18 on all EAS Build images. We have already updated the `latest` image accordingly.
In the process of doing the Node.js upgrade, we will also drop our Ubuntu 18 images, because they do not support Node 18. The lowest available Ubuntu version will be 20.
The default Node version on EAS Build tracks the current maintenance LTS (see: [Node.js releases](https://nodejs.org/en/about/previous-releases)). This is common practice for similar hosted services.
## [What do you need to do? ](https://expo.dev/changelog/2023-11-03-node-default#what-do-you-need-to-do)
**If you aren’t ready to make any changes yet and want to ensure that you remain on Node 16 after the effective date of the upgrade:** you can explicitly lock your builds to Node 16 by adding the following to your build profiles: `"node": "16.18.1"`.
**To prepare your app for the upgrade (recommended)** , you can do the following:
  * **Use Node 18+ locally:** It’s likely that your project already runs on Node 18 or higher — most developers are already using a recent version on their local machines. If not, update to Node 18 or greater on your local development machine, then ensure your dependencies install successfully and your app runs.
  * **Opt in early to Node 18 on EAS Build**
    * Set `"image": "latest"` on your build profiles, or, alternatively, `"node": "18.18.0"` to install Node 18 on your currently used image.
  * **Switch to Ubuntu 20+ for Android builds on EAS Build**
    * Ubuntu 18 is used by default on SDK 45 ([released May 5, 2022](https://blog.expo.dev/expo-sdk-45-f4e332954a68), it includes React Native 0.67) and older, so you are likely already using Ubuntu 20+ for your Android builds — unless you explicitly specify [`ubuntu-18.04-jdk-8-ndk-r19c`](https://docs.expo.dev/build-reference/infrastructure/#ubuntu-1804-jdk-8-ndk-r19c) or [`ubuntu-18.04-jdk-11-ndk-r19c`](https://docs.expo.dev/build-reference/infrastructure/#ubuntu-1804-jdk-11-ndk-r19c) as your build image.
    * If you haven’t specified an image and you want to know which is used for your project: find a recent build and look at the “Spin up build environment phase” - you will find a log similar to `Using image "ubuntu-20.04-jdk-11-ndk-21.4.7075529" based on "ubuntu-2004-focal-v20220823"`.

## [What happens if you don’t take any action? ](https://expo.dev/changelog/2023-11-03-node-default#what-happens-if-you-dont-take-any-action)
Most apps are unlikely to experience any issues as a result of this change; however, in some cases, projects may not build. For example, you may encounter dependencies that are incompatible with Node 18.
To keep your builds green, we encourage developers to either lock down the Node version, or prepare for the change / opt-in early, as suggested above.
**If you are still unsure how to proceed** , we recommend you ask questions in our [💬 Discord community](https://chat.expo.dev/).

