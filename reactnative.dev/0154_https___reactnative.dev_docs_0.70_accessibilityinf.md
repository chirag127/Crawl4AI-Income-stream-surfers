---
url: https://reactnative.dev/docs/0.70/accessibilityinfo
title: https://reactnative.dev/docs/0.70/accessibilityinfo
date: 2025-05-10T21:35:44.696456
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/0.70/accessibilityinfo#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
This is documentation for React Native **0.70** , which is no longer in active development.
For up-to-date documentation, see the (0.79).
Version: 0.70
On this page
Sometimes it's useful to know whether or not the device has a screen reader that is currently active. The `AccessibilityInfo` API is designed for this purpose. You can use it to query the current state of the screen reader as well as to register to be notified when the state of the screen reader changes.
## Example[​](https://reactnative.dev/docs/0.70/accessibilityinfo#example "Direct link to Example")
  * Function Component
  * Class Component


# Reference
## Methods[​](https://reactnative.dev/docs/0.70/accessibilityinfo#methods "Direct link to Methods")
### `addEventListener()`[​](https://reactnative.dev/docs/0.70/accessibilityinfo#addeventlistener "Direct link to addeventlistener")
jsx
```
staticaddEventListener(eventName, handler)
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
### `announceForAccessibility()`[​](https://reactnative.dev/docs/0.70/accessibilityinfo#announceforaccessibility "Direct link to announceforaccessibility")
jsx
```
staticannounceForAccessibility(announcement)
```

Post a string to be announced by the screen reader.
### `announceForAccessibilityWithOptions()`[​](https://reactnative.dev/docs/0.70/accessibilityinfo#announceforaccessibilitywithoptions "Direct link to announceforaccessibilitywithoptions")
jsx
```
staticannounceForAccessibilityWithOptions(announcement, options)
```

Post a string to be announced by the screen reader with modification options. By default announcements will interrupt any existing speech, but on iOS they can be queued behind existing speech by setting `queue` to `true` in the options object.
**Parameters:**
Name| Type| Description  
---|---|---  
announcement Required| string| The string to be announced  
options Required| object| `queue` - queue the announcement behind existing speech iOS  
### `getRecommendedTimeoutMillis()`
Android
[​](https://reactnative.dev/docs/0.70/accessibilityinfo#getrecommendedtimeoutmillis-android "Direct link to getrecommendedtimeoutmillis-android")
jsx
```
staticgetRecommendedTimeoutMillis(originalTimeout)
```

Gets the timeout in millisecond that the user needs. This value is set in "Time to take action (Accessibility timeout)" of "Accessibility" settings.
**Parameters:**
Name| Type| Description  
---|---|---  
originalTimeout Required| number| The timeout to return if "Accessibility timeout" is not set. Specify in milliseconds.  
### `isAccessibilityServiceEnabled()`
Android
[​](https://reactnative.dev/docs/0.70/accessibilityinfo#isaccessibilityserviceenabled-android "Direct link to isaccessibilityserviceenabled-android")
jsx
```
staticisAccessibilityServiceEnabled():Promise<boolean>
```

Check whether any accessibility service is enabled. This includes TalkBack but also any third-party accessibility app that may be installed. To only check whether TalkBack is enabled, use [isScreenReaderEnabled](https://reactnative.dev/docs/0.70/accessibilityinfo#isscreenreaderenabled). Returns a promise which resolves to a boolean. The result is `true` when some accessibility services is enabled and `false` otherwise.
> **Note** : Please use [isScreenReaderEnabled](https://reactnative.dev/docs/0.70/accessibilityinfo#isscreenreaderenabled) if you only want to check the status of TalkBack.
### `isBoldTextEnabled()`
iOS
[​](https://reactnative.dev/docs/0.70/accessibilityinfo#isboldtextenabled-ios "Direct link to isboldtextenabled-ios")
jsx
```
staticisBoldTextEnabled()
```

Query whether a bold text is currently enabled. Returns a promise which resolves to a boolean. The result is `true` when bold text is enabled and `false` otherwise.
### `isGrayscaleEnabled()`
iOS
[​](https://reactnative.dev/docs/0.70/accessibilityinfo#isgrayscaleenabled-ios "Direct link to isgrayscaleenabled-ios")
jsx
```
staticisGrayscaleEnabled()
```

Query whether grayscale is currently enabled. Returns a promise which resolves to a boolean. The result is `true` when grayscale is enabled and `false` otherwise.
### `isInvertColorsEnabled()`
iOS
[​](https://reactnative.dev/docs/0.70/accessibilityinfo#isinvertcolorsenabled-ios "Direct link to isinvertcolorsenabled-ios")
jsx
```
staticisInvertColorsEnabled()
```

Query whether invert colors is currently enabled. Returns a promise which resolves to a boolean. The result is `true` when invert colors is enabled and `false` otherwise.
### `isReduceMotionEnabled()`[​](https://reactnative.dev/docs/0.70/accessibilityinfo#isreducemotionenabled "Direct link to isreducemotionenabled")
jsx
```
staticisReduceMotionEnabled()
```

Query whether reduce motion is currently enabled. Returns a promise which resolves to a boolean. The result is `true` when reduce motion is enabled and `false` otherwise.
### `isReduceTransparencyEnabled()`
iOS
[​](https://reactnative.dev/docs/0.70/accessibilityinfo#isreducetransparencyenabled-ios "Direct link to isreducetransparencyenabled-ios")
jsx
```
staticisReduceTransparencyEnabled()
```

Query whether reduce transparency is currently enabled. Returns a promise which resolves to a boolean. The result is `true` when a reduce transparency is enabled and `false` otherwise.
### `isScreenReaderEnabled()`[​](https://reactnative.dev/docs/0.70/accessibilityinfo#isscreenreaderenabled "Direct link to isscreenreaderenabled")
jsx
```
staticisScreenReaderEnabled()
```

Query whether a screen reader is currently enabled. Returns a promise which resolves to a boolean. The result is `true` when a screen reader is enabled and `false` otherwise.
### `removeEventListener()`[​](https://reactnative.dev/docs/0.70/accessibilityinfo#removeeventlistener "Direct link to removeeventlistener")
jsx
```
staticremoveEventListener(eventName, handler)
```

> **Deprecated.** Use the `remove()` method on the event subscription returned by [`addEventListener()`](https://reactnative.dev/docs/0.70/accessibilityinfo#addeventlistener).
### `setAccessibilityFocus()`[​](https://reactnative.dev/docs/0.70/accessibilityinfo#setaccessibilityfocus "Direct link to setaccessibilityfocus")
jsx
```
staticsetAccessibilityFocus(reactTag)
```

Set accessibility focus to a React component.
On Android, this calls `UIManager.sendAccessibilityEvent` method with passed `reactTag` and `UIManager.AccessibilityEventTypes.typeViewFocused` arguments.
> **Note** : Make sure that any `View` you want to receive the accessibility focus has `accessible={true}`.
Is this page useful?
  * [Methods](https://reactnative.dev/docs/0.70/accessibilityinfo#methods)
    * [`addEventListener()`](https://reactnative.dev/docs/0.70/accessibilityinfo#addeventlistener)
    * [`announceForAccessibility()`](https://reactnative.dev/docs/0.70/accessibilityinfo#announceforaccessibility)
    * [`announceForAccessibilityWithOptions()`](https://reactnative.dev/docs/0.70/accessibilityinfo#announceforaccessibilitywithoptions)
    * [`getRecommendedTimeoutMillis()` Android](https://reactnative.dev/docs/0.70/accessibilityinfo#getrecommendedtimeoutmillis-android)
    * [`isAccessibilityServiceEnabled()` Android](https://reactnative.dev/docs/0.70/accessibilityinfo#isaccessibilityserviceenabled-android)
    * [`isBoldTextEnabled()` iOS](https://reactnative.dev/docs/0.70/accessibilityinfo#isboldtextenabled-ios)
    * [`isGrayscaleEnabled()` iOS](https://reactnative.dev/docs/0.70/accessibilityinfo#isgrayscaleenabled-ios)
    * [`isInvertColorsEnabled()` iOS](https://reactnative.dev/docs/0.70/accessibilityinfo#isinvertcolorsenabled-ios)
    * [`isReduceMotionEnabled()`](https://reactnative.dev/docs/0.70/accessibilityinfo#isreducemotionenabled)
    * [`isReduceTransparencyEnabled()` iOS](https://reactnative.dev/docs/0.70/accessibilityinfo#isreducetransparencyenabled-ios)
    * [`isScreenReaderEnabled()`](https://reactnative.dev/docs/0.70/accessibilityinfo#isscreenreaderenabled)
    * [`removeEventListener()`](https://reactnative.dev/docs/0.70/accessibilityinfo#removeeventlistener)
    * [`setAccessibilityFocus()`](https://reactnative.dev/docs/0.70/accessibilityinfo#setaccessibilityfocus)



