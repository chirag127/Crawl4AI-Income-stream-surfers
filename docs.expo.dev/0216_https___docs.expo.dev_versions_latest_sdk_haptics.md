---
url: https://docs.expo.dev/versions/latest/sdk/haptics
title: https://docs.expo.dev/versions/latest/sdk/haptics
date: 2025-04-30T17:16:24.856370
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo Haptics
A library that provides access to the system's vibration effects on Android and the haptics engine on iOS.
Android
iOS
Bundled version:
~14.0.1
`expo-haptics` provides haptic (touch) feedback for:
  * Android devices using Vibrator system service.
  * iOS 10+ devices using the Taptic Engine.


On iOS, the Taptic engine will do nothing if any of the following conditions are true on a user's device:
  * Low Power Mode is enabled. This can be detected with [`expo-battery`](https://docs.expo.dev/versions/latest/sdk/battery).
  * User disabled the Taptic Engine in settings.
  * iOS Camera is active (to prevent destabilization).
  * iOS dictation is active (to not disturb the microphone input).


## Installation
Terminal
Copy
`- ``npx expo install expo-haptics`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Configuration
On Android, this library requires permission to control vibration on the device. The `VIBRATE` permission is added automatically.
## Usage
Haptics usage
```
import { StyleSheet, View, Text, Button } from 'react-native';
import * as Haptics from 'expo-haptics';
export default function App() {
 return (
  <View style={styles.container}><Text style={styles.text}>Haptics.selectionAsync</Text><View style={styles.buttonContainer}><Button title="Selection" onPress={() => Haptics.selectionAsync()} /></View><Text style={styles.text}>Haptics.notificationAsync</Text><View style={styles.buttonContainer}><Button
     title="Success"
     onPress={
      () =>
       Haptics.notificationAsync(
        Haptics.NotificationFeedbackType.Success
       )
     }
    /><Button
     title="Error"
     onPress={
      () =>
       Haptics.notificationAsync(
        Haptics.NotificationFeedbackType.Error
       )
     }
    /><Button
     title="Warning"
     onPress={
      () =>
       Haptics.notificationAsync(
        Haptics.NotificationFeedbackType.Warning
       )
     }
    /></View><Text style={styles.text}>Haptics.impactAsync</Text><View style={styles.buttonContainer}><Button
     title="Light"
     onPress={
      () => Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light)
     }
    /><Button
     title="Medium"
     onPress={
      () => Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Medium)
     }
    /><Button
     title="Heavy"
     onPress={
      () => Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Heavy)
     }
    /><Button
     title="Rigid"
     onPress={
      () => Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Rigid)
     }
    /><Button
     title="Soft"
     onPress={
      () => Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Soft)
     }
    /></View></View>
 );
}
const styles = StyleSheet.create({
 container: {
  flex: 1,
  justifyContent: 'center',
  paddingHorizontal: 16,
 },
 buttonContainer: {
  flexDirection: 'row',
  alignItems: 'stretch',
  marginTop: 10,
  marginBottom: 30,
  justifyContent: 'space-between',
 },
});

Show More

```

## API
```
import * as Haptics from 'expo-haptics';

```

## Methods
### `Haptics.impactAsync(style)`
Android
iOS
Parameter| Type| Description  
---|---|---  
style(optional)| `ImpactFeedbackStyle[](https://docs.expo.dev/versions/latest/sdk/haptics/#impactfeedbackstyle)`| A collision indicator that on iOS is directly mapped to [`UIImpactFeedbackStyle`](https://developer.apple.com/documentation/uikit/uiimpactfeedbackstyle), while on Android these are simulated using [Vibrator](https://developer.android.com/reference/android/os/Vibrator). You can use one of `Haptics.ImpactFeedbackStyle.{Light, Medium, Heavy}`.Default:`ImpactFeedbackStyle.Medium`  
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
A `Promise` which fulfils once native size haptics functionality is triggered.
### `Haptics.notificationAsync(type)`
Android
iOS
Parameter| Type| Description  
---|---|---  
type(optional)| `NotificationFeedbackType[](https://docs.expo.dev/versions/latest/sdk/haptics/#notificationfeedbacktype)`| A notification feedback type that on iOS is directly mapped to [UINotificationFeedbackType](https://developer.apple.com/documentation/uikit/uinotificationfeedbacktype), while on Android these are simulated using [Vibrator](https://developer.android.com/reference/android/os/Vibrator). You can use one of `Haptics.NotificationFeedbackType.{Success, Warning, Error}`.Default:`NotificationFeedbackType.Success`  
The kind of notification response used in the feedback.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
A `Promise` which fulfils once native size haptics functionality is triggered.
### `Haptics.selectionAsync()`
Android
iOS
Used to let a user know when a selection change has been registered.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
A `Promise` which fulfils once native size haptics functionality is triggered.
## Enums
### `ImpactFeedbackStyle`
Android
iOS
The mass of the objects in the collision simulated by a UIImpactFeedbackGenerator object [`UINotificationFeedbackStyle`](https://developer.apple.com/documentation/uikit/uiimpactfeedbackstyle)
#### `Heavy`
`ImpactFeedbackStyle.Heavy ＝ "heavy"`
A collision between large, heavy user interface elements.
#### `Light`
`ImpactFeedbackStyle.Light ＝ "light"`
A collision between small, light user interface elements.
#### `Medium`
`ImpactFeedbackStyle.Medium ＝ "medium"`
A collision between moderately sized user interface elements.
#### `Rigid`
`ImpactFeedbackStyle.Rigid ＝ "rigid"`
A collision between user interface elements that are rigid, exhibiting a small amount of compression or elasticity.
#### `Soft`
`ImpactFeedbackStyle.Soft ＝ "soft"`
A collision between user interface elements that are soft, exhibiting a large amount of compression or elasticity.
### `NotificationFeedbackType`
Android
iOS
The type of notification feedback generated by a UINotificationFeedbackGenerator object. [`UINotificationFeedbackType`](https://developer.apple.com/documentation/uikit/uinotificationfeedbacktype)
#### `Error`
`NotificationFeedbackType.Error ＝ "error"`
A notification feedback type indicating that a task has failed.
#### `Success`
`NotificationFeedbackType.Success ＝ "success"`
A notification feedback type indicating that a task has completed successfully.
#### `Warning`
`NotificationFeedbackType.Warning ＝ "warning"`
A notification feedback type indicating that a task has produced a warning.

