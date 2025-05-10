---
url: https://docs.expo.dev/versions/latest/sdk/battery
title: https://docs.expo.dev/versions/latest/sdk/battery
date: 2025-04-30T17:15:40.431960
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo Battery
A library that provides battery information for the physical device, as well as corresponding event listeners.
Android
iOS (device only)
Web
Bundled version:
~9.0.2
`expo-battery` provides battery information for the physical device (such as battery level, whether or not the device is charging, and more) as well as corresponding event listeners.
## Installation
Terminal
Copy
`- ``npx expo install expo-battery`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Usage
Basic Battery Usage
```
import { useBatteryLevel } from 'expo-battery';
import { StyleSheet, Text, View } from 'react-native';
export default function App() {
 const batteryLevel = useBatteryLevel();
 return (
  <View style={styles.container}><Text>Current Battery Level: {batteryLevel}</Text></View>
 );
}
const styles = StyleSheet.create({
 container: {
  flex: 1,
  marginTop: 15,
  alignItems: 'center',
  justifyContent: 'center',
 },
});

Show More

```

## API
```
import * as Battery from 'expo-battery';

```

## Hooks
### `useBatteryLevel()`
Android
iOS
Web
Gets the device's battery level, as in [`getBatteryLevelAsync`](https://docs.expo.dev/versions/latest/sdk/battery/#getbatterylevelasync).
Returns:
`number`
The battery level of the device.
Example
```
const batteryLevel = useBatteryLevel();

```

### `useBatteryState()`
Android
iOS
Web
Gets the device's battery state, as in [`getBatteryStateAsync`](https://docs.expo.dev/versions/latest/sdk/battery/#getbatterystateasync).
Returns:
The battery state of the device.
Example
```
const batteryState = useBatteryState();

```

