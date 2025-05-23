---
url: https://docs.expo.dev/archive/customizing-webpack
title: https://docs.expo.dev/archive/customizing-webpack
date: 2025-04-30T17:12:45.573949
depth: 2
---

[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Bundle with webpack
Learn about different webpack bundler configurations that can be customized.
> Deprecated: In SDK 50 and above, Expo Webpack has been deprecated in favor of [Expo Router](https://docs.expo.dev/router/introduction). Learn how to [migrate from Expo Webpack to Expo Router](https://docs.expo.dev/router/migrate/from-expo-webpack).
To enable Webpack web support, modify your [app config](https://docs.expo.dev/workflow/configuration) using the `expo.web.bundler` field:
app.json
Copy
```
{
 "expo": {
  "web": {
   "bundler": "webpack"
  }
 }
}

```

## Customizing the Webpack config
When you run `npx expo start --web` or `expo export:web` the CLI checks to see if your project has a webpack.config.js in the root directory. If the file doesn't exist in your project, then Expo uses the default `@expo/webpack-config` (preferred).
To edit the config, install `@expo/webpack-config` as a dev dependency and create a template webpack.config.js at the root of your project. This can be done by running the following command:
Terminal
Copy
`- ``npx expo customize webpack.config.js`
You can now make changes to a config object based on the default config and return it for Expo CLI to use. Deleting the config will cause Expo to fall back to the default again.
If you create a new webpack config or make any changes to it you'll need to restart your webpack dev server by running:
Terminal
Copy
`- ``npx expo start`
## Example
webpack.config.js
Copy
```
const createExpoWebpackConfigAsync = require('@expo/webpack-config');
// Expo CLI will await this method so you can optionally return a promise.
module.exports = async function (env, argv) {
 const config = await createExpoWebpackConfigAsync(env, argv);
 // If you want to add a new alias to the config.
 config.resolve.alias['moduleA'] = 'moduleB';
 // Maybe you want to turn off compression in dev mode.
 if (config.mode === 'development') {
  config.devServer.compress = false;
 }
 // Or prevent minimizing the bundle when you build.
 if (config.mode === 'production') {
  config.optimization.minimize = false;
 }
 // Finally return the new config for the CLI to use.
 return config;
};

Show More

```

## Editing static files
You can also use `npx expo customize` to generate static project files such as index.html and so on. These can be used to customize your project more familiarly.
All the files you select from the terminal prompt will be copied to a web directory in your project's root directory. Think of this directory as public in Create React App. The web is used instead of public because Expo webpack is web-only, the static directory does not work for Android or iOS apps. For mobile platforms, the platform-specific project files are included in android and ios directories.
Deleting any of these files will cause Expo webpack to fall back to their respective default copies.
### Why
  * Customizing the favicon icon.
  * Adding third-party API code to the `<head/>` in your index.html.



