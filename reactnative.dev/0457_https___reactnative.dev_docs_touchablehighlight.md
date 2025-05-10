---
url: https://reactnative.dev/docs/touchablehighlight
title: https://reactnative.dev/docs/touchablehighlight
date: 2025-05-10T21:42:38.848884
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/touchablehighlight#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
> If you're looking for a more extensive and future-proof way to handle touch-based input, check out the [Pressable](https://reactnative.dev/docs/pressable) API.
A wrapper for making views respond properly to touches. On press down, the opacity of the wrapped view is decreased, which allows the underlay color to show through, darkening or tinting the view.
The underlay comes from wrapping the child in a new View, which can affect layout, and sometimes cause unwanted visual artifacts if not used correctly, for example if the backgroundColor of the wrapped view isn't explicitly set to an opaque color.
TouchableHighlight must have one child (not zero or more than one). If you wish to have several child components, wrap them in a View.
tsx
```
functionMyComponent(props:MyComponentProps){return(<View{...props}style={{flex:1, backgroundColor:'#fff'}}><Text>My Component</Text></View><TouchableHighlightactiveOpacity={0.6}underlayColor="#DDDDDD"onPress={()=>alert('Pressed!')}><MyComponent/></TouchableHighlight>;
```

## Example[​](https://reactnative.dev/docs/touchablehighlight#example "Direct link to Example")
# Reference
## Props[​](https://reactnative.dev/docs/touchablehighlight#props "Direct link to Props")
### [TouchableWithoutFeedback Props](https://reactnative.dev/docs/touchablewithoutfeedback#props)[​](https://reactnative.dev/docs/touchablehighlight#touchablewithoutfeedback-props "Direct link to touchablewithoutfeedback-props")
Inherits [TouchableWithoutFeedback Props](https://reactnative.dev/docs/touchablewithoutfeedback#props).
### `activeOpacity`[​](https://reactnative.dev/docs/touchablehighlight#activeopacity "Direct link to activeopacity")
Determines what the opacity of the wrapped view should be when touch is active. The value should be between 0 and 1. Defaults to 0.85. Requires `underlayColor` to be set.
Type  
---  
number  
### `onHideUnderlay`[​](https://reactnative.dev/docs/touchablehighlight#onhideunderlay "Direct link to onhideunderlay")
Called immediately after the underlay is hidden.
Type  
---  
function  
### `onShowUnderlay`[​](https://reactnative.dev/docs/touchablehighlight#onshowunderlay "Direct link to onshowunderlay")
Called immediately after the underlay is shown.
Type  
---  
function  
### `style`[​](https://reactnative.dev/docs/touchablehighlight#style "Direct link to style")
Type  
---  
View.style  
### `underlayColor`[​](https://reactnative.dev/docs/touchablehighlight#underlaycolor "Direct link to underlaycolor")
The color of the underlay that will show through when the touch is active.
Type  
---  
### `hasTVPreferredFocus`
iOS
[​](https://reactnative.dev/docs/touchablehighlight#hastvpreferredfocus-ios "Direct link to hastvpreferredfocus-ios")
_(Apple TV only)_ TV preferred focus (see documentation for the View component).
Type  
---  
bool  
### `nextFocusDown`
Android
[​](https://reactnative.dev/docs/touchablehighlight#nextfocusdown-android "Direct link to nextfocusdown-android")
TV next focus down (see documentation for the View component).
Type  
---  
number  
### `nextFocusForward`
Android
[​](https://reactnative.dev/docs/touchablehighlight#nextfocusforward-android "Direct link to nextfocusforward-android")
TV next focus forward (see documentation for the View component).
Type  
---  
number  
### `nextFocusLeft`
Android
[​](https://reactnative.dev/docs/touchablehighlight#nextfocusleft-android "Direct link to nextfocusleft-android")
TV next focus left (see documentation for the View component).
Type  
---  
number  
### `nextFocusRight`
Android
[​](https://reactnative.dev/docs/touchablehighlight#nextfocusright-android "Direct link to nextfocusright-android")
TV next focus right (see documentation for the View component).
Type  
---  
number  
### `nextFocusUp`
Android
[​](https://reactnative.dev/docs/touchablehighlight#nextfocusup-android "Direct link to nextfocusup-android")
TV next focus up (see documentation for the View component).
Type  
---  
number  
### `testOnly_pressed`[​](https://reactnative.dev/docs/touchablehighlight#testonly_pressed "Direct link to testonly_pressed")
Handy for snapshot tests.
Type  
---  
bool  
Is this page useful?
  * [Props](https://reactnative.dev/docs/touchablehighlight#props)
    * [TouchableWithoutFeedback Props](https://reactnative.dev/docs/touchablehighlight#touchablewithoutfeedback-props)
    * [`hasTVPreferredFocus` iOS](https://reactnative.dev/docs/touchablehighlight#hastvpreferredfocus-ios)
    * [`nextFocusDown` Android](https://reactnative.dev/docs/touchablehighlight#nextfocusdown-android)
    * [`nextFocusForward` Android](https://reactnative.dev/docs/touchablehighlight#nextfocusforward-android)
    * [`nextFocusLeft` Android](https://reactnative.dev/docs/touchablehighlight#nextfocusleft-android)
    * [`nextFocusRight` Android](https://reactnative.dev/docs/touchablehighlight#nextfocusright-android)
    * [`nextFocusUp` Android](https://reactnative.dev/docs/touchablehighlight#nextfocusup-android)
    * [`testOnly_pressed`](https://reactnative.dev/docs/touchablehighlight#testonly_pressed)



