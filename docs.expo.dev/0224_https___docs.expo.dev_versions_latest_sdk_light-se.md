---
url: https://docs.expo.dev/versions/latest/sdk/light-sensor
title: https://docs.expo.dev/versions/latest/sdk/light-sensor
date: 2025-04-30T17:16:26.468453
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo LightSensor
A library that provides access to the device's light sensor.
Android
Bundled version:
~14.0.2
`LightSensor` from `expo-sensors` provides access to the device's light sensor to respond to illuminance changes.
## Installation
Terminal
Copy
`- ``npx expo install expo-sensors`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Usage
Basic Light Sensor usage
```
import { useState, useEffect } from 'react';
import { StyleSheet, Text, TouchableOpacity, View, Platform } from 'react-native';
import { LightSensor } from 'expo-sensors';
export default function App() {
 const [{ illuminance }, setData] = useState({ illuminance: 0 });
 const [subscription, setSubscription] = useState(null);
 const toggle = () => {
  if (subscription) {
   unsubscribe();
  } else {
   subscribe();
  }
 };
 const subscribe = () => {
  setSubscription(
   LightSensor.addListener(sensorData => {
    setData(sensorData);
   })
  );
 };
 const unsubscribe = () => {
  subscription && subscription.remove();
  setSubscription(null);
 };
 useEffect(() => {
  subscribe();
  return () => unsubscribe();
 }, []);
 return (
  <View style={styles.sensor}><Text>Light Sensor:</Text><Text>
    Illuminance: {Platform.OS === 'android' ? `${illuminance} lx` : `Only available on Android`}</Text><View style={styles.buttonContainer}><TouchableOpacity onPress={toggle} style={styles.button}><Text>Toggle</Text></TouchableOpacity></View></View>
 );
}
const styles = StyleSheet.create({
 sensor: {
  flex: 1,
  justifyContent: 'center',
  alignItems: 'center',
  paddingHorizontal: 10,
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
});

Show More

```

## API
```
import { LightSensor } from 'expo-sensors';

```

## Classes
### `LightSensor`
Android
Type: Class extends `DeviceSensor[](https://docs.expo.dev/versions/latest/sdk/sensors)<LightSensorMeasurement[](https://docs.expo.dev/versions/latest/sdk/light-sensor/#lightsensormeasurement)>`
LightSensor Methods
### `addListener(listener)`
Android
Parameter| Type| Description  
---|---|---  
listener| `Listener<LightSensorMeasurement[](https://docs.expo.dev/versions/latest/sdk/light-sensor/#lightsensormeasurement)>`| A callback that is invoked when a LightSensor update is available. When invoked, the listener is provided a single argument that is the illuminance value.  
Subscribe for updates to the light sensor.
Returns:
`EventSubscription`
A subscription that you can call `remove()` on when you would like to unsubscribe the listener.
### `getListenerCount()`
Android
Returns the registered listeners count.
Returns:
`number`
### `getPermissionsAsync()`
Android
Checks user's permissions for accessing sensor.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/light-sensor/#permissionresponse)>`
### `hasListeners()`
Android
Returns boolean which signifies if sensor has any listeners registered.
Returns:
`boolean`
### `isAvailableAsync()`
Android
> You should always check the sensor availability before attempting to use it.
Returns whether the light sensor is available and enabled on the device. Requires at least Android 2.3 (API Level 9).
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
A promise that resolves to a `boolean` denoting the availability of the light sensor.
### `removeAllListeners()`
Android
Removes all registered listeners.
Returns:
`void`
### `removeSubscription(subscription)`
Android
Parameter| Type| Description  
---|---|---  
subscription| `EventSubscription`| A subscription to remove.  
Removes the given subscription.
Returns:
`void`
### `requestPermissionsAsync()`
Android
Asks the user to grant permissions for accessing sensor.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/light-sensor/#permissionresponse)>`
### `setUpdateInterval(intervalMs)`
Android
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
An object obtained by permissions get and request functions.
Property| Type| Description  
---|---|---  
canAskAgain| `boolean`| Indicates if user can be asked again for specific permission. If not, one should be directed to the Settings app in order to enable/disable the permission.  
expires| `PermissionExpiration[](https://docs.expo.dev/versions/latest/sdk/light-sensor/#permissionexpiration)`| Determines time when the permission expires.  
granted| `boolean`| A convenience boolean that indicates if the permission is granted.  
status| `PermissionStatus[](https://docs.expo.dev/versions/latest/sdk/light-sensor/#permissionstatus)`| Determines the status of the permission.  
## Types
### `LightSensorMeasurement`
Android
Property| Type| Description  
---|---|---  
illuminance| `number`| Ambient light level registered by the device measured in lux (lx).  
timestamp| `number`| Timestamp of the measurement in seconds.  
### `PermissionExpiration`
Android
Literal Type: `union`
Permission expiration time. Currently, all permissions are granted permanently.
Acceptable values are: `'never'` | `number`
### `Subscription`
Android
A subscription object that allows to conveniently remove an event listener from the emitter.
Property| Type| Description  
---|---|---  
remove| `() => void`| Removes an event listener for which the subscription has been created. After calling this function, the listener will no longer receive any events from the emitter.  
## Enums
### `PermissionStatus`
Android
#### `DENIED`
`PermissionStatus.DENIED ＝ "denied"`
User has denied the permission.
#### `GRANTED`
`PermissionStatus.GRANTED ＝ "granted"`
User has granted the permission.
#### `UNDETERMINED`
`PermissionStatus.UNDETERMINED ＝ "undetermined"`
User hasn't granted or denied the permission yet.

