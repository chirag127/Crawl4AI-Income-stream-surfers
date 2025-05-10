---
url: https://reactnative.dev/docs/switch
title: https://reactnative.dev/docs/switch
date: 2025-05-10T21:42:14.717924
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/switch#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
Renders a boolean input.
This is a controlled component that requires an `onValueChange` callback that updates the `value` prop in order for the component to reflect user actions. If the `value` prop is not updated, the component will continue to render the supplied `value` prop instead of the expected result of any user actions.
## Example[​](https://reactnative.dev/docs/switch#example "Direct link to Example")
# Reference
## Props[​](https://reactnative.dev/docs/switch#props "Direct link to Props")
### [View Props](https://reactnative.dev/docs/view#props)[​](https://reactnative.dev/docs/switch#view-props "Direct link to view-props")
Inherits [View Props](https://reactnative.dev/docs/view#props).
### `disabled`[​](https://reactnative.dev/docs/switch#disabled "Direct link to disabled")
If true the user won't be able to toggle the switch.
Type| Default  
---|---  
bool| `false`  
### `ios_backgroundColor`
iOS
[​](https://reactnative.dev/docs/switch#ios_backgroundcolor-ios "Direct link to ios_backgroundcolor-ios")
On iOS, custom color for the background. This background color can be seen either when the switch value is `false` or when the switch is disabled (and the switch is translucent).
Type  
---  
### `onChange`[​](https://reactnative.dev/docs/switch#onchange "Direct link to onchange")
Invoked when the user tries to change the value of the switch. Receives the change event as an argument. If you want to only receive the new value, use `onValueChange` instead.
Type  
---  
function  
### `onValueChange`[​](https://reactnative.dev/docs/switch#onvaluechange "Direct link to onvaluechange")
Invoked when the user tries to change the value of the switch. Receives the new value as an argument. If you want to instead receive an event, use `onChange`.
Type  
---  
function  
### `thumbColor`[​](https://reactnative.dev/docs/switch#thumbcolor "Direct link to thumbcolor")
Color of the foreground switch grip. If this is set on iOS, the switch grip will lose its drop shadow.
Type  
---  
### `trackColor`[​](https://reactnative.dev/docs/switch#trackcolor "Direct link to trackcolor")
Custom colors for the switch track.
_iOS_ : When the switch value is `false`, the track shrinks into the border. If you want to change the color of the background exposed by the shrunken track, use [`ios_backgroundColor`](https://reactnative.dev/docs/switch#ios_backgroundColor).
Type  
---  
`object: {false: color[](https://reactnative.dev/docs/colors), true: color[](https://reactnative.dev/docs/colors)}`  
### `value`[​](https://reactnative.dev/docs/switch#value "Direct link to value")
The value of the switch. If true the switch will be turned on. Default value is false.
Type  
---  
bool  
Is this page useful?
  * [Props](https://reactnative.dev/docs/switch#props)
    * [`ios_backgroundColor` iOS](https://reactnative.dev/docs/switch#ios_backgroundcolor-ios)



