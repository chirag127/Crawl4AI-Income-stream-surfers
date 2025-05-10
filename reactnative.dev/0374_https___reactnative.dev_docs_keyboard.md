---
url: https://reactnative.dev/docs/keyboard
title: https://reactnative.dev/docs/keyboard
date: 2025-05-10T21:40:25.802442
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/keyboard#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
`Keyboard` module to control keyboard events.
### Usage[​](https://reactnative.dev/docs/keyboard#usage "Direct link to Usage")
The Keyboard module allows you to listen for native events and react to them, as well as make changes to the keyboard, like dismissing it.
# Reference
## Methods[​](https://reactnative.dev/docs/keyboard#methods "Direct link to Methods")
### `addListener()`[​](https://reactnative.dev/docs/keyboard#addlistener "Direct link to addlistener")
tsx
```
staticaddListener:( eventType:KeyboardEventName, listener:KeyboardEventListener,)=>EmitterSubscription;
```

The `addListener` function connects a JavaScript function to an identified native keyboard notification event.
This function then returns the reference to the listener.
**Parameters:**
Name| Type| Description  
---|---|---  
eventName Required| string| The string that identifies the event you're listening for. See the list below.  
callback Required| function| The function to be called when the event fires  
**`eventName`**
This can be any of the following:
  * `keyboardWillShow`
  * `keyboardDidShow`
  * `keyboardWillHide`
  * `keyboardDidHide`
  * `keyboardWillChangeFrame`
  * `keyboardDidChangeFrame`


> Note that only `keyboardDidShow` and `keyboardDidHide` events are available on Android. The events will not be fired when using Android 10 and under if your activity has `android:windowSoftInputMode` set to `adjustNothing`.
### `dismiss()`[​](https://reactnative.dev/docs/keyboard#dismiss "Direct link to dismiss")
tsx
```
staticdismiss();
```

Dismisses the active keyboard and removes focus.
### `scheduleLayoutAnimation`[​](https://reactnative.dev/docs/keyboard#schedulelayoutanimation "Direct link to schedulelayoutanimation")
tsx
```
staticscheduleLayoutAnimation(event:KeyboardEvent);
```

Useful for syncing TextInput (or other keyboard accessory view) size of position changes with keyboard movements.
### `isVisible()`[​](https://reactnative.dev/docs/keyboard#isvisible "Direct link to isvisible")
tsx
```
staticisVisible():boolean;
```

Whether the keyboard is last known to be visible.
### `metrics()`[​](https://reactnative.dev/docs/keyboard#metrics "Direct link to metrics")
tsx
```
staticmetrics():KeyboardMetrics|undefined;
```

Return the metrics of the soft-keyboard if visible.
Is this page useful?
  * [Methods](https://reactnative.dev/docs/keyboard#methods)
    * [`scheduleLayoutAnimation`](https://reactnative.dev/docs/keyboard#schedulelayoutanimation)



