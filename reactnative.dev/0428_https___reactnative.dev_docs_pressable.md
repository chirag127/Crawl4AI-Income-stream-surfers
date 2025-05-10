---
url: https://reactnative.dev/docs/pressable
title: https://reactnative.dev/docs/pressable
date: 2025-05-10T21:41:45.274699
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/pressable#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
Pressable is a Core Component wrapper that can detect various stages of press interactions on any of its defined children.
tsx
```
<PressableonPress={onPressFunction}><Text>I'm pressable!</Text></Pressable>
```

## How it works[​](https://reactnative.dev/docs/pressable#how-it-works "Direct link to How it works")
On an element wrapped by `Pressable`:
  * [`onPressIn`](https://reactnative.dev/docs/pressable#onpressin) is called when a press is activated.
  * [`onPressOut`](https://reactnative.dev/docs/pressable#onpressout) is called when the press gesture is deactivated.


After pressing [`onPressIn`](https://reactnative.dev/docs/pressable#onpressin), one of two things will happen:
  1. The person will remove their finger, triggering [`onPressOut`](https://reactnative.dev/docs/pressable#onpressout) followed by [`onPress`](https://reactnative.dev/docs/pressable#onpress).
  2. If the person leaves their finger longer than 500 milliseconds before removing it, [`onLongPress`](https://reactnative.dev/docs/pressable#onlongpress) is triggered. ([`onPressOut`](https://reactnative.dev/docs/pressable#onpressout) will still fire when they remove their finger.)


Fingers are not the most precise instruments, and it is common for users to accidentally activate the wrong element or miss the activation area. To help, `Pressable` has an optional `HitRect` you can use to define how far a touch can register away from the wrapped element. Presses can start anywhere within a `HitRect`.
`PressRect` allows presses to move beyond the element and its `HitRect` while maintaining activation and being eligible for a "press"—think of sliding your finger slowly away from a button you're pressing down on.
> The touch area never extends past the parent view bounds and the Z-index of sibling views always takes precedence if a touch hits two overlapping views.
You can set `HitRect` with `hitSlop` and set `PressRect` with `pressRetentionOffset`.
> `Pressable` uses React Native's `Pressability` API. For more information around the state machine flow of Pressability and how it works, check out the implementation for [Pressability](https://github.com/facebook/react-native/blob/main/packages/react-native/Libraries/Pressability/Pressability.js#L350).
## Example[​](https://reactnative.dev/docs/pressable#example "Direct link to Example")
## Props[​](https://reactnative.dev/docs/pressable#props "Direct link to Props")
### `android_disableSound`
Android
[​](https://reactnative.dev/docs/pressable#android_disablesound-android "Direct link to android_disablesound-android")
If true, doesn't play Android system sound on press.
Type| Default  
---|---  
boolean| `false`  
### `android_ripple`
Android
[​](https://reactnative.dev/docs/pressable#android_ripple-android "Direct link to android_ripple-android")
Enables the Android ripple effect and configures its properties.
Type  
---  
### `children`[​](https://reactnative.dev/docs/pressable#children "Direct link to children")
Either children or a function that receives a boolean reflecting whether the component is currently pressed.
Type  
---  
### `unstable_pressDelay`[​](https://reactnative.dev/docs/pressable#unstable_pressdelay "Direct link to unstable_pressdelay")
Duration (in milliseconds) to wait after press down before calling `onPressIn`.
Type  
---  
number  
### `delayLongPress`[​](https://reactnative.dev/docs/pressable#delaylongpress "Direct link to delaylongpress")
Duration (in milliseconds) from `onPressIn` before `onLongPress` is called.
Type| Default  
---|---  
number| `500`  
### `disabled`[​](https://reactnative.dev/docs/pressable#disabled "Direct link to disabled")
Whether the press behavior is disabled.
Type| Default  
---|---  
boolean| `false`  
### `hitSlop`[​](https://reactnative.dev/docs/pressable#hitslop "Direct link to hitslop")
Sets additional distance outside of element in which a press can be detected.
Type  
---  
[Rect](https://reactnative.dev/docs/rect) or number  
### `onHoverIn`[​](https://reactnative.dev/docs/pressable#onhoverin "Direct link to onhoverin")
Called when the hover is activated to provide visual feedback.
Type  
---  
`({ nativeEvent: MouseEvent[](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent) }) => void`  
### `onHoverOut`[​](https://reactnative.dev/docs/pressable#onhoverout "Direct link to onhoverout")
Called when the hover is deactivated to undo visual feedback.
Type  
---  
`({ nativeEvent: MouseEvent[](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent) }) => void`  
### `onLongPress`[​](https://reactnative.dev/docs/pressable#onlongpress "Direct link to onlongpress")
Called if the time after `onPressIn` lasts longer than 500 milliseconds. This time period can be customized with [`delayLongPress`](https://reactnative.dev/docs/pressable#delaylongpress).
Type  
---  
`({nativeEvent: PressEvent[](https://reactnative.dev/docs/pressevent)}) => void`  
### `onPress`[​](https://reactnative.dev/docs/pressable#onpress "Direct link to onpress")
Called after `onPressOut`.
Type  
---  
`({nativeEvent: PressEvent[](https://reactnative.dev/docs/pressevent)}) => void`  
### `onPressIn`[​](https://reactnative.dev/docs/pressable#onpressin "Direct link to onpressin")
Called immediately when a touch is engaged, before `onPressOut` and `onPress`.
Type  
---  
`({nativeEvent: PressEvent[](https://reactnative.dev/docs/pressevent)}) => void`  
### `onPressOut`[​](https://reactnative.dev/docs/pressable#onpressout "Direct link to onpressout")
Called when a touch is released.
Type  
---  
`({nativeEvent: PressEvent[](https://reactnative.dev/docs/pressevent)}) => void`  
### `pressRetentionOffset`[​](https://reactnative.dev/docs/pressable#pressretentionoffset "Direct link to pressretentionoffset")
Additional distance outside of this view in which a touch is considered a press before `onPressOut` is triggered.
Type| Default  
---|---  
[Rect](https://reactnative.dev/docs/rect) or number| `{bottom: 30, left: 20, right: 20, top: 20}`  
### `style`[​](https://reactnative.dev/docs/pressable#style "Direct link to style")
Either view styles or a function that receives a boolean reflecting whether the component is currently pressed and returns view styles.
Type  
---  
[View Style](https://reactnative.dev/docs/view-style-props) or `({ pressed: boolean }) => View Style[](https://reactnative.dev/docs/view-style-props)`  
### `testOnly_pressed`[​](https://reactnative.dev/docs/pressable#testonly_pressed "Direct link to testonly_pressed")
Used only for documentation or testing (e.g. snapshot testing).
Type| Default  
---|---  
boolean| `false`  
## Type Definitions[​](https://reactnative.dev/docs/pressable#type-definitions "Direct link to Type Definitions")
### RippleConfig[​](https://reactnative.dev/docs/pressable#rippleconfig "Direct link to RippleConfig")
Ripple effect configuration for the `android_ripple` property.
Type  
---  
object  
**Properties:**
Name| Type| Required| Description  
---|---|---|---  
color| No| Defines the color of the ripple effect.  
borderless| boolean| No| Defines if ripple effect should not include border.  
radius| number| No| Defines the radius of the ripple effect.  
foreground| boolean| No| Set to true to add the ripple effect to the foreground of the view, instead of the background. This is useful if one of your child views has a background of its own, or you're e.g. displaying images, and you don't want the ripple to be covered by them.  
Is this page useful?
  * [Props](https://reactnative.dev/docs/pressable#props)
    * [`android_disableSound` Android](https://reactnative.dev/docs/pressable#android_disablesound-android)
    * [`android_ripple` Android](https://reactnative.dev/docs/pressable#android_ripple-android)
    * [`unstable_pressDelay`](https://reactnative.dev/docs/pressable#unstable_pressdelay)
    * [`pressRetentionOffset`](https://reactnative.dev/docs/pressable#pressretentionoffset)
    * [`testOnly_pressed`](https://reactnative.dev/docs/pressable#testonly_pressed)
  * [Type Definitions](https://reactnative.dev/docs/pressable#type-definitions)



