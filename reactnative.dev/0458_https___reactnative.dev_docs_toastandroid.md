---
url: https://reactnative.dev/docs/toastandroid
title: https://reactnative.dev/docs/toastandroid
date: 2025-05-10T21:42:39.776206
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/toastandroid#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
React Native's ToastAndroid API exposes the Android platform's ToastAndroid module as a JS module. It provides the method `show(message, duration)` which takes the following parameters:
  * _message_ A string with the text to toast
  * _duration_ The duration of the toast—either `ToastAndroid.SHORT` or `ToastAndroid.LONG`


You can alternatively use `showWithGravity(message, duration, gravity)` to specify where the toast appears in the screen's layout. May be `ToastAndroid.TOP`, `ToastAndroid.BOTTOM` or `ToastAndroid.CENTER`.
The `showWithGravityAndOffset(message, duration, gravity, xOffset, yOffset)` method adds the ability to specify an offset with in pixels.
> Starting with Android 11 (API level 30), setting the gravity has no effect on text toasts. Read about the changes [here](https://developer.android.com/about/versions/11/behavior-changes-11#text-toast-api-changes).
# Reference
## Methods[​](https://reactnative.dev/docs/toastandroid#methods "Direct link to Methods")
### `show()`[​](https://reactnative.dev/docs/toastandroid#show "Direct link to show")
tsx
```
staticshow(message:string, duration:number);
```

### `showWithGravity()`[​](https://reactnative.dev/docs/toastandroid#showwithgravity "Direct link to showwithgravity")
This property will only work on Android API 29 and below. For similar functionality on higher Android APIs, consider using snackbar or notification.
tsx
```
staticshowWithGravity(message:string, duration:number, gravity:number);
```

### `showWithGravityAndOffset()`[​](https://reactnative.dev/docs/toastandroid#showwithgravityandoffset "Direct link to showwithgravityandoffset")
This property will only work on Android API 29 and below. For similar functionality on higher Android APIs, consider using snackbar or notification.
tsx
```
staticshowWithGravityAndOffset( message:string, duration:number, gravity:number, xOffset:number, yOffset:number,
```

## Properties[​](https://reactnative.dev/docs/toastandroid#properties "Direct link to Properties")
### `SHORT`[​](https://reactnative.dev/docs/toastandroid#short "Direct link to short")
Indicates the duration on the screen.
tsx
```
staticSHORT:number;
```

### `LONG`[​](https://reactnative.dev/docs/toastandroid#long "Direct link to long")
Indicates the duration on the screen.
tsx
```
staticLONG:number;
```

### `TOP`[​](https://reactnative.dev/docs/toastandroid#top "Direct link to top")
Indicates the position on the screen.
tsx
```
staticTOP:number;
```

### `BOTTOM`[​](https://reactnative.dev/docs/toastandroid#bottom "Direct link to bottom")
Indicates the position on the screen.
tsx
```
staticBOTTOM:number;
```

### `CENTER`[​](https://reactnative.dev/docs/toastandroid#center "Direct link to center")
Indicates the position on the screen.
tsx
```
staticCENTER:number;
```

Is this page useful?
  * [Methods](https://reactnative.dev/docs/toastandroid#methods)
    * [`showWithGravity()`](https://reactnative.dev/docs/toastandroid#showwithgravity)
    * [`showWithGravityAndOffset()`](https://reactnative.dev/docs/toastandroid#showwithgravityandoffset)
  * [Properties](https://reactnative.dev/docs/toastandroid#properties)



