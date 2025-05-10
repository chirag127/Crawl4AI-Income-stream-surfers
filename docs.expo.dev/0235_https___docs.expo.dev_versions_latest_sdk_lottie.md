---
url: https://docs.expo.dev/versions/latest/sdk/lottie
title: https://docs.expo.dev/versions/latest/sdk/lottie
date: 2025-04-30T17:16:54.569387
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Lottie
A library that allows rendering After Effects animations.
Android
iOS
tvOS
Web
Bundled version:
7.1.0
> This library is listed in the Expo SDK reference because it is included in [Expo Go](https://docs.expo.dev/get-started/set-up-your-environment). You may use any library of your choice with [development builds](https://docs.expo.dev/develop/development-builds/introduction).
[Lottie](https://airbnb.io/lottie/) renders After Effects animations in real time, allowing apps to use animations as easily as they use static images.
## Installation
Terminal
Copy
`- ``npx expo install lottie-react-native`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project. Then, follow the [installation instructions](https://github.com/lottie-react-native/lottie-react-native#installing) provided in the library's README or documentation.
## Usage
Lottie
```
import { useRef, useEffect } from 'react';
import { Button, StyleSheet, View } from 'react-native';
import LottieView from 'lottie-react-native';
export default function App() {
 const animation = useRef<LottieView>(null);
 useEffect(() => {
  // You can control the ref programmatically, rather than using autoPlay
  // animation.current?.play();
 }, []);
 return (
  <View style={styles.animationContainer}><LottieView
    autoPlay
    ref={animation}
    style={{
     width: 200,
     height: 200,
     backgroundColor: '#eee',
    }}
    // Find more Lottie files at https://lottiefiles.com/featured
    source={require('./assets/gradientBall.json')}
   /><View style={styles.buttonContainer}><Button
     title="Restart Animation"
     onPress={() => {
      animation.current?.reset();
      animation.current?.play();
     }}
    /></View></View>
 );
}
const styles = StyleSheet.create({
 animationContainer: {
  backgroundColor: '#fff',
  alignItems: 'center',
  justifyContent: 'center',
  flex: 1,
 },
 buttonContainer: {
  paddingTop: 20,
 },
});

Show More

```

## API
```
import LottieView from 'lottie-react-native';

```

Refer to the [lottie-react-native repository](https://github.com/lottie-react-native/lottie-react-native#usage) for more detailed documentation.

