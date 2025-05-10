---
url: https://docs.expo.dev/versions/latest/sdk/sensors
title: https://docs.expo.dev/versions/latest/sdk/sensors
date: 2025-04-30T17:17:22.526287
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo Sensors
A library that provides access to a device's accelerometer, barometer, motion, gyroscope, light, magnetometer, and pedometer.
Android
iOS
Web
Bundled version:
~14.0.2
`expo-sensors` provide various APIs for accessing device sensors to measure motion, orientation, pressure, magnetic fields, ambient light, and step count.
## Installation
Terminal
Copy
`- ``npx expo install expo-sensors`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Configuration in app config
You can configure `expo-sensors` using its built-in [config plugin](https://docs.expo.dev/config-plugins/introduction) if you use config plugins in your project ([EAS Build](https://docs.expo.dev/build/introduction) or `npx expo run:[android|ios]`). The plugin allows you to configure various properties that cannot be set at runtime and require building a new app binary to take effect.
### Example app.json with config plugin
app.json
Copy
```
{
 "expo": {
  "plugins": [
   [
    "expo-sensors",
    {
     "motionPermission": "Allow $(PRODUCT_NAME) to access your device motion"
    }
   ]
  ]
 }
}

```

### Configurable properties
Name| Default| Description  
---|---|---  
`motionPermission`| `"Allow $(PRODUCT_NAME) to access your device motion"`| Only for: iOSA string to set the [`NSMotionUsageDescription`](https://docs.expo.dev/versions/latest/sdk/sensors/#permission-nsmotionusagedescription) permission message or `false` to disable motion permissions.  
Are you using this library in an existing React Native app?
If you're not using Continuous Native Generation ([CNG](https://docs.expo.dev/workflow/continuous-native-generation)) or you're using native android project manually, add `HIGH_SAMPLING_RATE_SENSORS` permission to your project's android/app/src/main/AndroidManifest.xml:
```
<uses-permission android:name="android.permission.HIGH_SAMPLING_RATE_SENSORS" />

```

## API
```
import * as Sensors from 'expo-sensors';
// OR
import {
 Accelerometer,
 Barometer,
 DeviceMotion,
 Gyroscope,
 LightSensor,
 Magnetometer,
 MagnetometerUncalibrated,
 Pedometer,
} from 'expo-sensors';

```

## Permissions
### Android
Starting in Android 12 (API level 31), the system has a 200Hz limit for each sensor updates.
If you need an update interval of less than 200Hz, you must add the following permissions to your app.json inside the [`expo.android.permissions`](https://docs.expo.dev/versions/latest/config/app#permissions) array.
Android Permission| Description  
---|---  
`HIGH_SAMPLING_RATE_SENSORS`| Allows an app to access sensor data with a sampling rate greater than 200 Hz.  
### iOS
The following usage description keys are used by this library:
Info.plist Key| Description  
---|---  
`NSMotionUsageDescription`| A message that tells the user why the app is requesting access to the device’s motion data.  
## Available sensors
For more information, see the documentation for the sensor you are interested in:
[AccelerometerMeasures device acceleration on all platforms.](https://docs.expo.dev/versions/latest/sdk/accelerometer) [BarometerMeasures pressure on Android and iOS platforms.](https://docs.expo.dev/versions/latest/sdk/barometer) [DeviceMotionMeasures device motion on all platforms.](https://docs.expo.dev/versions/latest/sdk/devicemotion) [GyroscopeMeasures device rotation on all platforms.](https://docs.expo.dev/versions/latest/sdk/gyroscope) [MagnetometerMeasures magnetic fields on Android and iOS platforms.](https://docs.expo.dev/versions/latest/sdk/magnetometer) [LightSensorMeasures ambient light on Android platform.](https://docs.expo.dev/versions/latest/sdk/light-sensor) [PedometerMeasures steps count on Android and iOS platforms.](https://docs.expo.dev/versions/latest/sdk/pedometer)

