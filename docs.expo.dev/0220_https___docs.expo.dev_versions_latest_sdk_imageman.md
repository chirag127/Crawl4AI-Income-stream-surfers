---
url: https://docs.expo.dev/versions/latest/sdk/imagemanipulator
title: https://docs.expo.dev/versions/latest/sdk/imagemanipulator
date: 2025-04-30T17:16:24.912257
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo ImageManipulator
A library that provides an API for image manipulation on the local file system.
Android
iOS
Web
Bundled version:
~13.0.6
`expo-image-manipulator` provides an API to modify images stored on the local file system.
## Installation
Terminal
Copy
`- ``npx expo install expo-image-manipulator`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Usage
This will first rotate the image 90 degrees clockwise, then flip the rotated image vertically and save it as a PNG.
Basic ImageManipulator usage
```
import { useState } from 'react';
import { Button, Image, StyleSheet, View } from 'react-native';
import { Asset } from 'expo-asset';
import { FlipType, SaveFormat, useImageManipulator } from 'expo-image-manipulator';
const IMAGE = Asset.fromModule(require('./assets/snack-icon.png'));
export default function App() {
 const [image, setImage] = useState(IMAGE);
 const context = useImageManipulator(IMAGE.uri);
 const rotate90andFlip = async () => {
  context.rotate(90).flip(FlipType.Vertical);
  const image = await context.renderAsync();
  const result = await image.saveAsync({
   format: SaveFormat.PNG,
  });
  setImage(result);
 };
 return (
  <View style={styles.container}><View style={styles.imageContainer}><Image source={{ uri: image.localUri || image.uri }} style={styles.image} /></View><Button title="Rotate and Flip" onPress={rotate90andFlip} /></View>
 );
}
const styles = StyleSheet.create({
 container: {
  flex: 1,
  justifyContent: 'center',
 },
 imageContainer: {
  marginVertical: 20,
  alignItems: 'center',
  justifyContent: 'center',
 },
 image: {
  width: 300,
  height: 300,
  resizeMode: 'contain',
 },
});

Show More

```

## API
```
import * as ImageManipulator from 'expo-image-manipulator';

```

