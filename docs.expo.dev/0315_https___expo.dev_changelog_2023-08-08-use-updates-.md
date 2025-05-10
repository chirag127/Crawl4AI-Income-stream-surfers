---
url: https://expo.dev/changelog/2023-08-08-use-updates-api
title: https://expo.dev/changelog/2023-08-08-use-updates-api
date: 2025-04-30T17:18:38.392743
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [UseUpdates() API for expo-updates](https://expo.dev/changelog/2023-08-08-use-updates-api)
Aug 8, 2023 by
Doug Lowder
The `expo-updates` module allows your app to download and manage remote updates to your application code.
We now provide a React hook, `useUpdates()`, for hooking into state and lifecycle updates from the module. The new hook makes use of a new state machine implemented within the native code.
Features:
  * Wraps information on the currently running app bundle, and any available or downloaded new updates
  * Reads from and receives change events from the native state machine, so it always reflects the current state of the system
  * Can be used from any component in the application
  * Tracks the last time the device checked the update server for an available update
  * Existing async methods (`checkForUpdateAsync()`, `fetchUpdateAsync()`) can be called without waiting for results -- the hook will automatically refresh when the methods complete
  * Surfaces errors that occur during initialization, checking for update, or downloading an update


The `useUpdates()` hook is currently in alpha and will be stable in SDK 50.
## [Example app ](https://expo.dev/changelog/2023-08-08-use-updates-api#example-app)
We have created the [Updates API Demo app](https://github.com/expo/UpdatesAPIDemo) as a working example of an app that uses the new API.
## [Example usage ](https://expo.dev/changelog/2023-08-08-use-updates-api#example-usage)
Code
Copy
```

import{StatusBar}from'expo-status-bar';
import*asUpdatesfrom'expo-updates';
import{ useEffect }from'react';
import{Text,View}from'react-native';
exportdefaultfunctionUpdatesDemo(){
const{ currentlyRunning, isUpdateAvailable, isUpdatePending }=Updates.useUpdates();
// If true, we show the button to download and run the update
const showDownloadButton = isUpdateAvailable;
useEffect(()=>{
if(isUpdatePending){
// Update has been successfully downloaded,
// so reload with the new update bundle
Updates.reloadAsync();
},[isUpdatePending]);
// Show whether or not we are running embedded code or an update
const runTypeMessage = currentlyRunning.isEmbeddedLaunch
?'This app is running from built-in code'
:'This app is running an update';
return(
<View style={styles.container}>
<Text style={styles.headerText}>UpdatesDemo</Text>
<Text>{runTypeMessage}</Text>
<Button
    pressHandler={()=>Updates.checkForUpdateAsync()}
    text="Check manually for updates"
/>
{showDownloadButton &&(
<Button pressHandler={()=>Updates.fetchUpdateAsync()} text="Download and run update"/>
)}
<StatusBar style="auto"/>
</View>
);

```


