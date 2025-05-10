---
url: https://docs.expo.dev/versions/latest/sdk/dev-client
title: https://docs.expo.dev/versions/latest/sdk/dev-client
date: 2025-04-30T17:16:01.552519
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo DevClient
A library that allows creating a development build and includes useful development tools.
Android
iOS
Bundled version:
~5.0.20
`expo-dev-client` adds various useful development tools to your debug builds:
  * A configurable launcher UI, so you can launch updates (such as from [PR previews](https://docs.expo.dev/develop/development-builds/development-workflows#pr-previews)) and switch between development servers without needing to recompile the native app
  * Improved debugging tools (such as support for [inspecting network requests](https://docs.expo.dev/debugging/tools#inspecting-network-requests))
  * [A powerful and extensible developer menu UI](https://docs.expo.dev/debugging/tools#developer-menu)


Expo documentation refers to debug builds that include `expo-dev-client` as [development builds](https://docs.expo.dev/develop/development-builds/introduction).
## Installation
Terminal
Copy
`- ``npx expo install expo-dev-client`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), start by installing [`expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project. Then, follow the instructions from [Install `expo-dev-client` in an existing React Native project](https://docs.expo.dev/bare/install-dev-builds-in-bare).
## Configuration in app config
You can configure development client launcher using its built-in [config plugin](https://docs.expo.dev/config-plugins/introduction) if you use config plugins in your project ([EAS Build](https://docs.expo.dev/build/introduction) or `npx expo run:[android|ios]`). The plugin allows you to configure various properties that cannot be set at runtime and require building a new app binary to take effect.
### Example app.json with config plugin
app.json
Copy
```
{
 "expo": {
  "plugins": [
   [
    "expo-dev-client",
    {
     "launchMode": "most-recent"
    }
   ]
  ]
 }
}

```

### Configurable properties
Name| Default| Description  
---|---|---  
`launchMode`| `"most-recent"`| Determines whether to launch the most recently opened project or navigate to the launcher screen.
  * `most-recent` - Attempt to launch directly into a previously opened project and if unable to connect, fall back to the launcher screen.
  * `launcher` - Opens the launcher screen.

  
`addGeneratedScheme`| `true`| By default, `expo-dev-client` will register a custom URL scheme to open a project. Set this property to `false` to disable this scheme.  
## API
```
import * as DevClient from 'expo-dev-client';

```

## Methods
### `DevClient.closeMenu()`
Android
iOS
A method that closes development client menu when called.
Returns:
`void`
### `DevClient.hideMenu()`
Android
iOS
A method that hides development client menu when called.
Returns:
`void`
### `DevClient.isDevelopmentBuild()`
Android
iOS
A method that returns a boolean to indicate if the current application is a development build.
Returns:
`boolean`
### `DevClient.openMenu()`
Android
iOS
A method that opens development client menu when called.
Returns:
`void`
### `DevClient.registerDevMenuItems(items)`
Android
iOS
Parameter| Type  
---|---  
items| `ExpoDevMenuItem[][](https://docs.expo.dev/versions/latest/sdk/dev-client/#expodevmenuitem)`  
A method that allows to specify custom entries in the development client menu.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
## Types
### `ExpoDevMenuItem`
Android
iOS
An object representing the custom development client menu entry.
Property| Type| Description  
---|---|---  
callback| `() => void`| Callback to fire, when user selects an item.  
name| `string`| Name of the entry, will be used as label.  
shouldCollapse(optional)| `boolean`| A boolean specifying if the menu should close after the user interaction.Default:`false`

