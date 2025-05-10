---
url: https://docs.expo.dev/versions/latest/sdk/manifests
title: https://docs.expo.dev/versions/latest/sdk/manifests
date: 2025-04-30T17:16:54.566048
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo Manifests
A library that provides types for Expo Manifests.
Android
iOS
tvOS
## Installation
Terminal
Copy
`- ``npx expo install expo-manifests`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## API
```
import * as Manifests from 'expo-manifests';

```

## Types
> Deprecated Renamed to `EmbeddedManifest`, will be removed in a few versions.
### `BareManifest`
Android
iOS
tvOS
Type: 
### `ClientScopingConfig`
Android
iOS
tvOS
Property| Type| Description  
---|---|---  
scopeKey(optional)| `string`| An opaque unique string for scoping client-side data to this project. This value will not change when a project is transferred between accounts or renamed.  
### `EASConfig`
Android
iOS
tvOS
Property| Type| Description  
---|---|---  
projectId(optional)| `string`| The ID for this project if it's using EAS. UUID. This value will not change when a project is transferred between accounts or renamed.  
### `EmbeddedManifest`
Android
iOS
tvOS
An embedded manifest.
Generated during build in createManifest.js build step script.
Property| Type| Description  
---|---|---  
assets| `any[]`  
commitTime| `number`  
id| `string`  
### `ExpoClientConfig`
Android
iOS
tvOS
Type: extended by:
Property| Type| Description  
---|---|---  
hostUri(optional)| `string`| Only present during development using `@expo/cli`.  
### `ExpoGoConfig`
Android
iOS
tvOS
Property| Type| Description  
---|---|---  
debuggerHost(optional)| `string`  
developer(optional)| `Record<string, any> & {  tool: string }`  
mainModuleName(optional)| `string`  
packagerOpts(optional)| `ExpoGoPackagerOpts[](https://docs.expo.dev/versions/latest/sdk/manifests#expogopackageropts)`  
### `ExpoGoPackagerOpts`
Android
iOS
tvOS
Type: `Record<string, any>` extended by:
Property| Type| Description  
---|---|---  
dev(optional)| `boolean`  
hostType(optional)| `string`  
lanType(optional)| `string`  
minify(optional)| `boolean`  
strict(optional)| `boolean`  
urlRandomness(optional)| `string`  
urlType(optional)| `string`  
### `ExpoUpdatesManifest`
Android
iOS
tvOS
A `expo-updates` manifest.
Property| Type| Description  
---|---|---  
assets| `ManifestAsset[][](https://docs.expo.dev/versions/latest/sdk/manifests/#manifestasset)`  
createdAt| `string`  
extra(optional)|   
id| `string`  
launchAsset|   
metadata| `object`  
runtimeVersion| `string`  
### `ManifestAsset`
Android
iOS
tvOS
Property| Type| Description  
---|---|---  
url| `string`  
### `ManifestExtra`
Android
iOS
tvOS
Type: `ClientScopingConfig[](https://docs.expo.dev/versions/latest/sdk/manifests#clientscopingconfig)` extended by:
Property| Type| Description  
---|---|---  
eas(optional)|   
expoClient(optional)|   
expoGo(optional)|   
> Deprecated renamed to `ExpoUpdatesManifest`, will be removed in a few versions.
### `NewManifest`
Android
iOS
tvOS
Type: `ExpoUpdatesManifest[](https://docs.expo.dev/versions/latest/sdk/manifests#expoupdatesmanifest)`

