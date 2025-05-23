---
url: https://docs.expo.dev/deploy/app-stores-metadata
title: https://docs.expo.dev/deploy/app-stores-metadata
date: 2025-04-30T17:11:43.069512
depth: 1
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# App stores metadata
A brief overview of how to use EAS Metadata to automate and maintain your app store presence.
> EAS Metadata is in preview and subject to breaking changes.
When submitting your app to app stores, you need to provide metadata. This process is lengthy and is often about complex topics that don't apply to your app. After the information you provide gets reviewed and if there is any issue with it, you need to restart this process.
EAS Metadata enables you to automate and maintain this information from the command line instead of going through multiple forms in the app store dashboards. It can also instantly identify well-known app store restrictions that could trigger a rejection after a lengthy review queue. This guide shows how to use EAS Metadata to automate and maintain your app store presence.
## Prerequisites
EAS Metadata currently only supports the Apple App Store.
> Using VS Code? Install the [Expo Tools extension](https://github.com/expo/vscode-expo#readme) for auto-complete, suggestions, and warnings in your store.config.json files.
## Create a store config
EAS Metadata uses [store.config.json](https://docs.expo.dev/eas/metadata/config) file to hold all the information you want to upload to the app stores. This file is located at the root of your Expo project.
Create a new store.config.json file at the root of your project directory as shown in the example below:
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

The above example file contains JSON schema. Replace the example values with your own. It is usually contains your app's `title`, `subtitle` , `description`, `keywords`, and `marketingUrl` and so on.
An important thing to remember from the above example is the `configVersion` property. It helps with versioning changes that are not backward compatible.
> For more information on properties that can be defined in store.config.json, see [Schema for EAS Metadata](https://docs.expo.dev/eas/metadata/schema#config-schema).
## Upload the store config
> Before pushing the store.config.json to the app stores, you must upload a new binary of your app. See [App Store submissions](https://docs.expo.dev/deploy/submit-to-app-stores) for more information. After the binary is submitted and processed, you can continue with the step below.
After you have created the store.config.json file and added the necessary information related to your app, you can push the store config to the app stores by running the command:
Terminal
Copy
`- ``eas metadata:push`
If EAS Metadata runs into any issues with your store config, it will warn you when running this command. When there are no errors, or you confirm to push it with possible issues, it will try to upload as much as possible.
You can also re-use this command when you modify the store.config.json file and want to push the latest changes to the app stores.
## Next steps
[EAS Metadata schemaA reference of store config in EAS Metadata.](https://docs.expo.dev/eas/metadata/schema) [Static and dynamic configurations with EAS MetadataLearn about different ways to configure EAS Metadata.](https://docs.expo.dev/eas/metadata/config)

