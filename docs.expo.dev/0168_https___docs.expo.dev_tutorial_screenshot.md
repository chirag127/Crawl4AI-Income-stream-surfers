---
url: https://docs.expo.dev/tutorial/screenshot
title: https://docs.expo.dev/tutorial/screenshot
date: 2025-04-30T17:15:11.800684
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Take a screenshot
In this tutorial, learn how to capture a screenshot using a third-party library and Expo Media Library.
In this chapter, we'll learn how to take a screenshot using a third-party library and save it on the device's media library. We'll use [`react-native-view-shot`](https://github.com/gre/react-native-view-shot) to take a screenshot and [`expo-media-library`](https://docs.expo.dev/versions/latest/sdk/media-library) to save an image on device's media library.
> So far, we have used third-party libraries, such as `react-native-gesture-handler`, `react-native-reanimated`. We can find hundreds of other third-party libraries on [React Native Directory](https://reactnative.directory/) depending on a use case.
[Watch: Taking screenshots in your universal Expo app](https://www.youtube.com/watch?v=Jft3_Yfr-p4)
1
## Install libraries
To install `react-native-view-shot` and `expo-media-library`, run the following commands:
Terminal
Copy
`- ``npx expo install react-native-view-shot expo-media-library`
2
## Prompt for permissions
An app that requires sensitive information, such as accessing a device's media library, has to prompt permission to allow or deny access. Using `usePermissions()` hook from `expo-media-library`, we can use the permission `status` and `requestPermission()` method to ask for access.
When the app loads for the first time and the permission status is neither granted nor denied, the value of the `status` is `null`. When asked for permission, a user can either grant the permission or deny it. We can add a condition to check if it is `null`, and if it is, trigger the `requestPermission()` method. After getting the access, the value of the `status` changes to `granted`.
Add the following code snippet inside the app/(tabs)/index.tsx:
app/(tabs)/index.tsx
Copy
```
import * as MediaLibrary from 'expo-media-library';
// ...rest of the code remains same
export default function Index() {
 const [status, requestPermission] = MediaLibrary.usePermissions();
 // ...rest of the code remains same
 if (status === null) {
  requestPermission();
 }
 // ...rest of the code remains same
}

```

3
## Create a ref to save the current view
We'll use `react-native-view-shot` to allow the user to take a screenshot within the app. This library captures the screenshot of a `<View>` as an image using the `captureRef()` method. It returns the URI of the captured screenshot image file.
  1. Import `captureRef` from `react-native-view-shot` and `useRef` from React.
  2. Create an `imageRef` reference variable to store the reference of the screenshot image captured.
  3. Wrap the `<ImageViewer>` and `<EmojiSticker>` components inside a `<View>` and then pass the reference variable to it.


app/(tabs)/index.tsx
Copy
```
import { useState, useRef } from 'react';
import { captureRef } from 'react-native-view-shot';
export default function Index() {
 const imageRef = useRef<View>(null);
 // ...rest of the code remains same
 return (
  <GestureHandlerRootView style={styles.container}><View style={styles.imageContainer}>
    <View ref={imageRef} collapsable={false}>
     <ImageViewer imgSource={PlaceholderImage} selectedImage={selectedImage} />{pickedEmoji && <EmojiSticker imageSize={40} stickerSource={pickedEmoji} />}
    </View>
   </View>{/* ...rest of the code remains same */}</GestureHandlerRootView>
 );
}

Show More

```

In the above snippet, the `collapsable` prop is set to `false`. This allows the `<View>` component to screenshot only of the background image and emoji sticker.
4
## Capture a screenshot and save it
We can capture a screenshot of the view by calling the `captureRef()` method from `react-native-view-shot` inside the `onSaveImageAsync()` function. It accepts an optional argument where we can pass the `width` and `height` of the screenshot capturing area. We can read more about available options in [the library's documentation](https://github.com/gre/react-native-view-shot#capturerefview-options-lower-level-imperative-api).
The `captureRef()` method also returns a promise that fulfills with the screenshot's URI. We will pass this URI as a parameter to [`MediaLibrary.saveToLibraryAsync()`](https://docs.expo.dev/versions/latest/sdk/media-library#medialibrarysavetolibraryasynclocaluri) and save the screenshot to the device's media library.
Inside app/(tabs)/index.tsx, update the `onSaveImageAsync()` function with the following code:
app/(tabs)/index.tsx
Copy
```
import { View, StyleSheet } from 'react-native';
import * as ImagePicker from 'expo-image-picker';
import { useState, useRef } from 'react';
import { GestureHandlerRootView } from 'react-native-gesture-handler';
import * as MediaLibrary from 'expo-media-library';
import { captureRef } from 'react-native-view-shot';
import { type ImageSource } from 'expo-image';
import Button from '@/components/Button';
import ImageViewer from '@/components/ImageViewer';
import IconButton from '@/components/IconButton';
import CircleButton from '@/components/CircleButton';
import EmojiPicker from '@/components/EmojiPicker';
import EmojiList from '@/components/EmojiList';
import EmojiSticker from '@/components/EmojiSticker';
const PlaceholderImage = require('@/assets/images/background-image.png');
export default function Index() {
 const [selectedImage, setSelectedImage] = useState<string | undefined>(undefined);
 const [showAppOptions, setShowAppOptions] = useState<boolean>(false);
 const [isModalVisible, setIsModalVisible] = useState<boolean>(false);
 const [pickedEmoji, setPickedEmoji] = useState<ImageSource | undefined>(undefined);
 const [status, requestPermission] = MediaLibrary.usePermissions();
 const imageRef = useRef<View>(null);
 if (status === null) {
  requestPermission();
 }
 const pickImageAsync = async () => {
  let result = await ImagePicker.launchImageLibraryAsync({
   mediaTypes: ['images'],
   allowsEditing: true,
   quality: 1,
  });
  if (!result.canceled) {
   setSelectedImage(result.assets[0].uri);
   setShowAppOptions(true);
  } else {
   alert('You did not select any image.');
  }
 };
 const onReset = () => {
  setShowAppOptions(false);
 };
 const onAddSticker = () => {
  setIsModalVisible(true);
 };
 const onModalClose = () => {
  setIsModalVisible(false);
 };
 const onSaveImageAsync = async () => {
  try {
   const localUri = await captureRef(imageRef, {
    height: 440,
    quality: 1,
   });
   await MediaLibrary.saveToLibraryAsync(localUri);
   if (localUri) {
    alert('Saved!');
   }
  } catch (e) {
   console.log(e);
  }
 };
 return (
  <GestureHandlerRootView style={styles.container}><View style={styles.imageContainer}><View ref={imageRef} collapsable={false}><ImageViewer imgSource={PlaceholderImage} selectedImage={selectedImage} />{pickedEmoji && <EmojiSticker imageSize={40} stickerSource={pickedEmoji} />}</View></View>{showAppOptions ? (
    <View style={styles.optionsContainer}><View style={styles.optionsRow}><IconButton icon="refresh" label="Reset" onPress={onReset} /><CircleButton onPress={onAddSticker} /><IconButton icon="save-alt" label="Save" onPress={onSaveImageAsync} /></View></View>
   ) : (
    <View style={styles.footerContainer}><Button theme="primary" label="Choose a photo" onPress={pickImageAsync} /><Button label="Use this photo" onPress={() => setShowAppOptions(true)} /></View>
   )}<EmojiPicker isVisible={isModalVisible} onClose={onModalClose}><EmojiList onSelect={setPickedEmoji} onCloseModal={onModalClose} /></EmojiPicker></GestureHandlerRootView>
 );
}
const styles = StyleSheet.create({
 container: {
  flex: 1,
  backgroundColor: '#25292e',
  alignItems: 'center',
 },
 imageContainer: {
  flex: 1,
 },
 footerContainer: {
  flex: 1 / 3,
  alignItems: 'center',
 },
 optionsContainer: {
  position: 'absolute',
  bottom: 80,
 },
 optionsRow: {
  alignItems: 'center',
  flexDirection: 'row',
 },
});

Show More

```

Now, choose a photo and add a sticker in the app. Then tap the "Save" button. We should see the following result on Android and iOS:
## Summary
Chapter 7: Take a screenshot
We've successfully used `react-native-view-shot` and `expo-media-library` to capture a screenshot and save it on the device's library.
Mark this chapter as read
In the next chapter, let's learn how to handle the differences between mobile and web platforms to implement the same functionality on web.
[Next: Handle platform differences](https://docs.expo.dev/tutorial/platform-differences)

