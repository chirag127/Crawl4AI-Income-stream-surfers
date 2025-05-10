---
url: https://docs.expo.dev/versions/latest/sdk/live-photo
title: https://docs.expo.dev/versions/latest/sdk/live-photo
date: 2025-04-30T17:16:49.235691
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo LivePhoto
A library that allows displaying Live Photos on iOS.
iOS
## Installation
Terminal
Copy
`- ``npx expo install expo-live-photo`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Usage
Here's a simple example of `expo-live-photo` usage combined with `expo-image-picker`.
LivePhoto
```
import * as ImagePicker from 'expo-image-picker';
import { LivePhotoAsset, LivePhotoView, LivePhotoViewType } from 'expo-live-photo';
import { useRef, useState } from 'react';
import { View, StyleSheet, Text, Button } from 'react-native';
export default function LivePhotoScreen() {
 const viewRef = useRef<LivePhotoViewType>(null);
 const [livePhoto, setLivePhoto] = useState<LivePhotoAsset | null>(null);
 const pickImage = async () => {
  const result = await ImagePicker.launchImageLibraryAsync({
   mediaTypes: ['livePhotos'],
  });
  if (!result.canceled && result.assets[0].pairedVideoAsset?.uri) {
   setLivePhoto({
    photoUri: result.assets[0].uri,
    pairedVideoUri: result.assets[0].pairedVideoAsset.uri,
   });
  } else {
   console.error('Failed to pick a live photo');
  }
 };
 if (!LivePhotoView.isAvailable()) {
  return (
   <View style={styles.container}><Text>expo-live-photo is not available on this platform 😕</Text></View>
  );
 }
 return (
  <View style={styles.container}><LivePhotoView
    ref={viewRef}
    source={livePhoto}
    style={[styles.livePhotoView, { display: livePhoto ? 'flex' : 'none' }]}
    onLoadComplete={() => {
     console.log('Live photo loaded successfully!');
    }}
    onLoadError={error => {
     console.error('Failed to load the live photo: ', error.message);
    }}
   /><View style={livePhoto ? styles.pickImageCollapsed : styles.pickImageExpanded}><Button title={livePhoto ? 'Change Image' : 'Pick an image'} onPress={pickImage} /></View><Button title="Start Playback Hint" onPress={() => viewRef.current?.startPlayback('hint')} /><Button title="Start Playback" onPress={() => viewRef.current?.startPlayback('full')} /><Button title="Stop Playback" onPress={() => viewRef.current?.stopPlayback()} /></View>
 );
}
const styles = StyleSheet.create({
 container: {
  flex: 1,
  alignItems: 'center',
  paddingVertical: 20,
  paddingHorizontal: 40,
 },
 livePhotoView: {
  alignSelf: 'stretch',
  height: 300,
 },
 pickImageExpanded: {
  alignSelf: 'stretch',
  height: 300,
  justifyContent: 'center',
 },
 pickImageCollapsed: {
  marginVertical: 10,
 },
 button: {
  marginVertical: 10,
 },
});

Show More

```

## API
```
import { LivePhotoView } from 'expo-live-photo';

```

## Component
### `LivePhotoView`
iOS
Type: `React.Element[](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<LivePhotoViewProps[](https://docs.expo.dev/versions/latest/sdk/live-photo/#livephotoviewprops)>`
LivePhotoViewProps
### `contentFit`
iOS
Optional • Type: • Default: `'contain'`
Determines how the image should be scaled to fit the container.
  * `'contain'` - Scales the image so that its larger dimension fits the target size.
  * `'cover'` - Scales the image so that it completely fills the target size.


### `isMuted`
iOS
Optional • Type: `boolean` • Default: `true`
Determines whether the live photo should also play audio.
### `onLoadComplete`
iOS
Optional • Type: `() => void`
Called when the live photo is loaded and ready to play.
### `onLoadError`
iOS
Optional • Type: `(error: LivePhotoLoadError[](https://docs.expo.dev/versions/latest/sdk/live-photo/#livephotoloaderror)) => void`
Called when an error occurred while loading.
### `onLoadStart`
iOS
Optional • Type: `() => void`
Called when the live photo starts loading.
### `onPlaybackStart`
iOS
Optional • Type: `() => void`
Called when the playback starts.
### `onPlaybackStop`
iOS
Optional • Type: `() => void`
Called when the playback stops.
### `onPreviewPhotoLoad`
iOS
Optional • Type: `() => void`
Called when the live photo preview photo is loaded.
### `source`
iOS
Optional • Literal type: `union`
The live photo asset to display.
Acceptable values are: `null` | `LivePhotoAsset[](https://docs.expo.dev/versions/latest/sdk/live-photo/#livephotoasset)`
### `useDefaultGestureRecognizer`
iOS
Optional • Type: `boolean` • Default: `true`
Determines whether the default iOS gesture recognizer should be used. When `true` the playback will start if the user presses and holds on the `LivePhotoView`.
#### Inherited Props
  * 

## Component Methods
### `isAvailable()`
iOS
Determines whether the current device is capable of displaying live photos.
Returns:
`boolean`
## Interfaces
### `LivePhotoViewStatics`
iOS
LivePhotoViewStatics Methods
### `isAvailable()`
iOS
Determines whether the current device is capable of displaying live photos.
Returns:
`boolean`
## Types
### `ContentFit`
iOS
Literal Type: `string`
Determines how the image should be scaled to fit the container.
  * `'contain'` - Scales the image so that its larger dimension fits the target size.
  * `'cover'` - Scales the image so that it completely fills the target size.


Acceptable values are: `'contain'` | `'cover'`
### `LivePhotoAsset`
iOS
A live photo asset.
> Note: Due to native limitations, the photo and video parts of the live photo must come from a valid live photo file and be unaltered. When taken, the photo is paired with the video via metadata. If the pairing is broken, joining them into a live photo is impossible.
Property| Type| Description  
---|---|---  
pairedVideoUri| `string`| The URI of the video part of the live photo.  
photoUri| `string`| The URI of the photo part of the live photo.  
### `LivePhotoLoadError`
iOS
Property| Type| Description  
---|---|---  
message| `string`| Reason for the load failure.  
### `LivePhotoViewType`
iOS
Property| Type| Description  
---|---|---  
startPlayback| `(playbackStyle: PlaybackStyle[](https://docs.expo.dev/versions/latest/sdk/live-photo/#playbackstyle)) => void`| Start the playback of the video part of the live photo.`playbackStyle: PlaybackStyle[](https://docs.expo.dev/versions/latest/sdk/live-photo/#playbackstyle)`determines what (`PlaybackStyle`)[#playbackstyle] to use. If not provided, the full video will be played.  
stopPlayback| `() => void`| Stop the playback of the video part of the live photo.  
### `PlaybackStyle`
iOS
Literal Type: `string`
Determines what style to use when playing the live photo.
  * `'hint'` - A short part of the video will be played to indicate that a live photo is being displayed.
  * `'full'` - The full video part will be played.


Acceptable values are: `'hint'` | `'full'`

