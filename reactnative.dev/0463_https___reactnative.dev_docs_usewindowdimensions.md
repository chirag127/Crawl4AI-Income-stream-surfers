---
url: https://reactnative.dev/docs/usewindowdimensions
title: https://reactnative.dev/docs/usewindowdimensions
date: 2025-05-10T21:42:44.046607
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/usewindowdimensions#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
tsx
```
import{useWindowDimensions}from'react-native';
```

`useWindowDimensions` automatically updates all of its values when screen size or font scale changes. You can get your application window's width and height like so:
tsx
```
const{height, width}=useWindowDimensions();
```

## Example[​](https://reactnative.dev/docs/usewindowdimensions#example "Direct link to Example")
## Properties[​](https://reactnative.dev/docs/usewindowdimensions#properties "Direct link to Properties")
### `fontScale`[​](https://reactnative.dev/docs/usewindowdimensions#fontscale "Direct link to fontscale")
tsx
```
useWindowDimensions().fontScale;
```

The scale of the font currently used. Some operating systems allow users to scale their font sizes larger or smaller for reading comfort. This property will let you know what is in effect.
### `height`[​](https://reactnative.dev/docs/usewindowdimensions#height "Direct link to height")
tsx
```
useWindowDimensions().height;
```

The height in pixels of the window or screen your app occupies.
### `scale`[​](https://reactnative.dev/docs/usewindowdimensions#scale "Direct link to scale")
tsx
```
useWindowDimensions().scale;
```

The pixel ratio of the device your app is running on. The values can be:
  * `1` which indicates that one point equals one pixel (usually PPI/DPI of 96, 76 on some platforms).
  * `2` or `3` which indicates a Retina or high DPI display.


### `width`[​](https://reactnative.dev/docs/usewindowdimensions#width "Direct link to width")
tsx
```
useWindowDimensions().width;
```

The width in pixels of the window or screen your app occupies.
Is this page useful?
  * [Properties](https://reactnative.dev/docs/usewindowdimensions#properties)



