---
url: https://docs.expo.dev/versions/latest/sdk/screen-capture
title: https://docs.expo.dev/versions/latest/sdk/screen-capture
date: 2025-04-30T17:17:22.535723
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo ScreenCapture
A library that allows you to protect screens in your app from being captured or recorded.
Android
iOS
Bundled version:
~7.0.1
`expo-screen-capture` allows you to protect screens in your app from being captured or recorded, as well as be notified if a screenshot is taken while your app is foregrounded. The two most common reasons you may want to prevent screen capture are:
  * If a screen is displaying sensitive information (password, credit card data, and so on)
  * You are displaying paid content that you don't want to be recorded and shared


This is especially important on Android since the [`android.media.projection`](https://developer.android.com/about/versions/android-5.0.html#ScreenCapture) API allows third-party apps to perform screen capture or screen sharing (even if the app is in the background).
On Android, the screen capture callback works without additional permissions only for Android 14+. You don't need to request or check permissions for blocking screen capture or using the callback on Android 14+.
If you want to use the screen capture callback on Android 13 or lower, you need to add the `READ_MEDIA_IMAGES` permission to your AndroidManifest.xml file. You can use the `android.permissions` key in your app config. See [Android permissions](https://docs.expo.dev/guides/permissions#android) for more information.
> The `READ_MEDIA_IMAGES` permission can be added only for apps needing broad access to photos. See [Details on Google Play's Photo and Video Permissions policy](https://support.google.com/googleplay/android-developer/answer/14115180).
> Currently, taking screenshots on iOS cannot be prevented. This is due to underlying OS limitations.
## Installation
Terminal
Copy
`- ``npx expo install expo-screen-capture`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Usage
### Example: hook
Screen Capture hook
```
import { usePreventScreenCapture } from 'expo-screen-capture';
import { Text, View } from 'react-native';
export default function ScreenCaptureExample() {
 usePreventScreenCapture();
 return (
  <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}><Text>As long as this component is mounted, this screen is unrecordable!</Text></View>
 );
}

```

### Example: Blocking screen capture imperatively
Blocking screen capture
```
import * as ScreenCapture from 'expo-screen-capture';
import { useEffect } from 'react';
import { Button, StyleSheet, View } from 'react-native';
export default function ScreenCaptureExample() {
 const activate = async () => {
  await ScreenCapture.preventScreenCaptureAsync();
 };
 const deactivate = async () => {
  await ScreenCapture.allowScreenCaptureAsync();
 };
 return (
  <View style={styles.container}><Button title="Activate" onPress={activate} /><Button title="Deactivate" onPress={deactivate} /></View>
 );
}
const styles = StyleSheet.create({
 container: {
  flex: 1,
  alignItems: 'center',
  justifyContent: 'center',
 },
});

Show More

```

### Example: Callback for screen capture
Callback for screen capture
```
import * as ScreenCapture from 'expo-screen-capture';
import { useEffect } from 'react';
import { Button, StyleSheet, View } from 'react-native';
export default function useScreenCaptureCallback() {
 // Only use this if you add the READ_MEDIA_IMAGES permission to your AndroidManifest.xml
 const hasPermissions = async () => {
  const { status } = await ScreenCapture.requestPermissionsAsync();
  return status === 'granted';
 };
 useEffect(() => {
  let subscription;
  const addListenerAsync = async () => {
   if (await hasPermissions()) {
    subscription = ScreenCapture.addScreenshotListener(() => {
     alert('Thanks for screenshotting my beautiful app 😊');
    });
   } else {
    console.error('Permissions needed to subscribe to screenshot events are missing!');
   }
  };
  addListenerAsync();
  return () => {
   subscription?.remove();
  };
 }, []);
}

Show More

```

## API
```
import * as ScreenCapture from 'expo-screen-capture';

```

## Hooks
### `usePermissions(options)`
Android
iOS
Parameter| Type  
---|---  
options(optional)| `PermissionHookOptions[](https://docs.expo.dev/versions/latest/sdk/screen-capture/#permissionhookoptions)<object>`  
Check or request permissions necessary for detecting when a screenshot is taken. This uses both [`requestPermissionsAsync`](https://docs.expo.dev/versions/latest/sdk/screen-capture/#screencapturerequestpermissionsasync) and [`getPermissionsAsync`](https://docs.expo.dev/versions/latest/sdk/screen-capture/#screencapturegetpermissionsasync) to interact with the permissions.
Returns:
`[null | PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/screen-capture/#permissionresponse), RequestPermissionMethod<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/screen-capture/#permissionresponse)>, GetPermissionMethod<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/screen-capture/#permissionresponse)>]`
Example
```
const [status, requestPermission] = ScreenCapture.usePermissions();

```

### `usePreventScreenCapture(key)`
Android
iOS
Parameter| Type| Description  
---|---|---  
key(optional)| `string`| If provided, this will prevent multiple instances of this hook or the `preventScreenCaptureAsync` and `allowScreenCaptureAsync` methods from conflicting with each other. This argument is useful if you have multiple active components using the `allowScreenCaptureAsync` hook.Default:`'default'`  
A React hook to prevent screen capturing for as long as the owner component is mounted.
Returns:
`void`
## Methods
### `ScreenCapture.allowScreenCaptureAsync(key)`
Android
iOS
Parameter| Type| Description  
---|---|---  
key(optional)| `string`| This will prevent multiple instances of the `preventScreenCaptureAsync` and `allowScreenCaptureAsync` methods from conflicting with each other. If provided, the value must be the same as the key passed to `preventScreenCaptureAsync` in order to re-enable screen capturing.Default:`'default'`  
Re-allows the user to screen record or screenshot your app. If you haven't called `preventScreenCapture()` yet, this method does nothing.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `ScreenCapture.getPermissionsAsync()`
Android
iOS
Checks user's permissions for detecting when a screenshot is taken.
> Only Android requires additional permissions to detect screenshots. On iOS devices, this method will always resolve to a `granted` permission response.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/screen-capture/#permissionresponse)>`
A promise that resolves to a [`PermissionResponse`](https://docs.expo.dev/versions/latest/sdk/screen-capture/#permissionresponse) object.
### `ScreenCapture.isAvailableAsync()`
Android
iOS
Returns whether the Screen Capture API is available on the current device.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
A promise that resolves to a `boolean` indicating whether the Screen Capture API is available on the current device.
### `ScreenCapture.preventScreenCaptureAsync(key)`
Android
iOS 11+
Parameter| Type| Description  
---|---|---  
key(optional)| `string`| Optional. If provided, this will help prevent multiple instances of the `preventScreenCaptureAsync` and `allowScreenCaptureAsync` methods (and `usePreventScreenCapture` hook) from conflicting with each other. When using multiple keys, you'll have to re-allow each one in order to re-enable screen capturing.Default:`'default'`  
Prevents screenshots and screen recordings until `allowScreenCaptureAsync` is called or the app is restarted. If you are already preventing screen capture, this method does nothing (unless you pass a new and unique `key`).
> Please note that on iOS, this will only prevent screen recordings, and is only available on iOS 11 and newer. On older iOS versions, this method does nothing.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `ScreenCapture.requestPermissionsAsync()`
Android
iOS
Asks the user to grant permissions necessary for detecting when a screenshot is taken.
> Only Android requires additional permissions to detect screenshots. On iOS devices, this method will always resolve to a `granted` permission response.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/screen-capture/#permissionresponse)>`
A promise that resolves to a [`PermissionResponse`](https://docs.expo.dev/versions/latest/sdk/screen-capture/#permissionresponse) object.
## Event Subscriptions
### `ScreenCapture.addScreenshotListener(listener)`
Android
iOS
Parameter| Type| Description  
---|---|---  
listener| `() => void`| The function that will be executed when the user takes a screenshot. This function accepts no arguments.  
Adds a listener that will fire whenever the user takes a screenshot while the app is foregrounded. On Android, this method requires the `READ_EXTERNAL_STORAGE` permission. You can request this with [`MediaLibrary.requestPermissionsAsync()`](https://docs.expo.dev/versions/latest/sdk/media-library#medialibraryrequestpermissionsasync).
Returns:
`EventSubscription`
A `Subscription` object that you can use to unregister the listener, either by calling `remove()` or passing it to `removeScreenshotListener`.
### `ScreenCapture.removeScreenshotListener(subscription)`
Android
iOS
Parameter| Type| Description  
---|---|---  
subscription| `EventSubscription`| Subscription returned by `addScreenshotListener`.  
Removes the subscription you provide, so that you are no longer listening for screenshots. You can also call `remove()` on that `Subscription` object.
Returns:
`void`
Example
```
let mySubscription = addScreenshotListener(() => {
 console.log("You took a screenshot!");
});
...
mySubscription.remove();
// OR
removeScreenshotListener(mySubscription);

```

## Interfaces
### `PermissionResponse`
Android
iOS
An object obtained by permissions get and request functions.
Property| Type| Description  
---|---|---  
canAskAgain| `boolean`| Indicates if user can be asked again for specific permission. If not, one should be directed to the Settings app in order to enable/disable the permission.  
expires| `PermissionExpiration[](https://docs.expo.dev/versions/latest/sdk/screen-capture/#permissionexpiration)`| Determines time when the permission expires.  
granted| `boolean`| A convenience boolean that indicates if the permission is granted.  
status| `PermissionStatus[](https://docs.expo.dev/versions/latest/sdk/screen-capture/#permissionstatus)`| Determines the status of the permission.  
## Types
### `PermissionHookOptions`
Android
iOS
Literal Type: `union`
Acceptable values are: `PermissionHookBehavior` | `Options`
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

