---
url: https://docs.expo.dev/versions/latest/sdk/webview
title: https://docs.expo.dev/versions/latest/sdk/webview
date: 2025-04-30T17:17:50.600462
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# React Native WebView
A library that provides a WebView component.
Android
iOS
Bundled version:
13.12.5
`react-native-webview` provides a `WebView` component that renders web content in a native view.
## Installation
Terminal
Copy
`- ``npx expo install react-native-webview`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project. Then, follow the [installation instructions](https://github.com/react-native-webview/react-native-webview/blob/master/docs/Getting-Started.md#react-native-webview-getting-started-guide) provided in the library's README or documentation.
## Usage
You should refer to the [`react-native-webview` documentation](https://github.com/react-native-webview/react-native-webview/blob/master/docs/Guide.md#react-native-webview-guide) for more information on the API and its usage. The following example (courtesy of that repository) is a quick way to get up and running!
Basic Webview usage
```
import { WebView } from 'react-native-webview';
import Constants from 'expo-constants';
import { StyleSheet } from 'react-native';
export default function App() {
 return (
  <WebView
   style={styles.container}
   source={{ uri: 'https://expo.dev' }}
  />
 );
}
const styles = StyleSheet.create({
 container: {
  flex: 1,
  marginTop: Constants.statusBarHeight,
 },
});

Show More

```

Minimal example with inline HTML:
Webview inline HTML
```
import { WebView } from 'react-native-webview';
import Constants from 'expo-constants';
import { StyleSheet } from 'react-native';
export default function App() {
 return (
  <WebView
   style={styles.container}
   originWhitelist={['*']}
   source={{ html: '<h1><center>Hello world</center></h1>' }}
  />
 );
}
const styles = StyleSheet.create({
 container: {
  flex: 1,
  marginTop: Constants.statusBarHeight,
 },
});

Show More

```


