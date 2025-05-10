---
url: https://expo.dev/blog/out-with-the-old-in-with-the-new-architecture
title: https://expo.dev/blog/out-with-the-old-in-with-the-new-architecture
date: 2025-04-30T17:18:15.242050
depth: 2
---

[All Posts](https://expo.dev/blog)
Share this post
# Out with the old, in with the New Architecture (by default)
React Native, Development•April 22, 2025•5 minute read
Brent Vatne
Engineering
In SDK 53, the New Architecture will be enabled by default on all projects. You can still opt out, but the legacy architecture won't be around forever.
In SDK 53 ([currently in beta](https://expo.dev/changelog/sdk-53-beta)), [the New Architecture](https://reactnative.dev/blog/2024/10/23/the-new-architecture-is-here) will be enabled by default on all projects — if you want to continue to use the legacy architecture, you will need to explicitly opt out by setting `"newArchEnabled": false` in your **app.json**. This change is consistent with the behavior of React Native, where the New Architecture is also enabled by default in all projects.
This is the next step in rolling out the New Architecture [as announced in SDK 52](https://expo.dev/changelog/2024-11-12-sdk-52), when the New Architecture was enabled for all new projects created with `create-expo-app` by setting the `"newArchEnabled": true` field in **app.json** automatically. As of the time of writing, the New Architecture was enabled in 74.6% of the SDK 52 projects built on EAS Build in April, 2025.
### [Why migrate? ](https://expo.dev/blog/out-with-the-old-in-with-the-new-architecture#why-migrate)
  * **New React and React Native features are coming to the New Architecture only**. For example, the New Architecture includes [full support for Suspense](https://reactnative.dev/blog/2024/10/23/the-new-architecture-is-here#full-support-for-suspense) and [new styling capabilities are not implemented in the legacy architecture](https://reactnative.dev/blog/2025/01/21/version-0.77#new-css-features-for-better-layouts-sizing-and-blending).
  * **Early adopters ([such as Kraken](https://blog.kraken.com/product/engineering/how-kraken-fixed-performance-issues-via-incremental-adoption-of-the-react-native-new-architecture)) have paved the way** by reporting and fixing bugs in the sprawling ecosystem of libraries. In many cases, the transition to the New Architecture should be mostly straightforward — but this certainly is not true of all apps. The larger your app and the more niche or outdated your dependencies, the more you may have to invest in the migration.
  * **The legacy architecture will not be around forever** — it’s _possible_ that the legacy architecture will be removed from React Native in a late 2025 release. When it is removed, you will not be able to upgrade React Native or the Expo SDK without migrating to the New Architecture. Additionally, libraries like r[eact-native-reanimated](https://github.com/software-mansion/react-native-reanimated) and [@shopify/flash-list](https://github.com/Shopify/flash-list) will only support the New Architecture in upcoming releases, in order to take advantage of new features that enable improved performance and other benefits.

### [Potential blockers to migrating ](https://expo.dev/blog/out-with-the-old-in-with-the-new-architecture#potential-blockers-to-migrating)
Many issues identified during SDK 52 have since been resolved, including a long list of improvements to [react-native-reanimated](https://github.com/software-mansion/react-native-reanimated) and [react-native-screens](https://github.com/software-mansion/react-native-screens) by the maintainers at [Software Mansion](https://swmansion.com/). If you tried migrating to the New Architecture previously and encountered performance issues with your animations, or unexpected quirks with navigation, there is a good chance that those issues have been resolved already or will be soon!
In some cases, you might not be able to fully migrate your app yet. If you use one of the following libraries, you can [opt in to using the legacy architecture](https://docs.expo.dev/guides/new-architecture/#disable-the-new-architecture-in-an-existing-project) if needed.
  * **react-native-maps** : Initial support for the New Architecture is available in version 1.21.0, which is still stabilizing. We encourage your to test it in your app, report issues that you find, and [follow along with the discussion on GitHub](https://github.com/react-native-maps/react-native-maps/discussions/5355). We are also investigating another approach that may provider a smoother migration path, by leaning on the [interop layer](https://github.com/reactwg/react-native-new-architecture/discussions/175) rather than rewriting the module. It’s worth mentioning that if your app can force a minimum version of iOS 18, or does not need to support maps on iOS, then you can consider using [`expo-maps`](https://docs.expo.dev/versions/latest/sdk/maps/) instead.
  * **@stripe/react-native** does not yet support the New Architecture. [Follow along with progress](https://github.com/stripe/stripe-react-native/issues/1275).

### [Found a blocker? ](https://expo.dev/blog/out-with-the-old-in-with-the-new-architecture#found-a-blocker)
**Nearly three out of every four up-to-date apps built on EAS use the New Architecture** , but your app, like you, is one of one — New Architecture support in your app may bring you down some paths that others have yet to encounter.
If you run into any issues that are preventing you from upgrading, [file an issue on GitHub](https://github.com/expo/expo/issues). Be sure to include a minimal reproducible example, this is essential for us to resolve your issue in a timely fashion. We’d encourage you to then temporarily disable that particular code in your app, and push on to see if you discover any other blockers. If you do, report those and repeat. When you’re done, add back your disabled features and [opt in to using the legacy architecture](https://docs.expo.dev/guides/new-architecture/#disable-the-new-architecture-in-an-existing-project).
### [What is next? ](https://expo.dev/blog/out-with-the-old-in-with-the-new-architecture#what-is-next)
I promise, you will stop hearing about the New Architecture soon. You will wake up early next year and ask yourself — was that a dream? Was there ever a legacy architecture? New Architecture? All I know is React Native. And you’ll go and build apps and be happy.
#### Table of Contents
[Why migrate?](https://expo.dev/blog/out-with-the-old-in-with-the-new-architecture#why-migrate)[Potential blockers to migrating](https://expo.dev/blog/out-with-the-old-in-with-the-new-architecture#potential-blockers-to-migrating)[Found a blocker?](https://expo.dev/blog/out-with-the-old-in-with-the-new-architecture#found-a-blocker)[What is next?](https://expo.dev/blog/out-with-the-old-in-with-the-new-architecture#what-is-next)
Share this post
### Sign up for the Expo Newsletter
Sign up to receive a summary of new features, capabilities, content, and news about Expo and the React Native community.
### Create amazing apps, in record time
[Learn More](https://expo.dev/eas)

