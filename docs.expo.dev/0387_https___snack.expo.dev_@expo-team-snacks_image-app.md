---
url: https://snack.expo.dev/@expo-team-snacks/image-app
title: https://snack.expo.dev/@expo-team-snacks/image-app
date: 2025-04-30T17:19:41.403102
depth: 2
---

# 
Image app 
This Snack provides the complete Expo tutorial example. 
Edit details
[Log in](https://expo.dev/login?redirect_uri=https%3A%2F%2Fsnack.expo.dev%2F%40expo-team-snacks%2Fimage-app%3FhideQueryParams%3Dtrue) to save your changes as you work
[Expo Docs](https://docs.expo.dev/versions/v52.0.0/)SavedRun on deviceDownload as zipShow embed code
#### Open files
  * ×
App.js


#### Project
assets
components
App.js
package.json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
import { useState, useRef } from'react';
import { StatusBar } from'expo-status-bar';
import { StyleSheet, View, Platform } from
'react-native';
import * as ImagePickerfrom'expo-image-picker';
import { GestureHandlerRootView } from
'react-native-gesture-handler';
import * as MediaLibraryfrom'expo-media-library';
import { captureRef } from'react-native-view-shot';
import domtoimage from'dom-to-image';
importButtonfrom'./components/Button';
importImageViewerfrom'./components/ImageViewer';
importCircleButtonfrom'./components/CircleButton';
importIconButtonfrom'./components/IconButton';
importEmojiPickerfrom'./components/EmojiPicker';
importEmojiListfrom'./components/EmojiList';
importEmojiStickerfrom'./components/EmojiSticker';
constPlaceholderImage = require('./assets/images/
background-image.png');
exportdefaultfunctionApp() {
const [isModalVisible, setIsModalVisible] = 
useState(false);
const [showAppOptions, setShowAppOptions] = 
useState(false);
Enter to Rename, Shift+Enter to Preview
My DeviceAndroidiOSWeb
package.json (4:5) 'expo-status-bar@~2.0.0' is not the recommended version for SDK 52.0.0. Update to ~2.0.1
Prettier
Editor
Expov48.0.0v49.0.0v50.0.0v51.0.0v52.0.0
Devices0
Preview

