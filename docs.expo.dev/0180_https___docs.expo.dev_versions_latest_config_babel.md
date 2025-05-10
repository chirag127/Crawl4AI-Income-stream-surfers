---
url: https://docs.expo.dev/versions/latest/config/babel
title: https://docs.expo.dev/versions/latest/config/babel
date: 2025-04-30T17:15:18.526502
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# babel.config.js
A reference for Babel configuration file.
Babel is used as the JavaScript compiler to transform modern JavaScript (ES6+) into a version compatible with the JavaScript engine on mobile devices.
Each new Expo project created using `npx create-expo-app` configures Babel automatically and uses [`babel-preset-expo`](https://github.com/expo/expo/tree/main/packages/babel-preset-expo) as the default preset. There is no need to create a babel.config.js file unless you need to customize the Babel configuration.
## Create babel.config.js
If your project requires a custom Babel configuration, you need to create the babel.config.js file in your project by following the steps below:
  1. Navigate to the root of your project, run the following command inside a terminal:


Terminal
Copy
`- ``npx expo customize`
  1. This command prompts generating different config files. Select babel.config.js.
  2. The babel.config.js file is created in the root of your project with the default configuration as shown below:


babel.config.js
Copy
```
module.exports = function (api) {
 api.cache(true);
 return {
  presets: ['babel-preset-expo'],
 };
};

```

  1. If you make a change to the babel.config.js file, you need to restart the Metro bundler to apply the changes and use `--clear` option from Expo CLI to clear the Metro bundler cache:


Terminal
Copy
`- ``npx expo start --clear`
## babel-preset-expo
[`babel-preset-expo`](https://github.com/expo/expo/tree/main/packages/babel-preset-expo) is the default preset used in Expo projects. It extends the default React Native preset (`@react-native/babel-preset`) and adds support for decorators, tree-shaking web libraries, and loading font icons.

