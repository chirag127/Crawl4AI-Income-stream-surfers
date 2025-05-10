---
url: https://reactnative.dev/docs/handling-touches
title: https://reactnative.dev/docs/handling-touches
date: 2025-05-10T21:40:25.800765
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/handling-touches#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
Users interact with mobile apps mainly through touch. They can use a combination of gestures, such as tapping on a button, scrolling a list, or zooming on a map. React Native provides components to handle all sorts of common gestures, as well as a comprehensive [gesture responder system](https://reactnative.dev/docs/gesture-responder-system) to allow for more advanced gesture recognition, but the one component you will most likely be interested in is the basic Button.
## Displaying a basic button[​](https://reactnative.dev/docs/handling-touches#displaying-a-basic-button "Direct link to Displaying a basic button")
[Button](https://reactnative.dev/docs/button) provides a basic button component that is rendered nicely on all platforms. The minimal example to display a button looks like this:
tsx
```
<ButtononPress={()=>{console.log('You tapped the button!');title="Press Me"/>
```

This will render a blue label on iOS, and a blue rounded rectangle with light text on Android. Pressing the button will call the "onPress" function, which in this case displays an alert popup. If you like, you can specify a "color" prop to change the color of your button.
Go ahead and play around with the `Button` component using the example below. You can select which platform your app is previewed in by clicking on the toggle in the bottom right and then clicking on "Tap to Play" to preview the app.
## Touchables[​](https://reactnative.dev/docs/handling-touches#touchables "Direct link to Touchables")
If the basic button doesn't look right for your app, you can build your own button using any of the "Touchable" components provided by React Native. These components provide the capability to capture tapping gestures and can display feedback when a gesture is recognized. However, these components do not provide any default styling, so you will need to do a bit of work to get them looking nice in your app.
Which "Touchable" component you use will depend on what kind of feedback you want to provide:
  * Generally, you can use [**TouchableHighlight**](https://reactnative.dev/docs/touchablehighlight) anywhere you would use a button or link on web. The view's background will be darkened when the user presses down on the button.
  * You may consider using [**TouchableNativeFeedback**](https://reactnative.dev/docs/touchablenativefeedback) on Android to display ink surface reaction ripples that respond to the user's touch.
  * [**TouchableOpacity**](https://reactnative.dev/docs/touchableopacity) can be used to provide feedback by reducing the opacity of the button, allowing the background to be seen through while the user is pressing down.
  * If you need to handle a tap gesture but you don't want any feedback to be displayed, use [**TouchableWithoutFeedback**](https://reactnative.dev/docs/touchablewithoutfeedback).


In some cases, you may want to detect when a user presses and holds a view for a set amount of time. These long presses can be handled by passing a function to the `onLongPress` props of any of the "Touchable" components.
Let's see all of these in action:
## Scrolling and swiping[​](https://reactnative.dev/docs/handling-touches#scrolling-and-swiping "Direct link to Scrolling and swiping")
Gestures commonly used on devices with touchable screens include swipes and pans. These allow the user to scroll through a list of items, or swipe through pages of content. For these, check out the [ScrollView](https://reactnative.dev/docs/scrollview) Core Component.
## Known issues[​](https://reactnative.dev/docs/handling-touches#known-issues "Direct link to Known issues")
  * [react-native#29308](https://github.com/facebook/react-native/issues/29308#issuecomment-792864162): The touch area never extends past the parent view bounds and on Android negative margin is not supported.


Is this page useful?
  * [Displaying a basic button](https://reactnative.dev/docs/handling-touches#displaying-a-basic-button)
  * [Scrolling and swiping](https://reactnative.dev/docs/handling-touches#scrolling-and-swiping)



