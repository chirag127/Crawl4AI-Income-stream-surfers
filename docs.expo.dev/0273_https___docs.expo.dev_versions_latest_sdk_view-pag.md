---
url: https://docs.expo.dev/versions/latest/sdk/view-pager
title: https://docs.expo.dev/versions/latest/sdk/view-pager
date: 2025-04-30T17:17:50.636385
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# ViewPager
A component library that provides a carousel-like view to swipe through pages of content.
Android
iOS
Bundled version:
6.5.1
> This library is listed in the Expo SDK reference because it is included in [Expo Go](https://expo.dev/go). You may use any library of your choice with [development builds](https://docs.expo.dev/develop/development-builds/introduction).
`react-native-pager-view` exposes a component that provides the layout and gestures to scroll between pages of content, like a carousel.
## Installation
Terminal
Copy
`- ``npx expo install react-native-pager-view`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project. Then, follow the [installation instructions](https://github.com/callstack/react-native-pager-view#linking) provided in the library's README or documentation.
## Usage
See full documentation at [callstack/react-native-pager-view](https://github.com/callstack/react-native-pager-view).
## Example
App.js
Copy
```
import { StyleSheet, View, Text } from 'react-native';
import PagerView from 'react-native-pager-view';
export default function MyPager() {
 return (
  <View style={styles.container}><PagerView style={styles.container} initialPage={0}><View style={styles.page} key="1"><Text>First page</Text><Text>Swipe ➡️</Text></View><View style={styles.page} key="2"><Text>Second page</Text></View><View style={styles.page} key="3"><Text>Third page</Text></View></PagerView></View>
 );
}
const styles = StyleSheet.create({
 container: {
  flex: 1,
 },
 page: {
  justifyContent: 'center',
  alignItems: 'center',
 },
});

Show More

```


