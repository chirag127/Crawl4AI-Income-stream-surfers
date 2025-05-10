---
url: https://reactnative.dev/docs/keyboardavoidingview
title: https://reactnative.dev/docs/keyboardavoidingview
date: 2025-05-10T21:40:25.797419
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/keyboardavoidingview#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
This component will automatically adjust its height, position, or bottom padding based on the keyboard height to remain visible while the virtual keyboard is displayed.
## Example[​](https://reactnative.dev/docs/keyboardavoidingview#example "Direct link to Example")
# Reference
## Props[​](https://reactnative.dev/docs/keyboardavoidingview#props "Direct link to Props")
### [View Props](https://reactnative.dev/docs/view#props)[​](https://reactnative.dev/docs/keyboardavoidingview#view-props "Direct link to view-props")
Inherits [View Props](https://reactnative.dev/docs/view#props).
### `behavior`[​](https://reactnative.dev/docs/keyboardavoidingview#behavior "Direct link to behavior")
Specify how to react to the presence of the keyboard.
> Android and iOS both interact with this prop differently. On both iOS and Android, setting `behavior` is recommended.
Type  
---  
enum(`'height'`, `'position'`, `'padding'`)  
### `contentContainerStyle`[​](https://reactnative.dev/docs/keyboardavoidingview#contentcontainerstyle "Direct link to contentcontainerstyle")
The style of the content container (View) when behavior is `'position'`.
Type  
---  
### `enabled`[​](https://reactnative.dev/docs/keyboardavoidingview#enabled "Direct link to enabled")
Enabled or disabled KeyboardAvoidingView.
Type| Default  
---|---  
boolean| `true`  
### `keyboardVerticalOffset`[​](https://reactnative.dev/docs/keyboardavoidingview#keyboardverticaloffset "Direct link to keyboardverticaloffset")
This is the distance between the top of the user screen and the react native view, may be non-zero in some use cases.
Type| Default  
---|---  
number  
Is this page useful?
  * [Props](https://reactnative.dev/docs/keyboardavoidingview#props)
    * [`contentContainerStyle`](https://reactnative.dev/docs/keyboardavoidingview#contentcontainerstyle)
    * [`keyboardVerticalOffset`](https://reactnative.dev/docs/keyboardavoidingview#keyboardverticaloffset)



