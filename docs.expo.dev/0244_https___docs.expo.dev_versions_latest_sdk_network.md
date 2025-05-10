---
url: https://docs.expo.dev/versions/latest/sdk/network
title: https://docs.expo.dev/versions/latest/sdk/network
date: 2025-04-30T17:16:56.371790
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo Network
A library that provides access to the device's network such as its IP address, MAC address, and airplane mode status.
Android
iOS
tvOS
Web
Bundled version:
~7.0.5
`expo-network` provides useful information about the device's network such as its IP address, MAC address, and airplane mode status.
## Installation
Terminal
Copy
`- ``npx expo install expo-network`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Configuration
On Android, this module requires permissions to access the network and Wi-Fi state. The permissions `ACCESS_NETWORK_STATE` and `ACCESS_WIFI_STATE` are added automatically.
## API
```
import * as Network from 'expo-network';

```

## Hooks
### `useNetworkState()`
Android
iOS
tvOS
Web
Returns the current network state of the device. This method initiates a listener for network state changes and cleans up before unmounting.
Returns:
The current network state of the device, including connectivity and type.
Example
```
const networkState = useNetworkState();
console.log(`Current network type: ${networkState.type}`);

```

## Methods
### `Network.getIpAddressAsync()`
Android
iOS
tvOS
Web
Gets the device's current IPv4 address. Returns `0.0.0.0` if the IP address could not be retrieved.
On web, this method uses the third-party [`ipify service`](https://www.ipify.org/) to get the public IP address of the current device.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<string>`
A `Promise` that fulfils with a `string` of the current IP address of the device's main network interface. Can only be IPv4 address.
Example
```
await Network.getIpAddressAsync();
// "92.168.32.44"

```

### `Network.getNetworkStateAsync()`
Android
iOS
tvOS
Web
Gets the device's current network connection state.
On web, `navigator.connection.type` is not available on browsers. So if there is an active network connection, the field `type` returns `NetworkStateType.UNKNOWN`. Otherwise, it returns `NetworkStateType.NONE`.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
A `Promise` that fulfils with a `NetworkState` object.
Example
```
await Network.getNetworkStateAsync();
// {
//  type: NetworkStateType.CELLULAR,
//  isConnected: true,
//  isInternetReachable: true,
// }

```

### `Network.isAirplaneModeEnabledAsync()`
Android
Tells if the device is in airplane mode.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
Returns a `Promise` that fulfils with a `boolean` value for whether the device is in airplane mode or not.
Example
```
await Network.isAirplaneModeEnabledAsync();
// false

```

## Event Subscriptions
### `Network.addNetworkStateListener(listener)`
Android
iOS
tvOS
Web
Parameter| Type| Description  
---|---|---  
listener| `(event: NetworkState[](https://docs.expo.dev/versions/latest/sdk/network/#networkstate)) => void`| Callback to execute when the network state changes. The callback is provided with a single argument that is an object containing information about the network state.  
Adds a listener that will fire whenever the network state changes.
Returns:
`EventSubscription`
A subscription object with a remove function to unregister the listener.
Example
```
const subscription = addNetworkStateListener(({ type, isConnected, isInternetReachable }) => {
 console.log(`Network type: ${type}, Connected: ${isConnected}, Internet Reachable: ${isInternetReachable}`);
});

```

## Types
### `NetworkState`
Android
iOS
tvOS
Web
Property| Type| Description  
---|---|---  
isConnected(optional)| `boolean`| If there is an active network connection. Note that this does not mean that internet is reachable. This field is `false` if the type is either `Network.NetworkStateType.NONE` or `Network.NetworkStateType.UNKNOWN`, `true` otherwise.  
isInternetReachable(optional)| `boolean`| If the internet is reachable with the currently active network connection. On Android, this depends on `NetInfo.isConnected()` (API level < 29) or `ConnectivityManager.getActiveNetwork()` (API level >= 29). On iOS, this value will always be the same as `isConnected`.  
type(optional)| `NetworkStateType[](https://docs.expo.dev/versions/latest/sdk/network/#networkstatetype)`| A [`NetworkStateType`](https://docs.expo.dev/versions/latest/sdk/network/#networkstatetype) enum value that represents the current network connection type.  
### `NetworkStateEvent`
Android
iOS
tvOS
Web
Type: 
Represents an event that provides the updated network state when there is a change in the network status. This is passed as the argument to listeners registered with [`addNetworkStateListener()`](https://docs.expo.dev/versions/latest/sdk/network/#networkaddnetworkstatelistenerlistener).
## Enums
### `NetworkStateType`
Android
iOS
tvOS
Web
An enum of the different types of devices supported by Expo.
#### `BLUETOOTH`
Android
`NetworkStateType.BLUETOOTH ＝ "BLUETOOTH"`
Active network connection over Bluetooth.
#### `CELLULAR`
Android
iOS
`NetworkStateType.CELLULAR ＝ "CELLULAR"`
Active network connection over mobile data or [`DUN-specific`](https://developer.android.com/reference/android/net/ConnectivityManager#TYPE_MOBILE_DUN) mobile connection when setting an upstream connection for tethering.
#### `ETHERNET`
Android
iOS
`NetworkStateType.ETHERNET ＝ "ETHERNET"`
Active network connection over Ethernet.
#### `NONE`
`NetworkStateType.NONE ＝ "NONE"`
No active network connection detected.
#### `OTHER`
Android
`NetworkStateType.OTHER ＝ "OTHER"`
Active network connection over other network connection types.
#### `UNKNOWN`
`NetworkStateType.UNKNOWN ＝ "UNKNOWN"`
The connection type could not be determined.
#### `VPN`
Android
`NetworkStateType.VPN ＝ "VPN"`
Active network connection over VPN.
#### `WIFI`
Android
iOS
`NetworkStateType.WIFI ＝ "WIFI"`
Active network connection over Wi-Fi.
#### `WIMAX`
Android
`NetworkStateType.WIMAX ＝ "WIMAX"`
Active network connection over WiMAX.
## Error codes
Code| Description  
---|---  
ERR_NETWORK_IP_ADDRESS| On Android, there may be an unknown Wi-Fi host when trying to access `WifiManager` in `getIpAddressAsync`. On iOS, no network interfaces could be retrieved.  
ERR_NETWORK_UNDEFINED_INTERFACE| An undefined `interfaceName` was passed as an argument in `getMacAddressAsync`.  
ERR_NETWORK_SOCKET_EXCEPTION| An error was encountered in creating or accessing the socket in `getMacAddressAsync`.  
ERR_NETWORK_INVALID_PERMISSION_INTERNET| There are invalid permissions for [`android.permission.ACCESS_WIFI_STATE`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_WIFI_STATE) in `getMacAddressAsync`.  
ERR_NETWORK_NO_ACCESS_NETWORKINFO| Unable to access network information

