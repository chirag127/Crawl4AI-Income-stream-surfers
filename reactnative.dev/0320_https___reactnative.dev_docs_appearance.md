---
url: https://reactnative.dev/docs/appearance
title: https://reactnative.dev/docs/appearance
date: 2025-05-10T21:39:27.416998
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/appearance#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
tsx
```
import{Appearance}from'react-native';
```

The `Appearance` module exposes information about the user's appearance preferences, such as their preferred color scheme (light or dark).
#### Developer notes[​](https://reactnative.dev/docs/appearance#developer-notes "Direct link to Developer notes")
  * Android
  * iOS
  * Web


> The `Appearance` API is inspired by the [Media Queries draft](https://drafts.csswg.org/mediaqueries-5/) from the W3C. The color scheme preference is modeled after the [`prefers-color-scheme` CSS media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme).
> The color scheme preference will map to the user's Light or [Dark theme](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme) preference on Android 10 (API level 29) devices and higher.
> The color scheme preference will map to the user's Light or [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/ios/visual-design/dark-mode/) preference on iOS 13 devices and higher.
> Note: When taking a screenshot, by default, the color scheme may flicker between light and dark mode. It happens because the iOS takes snapshots on both color schemes and updating the user interface with color scheme is asynchronous.
## Example[​](https://reactnative.dev/docs/appearance#example "Direct link to Example")
You can use the `Appearance` module to determine if the user prefers a dark color scheme:
tsx
```
const colorScheme =Appearance.getColorScheme();if(colorScheme ==='dark'){// Use dark color scheme
```

Although the color scheme is available immediately, this may change (e.g. scheduled color scheme change at sunrise or sunset). Any rendering logic or styles that depend on the user preferred color scheme should try to call this function on every render, rather than caching the value. For example, you may use the [`useColorScheme`](https://reactnative.dev/docs/usecolorscheme) React hook as it provides and subscribes to color scheme updates, or you may use inline styles rather than setting a value in a `StyleSheet`.
# Reference
## Methods[​](https://reactnative.dev/docs/appearance#methods "Direct link to Methods")
### `getColorScheme()`[​](https://reactnative.dev/docs/appearance#getcolorscheme "Direct link to getcolorscheme")
tsx
```
staticgetColorScheme():'light'|'dark'|null;
```

Indicates the current user preferred color scheme. The value may be updated later, either through direct user action (e.g. theme selection in device settings or application-level selected user interface style via `setColorScheme`) or on a schedule (e.g. light and dark themes that follow the day/night cycle).
Supported color schemes:
  * `light`: The user prefers a light color theme.
  * `dark`: The user prefers a dark color theme.
  * null: The user has not indicated a preferred color theme.


See also: `useColorScheme` hook.
> Note: `getColorScheme()` will always return `light` when debugging with Chrome.
### `setColorScheme()`[​](https://reactnative.dev/docs/appearance#setcolorscheme "Direct link to setcolorscheme")
tsx
```
staticsetColorScheme('light'|'dark'|null):void;
```

Force the application to always adopt a light or dark interface style. The default value is `null` which causes the application to inherit the system's interface style. If you assign a different value, the new style applies to the application and all native elements within the application (Alerts, Pickers etc).
Supported color schemes:
  * `light`: Apply light user interface style.
  * `dark`: Apply dark user interface style.
  * null: Follow the system's interface style.


> Note: The change will not affect the system's selected interface style or any style set in other applications.
### `addChangeListener()`[​](https://reactnative.dev/docs/appearance#addchangelistener "Direct link to addchangelistener")
tsx
```
staticaddChangeListener( listener:(preferences:{colorScheme:'light'|'dark'|null})=>void,):NativeEventSubscription;
```

Add an event handler that is fired when appearance preferences change.
Is this page useful?
  * [Methods](https://reactnative.dev/docs/appearance#methods)
    * [`getColorScheme()`](https://reactnative.dev/docs/appearance#getcolorscheme)
    * [`setColorScheme()`](https://reactnative.dev/docs/appearance#setcolorscheme)
    * [`addChangeListener()`](https://reactnative.dev/docs/appearance#addchangelistener)



