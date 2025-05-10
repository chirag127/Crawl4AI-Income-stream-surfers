---
url: https://docs.expo.dev/versions/latest/sdk/accelerometer
title: https://docs.expo.dev/versions/latest/sdk/accelerometer
date: 2025-04-30T17:15:18.486481
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo Accelerometer
A library that provides access to the device's accelerometer sensor.
Android
iOS (device only)
Web
Bundled version:
~14.0.2
`Accelerometer` from `expo-sensors` provides access to the device accelerometer sensor(s) and associated listeners to respond to changes in acceleration in three-dimensional space, meaning any movement or vibration.
## Installation
Terminal
Copy
`- ``npx expo install expo-sensors`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Usage
Basic Accelerometer usage
```
import { useState, useEffect } from 'react';
import { StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { Accelerometer } from 'expo-sensors';
export default function App() {
 const [{ x, y, z }, setData] = useState({
  x: 0,
  y: 0,
  z: 0,
 });
 const [subscription, setSubscription] = useState(null);
 const _slow = () => Accelerometer.setUpdateInterval(1000);
 const _fast = () => Accelerometer.setUpdateInterval(16);
 const _subscribe = () => {
  setSubscription(Accelerometer.addListener(setData));
 };
 const _unsubscribe = () => {
  subscription && subscription.remove();
  setSubscription(null);
 };
 useEffect(() => {
  _subscribe();
  return () => _unsubscribe();
 }, []);
 return (
  <View style={styles.container}><Text style={styles.text}>Accelerometer: (in gs where 1g = 9.81 m/s^2)</Text><Text style={styles.text}>x: {x}</Text><Text style={styles.text}>y: {y}</Text><Text style={styles.text}>z: {z}</Text><View style={styles.buttonContainer}><TouchableOpacity onPress={subscription ? _unsubscribe : _subscribe} style={styles.button}><Text>{subscription ? 'On' : 'Off'}</Text></TouchableOpacity><TouchableOpacity onPress={_slow} style={[styles.button, styles.middleButton]}><Text>Slow</Text></TouchableOpacity><TouchableOpacity onPress={_fast} style={styles.button}><Text>Fast</Text></TouchableOpacity></View></View>
 );
}
const styles = StyleSheet.create({
 container: {
  flex: 1,
  justifyContent: 'center',
  paddingHorizontal: 20,
 },
 text: {
  textAlign: 'center',
 },
 buttonContainer: {
  flexDirection: 'row',
  alignItems: 'stretch',
  marginTop: 15,
 },
 button: {
  flex: 1,
  justifyContent: 'center',
  alignItems: 'center',
  backgroundColor: '#eee',
  padding: 10,
 },
 middleButton: {
  borderLeftWidth: 1,
  borderRightWidth: 1,
  borderColor: '#ccc',
 },
});

Show More

```

## API
```
import { Accelerometer } from 'expo-sensors';

```

