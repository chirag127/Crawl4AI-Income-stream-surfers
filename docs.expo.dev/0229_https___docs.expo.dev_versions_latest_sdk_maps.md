---
url: https://docs.expo.dev/versions/latest/sdk/maps
title: https://docs.expo.dev/versions/latest/sdk/maps
date: 2025-04-30T17:16:49.239677
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo Maps
A library that provides access to Google Maps on Android and Apple Maps on iOS.
Android
iOS
> This library is currently in alpha and will frequently experience breaking changes. It is not available in the Expo Go app – use [development builds](https://docs.expo.dev/develop/development-builds/introduction) to try it out.
## Installation
Terminal
Copy
`- ``npx expo install expo-maps`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Configuration
Expo Maps provides access to the platform native map APIs on Android and iOS.
  * Apple Maps (available on 
iOS
only). No additional configuration is required to use it after installing this package.
  * Google Maps (available on 
Android
only). While Google provides a Google Maps SDK for iOS, Expo Maps supports it exclusively on Android. If you want to use Google Maps on iOS, you can look into using an [alternative library](https://reactnative.directory/) or [writing your own](https://docs.expo.dev/modules/overview).


### Google Cloud API setup
Before you can use Google Maps on Android, you need to register a Google Cloud API project, enable the Maps SDK for Android, and add the associated configuration to your Expo project.
Set up Google Maps on Android
> If you have already registered a project for another Google service on Android, such as Google Sign In, you enable the Maps SDK for Android on your project and jump to step 4.
1
Register a Google Cloud API project and enable the Maps SDK for Android
  * Open your browser to the [Google API Manager](https://console.developers.google.com/apis) and create a project.
  * Once it's created, go to the project and enable the Maps SDK for Android.


2
Copy your app's SHA-1 certificate fingerprint
For Google Play Store
For development builds
  * If you are deploying your app to the Google Play Store, you'll need to [upload your app binary to Google Play console](https://docs.expo.dev/submit/android) at least once. This is required for Google to generate your app signing credentials.
  * Go to the [Google Play Console](https://play.google.com/console) > (your app) > Release > Setup > App integrity > App Signing.
  * Copy the value of SHA-1 certificate fingerprint.


  * If you have already created a [development build](https://docs.expo.dev/develop/development-builds/introduction), your project will be signed using a debug keystore.
  * After the build is complete, go to your [project's dashboard](https://expo.dev/accounts/%5Busername%5D/projects/%5Bproject-name%5D), then, under Configure > click Credentials.
  * Under Application Identifiers, click your project's package name and under Android Keystore copy the value of SHA-1 Certificate Fingerprint.


3
Create an API key
  * Go to [Google Cloud Credential manager](https://console.cloud.google.com/apis/credentials) and click Create Credentials, then API Key.
  * In the modal, click Edit API key.
  * Under Key restrictions > Application restrictions, choose Android apps.
  * Under Restrict usage to your Android apps, click Add an item.
  * Add your `android.package` from app.json (for example: `com.company.myapp`) to the package name field.
  * Then, add the SHA-1 certificate fingerprint's value from step 2.
  * Click Done and then click Save.


4
Add the API key to your project
  * Copy your API Key into your app.json under the `android.config.googleMaps.apiKey` field.
  * Create a new development build, and you can now use the Google Maps API on Android with `expo-maps`.


## Permissions
To display the user's location on the map, you need to declare and request location permission beforehand. You can configure this using the built-in [config plugin](https://docs.expo.dev/config-plugins/introduction) if you use config plugins in your project ([EAS Build](https://docs.expo.dev/build/introduction) or `npx expo run:[android|ios]`). The plugin allows you to configure various properties that cannot be set at runtime and require building a new app binary to take effect.
### Example app.json with config plugin
app.json
Copy
```
{
 "expo": {
  "plugins": [
   [
    "expo-maps",
    {
     "requestLocationPermission": "true",
     "locationPermission": "Allow $(PRODUCT_NAME) to use your location"
    }
   ]
  ]
 }
}

```

### Configurable properties
Name| Default| Description  
---|---|---  
`requestLocationPermission`| `false`| A boolean to add permissions to AndroidManifest.xml and Info.plist.  
`locationPermission`| `"Allow $(PRODUCT_NAME) to use your location"`| Only for: iOSA string to set the [`NSLocationWhenInUseUsageDescription`](https://docs.expo.dev/versions/latest/sdk/maps/#permission-nslocationwheninuseusagedescription) permission message.  
## Usage
```
import { AppleMaps, GoogleMaps } from 'expo-maps';
import { Platform, Text } from 'react-native';
export default function App() {
 if (Platform.OS === 'ios') {
  return <AppleMaps.View style={{ flex: 1 }} />;
 } else if (Platform.OS === 'android') {
  return <GoogleMaps.View style={{ flex: 1 }} />;
 } else {
  return <Text>Maps are only available on Android and iOS</Text>;
 }
}

```

## API
```
import { AppleMaps, GoogleMaps } from 'expo-maps';
// ApplesMaps.View and GoogleMaps.View are the React components

```

## Components
### `AppleMapsView`
iOS
Type: `React.Element<AppleMapsViewProps[](https://docs.expo.dev/versions/latest/sdk/maps/#applemapsviewprops)>`
AppleMapsViewProps
### `annotations`
iOS
Optional • Type: `AppleMapsAnnotation[][](https://docs.expo.dev/versions/latest/sdk/maps/#applemapsannotation)`
The array of annotations to display on the map.
### `cameraPosition`
iOS
Optional • Type: 
The initial camera position of the map.
### `markers`
iOS
Optional • Type: `AppleMapsMarker[][](https://docs.expo.dev/versions/latest/sdk/maps/#applemapsmarker)`
The array of markers to display on the map.
### `onCameraMove`
iOS
Optional • Type: `(event: {  bearing: number,   coordinates: Coordinates[](https://docs.expo.dev/versions/latest/sdk/maps/#coordinates),   tilt: number,   zoom: number }) => void`
Lambda invoked when the map was moved by the user.
### `onMapClick`
iOS
Optional • Type: `(event: {  coordinates: Coordinates[](https://docs.expo.dev/versions/latest/sdk/maps/#coordinates) }) => void`
Lambda invoked when the user clicks on the map. It won't be invoked if the user clicks on POI or a marker.
### `onMarkerClick`
iOS
Optional • Type: `(event: AppleMapsMarker[](https://docs.expo.dev/versions/latest/sdk/maps/#applemapsmarker)) => void`
Lambda invoked when the marker is clicked
### `properties`
iOS
Optional • Type: `AppleMapsProperties[](https://docs.expo.dev/versions/latest/sdk/maps/#applemapsproperties)`
The properties for the map.
### `style`
iOS
Optional • Type: `StyleProp<>`
### `uiSettings`
iOS
Optional • Type: `AppleMapsUISettings[](https://docs.expo.dev/versions/latest/sdk/maps/#applemapsuisettings)`
The `MapUiSettings` to be used for UI-specific settings on the map.
### `GoogleMapsView`
Android
Type: `React.Element[](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<Omit[](https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys)<GoogleMapsViewProps[](https://docs.expo.dev/versions/latest/sdk/maps/#googlemapsviewprops), 'ref'>>`
GoogleMapsViewProps
### `cameraPosition`
Android
Optional • Type: 
The initial camera position of the map.
### `colorScheme`
Android
Optional • Type: `GoogleMapsColorScheme[](https://docs.expo.dev/versions/latest/sdk/maps/#googlemapscolorscheme)`
Defines the color scheme for the map.
### `markers`
Android
Optional • Type: `GoogleMapsMarker[][](https://docs.expo.dev/versions/latest/sdk/maps/#googlemapsmarker)`
The array of markers to display on the map.
### `onCameraMove`
Android
Optional • Type: `(event: {  bearing: number,   coordinates: Coordinates[](https://docs.expo.dev/versions/latest/sdk/maps/#coordinates),   tilt: number,   zoom: number }) => void`
Lambda invoked when the map was moved by the user.
### `onMapClick`
Android
Optional • Type: `(event: {  coordinates: Coordinates[](https://docs.expo.dev/versions/latest/sdk/maps/#coordinates) }) => void`
Lambda invoked when the user clicks on the map. It won't be invoked if the user clicks on POI or a marker.
### `onMapLoaded`
Android
Optional • Type: `() => void`
Lambda invoked when the map is loaded.
### `onMapLongClick`
Android
Optional • Type: `(event: {  coordinates: Coordinates[](https://docs.expo.dev/versions/latest/sdk/maps/#coordinates) }) => void`
Lambda invoked when the user long presses on the map.
### `onMarkerClick`
Android
Optional • Type: `(event: GoogleMapsMarker[](https://docs.expo.dev/versions/latest/sdk/maps/#googlemapsmarker)) => void`
Lambda invoked when the marker is clicked
### `onPOIClick`
Android
Optional • Type: `(event: {  coordinates: Coordinates[](https://docs.expo.dev/versions/latest/sdk/maps/#coordinates),   name: string }) => void`
Lambda invoked when a POI is clicked.
### `properties`
Android
Optional • Type: `GoogleMapsProperties[](https://docs.expo.dev/versions/latest/sdk/maps/#googlemapsproperties)`
The properties for the map.
### `ref`
Android
Optional • Type: `Ref[](https://docs.expo.dev/versions/latest/sdk/maps/#ref)<GoogleMapsViewType[](https://docs.expo.dev/versions/latest/sdk/maps/#googlemapsviewtype)>`
### `style`
Android
Optional • Type: `StyleProp<>`
### `uiSettings`
Android
Optional • Type: `GoogleMapsUISettings[](https://docs.expo.dev/versions/latest/sdk/maps/#googlemapsuisettings)`
The `MapUiSettings` to be used for UI-specific settings on the map.
### `userLocation`
Android
Optional • Type: `GoogleMapsUserLocation[](https://docs.expo.dev/versions/latest/sdk/maps/#googlemapsuserlocation)`
User location, overrides default behavior.
### `GoogleStreetView`
Android
Type: `React.Element<GoogleStreetViewProps[](https://docs.expo.dev/versions/latest/sdk/maps/#googlestreetviewprops)>`
GoogleStreetViewProps
### `isPanningGesturesEnabled`
Android
Optional • Type: `boolean`
### `isStreetNamesEnabled`
Android
Optional • Type: `boolean`
### `isUserNavigationEnabled`
Android
Optional • Type: `boolean`
### `isZoomGesturesEnabled`
Android
Optional • Type: `boolean`
### `position`
Android
Optional • Type: 
### `style`
Android
Optional • Type: `StyleProp<>`
## Hooks
### `useLocationPermissions(options)`
Android
iOS
Parameter| Type  
---|---  
options(optional)| `PermissionHookOptions[](https://docs.expo.dev/versions/latest/sdk/maps/#permissionhookoptions)<object>`  
Check or request permissions to access the location. This uses both `requestPermissionsAsync` and `getPermissionsAsync` to interact with the permissions.
Returns:
`[null | PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/maps/#permissionresponse), RequestPermissionMethod<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/maps/#permissionresponse)>, GetPermissionMethod<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/maps/#permissionresponse)>]`
Example
```
const [status, requestPermission] = useLocationPermissions();

```

## Methods
### `Maps.getPermissionsAsync()`
Android
iOS
Checks user's permissions for accessing location.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/maps/#permissionresponse)>`
A promise that fulfills with an object of type [`PermissionResponse`](https://docs.expo.dev/versions/latest/sdk/maps/#permissionresponse).
### `Maps.requestPermissionsAsync()`
Android
iOS
Asks the user to grant permissions for location.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/maps/#permissionresponse)>`
A promise that fulfills with an object of type [`PermissionResponse`](https://docs.expo.dev/versions/latest/sdk/maps/#permissionresponse).
## Types
### `AppleMapsAnnotation`
iOS
Type: `AppleMapsMarker[](https://docs.expo.dev/versions/latest/sdk/maps/#applemapsmarker)` extended by:
Property| Type| Description  
---|---|---  
backgroundColor(optional)| `string`| The background color of the annotation.  
icon(optional)| `SharedRefType[](https://docs.expo.dev/versions/latest/sdk/maps/#sharedreftype)<'image'>`| The custom icon to display in the annotation.  
text(optional)| `string`| The text to display in the annotation.  
textColor(optional)| `string`| The text color of the annotation.  
### `AppleMapsMarker`
iOS
Property| Type| Description  
---|---|---  
coordinates(optional)| | The coordinates of the marker.  
systemImage(optional)| `string`| The SF Symbol to display for the marker.  
tintColor(optional)| `string`| The tint color of the marker.  
title(optional)| `string`| The title of the marker, displayed in the callout when the marker is clicked.  
### `AppleMapsProperties`
iOS
Property| Type| Description  
---|---|---  
isTrafficEnabled(optional)| `boolean`| Whether the traffic layer is enabled on the map.  
mapType(optional)| `AppleMapsMapType[](https://docs.expo.dev/versions/latest/sdk/maps/#applemapsmaptype)`| Defines which map type should be used.  
selectionEnabled(optional)| `boolean`| If true, the user can select a location on the map to get more information.  
### `AppleMapsUISettings`
iOS
Property| Type| Description  
---|---|---  
compassEnabled(optional)| `boolean`| Whether the compass is enabled on the map. If enabled, the compass is only visible when the map is rotated.  
myLocationButtonEnabled(optional)| `boolean`| Whether the my location button is visible.  
scaleBarEnabled(optional)| `boolean`| Whether the scale bar is displayed when zooming.  
togglePitchEnabled(optional)| `boolean`| Whether the user is allowed to change the pitch type.  
### `CameraPosition`
Android
iOS
Property| Type| Description  
---|---|---  
coordinates(optional)| | The middle point of the camera.  
zoom(optional)| `number`| The zoom level of the camera. For some view sizes, lower zoom levels might not be available.  
### `Coordinates`
Android
iOS
Property| Type| Description  
---|---|---  
latitude(optional)| `number`| The latitude of the coordinate.  
longitude(optional)| `number`| The longitude of the coordinate.  
### `GoogleMapsMarker`
Android
Property| Type| Description  
---|---|---  
coordinates(optional)| | The coordinates of the marker.  
draggable(optional)| `boolean`| Whether the marker is draggable.  
icon(optional)| `SharedRefType[](https://docs.expo.dev/versions/latest/sdk/maps/#sharedreftype)<'image'>`| The custom icon to display for the marker.  
showCallout(optional)| `boolean`| Whether the callout should be shown when the marker is clicked.  
snippet(optional)| `string`| The snippet of the marker, Displayed in the callout when the marker is clicked.  
title(optional)| `string`| The title of the marker, displayed in the callout when the marker is clicked.  
### `GoogleMapsProperties`
Android
Property| Type| Description  
---|---|---  
isBuildingEnabled(optional)| `boolean`| Whether the building layer is enabled on the map.  
isIndoorEnabled(optional)| `boolean`| Whether the indoor layer is enabled on the map.  
isMyLocationEnabled(optional)| `boolean`| Whether finding the user's location is enabled on the map.  
isTrafficEnabled(optional)| `boolean`| Whether the traffic layer is enabled on the map.  
mapType(optional)| `GoogleMapsMapType[](https://docs.expo.dev/versions/latest/sdk/maps/#googlemapsmaptype)`| Defines which map type should be used.  
maxZoomPreference(optional)| `number`| The maximum zoom level for the map.  
minZoomPreference(optional)| `number`| The minimum zoom level for the map.  
selectionEnabled(optional)| `boolean`| If true, the user can select a location on the map to get more information.  
### `GoogleMapsUISettings`
Android
Property| Type| Description  
---|---|---  
compassEnabled(optional)| `boolean`| Whether the compass is enabled on the map. If enabled, the compass is only visible when the map is rotated.  
indoorLevelPickerEnabled(optional)| `boolean`| Whether the indoor level picker is enabled .  
mapToolbarEnabled(optional)| `boolean`| Whether the map toolbar is visible.  
myLocationButtonEnabled(optional)| `boolean`| Whether the my location button is visible.  
rotationGesturesEnabled(optional)| `boolean`| Whether rotate gestures are enabled.  
scaleBarEnabled(optional)| `boolean`| Whether the scale bar is displayed when zooming.  
scrollGesturesEnabled(optional)| `boolean`| Whether the scroll gestures are enabled.  
scrollGesturesEnabledDuringRotateOrZoom(optional)| `boolean`| Whether the scroll gestures are enabled during rotation or zoom.  
tiltGesturesEnabled(optional)| `boolean`| Whether the tilt gestures are enabled.  
togglePitchEnabled(optional)| `boolean`| Whether the user is allowed to change the pitch type.  
zoomControlsEnabled(optional)| `boolean`| Whether the zoom controls are visible.  
zoomGesturesEnabled(optional)| `boolean`| Whether the zoom gestures are enabled.  
### `GoogleMapsUserLocation`
Android
Property| Type| Description  
---|---|---  
coordinates| | User location coordinates.  
followUserLocation| `boolean`| Should the camera follow the users' location.  
### `GoogleMapsViewType`
Android
Property| Type| Description  
---|---|---  
setCameraPosition| `(config: SetCameraPositionConfig[](https://docs.expo.dev/versions/latest/sdk/maps/#setcamerapositionconfig)) => void`| Update camera position.`config: SetCameraPositionConfig[](https://docs.expo.dev/versions/latest/sdk/maps/#setcamerapositionconfig)`New camera position config.  
### `SetCameraPositionConfig`
Android
Type: extended by:
Property| Type| Description  
---|---|---  
duration(optional)| `number`| The duration of the animation in milliseconds.  
## Enums
### `AppleMapsMapType`
iOS
The type of map to display.
#### `HYBRID`
`AppleMapsMapType.HYBRID ＝ "HYBRID"`
A satellite image of the area with road and road name layers on top.
#### `IMAGERY`
`AppleMapsMapType.IMAGERY ＝ "IMAGERY"`
A satellite image of the area.
#### `STANDARD`
`AppleMapsMapType.STANDARD ＝ "STANDARD"`
A street map that shows the position of all roads and some road names.
### `GoogleMapsColorScheme`
Android
#### `DARK`
`GoogleMapsColorScheme.DARK ＝ "DARK"`
#### `FOLLOW_SYSTEM`
`GoogleMapsColorScheme.FOLLOW_SYSTEM ＝ "FOLLOW_SYSTEM"`
#### `LIGHT`
`GoogleMapsColorScheme.LIGHT ＝ "LIGHT"`
### `GoogleMapsMapType`
Android
The type of map to display.
#### `HYBRID`
`GoogleMapsMapType.HYBRID ＝ "HYBRID"`
Satellite imagery with roads and points of interest overlayed.
#### `NORMAL`
`GoogleMapsMapType.NORMAL ＝ "NORMAL"`
Standard road map.
#### `SATELLITE`
`GoogleMapsMapType.SATELLITE ＝ "SATELLITE"`
Satellite imagery.
#### `TERRAIN`
`GoogleMapsMapType.TERRAIN ＝ "TERRAIN"`
Topographic data.
## Permissions
### Android
To show the user's location on the map, the `expo-maps` library requires the following permissions:
  * `ACCESS_COARSE_LOCATION`: for approximate device location
  * `ACCESS_FINE_LOCATION`: for precise device location


Android Permission| Description  
---|---  
`ACCESS_COARSE_LOCATION`| Allows an app to access approximate location.
> Alternatively, you might want .  
`ACCESS_FINE_LOCATION`| Allows an app to access precise location.
> Alternatively, you might want `ACCESS_COARSE_LOCATION[](https://developer.android.com/reference/android/Manifest.permission#ACCESS_COARSE_LOCATION)`.  
`FOREGROUND_SERVICE`| Allows a regular application to use Service.startForeground.
> Allows a regular application to use `Service.startForeground[](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))`.  
`FOREGROUND_SERVICE_LOCATION`| Allows a regular application to use Service.startForeground with the type "location".
> Allows a regular application to use `Service.startForeground[](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "location".  
`ACCESS_BACKGROUND_LOCATION`| Allows an app to access location in the background.
> If you're requesting this permission, you must also request either `ACCESS_COARSE_LOCATION[](https://developer.android.com/reference/android/Manifest.permission#ACCESS_COARSE_LOCATION)` or . Requesting this permission by itself doesn't give you location access.  
### iOS
The following usage description keys are used by this library:
Info.plist Key| Description  
---|---  
`NSLocationWhenInUseUsageDescription`| A message that tells the user why the app is requesting access to the user’s location information while the app is running in the foreground.

