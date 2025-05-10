---
url: https://expo.dev/changelog/2023-08-10-dev-tools-plugins
title: https://expo.dev/changelog/2023-08-10-dev-tools-plugins
date: 2025-04-30T17:18:38.430391
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [Proof of concept: Expo CLI Dev Tools Plugins](https://expo.dev/changelog/2023-08-10-dev-tools-plugins)
Aug 10, 2023 by
Kudo Chien
In Expo SDK 49, we released support for debugging network requests from the JS debugger, and we also added integration with React Dev Tools so you can launch it directly from Expo CLI. These features have made it possible for many developers to migrate away from Flipper, but there’s still one big missing piece that we need to solve, and ideally we can solve it before the [upcoming deprecation of Flipper](https://github.com/react-native-community/discussions-and-proposals/pull/641): that feature is [support for dev tools plugins](https://fbflipper.com/docs/tutorial/intro/).
So, what is a Flipper plugin exactly? If you look closely at Flipper plugins, you’ll see that they are essentially made up of a web UI running on your development machine, and a message bus to send messages between the web UI and the running Android or iOS app. Flipper plugins have been used to expose dev tools for libraries like Apollo, XState, Redux, and so on. Today, we’re demoing a proof of concept that aims to show that it is possible to implement a similar solution on top of existing Expo infrastructure. For this demo, we built an Expo Dev Tools plugin that re-creates [flipper-plugin-react-native-apollo-dev-tools](https://github.com/razorpay/react-native-apollo-devtools/tree/master/packages/flipper-plugin-react-native-apollo-devtools), but without Flipper.
You can try this demo out by cloning it from GitHub: [Kudo/expo-devtools-plugin-demo](https://github.com/Kudo/expo-devtools-plugin-demo). Note that this is an early proof of concept that leans heavily on `patch-package` to modify code in **node_modules**.
If you depend on a Flipper plugin that you’d like to see running as an Expo CLI Dev Tools Plugin and want to try building it yourself, you can refer to the code and the [README](https://github.com/Kudo/expo-devtools-plugin-demo/blob/main/README.md) in this project as a starting point for experimentation. Reach out if you need any assistance.
Let us know what you think, what plugins you’d like to see available, what plugins you build, and any other feedback you might have! Feel free to send us feedback on [Discord](https://chat.expo.dev/), [@expo](https://twitter.com/expo), [Threads](https://www.threads.net/@expo.dev), or [Bluesky](https://bsky.app/profile/expo.dev).
_Thank you to the Flipper team for your work on Flipper plugins, and the Razorpay team for react-native-apollo-devtools._

