---
url: https://docs.expo.dev/versions/latest/sdk/svg
title: https://docs.expo.dev/versions/latest/sdk/svg
date: 2025-04-30T17:17:28.195694
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# React Native SVG
A library that allows using SVGs in your app.
Android
iOS
macOS
tvOS
Web
Bundled version:
15.8.0
> This library is listed in the Expo SDK reference because it is included in [Expo Go](https://expo.dev/go). You may use any library of your choice with [development builds](https://docs.expo.dev/develop/development-builds/introduction).
`react-native-svg` allows you to use SVGs in your app, with support for interactivity and animation.
## Installation
Terminal
Copy
`- ``npx expo install react-native-svg`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project. Then, follow the [installation instructions](https://github.com/react-native-community/react-native-svg#with-react-native-cli) provided in the library's README or documentation.
## API
```
import * as Svg from 'react-native-svg';

```

### `Svg`
A set of drawing primitives such as `Circle`, `Rect`, `Path`, `ClipPath`, and `Polygon`. It supports most SVG elements and properties. The implementation is provided by [react-native-svg](https://github.com/react-native-community/react-native-svg), and documentation is provided in that repository.
SVG
```
import Svg, { Circle, Rect } from 'react-native-svg';
export default function SvgComponent(props) {
 return (
  <Svg height="50%" width="50%" viewBox="0 0 100 100" {...props}><Circle cx="50" cy="50" r="45" stroke="blue" strokeWidth="2.5" fill="green" /><Rect x="15" y="15" width="70" height="70" stroke="red" strokeWidth="2" fill="yellow" /></Svg>
 );
}

```

### Pro tips
Here are some helpful links that will get you moving fast!
  * Looking for SVGs? Try the [noun project](https://thenounproject.com/).
  * Create or modify your own SVGs for free using [Figma](https://www.figma.com/).
  * Optimize your SVG with [SVGOMG](https://jakearchibald.github.io/svgomg/). This will make the code smaller and easier to work with. Be sure not to remove the `viewbox` for best results on Android.
  * Convert your SVG to an Expo component in the browser using [React SVGR](https://react-svgr.com/playground/?native=true&typescript=true).



