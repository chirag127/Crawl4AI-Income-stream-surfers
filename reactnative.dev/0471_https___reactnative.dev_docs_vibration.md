---
url: https://reactnative.dev/docs/vibration
title: https://reactnative.dev/docs/vibration
date: 2025-05-10T21:42:55.719159
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/vibration#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
Vibrates the device.
## Example[​](https://reactnative.dev/docs/vibration#example "Direct link to Example")
> Android apps should request the `android.permission.VIBRATE` permission by adding `<uses-permission android:name="android.permission.VIBRATE"/>` to `AndroidManifest.xml`.
> The Vibration API is implemented as a `AudioServicesPlaySystemSound(kSystemSoundID_Vibrate)` call on iOS.
# Reference
## Methods[​](https://reactnative.dev/docs/vibration#methods "Direct link to Methods")
### `cancel()`[​](https://reactnative.dev/docs/vibration#cancel "Direct link to cancel")
tsx
```
staticcancel();
```

Call this to stop vibrating after having invoked `vibrate()` with repetition enabled.
### `vibrate()`[​](https://reactnative.dev/docs/vibration#vibrate "Direct link to vibrate")
tsx
```
staticvibrate( pattern?:number|number[], repeat?:boolean
```

Triggers a vibration with a fixed duration.
**On Android,** the vibration duration defaults to 400 milliseconds, and an arbitrary vibration duration can be specified by passing a number as the value for the `pattern` argument. **On iOS,** the vibration duration is fixed at roughly 400 milliseconds.
The `vibrate()` method can take a `pattern` argument with an array of numbers that represent time in milliseconds. You may set `repeat` to true to run through the vibration pattern in a loop until `cancel()` is called.
**On Android,** the odd indices of the `pattern` array represent the vibration duration, while the even ones represent the separation time. **On iOS,** the numbers in the `pattern` array represent the separation time, as the vibration duration is fixed.
**Parameters:**
Name| Type| Default| Description  
---|---|---|---  
pattern| number Androidarray of numbers| `400`| Vibration duration in milliseconds.Vibration pattern as an array of numbers in milliseconds.  
repeat| boolean| `false`| Repeat vibration pattern until `cancel()`.  
Is this page useful?
  * [Methods](https://reactnative.dev/docs/vibration#methods)



