---
url: https://docs.expo.dev/versions/latest/sdk/magnetometer
title: https://docs.expo.dev/versions/latest/sdk/magnetometer
date: 2025-04-30T17:16:49.242289
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo Magnetometer
A library that provides access to the device's magnetometer sensor.
Android
iOS
Bundled version:
~14.0.2
`Magnetometer` from `expo-sensors` provides access to the device magnetometer sensor(s) to respond to and measure the changes in the magnetic field measured in microtesla (`μT`).
You can access the calibrated values with `Magnetometer` and uncalibrated raw values with `MagnetometerUncalibrated`.
## Installation
Terminal
Copy
`- ``npx expo install expo-sensors`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Usage
Magnetometer
```
import { useState, useEffect } from 'react';
import { StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { Magnetometer } from 'expo-sensors';
export default function Compass() {
 const [{ x, y, z }, setData] = useState({
  x: 0,
  y: 0,
  z: 0,
 });
 const [subscription, setSubscription] = useState(null);
 const _slow = () => Magnetometer.setUpdateInterval(1000);
 const _fast = () => Magnetometer.setUpdateInterval(16);
 const _subscribe = () => {
  setSubscription(
   Magnetometer.addListener(result => {
    setData(result);
   })
  );
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
  <View style={styles.container}><Text style={styles.text}>Magnetometer:</Text><Text style={styles.text}>x: {x}</Text><Text style={styles.text}>y: {y}</Text><Text style={styles.text}>z: {z}</Text><View style={styles.buttonContainer}><TouchableOpacity onPress={subscription ? _unsubscribe : _subscribe} style={styles.button}><Text>{subscription ? 'On' : 'Off'}</Text></TouchableOpacity><TouchableOpacity onPress={_slow} style={[styles.button, styles.middleButton]}><Text>Slow</Text></TouchableOpacity><TouchableOpacity onPress={_fast} style={styles.button}><Text>Fast</Text></TouchableOpacity></View></View>
 );
}
const styles = StyleSheet.create({
 container: {
  flex: 1,
  justifyContent: 'center',
  paddingHorizontal: 10,
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
import { Magnetometer, MagnetometerUncalibrated } from 'expo-sensors';

```

## Classes
### `Magnetometer`
Android
iOS
Type: Class extends `DeviceSensor[](https://docs.expo.dev/versions/latest/sdk/sensors)<MagnetometerMeasurement[](https://docs.expo.dev/versions/latest/sdk/magnetometer/#magnetometermeasurement)>`
Magnetometer Methods
### `addListener(listener)`
Android
iOS
Parameter| Type| Description  
---|---|---  
listener| `Listener<MagnetometerMeasurement[](https://docs.expo.dev/versions/latest/sdk/magnetometer/#magnetometermeasurement)>`| A callback that is invoked when a magnetometer update is available. When invoked, the listener is provided with a single argument that is `MagnetometerMeasurement`.  
Subscribe for updates to the magnetometer.
Returns:
`EventSubscription`
A subscription that you can call `remove()` on when you would like to unsubscribe the listener.
### `getListenerCount()`
Android
iOS
Returns the registered listeners count.
Returns:
`number`
### `getPermissionsAsync()`
Android
iOS
Checks user's permissions for accessing sensor.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/magnetometer/#permissionresponse)>`
### `hasListeners()`
Android
iOS
Returns boolean which signifies if sensor has any listeners registered.
Returns:
`boolean`
### `isAvailableAsync()`
Android
iOS
> You should always check the sensor availability before attempting to use it.
Check the availability of the device magnetometer. Requires at least Android 2.3 (API Level 9) and iOS 8.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
A promise that resolves to a `boolean` denoting the availability of the sensor.
### `removeAllListeners()`
Android
iOS
Removes all registered listeners.
Returns:
`void`
### `removeSubscription(subscription)`
Android
iOS
Parameter| Type| Description  
---|---|---  
subscription| `EventSubscription`| A subscription to remove.  
Removes the given subscription.
Returns:
`void`
### `requestPermissionsAsync()`
Android
iOS
Asks the user to grant permissions for accessing sensor.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/magnetometer/#permissionresponse)>`
### `setUpdateInterval(intervalMs)`
Android
iOS
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
An object obtained by permissions get and request functions.
Property| Type| Description  
---|---|---  
canAskAgain| `boolean`| Indicates if user can be asked again for specific permission. If not, one should be directed to the Settings app in order to enable/disable the permission.  
expires| `PermissionExpiration[](https://docs.expo.dev/versions/latest/sdk/magnetometer/#permissionexpiration)`| Determines time when the permission expires.  
granted| `boolean`| A convenience boolean that indicates if the permission is granted.  
status| `PermissionStatus[](https://docs.expo.dev/versions/latest/sdk/magnetometer/#permissionstatus)`| Determines the status of the permission.  
## Types
### `MagnetometerMeasurement`
Android
iOS
Each of these keys represents the strength of magnetic field along that particular axis measured in microteslas (`μT`).
Property| Type| Description  
---|---|---  
timestamp| `number`| Timestamp of the measurement in seconds.  
`number`| Value representing strength of magnetic field recorded in X axis.  
`number`| Value representing strength of magnetic field recorded in Y axis.  
`number`| Value representing strength of magnetic field recorded in Z axis.  
### `PermissionExpiration`
Android
iOS
Literal Type: `union`
Permission expiration time. Currently, all permissions are granted permanently.
Acceptable values are: `'never'` | `number`
### `Subscription`
Android
iOS
A subscription object that allows to conveniently remove an event listener from the emitter.
Property| Type| Description  
---|---|---  
remove| `() => void`| Removes an event listener for which the subscription has been created. After calling this function, the listener will no longer receive any events from the emitter.  
## Enums
### `PermissionStatus`
Android
iOS
#### `DENIED`
`PermissionStatus.DENIED ＝ "denied"`
User has denied the permission.
#### `GRANTED`
`PermissionStatus.GRANTED ＝ "granted"`
User has granted the permission.
#### `UNDETERMINED`
`PermissionStatus.UNDETERMINED ＝ "undetermined"`
User hasn't granted or denied the permission yet.

