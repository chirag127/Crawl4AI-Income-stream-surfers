---
url: https://docs.expo.dev/versions/latest/sdk/background-task
title: https://docs.expo.dev/versions/latest/sdk/background-task
date: 2025-04-30T17:15:33.783175
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo BackgroundTask
A library that provides an API for running background tasks.
Android
iOS
Bundled version:
~0.1.4
> This library is currently in beta and subject to breaking changes.
`expo-background-task` provides an API to run deferrable background tasks in a way that optimizes battery and power consumption on the end user's device. This module uses the [`WorkManager`](https://developer.android.com/topic/libraries/architecture/workmanager) API on Android and the [`BGTaskScheduler`](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler) API on iOS to schedule tasks. It also uses the [`expo-task-manager`](https://docs.expo.dev/versions/latest/sdk/task-manager) Native API to run JavaScript tasks.
## Background tasks
A background task is a deferrable unit of work that is performed in the background, outside your app's lifecycle. This is useful for tasks that need to be executed when the app is inactive, such as syncing data with a server, fetching new content, or even checking if there are any [`expo-updates`](https://docs.expo.dev/versions/latest/sdk/updates).
### When are background tasks run?
The Expo Background Task API leverages each platform to execute tasks at the most optimal time for both the user and the device when the app is in the background.
This means that the task may not run immediately after it is scheduled, but it will run at some point in the future if the system decides so. You can specify a minimum interval in minutes for the task to run. The task will execute sometime after the interval has passed, provided the specified conditions are met.
A background task will only run if the battery has enough charge (or the device is plugged into power) and the network is available. Without these conditions, the task won't execute. The exact behavior will vary depending on the operating system.
### When will they be stopped?
Background tasks are managed by platform APIs and system constraints. Knowing when tasks stop helps plan their use effectively.
  * Background tasks are stopped if the user kills the app. Tasks resume when the app is restarted.
  * If the system stops the app or the device reboots, background tasks will resume, and the app will be restarted.


