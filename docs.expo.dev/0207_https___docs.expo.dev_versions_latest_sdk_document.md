---
url: https://docs.expo.dev/versions/latest/sdk/document-picker
title: https://docs.expo.dev/versions/latest/sdk/document-picker
date: 2025-04-30T17:16:13.099251
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo DocumentPicker
A library that provides access to the system's UI for selecting documents from the available providers on the user's device.
Android
iOS
Web
Bundled version:
~13.0.3
`expo-document-picker` provides access to the system's UI for selecting documents from the available providers on the user's device.
## Installation
Terminal
Copy
`- ``npx expo install expo-document-picker`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Configuration in app config
You can configure `expo-document-picker` using its built-in [config plugin](https://docs.expo.dev/config-plugins/introduction) if you use config plugins in your project ([EAS Build](https://docs.expo.dev/build/introduction) or `npx expo run:[android|ios]`). The plugin allows you to configure various properties that cannot be set at runtime and require building a new app binary to take effect. If your app does not use EAS Build, then you'll need to manually configure the package.
### Example app.json with config plugin
If you want to enable [iCloud storage features](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_developer_icloud-services), set the `expo.ios.usesIcloudStorage` key to `true` in the [app config](https://docs.expo.dev/workflow/configuration) file as specified [configuration properties](https://docs.expo.dev/versions/latest/config/app#usesicloudstorage).
Running [EAS Build](https://docs.expo.dev/build/introduction) locally will use [iOS capabilities signing](https://docs.expo.dev/build-reference/ios-capabilities) to enable the required capabilities before building.
app.json
Copy
```
{
 "expo": {
  "plugins": [
   [
    "expo-document-picker",
    {
     "iCloudContainerEnvironment": "Production"
    }
   ]
  ]
 }
}

```

### Configurable properties
Name| Default| Description  
---|---|---  
`iCloudContainerEnvironment`| `undefined`| Only for: iOSSets the iOS `com.apple.developer.icloud-container-environment` entitlement used for AdHoc iOS builds. Possible values: `Development`, `Production`. [Learn more](https://github.com/expo/eas-cli/issues/693).  
`kvStoreIdentifier`| `undefined`| Only for: iOSOverrides the default iOS `com.apple.developer.ubiquity-kvstore-identifier` entitlement, which uses your Apple Team ID and bundle identifier. This may be needed if your app was transferred to another Apple Team after enabling iCloud storage.  
Are you using this library in an existing React Native app?
Apps that don't use [EAS Build](https://docs.expo.dev/build/introduction) and want [iCloud storage features](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_developer_icloud-services) must [manually configure](https://docs.expo.dev/build-reference/ios-capabilities#manual-setup) the [iCloud service with CloudKit support](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_developer_icloud-container-environment) for their bundle identifier.
If you enable the iCloud capability through the [Apple Developer Console](https://docs.expo.dev/build-reference/ios-capabilities#apple-developer-console), then be sure to add the following entitlements in your `ios/[app]/[app].entitlements` file (where `dev.expo.my-app` if your bundle identifier):
```
<key>com.apple.developer.icloud-container-identifiers</key>
<array>
  <string>iCloud.dev.expo.my-app</string>
</array>
<key>com.apple.developer.icloud-services</key>
<array>
  <string>CloudDocuments</string>
</array>
<key>com.apple.developer.ubiquity-container-identifiers</key>
<array>
  <string>iCloud.dev.expo.my-app</string>
</array>
<key>com.apple.developer.ubiquity-kvstore-identifier</key>
<string>$(TeamIdentifierPrefix)dev.expo.my-app</string>

```

Apple Developer Console also requires an iCloud Container to be created. When registering the new container, you are asked to provide a description and identifier for the container. You may enter any name under the description. Under the identifier, add `iCloud.<your_bundle_identifier>` (same value used for `com.apple.developer.icloud-container-identifiers` and `com.apple.developer.ubiquity-container-identifiers` entitlements).
## Using with `expo-file-system`
When using `expo-document-picker` with [`expo-file-system`](https://docs.expo.dev/versions/latest/sdk/filesystem), it's not always possible for the file system to read the file immediately after the `expo-document-picker` picks it.
To allow the `expo-file-system` to read the file immediately after it is picked, you'll need to ensure that the [`copyToCacheDirectory`](https://docs.expo.dev/versions/latest/sdk/document-picker#documentpickeroptions) option is set to `true`.
## API
```
import * as DocumentPicker from 'expo-document-picker';

```

## Component
### `getDocumentAsync`
Android
iOS
Web
Type: `React.Element[](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<DocumentPickerOptions[](https://docs.expo.dev/versions/latest/sdk/document-picker/#documentpickeroptions)>`
Display the system UI for choosing a document. By default, the chosen file is copied to [the app's internal cache directory](https://docs.expo.dev/versions/latest/sdk/filesystem#filesystemcachedirectory).
> Notes for Web: The system UI can only be shown after user activation (e.g. a `Button` press). Therefore, calling `getDocumentAsync` in `componentDidMount`, for example, will not work as intended. The `cancel` event will not be returned in the browser due to platform restrictions and inconsistencies across browsers.
## Types
### `DocumentPickerAsset`
Android
iOS
Web
Property| Type| Description  
---|---|---  
file(optional)| | Only for: Web`File` object for the parity with web File API.  
lastModified(optional)| `number`| Timestamp of last document modification.  
mimeType(optional)| `string`| Document MIME type.  
name| `string`| Document original name.  
size(optional)| `number`| Document size in bytes.  
uri| `string`| An URI to the local document file.  
### `DocumentPickerCanceledResult`
Android
iOS
Web
Type representing canceled pick result.
Property| Type| Description  
---|---|---  
assets| `null`| Always `null` when the request was canceled.  
canceled| `true`| Always `true` when the request was canceled.  
output(optional)| `null`| Only for: WebAlways `null` when the request was canceled.  
### `DocumentPickerOptions`
Android
iOS
Web
Property| Type| Description  
---|---|---  
copyToCacheDirectory(optional)| `boolean`| If `true`, the picked file is copied to [`FileSystem.CacheDirectory`](https://docs.expo.dev/versions/latest/sdk/filesystem#filesystemcachedirectory), which allows other Expo APIs to read the file immediately. This may impact performance for large files, so you should consider setting this to `false` if you expect users to pick particularly large files and your app does not need immediate read access.Default:`true`  
multiple(optional)| `boolean`| Allows multiple files to be selected from the system UI.Default:`false`  
type(optional)| `string | string[]`| The [MIME type(s)](https://en.wikipedia.org/wiki/Media_type) of the documents that are available to be picked. It also supports wildcards like `'image/*'` to choose any image. To allow any type of document you can use `'*/*'`.Default:`'*/*'`  
### `DocumentPickerResult`
Android
iOS
Web
Literal Type: `union`
Type representing successful and canceled document pick result.
Acceptable values are: `DocumentPickerSuccessResult[](https://docs.expo.dev/versions/latest/sdk/document-picker/#documentpickersuccessresult)` | `DocumentPickerCanceledResult[](https://docs.expo.dev/versions/latest/sdk/document-picker/#documentpickercanceledresult)`
### `DocumentPickerSuccessResult`
Android
iOS
Web
Type representing successful pick result.
Property| Type| Description  
---|---|---  
assets| `DocumentPickerAsset[][](https://docs.expo.dev/versions/latest/sdk/document-picker/#documentpickerasset)`| An array of picked assets.  
canceled| `false`| If asset data have been returned this should always be `false`.  
output(optional)| | Only for: Web`FileList` object for the parity with web File API.

