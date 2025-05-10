---
url: https://docs.expo.dev/versions/latest/sdk/captureRef
title: https://docs.expo.dev/versions/latest/sdk/captureRef
date: 2025-04-30T17:15:47.401923
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# captureRef
A library that allows you to capture a React Native view and save it as an image.
Android
iOS
Bundled version:
~4.0.3
> This library is listed in the Expo SDK reference because it is included in [Expo Go](https://docs.expo.dev/get-started/set-up-your-environment). You may use any library of your choice with [development builds](https://docs.expo.dev/develop/development-builds/introduction).
Given a view, `captureRef` will essentially screenshot that view and return an image for you. This is very useful for things like signature pads, where the user draws something, and then you want to save an image from it.
If you're interested in taking snapshots from the GLView, we recommend you use [GLView's takeSnapshotAsync](https://docs.expo.dev/versions/latest/sdk/gl-view#takesnapshotasyncoptions) instead.
## Installation
Terminal
Copy
`- ``npx expo install react-native-view-shot`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project. Then, follow the [installation instructions](https://github.com/gre/react-native-view-shot) provided in the library's README or documentation.
## API
```
import { captureRef } from 'react-native-view-shot';

```

### `captureRef(view, options)`
Snapshots the given view.
#### Arguments
  * view (_number|ReactElement_) -- The `ref` or `reactTag` (also known as node handle) for the view to snapshot.
  * options (_object_) --
An optional map of optional options
    * format (_string_) -- `"png" | "jpg" | "webm"`, defaults to `"png"`, `"webm"` supported only on Android.
    * quality (_number_) -- Number between 0 and 1 where 0 is worst quality and 1 is best, defaults to `1`
    * result (_string_) -- The type for the resulting image. - `'tmpfile'` -- (default) Return a temporary file uri. - `'base64'` -- base64 encoded image. - `'data-uri'` -- base64 encoded image with data-uri prefix.
    * height (_number_) -- Height of result in pixels
    * width (_number_) -- Width of result in pixels
    * snapshotContentContainer (_bool_) -- if true and when view is a ScrollView, the "content container" height will be evaluated instead of the container height


#### Returns
An image of the format specified in the options parameter.
## Note on pixel values
Remember to take the device `PixelRatio` into account. When you work with pixel values in a UI, most of the time those units are "logical pixels" or "device-independent pixels". With images like PNG files, you often work with "physical pixels". You can get the `PixelRatio` of the device using the React Native API: `PixelRatio.get()`
For example, to save a 'FullHD' picture of `1080x1080`, you would do something like this:
```
const targetPixelCount = 1080; // If you want full HD pictures
const pixelRatio = PixelRatio.get(); // The pixel ratio of the device
// pixels * pixelRatio = targetPixelCount, so pixels = targetPixelCount / pixelRatio
const pixels = targetPixelCount / pixelRatio;
const result = await captureRef(this.imageContainer, {
 result: 'tmpfile',
 height: pixels,
 width: pixels,
 quality: 1,
 format: 'png',
});

```


