---
url: https://docs.expo.dev/versions/latest/sdk/netinfo
title: https://docs.expo.dev/versions/latest/sdk/netinfo
date: 2025-04-30T17:16:54.574456
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# NetInfo
A cross-platform API that provides access to network information.
Android
iOS
tvOS
Web
Bundled version:
11.4.1
`@react-native-community/netinfo` allows you to get information about connection type and connection quality.
## Installation
Terminal
Copy
`- ``npx expo install @react-native-community/netinfo`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project. Then, follow the [installation instructions](https://github.com/react-native-community/react-native-netinfo#getting-started) provided in the library's README or documentation.
## API
To import this library, use:
```
import NetInfo from '@react-native-community/netinfo';

```

If you want to grab information about the network connection just once, you can use:
```
NetInfo.fetch().then(state => {
 console.log('Connection type', state.type);
 console.log('Is connected?', state.isConnected);
});

```

Or, if you'd rather subscribe to updates about the network state (which then allows you to run code/perform actions anytime the network state changes) use:
```
const unsubscribe = NetInfo.addEventListener(state => {
 console.log('Connection type', state.type);
 console.log('Is connected?', state.isConnected);
});
// To unsubscribe to these update, just use:
unsubscribe();

```

## Accessing the SSID
To access the `ssid` property (available under `state.details.ssid`), there are a few additional configuration steps:
### Android and iOS
  * Request location permissions with [`Location.requestForegroundPermissionsAsync()`](https://docs.expo.dev/versions/latest/sdk/location#locationrequestforegroundpermissionsasync) or [`Location.requestBackgroundPermissionsAsync()`](https://docs.expo.dev/versions/latest/sdk/location#locationrequestbackgroundpermissionsasync).


### iOS only
  * Add the `com.apple.developer.networking.wifi-info` entitlement to your app.json under `ios.entitlements`:
app.json
Copy
```
 "ios": {
  "entitlements": {
   "com.apple.developer.networking.wifi-info": true
  }
 }

```

  * Check the Access Wi-Fi Information box in your app's App Identifier, [which can be found here](https://developer.apple.com/account/resources/identifiers/list).
  * Rebuild your app with [`eas build --platform ios`](https://docs.expo.dev/build/setup#4-run-a-build) or [`npx expo run:ios`](https://docs.expo.dev/more/expo-cli#compiling).


For more information on API and usage, see [`react-native-netinfo` documentation](https://github.com/react-native-community/react-native-netinfo#react-native-communitynetinfo).

