---
url: https://reactnative.dev/docs/next/accessibilityinfo
title: https://reactnative.dev/docs/next/accessibilityinfo
date: 2025-05-10T21:41:07.217163
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/next/accessibilityinfo#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
This is unreleased documentation for React Native **Next** version.
For up-to-date documentation, see the (0.79).
Version: Next
On this page
Sometimes it's useful to know whether or not the device has a screen reader that is currently active. The `AccessibilityInfo` API is designed for this purpose. You can use it to query the current state of the screen reader as well as to register to be notified when the state of the screen reader changes.
## Example[​](https://reactnative.dev/docs/next/accessibilityinfo#example "Direct link to Example")
# Reference
## Methods[​](https://reactnative.dev/docs/next/accessibilityinfo#methods "Direct link to Methods")
### `addEventListener()`[​](https://reactnative.dev/docs/next/accessibilityinfo#addeventlistener "Direct link to addeventlistener")
tsx
```
staticaddEventListener( eventName:AccessibilityChangeEventName|AccessibilityAnnouncementEventName,handler:(  event:AccessibilityChangeEvent|AccessibilityAnnouncementFinishedEvent,)=>void,):EmitterSubscription;
```

Add an event handler. Supported events:
Event name| Description  
---|---  
`accessibilityServiceChanged`Android| Fires when some services such as TalkBack, other Android assistive technologies, and third-party accessibility services are enabled. The argument to the event handler is a boolean. The boolean is `true` when a some accessibility services is enabled and `false` otherwise.  
`announcementFinished`iOS| Fires when the screen reader has finished making an announcement. The argument to the event handler is a dictionary with these keys:
  * `announcement`: The string announced by the screen reader.
  * `success`: A boolean indicating whether the announcement was successfully made.

  
`boldTextChanged`iOS| Fires when the state of the bold text toggle changes. The argument to the event handler is a boolean. The boolean is `true` when bold text is enabled and `false` otherwise.  
`grayscaleChanged`iOS| Fires when the state of the gray scale toggle changes. The argument to the event handler is a boolean. The boolean is `true` when a gray scale is enabled and `false` otherwise.  
`invertColorsChanged`iOS| Fires when the state of the invert colors toggle changes. The argument to the event handler is a boolean. The boolean is `true` when invert colors is enabled and `false` otherwise.  
`reduceMotionChanged`| Fires when the state of the reduce motion toggle changes. The argument to the event handler is a boolean. The boolean is `true` when a reduce motion is enabled (or when "Transition Animation Scale" in "Developer options" is "Animation off") and `false` otherwise.  
`reduceTransparencyChanged`iOS| Fires when the state of the reduce transparency toggle changes. The argument to the event handler is a boolean. The boolean is `true` when reduce transparency is enabled and `false` otherwise.  
`screenReaderChanged`| Fires when the state of the screen reader changes. The argument to the event handler is a boolean. The boolean is `true` when a screen reader is enabled and `false` otherwise.  
### `announceForAccessibility()`[​](https://reactnative.dev/docs/next/accessibilityinfo#announceforaccessibility "Direct link to announceforaccessibility")
tsx
```
staticannounceForAccessibility(announcement:string);
```

Post a string to be announced by the screen reader.
### `announceForAccessibilityWithOptions()`[​](https://reactnative.dev/docs/next/accessibilityinfo#announceforaccessibilitywithoptions "Direct link to announceforaccessibilitywithoptions")
tsx
```
staticannounceForAccessibilityWithOptions( announcement:string, options: options:{queue?:boolean},
```

