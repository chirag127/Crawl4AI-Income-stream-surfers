---
url: https://reactnative.dev/docs/share
title: https://reactnative.dev/docs/share
date: 2025-05-10T21:42:10.499857
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/share#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
## Example[​](https://reactnative.dev/docs/share#example "Direct link to Example")
  * TypeScript
  * JavaScript


# Reference
## Methods[​](https://reactnative.dev/docs/share#methods "Direct link to Methods")
### `share()`[​](https://reactnative.dev/docs/share#share "Direct link to share")
tsx
```
staticshare(content:ShareContent, options?:ShareOptions);
```

Open a dialog to share text content.
In iOS, returns a Promise which will be invoked with an object containing `action` and `activityType`. If the user dismissed the dialog, the Promise will still be resolved with action being `Share.dismissedAction` and all the other keys being undefined. Note that some share options will not appear or work on the iOS simulator.
In Android, returns a Promise which will always be resolved with action being `Share.sharedAction`.
**Properties:**
Name| Type| Description  
---|---|---  
content Required| object| `message` - a message to share`url` - a URL to share iOS`title` - title of the message AndroidAt least one of `url` and `message` is required.  
options| object| `dialogTitle` Android`excludedActivityTypes` iOS`subject` - a subject to share via email iOS`tintColor` iOS`anchor` - the node to which the action sheet should be anchored (used for iPad) iOS  
## Properties[​](https://reactnative.dev/docs/share#properties "Direct link to Properties")
### `sharedAction`[​](https://reactnative.dev/docs/share#sharedaction "Direct link to sharedaction")
tsx
```
static sharedAction:'sharedAction';
```

The content was successfully shared.
### `dismissedAction`
iOS
[​](https://reactnative.dev/docs/share#dismissedaction-ios "Direct link to dismissedaction-ios")
tsx
```
static dismissedAction:'dismissedAction';
```

The dialog has been dismissed.
Is this page useful?
  * [Methods](https://reactnative.dev/docs/share#methods)
  * [Properties](https://reactnative.dev/docs/share#properties)
    * [`dismissedAction` iOS](https://reactnative.dev/docs/share#dismissedaction-ios)



