---
url: https://docs.expo.dev/debugging/create-devtools-plugins
title: https://docs.expo.dev/debugging/create-devtools-plugins
date: 2025-04-30T17:13:10.974649
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Create a dev tools plugin
Learn how to create a dev tools plugin to enhance your development experience.
> Dev Tools plugins are compatible with SDK 50 and above.
> Tip: Check out the [Expo DevTools Plugins](https://github.com/expo/dev-plugins) for complete examples.
You can create a dev tools plugin, whether that's for inspecting aspects of a common framework or library or something specific to your custom code. This guide will walk you through creating a dev tools plugin.
## What is a dev tools plugin?
A dev tools plugin runs in your web browser in your local development environment and connects to your Expo app.
A plugin consists of three key elements:
  * An Expo app to display the dev tools web user interface.
  * An expo-module.config.json for Expo CLI recognition.
  * Calls to `expo/devtools` API for the app to communicate back and forth with the dev tool's web interface.


Plugins can be distributed on npm or included inside your app's monorepo. They typically export a single hook that can be used in your app's root component to initiate two-way communication with the web interface when your app is running in debug mode.
1
## Create a plugin
### Create a new plugin project
`create-dev-plugin` will set up a new plugin project for you. Run the following command to create a new plugin project:
Terminal
Copy
`- ``npx create-dev-plugin@latest`
`create-dev-plugin` will prompt you for the name of your plugin, a description, and the name of the hook that will be used by consumers of your plugin.
The plugin project will contain the following directories:
  * src - this exports the hook that will be used inside the consuming app to connect it to the plugin.
  * webui - this contains the web user interface for the plugin.


### Customize a plugin's functionality
The template includes a simple example of sending and receiving messages between the plugin and the app. `useDevToolsPluginClient`, imported from `expo/devtools`, provides functionality for sending and receiving messages between the plugin and the app.
The client object returned by `useDevToolsPluginClient` includes:
### `addMessageListener`
Listens for a message matching the typed string and invokes the callback with the message data.
```
const client = useDevToolsPluginClient('my-devtools-plugin');
client.addMessageListener('ping', data => {
 alert(`Received ping from ${data.from}`);
});

```

### `sendMessage`
Listens for a message matching the typed string and invokes the callback with the message data.
```
const client = useDevToolsPluginClient('my-devtools-plugin');
client?.sendMessage('ping', { from: 'web' });

```

Edit the Expo app inside the webui directory to customize the user interface that displays diagnostic information from your app or triggers test scenarios:
webui/App.tsx
Copy
```
import { useDevToolsPluginClient, type EventSubscription } from 'expo/devtools';
import { useEffect } from 'react';
export default function App() {
 const client = useDevToolsPluginClient('my-devtools-plugin');
 useEffect(() => {
  const subscriptions: EventSubscription[] = [];
  subscriptions.push(
   client?.addMessageListener('ping', data => {
    alert(`Received ping from ${data.from}`);
   })
  );
  return () => {
   for (const subscription of subscriptions) {
    subscription?.remove();
   }
  };
 }, [client]);
}

Show More

```

Edit the hook in the src directory to customize what diagnostic information is sent to the plugin or how the app should respond to any messages from the web user interface:
src/useMyDevToolsPlugin.ts
Copy
```
import { useDevToolsPluginClient } from 'expo/devtools';
export function useMyDevToolsPlugin() {
 const client = useDevToolsPluginClient('my-devtools-plugin');
 const sendPing = () => {
  client?.sendMessage('ping', { from: 'app' });
 };
 return {
  sendPing,
 };
}

```

If you update the hook to return functions that will be called by the app, you will also need to update src/index.ts so it exports no-op functions when the app is not running in debug mode:
src/index.ts
Copy
```
if (process.env.NODE_ENV !== 'production') {
 useMyDevToolsPlugin = require('./useMyDevToolsPlugin').useMyDevToolsPlugin;
} else {
 useMyDevToolsPlugin = () => ({
+  sendPing: () => {},
 });
}

```

2
## Test a plugin
Since the plugin web UI is an Expo app, you can test it just like you would any other Expo app, with `npx expo start`, except that you will run it in the browser only. The template includes a convenience command to run the plugin in local development mode:
Terminal
Copy
`- ``npm run web:dev`
3
## Build a plugin for distribution
To prepare your plugin for distribution or use within your monorepo, you will need to build the plugin with the following command:
Terminal
Copy
`- ``npm run build:all`
This command will build the hook code into the build directory, and the web user interface into the dist directory.
4
## Use the plugin
Import the plugin's hook into your app's root component and call it to connect your app to the plugin:
App.js
Copy
```
import { useMyDevToolsPlugin } from 'my-devtools-plugin';
import { Button } from 'react-native';
export default function App() {
 const { sendPing } = useMyDevToolsPlugin();
 return (
  <View style={styles.container}><Button
    title="Ping"
    onPress={() => {
     sendPing();
    }}
   /></View>
 );
}

```


