---
url: https://reactnative.dev/blog/2016/10/25/0.36-headless-js-the-keyboard-api-and-more
title: https://reactnative.dev/blog/2016/10/25/0.36-headless-js-the-keyboard-api-and-more
date: 2025-05-10T21:33:39.810671
depth: 2
---

[Skip to main content](https://reactnative.dev/blog/2016/10/25/0.36-headless-js-the-keyboard-api-and-more#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
Today we are releasing [React Native 0.36](https://github.com/facebook/react-native/releases/tag/v0.36.0). Read on to learn more about what's new.
## Headless JS[​](https://reactnative.dev/blog/2016/10/25/0.36-headless-js-the-keyboard-api-and-more#headless-js "Direct link to Headless JS")
Headless JS is a way to run tasks in JavaScript while your app is in the background. It can be used, for example, to sync fresh data, handle push notifications, or play music. It is only available on Android, for now.
To get started, define your async task in a dedicated file (e.g. `SomeTaskName.js`):
```
module.exports=asynctaskData=>{// Perform your task here.
```

Next, register your task in on `AppRegistry`:
```
AppRegistry.registerHeadlessTask('SomeTaskName',()=>require('SomeTaskName'),
```

Using Headless JS does require some native Java code to be written in order to allow you to start up the service when needed. Take a look at our new [Headless JS docs](https://reactnative.dev/docs/headless-js-android) to learn more!
## The Keyboard API[​](https://reactnative.dev/blog/2016/10/25/0.36-headless-js-the-keyboard-api-and-more#the-keyboard-api "Direct link to The Keyboard API")
Working with the on-screen keyboard is now easier with [`Keyboard`](https://reactnative.dev/docs/keyboard). You can now listen for native keyboard events and react to them. For example, to dismiss the active keyboard, simply call `Keyboard.dismiss()`:
```
import{Keyboard}from'react-native';// Hide that keyboard!Keyboard.dismiss();
```

## Animated Division[​](https://reactnative.dev/blog/2016/10/25/0.36-headless-js-the-keyboard-api-and-more#animated-division "Direct link to Animated Division")
Combining two animated values via addition, multiplication, and modulo are already supported by React Native. With version 0.36, combining two [animated values via division](https://reactnative.dev/docs/animated#divide) is now possible. There are some cases where an animated value needs to invert another animated value for calculation. An example is inverting a scale (2x --> 0.5x):
```
const a =Animated.Value(1);const b =Animated.divide(1, a);Animated.spring(a,{ toValue:2,}).start();
```

`b` will then follow `a`'s spring animation and produce the value of `1 / a`.
The basic usage is like this:
```
<Animated.Viewstyle={{transform:[{scale: a}]}}><Animated.Imagestyle={{transform:[{scale: b}]}}/><Animated.View>
```

In this example, the inner image won't get stretched at all because the parent's scaling gets cancelled out. If you'd like to learn more, check out the [Animations guide](https://reactnative.dev/docs/animations).
## Dark Status Bars[​](https://reactnative.dev/blog/2016/10/25/0.36-headless-js-the-keyboard-api-and-more#dark-status-bars "Direct link to Dark Status Bars")
A new `barStyle` value has been added to `StatusBar`: `dark-content`. With this addition, you can now use [`barStyle`](https://reactnative.dev/docs/statusbar#barstyle) on both Android and iOS. The behavior will now be the following:
  * `default`: Use the platform default (light on iOS, dark on Android).
  * `light-content`: Use a light status bar with black text and icons.
  * `dark-content`: Use a dark status bar with white text and icons.


## ...and more[​](https://reactnative.dev/blog/2016/10/25/0.36-headless-js-the-keyboard-api-and-more#and-more "Direct link to ...and more")
The above is just a sample of what has changed in 0.36. Check out the [release notes on GitHub](https://github.com/facebook/react-native/releases/tag/v0.36.0) to see the full list of new features, bug fixes, and breaking changes.
You can upgrade to 0.36 by running the following commands in a terminal:
```
$ npminstall--save react-native@0.36$ react-native upgrade
```

  * [The Keyboard API](https://reactnative.dev/blog/2016/10/25/0.36-headless-js-the-keyboard-api-and-more#the-keyboard-api)
  * [Animated Division](https://reactnative.dev/blog/2016/10/25/0.36-headless-js-the-keyboard-api-and-more#animated-division)
  * [Dark Status Bars](https://reactnative.dev/blog/2016/10/25/0.36-headless-js-the-keyboard-api-and-more#dark-status-bars)



