---
url: https://reactnative.dev/docs/settings
title: https://reactnative.dev/docs/settings
date: 2025-05-10T21:42:04.849578
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/settings#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
`Settings` serves as a wrapper for [`NSUserDefaults`](https://developer.apple.com/documentation/foundation/nsuserdefaults), a persistent key-value store available only on iOS.
## Example[​](https://reactnative.dev/docs/settings#example "Direct link to Example")
# Reference
## Methods[​](https://reactnative.dev/docs/settings#methods "Direct link to Methods")
### `clearWatch()`[​](https://reactnative.dev/docs/settings#clearwatch "Direct link to clearwatch")
tsx
```
staticclearWatch(watchId:number);
```

`watchId` is the number returned by `watchKeys()` when the subscription was originally configured.
### `get()`[​](https://reactnative.dev/docs/settings#get "Direct link to get")
tsx
```
staticget(key:string):any;
```

Get the current value for a given `key` in `NSUserDefaults`.
### `set()`[​](https://reactnative.dev/docs/settings#set "Direct link to set")
tsx
```
staticset(settings:Record<string,any>);
```

Set one or more values in `NSUserDefaults`.
### `watchKeys()`[​](https://reactnative.dev/docs/settings#watchkeys "Direct link to watchkeys")
tsx
```
staticwatchKeys(keys:string| array<string>,callback:()=>void):number;
```

Subscribe to be notified when the value for any of the keys specified by the `keys` parameter has been changed in `NSUserDefaults`. Returns a `watchId` number that may be used with `clearWatch()` to unsubscribe.
> **Note:** `watchKeys()` by design ignores internal `set()` calls and fires callback only on changes preformed outside of React Native code.
Is this page useful?
  * [Methods](https://reactnative.dev/docs/settings#methods)