## Constants
### `ImageManipulator.ImageManipulator`
Android
iOS
Web
Type: `ImageManipulator[](https://docs.expo.dev/versions/latest/sdk/imagemanipulator/#imagemanipulator)`
## Hooks
### `useImageManipulator(uri)`
Android
iOS
Web
Parameter| Type  
---|---  
uri| `string`  
Returns:
## Classes
### `Context`
Android
iOS
Web
Type: Class extends 
A context for an image manipulation. It provides synchronous, chainable functions that schedule transformations on the original image to the background thread. Use an asynchronous [`renderAsync`](https://docs.expo.dev/versions/latest/sdk/imagemanipulator/#contextrenderasync) to await for all transformations to finish and access the final image.
Context Methods
### `crop(rect)`
Android
iOS
Web
Parameter| Type| Description  
---|---|---  
rect| `{  height: number,   originX: number,   originY: number,   width: number }`| Fields specify top-left corner and dimensions of a crop rectangle.  
Crops the image to the given rectangle's origin and size.
Returns:
### `extent(options)`
Web
Parameter| Type  
---|---  
options| `{  backgroundColor: null | string,   height: number,   originX: number,   originY: number,   width: number }`  
Set the image size and offset. If the image is enlarged, unfilled areas are set to the `backgroundColor`. To position the image, use `originX` and `originY`.
Returns:
### `flip(flipType)`
Android
iOS
Web
Parameter| Type| Description  
---|---|---  
flipType| `'vertical' | 'horizontal'`| An axis on which image will be flipped. Only one flip per transformation is available. If you want to flip according to both axes then provide two separate transformations.  
Flips the image vertically or horizontally.
Returns:
### `renderAsync()`
Android
iOS
Web
Awaits for all manipulation tasks to finish and resolves with a reference to the resulted native image.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
### `reset()`
Android
iOS
Web
Resets the manipulator context to the originally loaded image.
Returns:
### `resize(size)`
Android
iOS
Web
Parameter| Type| Description  
---|---|---  
size| `{  height: null | number,   width: null | number }`| Values correspond to the result image dimensions. If you specify only one value, the other will be calculated automatically to preserve image ratio.  
Resizes the image to the given size.
Returns:
### `rotate(degrees)`
Android
iOS
Web
Parameter| Type| Description  
---|---|---  
degrees| `number`| Degrees to rotate the image. Rotation is clockwise when the value is positive and counter-clockwise when negative.  
Rotates the image by the given number of degrees.
Returns:
### `ImageManipulator`
Android
iOS
Web
Type: Class extends 
ImageManipulator Properties
### `Context`
Android
iOS
Web
Type: `Context`
### `Image`
Android
iOS
Web
Type: `ImageRef`
ImageManipulator Methods
### `manipulate(uri)`
Android
iOS
Web
Parameter| Type  
---|---  
uri| `string`  
Loads an image from the given URI and creates a new image manipulation context.
Returns:
### `ImageRef`
Android
iOS
Web
Type: Class extends `SharedRef[](https://docs.expo.dev/versions/v52.0.0/sdk/expo#sharedref)<'image'>`
A reference to a native instance of the image.
ImageRef Properties
### `height`
Android
iOS
Web
Type: `number`
Height of the image.
### `nativeRefType`
Android
iOS
Web
Type: `string`
The type of the native reference.
### `width`
Android
iOS
Web
Type: `number`
Width of the image.
ImageRef Methods
### `saveAsync(options)`
Android
iOS
Web
Parameter| Type| Description  
---|---|---  
options(optional)| | A map defining how modified image should be saved.  
Saves the image to the file system in the cache directory.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
## Methods
> Deprecated It has been replaced by the new, contextual and object-oriented API. Use [`ImageManipulator.manipulate`](https://docs.expo.dev/versions/latest/sdk/imagemanipulator/#manipulateuri) or [`useImageManipulator`](https://docs.expo.dev/versions/latest/sdk/imagemanipulator/#useimagemanipulatoruri) instead.
### `ImageManipulator.manipulateAsync(uri, actions, saveOptions)`
Android
iOS
Web
Parameter| Type| Description  
---|---|---  
uri| `string`| URI of the file to manipulate. Should be on the local file system or a base64 data URI.  
actions(optional)| | An array of objects representing manipulation options. Each object should have only one of the keys that corresponds to specific transformation.Default:`[]`  
saveOptions(optional)| | A map defining how modified image should be saved.Default:`{}`  
Manipulate the image provided via `uri`. Available modifications are rotating, flipping (mirroring), resizing and cropping. Each invocation results in a new file. With one invocation you can provide a set of actions to perform over the image. Overwriting the source file would not have an effect in displaying the result as images are cached.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
Promise which fulfils with [`ImageResult`](https://docs.expo.dev/versions/latest/sdk/imagemanipulator/#imageresult) object.
## Types
### `Action`
Android
iOS
Web
Literal Type: `union`
Acceptable values are:  |  |  |  | 
### `ActionCrop`
Android
iOS
Web
Property| Type| Description  
---|---|---  
crop| `{  height: number,   originX: number,   originY: number,   width: number }`| Fields specify top-left corner and dimensions of a crop rectangle.  
### `ActionExtent`
Android
iOS
Web
Property| Type| Description  
---|---|---  
extent| `{  backgroundColor: string | null,   height: number,   originX: number,   originY: number,   width: number }`| Only for: WebSet the image size and offset. If the image is enlarged, unfilled areas are set to the `backgroundColor`. To position the image, use `originX` and `originY`.  
### `ActionFlip`
Android
iOS
Web
Property| Type| Description  
---|---|---  
flip| | An axis on which image will be flipped. Only one flip per transformation is available. If you want to flip according to both axes then provide two separate transformations.  
### `ActionResize`
Android
iOS
Web
Property| Type| Description  
---|---|---  
resize| `{  height: number,   width: number }`| Values correspond to the result image dimensions. If you specify only one value, the other will be calculated automatically to preserve image ratio.  
### `ActionRotate`
Android
iOS
Web
Property| Type| Description  
---|---|---  
rotate| `number`| Degrees to rotate the image. Rotation is clockwise when the value is positive and counter-clockwise when negative.  
### `ImageResult`
Android
iOS
Web
Property| Type| Description  
---|---|---  
base64(optional)| `string`| It is included if the `base64` save option was truthy, and is a string containing the JPEG/PNG (depending on `format`) data of the image in Base64. Prepend that with `'data:image/xxx;base64,'` to get a data URI, which you can use as the source for an `Image` element for example (where `xxx` is `jpeg` or `png`).  
height| `number`| Height of the image or video.  
uri| `string`| An URI to the modified image (usable as the source for an `Image` or `Video` element).  
width| `number`| Width of the image or video.  
### `SaveOptions`
Android
iOS
Web
A map defining how modified image should be saved.
Property| Type| Description  
---|---|---  
base64(optional)| `boolean`| Whether to also include the image data in Base64 format.  
compress(optional)| `number`| A value in range `0.0` - `1.0` specifying compression level of the result image. `1` means no compression (highest quality) and `0` the highest compression (lowest quality).  
format(optional)| | Specifies what type of compression should be used and what is the result file extension. `SaveFormat.PNG` compression is lossless but slower, `SaveFormat.JPEG` is faster but the image has visible artifacts. Defaults to `SaveFormat.JPEG`  
## Enums
### `FlipType`
Android
iOS
Web
#### `Horizontal`
`FlipType.Horizontal ＝ "horizontal"`
#### `Vertical`
`FlipType.Vertical ＝ "vertical"`
### `SaveFormat`
Android
iOS
Web
#### `JPEG`
`SaveFormat.JPEG ＝ "jpeg"`
#### `PNG`
`SaveFormat.PNG ＝ "png"`
#### `WEBP`
`SaveFormat.WEBP ＝ "webp"`

