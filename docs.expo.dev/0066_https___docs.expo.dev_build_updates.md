---
url: https://docs.expo.dev/build/updates
title: https://docs.expo.dev/build/updates
date: 2025-04-30T17:13:10.944295
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Using EAS Update
Learn how to use EAS Update with EAS Build.
EAS Build includes some special benefits for [`expo-updates`](https://docs.expo.dev/versions/latest/sdk/updates) library. In particular, you can configure the [`channel`](https://docs.expo.dev/eas-update/how-it-works#distributing-builds) property in eas.json and EAS Build will take care of updating it in your native project at build time.
This document covers concerns specific to using `expo-updates` library with EAS Build. For more general information about configuring the library with EAS Update, see [Getting started with EAS Update ](https://docs.expo.dev/eas-update/getting-started).
## Setting the channel for a build profile
Each [build profile](https://docs.expo.dev/build/eas-json#build-profiles) can be assigned to a channel, so updates for builds produced for a given profile will pull only those releases that are published to its channel.
The following example demonstrates how you might use the `"production"` channel for production builds, and the `"staging"` channel for test builds distributed with [internal distribution](https://docs.expo.dev/build/internal-distribution).
eas.json
Copy
```
{
 "build": {
  "production": {
   "channel": "production"
  },
  "preview": {
   "channel": "staging",
   "distribution": "internal"
  }
 }
}

```

## Binary compatibility and runtime versions
Your native runtime may change on each build, depending on whether you modify the code in a way that changes the API contract with JavaScript. If you publish a JavaScript bundle to a binary with an incompatible native runtime (for example, a function that the JavaScript bundle expects to exist does not exist) then your app may not work as expected, or it may crash.
We recommend using a different [runtime version](https://docs.expo.dev/distribution/runtime-versions) for each binary version of your app. Any time you change the native runtime (in managed apps, this happens when you add or remove a native library, or modify app.json), you should increment the runtime version.
## Previewing updates in development builds
Updates published with the `runtimeVersion` field can't be loaded in Expo Go. Instead, you should use [`expo-dev-client`](https://docs.expo.dev/versions/latest/sdk/dev-client) to create a development build.
## Environment variables and `eas update`
Environment variables set on the `env` field in build profiles are not available when you run `eas update`. Learn more about using [environment variables with EAS Update](https://docs.expo.dev/eas-update/environment-variables).

