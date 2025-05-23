---
url: https://docs.expo.dev/guides/adopting-prebuild
title: https://docs.expo.dev/guides/adopting-prebuild
date: 2025-04-30T17:14:04.124191
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Adopt Prebuild
Learn how to adopt Expo Prebuild in a project that was bootstrapped with React Native CLI.
There are [many advantages](https://docs.expo.dev/workflow/prebuild#pitch) of using [Expo Prebuild](https://docs.expo.dev/workflow/prebuild) to [continuously generate your native projects](https://docs.expo.dev/workflow/continuous-native-generation). This guide will show you how to adopt Expo Prebuild in a project that was bootstrapped with `npx @react-native-community/cli@latest init`. The amount of time it will take to convert your project depends on the amount of custom native changes that you have made to your Android and iOS native projects. This may take a minute or two on a brand new project, and on a large project, it will be much longer.
Adopting prebuild will automatically add support for developing modules with the [Expo native module API](https://docs.expo.dev/modules/module-api) by linking `expo-modules-core` natively. You can also use any command from [Expo CLI](https://docs.expo.dev/more/expo-cli) in your project.
> [Not all versions of `react-native` are explicitly supported](https://docs.expo.dev/versions/latest#each-expo-sdk-version-depends-on-a-react-native-version). Make sure to use a version of `react-native` that has a corresponding Expo SDK version.
## Install the `expo` package
The `expo` package contains the [`npx expo prebuild`](https://docs.expo.dev/more/expo-cli#prebuild) command and indicates which [prebuild template](https://docs.expo.dev/workflow/prebuild#templates) to use:
Terminal
Copy
`- ``npm install expo`
Ensure you install the version of `expo` that works for your currently installed [version of `react-native`](https://docs.expo.dev/versions/latest#each-expo-sdk-version-depends-on-a-react-native-version).
## Update the entry file
Modify the entry file to use [`registerRootComponent`](https://docs.expo.dev/versions/latest/sdk/register-root-component) instead of `AppRegistry.registerComponent`:
```
+ import {registerRootComponent} from 'expo';

- import {AppRegistry} from 'react-native';
import App from './App';
- import {name as appName} from './app.json';

- AppRegistry.registerComponent(appName, () => App);
+ registerRootComponent(App);

```

> Learn more about [`registerRootComponent`](https://docs.expo.dev/versions/latest/sdk/expo#registerrootcomponentcomponent).
## Prebuild
> Make sure you have committed your changes in case you want to revert, the command will warn you about this too!
If you're migrating an existing project, then you may want to refer to [migrating native customizations](https://docs.expo.dev/guides/adopting-prebuild#migrate-native-customizations) first.
Run the following command to regenerate the android and ios directories based on the app config (app.json/app.config.js) configuration:
Terminal
Copy
`- ``npx expo prebuild --clean`
You can test that everything worked by building the projects locally:
Terminal
`# Build your native Android project`
`- ``npx expo run:android`
`# Build your native iOS project`
`- ``npx expo run:ios`
> Learn more about [compiling native apps](https://docs.expo.dev/more/expo-cli#compiling).
## Extra changes
The following changes are optional but recommended.
.gitignore
You can add .expo to your .gitignore to prevent generated values from Expo CLI from being committed. These [values are unique to your project](https://docs.expo.dev/more/expo-cli#expo-directory) on your local computer.
You can also add android and ios to the .gitignore if you want to ensure they are not committed between prebuilds.
app.json
Remove all fields that are outside the top-level `expo` object as these will not be used in `npx expo prebuild`.
```
{
- "name": "myapp",
- "displayName": "myapp"
+ "expo": {
+  "name": "myapp"
+ }
}

```

metro.config.js
See [Customizing Metro](https://docs.expo.dev/guides/customizing-metro).
package.json
You may want to change the scripts to use the [Expo CLI](https://docs.expo.dev/more/expo-cli#compiling) run commands:
```
 "scripts": {
  "start": "expo start",
-  "android": "react-native run-android",
-  "ios": "react-native run-ios",
+  "android": "expo run:android",
+  "ios": "expo run:ios",
 },

```

These commands have better logging, auto code signing, better simulator handling, and they ensure you run `npx expo start` to serve files.
## Migrate native customizations
If your project has any native modifications (changes to the android or ios directories, such as app icon configuration or splash screen) then you'll need to configure your app config (app.json) to reflect those native changes.
  * Check to see if your changes overlap with the built-in [app config fields](https://docs.expo.dev/versions/latest/config/app). For example, if you have an app icon, be sure to define it as `expo.icon` in the app.json then re-run `npx expo prebuild`.
  * Look up if any of the packages you are using require an [Expo config plugin](https://docs.expo.dev/config-plugins/introduction). If a package in your project requires additional changes inside the android or ios directories, then you will probably need a Config Plugin. Some plugins can be automatically added by running `npx expo install` with all of the packages in your package.json dependencies. If a package requires a plugin but doesn't supply one, then you can try checking the community plugins at [`expo/config-plugins`](https://github.com/expo/config-plugins) to see if one already exists.
  * You can use the [VS Code Expo extension](https://marketplace.visualstudio.com/items?itemName=expo.vscode-expo-tools) to introspect your changes and debug if prebuild is generating the native code you expect. Just press `Cmd ⌘` + `Shift` + `p`, type "Expo: Preview Modifier", and select the native file you wish to introspect.
  * Additionally, you can develop local config plugins to fit your needs. [Learn more](https://docs.expo.dev/config-plugins/development-and-debugging#develop-a-plugin).


## Add more features
Prebuild is the tip of the automation iceberg, here are some features you can adopt next:
  * [EAS Build](https://docs.expo.dev/build/setup): Code signing and cloud building.
  * [EAS Update](https://docs.expo.dev/build/updates): Send over-the-air updates instantly.
  * [Expo for web](https://docs.expo.dev/workflow/web): Run your app in the browser.
  * [Expo Dev Client](https://docs.expo.dev/develop/development-builds/introduction): Create your own personal "Expo Go" type app around your native runtime.
  * [Expo native module API](https://docs.expo.dev/modules/module-api): Write modules with Swift and Kotlin. This is automatically supported when using `npx expo prebuild`.



