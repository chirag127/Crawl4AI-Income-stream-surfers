---
url: https://docs.expo.dev/router/installation
title: https://docs.expo.dev/router/installation
date: 2025-04-30T17:14:26.284759
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Install Expo Router
Learn how to quickly get started by creating a new project with Expo Router or adding the library to an existing project.
Find the steps below to create a new project with Expo Router library or add it to your existing project.
## Quick start
1
We recommend creating a new Expo app using `create-expo-app` to create a project with Expo Router library already installed and configured:
Terminal
Copy
`- ``npx create-expo-app@latest`
2
Now, you can start your project by running:
Terminal
Copy
`- ``npx expo start`
  * To view your app on a mobile device, we recommend starting with [Expo Go](https://docs.expo.dev/get-started/set-up-your-environment#how-would-you-like-to-develop). As your application grows in complexity and you need more control, you can create a [development build](https://docs.expo.dev/develop/development-builds/introduction).
  * Open the project in a web browser by pressing `w` in the Terminal UI. Press `a` for Android (Android Studio is required), or `i` for iOS (macOS with Xcode is required).


## Manual installation
Follow the steps below if you have a project that was previously created with Expo but does not have Expo Router library installed.
### Prerequisites
Make sure your computer is [set up for running an Expo app](https://docs.expo.dev/get-started/create-a-project).
1
### Install dependencies
You'll need to install the following dependencies:
Terminal
Copy
`- ``npx expo install expo-router react-native-safe-area-context react-native-screens expo-linking expo-constants expo-status-bar`
The above command will install versions of these libraries that are compatible with the Expo SDK version your project is using.
2
### Setup entry point
For the property `main`, use the `expo-router/entry` as its value in the package.json. The initial client file is [app/_layout.tsx](https://docs.expo.dev/router/basics/layout#root-layout).
package.json
Copy
```
{
 "main": "expo-router/entry"
}

```

Custom entry point to initialize and load side-effects
You can create a custom entry point in your Expo Router project to initialize and load side-effects before your app loads the root layout (app/_layout.tsx). Below are some of the common cases for a custom entry point:
  * Initializing global services like analytics, error reporting, and so on.
  * Setting up polyfills
  * Ignoring specific logs using `LogBox` from `react-native`


  1. Create a new file in the root of your project, such as index.js. After creating this file, the project structure should look like this:
`app`
`_layout.tsx`
`index.js`
`package.json`
`Other project files`
  2. Import or add your custom configuration to the file. Then, import `expo-router/entry` to register the app entry. Remember to always import it last to ensure all configurations are properly set up before the app renders.
index.js
Copy
```
// Import side effects first and services
// Initialize services
// Register app entry through Expo Router
import 'expo-router/entry';

```

  3. Update the `main` property in package.json to point to the new entry file.
package.json
Copy
```
{
 "main": "index.js"
}

```



3
### Modify project configuration
Add a deep linking `scheme` in your [app config](https://docs.expo.dev/workflow/configuration):
app.json
Copy
```
{
 "scheme": "your-app-scheme"
}

```

If you are developing your app for web, install the following dependencies:
Terminal
Copy
`- ``npx expo install react-native-web react-dom`
Then, enable [Metro web](https://docs.expo.dev/guides/customizing-metro#adding-web-support-to-metro) support by adding the following to your [app config](https://docs.expo.dev/workflow/configuration):
app.json
Copy
```
{
 "web": {
  "bundler": "metro"
 }
}

```

4
### Modify babel.config.js
Ensure you use `babel-preset-expo` as the `preset`, in the babel.config.js file or delete the file:
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

If you're upgrading from a version of Expo Router that is older than v3, remove the `plugins: ['expo-router/babel']`. `expo-router/babel` was merged in `babel-preset-expo` in SDK 50 (Expo Router v3).
5
### Clear bundler cache
After updating the Babel config file, run the following command to clear the bundler cache:
Terminal
Copy
`- ``npx expo start --clear`
6
### Update resolutions
If you're upgrading from an older version of Expo Router, ensure you remove all outdated Yarn resolutions or npm overrides in your package.json. Specifically, remove `metro`, `metro-resolver`, `react-refresh` resolutions from your package.json.

