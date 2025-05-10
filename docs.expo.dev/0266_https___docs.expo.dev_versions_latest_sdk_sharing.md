---
url: https://docs.expo.dev/versions/latest/sdk/sharing
title: https://docs.expo.dev/versions/latest/sdk/sharing
date: 2025-04-30T17:17:28.205758
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo Sharing
A library that provides implementing sharing files.
Android
iOS
Web
Bundled version:
~13.0.1
`expo-sharing` allows you to share files directly with other compatible applications.
#### Sharing limitations on web
  * `expo-sharing` for web is built on top of the Web Share API, which still has [very limited browser support](https://caniuse.com/#feat=web-share). Be sure to check that the API can be used before calling it by using `Sharing.isAvailableAsync()`.
  * HTTPS required on web: The Web Share API is only available on web when the page is served over https. Run your app with `npx expo start --tunnel` to enable it.
  * No local file sharing on web: Sharing local files by URI works on Android and iOS, but not on web. You cannot share local files on web by URI — you will need to upload them somewhere and share that URI.


#### Sharing to your app from other apps
Currently `expo-sharing` only supports sharing _from your app to other apps_ and you cannot register to your app to have content shared to it through the native share dialog on native platforms. You can read more [in the related feature request](https://expo.canny.io/feature-requests/p/share-extension-ios-share-intent-android). You can setup this functionality manually in Xcode and Android Studio and create an [Expo Config Plugin](https://docs.expo.dev/config-plugins/introduction) to continue using [Expo Prebuild](https://docs.expo.dev/workflow/prebuild).
## Installation
Terminal
Copy
`- ``npx expo install expo-sharing`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## API
```
import * as Sharing from 'expo-sharing';

```

## Methods
### `Sharing.isAvailableAsync()`
Android
iOS
Web
Determine if the sharing API can be used in this app.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
A promise that fulfills with `true` if the sharing API can be used, and `false` otherwise.
### `Sharing.shareAsync(url, options)`
Android
iOS
Web
Parameter| Type| Description  
---|---|---  
url| `string`| Local file URL to share.  
options(optional)| `SharingOptions[](https://docs.expo.dev/versions/latest/sdk/sharing/#sharingoptions)`| A map of share options.Default:`{}`  
Opens action sheet to share file to different applications which can handle this type of file.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
## Types
### `SharingOptions`
Android
iOS
Web
Property| Type| Description  
---|---|---  
dialogTitle(optional)| `string`| Only for: AndroidWebSets share dialog title.  
mimeType(optional)| `string`| Only for: AndroidSets `mimeType` for `Intent`.  
UTI(optional)| `string`| Only for: iOS[Uniform Type Identifier](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_conc/understand_utis_conc.html)
  * the type of the target file.



