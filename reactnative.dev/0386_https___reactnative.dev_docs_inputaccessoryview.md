---
url: https://reactnative.dev/docs/inputaccessoryview
title: https://reactnative.dev/docs/inputaccessoryview
date: 2025-05-10T21:40:35.120263
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/inputaccessoryview#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
A component which enables customization of the keyboard input accessory view on iOS. The input accessory view is displayed above the keyboard whenever a `TextInput` has focus. This component can be used to create custom toolbars.
To use this component wrap your custom toolbar with the InputAccessoryView component, and set a `nativeID`. Then, pass that `nativeID` as the `inputAccessoryViewID` of whatever `TextInput` you desire. A basic example:
This component can also be used to create sticky text inputs (text inputs which are anchored to the top of the keyboard). To do this, wrap a `TextInput` with the `InputAccessoryView` component, and don't set a `nativeID`. For an example, look at [InputAccessoryViewExample.js](https://github.com/facebook/react-native/blob/main/packages/rn-tester/js/examples/InputAccessoryView/InputAccessoryViewExample.js).
# Reference
## Props[​](https://reactnative.dev/docs/inputaccessoryview#props "Direct link to Props")
### `backgroundColor`[​](https://reactnative.dev/docs/inputaccessoryview#backgroundcolor "Direct link to backgroundcolor")
Type  
---  
### `nativeID`[​](https://reactnative.dev/docs/inputaccessoryview#nativeid "Direct link to nativeid")
An ID which is used to associate this `InputAccessoryView` to specified TextInput(s).
Type  
---  
string  
### `style`[​](https://reactnative.dev/docs/inputaccessoryview#style "Direct link to style")
Type  
---  
# Known issues
  * [react-native#18997](https://github.com/facebook/react-native/issues/18997): Doesn't support multiline `TextInput`
  * [react-native#20157](https://github.com/facebook/react-native/issues/20157): Can't use with a bottom tab bar


Is this page useful?
  * [Props](https://reactnative.dev/docs/inputaccessoryview#props)



