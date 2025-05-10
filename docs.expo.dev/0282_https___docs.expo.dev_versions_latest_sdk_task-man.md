---
url: https://docs.expo.dev/versions/latest/sdk/task-manager
title: https://docs.expo.dev/versions/latest/sdk/task-manager
date: 2025-04-30T17:17:50.738830
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo TaskManager
A library that provides support for tasks that can run in the background.
Android
iOS
Bundled version:
~12.0.6
`expo-task-manager` provides an API that allows you to manage long-running tasks, in particular those tasks that can run while your app is in the background. Some features of this library are used by other libraries under the hood. Here is a list of Expo SDK libraries that use `TaskManager`.
## Libraries using Expo TaskManager


## Installation
Terminal
Copy
`- ``npx expo install expo-task-manager`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Configuration 
iOS
`TaskManager` works out of the box in the Expo Go app on Android. However, on iOS, you'll need to use a [development build](https://docs.expo.dev/develop/development-builds/introduction).
Standalone apps need some extra configuration: on iOS, each background feature requires a special key in `UIBackgroundModes` array in your Info.plist file.
Read more about how to configure this in the reference for each of the [libraries](https://docs.expo.dev/versions/latest/sdk/task-manager#libraries-using-expo-taskmanager) that use `TaskManager`.
## Example
Example
```
import React from 'react';
import { Button, View, StyleSheet } from 'react-native';
import * as TaskManager from 'expo-task-manager';
import * as Location from 'expo-location';
const LOCATION_TASK_NAME = 'background-location-task';
const requestPermissions = async () => {
 const { status: foregroundStatus } = await Location.requestForegroundPermissionsAsync();
 if (foregroundStatus === 'granted') {
  const { status: backgroundStatus } = await Location.requestBackgroundPermissionsAsync();
  if (backgroundStatus === 'granted') {
   await Location.startLocationUpdatesAsync(LOCATION_TASK_NAME, {
    accuracy: Location.Accuracy.Balanced,
   });
  }
 }
};
const PermissionsButton = () => (
 <View style={styles.container}><Button onPress={requestPermissions} title="Enable background location" /></View>
);
TaskManager.defineTask(LOCATION_TASK_NAME, ({ data, error }) => {
 if (error) {
  // Error occurred - check `error.message` for more details.
  return;
 }
 if (data) {
  const { locations } = data;
  // do something with the locations captured in the background
 }
});
const styles = StyleSheet.create({
 container: {
  flex: 1,
  alignItems: 'center',
  justifyContent: 'center',
 },
});
export default PermissionsButton;

Show More

```

## API
```
import * as TaskManager from 'expo-task-manager';

```

## Methods
### `TaskManager.defineTask(taskName, taskExecutor)`
Android
iOS
Parameter| Type| Description  
---|---|---  
taskName| `string`| Name of the task. It must be the same as the name you provided when registering the task.  
taskExecutor| `TaskManagerTaskExecutor[](https://docs.expo.dev/versions/latest/sdk/task-manager/#taskmanagertaskexecutor)<T>`| A function that will be invoked when the task with given `taskName` is executed.  
Defines task function. It must be called in the global scope of your JavaScript bundle. In particular, it cannot be called in any of React lifecycle methods like `componentDidMount`. This limitation is due to the fact that when the application is launched in the background, we need to spin up your JavaScript app, run your task and then shut down — no views are mounted in this scenario.
Returns:
`void`
### `TaskManager.getRegisteredTasksAsync()`
Android
iOS
Provides information about tasks registered in the app.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<TaskManagerTask[][](https://docs.expo.dev/versions/latest/sdk/task-manager/#taskmanagertask)>`
A promise which fulfills with an array of tasks registered in the app.
Example
```
[
 {
  taskName: 'location-updates-task-name',
  taskType: 'location',
  options: {
   accuracy: Location.Accuracy.High,
   showsBackgroundLocationIndicator: false,
  },
 },
 {
  taskName: 'geofencing-task-name',
  taskType: 'geofencing',
  options: {
   regions: [...],
  },
 },
]

```

### `TaskManager.getTaskOptionsAsync(taskName)`
Android
iOS
Parameter| Type| Description  
---|---|---  
taskName| `string`| Name of the task.  
Retrieves `options` associated with the task, that were passed to the function registering the task (e.g. `Location.startLocationUpdatesAsync`).
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<TaskOptions>`
A promise which fulfills with the `options` object that was passed while registering task with given name or `null` if task couldn't be found.
### `TaskManager.isAvailableAsync()`
Android
iOS
Determine if the `TaskManager` API can be used in this app.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
A promise which fulfills with `true` if the API can be used, and `false` otherwise. With Expo Go, `TaskManager` is not available on Android, and does not support background execution on iOS. Use a development build to avoid limitations: <https://expo.fyi/dev-client>. On the web, it always returns `false`.
### `TaskManager.isTaskDefined(taskName)`
Android
iOS
Parameter| Type| Description  
---|---|---  
taskName| `string`| Name of the task.  
Checks whether the task is already defined.
Returns:
`boolean`
### `TaskManager.isTaskRegisteredAsync(taskName)`
Android
iOS
Parameter| Type| Description  
---|---|---  
taskName| `string`| Name of the task.  
Determine whether the task is registered. Registered tasks are stored in a persistent storage and preserved between sessions.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
A promise which resolves to `true` if a task with the given name is registered, otherwise `false`.
### `TaskManager.unregisterAllTasksAsync()`
Android
iOS
Unregisters all tasks registered for the running app. You may want to call this when the user is signing out and you no longer need to track his location or run any other background tasks.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
A promise which fulfills as soon as all tasks are completely unregistered.
### `TaskManager.unregisterTaskAsync(taskName)`
Android
iOS
Parameter| Type| Description  
---|---|---  
taskName| `string`| Name of the task to unregister.  
Unregisters task from the app, so the app will not be receiving updates for that task anymore. _It is recommended to use methods specialized by modules that registered the task, eg.[`Location.stopLocationUpdatesAsync`](https://docs.expo.dev/versions/latest/sdk/location#expolocationstoplocationupdatesasynctaskname)._
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
A promise which fulfills as soon as the task is unregistered.
## Interfaces
### `TaskManagerError`
Android
iOS
Error object that can be received through [`TaskManagerTaskBody`](https://docs.expo.dev/versions/latest/sdk/task-manager/#taskmanagertaskbody) when the task fails.
Property| Type| Description  
---|---|---  
code| `string | number`  
message| `string`  
### `TaskManagerTask`
Android
iOS
Represents an already registered task.
Property| Type| Description  
---|---|---  
options| `any`| Provides `options` that the task was registered with.  
taskName| `string`| Name that the task is registered with.  
taskType| `string`| Type of the task which depends on how the task was registered.  
### `TaskManagerTaskBody`
Android
iOS
Represents the object that is passed to the task executor.
Property| Type| Description  
---|---|---  
data| An object of data passed to the task executor. Its properties depend on the type of the task.  
error| `null | `| Error object if the task failed or `null` otherwise.  
executionInfo| `TaskManagerTaskBodyExecutionInfo[](https://docs.expo.dev/versions/latest/sdk/task-manager/#taskmanagertaskbodyexecutioninfo)`| Additional details containing unique ID of task event and name of the task.  
### `TaskManagerTaskBodyExecutionInfo`
Android
iOS
Additional details about execution provided in `TaskManagerTaskBody`.
Property| Type| Description  
---|---|---  
appState(optional)| `'active' | 'background' | 'inactive'`| Only for: iOSState of the application.  
eventId| `string`| Unique ID of task event.  
taskName| `string`| Name of the task.  
## Types
### `TaskManagerTaskExecutor(body)`
Android
iOS
Type of task executor – a function that handles the task.
Parameter| Type  
---|---  
body| `TaskManagerTaskBody[](https://docs.expo.dev/versions/latest/sdk/task-manager/#taskmanagertaskbody)<T>`  
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<any>`

