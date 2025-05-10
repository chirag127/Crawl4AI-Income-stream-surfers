---
url: https://docs.expo.dev/eas/metadata/config
title: https://docs.expo.dev/eas/metadata/config
date: 2025-04-30T17:13:38.603490
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Configuring EAS Metadata
Learn about different ways to configure EAS Metadata.
> EAS Metadata is in preview and subject to breaking changes.
EAS Metadata is configured by a store.config.json file at the _root of your project_.
You can configure the path or name of the store config file with the eas.json [`metadataPath`](https://docs.expo.dev/submit/eas-json#metadatapath) property. Besides the default JSON format, EAS Metadata also supports more dynamic config using JavaScript files.
## Static store config
The default store config type for EAS Metadata is a simple JSON file. The code snippet below shows an example store config with basic App Store information written in English (U.S.).
You can find all configuration options in the [store config schema](https://docs.expo.dev/eas/metadata/schema).
> If you have the [VS Code Expo Tools extension](https://github.com/expo/vscode-expo#readme) installed, you get auto-complete, suggestions, and warnings for store.config.json files.
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

## Dynamic store config
At times, Metadata properties can benefit from dynamic values. For example, the Metadata copyright notice should contain the current year. This can be automated with EAS Metadata.
To generate content dynamically, start by creating a JavaScript config file store.config.js. Then, use the [`metadataPath`](https://docs.expo.dev/eas/json#metadatapath) property in the eas.json file to pick the JS config file.
> `eas metadata:pull` can't update dynamic store config files. Instead, it creates a JSON file with the same name as the configured file. You can import the JSON file to reuse the data from `eas metadata:pull`.
store.config.js
Copy
```
// Use the data from `eas metadata:pull`
const config = require('./store.config.json');
const year = new Date().getFullYear();
config.apple.copyright = `${year} Acme, Inc.`;
module.exports = config;

```

eas.json
Copy
```
{
 "submit": {
  "production": {
   "ios": {
    "metadataPath": "./store.config.js"
   }
  }
 }
}

```

## Store config with external content
When using external services for localizations, you have to fetch external content. EAS Metadata supports synchronous and asynchronous functions exported from dynamic store config files. The function results are awaited before validating and syncing with the stores.
> The store.config.js function is evaluated in Node.js. If you need special values, like secrets, use environment variables.
store.config.js
Copy
```
// Use the data from `eas metadata:pull`
const config = require('./store.config.json');
module.exports = async () => {
 const year = new Date().getFullYear();
 const info = await fetchLocalizations('...').then(response => response.json());
 config.apple.copyright = `${year} Acme, Inc.`;
 config.apple.info = info;
 return config;
};

```

eas.json
Copy
```
{
 "submit": {
  "production": {
   "ios": {
    "metadataPath": "./store.config.js"
   }
  }
 }
}

```


