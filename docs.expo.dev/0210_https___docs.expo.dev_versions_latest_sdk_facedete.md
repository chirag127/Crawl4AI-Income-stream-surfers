---
url: https://docs.expo.dev/versions/latest/sdk/facedetector
title: https://docs.expo.dev/versions/latest/sdk/facedetector
date: 2025-04-30T17:16:13.110551
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo FaceDetector
A library that uses Google Mobile Vision to detect faces on images.
Android (device only)
iOS (device only)
Bundled version:
~13.0.2
> Deprecated: This library is not available from SDK 51. We recommend [`react-native-vision-camera`](https://github.com/mrousavy/react-native-vision-camera) if you require this functionality.
`expo-face-detector` lets you use the power of the [Google's ML Kit](https://developers.google.com/ml-kit/vision/face-detection) framework to detect faces on images.
#### Known issues 
Android
Face detector does not recognize faces that aren't aligned with the interface (top of the interface matches top of the head).
## Installation
This module is not available in the [Expo Go app](https://expo.dev/go) because it has dependencies that break builds for iOS Simulators.
You can create a [development build](https://docs.expo.dev/develop/development-builds/create-a-build) to work with this package.
Terminal
Copy
`- ``npx expo install expo-face-detector`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Usage
### Settings
To configure detector's behavior modules pass a [`DetectionOptions`](https://docs.expo.dev/versions/latest/sdk/facedetector#detectionoptions) object which is then interpreted by this module.
### Example
You can use the following snippet to detect faces in a fast mode without detecting landmarks or whether a face is smiling.
Quick face detection
```
import { Camera } from 'expo-camera';
import * as FaceDetector from 'expo-face-detector';
const App = () => (
 <Camera
  // other props
  onFacesDetected={handleFacesDetected}
  faceDetectorSettings={{
   mode: FaceDetector.FaceDetectorMode.fast,
   detectLandmarks: FaceDetector.FaceDetectorLandmarks.none,
   runClassifications: FaceDetector.FaceDetectorClassifications.none,
   minDetectionInterval: 100,
   tracking: true,
  }}
 />
);
const handleFacesDetected = ({ faces }) => {
 console.log(faces);
};
export default App;

Show More

```

## API
```
import * as FaceDetector from 'expo-face-detector';

```

## Methods
> Deprecated If you require this functionality, we recommend using [react-native-vision-camera](https://github.com/mrousavy/react-native-vision-camera)
### `FaceDetector.detectFacesAsync(uri, options)`
Android
iOS
Parameter| Type| Description  
---|---|---  
uri| `string`| `file://` URI to the image.  
options(optional)| `DetectionOptions[](https://docs.expo.dev/versions/latest/sdk/facedetector/#detectionoptions)`| A map of detection options.Default:`{}`  
Detect faces on a picture.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
Returns a Promise which fulfils with [`DetectionResult`](https://docs.expo.dev/versions/latest/sdk/facedetector/#detectionresult) object.
## Types
### `DetectionOptions`
Android
iOS
In order to configure detector's behavior modules pass a settings object which is then interpreted by this module.
Property| Type| Description  
---|---|---  
detectLandmarks(optional)| `FaceDetectorLandmarks[](https://docs.expo.dev/versions/latest/sdk/facedetector/#facedetectorlandmarks)`| Whether to detect and return landmarks positions on the face (ears, eyes, mouth, cheeks, nose). Use `FaceDetector.FaceDetectorLandmarks.{all, none}`.  
minDetectionInterval(optional)| `number`| Minimal interval in milliseconds between two face detection events being submitted to JS. Use, when you expect lots of faces for long time and are afraid of JS Bridge being overloaded.Default:`0`  
mode(optional)| `FaceDetectorMode[](https://docs.expo.dev/versions/latest/sdk/facedetector/#facedetectormode)`| Whether to detect faces in fast or accurate mode. Use `FaceDetector.FaceDetectorMode.{fast, accurate}`.  
runClassifications(optional)| `FaceDetectorClassifications[](https://docs.expo.dev/versions/latest/sdk/facedetector/#facedetectorclassifications)`| Whether to run additional classifications on detected faces (smiling probability, open eye probabilities). Use `FaceDetector.FaceDetectorClassifications.{all, none}`.  
tracking(optional)| `boolean`| Flag to enable tracking of faces between frames. If true, each face will be returned with `faceID` attribute which should be consistent across frames.Default:`false`  
### `DetectionResult`
Android
iOS
Property| Type| Description  
---|---|---  
faces| `FaceFeature[][](https://docs.expo.dev/versions/latest/sdk/facedetector/#facefeature)`| Array of faces objects.  
image|   
### `FaceFeature`
Android
iOS
Property| Type| Description  
---|---|---  
bottomMouthPosition(optional)| | Position of the bottom edge of the mouth in image coordinates. Returned only if detection classifications property is set to `FaceDetectorLandmarks.all`.  
bounds| `FaceFeatureBounds[](https://docs.expo.dev/versions/latest/sdk/facedetector/#facefeaturebounds)`| An object containing face bounds.  
faceID(optional)| `number`| A face identifier (used for tracking, if the same face appears on consecutive frames it will have the same `faceID`).  
leftCheekPosition(optional)| | Position of the left cheek in image coordinates. Returned only if detection classifications property is set to `FaceDetectorLandmarks.all`.  
leftEarPosition(optional)| | Position of the left ear in image coordinates. Returned only if detection classifications property is set to `FaceDetectorLandmarks.all`.  
leftEyeOpenProbability(optional)| `number`| Probability that the left eye is open. Returned only if detection classifications property is set to `FaceDetectorClassifications.all`.  
leftEyePosition(optional)| | Position of the left eye in image coordinates. Returned only if detection classifications property is set to `FaceDetectorLandmarks.all`.  
leftMouthPosition(optional)| | Position of the left edge of the mouth in image coordinates. Returned only if detection classifications property is set to `FaceDetectorLandmarks.all`.  
mouthPosition(optional)| | Position of the center of the mouth in image coordinates. Returned only if detection classifications property is set to `FaceDetectorLandmarks.all`.  
noseBasePosition(optional)| | Position of the nose base in image coordinates. Returned only if detection classifications property is set to `FaceDetectorLandmarks.all`.  
rightCheekPosition(optional)| | Position of the right cheek in image coordinates. Returned only if detection classifications property is set to `FaceDetectorLandmarks.all`.  
rightEarPosition(optional)| | Position of the right ear in image coordinates. Returned only if detection classifications property is set to `FaceDetectorLandmarks.all`.  
rightEyeOpenProbability(optional)| `number`| Probability that the right eye is open. Returned only if detection classifications property is set to `FaceDetectorClassifications.all`.  
rightEyePosition(optional)| | Position of the right eye in image coordinates. Returned only if detection classifications property is set to `FaceDetectorLandmarks.all`.  
rightMouthPosition(optional)| | Position of the right edge of the mouth in image coordinates. Returned only if detection classifications property is set to `FaceDetectorLandmarks.all`.  
rollAngle(optional)| `number`| Roll angle of the face (bank).  
smilingProbability(optional)| `number`| Probability that the face is smiling. Returned only if detection classifications property is set to `FaceDetectorClassifications.all`.  
yawAngle(optional)| `number`| Yaw angle of the face (heading, turning head left or right).  
### `FaceFeatureBounds`
Android
iOS
Property| Type| Description  
---|---|---  
origin| | Position of the top left corner of a square containing the face in image coordinates,  
size| `{  height: number,   width: number }`| Size of the square containing the face in image coordinates,  
### `Image`
Android
iOS
Property| Type| Description  
---|---|---  
height| `number`| Height of the image in pixels.  
orientation| `number`| Orientation of the image (value conforms to the EXIF orientation tag standard).  
uri| `string`| URI of the image.  
width| `number`| Width of the image in pixels.  
### `Point`
Android
iOS
Property| Type| Description  
---|---|---  
`number`  
`number`  
## Enums
### `FaceDetectorClassifications`
Android
iOS
#### `none`
`FaceDetectorClassifications.none ＝ 1`
#### `all`
`FaceDetectorClassifications.all ＝ 2`
### `FaceDetectorLandmarks`
Android
iOS
#### `none`
`FaceDetectorLandmarks.none ＝ 1`
#### `all`
`FaceDetectorLandmarks.all ＝ 2`
### `FaceDetectorMode`
Android
iOS
#### `fast`
`FaceDetectorMode.fast ＝ 1`
#### `accurate`
`FaceDetectorMode.accurate ＝ 2`

