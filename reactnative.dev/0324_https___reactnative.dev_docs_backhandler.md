---
url: https://reactnative.dev/docs/backhandler
title: https://reactnative.dev/docs/backhandler
date: 2025-05-10T21:39:31.039087
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/backhandler#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
The Backhandler API detects hardware button presses for back navigation, lets you register event listeners for the system's back action, and lets you control how your application responds. It is Android-only.
The event subscriptions are called in reverse order (i.e. the last registered subscription is called first).
  * **If one subscription returns true,** then subscriptions registered earlier will not be called.
  * **If no subscription returns true or none are registered,** it programmatically invokes the default back button functionality to exit the app.


> **Warning for modal users:** If your app shows an opened `Modal`, `BackHandler` will not publish any events ([see `Modal` docs](https://reactnative.dev/docs/modal#onrequestclose)).
## Pattern[​](https://reactnative.dev/docs/backhandler#pattern "Direct link to Pattern")
tsx
```
const subscription =BackHandler.addEventListener('hardwareBackPress',function(){/**   * this.onMainScreen and this.goBack are just examples,   * you need to use your own implementation here.   * Typically you would use the navigator here to go to the last state.   */if(!this.onMainScreen()){this.goBack();/**    * When true is returned the event will not be bubbled up    * & no other back action will execute    */returntrue;/**   * Returning false will let the event to bubble up & let other event listeners   * or the system's default back action to be executed.   */returnfalse;// Unsubscribe the listener on unmountsubscription.remove();
```

## Example[​](https://reactnative.dev/docs/backhandler#example "Direct link to Example")
The following example implements a scenario where you confirm if the user wants to exit the app:
`BackHandler.addEventListener` creates an event listener & returns a `NativeEventSubscription` object which should be cleared using `NativeEventSubscription.remove` method.
## Usage with React Navigation[​](https://reactnative.dev/docs/backhandler#usage-with-react-navigation "Direct link to Usage with React Navigation")
If you are using React Navigation to navigate across different screens, you can follow their guide on [Custom Android back button behaviour](https://reactnavigation.org/docs/custom-android-back-button-handling/)
## Backhandler hook[​](https://reactnative.dev/docs/backhandler#backhandler-hook "Direct link to Backhandler hook")
[React Native Hooks](https://github.com/react-native-community/hooks#usebackhandler) has a nice `useBackHandler` hook which will simplify the process of setting up event listeners.
# Reference
## Methods[​](https://reactnative.dev/docs/backhandler#methods "Direct link to Methods")
### `addEventListener()`[​](https://reactnative.dev/docs/backhandler#addeventlistener "Direct link to addeventlistener")
tsx
```
staticaddEventListener( eventName:BackPressEventName,handler:()=>boolean|null|undefined,):NativeEventSubscription;
```

### `exitApp()`[​](https://reactnative.dev/docs/backhandler#exitapp "Direct link to exitapp")
tsx
```
staticexitApp();
```

Is this page useful?
  * [Usage with React Navigation](https://reactnative.dev/docs/backhandler#usage-with-react-navigation)
  * [Backhandler hook](https://reactnative.dev/docs/backhandler#backhandler-hook)
  * [Methods](https://reactnative.dev/docs/backhandler#methods)
    * [`addEventListener()`](https://reactnative.dev/docs/backhandler#addeventlistener)



