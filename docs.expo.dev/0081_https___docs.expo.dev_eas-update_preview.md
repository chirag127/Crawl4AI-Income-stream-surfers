---
url: https://docs.expo.dev/eas-update/preview
title: https://docs.expo.dev/eas-update/preview
date: 2025-04-30T17:13:14.785061
depth: 2
---

Search
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Preview updates
Learn how to preview updates in development, preview, and production builds.
Before deploying an update to production, you will often want to test it in a production-like environment. This guide will outline different approaches for previewing updates, and link out to more detailed guides for each approach.
## Previewing updates in development builds
Development builds are a great way to preview updates from pull requests, directly from the EAS dashboard, or from the built-in UI provided by the `expo-dev-client` library.
[Preview updates in development buildsLearn how to preview updates in development builds.](https://docs.expo.dev/eas-update/expo-dev-client) [Use GitHub Actions to automate publishing updatesLearn how to use GitHub Actions to automate publishing updates with EAS Update](https://docs.expo.dev/eas-update/github-actions) [Launch preview updates from the EAS dashboard using OrbitLearn how to launch updates with the macOS, Windows, and Linux desktop app Expo Orbit](https://docs.expo.dev/review/with-orbit)
## Previewing updates in preview builds
Non-technical users will typically not want to interact with a development build, and they will want to test changes from a preview build on an [App store testing track](https://docs.expo.dev/review/overview#app-store-testing-tracks) or [internal distribution](https://docs.expo.dev/review/overview#internal-distribution-with-eas-build).
If your team is smaller, it may be sufficient to deploy a single preview build at a time to an app store testing track or internal distribution. You can then publish updates to the channel that is used by that preview build. [Learn more about preview builds](https://docs.expo.dev/review/overview).
Alternatively, you can build a mechanism into your preview build that allows users to select a different update or channel to load. This can be useful in cases where the [app runtime](https://docs.expo.dev/eas-update/runtime-versions) doesn't change often, and many different updates can be loaded in the same app. [Learn more](https://docs.expo.dev/eas-update/override).
[Override update configuration at runtimeLearn how to override the update URL and channel at runtime.](https://docs.expo.dev/eas-update/override)
## Previewing updates in production builds
Before deploying an update to all end-users, some teams will want to first roll it out in production to a small set of internal users. One way this can be accomplished is by [overriding the update channel](https://docs.expo.dev/eas-update/override) at runtime for a known subset of users. Be sure to note the [security considerations](https://docs.expo.dev/eas-update/override#security-considerations) before proceeding down this path. Additionally, it is not recommended to use this approach for non-internal users because it makes it possible to get the app into a state where it must be uninstalled and reinstalled.
Another approach is to use a deployment pattern like the [Persistent Staging Flow](https://docs.expo.dev/eas-update/deployment-patterns#persistent-staging-flow), which involves always having a version of your production app that points to a staging channel.
[Persistent Staging FlowLearn how to use the Persistent Staging Flow to always have a version of your production app that points to a staging channel.](https://docs.expo.dev/eas-update/deployment-patterns#persistent-staging-flow)

