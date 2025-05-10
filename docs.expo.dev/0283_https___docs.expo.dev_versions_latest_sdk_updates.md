---
url: https://docs.expo.dev/versions/latest/sdk/updates
title: https://docs.expo.dev/versions/latest/sdk/updates
date: 2025-04-30T17:17:54.315275
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo Updates
A library that enables your app to manage remote updates to your application code.
Android
iOS
tvOS
Bundled version:
~0.27.4
`expo-updates` is a library that enables your app to manage remote updates to your application code. It communicates with the configured remote update service to get information about available updates.
## Installation
The `expo-updates` library can be automatically configured using [EAS Update](https://docs.expo.dev/eas-update/introduction), which is a hosted service that manages and serves updates to your app. To get started with EAS Update, follow the instructions in the [Get started](https://docs.expo.dev/eas-update/getting-started) guide.
Alternatively, it is also possible to configure the `expo-updates` library manually in cases where a different remote update service is required or configuration is only specified in native files.
Manual installation, configuration, and custom remote update services
Terminal
Copy
`- ``npx expo install expo-updates`
If you're installing this library in a [bare React Native app](https://docs.expo.dev/bare/overview) or a generic app with manually configured native code, follow these [installation instructions](https://docs.expo.dev/bare/installing-updates).
If using [app config](https://docs.expo.dev/workflow/configuration) for configuration, this library can be configured by setting at least the following app config properties:
  * [`updates.url`](https://docs.expo.dev/versions/latest/config/app#updates): a URL of a remote service implementing the [Expo Updates protocol](https://docs.expo.dev/technical-specs/expo-updates-1)
  * [`runtimeVersion`](https://docs.expo.dev/versions/latest/config/app#runtimeversion): a [runtime version](https://docs.expo.dev/versions/latest/sdk/updates#runtime-version)


The remote service must implement the [Expo Updates protocol](https://docs.expo.dev/technical-specs/expo-updates-1). [EAS Update](https://docs.expo.dev/eas-update/introduction) is one such service, but it is also possible to use this library with a custom server.
[Custom Expo Updates ServerExample implementation of a custom server and an app using that server](https://github.com/expo/custom-expo-updates-server)
## Configuration
There are build-time configuration options that control the behavior of the library. For most apps, these configuration values are set in the [app config](https://docs.expo.dev/workflow/configuration) under the [`updates` property](https://docs.expo.dev/versions/latest/config/app#updates).
[App config property](https://docs.expo.dev/versions/latest/config/app#updates)| Default| Required?| iOS plist/dictionary key| Android meta-data name| Android Map key  
---|---|---|---|---|---  
`true`| `EXUpdatesEnabled`| `expo.modules.updates.ENABLED`| `enabled`  
(none)| `EXUpdatesURL`| `expo.modules.updates.EXPO_UPDATE_URL`| `updateUrl`  
[`updates.requestHeaders`](https://docs.expo.dev/versions/latest/config/app#requestheaders)| (none)| `EXUpdatesRequestHeaders`| `expo.modules.updates.UPDATES_CONFIGURATION_REQUEST_HEADERS_KEY`| `requestHeaders`  
(none)| `EXUpdatesRuntimeVersion`| `expo.modules.updates.EXPO_RUNTIME_VERSION`| `runtimeVersion`  
[`updates.checkAutomatically`](https://docs.expo.dev/versions/latest/config/app#checkautomatically)| `ALWAYS`| `EXUpdatesCheckOnLaunch`| `expo.modules.updates.EXPO_UPDATES_CHECK_ON_LAUNCH`| `checkOnLaunch`  
[`updates.fallbackToCacheTimeout`](https://docs.expo.dev/versions/latest/config/app#fallbacktocachetimeout)| `EXUpdatesLaunchWaitMs`| `expo.modules.updates.EXPO_UPDATES_LAUNCH_WAIT_MS`| `launchWaitMs`  
[`updates.useEmbeddedUpdate`](https://docs.expo.dev/versions/latest/config/app#useembeddedupdate)| `true`| `EXUpdatesHasEmbeddedUpdate`| `expo.modules.updates.HAS_EMBEDDED_UPDATE`| `hasEmbeddedUpdate`  
[`updates.codeSigningCertificate`](https://docs.expo.dev/versions/latest/config/app#codesigningcertificate)| (none)| `EXUpdatesCodeSigningCertificate`| `expo.modules.updates.CODE_SIGNING_CERTIFICATE`| `codeSigningCertificate`  
[`updates.codeSigningMetadata`](https://docs.expo.dev/versions/latest/config/app#codesigningmetadata)| (none)| `EXUpdatesCodeSigningMetadata`| `expo.modules.updates.CODE_SIGNING_METADATA`| `codeSigningMetadata`  
[`updates.assetPatternsToBeBundled`](https://docs.expo.dev/versions/latest/config/app#assetpatternstobebundled)| (none)| N/A| N/A| N/A  
The two core required configuration options are:
  * [`updates.url`](https://docs.expo.dev/versions/latest/config/app#updates): the URL at which the library fetches remote updates
  * [`runtimeVersion`](https://docs.expo.dev/versions/latest/config/app#runtimeversion): a [runtime version](https://docs.expo.dev/versions/latest/sdk/updates#runtime-version)


These are configured automatically when following the EAS Update [Get started](https://docs.expo.dev/eas-update/getting-started) guide.
#### Runtime version
Each time you build a binary for your app it includes the native code and configuration present at the time of the build as well as native configuration, and this unique combination is represented by a string called a runtime version. A remote update targets one runtime version, indicating that only binaries with a matching runtime version can load the remote update.
Manual configuration
The runtime version can be managed manually by setting the string value in the config field.
```
{
 "expo": {
  "runtimeVersion": "<runtime_version_string>"
 }
}

```

Automatic configuration using runtime version policies
Runtime version policies derive the runtime version from another piece of information already present in your project. They can be set in the [`runtimeVersion`](https://docs.expo.dev/versions/latest/config/app#runtimeversion) config field as follows:
```
{
 "expo": {
  "runtimeVersion": {
   "policy": "<policy_name>"
  }
 }
}

```

Available policy types:
appVersion
The `"appVersion"` policy is provided for projects with that wish to define their runtime compatibility based on the app version.
For example, in a project that has the following in its app config:
```
{
 "expo": {
  "runtimeVersion": {
   "policy": "appVersion"
  },
  "version": "1.0.0",
  "ios": {
   "buildNumber": "1"
  },
  "android": {
   "versionCode": 1
  }
 }
}

```

The `"appVersion"` policy will set the runtime version to the project's current `"version"` property. In this case, the runtime version for the Android and iOS builds and any updates would be `"1.0.0"`.
This policy is great for projects that contain custom native code and that update the `"version"` field after every public release. To submit an app, the app stores require an updated native version number for each submitted build, which makes this policy convenient if you want to be sure that every version installed on user devices has a different runtime version.
When using this policy, you need to manually update `"version"` field in the app config every time there is a public release, but for Play Store's Internal Test Track and the App Store's TestFlight uploads, you can rely on `"autoIncrement"` option in eas.json to [manage versions for you](https://docs.expo.dev/build-reference/app-versions#remote-version-source).
nativeVersion
The `"nativeVersion"` policy is provided for projects that wish to define their runtime compatibility based on the project's current `"version"` and `"versionCode"` (Android) or `"buildNumber"` (iOS) properties.
For example, in a project that has the following in its app config:
```
{
 "expo": {
  "runtimeVersion": {
   "policy": "nativeVersion"
  },
  "version": "1.0.0",
  "ios": {
   "buildNumber": "1"
  },
  "android": {
   "versionCode": 1
  }
 }
}

```

The runtime version for the Android and iOS builds and any updates would be the combination of `"[version]([buildNumber|versionCode])"`, which in this case would be `"1.0.0(1)"`.
This policy is great for projects containing custom native code that update the native version numbers (`"buildNumber"` for iOS and `"versionCode"` for Android) for each build. To submit an app, the app stores require an updated native version number for each submitted build, which makes this policy convenient if you want to be sure that every app uploaded to the Play Store's Internal Test Track and the App Store's TestFlight distribution tools has a different `runtimeVersion`.
It's important to know that this policy requires management of the native version numbers manually between each build.
Also, if you select a different native version between Android and iOS, you'll end up with builds and updates with separate runtime versions.
fingerprint
The `"fingerprint"` runtime version policy automatically calculates the runtime version for you, including through changes like SDK upgrades or adding custom native code.
```
{
 "expo": {
  "runtimeVersion": {
   "policy": "fingerprint"
  }
 }
}

```

This policy works for both projects with and without custom native code. It works by using the [`@expo/fingerprint`](https://docs.expo.dev/versions/latest/sdk/fingerprint) package to calculate the hash of your project during builds and updates to determine build-update compatibility (also known as the runtime).
#### Native configuration and overriding
If your project does not use Continuous Native Generation, these configuration values may also be set in your app's native configuration files or overridden at during initialization in native code.
Native configuration instructions
On Android, these options are set as `meta-data` tags in the AndroidManifest.xml file (adjacent to the tags added during installation if auto-setup was used). You can also set or override them at runtime using `UpdatesController.overrideConfiguration()`.
On iOS, these properties are set as keys in the Expo.plist file. You can also set or override them at runtime by calling `AppController.overrideConfiguration`.
Importing Swift generated headers for use in Objective-C++
If your iOS native code or `AppDelegate.mm` is written in Objective-C++, you will need to add the following imports to reference methods on `EXUpdatesAppController`. This is only necessary for overriding configuration at runtime.
```
#import "ExpoModulesCore-Swift.h"
#import "EXUpdatesInterface-Swift.h"
#import "EXUpdates-Swift.h"

```

## Usage
By default, `expo-updates` checks for updates when the app launches. If an update is available, it downloads the update and applies it the next time the app is restarted. You can tune this startup behavior using the `checkAutomatically` and `fallbackToCacheTimeout` configuration options above.
The library also provides a variety of constants to inspect the current update and functions to customize update behavior from your application code (after startup). For example, one common alternative usage pattern is to manually check for updates after the app has started instead of doing the default check on launch.
Example: Check for updates manually
You can configure your app to check for updates manually by doing the following steps:
  1. Set the `checkAutomatically` configuration value to `ON_ERROR_RECOVERY` or `NEVER` to disable the library's default launch behavior.
  2. Add the following code to check for available updates, download them, and reload:
App.js
Copy
```
import { View, Button } from 'react-native';
import * as Updates from 'expo-updates';
function App() {
 async function onFetchUpdateAsync() {
  try {
   const update = await Updates.checkForUpdateAsync();
   if (update.isAvailable) {
    await Updates.fetchUpdateAsync();
    await Updates.reloadAsync();
   }
  } catch (error) {
   // You can also add an alert() to see the error message in case of an error when fetching updates.
   alert(`Error fetching latest Expo update: ${error}`);
  }
 }
 return (
  <View><Button title="Fetch update" onPress={onFetchUpdateAsync} /></View>
 );
}

Show More

```



## Testing
Most of the methods and constants in this library can be used or tested only in release builds. In debug builds, the default behavior is to always load the latest JavaScript from a development server. It is possible to [build a debug version of your app with the same updates behavior as a release build](https://docs.expo.dev/eas-update/debug-advanced#debugging-of-native-code-while-loading-the-app-through-expo-updates). Such an app will not open the latest JavaScript from your development server — it will load published updates just as a release build does. This may be useful for debugging the behavior of your app when it is not connected to a development server.
To test the content of an update in a development build, run [`eas update`](https://docs.expo.dev/eas-update/getting-started) and then browse to the update in your development build. Note that this only simulates what an update will look like in your app, and most of the [Updates API](https://docs.expo.dev/versions/latest/sdk/updates#api) is unavailable when running in a development build.
To test updates in a release build, you can create a [.apk](https://docs.expo.dev/build-reference/apk) or a [simulator build](https://docs.expo.dev/build-reference/simulators), or make a release build locally with `npx expo run:android --variant release` and `npx expo run:ios --configuration Release` (you don't need to submit this build to the store to test). The full [Updates API](https://docs.expo.dev/versions/latest/sdk/updates#api) is available in a release build.
To test the content of an update in Expo Go, run [`eas update`](https://docs.expo.dev/eas-update/getting-started) and then browse to the update in Expo Go. Note that this only simulates what an update will look like in your app, and most of the [Updates API](https://docs.expo.dev/versions/latest/sdk/updates#api) is unavailable when running in Expo Go. Also note that only updates using [Expo Go-compatible libraries](https://docs.expo.dev/workflow/using-libraries#determining-third-party-library-compatibility) are supported.
## API
```
import * as Updates from 'expo-updates';

```

## Constants
### `Updates.channel`
Android
iOS
tvOS
Type: `string | null`
The channel name of the current build, if configured for use with EAS Update. `null` otherwise.
Expo Go and development builds are not set to a specific channel and can run any updates compatible with their native runtime. Therefore, this value will always be `null` when running an update on Expo Go or a development build.
### `Updates.checkAutomatically`
Android
iOS
tvOS
Type: `UpdatesCheckAutomaticallyValue[](https://docs.expo.dev/versions/latest/sdk/updates/#updatescheckautomaticallyvalue) | null`
Determines if and when `expo-updates` checks for and downloads updates automatically on startup.
### `Updates.createdAt`
Android
iOS
tvOS
Type: `null`
If `expo-updates` is enabled, this is a `Date` object representing the creation time of the update that's currently running (whether it was embedded or downloaded at runtime).
In development mode, or any other environment in which `expo-updates` is disabled, this value is null.
### `Updates.emergencyLaunchReason`
Android
iOS
tvOS
Type: `null | string`
If `isEmergencyLaunch` is set to true, this will contain a string error message describing what failed during initialization.
### `Updates.isEmbeddedLaunch`
Android
iOS
tvOS
Type: `boolean`
This will be true if the currently running update is the one embedded in the build, and not one downloaded from the updates server.
### `Updates.isEmergencyLaunch`
Android
iOS
tvOS
Type: `boolean`
`expo-updates` does its very best to always launch monotonically newer versions of your app so you don't need to worry about backwards compatibility when you put out an update. In very rare cases, it's possible that `expo-updates` may need to fall back to the update that's embedded in the app binary, even after newer updates have been downloaded and run (an "emergency launch"). This boolean will be `true` if the app is launching under this fallback mechanism and `false` otherwise. If you are concerned about backwards compatibility of future updates to your app, you can use this constant to provide special behavior for this rare case.
### `Updates.isEnabled`
Android
iOS
tvOS
Type: `boolean`
Whether `expo-updates` is enabled. This may be false in a variety of cases including:
  * enabled set to false in configuration
  * missing or invalid URL in configuration
  * missing runtime version or SDK version in configuration
  * error accessing storage on device during initialization


When false, the embedded update is loaded.
### `Updates.latestContext`
Android
iOS
tvOS
Type: `UpdatesNativeStateMachineContext[](https://docs.expo.dev/versions/latest/sdk/updates/#updatesnativestatemachinecontext)`
### `Updates.launchDuration`
Android
iOS
tvOS
Type: `null | number`
Number of milliseconds it took to launch.
### `Updates.manifest`
Android
iOS
tvOS
Type: `Partial[](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)<>`
If `expo-updates` is enabled, this is the [manifest](https://docs.expo.dev/versions/latest/sdk/constants#manifest) (or [classic manifest](https://docs.expo.dev/versions/latest/sdk/constants#appmanifest)) object for the update that's currently running.
In development mode, or any other environment in which `expo-updates` is disabled, this object is empty.
### `Updates.runtimeVersion`
Android
iOS
tvOS
Type: `string | null`
The runtime version of the current build.
### `Updates.updateId`
Android
iOS
tvOS
Type: `string | null`
The UUID that uniquely identifies the currently running update. The UUID is represented in its canonical string form and will always use lowercase letters. This value is `null` when running in a local development environment or any other environment where `expo-updates` is disabled.
Example
`"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"`
## Hooks
### `useUpdates()`
Android
iOS
tvOS
Hook that obtains information on available updates and on the currently running update.
Returns:
`UseUpdatesReturnType[](https://docs.expo.dev/versions/latest/sdk/updates/#useupdatesreturntype)`
the structures with information on currently running and available updates.
Example
UpdatesDemo.tsx
Copy
```
import { StatusBar } from 'expo-status-bar';
import * as Updates from 'expo-updates';
import { useEffect } from 'react';
import { Button, Text, View } from 'react-native';
export default function UpdatesDemo() {
 const {
  currentlyRunning,
  isUpdateAvailable,
  isUpdatePending
 } = Updates.useUpdates();
 useEffect(() => {
  if (isUpdatePending) {
   // Update has successfully downloaded; apply it now
   Updates.reloadAsync();
  }
 }, [isUpdatePending]);
 // If true, we show the button to download and run the update
 const showDownloadButton = isUpdateAvailable;
 // Show whether or not we are running embedded code or an update
 const runTypeMessage = currentlyRunning.isEmbeddedLaunch
  ? 'This app is running from built-in code'
  : 'This app is running an update';
 return (
  <View style={styles.container}><Text style={styles.headerText}>Updates Demo</Text><Text>{runTypeMessage}</Text><Button onPress={() => Updates.checkForUpdateAsync()} title="Check manually for updates" />{showDownloadButton ? (
    <Button onPress={() => Updates.fetchUpdateAsync()} title="Download and run update" />
   ) : null}<StatusBar style="auto" /></View>
 );
}

Show More

```

## Classes
### `ExpoUpdatesModule`
Android
iOS
tvOS
Type: Class extends `_default[](https://docs.expo.dev/versions/latest/sdk/updates/#_default)<>` implements `UpdatesModuleInterface[](https://docs.expo.dev/versions/latest/sdk/updates/#updatesmoduleinterface)`
## Methods
### `Updates.checkForUpdateAsync()`
Android
iOS
tvOS
Checks the server to see if a newly deployed update to your project is available. Does not actually download the update. This method cannot be used in development mode, and the returned promise will be rejected if you try to do so.
Checking for an update uses a device's bandwidth and battery life like any network call. Additionally, updates served by Expo may be rate limited. A good rule of thumb to check for updates judiciously is to check when the user launches or foregrounds the app. Avoid polling for updates in a frequent loop.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<UpdateCheckResult[](https://docs.expo.dev/versions/latest/sdk/updates/#updatecheckresult)>`
A promise that fulfills with an [`UpdateCheckResult`](https://docs.expo.dev/versions/latest/sdk/updates/#updatecheckresult) object.
The promise rejects in Expo Go or if the app is in development mode, or if there is an unexpected error or timeout communicating with the server. It also rejects when `expo-updates` is not enabled.
### `Updates.clearLogEntriesAsync()`
Android
iOS
tvOS
Clears existing `expo-updates` log entries.
> For now, this operation does nothing on the client. Once log persistence has been implemented, this operation will actually remove existing logs.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
A promise that fulfills if the clear operation was successful.
The promise rejects if there is an unexpected error in clearing the logs.
### `Updates.fetchUpdateAsync()`
Android
iOS
tvOS
Downloads the most recently deployed update to your project from server to the device's local storage. This method cannot be used in development mode, and the returned promise will be rejected if you try to do so.
> Note: [`reloadAsync()`](https://docs.expo.dev/versions/latest/sdk/updates/#updatesreloadasync) can be called after promise resolution to reload the app using the most recently downloaded version. Otherwise, the update will be applied on the next app cold start.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<UpdateFetchResult[](https://docs.expo.dev/versions/latest/sdk/updates/#updatefetchresult)>`
A promise that fulfills with an [`UpdateFetchResult`](https://docs.expo.dev/versions/latest/sdk/updates/#updatefetchresult) object.
The promise rejects in Expo Go or if the app is in development mode, or if there is an unexpected error or timeout communicating with the server. It also rejects when `expo-updates` is not enabled.
### `Updates.getExtraParamsAsync()`
Android
iOS
tvOS
Retrieves the current extra params.
This method cannot be used in Expo Go or development mode. It also rejects when `expo-updates` is not enabled.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<Record<string, string>>`
### `Updates.readLogEntriesAsync(maxAge)`
Android
iOS
tvOS
Parameter| Type| Description  
---|---|---  
maxAge(optional)| `number`| Sets the max age of retrieved log entries in milliseconds. Default to `3600000` ms (1 hour).Default:`3600000`  
Retrieves the most recent `expo-updates` log entries.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<UpdatesLogEntry[][](https://docs.expo.dev/versions/latest/sdk/updates/#updateslogentry)>`
A promise that fulfills with an array of [`UpdatesLogEntry`](https://docs.expo.dev/versions/latest/sdk/updates/#updateslogentry) objects;
The promise rejects if there is an unexpected error in retrieving the logs.
### `Updates.reloadAsync()`
Android
iOS
tvOS
Instructs the app to reload using the most recently downloaded version. This is useful for triggering a newly downloaded update to launch without the user needing to manually restart the app. Unlike `Expo.reloadAppAsync()` provided by the `expo` package, this function not only reloads the app but also changes the loaded JavaScript bundle to that of the most recently downloaded update.
It is not recommended to place any meaningful logic after a call to `await Updates.reloadAsync()`. This is because the promise is resolved after verifying that the app can be reloaded, and immediately before posting an asynchronous task to the main thread to actually reload the app. It is unsafe to make any assumptions about whether any more JS code will be executed after the `Updates.reloadAsync` method call resolves, since that depends on the OS and the state of the native module and main threads.
This method cannot be used in Expo Go or development mode, and the returned promise will be rejected if you try to do so. It also rejects when `expo-updates` is not enabled.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
A promise that fulfills right before the reload instruction is sent to the JS runtime, or rejects if it cannot find a reference to the JS runtime. If the promise is rejected in production mode, it most likely means you have installed the module incorrectly. Double check you've followed the installation instructions. In particular, on iOS ensure that you set the `bridge` property on `EXUpdatesAppController` with a pointer to the `RCTBridge` you want to reload, and on Android ensure you either call `UpdatesController.initialize` with the instance of `ReactApplication` you want to reload, or call `UpdatesController.setReactNativeHost` with the proper instance of `ReactNativeHost`.
### `Updates.setExtraParamAsync(key, value)`
Android
iOS
tvOS
Parameter| Type  
---|---  
key| `string`  
value| `undefined | null | string`  
Sets an extra param if value is non-null, otherwise unsets the param. Extra params are sent as an [Expo Structured Field Value Dictionary](https://docs.expo.dev/technical-specs/expo-sfv-0) in the `Expo-Extra-Params` header of update requests. A compliant update server may use these params when selecting an update to serve.
This method cannot be used in Expo Go or development mode. It also rejects when `expo-updates` is not enabled.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
## Interfaces
### `UpdatesModuleInterface`
Android
iOS
tvOS
Common interface for all native module implementations (android, ios, web).
Property| Type| Description  
---|---|---  
channel| `string`| Can be empty string  
checkAutomatically| `UpdatesCheckAutomaticallyNativeValue[](https://docs.expo.dev/versions/latest/sdk/updates/#updatescheckautomaticallynativevalue)`  
checkForUpdateAsync| `() => Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<UpdateCheckResultRollBack[](https://docs.expo.dev/versions/latest/sdk/updates/#updatecheckresultrollback) | UpdateCheckResultNotAvailable[](https://docs.expo.dev/versions/latest/sdk/updates/#updatecheckresultnotavailable) | Omit<UpdateCheckResultAvailable, "manifest"> & ({ manifestString: string; } | { manifest: Manifest; })>`  
clearLogEntriesAsync| `() => Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`  
commitTime(optional)| `string`  
emergencyLaunchReason| `null | string`  
fetchUpdateAsync| `() => Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<UpdateFetchResultFailure[](https://docs.expo.dev/versions/latest/sdk/updates/#updatefetchresultfailure) | UpdateFetchResultRollBackToEmbedded[](https://docs.expo.dev/versions/latest/sdk/updates/#updatefetchresultrollbacktoembedded) | Omit<UpdateFetchResultSuccess, "manifest"> & ({ manifestString: string; } | { manifest: Manifest; })>`  
getExtraParamsAsync| `() => Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<Record<string, string>>`  
initialContext| `UpdatesNativeStateMachineContext[](https://docs.expo.dev/versions/latest/sdk/updates/#updatesnativestatemachinecontext) & {  downloadedManifestString: string,   lastCheckForUpdateTimeString: string,   latestManifestString: string,   rollbackString: string }`  
isEmbeddedLaunch| `boolean`  
isEmergencyLaunch| `boolean`  
isEnabled| `boolean`  
isUsingEmbeddedAssets(optional)| `boolean`  
launchDuration| `null | number`  
localAssets(optional)| `Record<string, string>`  
manifest(optional)|   
manifestString(optional)| `string`  
readLogEntriesAsync| `(maxAge: number) => Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<UpdatesLogEntry[][](https://docs.expo.dev/versions/latest/sdk/updates/#updateslogentry)>`  
reload| `() => Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`  
runtimeVersion| `string`| Can be empty string  
setExtraParamAsync| `(key: string, value: null | string) => Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`  
shouldDeferToNativeForAPIMethodAvailabilityInDevelopment| `boolean`  
updateId(optional)| `string`  
## Types
### `CurrentlyRunningInfo`
Android
iOS
tvOS
Structure encapsulating information on the currently running app (either the embedded bundle or a downloaded update).
Property| Type| Description  
---|---|---  
channel(optional)| `string`| The channel name of the current build, if configured for use with EAS Update, `undefined` otherwise.  
createdAt(optional)| | If `expo-updates` is enabled, this is a `Date` object representing the creation time of the update that's currently running (whether it was embedded or downloaded at runtime). In development mode, or any other environment in which `expo-updates` is disabled, this value is undefined.  
emergencyLaunchReason| `string | null`| If `isEmergencyLaunch` is set to true, this will contain a string error message describing what failed during initialization.  
isEmbeddedLaunch| `boolean`| This will be true if the currently running update is the one embedded in the build, and not one downloaded from the updates server.  
isEmergencyLaunch| `boolean`| `expo-updates` does its very best to always launch monotonically newer versions of your app so you don't need to worry about backwards compatibility when you put out an update. In very rare cases, it's possible that `expo-updates` may need to fall back to the update that's embedded in the app binary, even after newer updates have been downloaded and run (an "emergency launch"). This boolean will be `true` if the app is launching under this fallback mechanism and `false` otherwise. If you are concerned about backwards compatibility of future updates to your app, you can use this constant to provide special behavior for this rare case.  
launchDuration(optional)| `number`| Number of milliseconds it took to launch.  
manifest(optional)| `Partial[](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)<>`| If `expo-updates` is enabled, this is the [manifest](https://docs.expo.dev/versions/latest/sdk/updates/#updatesmanifest) object for the update that's currently running. In development mode, or any other environment in which `expo-updates` is disabled, this object is empty.  
runtimeVersion(optional)| `string`| The runtime version of the current build.  
updateId(optional)| `string`| The UUID that uniquely identifies the currently running update if `expo-updates` is enabled. The UUID is represented in its canonical string form and will always use lowercase letters. In development mode, or any other environment in which `expo-updates` is disabled, this value is undefined.Example`"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"`  
### `Manifest`
Android
iOS
tvOS
Literal Type: `union`
Acceptable values are: `ExpoUpdatesManifest[](https://docs.expo.dev/versions/latest/sdk/manifests#expoupdatesmanifest)` | 
### `UpdateCheckResult`
Android
iOS
tvOS
Literal Type: `union`
The result of checking for a new update.
Acceptable values are: `UpdateCheckResultRollBack[](https://docs.expo.dev/versions/latest/sdk/updates/#updatecheckresultrollback)` | `UpdateCheckResultAvailable[](https://docs.expo.dev/versions/latest/sdk/updates/#updatecheckresultavailable)` | `UpdateCheckResultNotAvailable[](https://docs.expo.dev/versions/latest/sdk/updates/#updatecheckresultnotavailable)`
### `UpdateCheckResultAvailable`
Android
iOS
tvOS
The update check result when a new update is found on the server.
Property| Type| Description  
---|---|---  
isAvailable| `true`| Whether an update is available. This property is false for a roll back update.  
isRollBackToEmbedded| `false`| Whether a roll back to embedded update is available.  
manifest| | The manifest of the update when available.  
reason| `undefined`| If no new update is found, this contains one of several enum values indicating the reason.  
> Deprecated
### `UpdateCheckResultFailure`
Android
iOS
tvOS
Type: `UpdateCheckResultNotAvailable[](https://docs.expo.dev/versions/latest/sdk/updates/#updatecheckresultnotavailable)`
### `UpdateCheckResultNotAvailable`
Android
iOS
tvOS
The update check result if no new update was found.
Property| Type| Description  
---|---|---  
isAvailable| `false`| Whether an update is available. This property is false for a roll back update.  
isRollBackToEmbedded| `false`| Whether a roll back to embedded update is available.  
manifest| `undefined`| The manifest of the update when available.  
reason| `UpdateCheckResultNotAvailableReason[](https://docs.expo.dev/versions/latest/sdk/updates/#updatecheckresultnotavailablereason)`| If no new update is found, this contains one of several enum values indicating the reason.  
### `UpdateCheckResultRollBack`
Android
iOS
tvOS
The update check result when a rollback directive is received.
Property| Type| Description  
---|---|---  
isAvailable| `false`| Whether an update is available. This property is false for a roll back update.  
isRollBackToEmbedded| `true`| Whether a roll back to embedded update is available.  
manifest| `undefined`| The manifest of the update when available.  
reason| `undefined`| If no new update is found, this contains one of several enum values indicating the reason.  
> Deprecated
### `UpdateCheckResultSuccess`
Android
iOS
tvOS
Type: `UpdateCheckResultAvailable[](https://docs.expo.dev/versions/latest/sdk/updates/#updatecheckresultavailable)`
### `UpdateFetchResult`
Android
iOS
tvOS
Literal Type: `union`
The result of fetching a new update.
Acceptable values are: `UpdateFetchResultSuccess[](https://docs.expo.dev/versions/latest/sdk/updates/#updatefetchresultsuccess)` | `UpdateFetchResultFailure[](https://docs.expo.dev/versions/latest/sdk/updates/#updatefetchresultfailure)` | `UpdateFetchResultRollBackToEmbedded[](https://docs.expo.dev/versions/latest/sdk/updates/#updatefetchresultrollbacktoembedded)`
### `UpdateFetchResultFailure`
Android
iOS
tvOS
The failed result of fetching a new update.
Property| Type| Description  
---|---|---  
isNew| `false`| Whether the fetched update is new (that is, a different version than what's currently running). Always `false` when `isRollBackToEmbedded` is `true`.  
isRollBackToEmbedded| `false`| Whether the fetched update is a roll back to the embedded update.  
manifest| `undefined`| The manifest of the fetched update.  
### `UpdateFetchResultRollBackToEmbedded`
Android
iOS
tvOS
The roll back to embedded result of fetching a new update.
Property| Type| Description  
---|---|---  
isNew| `false`| Whether the fetched update is new (that is, a different version than what's currently running). Always `false` when `isRollBackToEmbedded` is `true`.  
isRollBackToEmbedded| `true`| Whether the fetched update is a roll back to the embedded update.  
manifest| `undefined`| The manifest of the fetched update.  
### `UpdateFetchResultSuccess`
Android
iOS
tvOS
The successful result of fetching a new update.
Property| Type| Description  
---|---|---  
isNew| `true`| Whether the fetched update is new (that is, a different version than what's currently running). Always `true` when `isRollBackToEmbedded` is `false`.  
isRollBackToEmbedded| `false`| Whether the fetched update is a roll back to the embedded update.  
manifest| | The manifest of the fetched update.  
### `UpdateInfo`
Android
iOS
tvOS
Literal Type: `union`
Combined structure representing any type of update.
Acceptable values are: `UpdateInfoNew[](https://docs.expo.dev/versions/latest/sdk/updates/#updateinfonew)` | `UpdateInfoRollback[](https://docs.expo.dev/versions/latest/sdk/updates/#updateinforollback)`
### `UpdateInfoNew`
Android
iOS
tvOS
Structure representing a new update.
Property| Type| Description  
---|---|---  
createdAt| | For all types of updates, this is a `Date` object representing the creation time or commit time of the update.  
manifest| | For updates of type `UpdateInfoType.NEW`, this is the [manifest](https://docs.expo.dev/versions/latest/sdk/constants/#manifest) for the update.  
type| `UpdateInfoType.NEW`| The type of update.  
updateId| `string`| For updates of type `UpdateInfoType.NEW`, this is a string that uniquely identifies the update. For the manifests used in the current Expo Updates protocol (including EAS Update), this represents the update's UUID in its canonical string form and will always use lowercase letters.Example`"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"`  
### `UpdateInfoRollback`
Android
iOS
tvOS
Structure representing a rollback directive.
Property| Type| Description  
---|---|---  
createdAt| | For all types of updates, this is a `Date` object representing the creation time or commit time of the update.  
manifest| `undefined`| For updates of type `UpdateInfoType.ROLLBACK`, this is always set to `undefined`.  
type| `UpdateInfoType.ROLLBACK`| The type of update.  
updateId| `undefined`| For updates of type `UpdateInfoType.ROLLBACK`, this is always set to `undefined`.  
### `UpdatesCheckAutomaticallyNativeValue`
Android
iOS
tvOS
Literal Type: `string`
Acceptable values are: `'ALWAYS'` | `'ERROR_RECOVERY_ONLY'` | `'NEVER'` | `'WIFI_ONLY'`
### `UpdatesEvents`
Android
iOS
tvOS
Property| Type| Description  
---|---|---  
Expo.nativeUpdatesStateChangeEvent| `(params: any) => void`  
### `UpdatesLogEntry`
Android
iOS
tvOS
An object representing a single log entry from `expo-updates` logging on the client.
Property| Type| Description  
---|---|---  
assetId(optional)| `string`| If present, the unique ID or hash of an asset associated with this log entry.  
code| `UpdatesLogEntryCode[](https://docs.expo.dev/versions/latest/sdk/updates/#updateslogentrycode)`| One of the defined code values for `expo-updates` log entries.  
level| `UpdatesLogEntryLevel[](https://docs.expo.dev/versions/latest/sdk/updates/#updateslogentrylevel)`| One of the defined log level or severity values.  
message| `string`| The log entry message.  
stacktrace(optional)| `string[]`| If present, an Android or iOS native stack trace associated with this log entry.  
timestamp| `number`| The time the log was written, in milliseconds since Jan 1 1970 UTC.  
updateId(optional)| `string`| If present, the unique ID of an update associated with this log entry.  
### `UseUpdatesReturnType`
Android
iOS
tvOS
The structures and methods returned by [`useUpdates()`](https://docs.expo.dev/versions/latest/sdk/updates/#useupdates).
Property| Type| Description  
---|---|---  
availableUpdate(optional)| | If a new available update has been found, either by using [`checkForUpdateAsync()`](https://docs.expo.dev/versions/latest/sdk/updates/#updatescheckforupdateasync), or by the `UpdateEvent` listener in `useUpdates()`, this will contain the information for that update.  
checkError(optional)| | If an error is returned from either the startup check for updates, or a call to [`checkForUpdateAsync()`](https://docs.expo.dev/versions/latest/sdk/updates/#updatescheckforupdateasync), the error description will appear here.  
currentlyRunning| `CurrentlyRunningInfo[](https://docs.expo.dev/versions/latest/sdk/updates/#currentlyrunninginfo)`| Information on the currently running app.  
downloadedUpdate(optional)| | If an available update has been downloaded, this will contain the information for that update.  
downloadError(optional)| | If an error is returned from either a startup update download, or a call to [`fetchUpdateAsync()`](https://docs.expo.dev/versions/latest/sdk/updates/#updatesfetchupdateasync), the error description will appear here.  
initializationError(optional)| | If an error occurs during initialization of [`useUpdates()`](https://docs.expo.dev/versions/latest/sdk/updates/#useupdates), the error description will appear here.  
isChecking| `boolean`| True if the app is currently checking for a new available update from the server.  
isDownloading| `boolean`| True if the app is currently downloading an update from the server.  
isUpdateAvailable| `boolean`| True if a new available update has been found, false otherwise.  
isUpdatePending| `boolean`| True if a new available update is available and has been downloaded.  
lastCheckForUpdateTimeSinceRestart(optional)| | A `Date` object representing the last time this client checked for an available update, or `undefined` if no check has yet occurred since the app started. Does not persist across app reloads or restarts.  
## Enums
### `UpdateCheckResultNotAvailableReason`
Android
iOS
tvOS
#### `NO_UPDATE_AVAILABLE_ON_SERVER`
`UpdateCheckResultNotAvailableReason.NO_UPDATE_AVAILABLE_ON_SERVER ＝ "noUpdateAvailableOnServer"`
No update manifest or rollback directive received from the update server.
#### `ROLLBACK_NO_EMBEDDED`
`UpdateCheckResultNotAvailableReason.ROLLBACK_NO_EMBEDDED ＝ "rollbackNoEmbeddedConfiguration"`
A rollback directive was received from the update server, but this app has no embedded update.
#### `ROLLBACK_REJECTED_BY_SELECTION_POLICY`
`UpdateCheckResultNotAvailableReason.ROLLBACK_REJECTED_BY_SELECTION_POLICY ＝ "rollbackRejectedBySelectionPolicy"`
A rollback directive was received from the update server, but the directive does not pass the configured selection policy.
#### `UPDATE_PREVIOUSLY_FAILED`
`UpdateCheckResultNotAvailableReason.UPDATE_PREVIOUSLY_FAILED ＝ "updatePreviouslyFailed"`
An update manifest was received from the update server, but the update has been previously launched on this device and never successfully launched.
#### `UPDATE_REJECTED_BY_SELECTION_POLICY`
`UpdateCheckResultNotAvailableReason.UPDATE_REJECTED_BY_SELECTION_POLICY ＝ "updateRejectedBySelectionPolicy"`
An update manifest was received from the update server, but the update is not launchable, or does not pass the configured selection policy.
### `UpdateInfoType`
Android
iOS
tvOS
The different possible types of updates. Currently, the only supported type is `UpdateInfoType.NEW`, indicating a new update that can be downloaded and launched on the device. In the future, other types of updates may be added to this list.
#### `NEW`
`UpdateInfoType.NEW ＝ "new"`
This is the type for new updates found on or downloaded from the update server, that are launchable on the device.
#### `ROLLBACK`
`UpdateInfoType.ROLLBACK ＝ "rollback"`
This type is used when an update is a directive to roll back to the embedded bundle.
### `UpdatesCheckAutomaticallyValue`
Android
iOS
tvOS
The possible settings that determine if `expo-updates` will check for updates on app startup. By default, Expo will check for updates every time the app is loaded. Set this to `ON_ERROR_RECOVERY` to disable automatic checking unless recovering from an error. Set this to `NEVER` to completely disable automatic checking.
#### `NEVER`
`UpdatesCheckAutomaticallyValue.NEVER ＝ "NEVER"`
Automatic update checks are off, and update checks must be done through the JS API.
#### `ON_ERROR_RECOVERY`
`UpdatesCheckAutomaticallyValue.ON_ERROR_RECOVERY ＝ "ON_ERROR_RECOVERY"`
Only checks for updates when the app starts up after an error recovery.
#### `ON_LOAD`
`UpdatesCheckAutomaticallyValue.ON_LOAD ＝ "ON_LOAD"`
Checks for updates whenever the app is loaded. This is the default setting.
#### `WIFI_ONLY`
`UpdatesCheckAutomaticallyValue.WIFI_ONLY ＝ "WIFI_ONLY"`
Only checks for updates when the app starts and has a Wi-Fi connection.
### `UpdatesLogEntryCode`
Android
iOS
tvOS
The possible code values for `expo-updates` log entries
#### `ASSETS_FAILED_TO_LOAD`
`UpdatesLogEntryCode.ASSETS_FAILED_TO_LOAD ＝ "AssetsFailedToLoad"`
#### `INITIALIZATION_ERROR`
`UpdatesLogEntryCode.INITIALIZATION_ERROR ＝ "InitializationError"`
#### `JS_RUNTIME_ERROR`
`UpdatesLogEntryCode.JS_RUNTIME_ERROR ＝ "JSRuntimeError"`
#### `NONE`
`UpdatesLogEntryCode.NONE ＝ "None"`
#### `NO_UPDATES_AVAILABLE`
`UpdatesLogEntryCode.NO_UPDATES_AVAILABLE ＝ "NoUpdatesAvailable"`
#### `UNKNOWN`
`UpdatesLogEntryCode.UNKNOWN ＝ "Unknown"`
#### `UPDATE_ASSETS_NOT_AVAILABLE`
`UpdatesLogEntryCode.UPDATE_ASSETS_NOT_AVAILABLE ＝ "UpdateAssetsNotAvailable"`
#### `UPDATE_CODE_SIGNING_ERROR`
`UpdatesLogEntryCode.UPDATE_CODE_SIGNING_ERROR ＝ "UpdateCodeSigningError"`
#### `UPDATE_FAILED_TO_LOAD`
`UpdatesLogEntryCode.UPDATE_FAILED_TO_LOAD ＝ "UpdateFailedToLoad"`
#### `UPDATE_HAS_INVALID_SIGNATURE`
`UpdatesLogEntryCode.UPDATE_HAS_INVALID_SIGNATURE ＝ "UpdateHasInvalidSignature"`
#### `UPDATE_SERVER_UNREACHABLE`
`UpdatesLogEntryCode.UPDATE_SERVER_UNREACHABLE ＝ "UpdateServerUnreachable"`
### `UpdatesLogEntryLevel`
Android
iOS
tvOS
The possible log levels for `expo-updates` log entries
#### `DEBUG`
`UpdatesLogEntryLevel.DEBUG ＝ "debug"`
#### `ERROR`
`UpdatesLogEntryLevel.ERROR ＝ "error"`
#### `FATAL`
`UpdatesLogEntryLevel.FATAL ＝ "fatal"`
#### `INFO`
`UpdatesLogEntryLevel.INFO ＝ "info"`
#### `TRACE`
`UpdatesLogEntryLevel.TRACE ＝ "trace"`
#### `WARN`
`UpdatesLogEntryLevel.WARN ＝ "warn"`
## Error codes
Code| Description  
---|---  
`ERR_UPDATES_DISABLED`| A method call was attempted when the Updates library was disabled, or the application was running in development mode  
`ERR_UPDATES_RELOAD`| An error occurred when trying to reload the application and it could not be reloaded. For bare React Native apps, double-check the setup steps for this library to ensure it has been installed correctly and the proper native initialization methods are called.  
`ERR_UPDATES_CHECK`| An unexpected error occurred when trying to check for new updates. Check the error message for more information.  
`ERR_UPDATES_FETCH`| An unexpected error occurred when trying to fetch a new update. Check the error message for more information.  
`ERR_UPDATES_READ_LOGS`| An unexpected error occurred when trying to read log entries. Check the error message for more information.  
`ERR_NOT_AVAILABLE_IN_DEV_CLIENT`| A method is not available when running in a development build. A release build should be used to test this method.

