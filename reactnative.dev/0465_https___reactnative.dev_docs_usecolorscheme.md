---
url: https://reactnative.dev/docs/usecolorscheme
title: https://reactnative.dev/docs/usecolorscheme
date: 2025-05-10T21:42:45.376559
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/usecolorscheme#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
tsx
```
import{useColorScheme}from'react-native';
```

The `useColorScheme` React hook provides and subscribes to color scheme updates from the [`Appearance`](https://reactnative.dev/docs/appearance) module. The return value indicates the current user preferred color scheme. The value may be updated later, either through direct user action (e.g. theme selection in device settings) or on a schedule (e.g. light and dark themes that follow the day/night cycle).
### Supported color schemes[​](https://reactnative.dev/docs/usecolorscheme#supported-color-schemes "Direct link to Supported color schemes")
  * `"light"`: The user prefers a light color theme.
  * `"dark"`: The user prefers a dark color theme.
  * `null`: The user has not indicated a preferred color theme.


## Example[​](https://reactnative.dev/docs/usecolorscheme#example "Direct link to Example")
You can find a complete example that demonstrates the use of this hook alongside a React context to add support for light and dark themes to your application in [`AppearanceExample.js`](https://github.com/facebook/react-native/blob/main/packages/rn-tester/js/examples/Appearance/AppearanceExample.js).
Is this page useful?
  * [Supported color schemes](https://reactnative.dev/docs/usecolorscheme#supported-color-schemes)