### `useLowPowerMode()`
Android
iOS
Web
Boolean that indicates if the device is in low power or power saver mode, as in [`isLowPowerModeEnabledAsync`](https://docs.expo.dev/versions/latest/sdk/battery/#islowpowermodeenabledasync).
Returns:
`boolean`
Returns a boolean indicating if the device is in low power mode.
Example
```
const lowPowerMode = useLowPowerMode();

```

### `usePowerState()`
Android
iOS
Web
Gets the device's power state information, as in [`getPowerStateAsync`](https://docs.expo.dev/versions/latest/sdk/battery/#getpowerstateasync).
Returns:
Returns power state information.
Example
```
const { lowPowerMode, batteryLevel, batteryState } = usePowerState();

```

## Methods
### `getBatteryLevelAsync()`
Android
iOS
Web
Gets the battery level of the device as a number between `0` and `1`, inclusive. If the device does not support retrieving the battery level, this method returns `-1`. On web, this method always returns `1`.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<number>`
A `Promise` that fulfils with a number between `0` and `1` representing the battery level, or `-1` if the device does not provide it.
Example
```
await Battery.getBatteryLevelAsync();
// 0.759999

```

### `getBatteryStateAsync()`
Android
iOS
Web
Tells the battery's current state. On web, this always returns `BatteryState.UNKNOWN`.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
Returns a `Promise` which fulfills with a [`Battery.BatteryState`](https://docs.expo.dev/versions/latest/sdk/battery/#batterystate) enum value for whether the device is any of the four states.
Example
```
await Battery.getBatteryStateAsync();
// BatteryState.CHARGING

```

### `getPowerStateAsync()`
Android
iOS
Web
Gets the power state of the device including the battery level, whether it is plugged in, and if the system is currently operating in Power Saver Mode (Android) or Low Power Mode (iOS). This method re-throws any errors that occur when retrieving any of the power-state information.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
Returns a `Promise` which fulfills with [`PowerState`](https://docs.expo.dev/versions/latest/sdk/battery/#powerstate) object.
Example
```
await Battery.getPowerStateAsync();
// {
//  batteryLevel: 0.759999,
//  batteryState: BatteryState.UNPLUGGED,
//  lowPowerMode: true,
// }

```

### `isAvailableAsync()`
Android
iOS
Web
Resolves with whether the battery API is available on the current device. The value of this property is `true` on Android and physical iOS devices and `false` on iOS simulators. On web, it depends on whether the browser supports the web battery API.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
### `isBatteryOptimizationEnabledAsync()`
Android
iOS
Web
Checks whether battery optimization is enabled for your application. If battery optimization is enabled for your app, background tasks might be affected when your app goes into doze mode state. (only on Android 6.0 or later)
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
Returns a `Promise` which fulfills with a `boolean` value of either `true` or `false`, indicating whether the battery optimization is enabled or disabled, respectively. (Android only)
Example
```
await Battery.isBatteryOptimizationEnabledAsync();
// true

```

### `isLowPowerModeEnabledAsync()`
Android
iOS
Web
Gets the current status of Power Saver mode on Android and Low Power mode on iOS. If a platform doesn't support Low Power mode reporting (like web, older Android devices), the reported low-power state is always `false`, even if the device is actually in low-power mode.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
Returns a `Promise` which fulfills with a `boolean` value of either `true` or `false`, indicating whether low power mode is enabled or disabled.
Example
Power Saver Mode (Android) or Low Power Mode (iOS) are enabled.
```
await Battery.isLowPowerModeEnabledAsync();
// true

```

## Event Subscriptions
### `addBatteryLevelListener(listener)`
Android
iOS
Web
Parameter| Type| Description  
---|---|---  
listener| `(event: BatteryLevelEvent[](https://docs.expo.dev/versions/latest/sdk/battery/#batterylevelevent)) => void`| A callback that is invoked when battery level changes. The callback is provided a single argument that is an object with a `batteryLevel` key.  
Subscribe to the battery level change updates.
On Android devices, the event fires only when significant changes happens, which is when the battery level drops below [`android.intent.action.BATTERY_LOW`](https://developer.android.com/reference/android/content/Intent#ACTION_BATTERY_LOW) or rises above [`android.intent.action.BATTERY_OKAY`](https://developer.android.com/reference/android/content/Intent#ACTION_BATTERY_OKAY) from a low battery level. See [Monitor the Battery Level and Charging State](https://developer.android.com/training/monitoring-device-state/battery-monitoring) in Android documentation for more information.
On iOS devices, the event fires when the battery level drops one percent or more, but is only fired once per minute at maximum.
On web, the event never fires.
Returns:
`EventSubscription`
A `Subscription` object on which you can call `remove()` to unsubscribe from the listener.
### `addBatteryStateListener(listener)`
Android
iOS
Web
Parameter| Type| Description  
---|---|---  
listener| `(event: BatteryStateEvent[](https://docs.expo.dev/versions/latest/sdk/battery/#batterystateevent)) => void`| A callback that is invoked when battery state changes. The callback is provided a single argument that is an object with a `batteryState` key.  
Subscribe to the battery state change updates to receive an object with a [`Battery.BatteryState`](https://docs.expo.dev/versions/latest/sdk/battery/#batterystate) enum value for whether the device is any of the four states.
On web, the event never fires.
Returns:
`EventSubscription`
A `Subscription` object on which you can call `remove()` to unsubscribe from the listener.
### `addLowPowerModeListener(listener)`
Android
iOS
Web
Parameter| Type| Description  
---|---|---  
listener| `(event: PowerModeEvent[](https://docs.expo.dev/versions/latest/sdk/battery/#powermodeevent)) => void`| A callback that is invoked when Power Saver Mode (Android) or Low Power Mode (iOS) changes. The callback is provided a single argument that is an object with a `lowPowerMode` key.  
Subscribe to Power Saver Mode (Android) or Low Power Mode (iOS) updates. The event fires whenever the power mode is toggled.
On web, the event never fires.
Returns:
`EventSubscription`
A `Subscription` object on which you can call `remove()` to unsubscribe from the listener.
## Types
### `BatteryLevelEvent`
Android
iOS
Web
Property| Type| Description  
---|---|---  
batteryLevel| `number`| A number between `0` and `1`, inclusive, or `-1` if the battery level is unknown.  
### `BatteryStateEvent`
Android
iOS
Web
Property| Type| Description  
---|---|---  
batteryState| | An enum value representing the battery state.  
### `PowerModeEvent`
Android
iOS
Web
Property| Type| Description  
---|---|---  
lowPowerMode| `boolean`| A boolean value, `true` if lowPowerMode is on, `false` if lowPowerMode is off.  
### `PowerState`
Android
iOS
Web
Property| Type| Description  
---|---|---  
batteryLevel| `number`| A number between `0` and `1`, inclusive, or `-1` if the battery level is unknown.  
batteryState| | An enum value representing the battery state.  
lowPowerMode| `boolean`| A boolean value, `true` if lowPowerMode is on, `false` if lowPowerMode is off.  
### `Subscription`
Android
iOS
Web
A subscription object that allows to conveniently remove an event listener from the emitter.
Property| Type| Description  
---|---|---  
remove| `() => void`| Removes an event listener for which the subscription has been created. After calling this function, the listener will no longer receive any events from the emitter.  
## Enums
### `BatteryState`
Android
iOS
Web
#### `UNKNOWN`
`BatteryState.UNKNOWN ＝ 0`
If the battery state is unknown or inaccessible.
#### `UNPLUGGED`
`BatteryState.UNPLUGGED ＝ 1`
If battery is not charging or discharging.
#### `CHARGING`
`BatteryState.CHARGING ＝ 2`
If battery is charging.
#### `FULL`
`BatteryState.FULL ＝ 3`
If the battery level is full.

