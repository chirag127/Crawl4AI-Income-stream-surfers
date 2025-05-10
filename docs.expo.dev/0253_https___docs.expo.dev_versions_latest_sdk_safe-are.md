---
url: https://docs.expo.dev/versions/latest/sdk/safe-area-context
title: https://docs.expo.dev/versions/latest/sdk/safe-area-context
date: 2025-04-30T17:17:22.530270
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview/)[EAS](https://docs.expo.dev/eas/)[Reference](https://docs.expo.dev/versions/latest/)[Learn](https://docs.expo.dev/tutorial/overview/)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive/)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# React Native Safe Area Context
A library with a flexible API for accessing the device's safe area inset information.
Android
iOS
tvOS
Web
Bundled version:
4.12.0
> This library is listed in the Expo SDK reference because it is included in [Expo Go](https://expo.dev/go). You may use any library of your choice with [development builds](https://docs.expo.dev/develop/development-builds/introduction/).
`react-native-safe-area-context` provides a flexible API for accessing device safe area inset information. This allows you to position your content appropriately around notches, status bars, home indicators, and other such device and operating system interface elements. It also provides a `SafeAreaView` component that you can use in place of `View` to automatically inset your views to account for safe areas.
## Installation
Terminal
Copy
`- ``npx expo install react-native-safe-area-context`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview/), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules/) in your project. Then, follow the [installation instructions](https://github.com/th3rdwave/react-native-safe-area-context#getting-started) provided in the library's README or documentation.
## API
```
import {
 SafeAreaView,
 SafeAreaProvider,
 SafeAreaInsetsContext,
 useSafeAreaInsets,
} from 'react-native-safe-area-context';

```

## Components
### `SafeAreaView`
`SafeAreaView` is a regular `View` component with the safe area edges applied as padding.
If you set your own padding on the view, it will be added to the padding from the safe area.
> If you are targeting web, you must set up `SafeAreaProvider` as described in the [Context](https://docs.expo.dev/versions/latest/sdk/safe-area-context/#context) section.
```
import { SafeAreaView } from 'react-native-safe-area-context';
function SomeComponent() {
 return (
  <SafeAreaView><View /></SafeAreaView>
 );
}

```

SafeAreaView Props
### `edges`
Optional • Type: [`Edge[]`](https://docs.expo.dev/versions/latest/sdk/safe-area-context/#edge) • Default: `["top", "right", "bottom", "left"]`
Sets the edges to apply the safe area insets to.
### `emulateUnlessSupported`
Optional • Type: `boolean` • Default: `true`
On iOS 10+, emulate the safe area using the status bar height and home indicator sizes.
## Hooks
### `useSafeAreaInsets()`
Hook gives you direct access to the safe area insets. This is a more advanced use-case, and might perform worse than `SafeAreaView` when rotating the device.
Example
```
import { useSafeAreaInsets } from 'react-native-safe-area-context';
function HookComponent() {
 const insets = useSafeAreaInsets();
 return <View style={{ paddingTop: insets.top }} />;
}

```

Returns
[`EdgeInsets`](https://docs.expo.dev/versions/latest/sdk/safe-area-context/#edgeinsets)
## Types
### `Edge`
String union of possible edges.
Acceptable values are: `'top'`, `'right'`, `'bottom'`, `'left'`.
### `EdgeInsets`
Represent the hook result.
EdgeInsets Properties
Name| Type| Description  
---|---|---  
`bottom`| `number`| Value of bottom inset.  
`left`| `number`| Value of left inset.  
`right`| `number`| Value of right inset.  
`top`| `number`| Value of top inset.  
## Guides
### Context
To use safe area context, you need to add `SafeAreaProvider` in your app root component.
> You may need to add it in other places too, including at the root of any modals any routes when using `react-native-screen`.
```
import { SafeAreaProvider } from 'react-native-safe-area-context';
function App() {
 return <SafeAreaProvider>...</SafeAreaProvider>;
}

```

Then, you can use [`useSafeAreaInsets()`](https://docs.expo.dev/versions/latest/sdk/safe-area-context/#usesafeareainsets) hook and also consumer API to access inset data:
```
import { SafeAreaInsetsContext } from 'react-native-safe-area-context';
function Component() {
 return (
  <SafeAreaInsetsContext.Consumer>{insets => <View style={{ paddingTop: insets.top }} />}</SafeAreaInsetsContext.Consumer>
 );
}

```

### Optimization
If you can, use `SafeAreaView`. It's implemented natively so when rotating the device, there is no delay from the asynchronous bridge.
To speed up the initial render, you can import `initialWindowMetrics` from this package and set as the `initialMetrics` prop on the provider as described in Web SSR. You cannot do this if your provider remounts, or you are using `react-native-navigation`.
```
import { SafeAreaProvider, initialWindowMetrics } from 'react-native-safe-area-context';
function App() {
 return <SafeAreaProvider initialMetrics={initialWindowMetrics}>...</SafeAreaProvider>;
}

```

### Web SSR
If you are doing server side rendering on the web, you can use `initialSafeAreaInsets` to inject values based on the device the user has, or simply pass zero. Otherwise, insets measurement will break rendering your page content since it is async.
### Migrating from CSS
#### Before
In a web-only app, you would use CSS environment variables to get the size of the screen's safe area insets.
styles.css
Copy
```
div {
 padding-top: env(safe-area-inset-top);
 padding-left: env(safe-area-inset-left);
 padding-bottom: env(safe-area-inset-bottom);
 padding-right: env(safe-area-inset-right);
}

```

#### After
Universally, the hook `useSafeAreaInsets()` can provide access to this information.
App.js
Copy
```
import { useSafeAreaInsets } from 'react-native-safe-area-context';
function App() {
 const insets = useSafeAreaInsets();
 return (
  <View
   style={{
    paddingTop: insets.top,
    paddingLeft: insets.left,
    paddingBottom: insets.bottom,
    paddingRight: insets.right,
   }}
  />
 );
}

```


