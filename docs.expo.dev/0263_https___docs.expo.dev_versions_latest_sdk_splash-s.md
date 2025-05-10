---
url: https://docs.expo.dev/versions/latest/sdk/splash-screen
title: https://docs.expo.dev/versions/latest/sdk/splash-screen
date: 2025-04-30T17:17:28.198656
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo SplashScreen
A library that provides access to controlling the visibility behavior of native splash screen.
Android
iOS
tvOS
Bundled version:
~0.29.24
The `SplashScreen` module from the `expo-splash-screen` library is used to tell the splash screen to remain visible until it has been explicitly told to hide. This is useful to do tasks that will happen behind the scenes such as making API calls, pre-loading fonts, animating the splash screen and so on.
Also, see the guide on [creating a splash screen image](https://docs.expo.dev/develop/user-interface/splash-screen-and-app-icon#splash-screen), or [quickly generate an icon and splash screen using your browser](https://buildicon.netlify.app/).
## Installation
Terminal
Copy
`- ``npx expo install expo-splash-screen`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Usage
This example shows how to keep the splash screen visible while loading app resources and then hide the splash screen when the app has rendered some initial content.
App.js
Copy
```
import { useCallback, useEffect, useState } from 'react';
import { Text, View } from 'react-native';
import Entypo from '@expo/vector-icons/Entypo';
import * as SplashScreen from 'expo-splash-screen';
import * as Font from 'expo-font';
// Keep the splash screen visible while we fetch resources
SplashScreen.preventAutoHideAsync();
// Set the animation options. This is optional.
SplashScreen.setOptions({
 duration: 1000,
 fade: true,
});
export default function App() {
 const [appIsReady, setAppIsReady] = useState(false);
 useEffect(() => {
  async function prepare() {
   try {
    // Pre-load fonts, make any API calls you need to do here
    await Font.loadAsync(Entypo.font);
    // Artificially delay for two seconds to simulate a slow loading
    // experience. Remove this if you copy and paste the code!
    await new Promise(resolve => setTimeout(resolve, 2000));
   } catch (e) {
    console.warn(e);
   } finally {
    // Tell the application to render
    setAppIsReady(true);
   }
  }
  prepare();
 }, []);
 const onLayoutRootView = useCallback(() => {
  if (appIsReady) {
   // This tells the splash screen to hide immediately! If we call this after
   // `setAppIsReady`, then we may see a blank screen while the app is
   // loading its initial state and rendering its first pixels. So instead,
   // we hide the splash screen once we know the root view has already
   // performed layout.
   SplashScreen.hide();
  }
 }, [appIsReady]);
 if (!appIsReady) {
  return null;
 }
 return (
  <View
   style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}
   onLayout={onLayoutRootView}><Text>SplashScreen Demo! 👋</Text><Entypo name="rocket" size={30} /></View>
 );
}

Show More

```

## Configuration
You can configure `expo-splash-screen` using its built-in [config plugin](https://docs.expo.dev/config-plugins/introduction) if you use config plugins in your project ([EAS Build](https://docs.expo.dev/build/introduction) or `npx expo run:[android|ios]`). The plugin allows you to configure various properties that cannot be set at runtime and require building a new app binary to take effect. If your app does not use EAS Build, then you'll need to manually configure the package.
Using the config plugin, as shown below, is the recommended method for configuring the splash screen. The other methods are now considered legacy and will be removed in the future.
### Example app.json with config plugin
app.json
Copy
```
{
 "expo": {
  "plugins": [
   [
    "expo-splash-screen",
    {
     "backgroundColor": "#232323",
     "image": "./assets/splash-icon.png",
     "dark": {
      "image": "./assets/splash-icon-dark.png",
      "backgroundColor": "#000000"
     },
     "imageWidth": 200
    }
   ]
  ],
 }
}

Show More

```

### Configurable properties
Name| Default| Description  
---|---|---  
`backgroundColor`| `#ffffff`| A hex color string representing the background color of the splash screen.  
`image`| `undefined`| The path to the image file that will be displayed on the splash screen. This should be your app icon or logo.  
`enableFullScreenImage_legacy`| `false`| Only for: iOSEnabling this property allows using a full screen image as the splashscreen. This is to help with the transition from the legacy splash screen configuration and will be removed in the future.  
`dark`| `undefined`| An object containing properties for configuring the splash screen when the device is in dark mode.  
`imageWidth`| `100`| The width to make the image.  
`android`| `undefined`| An object containing properties for configuring the splash screen on Android.  
`ios`| `undefined`| An object containing properties for configuring the splash screen on iOS.  
`resizeMode`| `undefined`| Determines how the image is scaled to fit the container defined by `imageWidth`. Possible values: `contain`, `cover`, or `native`.  
You can also configure `expo-splash-screen`, using the following [app config](https://docs.expo.dev/workflow/configuration) properties but the config plugin should be preferred.

Are you using this library in an existing React Native app?
See how to configure the native projects in the [installation instructions in the `expo-splash-screen` repository](https://github.com/expo/expo/tree/sdk-52/packages/expo-splash-screen#-installation-in-bare-react-native-projects).
### Animating the splash screen
`SplashScreen` provides an out-of-the-box fade animation. It can be configured using the `setOptions` method.
```
SplashScreen.setOptions({
 duration: 1000,
 fade: true,
});

```

If you prefer to use custom animation, see the [`with-splash-screen`](https://github.com/expo/examples/tree/master/with-splash-screen) example on how to apply any arbitrary animations to your splash screen. You can initialize a new project from this example by running `npx create-react-native-app -t with-splash-screen`.
## API
```
import * as SplashScreen from 'expo-splash-screen';

```

## Methods
### `SplashScreen.hide()`
Android
iOS
tvOS
Hides the native splash screen immediately. Be careful to ensure that your app has content ready to display when you hide the splash screen, or you may see a blank screen briefly. See the ["Usage"](https://docs.expo.dev/versions/latest/sdk/splash-screen/#usage) section for an example.
Returns:
`void`
### `SplashScreen.hideAsync()`
Android
iOS
tvOS
Hides the native splash screen immediately. This method is provided for backwards compatability. See the ["Usage"](https://docs.expo.dev/versions/latest/sdk/splash-screen/#usage) section for an example.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `SplashScreen.preventAutoHideAsync()`
Android
iOS
tvOS
Makes the native splash screen (configured in `app.json`) remain visible until `hideAsync` is called.
> Important note: It is recommended to call this in global scope without awaiting, rather than inside React components or hooks, because otherwise this might be called too late, when the splash screen is already hidden.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
Example
```
import * as SplashScreen from 'expo-splash-screen';
SplashScreen.preventAutoHideAsync();
export default function App() {
 // ...
}

```

### `SplashScreen.setOptions(options)`
Android
iOS
tvOS
Parameter| Type  
---|---  
options| `SplashScreenOptions[](https://docs.expo.dev/versions/latest/sdk/splash-screen/#splashscreenoptions)`  
Configures the splashscreens default animation behavior.
Returns:
`void`
## Types
### `SplashScreenOptions`
Android
iOS
tvOS
Property| Type| Description  
---|---|---  
duration(optional)| `number`| The duration of the fade out animation in milliseconds.Default:`400`  
fade(optional)| `boolean`| Only for: iOSWhether to hide the splash screen with a fade out animation.Default:`false`

