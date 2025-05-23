---
url: https://docs.expo.dev/versions/latest/sdk/map-view
title: https://docs.expo.dev/versions/latest/sdk/map-view
date: 2025-04-30T17:16:54.585802
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# React Native Maps
A library that provides a Map component that uses Google Maps on Android and Apple Maps or Google Maps on iOS.
Android
iOS
Bundled version:
1.18.0
> This library is listed in the Expo SDK reference because it is included in [Expo Go](https://expo.dev/go). You may use any library of your choice with [development builds](https://docs.expo.dev/develop/development-builds/introduction).
`react-native-maps` provides a Map component that uses Google Maps on Android and Apple Maps or Google Maps on iOS.
No additional setup is required when testing your project using Expo Go. However, to deploy the app binary on app stores additional steps are required for Google Maps. For more information, see the [instructions below](https://docs.expo.dev/versions/latest/sdk/map-view#deploy-app-with-google-maps).
## Installation
Terminal
Copy
`- ``npx expo install react-native-maps`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project. Then, follow the [installation instructions](https://github.com/react-native-maps/react-native-maps/blob/master/docs/installation.md) provided in the library's README or documentation.
## Usage
See full documentation at [`react-native-maps/react-native-maps`](https://github.com/react-native-maps/react-native-maps).
MapView
```
import React from 'react';
import MapView from 'react-native-maps';
import { StyleSheet, View } from 'react-native';
export default function App() {
 return (
  <View style={styles.container}><MapView style={styles.map} /></View>
 );
}
const styles = StyleSheet.create({
 container: {
  flex: 1,
 },
 map: {
  width: '100%',
  height: '100%',
 },
});

Show More

```

## Deploy app with Google Maps
### Android
> If you have already registered a project for another Google service on Android, such as Google Sign In, you enable the Maps SDK for Android on your project and jump to step 4.
1
#### Register a Google Cloud API project and enable the Maps SDK for Android
  * Open your browser to the [Google API Manager](https://console.developers.google.com/apis) and create a project.
  * Once it's created, go to the project and enable the Maps SDK for Android.


2
#### Copy your app's SHA-1 certificate fingerprint
For Google Play Store
For development builds
  * If you are deploying your app to the Google Play Store, you'll need to [upload your app binary to Google Play console](https://docs.expo.dev/submit/android) at least once. This is required for Google to generate your app signing credentials.
  * Go to the [Google Play Console](https://play.google.com/console) > (your app) > Release > Setup > App integrity > App Signing.
  * Copy the value of SHA-1 certificate fingerprint.


  * If you have already created a [development build](https://docs.expo.dev/develop/development-builds/introduction), your project will be signed using a debug keystore.
  * After the build is complete, go to your [project's dashboard](https://expo.dev/accounts/%5Busername%5D/projects/%5Bproject-name%5D), then, under Configure > click Credentials.
  * Under Application Identifiers, click your project's package name and under Android Keystore copy the value of SHA-1 Certificate Fingerprint.


3
#### Create an API key
  * Go to [Google Cloud Credential manager](https://console.cloud.google.com/apis/credentials) and click Create Credentials, then API Key.
  * In the modal, click Edit API key.
  * Under Key restrictions > Application restrictions, choose Android apps.
  * Under Restrict usage to your Android apps, click Add an item.
  * Add your `android.package` from app.json (for example: `com.company.myapp`) to the package name field.
  * Then, add the SHA-1 certificate fingerprint's value from step 2.
  * Click Done and then click Save.


4
#### Add the API key to your project
  * Copy your API Key into your your to either a .env file and then add it to your app.json under the `android.config.googleMaps.apiKey` field like or copy it:

```
  "android": {
   "config": {
    "googleMaps": {
     "apiKey": "process.env.GOOGLE_MAPS_API_KEY",
    },
   },
  }

```

  * In your code, import `{ PROVIDER_GOOGLE }` from `react-native-maps` and add the property `provider={PROVIDER_GOOGLE}` to your `<MapView>`. This property works on both Android and iOS.
  * Rebuild the app binary (or re-submit to the Google Play Store in case your app is already uploaded). An easy way to test if the configuration was successful is to do an [emulator build](https://docs.expo.dev/develop/development-builds/create-a-build#create-a-development-build-for-emulatorsimulator).


### iOS
> If you have already registered a project for another Google service on iOS, such as Google Sign In, you enable the Maps SDK for iOS on your project and jump to step 3.
1
#### Register a Google Cloud API project and enable the Maps SDK for iOS
  * Open your browser to the [Google API Manager](https://console.developers.google.com/apis) and create a project.
  * Then, go to the project, click Enable APIs and Services and enable the Maps SDK for iOS.


2
#### Create an API key
  * Go to [Google Cloud Credential manager](https://console.cloud.google.com/apis/credentials) and click Create Credentials, then API Key.
  * In the modal, click Edit API key.
  * Under Key restrictions > Application restrictions, choose iOS apps.
  * Under Accept requests from an iOS application with one of these bundle identifiers, click the Add an item button.
  * Add your `ios.bundleIdentifier` from app.json (for example: `com.company.myapp`) to the bundle ID field.
  * Click Done and then click Save.


3
#### Add the API key to your project
  * Copy your API Key into your your to either a .env file and then add it to your app.json under the `ios.config.googleMapsApiKey` field like or copy it:

```
  "ios": {
   "config": {
    "googleMapsApiKey": "process.env.GOOGLE_MAPS_API_KEY",
    },
   }

```

  * In your code, import `{ PROVIDER_GOOGLE }` from `react-native-maps` and add the property `provider={PROVIDER_GOOGLE}` to your `<MapView>`. This property works on both Android and iOS.
  * Rebuild the app binary. An easy way to test if the configuration was successful is to do a [simulator build](https://docs.expo.dev/develop/development-builds/create-a-build#create-a-development-build-for-emulatorsimulator).



