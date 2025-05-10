---
url: https://reactnative.dev/docs/appstate
title: https://reactnative.dev/docs/appstate
date: 2025-05-10T21:39:30.315179
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/appstate#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
`AppState` can tell you if the app is in the foreground or background, and notify you when the state changes.
AppState is frequently used to determine the intent and proper behavior when handling push notifications.
### App States[​](https://reactnative.dev/docs/appstate#app-states "Direct link to App States")
  * `active` - The app is running in the foreground
  * `background` - The app is running in the background. The user is either: 
    * in another app
    * on the home screen
    * [Android] on another `Activity` (even if it was launched by your app)
  * [iOS] `inactive` - This is a state that occurs when transitioning between foreground & background, and during periods of inactivity such as entering the multitasking view, opening the Notification Center or in the event of an incoming call.


For more information, see [Apple's documentation](https://developer.apple.com/documentation/uikit/app_and_scenes/managing_your_app_s_life_cycle)
## Basic Usage[​](https://reactnative.dev/docs/appstate#basic-usage "Direct link to Basic Usage")
To see the current state, you can check `AppState.currentState`, which will be kept up-to-date. However, `currentState` will be null at launch while `AppState` retrieves it over the bridge.
This example will only ever appear to say "Current state is: active" because the app is only visible to the user when in the `active` state, and the null state will happen only momentarily. If you want to experiment with the code we recommend to use your own device instead of embedded preview.
# Reference
## Events[​](https://reactnative.dev/docs/appstate#events "Direct link to Events")
### `change`[​](https://reactnative.dev/docs/appstate#change "Direct link to change")
This event is received when the app state has changed. The listener is called with one of [the current app state values](https://reactnative.dev/docs/appstate#app-states).
### `memoryWarning`[​](https://reactnative.dev/docs/appstate#memorywarning "Direct link to memorywarning")
This event is used in the need of throwing memory warning or releasing it.
### `focus`
Android
[​](https://reactnative.dev/docs/appstate#focus-android "Direct link to focus-android")
Received when the app gains focus (the user is interacting with the app).
### `blur`
Android
[​](https://reactnative.dev/docs/appstate#blur-android "Direct link to blur-android")
Received when the user is not actively interacting with the app. Useful in situations when the user pulls down the [notification drawer](https://developer.android.com/guide/topics/ui/notifiers/notifications#bar-and-drawer). `AppState` won't change but the `blur` event will get fired.
## Methods[​](https://reactnative.dev/docs/appstate#methods "Direct link to Methods")
### `addEventListener()`[​](https://reactnative.dev/docs/appstate#addeventlistener "Direct link to addeventlistener")
tsx
```
staticaddEventListener( type:AppStateEvent,listener:(state:AppStateStatus)=>void,):NativeEventSubscription;
```

Sets up a function that will be called whenever the specified event type on AppState occurs. Valid values for `eventType` are [listed above](https://reactnative.dev/docs/appstate#events). Returns the `EventSubscription`.
## Properties[​](https://reactnative.dev/docs/appstate#properties "Direct link to Properties")
### `currentState`[​](https://reactnative.dev/docs/appstate#currentstate "Direct link to currentstate")
tsx
```
static currentState:AppStateStatus;
```

Is this page useful?
  * [Events](https://reactnative.dev/docs/appstate#events)
    * [`focus` Android](https://reactnative.dev/docs/appstate#focus-android)
    * [`blur` Android](https://reactnative.dev/docs/appstate#blur-android)
  * [Methods](https://reactnative.dev/docs/appstate#methods)
    * [`addEventListener()`](https://reactnative.dev/docs/appstate#addeventlistener)
  * [Properties](https://reactnative.dev/docs/appstate#properties)



