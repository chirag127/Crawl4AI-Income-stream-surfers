---
url: https://docs.expo.dev/config-plugins/introduction
title: https://docs.expo.dev/config-plugins/introduction
date: 2025-04-30T17:13:10.950273
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Config plugins: Introduction
An introduction to config plugins for the Expo project.
An automatic setup for adding a native module to your project is possible. Sometimes, a module requires a more complex setup. A config plugin can be used to automatically configure your native project for a module and reduce the complexity by avoiding interaction with the native project.
## What is a config plugin
Config plugin is a system for extending the [app config](https://docs.expo.dev/workflow/configuration) and customizing the prebuild process for your app. They can be used to add native modules that aren't included, by default, or to add any native code that needs to be configured further.
Internally Expo CLI uses config plugins to generate and configure all the native code for a managed project. Plugins do things such as generate app icons, set the app name, and configure the AndroidManifest.xml, Info.plist, and so on.
You can think of plugins like a bundler for native projects, and running `npx expo prebuild` as a way to bundle the projects by evaluating all the project plugins. Doing so will generate android and ios directories. These directories can be modified manually after being generated, but then they can no longer be safely regenerated without potentially overwriting manual modifications.
## Use a config plugin
Expo config plugins mostly come from Node.js modules. You can install them just like other packages in your project.
For example, `expo-camera` has a plugin that adds camera permissions to the AndroidManifest.xml and Info.plist. To install it in your project, run the following command:
Terminal
Copy
`- ``npx expo install expo-camera`
In your [app's config](https://docs.expo.dev/versions/latest/config/app), you can add `expo-camera` to the list of plugins:
app.json
Copy
```
{
 "expo": {
  "plugins": ["expo-camera"]
 }
}

```

Some config plugins offer flexibility by allowing you to pass options to customize their configuration. To do this, you can pass an array with the Expo library name as the first argument, and an object containing the options as the second argument. For example, the `expo-camera` plugin allows you to customize the camera permission message:
app.json
Copy
```
{
 "expo": {
  "plugins": [
   [
    "expo-camera",
    {
     "cameraPermission": "Allow $(PRODUCT_NAME) to access your camera."
    }
   ]
  ]
 }
}

```

> Tip: For every Expo library that has a config plugin, you'll find more information about that in the library's API reference. For example, the [`expo-camera` library has a config plugin section](https://docs.expo.dev/versions/latest/sdk/camera#configuration-in-appjsonappconfigjs).
On running the `npx expo prebuild`, the [`mods`](https://docs.expo.dev/config-plugins/plugins-and-mods#how-mods-work) are compiled, and the native files change.
The changes don't take effect until you rebuild the native project, for example, with Xcode. If you're using config plugins in a managed app, they will be applied during the prebuild phase on `eas build`.

