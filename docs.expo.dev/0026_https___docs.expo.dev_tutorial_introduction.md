---
url: https://docs.expo.dev/tutorial/introduction
title: https://docs.expo.dev/tutorial/introduction
date: 2025-04-30T17:12:05.885342
depth: 1
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Tutorial: Using React Native and Expo
An introduction to a React Native tutorial on how to build a universal app that runs on Android, iOS and the web using Expo.
We're about to embark on a journey of building universal apps. In this tutorial, we'll create an Expo app that runs on Android, iOS, and web; all with a single codebase. Let's get started!
## About React Native and Expo tutorial
The objective of this tutorial is to get started with Expo and become familiar with the Expo SDK. It'll cover the following topics:
  * Create an app using the default template with TypeScript enabled
  * Implement a two-screen bottom tabs layout with Expo Router
  * Break down the app layout and implement it with flexbox
  * Use each platform's system UI to select an image from the media library
  * Create a sticker modal using the `<Modal>` and `<FlatList>` components from React Native
  * Add touch gestures to interact with a sticker
  * Use third-party libraries to capture a screenshot and save it to the disk
  * Handle platform differences between Android, iOS, and web
  * Finally, go through the process of configuring a status bar, a splash screen, and an icon to complete the app


These topics provide a foundation to learn the fundamentals of building an Expo app. The tutorial is self-paced and can take up to two hours to complete.
To keep it beginner friendly, we divided the tutorial into nine chapters so that you can follow along or put it down and come back to it later. Each chapter contains the necessary code snippets to complete the steps, so you can follow along by creating an app from scratch or copy and paste it.
Before we get started, take a look at what we'll build. It's an app named StickerSmash that runs on Android, iOS, and the web:
> The complete source code for this tutorial is available on [GitHub](https://github.com/expo/examples/tree/master/stickersmash).
## How to use this tutorial
We believe in [learning by doing](https://en.wikipedia.org/wiki/Learning-by-doing), so this tutorial emphasizes doing over explaining. You can follow along the journey of building an app by creating the app from scratch.
Throughout the tutorial, any important code or code that has changed between examples will be highlighted in green. You can hover over the highlights (on desktop) or tap them (on mobile) to learn more about the change. For example, the code highlighted in the snippet below explains what it does:
Hello World
Copy
```
import { StyleSheet, Text, View } from 'react-native';
export default function Index() {
 return (
  <View style={styles.container}>
   <Text>Hello world!</Text>
  </View>
 );
}
const styles = StyleSheet.create({
 container: {
  flex: 1,
  backgroundColor: '#fff',
  alignItems: 'center',
  justifyContent: 'center',
 },
});

Show More

```

## Next step
We're ready to start building our app.
[StartLet's start by creating a new Expo app.](https://docs.expo.dev/tutorial/create-your-first-app)