On Android, removing an app from the recent apps list doesn't completely stop it, whereas on iOS, swiping it away in the app switcher fully terminates it.
> On Android, behavior varies by device vendor. For example, some implementations treat removing an app from the recent apps list as killing it. Read more about these differences here: <https://dontkillmyapp.com>.
## Platform differences
### Android 
Android
On Android, the [`WorkManager`](https://developer.android.com/topic/libraries/architecture/workmanager) API allows specifying a minimum interval for a task to run (minimum 15 minutes). The task will execute sometime after the interval has passed, provided the specified conditions are met.
### iOS 
iOS
On iOS, the [`BGTaskScheduler`](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler) API decides the best time to launch your background task. The system will consider the battery level, the network availability, and the user's usage patterns to determine when to run the task. You can still specify a minimum interval for the task to run, but the system may choose to run the task at a later time.
## Known limitations
### iOS 
iOS
The [`Background Tasks`](https://developer.apple.com/documentation/backgroundtasks) API is unavailable on iOS simulators. It is only available when running on a physical device.
## Installation
Terminal
Copy
`- ``npx expo install expo-background-task`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Configuration 
iOS
To be able to run background tasks on iOS, you need to add the `processing` value to the `UIBackgroundModes` array in your app's Info.plist file. This is required for background fetch to work properly.
If you're using [CNG](https://docs.expo.dev/workflow/continuous-native-generation), the required `UIBackgroundModes` configuration will be applied automatically by prebuild.
Configure UIBackgroundModes manually on iOS
If you're not using Continuous Native Generation ([CNG](https://docs.expo.dev/workflow/continuous-native-generation)), then you'll need to add the following to your Info.plist file:
ios/project-name/Supporting/Info.plist
Copy
```
<key>UIBackgroundModes</key>
<array>
 <string>processing</string>
</array>

```

## Usage
Below is an example that demonstrates how to use `expo-background-task`.
App.tsx
Copy
```
import * as BackgroundTask from 'expo-background-task';
import * as TaskManager from 'expo-task-manager';
import { useEffect, useState } from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';
const BACKGROUND_TASK_IDENTIFIER = 'background-task';
// Register and create the task so that it is available also when the background task screen
// (a React component defined later in this example) is not visible.
// Note: This needs to be called in the global scope, not in a React component.
TaskManager.defineTask(BACKGROUND_TASK_IDENTIFIER, async () => {
 try {
  const now = Date.now();
  console.log(`Got background task call at date: ${new Date(now).toISOString()}`);
 } catch (error) {
  console.error('Failed to execute the background task:', error);
  return BackgroundTask.BackgroundTaskResult.Failed;
 }
 return BackgroundTask.BackgroundTaskResult.Success;
});
// 2. Register the task at some point in your app by providing the same name
// Note: This does NOT need to be in the global scope and CAN be used in your React components!
async function registerBackgroundTaskAsync() {
 return BackgroundTask.registerTaskAsync(BACKGROUND_TASK_IDENTIFIER);
}
// 3. (Optional) Unregister tasks by specifying the task name
// This will cancel any future background task calls that match the given name
// Note: This does NOT need to be in the global scope and CAN be used in your React components!
async function unregisterBackgroundTaskAsync() {
 return BackgroundTask.unregisterTaskAsync(BACKGROUND_TASK_IDENTIFIER);
}
export default function BackgroundTaskScreen() {
 const [isRegistered, setIsRegistered] = useState<boolean>(false);
 const [status, setStatus] = useState<BackgroundTask.BackgroundTaskStatus | null>(null);
 useEffect(() => {
  checkStatusAsync();
 }, []);
 const checkStatusAsync = async () => {
  const status = await BackgroundTask.getStatusAsync();
  setStatus(status);
 };
 const toggle = async () => {
  if (isRegistered) {
   await registerBackgroundTaskAsync();
  } else {
   await unregisterBackgroundTaskAsync();
  }
  setIsRegistered(!isRegistered);
 };
 return (
  <View style={styles.screen}><View style={styles.textContainer}><Text>
     Background Task Service Availability:{' '}<Text style={styles.boldText}>{status ? BackgroundTask.BackgroundTaskStatus[status] : null}</Text></Text></View><Button
    disabled={status === BackgroundTask.BackgroundTaskStatus.Restricted}
    title={isRegistered ? 'Cancel Background Task' : 'Schedule Background Task'}
    onPress={toggle}
   /><Button title="Check Background Task Status" onPress={checkStatusAsync} /></View>
 );
}
const styles = StyleSheet.create({
 screen: {
  flex: 1,
  justifyContent: 'center',
  alignItems: 'center',
 },
 textContainer: {
  margin: 10,
 },
 boldText: {
  fontWeight: 'bold',
 },
});

Show More

```

## Multiple background tasks
Since the Background Tasks API on iOS and the WorkManager API on Android limit the number of tasks that can be scheduled for a single app, Expo Background Task uses a single worker on both platforms. While you can define multiple JavaScript background tasks, they will all run through this single worker.
The last registered background task determines the minimum interval for execution.
## API
```
import * as BackgroundTask from 'expo-background-task';

```

## Methods
### `BackgroundTask.getStatusAsync()`
Android
iOS
Returns the status for the Background Task API. On web, it always returns `BackgroundTaskStatus.Restricted`, while on native platforms it returns `BackgroundTaskStatus.Available`.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<BackgroundTaskStatus[](https://docs.expo.dev/versions/latest/sdk/background-task/#backgroundtaskstatus)>`
A BackgroundTaskStatus enum value or `null` if not available.
### `BackgroundTask.registerTaskAsync(taskName, options)`
Android
iOS
Parameter| Type| Description  
---|---|---  
taskName| `string`| Name of the task to register. The task needs to be defined first - see [`TaskManager.defineTask`](https://docs.expo.dev/versions/latest/sdk/task-manager#taskmanagerdefinetasktaskname-taskexecutor) for more details.  
options(optional)| `BackgroundTaskOptions[](https://docs.expo.dev/versions/latest/sdk/background-task/#backgroundtaskoptions)`| An object containing the background task options.Default:`{}`  
Registers a background task with the given name. Registered tasks are saved in persistent storage and restored once the app is initialized.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
Example
```
import * as TaskManager from 'expo-task-manager';
// Register the task outside of the component
TaskManager.defineTask(BACKGROUND_TASK_IDENTIFIER, () => {
 try {
  await AsyncStorage.setItem(LAST_TASK_DATE_KEY, Date.now().toString());
 } catch (error) {
  console.error('Failed to save the last fetch date', error);
  return BackgroundTaskResult.Failed;
 }
 return BackgroundTaskResult.Success;
});

```

You can now use the `registerTaskAsync` function to register the task:
```
BackgroundTask.registerTaskAsync(BACKGROUND_TASK_IDENTIFIER, {});

```

### `BackgroundTask.unregisterTaskAsync(taskName)`
Android
iOS
Parameter| Type| Description  
---|---|---  
taskName| `string`| Name of the task to unregister.  
Unregisters a background task, so the application will no longer be executing this task.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
A promise which fulfils when the task is fully unregistered.
## Types
### `BackgroundTaskOptions`
Android
iOS
Options for registering a background task
Property| Type| Description  
---|---|---  
minimumInterval(optional)| `number`| Only for: AndroidInexact interval in minutes between subsequent repeats of the background tasks. The final interval may differ from the specified one to minimize wakeups and battery usage.
  * Defaults to once every 12 hours (The minimum interval is 15 minutes)
  * On iOS, the system determines the interval for background task execution, but will wait until the specified minimum interval has elapsed before starting a task.

  
## Enums
### `BackgroundTaskResult`
Android
iOS
Return value for background tasks.
#### `Success`
`BackgroundTaskResult.Success ＝ 1`
The task finished successfully.
#### `Failed`
`BackgroundTaskResult.Failed ＝ 2`
The task failed.
### `BackgroundTaskStatus`
Android
iOS
Availability status for background tasks
#### `Restricted`
`BackgroundTaskStatus.Restricted ＝ 1`
Background tasks are unavailable.
#### `Available`
`BackgroundTaskStatus.Available ＝ 2`
Background tasks are available for the app.

