---
url: https://docs.expo.dev/versions/latest/sdk/constants
title: https://docs.expo.dev/versions/latest/sdk/constants
date: 2025-04-30T17:15:49.695878
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo Constants
An API that provides system information that remains constant throughout the lifetime of your app's installation.
Android
iOS
tvOS
Web
Bundled version:
~17.0.8
`expo-constants` provides system information that remains constant throughout the lifetime of your app's installation.
## Installation
Terminal
Copy
`- ``npx expo install expo-constants`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## API
```
import Constants from 'expo-constants';

```

## Types
### `AndroidManifest`
Android
Type: `Record<string, any>` extended by:
Property| Type| Description  
---|---|---  
versionCode| `number`| 
> Deprecated Use `expo-application`'s [`Application.nativeBuildVersion`](https://docs.expo.dev/versions/latest/sdk/application#applicationnativebuildversion).
The version code set by `android.versionCode` in app.json. The value is set to `null` in case you run your app in Expo Go.  
### `ClientScopingConfig`
Android
iOS
tvOS
Web
Type: `ClientScopingConfigForReExport[](https://docs.expo.dev/versions/latest/sdk/manifests#clientscopingconfigforreexport)`
### `EASConfig`
Android
iOS
tvOS
Web
Type: `ManifestsEASConfig[](https://docs.expo.dev/versions/latest/sdk/manifests#manifestseasconfig)`
### `ExpoGoConfig`
Android
iOS
tvOS
Web
Type: `ManifestsExpoGoConfig[](https://docs.expo.dev/versions/latest/sdk/manifests#manifestsexpogoconfig)`
### `ExpoGoPackagerOpts`
Android
iOS
tvOS
Web
Type: `ExpoGoPackagerOptsForReExport[](https://docs.expo.dev/versions/latest/sdk/manifests#expogopackageroptsforreexport)`
### `IOSManifest`
iOS
Type: `Record<string, any>` extended by:
Property| Type| Description  
---|---|---  
buildNumber| `string | null`| The build number specified in the embedded Info.plist value for `CFBundleVersion` in this app. In a standalone app, you can set this with the `ios.buildNumber` value in app.json. This may differ from the value in `Constants.expoConfig.ios.buildNumber` because the manifest can be updated, whereas this value will never change for a given native binary. The value is set to `null` in case you run your app in Expo Go.  
model| `string | null`| 
> Deprecated Moved to `expo-device` as [`Device.modelName`](https://docs.expo.dev/versions/latest/sdk/device#devicemodelname).
The human-readable model name of this device. For example, `"iPhone 7 Plus"` if it can be determined, otherwise will be `null`.  
platform| `string`| 
> Deprecated Use `expo-device`'s [`Device.modelId`](https://docs.expo.dev/versions/latest/sdk/device#devicemodelid).
The Apple internal model identifier for this device.Example`iPhone1,1`  
systemVersion| `string`| 
> Deprecated Use `expo-device`'s [`Device.osVersion`](https://docs.expo.dev/versions/latest/sdk/device#deviceosversion).
The version of iOS running on this device.Example`10.3`  
userInterfaceIdiom| `UserInterfaceIdiom[](https://docs.expo.dev/versions/latest/sdk/constants/#userinterfaceidiom)`| 
> Deprecated Use `expo-device`'s [`Device.getDeviceTypeAsync()`](https://docs.expo.dev/versions/latest/sdk/device#devicegetdevicetypeasync).
The user interface idiom of the current device, such as whether the app is running on an iPhone, iPad, Mac or Apple TV.  
### `Manifest`
Android
iOS
tvOS
Web
Type: `ExpoUpdatesManifest[](https://docs.expo.dev/versions/latest/sdk/manifests#expoupdatesmanifest)`
### `ManifestAsset`
Android
iOS
tvOS
Web
Type: `ManifestAssetForReExport[](https://docs.expo.dev/versions/latest/sdk/manifests#manifestassetforreexport)`
type re-exports to prevent breaking change
### `ManifestExtra`
Android
iOS
tvOS
Web
Type: `ManifestExtraForReExport[](https://docs.expo.dev/versions/latest/sdk/manifests#manifestextraforreexport)`
### `NativeConstants`
Android
iOS
tvOS
Web
Type: `Record<string, any>` extended by:
Property| Type| Description  
---|---|---  
appOwnership| `null`| 
> Deprecated Use [`Constants.executionEnvironment`](https://docs.expo.dev/versions/latest/sdk/constants/#executionenvironment) instead.
Returns `expo` when running in Expo Go, otherwise `null`.  
debugMode| `boolean`| Returns `true` when the app is running in debug mode (`__DEV__`). Otherwise, returns `false`.  
deviceName(optional)| `string`| A human-readable name for the device type.  
deviceYearClass| `number | null`| 
> Deprecated Moved to `expo-device` as [`Device.deviceYearClass`](https://docs.expo.dev/versions/latest/sdk/device#deviceyearclass).
The [device year class](https://github.com/facebook/device-year-class) of this device.  
easConfig| `null`| The standard EAS config object populated when using EAS.  
executionEnvironment| `ExecutionEnvironment[](https://docs.expo.dev/versions/latest/sdk/constants/#executionenvironment)`| Returns the current execution environment.  
experienceUrl| `string`  
expoConfig| `{  hostUri: string } | null`| The standard Expo config object defined in app.json and app.config.js files. For both classic and modern manifests, whether they are embedded or remote.  
expoGoConfig| `null`| The standard Expo Go config object populated when running in Expo Go.  
expoRuntimeVersion| `string | null`| Nullable only on the web.  
expoVersion| `string | null`| The version string of the Expo Go app currently running. Returns `null` in bare workflow and web.  
getWebViewUserAgentAsync| `() => Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<string | null>`| Gets the user agent string which would be included in requests sent by a web view running on this device. This is probably not the same user agent you might be providing in your JS `fetch` requests.  
intentUri(optional)| `string`  
isDetached(optional)| `boolean`  
isHeadless| `boolean`| Returns `true` if the app is running in headless mode. Otherwise, returns `false`.  
linkingUri| `string`  
manifest2| `null`| Manifest for Expo apps using modern Expo Updates from a remote source, such as apps that use EAS Update. `Constants.expoConfig` should be used for accessing the Expo config object.  
platform(optional)| `PlatformManifest[](https://docs.expo.dev/versions/latest/sdk/constants/#platformmanifest)`| Returns the specific platform manifest object.
> Note: This is distinct from the `manifest` and `manifest2`.  
sessionId| `string`| A string that is unique to the current session of your app. It is different across apps and across multiple launches of the same app.  
statusBarHeight| `number`| The default status bar height for the device. Does not factor in changes when location tracking is in use or a phone call is active.  
systemFonts| `string[]`| A list of the system font names available on the current device.  
systemVersion(optional)| `number`  
### `PlatformManifest`
Android
iOS
tvOS
Web
Type: `Record<string, any>` extended by:
Property| Type| Description  
---|---|---  
android(optional)| `AndroidManifest[](https://docs.expo.dev/versions/latest/sdk/constants/#androidmanifest)`  
detach(optional)| `{  scheme: string }`  
developer(optional)| `string`  
hostUri(optional)| `string`  
ios(optional)|   
scheme(optional)| `string`  
web(optional)|   
### `WebManifest`
Web
Type: `Record<string, any>`
## Enums
### `AppOwnership`
Android
iOS
tvOS
Web
> Deprecated Use [`Constants.executionEnvironment`](https://docs.expo.dev/versions/latest/sdk/constants/#executionenvironment) instead.
#### `Expo`
`AppOwnership.Expo ＝ "expo"`
The experience is running inside the Expo Go app.
### `ExecutionEnvironment`
Android
iOS
tvOS
Web
#### `Bare`
`ExecutionEnvironment.Bare ＝ "bare"`
#### `Standalone`
`ExecutionEnvironment.Standalone ＝ "standalone"`
#### `StoreClient`
`ExecutionEnvironment.StoreClient ＝ "storeClient"`
### `UserInterfaceIdiom`
Android
iOS
tvOS
Web
Current supported values are `handset`, `tablet`, `desktop` and `tv`. CarPlay will show up as `unsupported`.
#### `Desktop`
`UserInterfaceIdiom.Desktop ＝ "desktop"`
#### `Handset`
`UserInterfaceIdiom.Handset ＝ "handset"`
#### `Tablet`
`UserInterfaceIdiom.Tablet ＝ "tablet"`
#### `TV`
`UserInterfaceIdiom.TV ＝ "tv"`
#### `Unsupported`
`UserInterfaceIdiom.Unsupported ＝ "unsupported"`

