---
url: https://docs.expo.dev/versions/latest/sdk/navigation-bar
title: https://docs.expo.dev/versions/latest/sdk/navigation-bar
date: 2025-04-30T17:16:56.373782
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo NavigationBar
A library that provides access to various interactions with the native navigation bar on Android.
Android
Bundled version:
~4.0.9
`expo-navigation-bar` enables you to modify and observe the native navigation bar on Android devices. Due to some Android platform restrictions, parts of this API overlap with the `expo-status-bar` API.
Properties are named after style properties; visibility, position, backgroundColor, borderColor, and so on.
The APIs in this package have no impact when "Gesture Navigation" is enabled on the Android device. There is currently no native Android API to detect if "Gesture Navigation" is enabled or not.
## Installation
Terminal
Copy
`- ``npx expo install expo-navigation-bar`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## API
```
import * as NavigationBar from 'expo-navigation-bar';

```

## Hooks
### `useVisibility()`
Android
React hook that statefully updates with the visibility of the system navigation bar.
Returns:
`NavigationBarVisibility[](https://docs.expo.dev/versions/latest/sdk/navigation-bar/#navigationbarvisibility) | null`
Visibility of the navigation bar, `null` during async initialization.
Example
```
function App() {
 const visibility = NavigationBar.useVisibility()
 // React Component...
}

```

## Methods
### `NavigationBar.getBackgroundColorAsync()`
Android
Gets the navigation bar's background color.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
Current navigation bar color in hex format. Returns `#00000000` (transparent) on unsupported platforms (iOS, web).
Example
```
const color = await NavigationBar.getBackgroundColorAsync();

```

