---
url: https://docs.expo.dev/versions/latest/sdk/reanimated
title: https://docs.expo.dev/versions/latest/sdk/reanimated
date: 2025-04-30T17:16:54.583799
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# React Native Reanimated
A library that provides an API that greatly simplifies the process of creating smooth, powerful, and maintainable animations.
Android
iOS
tvOS
Web
Bundled version:
~3.16.1
> This library is listed in the Expo SDK reference because it is included in [Expo Go](https://expo.dev/go). You may use any library of your choice with [development builds](https://docs.expo.dev/develop/development-builds/introduction).
[`react-native-reanimated`](https://docs.swmansion.com/react-native-reanimated/docs/fundamentals/getting-started/) provides an API that greatly simplifies the process of creating smooth, powerful, and maintainable animations.
> Reanimated uses React Native APIs that are incompatible with "Remote JS Debugging" for JavaScriptCore. To use a debugger with your app with `react-native-reanimated`, you'll need to use the [Hermes JavaScript engine](https://docs.expo.dev/guides/using-hermes) and the [JavaScript Inspector for Hermes](https://docs.expo.dev/guides/using-hermes#javascript-inspector-for-hermes).
## Installation
Terminal
Copy
`- ``npx expo install react-native-reanimated`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project. Then, follow the [installation instructions](https://docs.swmansion.com/react-native-reanimated/docs/fundamentals/getting-started/#platform-specific-setup) provided in the library's README or documentation.
No additional configuration is required. [Reanimated Babel plugin](https://docs.swmansion.com/react-native-reanimated/docs/fundamentals/glossary#reanimated-babel-plugin) is automatically configured in [`babel-preset-expo`](https://www.npmjs.com/package/babel-preset-expo) when you install the library.
## Usage
The following example shows how to use the `react-native-reanimated` library to create a simple animation. For more information on the API and its usage, see [`react-native-reanimated` documentation](https://docs.swmansion.com/react-native-reanimated/docs/fundamentals/your-first-animation).
Using react-native-reanimated
```
import Animated, {
 useSharedValue,
 withTiming,
 useAnimatedStyle,
 Easing,
} from 'react-native-reanimated';
import { View, Button, StyleSheet } from 'react-native';
export default function AnimatedStyleUpdateExample() {
 const randomWidth = useSharedValue(10);
 const config = {
  duration: 500,
  easing: Easing.bezier(0.5, 0.01, 0, 1),
 };
 const style = useAnimatedStyle(() => {
  return {
   width: withTiming(randomWidth.value, config),
  };
 });
 return (
  <View style={styles.container}><Animated.View style={[styles.box, style]} /><Button
    title="toggle"
    onPress={() => {
     randomWidth.value = Math.random() * 350;
    }}
   /></View>
 );
}
const styles = StyleSheet.create({
 container: {
  flex: 1,
  alignItems: 'center',
  justifyContent: 'center',
 },
 box: {
  width: 100,
  height: 80,
  backgroundColor: 'black',
  margin: 30,
 },
});

Show More

```


