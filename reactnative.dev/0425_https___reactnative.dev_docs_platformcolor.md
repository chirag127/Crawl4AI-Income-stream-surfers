---
url: https://reactnative.dev/docs/platformcolor
title: https://reactnative.dev/docs/platformcolor
date: 2025-05-10T21:41:45.264864
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/platformcolor#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
js
```
PlatformColor(color1,[color2,...colorN]);
```

You can use the `PlatformColor` function to access native colors on the target platform by supplying the native color’s corresponding string value. You pass a string to the `PlatformColor` function and, provided it exists on that platform, it will return the corresponding native color, which you can apply in any part of your application.
If you pass more than one string value to the `PlatformColor` function, it will treat the first value as the default and the rest as fallback.
js
```
PlatformColor('bogusName','linkColor');
```

Since native colors can be sensitive to themes and/or high contrast, this platform specific logic also translates inside your components.
### Supported colors[​](https://reactnative.dev/docs/platformcolor#supported-colors "Direct link to Supported colors")
For a full list of the types of system colors supported, see:
  * Android: 
    * [R.attr](https://developer.android.com/reference/android/R.attr) - `?attr` prefix
    * [R.color](https://developer.android.com/reference/android/R.color) - `@android:color` prefix
  * iOS (Objective-C and Swift notations): 
    * [UIColor Standard Colors](https://developer.apple.com/documentation/uikit/uicolor/standard_colors)
    * [UIColor UI Element Colors](https://developer.apple.com/documentation/uikit/uicolor/ui_element_colors)


#### Developer notes[​](https://reactnative.dev/docs/platformcolor#developer-notes "Direct link to Developer notes")
  * Web


> If you’re familiar with design systems, another way of thinking about this is that `PlatformColor` lets you tap into the local design system's color tokens so your app can blend right in!
## Example[​](https://reactnative.dev/docs/platformcolor#example "Direct link to Example")
The string value provided to the `PlatformColor` function must match the string as it exists on the native platform where the app is running. In order to avoid runtime errors, the function should be wrapped in a platform check, either through a `Platform.OS === 'platform'` or a `Platform.select()`, as shown on the example above.
> **Note:** You can find a complete example that demonstrates proper, intended use of `PlatformColor` in [PlatformColorExample.js](https://github.com/facebook/react-native/blob/main/packages/rn-tester/js/examples/PlatformColor/PlatformColorExample.js).
Is this page useful?
  * [Supported colors](https://reactnative.dev/docs/platformcolor#supported-colors)



