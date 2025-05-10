---
url: https://reactnative.dev/docs/button
title: https://reactnative.dev/docs/button
date: 2025-05-10T21:39:44.356734
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/button#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
A basic button component that should render nicely on any platform. Supports a minimal level of customization.
If this button doesn't look right for your app, you can build your own button using [Pressable](https://reactnative.dev/docs/pressable). For inspiration, look at the [source code for the Button component](https://github.com/facebook/react-native/blob/main/packages/react-native/Libraries/Components/Button.js).
tsx
```
<ButtononPress={onPressLearnMore}title="Learn More"color="#841584"accessibilityLabel="Learn more about this purple button"/>
```

## Example[​](https://reactnative.dev/docs/button#example "Direct link to Example")
# Reference
## Props[​](https://reactnative.dev/docs/button#props "Direct link to Props")
### 
Required
**`onPress`**[​](https://reactnative.dev/docs/button#requiredonpress "Direct link to requiredonpress")
Handler to be called when the user taps the button.
Type  
---  
`({nativeEvent: PressEvent[](https://reactnative.dev/docs/pressevent)})`  
### 
Required
**`title`**[​](https://reactnative.dev/docs/button#requiredtitle "Direct link to requiredtitle")
Text to display inside the button. On Android the given title will be converted to the uppercased form.
Type  
---  
string  
### `accessibilityLabel`[​](https://reactnative.dev/docs/button#accessibilitylabel "Direct link to accessibilitylabel")
Text to display for blindness accessibility features.
Type  
---  
string  
### `accessibilityLanguage`
iOS
[​](https://reactnative.dev/docs/button#accessibilitylanguage-ios "Direct link to accessibilitylanguage-ios")
A value indicating which language should be used by the screen reader when the user interacts with the element. It should follow the [BCP 47 specification](https://www.rfc-editor.org/info/bcp47).
See the [iOS `accessibilityLanguage` doc](https://developer.apple.com/documentation/objectivec/nsobject/1615192-accessibilitylanguage) for more information.
Type  
---  
string  
### `accessibilityActions`[​](https://reactnative.dev/docs/button#accessibilityactions "Direct link to accessibilityactions")
Accessibility actions allow an assistive technology to programmatically invoke the actions of a component. The `accessibilityActions` property should contain a list of action objects. Each action object should contain the field name and label.
See the [Accessibility guide](https://reactnative.dev/docs/accessibility#accessibility-actions) for more information.
Type| Required  
---|---  
array| No  
### `onAccessibilityAction`[​](https://reactnative.dev/docs/button#onaccessibilityaction "Direct link to onaccessibilityaction")
Invoked when the user performs the accessibility actions. The only argument to this function is an event containing the name of the action to perform.
See the [Accessibility guide](https://reactnative.dev/docs/accessibility#accessibility-actions) for more information.
Type| Required  
---|---  
function| No  
### `color`[​](https://reactnative.dev/docs/button#color "Direct link to color")
Color of the text (iOS), or background color of the button (Android).
Type| Default  
---|---  
`'#2196F3'` Android `'#007AFF'` iOS  
### `disabled`[​](https://reactnative.dev/docs/button#disabled "Direct link to disabled")
If `true`, disable all interactions for this component.
Type| Default  
---|---  
bool| `false`  
### `hasTVPreferredFocus`
TV
[​](https://reactnative.dev/docs/button#hastvpreferredfocus-tv "Direct link to hastvpreferredfocus-tv")
TV preferred focus.
Type| Default  
---|---  
bool| `false`  
### `nextFocusDown`
Android
TV
[​](https://reactnative.dev/docs/button#nextfocusdown-androidtv "Direct link to nextfocusdown-androidtv")
Designates the next view to receive focus when the user navigates down. See the [Android documentation](https://developer.android.com/reference/android/view/View.html#attr_android:nextFocusDown).
Type  
---  
number  
### `nextFocusForward`
Android
TV
[​](https://reactnative.dev/docs/button#nextfocusforward-androidtv "Direct link to nextfocusforward-androidtv")
Designates the next view to receive focus when the user navigates forward. See the [Android documentation](https://developer.android.com/reference/android/view/View.html#attr_android:nextFocusForward).
Type  
---  
number  
### `nextFocusLeft`
Android
TV
[​](https://reactnative.dev/docs/button#nextfocusleft-androidtv "Direct link to nextfocusleft-androidtv")
Designates the next view to receive focus when the user navigates left. See the [Android documentation](https://developer.android.com/reference/android/view/View.html#attr_android:nextFocusLeft).
Type  
---  
number  
### `nextFocusRight`
Android
TV
[​](https://reactnative.dev/docs/button#nextfocusright-androidtv "Direct link to nextfocusright-androidtv")
Designates the next view to receive focus when the user navigates right. See the [Android documentation](https://developer.android.com/reference/android/view/View.html#attr_android:nextFocusRight).
Type  
---  
number  
### `nextFocusUp`
Android
TV
[​](https://reactnative.dev/docs/button#nextfocusup-androidtv "Direct link to nextfocusup-androidtv")
Designates the next view to receive focus when the user navigates up. See the [Android documentation](https://developer.android.com/reference/android/view/View.html#attr_android:nextFocusUp).
Type  
---  
number  
### `testID`[​](https://reactnative.dev/docs/button#testid "Direct link to testid")
Used to locate this view in end-to-end tests.
Type  
---  
string  
### `touchSoundDisabled`
Android
[​](https://reactnative.dev/docs/button#touchsounddisabled-android "Direct link to touchsounddisabled-android")
If `true`, doesn't play system sound on touch.
Type| Default  
---|---  
boolean| `false`  
Is this page useful?
  * [Props](https://reactnative.dev/docs/button#props)
    * [Required**`onPress`**](https://reactnative.dev/docs/button#requiredonpress)
    * [Required**`title`**](https://reactnative.dev/docs/button#requiredtitle)
    * [`accessibilityLabel`](https://reactnative.dev/docs/button#accessibilitylabel)
    * [`accessibilityLanguage` iOS](https://reactnative.dev/docs/button#accessibilitylanguage-ios)
    * [`accessibilityActions`](https://reactnative.dev/docs/button#accessibilityactions)
    * [`onAccessibilityAction`](https://reactnative.dev/docs/button#onaccessibilityaction)
    * [`hasTVPreferredFocus` TV](https://reactnative.dev/docs/button#hastvpreferredfocus-tv)
    * [`nextFocusDown` AndroidTV](https://reactnative.dev/docs/button#nextfocusdown-androidtv)
    * [`nextFocusForward` AndroidTV](https://reactnative.dev/docs/button#nextfocusforward-androidtv)
    * [`nextFocusLeft` AndroidTV](https://reactnative.dev/docs/button#nextfocusleft-androidtv)
    * [`nextFocusRight` AndroidTV](https://reactnative.dev/docs/button#nextfocusright-androidtv)
    * [`nextFocusUp` AndroidTV](https://reactnative.dev/docs/button#nextfocusup-androidtv)
    * [`touchSoundDisabled` Android](https://reactnative.dev/docs/button#touchsounddisabled-android)



