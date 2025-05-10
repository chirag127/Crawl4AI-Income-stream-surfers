---
url: https://reactnative.dev/docs/style
title: https://reactnative.dev/docs/style
date: 2025-05-10T21:33:18.907788
depth: 1
---

[Skip to main content](https://reactnative.dev/docs/style#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
With React Native, you style your application using JavaScript. All of the core components accept a prop named `style`. The style names and [values](https://reactnative.dev/docs/colors) usually match how CSS works on the web, except names are written using camel casing, e.g. `backgroundColor` rather than `background-color`.
The `style` prop can be a plain old JavaScript object. That's what we usually use for example code. You can also pass an array of styles - the last style in the array has precedence, so you can use this to inherit styles.
As a component grows in complexity, it is often cleaner to use `StyleSheet.create` to define several styles in one place. Here's an example:
One common pattern is to make your component accept a `style` prop which in turn is used to style subcomponents. You can use this to make styles "cascade" the way they do in CSS.
There are a lot more ways to customize the text style. Check out the [Text component reference](https://reactnative.dev/docs/text) for a complete list.
Now you can make your text beautiful. The next step in becoming a style expert is to [learn how to control component size](https://reactnative.dev/docs/height-and-width).
## Known issues[​](https://reactnative.dev/docs/style#known-issues "Direct link to Known issues")
  * [react-native#29308](https://github.com/facebook/react-native/issues/29308#issuecomment-792864162): In some cases React Native does not match how CSS works on the web, for example the touch area never extends past the parent view bounds and on Android negative margin is not supported.


Is this page useful?



