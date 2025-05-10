---
url: https://docs.expo.dev/versions/latest/sdk/font
title: https://docs.expo.dev/versions/latest/sdk/font
date: 2025-04-30T17:16:24.926308
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo Font
A library that allows loading fonts at runtime and using them in React Native components.
Android
iOS
tvOS
Web
Bundled version:
~13.0.4
`expo-font` allows loading fonts from the web and using them in React Native components. See more detailed usage information in the [Fonts](https://docs.expo.dev/develop/user-interface/fonts) guide.
## Installation
Terminal
Copy
`- ``npx expo install expo-font`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Configuration in app config
The recommended way to add fonts to your app is through `expo-font` built-in [config plugin](https://docs.expo.dev/config-plugins/introduction) if you use config plugins in your project ([EAS Build](https://docs.expo.dev/build/introduction) or `npx expo run: [android|ios]`). The plugin allows you to embed font files at build time which is more efficient than using [`loadAsync`](https://docs.expo.dev/versions/latest/sdk/font#loadasyncfontfamilyorfontmap-source). See the [Fonts](https://docs.expo.dev/develop/user-interface/fonts#with-expo-font-config-plugin) guide on how to use it.
### Example app.json with config plugin
app.json
Copy
```
{
 "expo": {
  "plugins": [
   [
    "expo-font",
    {
     "fonts": ["path/to/file.ttf"]
    }
   ]
  ]
 }
}

```

### Configurable properties
Name| Default| Description  
---|---|---  
`fonts`| `[]`| An array of font files to link to the native project. The paths should be relative to the project root. The file names will become the font family names on Android. On iOS, the font family name may not be the same as the file name — use [`getLoadedFonts`](https://docs.expo.dev/versions/latest/sdk/font/#getloadedfonts) to see what fonts are available.  
Are you using this library in an existing React Native app?
  * Android: Copy font files to android/app/src/main/assets/fonts.
  * iOS: See [Adding a Custom Font to Your App](https://developer.apple.com/documentation/uikit/adding-a-custom-font-to-your-app) in the Apple Developer documentation.


## Usage
Minimal example of using a custom font
```
import { useFonts } from 'expo-font';
import * as SplashScreen from 'expo-splash-screen';
import { useEffect } from 'react';
import { Text, View, StyleSheet } from 'react-native';
SplashScreen.preventAutoHideAsync();
export default function App() {
 const [loaded, error] = useFonts({
  'Inter-Black': require('./assets/fonts/Inter-Black.otf'),
 });
 useEffect(() => {
  if (loaded || error) {
   SplashScreen.hideAsync();
  }
 }, [loaded, error]);
 if (!loaded && !error) {
  return null;
 }
 return (
  <View style={styles.container}><Text style={{ fontFamily: 'Inter-Black', fontSize: 30 }}>Inter Black</Text><Text style={{ fontSize: 30 }}>Platform Default</Text></View>
 );
}
const styles = StyleSheet.create({
 container: {
  flex: 1,
  justifyContent: 'center',
  alignItems: 'center',
 },
});

Show More

```

## API
```
import * as Font from 'expo-font';

```

## Hooks
### `useFonts(map)`
Android
iOS
tvOS
Web
Parameter| Type| Description  
---|---|---  
map| `string | Record<string, >`| A map of `fontFamily`s to [`FontSource`](https://docs.expo.dev/versions/latest/sdk/font/#fontsource)s. After loading the font you can use the key in the `fontFamily` style prop of a `Text` element.  
Load a map of fonts with [`loadAsync`](https://docs.expo.dev/versions/latest/sdk/font/#loadasyncfontfamilyorfontmap-source). This returns a `boolean` if the fonts are loaded and ready to use. It also returns an error if something went wrong, to use in development.
> Note, the fonts are not "reloaded" when you dynamically change the font map.
Returns:
`[boolean, null | ]`
  * loaded (`boolean`) - A boolean to detect if the font for `fontFamily` has finished loading.
  * error (`Error | null`) - An error encountered when loading the fonts.


Example
```
const [loaded, error] = useFonts({ ... });

```

## Methods
### `getLoadedFonts()`
Android
iOS
tvOS
Web
Synchronously get all the fonts that have been loaded. This includes fonts that were bundled at build time using the config plugin, as well as those loaded at runtime using `loadAsync`.
Returns:
`string[]`
Returns array of strings which you can use as `fontFamily` [style prop](https://reactnative.dev/docs/text#style).
### `isLoaded(fontFamily)`
Android
iOS
tvOS
Web
Parameter| Type| Description  
---|---|---  
fontFamily| `string`| The name used to load the `FontResource`.  
Synchronously detect if the font for `fontFamily` has finished loading.
Returns:
`boolean`
Returns `true` if the font has fully loaded.
### `isLoading(fontFamily)`
Android
iOS
tvOS
Web
Parameter| Type| Description  
---|---|---  
fontFamily| `string`| The name used to load the `FontResource`.  
Synchronously detect if the font for `fontFamily` is still being loaded.
Returns:
`boolean`
Returns `true` if the font is still loading.
### `loadAsync(fontFamilyOrFontMap, source)`
Android
iOS
tvOS
Web
Parameter| Type| Description  
---|---|---  
fontFamilyOrFontMap| `string | Record<string, >`| String or map of values that can be used as the `fontFamily` [style prop](https://reactnative.dev/docs/text#style) with React Native `Text` elements.  
source(optional)| | The font asset that should be loaded into the `fontFamily` namespace.  
An efficient method for loading fonts from static or remote resources which can then be used with the platform's native text elements. In the browser, this generates a `@font-face` block in a shared style sheet for fonts. No CSS is needed to use this method.
> Note: We recommend using the [config plugin](https://docs.expo.dev/versions/latest/sdk/font/#configuration-in-appjsonappconfigjs) instead whenever possible.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
Returns a promise that fulfils when the font has loaded. Often you may want to wrap the method in a `try/catch/finally` to ensure the app continues if the font fails to load.
## Types
### `FontResource`
Android
iOS
tvOS
Web
An object used to dictate the resource that is loaded into the provided font namespace when used with [`loadAsync`](https://docs.expo.dev/versions/latest/sdk/font/#loadasyncfontfamilyorfontmap-source).
Property| Type| Description  
---|---|---  
default(optional)| `string`  
display(optional)| | Only for: WebSets the [`font-display`](https://docs.expo.dev/versions/latest/sdk/font/#fontdisplay) property for a given typeface in the browser.  
uri(optional)| `string | number`  
### `FontSource`
Android
iOS
tvOS
Web
Literal Type: `union`
The different types of assets you can provide to the [`loadAsync()`](https://docs.expo.dev/versions/latest/sdk/font/#loadasyncfontfamilyorfontmap-source) function. A font source can be a URI, a module ID, or an Expo Asset.
Acceptable values are: `string` | `number` |  | 
## Enums
### `FontDisplay`
Web
Sets the [font-display](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display) for a given typeface. The default font value on web is `FontDisplay.AUTO`. Even though setting the `fontDisplay` does nothing on native platforms, the default behavior emulates `FontDisplay.SWAP` on flagship devices like iOS, Samsung, Pixel, etc. Default functionality varies on One Plus devices. In the browser this value is set in the generated `@font-face` CSS block and not as a style property meaning you cannot dynamically change this value based on the element it's used in.
#### `AUTO`
`FontDisplay.AUTO ＝ "auto"`
(Default) The font display strategy is defined by the user agent or platform. This generally defaults to the text being invisible until the font is loaded. Good for buttons or banners that require a specific treatment.
#### `BLOCK`
`FontDisplay.BLOCK ＝ "block"`
The text will be invisible until the font has loaded. If the font fails to load then nothing will appear - it's best to turn this off when debugging missing text.
#### `FALLBACK`
`FontDisplay.FALLBACK ＝ "fallback"`
Splits the behavior between `SWAP` and `BLOCK`. There will be a [100ms timeout](https://developers.google.com/web/updates/2016/02/font-display?hl=en) where the text with a custom font is invisible, after that the text will either swap to the styled text or it'll show the unstyled text and continue to load the custom font. This is good for buttons that need a custom font but should also be quickly available to screen-readers.
#### `OPTIONAL`
`FontDisplay.OPTIONAL ＝ "optional"`
This works almost identically to `FALLBACK`, the only difference is that the browser will decide to load the font based on slow connection speed or critical resource demand.
#### `SWAP`
`FontDisplay.SWAP ＝ "swap"`
Fallback text is rendered immediately with a default font while the desired font is loaded. This is good for making the content appear to load instantly and is usually preferred.
## Error codes
Code| Description  
---|---  
ERR_FONT_API| If the arguments passed to `loadAsync` are invalid.  
ERR_FONT_SOURCE| The provided resource was of an incorrect type.  
ERR_WEB_ENVIRONMENT| The browser's `document` element doesn't support injecting fonts.  
ERR_DOWNLOAD| Failed to download the provided resource.  
ERR_FONT_FAMILY| Invalid font family name was provided.  
ERR_UNLOAD| Attempting to unload fonts that haven't finished loading yet.