Post a string to be announced by the screen reader with modification options. By default announcements will interrupt any existing speech, but on iOS they can be queued behind existing speech by setting `queue` to `true` in the options object.
**Parameters:**
Name| Type| Description  
---|---|---  
announcement Required| string| The string to be announced  
options Required| object| `queue` - queue the announcement behind existing speech iOS  
### `getRecommendedTimeoutMillis()`
Android
[​](https://reactnative.dev/docs/next/accessibilityinfo#getrecommendedtimeoutmillis-android "Direct link to getrecommendedtimeoutmillis-android")
tsx
```
staticgetRecommendedTimeoutMillis(originalTimeout:number):Promise<number>;
```

Gets the timeout in millisecond that the user needs. This value is set in "Time to take action (Accessibility timeout)" of "Accessibility" settings.
**Parameters:**
Name| Type| Description  
---|---|---  
originalTimeout Required| number| The timeout to return if "Accessibility timeout" is not set. Specify in milliseconds.  
### `isAccessibilityServiceEnabled()`
Android
[​](https://reactnative.dev/docs/next/accessibilityinfo#isaccessibilityserviceenabled-android "Direct link to isaccessibilityserviceenabled-android")
tsx
```
staticisAccessibilityServiceEnabled():Promise<boolean>;
```

Check whether any accessibility service is enabled. This includes TalkBack but also any third-party accessibility app that may be installed. To only check whether TalkBack is enabled, use [isScreenReaderEnabled](https://reactnative.dev/docs/next/accessibilityinfo#isscreenreaderenabled). Returns a promise which resolves to a boolean. The result is `true` when some accessibility services is enabled and `false` otherwise.
> **Note** : Please use [isScreenReaderEnabled](https://reactnative.dev/docs/next/accessibilityinfo#isscreenreaderenabled) if you only want to check the status of TalkBack.
### `isBoldTextEnabled()`
iOS
[​](https://reactnative.dev/docs/next/accessibilityinfo#isboldtextenabled-ios "Direct link to isboldtextenabled-ios")
tsx
```
staticisBoldTextEnabled():Promise<boolean>:
```

Query whether a bold text is currently enabled. Returns a promise which resolves to a boolean. The result is `true` when bold text is enabled and `false` otherwise.
### `isGrayscaleEnabled()`
iOS
[​](https://reactnative.dev/docs/next/accessibilityinfo#isgrayscaleenabled-ios "Direct link to isgrayscaleenabled-ios")
tsx
```
staticisGrayscaleEnabled():Promise<boolean>;
```

Query whether grayscale is currently enabled. Returns a promise which resolves to a boolean. The result is `true` when grayscale is enabled and `false` otherwise.
### `isInvertColorsEnabled()`
iOS
[​](https://reactnative.dev/docs/next/accessibilityinfo#isinvertcolorsenabled-ios "Direct link to isinvertcolorsenabled-ios")
tsx
```
staticisInvertColorsEnabled():Promise<boolean>;
```

Query whether invert colors is currently enabled. Returns a promise which resolves to a boolean. The result is `true` when invert colors is enabled and `false` otherwise.
### `isReduceMotionEnabled()`[​](https://reactnative.dev/docs/next/accessibilityinfo#isreducemotionenabled "Direct link to isreducemotionenabled")
tsx
```
staticisReduceMotionEnabled():Promise<boolean>;
```

Query whether reduce motion is currently enabled. Returns a promise which resolves to a boolean. The result is `true` when reduce motion is enabled and `false` otherwise.
### `isReduceTransparencyEnabled()`
iOS
[​](https://reactnative.dev/docs/next/accessibilityinfo#isreducetransparencyenabled-ios "Direct link to isreducetransparencyenabled-ios")
tsx
```
staticisReduceTransparencyEnabled():Promise<boolean>;
```

Query whether reduce transparency is currently enabled. Returns a promise which resolves to a boolean. The result is `true` when a reduce transparency is enabled and `false` otherwise.
### `isScreenReaderEnabled()`[​](https://reactnative.dev/docs/next/accessibilityinfo#isscreenreaderenabled "Direct link to isscreenreaderenabled")
tsx
```
staticisScreenReaderEnabled():Promise<boolean>;
```

Query whether a screen reader is currently enabled. Returns a promise which resolves to a boolean. The result is `true` when a screen reader is enabled and `false` otherwise.
### `prefersCrossFadeTransitions()`
iOS
[​](https://reactnative.dev/docs/next/accessibilityinfo#preferscrossfadetransitions-ios "Direct link to preferscrossfadetransitions-ios")
tsx
```
staticprefersCrossFadeTransitions():Promise<boolean>;
```

Query whether reduce motion and prefer cross-fade transitions settings are currently enabled. Returns a promise which resolves to a boolean. The result is `true` when prefer cross-fade transitions is enabled and `false` otherwise.
### `setAccessibilityFocus()`[​](https://reactnative.dev/docs/next/accessibilityinfo#setaccessibilityfocus "Direct link to setaccessibilityfocus")
tsx
```
staticsetAccessibilityFocus(reactTag:number);
```

Set accessibility focus to a React component.
On Android, this calls `UIManager.sendAccessibilityEvent` method with passed `reactTag` and `UIManager.AccessibilityEventTypes.typeViewFocused` arguments.
> **Note** : Make sure that any `View` you want to receive the accessibility focus has `accessible={true}`.
Is this page useful?
  * [Methods](https://reactnative.dev/docs/next/accessibilityinfo#methods)
    * [`addEventListener()`](https://reactnative.dev/docs/next/accessibilityinfo#addeventlistener)
    * [`announceForAccessibility()`](https://reactnative.dev/docs/next/accessibilityinfo#announceforaccessibility)
    * [`announceForAccessibilityWithOptions()`](https://reactnative.dev/docs/next/accessibilityinfo#announceforaccessibilitywithoptions)
    * [`getRecommendedTimeoutMillis()` Android](https://reactnative.dev/docs/next/accessibilityinfo#getrecommendedtimeoutmillis-android)
    * [`isAccessibilityServiceEnabled()` Android](https://reactnative.dev/docs/next/accessibilityinfo#isaccessibilityserviceenabled-android)
    * [`isBoldTextEnabled()` iOS](https://reactnative.dev/docs/next/accessibilityinfo#isboldtextenabled-ios)
    * [`isGrayscaleEnabled()` iOS](https://reactnative.dev/docs/next/accessibilityinfo#isgrayscaleenabled-ios)
    * [`isInvertColorsEnabled()` iOS](https://reactnative.dev/docs/next/accessibilityinfo#isinvertcolorsenabled-ios)
    * [`isReduceMotionEnabled()`](https://reactnative.dev/docs/next/accessibilityinfo#isreducemotionenabled)
    * [`isReduceTransparencyEnabled()` iOS](https://reactnative.dev/docs/next/accessibilityinfo#isreducetransparencyenabled-ios)
    * [`isScreenReaderEnabled()`](https://reactnative.dev/docs/next/accessibilityinfo#isscreenreaderenabled)
    * [`prefersCrossFadeTransitions()` iOS](https://reactnative.dev/docs/next/accessibilityinfo#preferscrossfadetransitions-ios)
    * [`setAccessibilityFocus()`](https://reactnative.dev/docs/next/accessibilityinfo#setaccessibilityfocus)



