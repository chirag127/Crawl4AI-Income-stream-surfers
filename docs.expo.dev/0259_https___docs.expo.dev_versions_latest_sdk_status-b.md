---
url: https://docs.expo.dev/versions/latest/sdk/status-bar
title: https://docs.expo.dev/versions/latest/sdk/status-bar
date: 2025-04-30T17:17:28.184563
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo StatusBar
A library that provides the same interface as the React Native StatusBar API, but with slightly different defaults to work great in Expo environments.
Android
iOS
tvOS
Web
Bundled version:
~2.0.1
`expo-status-bar` gives you a component and imperative interface to control the app status bar to change its text color, background color, hide it, make it translucent or opaque, and apply animations to any of these changes. Exactly what you are able to do with the `StatusBar` component depends on the platform you're using.
> tvOS and web support
> For tvOS, the `expo-status-bar` code will compile and run, but no status bar will show.
> For web, there is no API available to control the operating system's status bar, so `expo-status-bar` will do nothing and won't throw an error.
## Installation
Terminal
Copy
`- ``npx expo install expo-status-bar`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Usage
Example
```
import { StyleSheet, Text, View } from 'react-native';
import { StatusBar } from 'expo-status-bar';
export default function App() {
 return (
  <View style={styles.container}><Text style={styles.text}>Notice that the status bar has light text!</Text><StatusBar style="light" /></View>
 );
}
const styles = StyleSheet.create({
 container: {
  flex: 1,
  backgroundColor: '#000',
  alignItems: 'center',
  justifyContent: 'center',
 },
 text: {
  color: '#fff',
 },
});

Show More

```

## API
```
import { StatusBar } from 'expo-status-bar';

```

## Component
### `StatusBar`
Android
iOS
tvOS
Web
Type: `React.Element[](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<StatusBarProps[](https://docs.expo.dev/versions/latest/sdk/status-bar/#statusbarprops)>`
A component that allows you to configure your status bar without directly calling imperative methods like `setBarStyle`.
You will likely have multiple `StatusBar` components mounted in the same app at the same time. For example, if you have multiple screens in your app, you may end up using one per screen. The props of each `StatusBar` component will be merged in the order that they were mounted. This component is built on top of the [StatusBar](https://reactnative.dev/docs/statusbar) component exported from React Native, and it provides defaults that work better for Expo users.
StatusBarProps
### `animated`
Android
iOS
tvOS
Web
Optional • Type: `boolean`
If the transition between status bar property changes should be animated. Supported for `backgroundColor`, `barStyle` and `hidden`.
### `backgroundColor`
Android
Optional • Type: `string`
The background color of the status bar.
### `hidden`
Android
iOS
tvOS
Web
Optional • Type: `boolean`
If the status bar is hidden.
### `hideTransitionAnimation`
iOS
Optional • Type: `StatusBarAnimation[](https://docs.expo.dev/versions/latest/sdk/status-bar/#statusbaranimation)` • Default: `'fade'`
The transition effect when showing and hiding the status bar using the hidden prop.
### `networkActivityIndicatorVisible`
iOS
Optional • Type: `boolean`
If the network activity indicator should be visible.
### `style`
Android
iOS
tvOS
Web
Optional • Type: `StatusBarStyle[](https://docs.expo.dev/versions/latest/sdk/status-bar/#statusbarstyle)` • Default: `'auto'`
Sets the color of the status bar text. Default value is `"auto"` which picks the appropriate value according to the active color scheme, eg: if your app is dark mode, the style will be `"light"`.
### `translucent`
Android
Optional • Type: `boolean`
If the status bar is translucent. When translucent is set to `true`, the app will draw under the status bar. This is the default behaviour in projects created with Expo tools because it is consistent with iOS.
## Methods
### `StatusBar.setStatusBarBackgroundColor(color, animated)`
Android
iOS
tvOS
Web
Parameter| Type| Description  
---|---|---  
color| | Background color.  
animated(optional)| `boolean`| Animate the style change.  
Set the background color of the status bar.
Returns:
`void`
### `StatusBar.setStatusBarHidden(hidden, animation)`
Android
iOS
tvOS
Web
Parameter| Type| Description  
---|---|---  
hidden| `boolean`| The dialog's title.  
animation(optional)| `StatusBarAnimation[](https://docs.expo.dev/versions/latest/sdk/status-bar/#statusbaranimation)`| Optional animation when changing the status bar hidden property.  
Toggle visibility of the status bar.
Returns:
`void`
### `StatusBar.setStatusBarNetworkActivityIndicatorVisible(visible)`
Android
iOS
tvOS
Web
Parameter| Type| Description  
---|---|---  
visible| `boolean`| Show the indicator.  
Toggle visibility of the network activity indicator.
Returns:
`void`
### `StatusBar.setStatusBarStyle(style, animated)`
Android
iOS
tvOS
Web
Parameter| Type| Description  
---|---|---  
style| `StatusBarStyle[](https://docs.expo.dev/versions/latest/sdk/status-bar/#statusbarstyle)`| The color of the status bar text.  
animated(optional)| `boolean`| If the transition should be animated.  
Set the bar style of the status bar.
Returns:
`void`
### `StatusBar.setStatusBarTranslucent(translucent)`
Android
iOS
tvOS
Web
Parameter| Type| Description  
---|---|---  
translucent| `boolean`| Set as translucent.  
Set the translucency of the status bar.
Returns:
`void`
## Types
### `StatusBarAnimation`
Android
iOS
tvOS
Web
Literal Type: `string`
Acceptable values are: `'none'` | `'fade'` | `'slide'`
### `StatusBarStyle`
Android
iOS
tvOS
Web
Literal Type: `string`
Acceptable values are: `'auto'` | `'inverted'` | `'light'` | `'dark'`

