---
url: https://docs.expo.dev/versions/latest/sdk/system-ui
title: https://docs.expo.dev/versions/latest/sdk/system-ui
date: 2025-04-30T17:17:41.684053
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo SystemUI
A library that allows interacting with system UI elements.
Android
iOS
Web
Bundled version:
~4.0.9
`expo-system-ui` enables you to interact with UI elements that fall outside of the React tree. Specifically the root view background color, and locking the user interface style globally on Android.
## Installation
Terminal
Copy
`- ``npx expo install expo-system-ui`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## API
```
import * as SystemUI from 'expo-system-ui';

```

## Methods
### `SystemUI.getBackgroundColorAsync()`
Android
iOS
Web
Gets the root view background color.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<null>`
Current root view background color in hex format. Returns `null` if the background color is not set.
Example
```
const color = await SystemUI.getBackgroundColorAsync();

```

### `SystemUI.setBackgroundColorAsync(color)`
Android
iOS
Web
Parameter| Type| Description  
---|---|---  
color| `null | `| Any valid [CSS 3 (SVG) color](http://www.w3.org/TR/css3-color/#svg-color).  
Changes the root view background color. Call this function in the root file outside of you component.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
Example
```
SystemUI.setBackgroundColorAsync("black");

```


