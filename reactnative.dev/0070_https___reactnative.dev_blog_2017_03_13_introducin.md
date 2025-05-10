---
url: https://reactnative.dev/blog/2017/03/13/introducing-create-react-native-app
title: https://reactnative.dev/blog/2017/03/13/introducing-create-react-native-app
date: 2025-05-10T21:33:49.462631
depth: 2
---

[Skip to main content](https://reactnative.dev/blog/2017/03/13/introducing-create-react-native-app#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
Today we’re announcing [Create React Native App](https://github.com/react-community/create-react-native-app): a new tool that makes it significantly easier to get started with a React Native project! It’s heavily inspired by the design of [Create React App](https://github.com/facebookincubator/create-react-app) and is the product of a collaboration between [Facebook](https://code.facebook.com) and [Expo](https://expo.io) (formerly Exponent).
Many developers struggle with installing and configuring React Native’s current native build dependencies, especially for Android. With Create React Native App, there’s no need to use Xcode or Android Studio, and you can develop for your iOS device using Linux or Windows. This is accomplished using the Expo app, which loads and runs CRNA projects written in pure JavaScript without compiling any native code.
Try creating a new project (replace with suitable yarn commands if you have it installed):
```
$ npm i -g create-react-native-app$ create-react-native-app my-project$ cd my-project$ npm start
```

This will start the React Native packager and print a QR code. Open it in the [Expo app](https://expo.io) to load your JavaScript. Calls to `console.log` are forwarded to your terminal. You can make use of any standard React Native APIs as well as the [Expo SDK](https://docs.expo.dev/versions/latest/).
## What about native code?[​](https://reactnative.dev/blog/2017/03/13/introducing-create-react-native-app#what-about-native-code "Direct link to What about native code?")
Many React Native projects have Java or Objective-C/Swift dependencies that need to be compiled. The Expo app does include APIs for camera, video, contacts, and more, and bundles popular libraries like [Airbnb’s react-native-maps](https://docs.expo.dev/versions/latest/sdk/map-view/), or [Facebook authentication](https://docs.expo.dev/versions/latest/sdk/facebook/). However if you need a native code dependency that Expo doesn’t bundle then you’ll probably need to have your own build configuration for it. Just like Create React App, “ejecting” is supported by CRNA.
You can run `npm run eject` to get a project very similar to what `react-native init` would generate. At that point you’ll need Xcode and/or Android Studio just as you would if you started with `react-native init` , adding libraries with `react-native link` will work, and you’ll have full control over the native code compilation process.
## Questions? Feedback?[​](https://reactnative.dev/blog/2017/03/13/introducing-create-react-native-app#questions-feedback "Direct link to Questions? Feedback?")
Create React Native App is now stable enough for general use, which means we’re very eager to hear about your experience using it! You can find me [on Twitter](https://twitter.com/dika10sune) or open an issue on [the GitHub repository](https://github.com/react-community/create-react-native-app). Pull requests are very welcome!
  * [What about native code?](https://reactnative.dev/blog/2017/03/13/introducing-create-react-native-app#what-about-native-code)
  * [Questions? Feedback?](https://reactnative.dev/blog/2017/03/13/introducing-create-react-native-app#questions-feedback)



