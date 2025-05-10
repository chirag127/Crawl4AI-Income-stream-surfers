---
url: https://docs.expo.dev/versions/latest/sdk/media-library
title: https://docs.expo.dev/versions/latest/sdk/media-library
date: 2025-04-30T17:16:54.581071
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo MediaLibrary
A library that provides access to the device's media library.
Android
iOS
Bundled version:
~17.0.6
`expo-media-library` provides access to the user's media library, allowing them to access their existing images and videos from your app, as well as save new ones. You can also subscribe to any updates made to the user's media library.
> Android allows full access to the media library (which is the purpose of this package) only for applications needing broad access to photos. See [Details on Google Play's Photo and Video Permissions policy](https://support.google.com/googleplay/android-developer/answer/14115180).
## Installation
Terminal
Copy
`- ``npx expo install expo-media-library`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Configuration in app config
You can configure `expo-media-library` using its built-in [config plugin](https://docs.expo.dev/config-plugins/introduction) if you use config plugins in your project ([EAS Build](https://docs.expo.dev/build/introduction) or `npx expo run:[android|ios]`). The plugin allows you to configure various properties that cannot be set at runtime and require building a new app binary to take effect.
### Example app.json with config plugin
```
{
 "expo": {
  "plugins": [
   [
    "expo-media-library",
    {
     "photosPermission": "Allow $(PRODUCT_NAME) to access your photos.",
     "savePhotosPermission": "Allow $(PRODUCT_NAME) to save photos.",
     "isAccessMediaLocationEnabled": true
    }
   ]
  ]
 }
}

```

### Configurable properties
Name| Default| Description  
---|---|---  
`photosPermission`| `"Allow $(PRODUCT_NAME) to access your photos."`| Only for: iOSSets the iOS `NSPhotoLibraryUsageDescription` permission message in Info.plist.  
`savePhotosPermission`| `"Allow $(PRODUCT_NAME) to save photos."`| Only for: iOSSets the iOS `NSPhotoLibraryAddUsageDescription` permission message in Info.plist.  
`isAccessMediaLocationEnabled`| `false`| Only for: AndroidSets whether or not to request the `ACCESS_MEDIA_LOCATION` permission on Android.  
Are you using this library in an existing React Native app?
If you're not using Continuous Native Generation ([CNG](https://docs.expo.dev/workflow/continuous-native-generation)) or you're using native android ios projects manually, then you need to add following permissions and configuration to your native projects:
Android
  * To access asset location (latitude and longitude EXIF tags), add `ACCESS_MEDIA_LOCATION` permission to your project's android/app/src/main/AndroidManifest.xml:
```
<uses-permission android:name="android.permission.ACCESS_MEDIA_LOCATION" />

```

  * [Scoped storage](https://developer.android.com/training/data-storage#scoped-storage) is available from Android 10. To make `expo-media-library` work with scoped storage, you need to add the following configuration to your android/app/src/main/AndroidManifest.xml:
```
<manifest ... >
 <application android:requestLegacyExternalStorage="true" ...>
</manifest>

```



iOS
  * Add `NSPhotoLibraryUsageDescription`, and `NSPhotoLibraryAddUsageDescription` keys to your project's ios/[app]/Info.plist:
```
<key>NSPhotoLibraryUsageDescription</key>
<string>Give $(PRODUCT_NAME) permission to access your photos</string>
<key>NSPhotoLibraryAddUsageDescription</key>
<string>Give $(PRODUCT_NAME) permission to save photos</string>

```



## Usage
Fetching albums and displaying assets
```
import { useState, useEffect } from 'react';
import { Button, Text, SafeAreaView, ScrollView, StyleSheet, Image, View, Platform } from 'react-native';
import * as MediaLibrary from 'expo-media-library';
export default function App() {
 const [albums, setAlbums] = useState(null);
 const [permissionResponse, requestPermission] = MediaLibrary.usePermissions();
 async function getAlbums() {
  if (permissionResponse.status !== 'granted') {
   await requestPermission();
  }
  const fetchedAlbums = await MediaLibrary.getAlbumsAsync({
   includeSmartAlbums: true,
  });
  setAlbums(fetchedAlbums);
 }
 return (
  <SafeAreaView style={styles.container}><Button onPress={getAlbums} title="Get albums" /><ScrollView>{albums && albums.map((album) => <AlbumEntry album={album} />)}</ScrollView></SafeAreaView>
 );
}
function AlbumEntry({ album }) {
 const [assets, setAssets] = useState([]);
 useEffect(() => {
  async function getAlbumAssets() {
   const albumAssets = await MediaLibrary.getAssetsAsync({ album });
   setAssets(albumAssets.assets);
  }
  getAlbumAssets();
 }, [album]);
 return (
  <View key={album.id} style={styles.albumContainer}><Text>{album.title} - {album.assetCount ?? 'no'} assets
   </Text><View style={styles.albumAssetsContainer}>{assets && assets.map((asset) => (
     <Image source={{ uri: asset.uri }} width={50} height={50} />
    ))}</View></View>
 );
}
%%placeholder-start%%const styles = StyleSheet.create({ ... }); %%placeholder-end%%const styles = StyleSheet.create({
 container: {
  flex: 1,
  gap: 8,
  justifyContent: 'center',
  ...Platform.select({
   android: {
    paddingTop: 40,
   },
  }),
 },
 albumContainer: {
  paddingHorizontal: 20,
  marginBottom: 12,
  gap: 4,
 },
 albumAssetsContainer: {
  flexDirection: 'row',
  flexWrap: 'wrap',
 },
});

Show More

```

## API
```
import * as MediaLibrary from 'expo-media-library';

```

## Component
### `getAlbumsAsync`
Android
iOS
Type: `React.Element[](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<AlbumsOptions[](https://docs.expo.dev/versions/latest/sdk/media-library/#albumsoptions)>`
Queries for user-created albums in media gallery.
## Constants
### `MediaLibrary.MediaType`
Android
iOS
Type: `MediaTypeObject[](https://docs.expo.dev/versions/latest/sdk/media-library/#mediatypeobject)`
Possible media types.
### `MediaLibrary.SortBy`
Android
iOS
Type: 
Supported keys that can be used to sort `getAssetsAsync` results.
## Hooks
### `usePermissions(options)`
Android
iOS
Parameter| Type  
---|---  
options(optional)| `PermissionHookOptions[](https://docs.expo.dev/versions/latest/sdk/media-library/#permissionhookoptions)<{  granularPermissions: GranularPermission[][](https://docs.expo.dev/versions/latest/sdk/media-library/#granularpermission),   writeOnly: boolean }>`  
Check or request permissions to access the media library. This uses both `requestPermissionsAsync` and `getPermissionsAsync` to interact with the permissions.
Returns:
`[null | PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/media-library/#permissionresponse), RequestPermissionMethod<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/media-library/#permissionresponse)>, GetPermissionMethod<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/media-library/#permissionresponse)>]`
Example
```
const [permissionResponse, requestPermission] = MediaLibrary.usePermissions();

```

## Methods
### `MediaLibrary.addAssetsToAlbumAsync(assets, album, copy)`
Android
iOS
Parameter| Type| Description  
---|---|---  
assets| ``| An array of [Asset](https://docs.expo.dev/versions/latest/sdk/media-library/#asset) or their IDs.  
album| | An [Album](https://docs.expo.dev/versions/latest/sdk/media-library/#album) or its ID.  
copy(optional)| `boolean`| Android only. Whether to copy assets to the new album instead of move them. Defaults to `true`.Default:`true`  
Adds array of assets to the album.
On Android, by default it copies assets from the current album to provided one, however it's also possible to move them by passing `false` as `copyAssets` argument. In case they're copied you should keep in mind that `getAssetsAsync` will return duplicated assets.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
Returns promise which fulfils with `true` if the assets were successfully added to the album.
### `MediaLibrary.albumNeedsMigrationAsync(album)`
Android
iOS
Parameter| Type| Description  
---|---|---  
album| | An [Album](https://docs.expo.dev/versions/latest/sdk/media-library/#album) or its ID.  
Checks if the album should be migrated to a different location. In other words, it checks if the application has the write permission to the album folder. If not, it returns `true`, otherwise `false`.
> Note: For Android below R, web or iOS, this function always returns `false`.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
Returns a promise which fulfils with `true` if the album should be migrated.
### `MediaLibrary.createAlbumAsync(albumName, asset, copyAsset)`
Android
iOS
Parameter| Type| Description  
---|---|---  
albumName| `string`| Name of the album to create.  
asset(optional)| | An [Asset](https://docs.expo.dev/versions/latest/sdk/media-library/#asset) or its ID (required on Android).  
copyAsset(optional)| `boolean`| Android Only. Whether to copy asset to the new album instead of move it. Defaults to `true`.Default:`true`  
Creates an album with given name and initial asset. The asset parameter is required on Android, since it's not possible to create empty album on this platform. On Android, by default it copies given asset from the current album to the new one, however it's also possible to move it by passing `false` as `copyAsset` argument. In case it's copied you should keep in mind that `getAssetsAsync` will return duplicated asset.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
Newly created [`Album`](https://docs.expo.dev/versions/latest/sdk/media-library/#album).
### `MediaLibrary.createAssetAsync(localUri)`
Android
iOS
Parameter| Type| Description  
---|---|---  
localUri| `string`| A URI to the image or video file. It must contain an extension. On Android it must be a local path, so it must start with `file:///`  
Creates an asset from existing file. The most common use case is to save a picture taken by [Camera](https://docs.expo.dev/versions/latest/sdk/camera). This method requires `CAMERA_ROLL` permission.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
A promise which fulfils with an object representing an [`Asset`](https://docs.expo.dev/versions/latest/sdk/media-library/#asset).
Example
```
const { uri } = await Camera.takePictureAsync();
const asset = await MediaLibrary.createAssetAsync(uri);

```

### `MediaLibrary.deleteAlbumsAsync(albums, assetRemove)`
Android
iOS
Parameter| Type| Description  
---|---|---  
albums| ``| An array of [`Album`](https://docs.expo.dev/versions/latest/sdk/media-library/#asset)s or their IDs.  
assetRemove(optional)| `boolean`| iOS Only. Whether to also delete assets belonging to given albums. Defaults to `false`.Default:`false`  
Deletes given albums from the library. On Android by default it deletes assets belonging to given albums from the library. On iOS it doesn't delete these assets, however it's possible to do by passing `true` as `deleteAssets`.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
Returns a promise which fulfils with `true` if the albums were successfully deleted from the library.
### `MediaLibrary.deleteAssetsAsync(assets)`
Android
iOS
Parameter| Type| Description  
---|---|---  
assets| ``| An array of [Asset](https://docs.expo.dev/versions/latest/sdk/media-library/#asset) or their IDs.  
Deletes assets from the library. On iOS it deletes assets from all albums they belong to, while on Android it keeps all copies of them (album is strictly connected to the asset). Also, there is additional dialog on iOS that requires user to confirm this action.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
Returns promise which fulfils with `true` if the assets were successfully deleted.
### `MediaLibrary.getAlbumAsync(title)`
Android
iOS
Parameter| Type| Description  
---|---|---  
title| `string`| Name of the album to look for.  
Queries for an album with a specific name.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
An object representing an [`Album`](https://docs.expo.dev/versions/latest/sdk/media-library/#album), if album with given name exists, otherwise returns `null`.
### `MediaLibrary.getAssetInfoAsync(asset, options)`
Android
iOS
Parameter| Type| Description  
---|---|---  
asset| | An [Asset](https://docs.expo.dev/versions/latest/sdk/media-library/#asset) or its ID.  
options(optional)| `MediaLibraryAssetInfoQueryOptions[](https://docs.expo.dev/versions/latest/sdk/media-library/#medialibraryassetinfoqueryoptions)`  
Provides more information about an asset, including GPS location, local URI and EXIF metadata.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
An [AssetInfo](https://docs.expo.dev/versions/latest/sdk/media-library/#assetinfo) object, which is an `Asset` extended by an additional fields.
### `MediaLibrary.getAssetsAsync(assetsOptions)`
Android
iOS
Parameter| Type  
---|---  
assetsOptions(optional)| `AssetsOptions[](https://docs.expo.dev/versions/latest/sdk/media-library/#assetsoptions)`  
Fetches a page of assets matching the provided criteria.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PagedInfo[](https://docs.expo.dev/versions/latest/sdk/media-library/#pagedinfo)<>>`
A promise that fulfils with to [`PagedInfo`](https://docs.expo.dev/versions/latest/sdk/media-library/#pagedinfo) object with array of [`Asset`](https://docs.expo.dev/versions/latest/sdk/media-library/#asset)s.
### `MediaLibrary.getMomentsAsync()`
iOS
Fetches a list of moments, which is a group of assets taken around the same place and time.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<any>`
An array of [albums](https://docs.expo.dev/versions/latest/sdk/media-library/#album) whose type is `moment`.
### `MediaLibrary.getPermissionsAsync(writeOnly, granularPermissions)`
Android
iOS
Parameter| Type| Description  
---|---|---  
writeOnly(optional)| `boolean`  
granularPermissions(optional)| `GranularPermission[][](https://docs.expo.dev/versions/latest/sdk/media-library/#granularpermission)`| A list of [`GranularPermission`](https://docs.expo.dev/versions/latest/sdk/media-library/#granularpermission) values. This parameter has an effect only on Android 13 and newer. By default, `expo-media-library` will ask for all possible permissions.  
Checks user's permissions for accessing media library.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/media-library/#permissionresponse)>`
A promise that fulfils with [`PermissionResponse`](https://docs.expo.dev/versions/latest/sdk/media-library/#permissionresponse) object.
### `MediaLibrary.isAvailableAsync()`
Android
iOS
Returns whether the Media Library API is enabled on the current device.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
A promise which fulfils with a `boolean`, indicating whether the Media Library API is available on the current device.
### `MediaLibrary.migrateAlbumIfNeededAsync(album)`
Android
iOS
Parameter| Type| Description  
---|---|---  
album| | An [Album](https://docs.expo.dev/versions/latest/sdk/media-library/#album) or its ID.  
Moves album content to the special media directories on Android R or above if needed. Those new locations are in line with the Android `scoped storage` - so your application won't lose write permission to those directories in the future.
This method does nothing if:
  * app is running on iOS, web or Android below R
  * app has write permission to the album folder


The migration is possible when the album contains only compatible files types. For instance, movies and pictures are compatible with each other, but music and pictures are not. If automatic migration isn't possible, the function rejects. In that case, you can use methods from the `expo-file-system` to migrate all your files manually.
#### Why do you need to migrate files?
Android R introduced a lot of changes in the storage system. Now applications can't save anything to the root directory. The only available locations are from the `MediaStore` API. Unfortunately, the media library stored albums in folders for which, because of those changes, the application doesn't have permissions anymore. However, it doesn't mean you need to migrate all your albums. If your application doesn't add assets to albums, you don't have to migrate. Everything will work as it used to. You can read more about scoped storage in [the Android documentation](https://developer.android.com/about/versions/11/privacy/storage).
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
A promise which fulfils to `void`.
### `MediaLibrary.presentPermissionsPickerAsync(mediaTypes)`
Android 14+
iOS
Parameter| Type| Description  
---|---|---  
mediaTypes(optional)| `MediaTypeFilter[][](https://docs.expo.dev/versions/latest/sdk/media-library/#mediatypefilter)`| Limits the type(s) of media that the user will be granting access to. By default, a list that shows both photos and videos is presented.  
Allows the user to update the assets that your app has access to. The system modal is only displayed if the user originally allowed only `limited` access to their media library, otherwise this method is a no-op.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
A promise that either rejects if the method is unavailable, or resolves to `void`.
> Note: This method doesn't inform you if the user changes which assets your app has access to. That information is only exposed by iOS, and to obtain it, you need to subscribe for updates to the user's media library using [`addListener()`](https://docs.expo.dev/versions/latest/sdk/media-library/#medialibraryaddlistenerlistener). If `hasIncrementalChanges` is `false`, the user changed their permissions.
### `MediaLibrary.removeAssetsFromAlbumAsync(assets, album)`
Android
iOS
Parameter| Type| Description  
---|---|---  
assets| ``| An array of [Asset](https://docs.expo.dev/versions/latest/sdk/media-library/#asset) or their IDs.  
album| | An [Album](https://docs.expo.dev/versions/latest/sdk/media-library/#album) or its ID.  
Removes given assets from album.
On Android, album will be automatically deleted if there are no more assets inside.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
Returns promise which fulfils with `true` if the assets were successfully removed from the album.
### `MediaLibrary.removeSubscription(subscription)`
Android
iOS
Parameter| Type  
---|---  
subscription| `EventSubscription`  
Returns:
`void`
### `MediaLibrary.requestPermissionsAsync(writeOnly, granularPermissions)`
Android
iOS
Parameter| Type| Description  
---|---|---  
writeOnly(optional)| `boolean`  
granularPermissions(optional)| `GranularPermission[][](https://docs.expo.dev/versions/latest/sdk/media-library/#granularpermission)`| A list of [`GranularPermission`](https://docs.expo.dev/versions/latest/sdk/media-library/#granularpermission) values. This parameter has an effect only on Android 13 and newer. By default, `expo-media-library` will ask for all possible permissions.  
Asks the user to grant permissions for accessing media in user's media library.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/media-library/#permissionresponse)>`
A promise that fulfils with [`PermissionResponse`](https://docs.expo.dev/versions/latest/sdk/media-library/#permissionresponse) object.
### `MediaLibrary.saveToLibraryAsync(localUri)`
Android
iOS
Parameter| Type| Description  
---|---|---  
localUri| `string`| A URI to the image or video file. It must contain an extension. On Android it must be a local path, so it must start with `file:///`.  
Saves the file at given `localUri` to the user's media library. Unlike [`createAssetAsync()`](https://docs.expo.dev/versions/latest/sdk/media-library/#medialibrarycreateassetasynclocaluri), This method doesn't return created asset. On iOS 11+, it's possible to use this method without asking for `CAMERA_ROLL` permission, however then yours `Info.plist` should have `NSPhotoLibraryAddUsageDescription` key.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
## Event Subscriptions
### `MediaLibrary.addListener(listener)`
Android
iOS
Parameter| Type| Description  
---|---|---  
listener| `(event: MediaLibraryAssetsChangeEvent[](https://docs.expo.dev/versions/latest/sdk/media-library/#medialibraryassetschangeevent)) => void`| A callback that is fired when any assets have been inserted or deleted from the library. On Android it's invoked with an empty object. On iOS, it's invoked with [`MediaLibraryAssetsChangeEvent`](https://docs.expo.dev/versions/latest/sdk/media-library/#medialibraryassetschangeevent) object. Additionally, only on iOS, the listener is also invoked when the user changes access to individual assets in the media library using `presentPermissionsPickerAsync()`.  
Subscribes for updates in user's media library.
Returns:
`EventSubscription`
An [`Subscription`](https://docs.expo.dev/versions/latest/sdk/media-library/#subscription) object that you can call `remove()` on when you would like to unsubscribe the listener.
### `MediaLibrary.removeAllListeners()`
Android
iOS
Removes all listeners.
Returns:
`void`
## Interfaces
### `EXPermissionResponse`
Android
iOS
An object obtained by permissions get and request functions.
Property| Type| Description  
---|---|---  
canAskAgain| `boolean`| Indicates if user can be asked again for specific permission. If not, one should be directed to the Settings app in order to enable/disable the permission.  
expires| `PermissionExpiration[](https://docs.expo.dev/versions/latest/sdk/media-library/#permissionexpiration)`| Determines time when the permission expires.  
granted| `boolean`| A convenience boolean that indicates if the permission is granted.  
status| `PermissionStatus[](https://docs.expo.dev/versions/latest/sdk/media-library/#permissionstatus)`| Determines the status of the permission.  
## Types
### `Album`
Android
iOS
Property| Type| Description  
---|---|---  
approximateLocation(optional)| | Only for: iOSApply only to albums whose type is `'moment'`. Approximated location of all assets in the moment.  
assetCount| `number`| Estimated number of assets in the album.  
endTime| `number`| Only for: iOSApply only to albums whose type is `'moment'`. Latest creation timestamp of all assets in the moment.  
id| `string`| Album ID.  
locationNames(optional)| `string[]`| Only for: iOSApply only to albums whose type is `'moment'`. Names of locations grouped in the moment.  
startTime| `number`| Only for: iOSApply only to albums whose type is `'moment'`. Earliest creation timestamp of all assets in the moment.  
title| `string`| Album title.  
type(optional)| | Only for: iOSThe type of the assets album.  
### `AlbumRef`
Android
iOS
Literal Type: `union`
Acceptable values are:  | `string`
### `AlbumsOptions`
Android
iOS
Property| Type| Description  
---|---|---  
includeSmartAlbums(optional)| `boolean`  
### `AlbumType`
Android
iOS
Literal Type: `string`
Acceptable values are: `'album'` | `'moment'` | `'smartAlbum'`
### `Asset`
Android
iOS
Property| Type| Description  
---|---|---  
albumId(optional)| `string`| Only for: AndroidAlbum ID that the asset belongs to.  
creationTime| `number`| File creation timestamp.  
duration| `number`| Duration of the video or audio asset in seconds.  
filename| `string`| Filename of the asset.  
height| `number`| Height of the image or video.  
id| `string`| Internal ID that represents an asset.  
mediaSubtypes(optional)| `MediaSubtype[][](https://docs.expo.dev/versions/latest/sdk/media-library/#mediasubtype)`| Only for: iOSAn array of media subtypes.  
mediaType| `MediaTypeValue[](https://docs.expo.dev/versions/latest/sdk/media-library/#mediatypevalue)`| Media type.  
modificationTime| `number`| Last modification timestamp.  
uri| `string`| URI that points to the asset. `ph://*` (iOS), `file://*` (Android)  
width| `number`| Width of the image or video.  
### `AssetInfo`
Android
iOS
Type: extended by:
Property| Type| Description  
---|---|---  
exif(optional)| `object`| EXIF metadata associated with the image.  
isFavorite(optional)| `boolean`| Only for: iOSWhether the asset is marked as favorite.  
isNetworkAsset(optional)| `boolean`| Only for: iOSThis field is available only if flag `shouldDownloadFromNetwork` is set to `false`. Whether the asset is stored on the network (iCloud on iOS).  
localUri(optional)| `string`| Local URI for the asset.  
location(optional)| | GPS location if available.  
orientation(optional)| `number`| Only for: iOSDisplay orientation of the image. Orientation is available only for assets whose `mediaType` is `MediaType.photo`. Value will range from 1 to 8, see [EXIF orientation specification](http://sylvana.net/jpegcrop/exif_orientation.html) for more details.  
### `AssetRef`
Android
iOS
Literal Type: `union`
Acceptable values are:  | `string`
### `AssetsOptions`
Android
iOS
Property| Type| Description  
---|---|---  
after(optional)| | Asset ID of the last item returned on the previous page. To get the ID of the next page, pass [`endCursor`](https://docs.expo.dev/versions/latest/sdk/media-library/#pagedinfo) as its value.  
album(optional)| | [Album](https://docs.expo.dev/versions/latest/sdk/media-library/#album) or its ID to get assets from specific album.  
createdAfter(optional)| `number`| `Date` object or Unix timestamp in milliseconds limiting returned assets only to those that were created after this date.  
createdBefore(optional)| `number`| Similarly as `createdAfter`, but limits assets only to those that were created before specified date.  
first(optional)| `number`| The maximum number of items on a single page.Default:`20`  
mediaType(optional)| ``| An array of [MediaTypeValue](https://docs.expo.dev/versions/latest/sdk/media-library/#mediatypevalue)s or a single `MediaTypeValue`.Default:`MediaType.photo`  
sortBy(optional)| ``| An array of [`SortByValue`](https://docs.expo.dev/versions/latest/sdk/media-library/#sortbyvalue)s or a single `SortByValue` value. By default, all keys are sorted in descending order, however you can also pass a pair `[key, ascending]` where the second item is a `boolean` value that means whether to use ascending order. Note that if the `SortBy.default` key is used, then `ascending` argument will not matter. Earlier items have higher priority when sorting out the results. If empty, this method uses the default sorting that is provided by the platform.  
### `GranularPermission`
Android 13+
Literal Type: `string`
Determines the type of media that the app will ask the OS to get access to.
Acceptable values are: `'audio'` | `'photo'` | `'video'`
### `Location`
Android
iOS
Property| Type| Description  
---|---|---  
latitude| `number`  
longitude| `number`  
### `MediaLibraryAssetInfoQueryOptions`
Android
iOS
Property| Type| Description  
---|---|---  
shouldDownloadFromNetwork(optional)| `boolean`| Whether allow the asset to be downloaded from network. Only available in iOS with iCloud assets.Default:`true`  
### `MediaLibraryAssetsChangeEvent`
Android
iOS
Property| Type| Description  
---|---|---  
deletedAssets(optional)| | Available only if `hasIncrementalChanges` is `true`. Array of [`Asset`](https://docs.expo.dev/versions/latest/sdk/media-library/#asset)s that have been deleted from the library.  
hasIncrementalChanges| `boolean`| Whether the media library's changes could be described as "incremental changes". `true` indicates the changes are described by the `insertedAssets`, `deletedAssets` and `updatedAssets` values. `false` indicates that the scope of changes is too large and you should perform a full assets reload (eg. a user has changed access to individual assets in the media library).  
insertedAssets(optional)| | Available only if `hasIncrementalChanges` is `true`. Array of [`Asset`](https://docs.expo.dev/versions/latest/sdk/media-library/#asset)s that have been inserted to the library.  
updatedAssets(optional)| | Available only if `hasIncrementalChanges` is `true`. Array of [`Asset`](https://docs.expo.dev/versions/latest/sdk/media-library/#asset)s that have been updated or completed downloading from network storage (iCloud on iOS).  
### `MediaSubtype`
Android
iOS
Literal Type: `string`
Constants identifying specific variations of asset media, such as panorama or screenshot photos, and time-lapse or high-frame-rate video. Maps to [these values](https://developer.apple.com/documentation/photokit/phassetmediasubtype#1603888).
Acceptable values are: `'depthEffect'` | `'hdr'` | `'highFrameRate'` | `'livePhoto'` | `'panorama'` | `'screenshot'` | `'stream'` | `'timelapse'`
### `MediaTypeFilter`
Android 14+
Literal Type: `string`
Represents the possible types of media that the app will ask the OS to get access to when calling [`presentPermissionsPickerAsync()`](https://docs.expo.dev/versions/latest/sdk/media-library/#medialibrarypresentpermissionspickerasyncmediatypes).
Acceptable values are: `'photo'` | `'video'`
### `MediaTypeObject`
Android
iOS
Property| Type| Description  
---|---|---  
audio| `'audio'`  
photo| `'photo'`  
unknown| `'unknown'`  
video| `'video'`  
### `MediaTypeValue`
Android
iOS
Literal Type: `string`
Acceptable values are: `'audio'` | `'photo'` | `'video'` | `'unknown'`
### `PagedInfo`
Android
iOS
Property| Type| Description  
---|---|---  
assets| `T[]`| A page of [`Asset`](https://docs.expo.dev/versions/latest/sdk/media-library/#asset)s fetched by the query.  
endCursor| `string`| ID of the last fetched asset. It should be passed as `after` option in order to get the next page.  
hasNextPage| `boolean`| Whether there are more assets to fetch.  
totalCount| `number`| Estimated total number of assets that match the query.  
### `PermissionExpiration`
Android
iOS
Literal Type: `union`
Permission expiration time. Currently, all permissions are granted permanently.
Acceptable values are: `'never'` | `number`
### `PermissionHookOptions`
Android
iOS
Literal Type: `union`
Acceptable values are: `PermissionHookBehavior` | `Options`
### `PermissionResponse`
Android
iOS
Type: `EXPermissionResponse[](https://docs.expo.dev/versions/latest/sdk/media-library/#expermissionresponse)` extended by:
Property| Type| Description  
---|---|---  
accessPrivileges(optional)| `'all' | 'limited' | 'none'`| Indicates if your app has access to the whole or only part of the photo library. Possible values are:
  * `'all'` if the user granted your app access to the whole photo library
  * `'limited'` if the user granted your app access only to selected photos (only available on Android API 14+ and iOS 14.0+)
  * `'none'` if user denied or hasn't yet granted the permission

  
### `SortByKey`
Android
iOS
Literal Type: `string`
Acceptable values are: `'default'` | `'mediaType'` | `'width'` | `'height'` | `'creationTime'` | `'modificationTime'` | `'duration'`
### `SortByObject`
Android
iOS
Property| Type| Description  
---|---|---  
creationTime| `'creationTime'`  
default| `'default'`  
duration| `'duration'`  
height| `'height'`  
mediaType| `'mediaType'`  
modificationTime| `'modificationTime'`  
width| `'width'`  
### `SortByValue`
Android
iOS
Literal Type: `union`
Acceptable values are: `[boolean]` | 
### `Subscription`
Android
iOS
A subscription object that allows to conveniently remove an event listener from the emitter.
Property| Type| Description  
---|---|---  
remove| `() => void`| Removes an event listener for which the subscription has been created. After calling this function, the listener will no longer receive any events from the emitter.  
## Enums
### `PermissionStatus`
Android
iOS
#### `DENIED`
`PermissionStatus.DENIED ＝ "denied"`
User has denied the permission.
#### `GRANTED`
`PermissionStatus.GRANTED ＝ "granted"`
User has granted the permission.
#### `UNDETERMINED`
`PermissionStatus.UNDETERMINED ＝ "undetermined"`
User hasn't granted or denied the permission yet.
## Permissions
### Android
The following permissions are added automatically through this library's AndroidManifest.xml:
Android Permission| Description  
---|---  
`READ_EXTERNAL_STORAGE`| Allows an application to read from external storage.  
`WRITE_EXTERNAL_STORAGE`| Allows an application to write to external storage.  
`READ_MEDIA_IMAGES`| Allows an application to read image files from external storage.  
`READ_MEDIA_VIDEO`| Allows an application to read video files from external storage.  
`READ_MEDIA_AUDIO`| Allows an application to read audio files from external storage.  
`READ_MEDIA_VISUAL_USER_SELECTED`| Allows an application to read image or video files from external storage that a user has selected via the permission prompt photo picker.
> Apps can check this permission to verify that a user has decided to use the photo picker, instead of granting access to or . It does not prevent apps from accessing the standard photo picker manually. This permission should be requested alongside and/or , depending on which type of media is desired.  
### iOS
The following usage description keys are used by this library:
Info.plist Key| Description  
---|---  
`NSPhotoLibraryUsageDescription`| A message that tells the user why the app is requesting access to the user’s photo library.  
`NSPhotoLibraryAddUsageDescription`| A message that tells the user why the app is requesting add-only access to the user’s photo library.

