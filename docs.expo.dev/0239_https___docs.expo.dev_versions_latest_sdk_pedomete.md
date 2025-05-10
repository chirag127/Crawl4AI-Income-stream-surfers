---
url: https://docs.expo.dev/versions/latest/sdk/pedometer
title: https://docs.expo.dev/versions/latest/sdk/pedometer
date: 2025-04-30T17:16:54.579081
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo Pedometer
A library that provides access to the device's pedometer sensor.
Android
iOS
Bundled version:
~14.0.2
`Pedometer` from `expo-sensors` uses the system `hardware.Sensor` on Android and Core Motion on iOS to get the user's step count, and also allows you to subscribe to pedometer updates.
## Installation
Terminal
Copy
`- ``npx expo install expo-sensors`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Usage
Pedometer
```
import { useState, useEffect } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { Pedometer } from 'expo-sensors';
export default function App() {
 const [isPedometerAvailable, setIsPedometerAvailable] = useState('checking');
 const [pastStepCount, setPastStepCount] = useState(0);
 const [currentStepCount, setCurrentStepCount] = useState(0);
 const subscribe = async () => {
  const isAvailable = await Pedometer.isAvailableAsync();
  setIsPedometerAvailable(String(isAvailable));
  if (isAvailable) {
   const end = new Date();
   const start = new Date();
   start.setDate(end.getDate() - 1);
   const pastStepCountResult = await Pedometer.getStepCountAsync(start, end);
   if (pastStepCountResult) {
    setPastStepCount(pastStepCountResult.steps);
   }
   return Pedometer.watchStepCount(result => {
    setCurrentStepCount(result.steps);
   });
  }
 };
 useEffect(() => {
  const subscription = subscribe();
  return () => subscription && subscription.remove();
 }, []);
 return (
  <View style={styles.container}><Text>Pedometer.isAvailableAsync(): {isPedometerAvailable}</Text><Text>Steps taken in the last 24 hours: {pastStepCount}</Text><Text>Walk! And watch this go up: {currentStepCount}</Text></View>
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
import { Pedometer } from 'expo-sensors';

```

## Methods
### `Pedometer.getPermissionsAsync()`
Android
iOS
Checks user's permissions for accessing pedometer.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/pedometer/#permissionresponse)>`
### `Pedometer.getStepCountAsync(start, end)`
iOS
Parameter| Type| Description  
---|---|---  
start| | A date indicating the start of the range over which to measure steps.  
end| | A date indicating the end of the range over which to measure steps.  
Get the step count between two dates.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
Returns a promise that fulfills with a [`PedometerResult`](https://docs.expo.dev/versions/latest/sdk/pedometer/#pedometerresult).
As [Apple documentation states](https://developer.apple.com/documentation/coremotion/cmpedometer/1613946-querypedometerdatafromdate?language=objc):
> Only the past seven days worth of data is stored and available for you to retrieve. Specifying a start date that is more than seven days in the past returns only the available data.
### `Pedometer.isAvailableAsync()`
Android
iOS
Returns whether the pedometer is enabled on the device.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
Returns a promise that fulfills with a `boolean`, indicating whether the pedometer is available on this device.
### `Pedometer.requestPermissionsAsync()`
Android
iOS
Asks the user to grant permissions for accessing pedometer.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/pedometer/#permissionresponse)>`
### `Pedometer.watchStepCount(callback)`
Android
iOS
Parameter| Type| Description  
---|---|---  
callback| `PedometerUpdateCallback[](https://docs.expo.dev/versions/latest/sdk/pedometer/#pedometerupdatecallback)`| A callback that is invoked when new step count data is available. The callback is provided with a single argument that is [`PedometerResult`](https://docs.expo.dev/versions/latest/sdk/pedometer/#pedometerresult).  
Subscribe to pedometer updates.
Returns:
`EventSubscription`
Returns a [`Subscription`](https://docs.expo.dev/versions/latest/sdk/pedometer/#subscription) that enables you to call `remove()` when you would like to unsubscribe the listener.
> Pedometer updates will not be delivered while the app is in the background. As an alternative, on Android, use another solution based on [`Health Connect API`](https://developer.android.com/health-and-fitness/guides/health-connect). On iOS, the `getStepCountAsync` method can be used to get the step count between two dates.
## Interfaces
### `PermissionResponse`
Android
iOS
An object obtained by permissions get and request functions.
Property| Type| Description  
---|---|---  
canAskAgain| `boolean`| Indicates if user can be asked again for specific permission. If not, one should be directed to the Settings app in order to enable/disable the permission.  
expires| `PermissionExpiration[](https://docs.expo.dev/versions/latest/sdk/pedometer/#permissionexpiration)`| Determines time when the permission expires.  
granted| `boolean`| A convenience boolean that indicates if the permission is granted.  
status| `PermissionStatus[](https://docs.expo.dev/versions/latest/sdk/pedometer/#permissionstatus)`| Determines the status of the permission.  
## Types
### `PedometerResult`
Android
iOS
Property| Type| Description  
---|---|---  
steps| `number`| Number of steps taken between the given dates.  
### `PedometerUpdateCallback(result)`
Android
iOS
Callback function providing event result as an argument.
Parameter| Type  
---|---  
result| `PedometerResult[](https://docs.expo.dev/versions/latest/sdk/pedometer/#pedometerresult)`  
Returns:
`void`
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