## Classes
### `Accelerometer`
Android
iOS
Web
Type: Class extends `DeviceSensor[](https://docs.expo.dev/versions/latest/sdk/sensors)<AccelerometerMeasurement[](https://docs.expo.dev/versions/latest/sdk/accelerometer/#accelerometermeasurement)>`
A base class for subscribable sensors. The events emitted by this class are measurements specified by the parameter type `Measurement`.
Accelerometer Methods
### `addListener(listener)`
Android
iOS
Web
Parameter| Type| Description  
---|---|---  
listener| `Listener<AccelerometerMeasurement[](https://docs.expo.dev/versions/latest/sdk/accelerometer/#accelerometermeasurement)>`| A callback that is invoked when an accelerometer update is available. When invoked, the listener is provided a single argument that is an `AccelerometerMeasurement` object.  
Subscribe for updates to the accelerometer.
Returns:
`EventSubscription`
A subscription that you can call `remove()` on when you would like to unsubscribe the listener.
### `getListenerCount()`
Android
iOS
Web
Returns the registered listeners count.
Returns:
`number`
### `getPermissionsAsync()`
Android
iOS
Web
Checks user's permissions for accessing sensor.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/accelerometer/#permissionresponse)>`
### `hasListeners()`
Android
iOS
Web
Returns boolean which signifies if sensor has any listeners registered.
Returns:
`boolean`
### `isAvailableAsync()`
Android
iOS
Web
> You should always check the sensor availability before attempting to use it.
Returns whether the accelerometer is enabled on the device.
On mobile web, you must first invoke `Accelerometer.requestPermissionsAsync()` in a user interaction (i.e. touch event) before you can use this module. If the `status` is not equal to `granted` then you should inform the end user that they may have to open settings.
On web this starts a timer and waits to see if an event is fired. This should predict if the iOS device has the device orientation API disabled in Settings > Safari > Motion & Orientation Access. Some devices will also not fire if the site isn't hosted with HTTPS as `DeviceMotion` is now considered a secure API. There is no formal API for detecting the status of `DeviceMotion` so this API can sometimes be unreliable on web.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
A promise that resolves to a `boolean` denoting the availability of the accelerometer.
### `removeAllListeners()`
Android
iOS
Web
Removes all registered listeners.
Returns:
`void`
### `removeSubscription(subscription)`
Android
iOS
Web
Parameter| Type| Description  
---|---|---  
subscription| `EventSubscription`| A subscription to remove.  
Removes the given subscription.
Returns:
`void`
### `requestPermissionsAsync()`
Android
iOS
Web
Asks the user to grant permissions for accessing sensor.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/accelerometer/#permissionresponse)>`
### `setUpdateInterval(intervalMs)`
Android
iOS
Web
Parameter| Type| Description  
---|---|---  
intervalMs| `number`| Desired interval in milliseconds between sensor updates.
> Starting from Android 12 (API level 31), the system has a 200ms limit for each sensor updates. If you need an update interval less than 200ms, you should:
>   * add `android.permission.HIGH_SAMPLING_RATE_SENSORS` to [app.json `permissions` field](https://docs.expo.dev/versions/latest/config/app#permissions)
>   * or if you are using bare workflow, add `<uses-permission android:name="android.permission.HIGH_SAMPLING_RATE_SENSORS"/>` to AndroidManifest.xml.
> 
  
Set the sensor update interval.
Returns:
`void`
## Interfaces
### `PermissionResponse`
Android
iOS
Web
An object obtained by permissions get and request functions.
Property| Type| Description  
---|---|---  
canAskAgain| `boolean`| Indicates if user can be asked again for specific permission. If not, one should be directed to the Settings app in order to enable/disable the permission.  
expires| `PermissionExpiration[](https://docs.expo.dev/versions/latest/sdk/accelerometer/#permissionexpiration)`| Determines time when the permission expires.  
granted| `boolean`| A convenience boolean that indicates if the permission is granted.  
status| `PermissionStatus[](https://docs.expo.dev/versions/latest/sdk/accelerometer/#permissionstatus)`| Determines the status of the permission.  
## Types
### `AccelerometerMeasurement`
Android
iOS
Web
Each of these keys represents the acceleration along that particular axis in g-force (measured in `g`s).
A `g` is a unit of gravitational force equal to that exerted by the earth’s gravitational field (`9.81 m/s^2`).
Property| Type| Description  
---|---|---  
timestamp| `number`| Timestamp of the measurement in seconds.  
`number`| Value of `g`s device reported in X axis.  
`number`| Value of `g`s device reported in Y axis.  
`number`| Value of `g`s device reported in Z axis.  
### `PermissionExpiration`
Android
iOS
Web
Literal Type: `union`
Permission expiration time. Currently, all permissions are granted permanently.
Acceptable values are: `'never'` | `number`
### `Subscription`
Android
iOS
Web
A subscription object that allows to conveniently remove an event listener from the emitter.
Property| Type| Description  
---|---|---  
remove| `() => void`| Removes an event listener for which the subscription has been created. After calling this function, the listener will no longer receive any events from the emitter.  
## Enums
### `PermissionStatus`
Android
iOS
Web
#### `DENIED`
`PermissionStatus.DENIED ＝ "denied"`
User has denied the permission.
#### `GRANTED`
`PermissionStatus.GRANTED ＝ "granted"`
User has granted the permission.
#### `UNDETERMINED`
`PermissionStatus.UNDETERMINED ＝ "undetermined"`
User hasn't granted or denied the permission yet.

