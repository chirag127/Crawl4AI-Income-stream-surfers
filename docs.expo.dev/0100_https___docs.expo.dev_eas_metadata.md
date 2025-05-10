---
url: https://docs.expo.dev/eas/metadata
title: https://docs.expo.dev/eas/metadata
date: 2025-04-30T17:13:41.798742
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# EAS Metadata
An introduction to automate and maintain your app store presence from the command line with EAS Metadata.
> EAS Metadata is in preview and subject to breaking changes.
EAS Metadata enables you to automate and maintain your app store presence from the command line.
You need to provide a lot of information to multiple app stores before your users can use your app. This information is often about complex topics that don't apply to your app. You have to start a lengthy review process after providing the information. When the reviewer finds any issues in the information you provided, you need to restart this process.
EAS Metadata uses a [store.config.json](https://docs.expo.dev/eas/metadata/config#static-store-config) file to provide information instead of going through multiple forms in the app store dashboards. When it's time to update the app stores, you can push the store config to the app stores.
Terminal
Copy
`- ``eas metadata:push`
EAS Metadata can also instantly identify known app store restrictions that could trigger a rejection after a lengthy review queue.
Adding the store config file to your repository enables you to collaborate with other team members to prepare the app submission.
> Using VS Code? Install the [Expo Tools extension](https://github.com/expo/vscode-expo#readme) for auto-complete, suggestions, and warnings in your store.config.json files.
## Get started
[IntroductionAdd EAS Metadata to a new project, or generate the store config from an existing app.](https://docs.expo.dev/eas/metadata/getting-started) [Customize the store configCustomize the store config to adapt EAS Metadata to your preferred workflow.](https://docs.expo.dev/eas/metadata/config) [Store config schemaExplore all configurable options EAS Metadata has to offer.](https://docs.expo.dev/eas/metadata/schema)

