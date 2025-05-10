---
url: https://reactnative.dev/docs/appregistry
title: https://reactnative.dev/docs/appregistry
date: 2025-05-10T21:39:29.178641
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/appregistry#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
### Project with Native Code Required
If you are using the managed Expo workflow there is only ever one entry component registered with `AppRegistry` and it is handled automatically (or through [registerRootComponent](https://docs.expo.dev/versions/latest/sdk/register-root-component/)). You do not need to use this API.
`AppRegistry` is the JS entry point to running all React Native apps. App root components should register themselves with `AppRegistry.registerComponent`, then the native system can load the bundle for the app and then actually run the app when it's ready by invoking `AppRegistry.runApplication`.
tsx
```
import{Text,AppRegistry}from'react-native';constApp=()=>(<View><Text>App1</Text></View>AppRegistry.registerComponent('Appname',()=>App);
```

To "stop" an application when a view should be destroyed, call `AppRegistry.unmountApplicationComponentAtRootTag` with the tag that was passed into `runApplication`. These should always be used as a pair.
`AppRegistry` should be required early in the `require` sequence to make sure the JS execution environment is setup before other modules are required.
# Reference
## Methods[​](https://reactnative.dev/docs/appregistry#methods "Direct link to Methods")
### `getAppKeys()`[​](https://reactnative.dev/docs/appregistry#getappkeys "Direct link to getappkeys")
tsx
```
staticgetAppKeys():string[];
```

Returns an array of strings.
### `getRegistry()`[​](https://reactnative.dev/docs/appregistry#getregistry "Direct link to getregistry")
tsx
```
staticgetRegistry():{sections:string[]; runnables:Runnable[]};
```

Returns a [Registry](https://reactnative.dev/docs/appregistry#registry) object.
### `getRunnable()`[​](https://reactnative.dev/docs/appregistry#getrunnable "Direct link to getrunnable")
tsx
```
staticgetRunnable(appKey:string)::Runnable|undefined;
```

Returns a [Runnable](https://reactnative.dev/docs/appregistry#runnable) object.
**Parameters:**
Name| Type  
---|---  
appKey Required| string  
### `getSectionKeys()`[​](https://reactnative.dev/docs/appregistry#getsectionkeys "Direct link to getsectionkeys")
tsx
```
staticgetSectionKeys():string[];
```

Returns an array of strings.
### `getSections()`[​](https://reactnative.dev/docs/appregistry#getsections "Direct link to getsections")
tsx
```
staticgetSections():Record<string,Runnable>;
```

Returns a [Runnables](https://reactnative.dev/docs/appregistry#runnables) object.
### `registerCancellableHeadlessTask()`[​](https://reactnative.dev/docs/appregistry#registercancellableheadlesstask "Direct link to registercancellableheadlesstask")
tsx
```
staticregisterCancellableHeadlessTask( taskKey:string, taskProvider:TaskProvider, taskCancelProvider:TaskCancelProvider,
```

Register a headless task which can be cancelled. A headless task is a bit of code that runs without a UI.
**Parameters:**
Name| Type| Description  
---|---|---  
taskKeyRequired| string| The native id for this task instance that was used when startHeadlessTask was called.  
taskProviderRequired| A promise returning function that takes some data passed from the native side as the only argument. When the promise is resolved or rejected the native side is notified of this event and it may decide to destroy the JS context.  
taskCancelProviderRequired| [TaskCancelProvider](https://reactnative.dev/docs/appregistry#taskcancelprovider)| a void returning function that takes no arguments; when a cancellation is requested, the function being executed by taskProvider should wrap up and return ASAP.  
### `registerComponent()`[​](https://reactnative.dev/docs/appregistry#registercomponent "Direct link to registercomponent")
tsx
```
staticregisterComponent( appKey:string, getComponentFunc:ComponentProvider, section?:boolean,):string;
```

**Parameters:**
Name| Type  
---|---  
appKey Required| string  
componentProvider Required| ComponentProvider  
section| boolean  
### `registerConfig()`[​](https://reactnative.dev/docs/appregistry#registerconfig "Direct link to registerconfig")
tsx
```
staticregisterConfig(config:AppConfig[]);
```

**Parameters:**
Name| Type  
---|---  
config Required  
### `registerHeadlessTask()`[​](https://reactnative.dev/docs/appregistry#registerheadlesstask "Direct link to registerheadlesstask")
tsx
```
staticregisterHeadlessTask( taskKey:string, taskProvider:TaskProvider,
```

Register a headless task. A headless task is a bit of code that runs without a UI.
This is a way to run tasks in JavaScript while your app is in the background. It can be used, for example, to sync fresh data, handle push notifications, or play music.
**Parameters:**
Name| Type| Description  
---|---|---  
taskKey Required| string| The native id for this task instance that was used when startHeadlessTask was called.  
taskProvider Required| A promise returning function that takes some data passed from the native side as the only argument. When the promise is resolved or rejected the native side is notified of this event and it may decide to destroy the JS context.  
### `registerRunnable()`[​](https://reactnative.dev/docs/appregistry#registerrunnable "Direct link to registerrunnable")
tsx
```
staticregisterRunnable(appKey:string, func:Runnable):string;
```

**Parameters:**
Name| Type  
---|---  
appKey Required| string  
run Required| function  
### `registerSection()`[​](https://reactnative.dev/docs/appregistry#registersection "Direct link to registersection")
tsx
```
staticregisterSection( appKey:string, component:ComponentProvider,
```

**Parameters:**
Name| Type  
---|---  
appKey Required| string  
component Required| ComponentProvider  
### `runApplication()`[​](https://reactnative.dev/docs/appregistry#runapplication "Direct link to runapplication")
tsx
```
staticrunApplication(appKey:string, appParameters:any):void;
```

Loads the JavaScript bundle and runs the app.
**Parameters:**
Name| Type  
---|---  
appKey Required| string  
appParameters Required| any  
### `setComponentProviderInstrumentationHook()`[​](https://reactnative.dev/docs/appregistry#setcomponentproviderinstrumentationhook "Direct link to setcomponentproviderinstrumentationhook")
tsx
```
staticsetComponentProviderInstrumentationHook( hook:ComponentProviderInstrumentationHook,
```

**Parameters:**
Name| Type  
---|---  
hook Required| function  
A valid `hook` function accepts the following as arguments:
Name| Type  
---|---  
component Required| ComponentProvider  
scopedPerformanceLogger Required| IPerformanceLogger  
The function must also return a React Component.
### `setWrapperComponentProvider()`[​](https://reactnative.dev/docs/appregistry#setwrappercomponentprovider "Direct link to setwrappercomponentprovider")
tsx
```
staticsetWrapperComponentProvider( provider:WrapperComponentProvider,
```

**Parameters:**
Name| Type  
---|---  
provider Required| ComponentProvider  
### `startHeadlessTask()`[​](https://reactnative.dev/docs/appregistry#startheadlesstask "Direct link to startheadlesstask")
tsx
```
staticstartHeadlessTask( taskId:number, taskKey:string, data:any,
```

Only called from native code. Starts a headless task.
**Parameters:**
Name| Type| Description  
---|---|---  
taskId Required| number| The native id for this task instance to keep track of its execution.  
taskKey Required| string| The key for the task to start.  
data Required| any| The data to pass to the task.  
### `unmountApplicationComponentAtRootTag()`[​](https://reactnative.dev/docs/appregistry#unmountapplicationcomponentatroottag "Direct link to unmountapplicationcomponentatroottag")
tsx
```
staticunmountApplicationComponentAtRootTag(rootTag:number);
```

Stops an application when a view should be destroyed.
**Parameters:**
Name| Type  
---|---  
rootTag Required| number  
## Type Definitions[​](https://reactnative.dev/docs/appregistry#type-definitions "Direct link to Type Definitions")
### AppConfig[​](https://reactnative.dev/docs/appregistry#appconfig "Direct link to AppConfig")
Application configuration for the `registerConfig` method.
Type  
---  
object  
**Properties:**
Name| Type  
---|---  
appKey Required| string  
component| ComponentProvider  
run| function  
section| boolean  
> **Note:** Every config is expected to set either `component` or `run` function.
### Registry[​](https://reactnative.dev/docs/appregistry#registry "Direct link to Registry")
Type  
---  
object  
**Properties:**
Name| Type  
---|---  
runnables| array of [Runnables](https://reactnative.dev/docs/appregistry#runnable)  
sections| array of strings  
### Runnable[​](https://reactnative.dev/docs/appregistry#runnable "Direct link to Runnable")
Type  
---  
object  
**Properties:**
Name| Type  
---|---  
component| ComponentProvider  
run| function  
### Runnables[​](https://reactnative.dev/docs/appregistry#runnables "Direct link to Runnables")
An object with key of `appKey` and value of type of [`Runnable`](https://reactnative.dev/docs/appregistry#runnable).
Type  
---  
object  
### Task[​](https://reactnative.dev/docs/appregistry#task "Direct link to Task")
A `Task` is a function that accepts any data as argument and returns a Promise that resolves to `undefined`.
Type  
---  
function  
### TaskCanceller[​](https://reactnative.dev/docs/appregistry#taskcanceller "Direct link to TaskCanceller")
A `TaskCanceller` is a function that accepts no argument and returns void.
Type  
---  
function  
### TaskCancelProvider[​](https://reactnative.dev/docs/appregistry#taskcancelprovider "Direct link to TaskCancelProvider")
A valid `TaskCancelProvider` is a function that returns a [`TaskCanceller`](https://reactnative.dev/docs/appregistry#taskcanceller).
Type  
---  
function  
### TaskProvider[​](https://reactnative.dev/docs/appregistry#taskprovider "Direct link to TaskProvider")
A valid `TaskProvider` is a function that returns a [`Task`](https://reactnative.dev/docs/appregistry#task).
Type  
---  
function  
Is this page useful?
  * [Methods](https://reactnative.dev/docs/appregistry#methods)
    * [`getSectionKeys()`](https://reactnative.dev/docs/appregistry#getsectionkeys)
    * [`registerCancellableHeadlessTask()`](https://reactnative.dev/docs/appregistry#registercancellableheadlesstask)
    * [`registerComponent()`](https://reactnative.dev/docs/appregistry#registercomponent)
    * [`registerConfig()`](https://reactnative.dev/docs/appregistry#registerconfig)
    * [`registerHeadlessTask()`](https://reactnative.dev/docs/appregistry#registerheadlesstask)
    * [`registerRunnable()`](https://reactnative.dev/docs/appregistry#registerrunnable)
    * [`registerSection()`](https://reactnative.dev/docs/appregistry#registersection)
    * [`runApplication()`](https://reactnative.dev/docs/appregistry#runapplication)
    * [`setComponentProviderInstrumentationHook()`](https://reactnative.dev/docs/appregistry#setcomponentproviderinstrumentationhook)
    * [`setWrapperComponentProvider()`](https://reactnative.dev/docs/appregistry#setwrappercomponentprovider)
    * [`startHeadlessTask()`](https://reactnative.dev/docs/appregistry#startheadlesstask)
    * [`unmountApplicationComponentAtRootTag()`](https://reactnative.dev/docs/appregistry#unmountapplicationcomponentatroottag)
  * [Type Definitions](https://reactnative.dev/docs/appregistry#type-definitions)
    * [TaskCanceller](https://reactnative.dev/docs/appregistry#taskcanceller)
    * [TaskCancelProvider](https://reactnative.dev/docs/appregistry#taskcancelprovider)



