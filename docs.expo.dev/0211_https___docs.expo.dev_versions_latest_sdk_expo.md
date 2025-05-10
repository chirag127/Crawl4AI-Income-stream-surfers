---
url: https://docs.expo.dev/versions/latest/sdk/expo
title: https://docs.expo.dev/versions/latest/sdk/expo
date: 2025-04-30T17:16:17.702023
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo
Set of common methods and types for Expo and related packages.
Android
iOS
tvOS
Web
## Installation
Terminal
Copy
`- ``npx expo install expo`
## API
```
import * as Expo from 'expo';

```

### `expo/fetch` API
`expo/fetch` provides a [WinterCG-compliant Fetch API](https://fetch.spec.wintercg.org/) that works consistently across web and mobile environments, ensuring a standardized and cross-platform fetch experience within Expo applications.
Streaming fetch
Copy
```
import { fetch } from 'expo/fetch';
const resp = await fetch('https://httpbin.org/drip?numbytes=512&duration=2', {
 headers: { Accept: 'text/event-stream' },
});
const reader = resp.body.getReader();
const chunks = [];
while (true) {
 const { done, value } = await reader.read();
 if (done) {
  break;
 }
 chunks.push(value);
}
const buffer = new Uint8Array(chunks.reduce((acc, chunk) => acc + chunk.length, 0));
console.log(buffer.length); // 512

```

## Constants
### `SharedRef`
Android
iOS
tvOS
Web
Type: `SharedRefType`
## Hooks
### `useEvent(eventEmitter, eventName, initialValue)`
Android
iOS
tvOS
Web
Parameter| Type| Description  
---|---|---  
eventEmitter| `EventEmitter[](https://docs.expo.dev/versions/v52.0.0/sdk/expo#eventemitter)<TEventsMap>`| An object that emits events. For example, a native module or shared object or an instance of [`EventEmitter`](https://docs.expo.dev/versions/latest/sdk/expo/#eventemitter).  
eventName| `TEventName`| Name of the event to listen to.  
initialValue(optional)| `null | TInitialValue`| An event parameter to use until the event is called for the first time.Default:`null`  
React hook that listens to events emitted by the given object. The returned value is an event parameter that gets updated whenever a new event is dispatched.
Returns:
`InferEventParameter<TEventListener, TInitialValue>`
A parameter of the event listener.
Example
```
import { useEvent } from 'expo';
import { VideoPlayer } from 'expo-video';
export function PlayerStatus({ videoPlayer }: { videoPlayer: VideoPlayer }) {
 const { status } = useEvent(videoPlayer, 'statusChange', { status: videoPlayer.status });
 return <Text>{`Player status: ${status}`}</Text>;
}

```

### `useEventListener(eventEmitter, eventName, listener)`
Android
iOS
tvOS
Web
Parameter| Type| Description  
---|---|---  
eventEmitter| `EventEmitter[](https://docs.expo.dev/versions/v52.0.0/sdk/expo#eventemitter)<TEventsMap>`| An object that emits events. For example, a native module or shared object or an instance of [`EventEmitter`](https://docs.expo.dev/versions/latest/sdk/expo/#eventemitter).  
eventName| `TEventName`| Name of the event to listen to.  
listener| `TEventListener`| A function to call when the event is dispatched.  
React hook that listens to events emitted by the given object and calls the listener function whenever a new event is dispatched. The event listener is automatically added during the first render and removed when the component unmounts.
Returns:
`void`
Example
```
import { useEventListener } from 'expo';
import { useVideoPlayer, VideoView } from 'expo-video';
export function VideoPlayerView() {
 const player = useVideoPlayer(videoSource);
 useEventListener(player, 'playingChange', ({ isPlaying }) => {
  console.log('Player is playing:', isPlaying);
 });
 return <VideoView player={player} />;
}

```

## Classes
### `EventEmitter`
Android
iOS
tvOS
Web
A class that provides a consistent API for emitting and listening to events. It shares many concepts with other emitter APIs, such as Node's EventEmitter and `fbemitter`. When the event is emitted, all of the functions attached to that specific event are called _synchronously_. Any values returned by the called listeners are _ignored_ and discarded. Its implementation is written in C++ and common for all the platforms.
EventEmitter Methods
### `addListener(eventName, listener)`
Android
iOS
tvOS
Web
Parameter| Type  
---|---  
eventName| `EventName`  
listener| `TEventsMap[EventName]`  
Adds a listener for the given event name.
Returns:
`EventSubscription`
### `emit(eventName, ...args)`
Android
iOS
tvOS
Web
Parameter| Type  
---|---  
eventName| `EventName`  
...args| `Parameters<TEventsMap[EventName]>`  
Synchronously calls all of the listeners attached to that specific event. The event can include any number of arguments that will be passed to the listeners.
Returns:
`void`
### `listenerCount(eventName)`
Android
iOS
tvOS
Web
Parameter| Type  
---|---  
eventName| `EventName`  
Returns a number of listeners added to the given event.
Returns:
`number`
### `removeAllListeners(eventName)`
Android
iOS
tvOS
Web
Parameter| Type  
---|---  
eventName| `keyof undefined`  
Removes all listeners for the given event name.
Returns:
`void`
### `removeListener(eventName, listener)`
Android
iOS
tvOS
Web
Parameter| Type  
---|---  
eventName| `EventName`  
listener| `TEventsMap[EventName]`  
Removes a listener for the given event name.
Returns:
`void`
### `startObserving(eventName)`
Android
iOS
tvOS
Web
Parameter| Type  
---|---  
eventName| `EventName`  
Function that is automatically invoked when the first listener for an event with the given name is added. Override it in a subclass to perform some additional setup once the event started being observed.
Returns:
`void`
### `stopObserving(eventName)`
Android
iOS
tvOS
Web
Parameter| Type  
---|---  
eventName| `EventName`  
Function that is automatically invoked when the last listener for an event with the given name is removed. Override it in a subclass to perform some additional cleanup once the event is no longer observed.
Returns:
`void`
### `NativeModule`
Android
iOS
tvOS
Web
Type: Class extends `EventEmitter[](https://docs.expo.dev/versions/v52.0.0/sdk/expo#eventemitter)<TEventsMap>`
A class for all native modules. Extends the [EventEmitter](https://docs.expo.dev/versions/latest/sdk/expo/#eventemitter) class.
### `SharedObject`
Android
iOS
tvOS
Web
Type: Class extends `EventEmitter[](https://docs.expo.dev/versions/v52.0.0/sdk/expo#eventemitter)<TEventsMap>` implements `EventEmitter[](https://docs.expo.dev/versions/v52.0.0/sdk/expo#eventemitter)<TEventsMap>`
Base class for all shared objects that extends the [EventEmitter](https://docs.expo.dev/versions/latest/sdk/expo/#eventemitter) class. The implementation is written in C++, installed through JSI and common for mobile platforms.
SharedObject Methods
### `release()`
Android
iOS
tvOS
Web
A function that detaches the JS and native objects to let the native object deallocate before the JS object gets deallocated by the JS garbage collector. Any subsequent calls to native functions of the object will throw an error as it is no longer associated with its native counterpart.
In most cases, you should never need to use this function, except some specific performance-critical cases when manual memory management makes sense and the native object is known to exclusively retain some native memory (such as binary data or image bitmap). Before calling this function, you should ensure that nothing else will use this object later on. Shared objects created by React hooks are usually automatically released in the effect's cleanup phase, for example: `useVideoPlayer()` from `expo-video` and `useImage()` from `expo-image`.
Returns:
`void`
### `SharedRef`
Android
iOS
tvOS
Web
Type: Class extends `SharedObject[](https://docs.expo.dev/versions/v52.0.0/sdk/expo#sharedobject)<TEventsMap>` implements `SharedObject[](https://docs.expo.dev/versions/v52.0.0/sdk/expo#sharedobject)<TEventsMap>`
A [SharedObject](https://docs.expo.dev/versions/latest/sdk/expo/#sharedobject) that holds a reference to any native object. Allows passing references to native instances among different independent libraries.
For instance, `ImageRef` from `expo-image` references a [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) on Android and an [UIImage](https://developer.apple.com/documentation/uikit/uiimage) on iOS. Since both types are common on these platforms, different native modules can use them without depending on each other. In particular, this enables the `expo-image-manipulator` to pass the resulted image directly to the image view from `expo-image` without any additional writes and reads from the file system.
SharedRef Properties
### `nativeRefType`
Android
iOS
tvOS
Web
Type: `string`
The type of the native reference.
## Methods
### `isRunningInExpoGo()`
Android
iOS
tvOS
Web
Returns a boolean value whether the app is running in Expo Go.
Returns:
`boolean`
### `registerRootComponent(component)`
Android
iOS
tvOS
Web
Parameter| Type| Description  
---|---|---  
component| `ComponentType<P>`| The React component class that renders the rest of your app.  
Sets the initial React component to render natively in the app's root React Native view on Android, iOS, tvOS and the web.
This method does the following:
  * Invokes React Native's `AppRegistry.registerComponent`.
  * Invokes React Native web's `AppRegistry.runApplication` on web to render to the root `index.html` file.
  * Polyfills the `process.nextTick` function globally.


This method also adds the following dev-only features that are removed in production bundles.
  * Adds the Fast Refresh and bundle splitting indicator to the app.
  * Asserts if the `expo-updates` package is misconfigured.
  * Asserts if `react-native` is not aliased to `react-native-web` when running in the browser.


Returns:
`void`
### `registerWebModule(moduleImplementation)`
Android
iOS
tvOS
Web
Parameter| Type| Description  
---|---|---  
moduleImplementation| `ModuleType`| – a class that extends `NativeModule`. The class is registered under `globalThis.expo.modules[className]`.  
Registers a web module.
Returns:
`ModuleType`
A singleton instance of the class passed into arguments.
### `reloadAppAsync(reason)`
Android
iOS
tvOS
Web
Parameter| Type| Description  
---|---|---  
reason(optional)| `string`| The reason for reloading the app. This is used only for some platforms.  
Reloads the app. This method works for both release and debug builds.
Unlike [`Updates.reloadAsync()`](https://docs.expo.dev/versions/latest/sdk/updates#updatesreloadasync), this function does not use a new update even if one is available. It only reloads the app using the same JavaScript bundle that is currently running.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `requireNativeModule(moduleName)`
Android
iOS
tvOS
Web
Parameter| Type| Description  
---|---|---  
moduleName| `string`| Name of the requested native module.  
Imports the native module registered with given name. In the first place it tries to load the module installed through the JSI host object and then falls back to the bridge proxy module. Notice that the modules loaded from the proxy may not support some features like synchronous functions.
Returns:
`ModuleType`
Object representing the native module.
### `requireNativeView(viewName)`
Android
iOS
tvOS
Web
Parameter| Type  
---|---  
viewName| `string`  
A drop-in replacement for `requireNativeComponent`.
Returns:
`React.ComponentType<P>`
### `requireOptionalNativeModule(moduleName)`
Android
iOS
tvOS
Web
Parameter| Type| Description  
---|---|---  
moduleName| `string`| Name of the requested native module.  
Imports the native module registered with the given name. The same as `requireNativeModule`, but returns `null` when the module cannot be found instead of throwing an error.
Returns:
`ModuleType | null`
Object representing the native module or `null` when it cannot be found.
## Event Subscriptions
### `useEventListener(eventEmitter, eventName, listener)`
Android
iOS
tvOS
Web
Parameter| Type| Description  
---|---|---  
eventEmitter| `EventEmitter[](https://docs.expo.dev/versions/v52.0.0/sdk/expo#eventemitter)<TEventsMap>`| An object that emits events. For example, a native module or shared object or an instance of [`EventEmitter`](https://docs.expo.dev/versions/latest/sdk/expo/#eventemitter).  
eventName| `TEventName`| Name of the event to listen to.  
listener| `TEventListener`| A function to call when the event is dispatched.  
React hook that listens to events emitted by the given object and calls the listener function whenever a new event is dispatched. The event listener is automatically added during the first render and removed when the component unmounts.
Returns:
`void`
Example
```
import { useEventListener } from 'expo';
import { useVideoPlayer, VideoView } from 'expo-video';
export function VideoPlayerView() {
 const player = useVideoPlayer(videoSource);
 useEventListener(player, 'playingChange', ({ isPlaying }) => {
  console.log('Player is playing:', isPlaying);
 });
 return <VideoView player={player} />;
}

```

## Common questions
### What if I want to name my main app file something other than App.js or app/_layout.tsx?
For projects that do not use [Expo Router](https://docs.expo.dev/router/introduction), you can set the `"main"` in package.json to any file within your project. If you do this, then you need to use `registerRootComponent`. The `export default` will not make this component the root for the app if you are using a custom entry file.
For example, let's say you want to make src/main.jsx the entry file for your app — maybe you don't like having JavaScript files in the project root. First, set this in package.json:
package.json
Copy
```
{
 "main": "src/main.jsx"
}

```

Then, in src/main.jsx, make sure you call `registerRootComponent` and pass in the component you want to render at the root of the app:
src/main.jsx
Copy
```
import { registerRootComponent } from 'expo';
import { View } from 'react-native';
function App() {
 return <View />;
}
registerRootComponent(App);

```

For projects that use [Expo Router](https://docs.expo.dev/router/introduction), you can create a custom entry point by following these steps from [Expo Router's installation guide](https://docs.expo.dev/router/installation#custom-entry-point-to-initialize-and-load). To use the top-level src directory in your Expo Router project, see [src directory reference](https://docs.expo.dev/router/reference/src-directory) for more information.

