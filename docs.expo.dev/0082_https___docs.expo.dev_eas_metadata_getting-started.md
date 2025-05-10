---
url: https://docs.expo.dev/eas/metadata/getting-started
title: https://docs.expo.dev/eas/metadata/getting-started
date: 2025-04-30T17:13:33.271211
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Get started with EAS Metadata
Learn how to automate and maintain your app store presence from the command line with EAS Metadata.
> EAS Metadata is in preview and subject to breaking changes.
EAS Metadata enables you to automate and maintain your app store presence from the command line. It uses a [store.config.json](https://docs.expo.dev/eas/metadata/config#static-store-config) file containing all required app information instead of going through multiple different forms. It also tries to find common pitfalls that could cause app rejections with built-in validation.
## Prerequisites
EAS Metadata currently only supports the Apple App Store.
> Using VS Code? Install the [Expo Tools extension](https://github.com/expo/vscode-expo#readme) for auto-complete, suggestions, and warnings in your store.config.json files.
## Create the store config
Let's start by creating our store.config.json file in the root directory of your project. This file holds all the information you want to upload to the app stores.
If you already have an app in the stores, you can pull the information into a store config by running:
Terminal
Copy
`- ``eas metadata:pull`
If you don't have an app in the stores yet, EAS Metadata can't generate the store config for you. Instead, create a new store config file.
store.config.json
Copy
```
{
 "configVersion": 0,
 "apple": {
  "info": {
   "en-US": {
    "title": "Awesome App",
    "subtitle": "Your self-made awesome app",
    "description": "The most awesome app you have ever seen",
    "keywords": ["awesome", "app"],
    "marketingUrl": "https://example.com/en/promo",
    "supportUrl": "https://example.com/en/support",
    "privacyPolicyUrl": "https://example.com/en/privacy"
   }
  }
 }
}

```

> By default, EAS Metadata uses the store.config.json file at the root of your project. You can change the name and location of this file by setting the eas.json [`metadataPath`](https://docs.expo.dev/submit/eas-json#metadatapath) property.
## Update the store config
Now it's time to edit the store.config.json file and customize it to your app needs. You can find all available options in the [store config schema](https://docs.expo.dev/eas/metadata/schema).
## Upload a new app version
Before pushing the store.config.json to the app stores, you must upload a new binary of your app. For more information, see [uploading new binaries to stores](https://docs.expo.dev/submit/introduction).
After the binary is submitted and processed, you can push the store config to the app stores.
## Upload the store config
When you are satisfied with the store.config.json settings, you can push it to the app stores by running the following command:
Terminal
Copy
`- ``eas metadata:push`
If EAS Metadata runs into any issues with your store config, it will warn you when running this command. When there are no errors, or you confirm to push it with possible issues, it will try to upload as much as possible.
When the store config partially fails, you can change the store config and retry. `eas metadata:push` can be used to retry pushing the missing items.
## Next steps
[Customize the store configCustomize the store config to adapt EAS Metadata to your preferred workflow.](https://docs.expo.dev/eas/metadata/config) [Store config schemaExplore all configurable options EAS Metadata has to offer.](https://docs.expo.dev/eas/metadata/schema)