### `NavigationBar.getBehaviorAsync()`
Android
Gets the behavior of the status and navigation bars when the user swipes or touches the screen.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<NavigationBarBehavior[](https://docs.expo.dev/versions/latest/sdk/navigation-bar/#navigationbarbehavior)>`
Navigation bar interaction behavior. Returns `inset-touch` on unsupported platforms (iOS, web).
Example
```
await NavigationBar.getBehaviorAsync()

```

### `NavigationBar.getBorderColorAsync()`
Android
Gets the navigation bar's top border color, also known as the "divider color".
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
Navigation bar top border color in hex format. Returns `#00000000` (transparent) on unsupported platforms (iOS, web).
Example
```
const color = await NavigationBar.getBorderColorAsync();

```

### `NavigationBar.getButtonStyleAsync()`
Android
Gets the navigation bar's button color styles.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<NavigationBarButtonStyle[](https://docs.expo.dev/versions/latest/sdk/navigation-bar/#navigationbarbuttonstyle)>`
Navigation bar foreground element color settings. Returns `light` on unsupported platforms (iOS, web).
Example
```
const style = await NavigationBar.getButtonStyleAsync();

```

### `NavigationBar.getVisibilityAsync()`
Android
Get the navigation bar's visibility.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<NavigationBarVisibility[](https://docs.expo.dev/versions/latest/sdk/navigation-bar/#navigationbarvisibility)>`
Navigation bar's current visibility status. Returns `hidden` on unsupported platforms (iOS, web).
Example
```
const visibility = await NavigationBar.getVisibilityAsync("hidden");

```

### `NavigationBar.setBackgroundColorAsync(color)`
Android
Parameter| Type| Description  
---|---|---  
color| | Any valid [CSS 3 (SVG) color](http://www.w3.org/TR/css3-color/#svg-color).  
Changes the navigation bar's background color.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
Example
```
NavigationBar.setBackgroundColorAsync("white");

```

### `NavigationBar.setBehaviorAsync(behavior)`
Android
Parameter| Type| Description  
---|---|---  
behavior| `NavigationBarBehavior[](https://docs.expo.dev/versions/latest/sdk/navigation-bar/#navigationbarbehavior)`| Dictates the interaction behavior of the navigation bar.  
Sets the behavior of the status bar and navigation bar when they are hidden and the user wants to reveal them.
For example, if the navigation bar is hidden (`setVisibilityAsync(false)`) and the behavior is `'overlay-swipe'`, the user can swipe from the bottom of the screen to temporarily reveal the navigation bar.
  * `'overlay-swipe'`: Temporarily reveals the System UI after a swipe gesture (bottom or top) without insetting your App's content.
  * `'inset-swipe'`: Reveals the System UI after a swipe gesture (bottom or top) and insets your App's content (Safe Area). The System UI is visible until you explicitly hide it again.
  * `'inset-touch'`: Reveals the System UI after a touch anywhere on the screen and insets your App's content (Safe Area). The System UI is visible until you explicitly hide it again.


Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
Example
```
await NavigationBar.setBehaviorAsync('overlay-swipe')

```

### `NavigationBar.setBorderColorAsync(color)`
Android
Parameter| Type| Description  
---|---|---  
color| | Any valid [CSS 3 (SVG) color](http://www.w3.org/TR/css3-color/#svg-color).  
Changes the navigation bar's border color.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
Example
```
NavigationBar.setBorderColorAsync("red");

```

### `NavigationBar.setButtonStyleAsync(style)`
Android
Parameter| Type| Description  
---|---|---  
style| `NavigationBarButtonStyle[](https://docs.expo.dev/versions/latest/sdk/navigation-bar/#navigationbarbuttonstyle)`| Dictates the color of the foreground element color.  
Changes the navigation bar's button colors between white (`light`) and a dark gray color (`dark`).
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
Example
```
NavigationBar.setButtonStyleAsync("light");

```

### `NavigationBar.setPositionAsync(position)`
Android
Parameter| Type| Description  
---|---|---  
position| `NavigationBarPosition[](https://docs.expo.dev/versions/latest/sdk/navigation-bar/#navigationbarposition)`| Based on CSS position property.  
Sets positioning method used for the navigation bar (and status bar). Setting position `absolute` will float the navigation bar above the content, whereas position `relative` will shrink the screen to inline the navigation bar.
When drawing behind the status and navigation bars, ensure the safe area insets are adjusted accordingly.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
Example
```
// enables edge-to-edge mode
await NavigationBar.setPositionAsync('absolute')
// transparent backgrounds to see through
await NavigationBar.setBackgroundColorAsync('#ffffff00')

```

### `NavigationBar.setVisibilityAsync(visibility)`
Android
Parameter| Type| Description  
---|---|---  
visibility| `NavigationBarVisibility[](https://docs.expo.dev/versions/latest/sdk/navigation-bar/#navigationbarvisibility)`| Based on CSS visibility property.  
Set the navigation bar's visibility.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
Example
```
NavigationBar.setVisibilityAsync("hidden");

```

### `NavigationBar.unstable_getPositionAsync()`
Android
Whether the navigation and status bars float above the app (absolute) or sit inline with it (relative). This value can be incorrect if `androidNavigationBar.visible` is used instead of the config plugin `position` property.
This method is unstable because the position can be set via another native module and get out of sync. Alternatively, you can get the position by measuring the insets returned by `react-native-safe-area-context`.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<NavigationBarPosition[](https://docs.expo.dev/versions/latest/sdk/navigation-bar/#navigationbarposition)>`
Navigation bar positional rendering mode. Returns `relative` on unsupported platforms (iOS, web).
Example
```
await NavigationBar.unstable_getPositionAsync()

```

## Event Subscriptions
### `NavigationBar.addVisibilityListener(listener)`
Android
Parameter| Type  
---|---  
listener| `(event: NavigationBarVisibilityEvent[](https://docs.expo.dev/versions/latest/sdk/navigation-bar/#navigationbarvisibilityevent)) => void`  
Observe changes to the system navigation bar. Due to platform constraints, this callback will also be triggered when the status bar visibility changes.
Returns:
`EventSubscription`
Example
```
NavigationBar.addVisibilityListener(({ visibility }) => {
 // ...
});

```

## Types
### `NavigationBarBehavior`
Android
Literal Type: `string`
Interaction behavior for the system navigation bar.
Acceptable values are: `'overlay-swipe'` | `'inset-swipe'` | `'inset-touch'`
### `NavigationBarButtonStyle`
Android
Literal Type: `string`
Appearance of the foreground elements in the navigation bar, i.e. the color of the menu, back, home button icons.
  * `dark` makes buttons darker to adjust for a mostly light nav bar.
  * `light` makes buttons lighter to adjust for a mostly dark nav bar.


Acceptable values are: `'light'` | `'dark'`
### `NavigationBarPosition`
Android
Literal Type: `string`
Navigation bar positional mode.
Acceptable values are: `'relative'` | `'absolute'`
### `NavigationBarVisibility`
Android
Literal Type: `string`
Visibility of the navigation bar.
Acceptable values are: `'visible'` | `'hidden'`
### `NavigationBarVisibilityEvent`
Android
Current system UI visibility state. Due to platform constraints, this will return when the status bar visibility changes as well as the navigation bar.
Property| Type| Description  
---|---|---  
rawVisibility| `number`| Native Android system UI visibility state, returned from the native Android `setOnSystemUiVisibilityChangeListener` API.  
visibility| `NavigationBarVisibility[](https://docs.expo.dev/versions/latest/sdk/navigation-bar/#navigationbarvisibility)`| Current navigation bar visibility.

