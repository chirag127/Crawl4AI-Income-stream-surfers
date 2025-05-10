---
url: https://reactnative.dev/docs/systrace
title: https://reactnative.dev/docs/systrace
date: 2025-05-10T21:42:10.506911
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/systrace#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
`Systrace` is a standard Android marker-based profiling tool (and is installed when you install the Android platform-tools package). Profiled code blocks are surrounded by start/end markers which are then visualized in a colorful chart format. Both the Android SDK and React Native framework provide standard markers that you can visualize.
## Example[​](https://reactnative.dev/docs/systrace#example "Direct link to Example")
`Systrace` allows you to mark JavaScript (JS) events with a tag and an integer value. Capture the non-Timed JS events in EasyProfiler.
# Reference
## Methods[​](https://reactnative.dev/docs/systrace#methods "Direct link to Methods")
### `isEnabled()`[​](https://reactnative.dev/docs/systrace#isenabled "Direct link to isenabled")
tsx
```
staticisEnabled():boolean;
```

### `beginEvent()`[​](https://reactnative.dev/docs/systrace#beginevent "Direct link to beginevent")
tsx
```
staticbeginEvent(eventName:string|(()=>string), args?:EventArgs);
```

beginEvent/endEvent for starting and then ending a profile within the same call stack frame.
### `endEvent()`[​](https://reactnative.dev/docs/systrace#endevent "Direct link to endevent")
tsx
```
staticendEvent(args?:EventArgs);
```

### `beginAsyncEvent()`[​](https://reactnative.dev/docs/systrace#beginasyncevent "Direct link to beginasyncevent")
tsx
```
staticbeginAsyncEvent( eventName:string|(()=>string), args?:EventArgs,):number;
```

beginAsyncEvent/endAsyncEvent for starting and then ending a profile where the end can either occur on another thread or out of the current stack frame, eg await the returned cookie variable should be used as input into the endAsyncEvent call to end the profile.
### `endAsyncEvent()`[​](https://reactnative.dev/docs/systrace#endasyncevent "Direct link to endasyncevent")
tsx
```
staticendAsyncEvent( eventName:EventName, cookie:number, args?:EventArgs,
```

### `counterEvent()`[​](https://reactnative.dev/docs/systrace#counterevent "Direct link to counterevent")
tsx
```
staticcounterEvent(eventName:string|(()=>string), value:number);
```

Register the value to the profileName on the systrace timeline.
Is this page useful?
  * [Methods](https://reactnative.dev/docs/systrace#methods)
    * [`beginAsyncEvent()`](https://reactnative.dev/docs/systrace#beginasyncevent)
    * [`endAsyncEvent()`](https://reactnative.dev/docs/systrace#endasyncevent)



