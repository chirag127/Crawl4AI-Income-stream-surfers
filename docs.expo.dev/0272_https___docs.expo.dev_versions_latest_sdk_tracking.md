---
url: https://docs.expo.dev/versions/latest/sdk/tracking-transparency
title: https://docs.expo.dev/versions/latest/sdk/tracking-transparency
date: 2025-04-30T17:17:50.610689
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo TrackingTransparency
A library for requesting permission to track the users on devices using iOS 14 and higher.
Android
iOS
tvOS
Bundled version:
~5.1.1
A library for requesting permission to track the user or their device. Examples of data used for tracking include email address, device ID, advertising ID, and more. This permission is only necessary on iOS 14 and higher; on iOS 13 and below this permission is always granted. If the "Allow Apps to Request to Track" device-level setting is off, this permission will be denied. Be sure to add `NSUserTrackingUsageDescription` to your [Info.plist](https://docs.expo.dev/versions/latest/config/app#infoplist) to explain how the user will be tracked. Otherwise, your app will be rejected by Apple.
For more information on Apple's new App Tracking Transparency framework, see their [documentation](https://developer.apple.com/app-store/user-privacy-and-data-use/).
## Installation
Terminal
Copy
`- ``npx expo install expo-tracking-transparency`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Configuration in app config
You can configure `expo-tracking-transparency` using its built-in [config plugin](https://docs.expo.dev/config-plugins/introduction) if you use config plugins in your project ([EAS Build](https://docs.expo.dev/build/introduction) or `npx expo run:[android|ios]`). The plugin allows you to configure various properties that cannot be set at runtime and require building a new app binary to take effect.
### Example app.json with config plugin
app.json
Copy
```
{
 "expo": {
  "plugins": [
   [
    "expo-tracking-transparency",
    {
     "userTrackingPermission": "This identifier will be used to deliver personalized ads to you."
    }
   ]
  ]
 }
}

```

### Configurable properties
Name| Default| Description  
---|---|---  
`userTrackingPermission`| `"Allow this app to collect app-related data that can be used for tracking you or your device."`| Only for: iOSSets the iOS `NSUserTrackingUsageDescription` permission message in Info.plist.  
Are you using this library in an existing React Native app?
If you're not using Continuous Native Generation ([CNG](https://docs.expo.dev/workflow/continuous-native-generation)) (you're using native android and ios projects manually), then you need to configure following permissions in your native projects:
  * For Android, add `com.google.android.gms.permission.AD_ID` permission to your project's android/app/src/main/AndroidManifest.xml.
```
<uses-permission android:name="com.google.android.gms.permission.AD_ID"/>

```

  * For iOS, add `NSUserTrackingUsageDescription` key to your project's ios/[app]/Info.plist:
```
<key>NSUserTrackingUsageDescription</key>
<string>Your custom usage description string here.</string>

```



## Usage
Basic tracking transparency usage
```
import { useEffect } from 'react';
import { Text, StyleSheet, View } from 'react-native';
import { requestTrackingPermissionsAsync } from 'expo-tracking-transparency';
export default function App() {
 useEffect(() => {
  (async () => {
   const { status } = await requestTrackingPermissionsAsync();
   if (status === 'granted') {
    console.log('Yay! I have user permission to track data');
   }
  })();
 }, []);
 return (
  <View style={styles.container}><Text>Tracking Transparency Module Example</Text></View>
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

## API
```
import * as ExpoTrackingTransparency from 'expo-tracking-transparency';

```

## Hooks
### `useTrackingPermissions(options)`
Android
iOS
tvOS
Parameter| Type  
---|---  
options(optional)| `PermissionHookOptions[](https://docs.expo.dev/versions/latest/sdk/tracking-transparency/#permissionhookoptions)<object>`  
Check or request the user to authorize or deny access to app-related data that can be used for tracking the user or the device. Examples of data used for tracking include email address, device ID, advertising ID, etc. On iOS 14.5 and above, if the user denies this permission, any attempt to collect the IDFA will return a string of 0s.
The system remembers the user’s choice and doesn’t prompt again unless a user uninstalls and then reinstalls the app on the device.
On Android, web, and iOS 13 and below, this method always returns that the permission was granted.
Returns:
`[null | PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/tracking-transparency/#permissionresponse), RequestPermissionMethod<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/tracking-transparency/#permissionresponse)>, GetPermissionMethod<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/tracking-transparency/#permissionresponse)>]`
Example
```
const [status, requestPermission] = useTrackingPermissions();

```

## Methods
### `getAdvertisingId()`
Android
iOS
tvOS
Gets the advertising ID, a UUID string intended only for advertising. Use this string for frequency capping, attribution, conversion events, estimating the number of unique users, advertising fraud detection, and debugging.
As a best practice, don't store the advertising ID. Instead, call this function each time your app needs to use the advertising ID. Users can change whether they allow app tracking and can reset their advertising ID at any time in their system settings. Check your app's authorization using `getTrackingPermissionsAsync()` to determine the user's intent.
On Android, this function returns the "Android Advertising ID" ([AAID](https://developers.google.com/android/reference/com/google/android/gms/ads/identifier/AdvertisingIdClient.Info#public-string-getid)). On Android devices that support multiple users, including guest users, it's possible for your app to obtain different advertising IDs on the same device. These different IDs correspond to different users who could be signed in on that device. See Google's documentation for more information: [Get a user-resettable advertising ID](https://developer.android.com/training/articles/ad-id).
On iOS, this function returns the "Identifier for Advertisers" ([IDFA](https://developer.apple.com/documentation/adsupport/asidentifiermanager/advertisingidentifier)), a string that's unique to each device. On devices running iOS 14.5 and newer, your app must request tracking authorization using `requestTrackingPermissionsAsync()` before it can get the advertising identifier.
Returns:
`string | null`
Returns either a UUID `string` or `null`. It returns null in the following cases:
  * On Android, when `isLimitAdTrackingEnabled()` is `true`
  * In the iOS simulator, regardless of any settings
  * On devices running iOS 14.5 and later if you haven't received permission using `requestTrackingPermissionsAsync()`
  * On iOS, if you've requested permission and the user declines
  * On iOS, when a profile or configuration restricts access to the advertising identifier, such as when the user has turned off the system-wide "Allow Apps to Request to Track" setting


Example
```
TrackingTransparency.getAdvertisingId();
// "E9228286-4C4E-4789-9D95-15827DCB291B"

```

### `getTrackingPermissionsAsync()`
Android
iOS
tvOS
Checks whether or not the user has authorized the app to access app-related data that can be used for tracking the user or the device. See `requestTrackingPermissionsAsync` for more details.
On Android, web, and iOS 13 and below, this method always returns that the permission was granted.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/tracking-transparency/#permissionresponse)>`
Example
```
const { granted } = await getTrackingPermissionsAsync();
if (granted) {
 // Your app is authorized to track the user or their device
}

```

### `isAvailable()`
Android
iOS
tvOS
Returns whether the TrackingTransparency API is available on the current device.
Returns:
`boolean`
On devices where the Tracking Transparency API is unavailable, the get and request permissions methods will always resolve to `granted`.
### `requestTrackingPermissionsAsync()`
Android
iOS
tvOS
Requests the user to authorize or deny access to app-related data that can be used for tracking the user or the device. Examples of data used for tracking include email address, device ID, advertising ID, etc. On iOS 14.5 and above, if the user denies this permission, any attempt to collect the IDFA will return a string of 0s.
The system remembers the user’s choice and doesn’t prompt again unless a user uninstalls and then reinstalls the app on the device.
On Android, web, and iOS 13 and below, this method always returns that the permission was granted.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/tracking-transparency/#permissionresponse)>`
Example
```
const { granted } = await requestTrackingPermissionsAsync();
if (granted) {
 // Your app is authorized to track the user or their device
}

```

## Interfaces
### `PermissionResponse`
Android
iOS
tvOS
An object obtained by permissions get and request functions.
Property| Type| Description  
---|---|---  
canAskAgain| `boolean`| Indicates if user can be asked again for specific permission. If not, one should be directed to the Settings app in order to enable/disable the permission.  
expires| `PermissionExpiration[](https://docs.expo.dev/versions/latest/sdk/tracking-transparency/#permissionexpiration)`| Determines time when the permission expires.  
granted| `boolean`| A convenience boolean that indicates if the permission is granted.  
status| `PermissionStatus[](https://docs.expo.dev/versions/latest/sdk/tracking-transparency/#permissionstatus)`| Determines the status of the permission.  
## Types
### `PermissionExpiration`
Android
iOS
tvOS
Literal Type: `union`
Permission expiration time. Currently, all permissions are granted permanently.
Acceptable values are: `'never'` | `number`
### `PermissionHookOptions`
Android
iOS
tvOS
Literal Type: `union`
Acceptable values are: `PermissionHookBehavior` | `Options`
## Enums
### `PermissionStatus`
Android
iOS
tvOS
#### `DENIED`
`PermissionStatus.DENIED ＝ "denied"`
User has denied the permission.
#### `GRANTED`
`PermissionStatus.GRANTED ＝ "granted"`
User has granted the permission.
#### `UNDETERMINED`
`PermissionStatus.UNDETERMINED ＝ "undetermined"`
User hasn't granted or denied the permission yet.
## Permissions
### Android
The following permissions are added automatically through the library's AndroidManifest.xml.
Android Permission| Description  
---|---  
`com.google.android.gms.permission.AD_ID`| Allows access to the Advertising ID for tracking and analytics. Required for apps targeting Android 13 (API level 33) or higher that use Google Play services' Advertising ID.  
### iOS
The following usage description keys are used by this library:
Info.plist Key| Description  
---|---  
`NSUserTrackingUsageDescription`| A message that informs the user why an app is requesting permission to use data for tracking the user or the device.

