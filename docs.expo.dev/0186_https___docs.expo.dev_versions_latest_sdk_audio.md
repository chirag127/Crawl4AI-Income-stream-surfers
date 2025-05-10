---
url: https://docs.expo.dev/versions/latest/sdk/audio
title: https://docs.expo.dev/versions/latest/sdk/audio
date: 2025-04-30T17:15:22.083624
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo Audio (expo-audio)
A library that provides an API to implement audio playback and recording in apps.
Android
iOS
Web
Bundled version:
~0.3.5
> This page documents an upcoming version of the Audio library. Expo Audio is currently in alpha and subject to breaking changes.
`expo-audio` is a cross-platform audio library for accessing the native audio capabilities of the device.
Note that audio automatically stops if headphones/bluetooth audio devices are disconnected.
## Installation
Terminal
Copy
`- ``npx expo install expo-audio`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Configuration in app config
You can configure `expo-audio` using its built-in [config plugin](https://docs.expo.dev/config-plugins/introduction) if you use config plugins in your project ([EAS Build](https://docs.expo.dev/build/introduction) or `npx expo run:[android|ios]`). The plugin allows you to configure various properties that cannot be set at runtime and require building a new app binary to take effect. If your app does not use EAS Build, then you'll need to manually configure the package.
### Example app.json with config plugin
app.json
Copy
```
{
 "expo": {
  "plugins": [
   [
    "expo-audio",
    {
     "microphonePermission": "Allow $(PRODUCT_NAME) to access your microphone."
    }
   ]
  ]
 }
}

```

### Configurable properties
Name| Default| Description  
---|---|---  
`microphonePermission`| `"Allow $(PRODUCT_NAME) to access your microphone"`| Only for: iOSA string to set the [`NSMicrophoneUsageDescription`](https://docs.expo.dev/versions/latest/sdk/audio/#permission-nsmicrophoneusagedescription) permission message.  
## Usage
### Playing sounds
Playing sounds
```
import { useEffect, useState } from 'react';
import { View, StyleSheet, Button } from 'react-native';
import { useAudioPlayer } from 'expo-audio';
const audioSource = require('./assets/Hello.mp3');
export default function App() {
 const player = useAudioPlayer(audioSource);
 return (
  <View style={styles.container}><Button title="Play Sound" onPress={() => player.play()} /></View>
 );
}
const styles = StyleSheet.create({
 container: {
  flex: 1,
  justifyContent: 'center',
  backgroundColor: '#ecf0f1',
  padding: 10,
 },
});

Show More

```

### Recording sounds
Recording sounds
```
import { useState } from 'react';
import { View, StyleSheet, Button } from 'react-native';
import { useAudioRecorder, RecordingOptions, AudioModule, RecordingPresets } from 'expo-audio';
export default function App() {
 const audioRecorder = useAudioRecorder(RecordingPresets.HIGH_QUALITY);
 const record = async () => {
  await audioRecorder.prepareToRecordAsync();
  audioRecorder.record();
 };
 const stopRecording = async () => {
  // The recording will be available on `audioRecorder.uri`.
  await audioRecorder.stop();
 };
 useEffect(() => {
  (async () => {
   const status = await AudioModule.requestRecordingPermissionsAsync();
   if (!status.granted) {
    Alert.alert('Permission to access microphone was denied');
   }
  })();
 }, []);
 return (
  <View style={styles.container}><Button
    title={audioRecorder.isRecording ? 'Stop Recording' : 'Start Recording'}
    onPress={audioRecorder.isRecording ? stopRecording : record}
   /></View>
 );
}
const styles = StyleSheet.create({
 container: {
  flex: 1,
  justifyContent: 'center',
  backgroundColor: '#ecf0f1',
  padding: 10,
 },
});

Show More

```

### Playing or recording audio in background 
iOS
On iOS, audio playback and recording in background is only available in standalone apps, and it requires some extra configuration. On iOS, each background feature requires a special key in `UIBackgroundModes` array in your Info.plist file. In standalone apps this array is empty by default, so to use background features you will need to add appropriate keys to your app.json configuration.
See an example of app.json that enables audio playback in background:
```
{
 "expo": {
  ...
  "ios": {
   ...
   "infoPlist": {
    ...
    "UIBackgroundModes": [
     "audio"
    ]
   }
  }
 }
}

```

### Notes on web usage
  * A MediaRecorder issue on Chrome produces WebM files missing the duration metadata. [See the open Chromium issue](https://bugs.chromium.org/p/chromium/issues/detail?id=642012).
  * MediaRecorder encoding options and other configurations are inconsistent across browsers, utilizing a Polyfill such as [kbumsik/opus-media-recorder](https://github.com/kbumsik/opus-media-recorder) or [ai/audio-recorder-polyfill](https://github.com/ai/audio-recorder-polyfill) in your application will improve your experience. Any options passed to `prepareToRecordAsync` will be passed directly to the MediaRecorder API and as such the polyfill.
  * Web browsers require sites to be served securely for them to listen to a mic. See [MediaDevices `getUserMedia()` security](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia#security) for more details.


## API
```
import { useAudioPlayer, useAudioRecorder } from 'expo-audio';

```

## Constants
### `Audio.AUDIO_SAMPLE_UPDATE`
Android
iOS
Web
Type: `'audioSampleUpdate'`
### `Audio.PLAYBACK_STATUS_UPDATE`
Android
iOS
Web
Type: `'playbackStatusUpdate'`
### `Audio.RECORDING_STATUS_UPDATE`
Android
iOS
Web
Type: `'recordingStatusUpdate'`
### `Audio.RecordingPresets`
Android
iOS
Web
Type: `Record<string, >`
Constant which contains definitions of the two preset examples of `RecordingOptions`, as implemented in the Audio SDK.
#### `HIGH_QUALITY`
```
RecordingPresets.HIGH_QUALITY = {
 extension: '.m4a',
 sampleRate: 44100,
 numberOfChannels: 2,
 bitRate: 128000,
 android: {
  outputFormat: 'mpeg4',
  audioEncoder: 'aac',
 },
 ios: {
  outputFormat: IOSOutputFormat.MPEG4AAC,
  audioQuality: AudioQuality.MAX,
  linearPCMBitDepth: 16,
  linearPCMIsBigEndian: false,
  linearPCMIsFloat: false,
 },
 web: {
  mimeType: 'audio/webm',
  bitsPerSecond: 128000,
 },
};

Show More

```

#### `LOW_QUALITY`
```
RecordingPresets.LOW_QUALITY = {
 extension: '.m4a',
 sampleRate: 44100,
 numberOfChannels: 2,
 bitRate: 64000,
 android: {
  extension: '.3gp',
  outputFormat: '3gp',
  audioEncoder: 'amr_nb',
 },
 ios: {
  audioQuality: AudioQuality.MIN,
  outputFormat: IOSOutputFormat.MPEG4AAC,
  linearPCMBitDepth: 16,
  linearPCMIsBigEndian: false,
  linearPCMIsFloat: false,
 },
 web: {
  mimeType: 'audio/webm',
  bitsPerSecond: 128000,
 },
};

Show More

```

## Hooks
### `useAudioPlayer(source, updateInterval)`
Android
iOS
Web
Parameter| Type  
---|---  
source(optional)| `number | `  
updateInterval(optional)| `number`  
Returns:
### `useAudioPlayerStatus(player)`
Android
iOS
Web
Parameter| Type  
---|---  
player|   
Returns:
### `useAudioRecorder(options, statusListener)`
Android
iOS
Web
Parameter| Type  
---|---  
options| `RecordingOptions[](https://docs.expo.dev/versions/latest/sdk/audio/#recordingoptions)`  
statusListener(optional)| `(status: RecordingStatus[](https://docs.expo.dev/versions/latest/sdk/audio/#recordingstatus)) => void`  
Returns:
`AudioRecorder[](https://docs.expo.dev/versions/latest/sdk/audio/#audiorecorder)`
### `useAudioRecorderState(recorder, interval)`
Android
iOS
Web
Parameter| Type  
---|---  
recorder| `AudioRecorder[](https://docs.expo.dev/versions/latest/sdk/audio/#audiorecorder)`  
interval(optional)| `number`  
Returns:
`RecorderState[](https://docs.expo.dev/versions/latest/sdk/audio/#recorderstate)`
### `useAudioSampleListener(player, listener)`
Android
iOS
Web
Parameter| Type  
---|---  
player|   
listener| `(data: AudioSample[](https://docs.expo.dev/versions/latest/sdk/audio/#audiosample)) => void`  
Returns:
`void`
## Classes
### `AudioPlayer`
Android
iOS
Web
Type: Class extends `SharedObject[](https://docs.expo.dev/versions/v52.0.0/sdk/expo#sharedobject)<>`
AudioPlayer Properties
### `currentTime`
Android
iOS
Web
Type: `number`
The current position through the audio item, in seconds.
### `duration`
Android
iOS
Web
Type: `number`
The total duration of the audio in seconds.
### `id`
Android
iOS
Web
Type: `number`
Unique identifier for the player object.
### `isAudioSamplingSupported`
Android
iOS
Web
Type: `boolean`
Boolean value indicating whether audio sampling is supported on the platform.
### `isBuffering`
Android
iOS
Web
Type: `boolean`
Boolean value indicating whether the player is buffering.
### `isLoaded`
Android
iOS
Web
Type: `boolean`
Boolean value indicating whether the player is finished loading.
### `loop`
Android
iOS
Web
Type: `boolean`
Boolean value indicating whether the player is currently looping.
### `muted`
Android
iOS
Web
Type: `boolean`
Boolean value indicating whether the player is currently muted.
### `paused`
Android
iOS
Web
Type: `boolean`
Boolean value indicating whether the player is currently paused.
### `playbackRate`
Android
iOS
Web
Type: `number`
The current playback rate of the audio.
### `playing`
Android
iOS
Web
Type: `boolean`
Boolean value indicating whether the player is currently playing.
### `shouldCorrectPitch`
Android
iOS
Web
Type: `boolean`
A boolean describing if we are correcting the pitch for a changed rate.
### `volume`
Android
iOS
Web
Type: `number`
The current volume of the audio.
AudioPlayer Methods
### `pause()`
Android
iOS
Web
Pauses the player.
Returns:
`void`
### `play()`
Android
iOS
Web
Start playing audio.
Returns:
`void`
### `remove()`
Android
iOS
Web
Remove the player from memory to free up resources.
Returns:
`void`
### `replace(source)`
Android
iOS
Web
Parameter| Type  
---|---  
source|   
Replaces the current audio source with a new one.
Returns:
`void`
### `seekTo(seconds)`
Android
iOS
Web
Parameter| Type| Description  
---|---|---  
seconds| `number`| The number of seconds to seek by.  
Seeks the playback by the given number of seconds.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `setPlaybackRate(rate, pitchCorrectionQuality)`
Android
iOS
Web
Parameter| Type| Description  
---|---|---  
rate| `number`| The playback rate of the audio.  
pitchCorrectionQuality(optional)| `PitchCorrectionQuality[](https://docs.expo.dev/versions/latest/sdk/audio/#pitchcorrectionquality)`| The quality of the pitch correction.  
Sets the current playback rate of the audio.
Returns:
`void`
### `AudioRecorder`
Android
iOS
Web
Type: Class extends `SharedObject[](https://docs.expo.dev/versions/v52.0.0/sdk/expo#sharedobject)<>`
AudioRecorder Properties
### `currentTime`
Android
iOS
Web
Type: `number`
The current length of the recording, in seconds.
### `id`
Android
iOS
Web
Type: `number`
Unique identifier for the recorder object.
### `isRecording`
Android
iOS
Web
Type: `boolean`
Boolean value indicating whether the recording is in progress.
### `uri`
Android
iOS
Web
Literal type: `union`
The uri of the recording.
Acceptable values are: `null` | `string`
AudioRecorder Methods
### `getAvailableInputs()`
Android
iOS
Web
Returns a list of available recording inputs. This method can only be called if the `Recording` has been prepared.
Returns:
`RecordingInput[][](https://docs.expo.dev/versions/latest/sdk/audio/#recordinginput)`
A `Promise` that is fulfilled with an array of `RecordingInput` objects.
### `getCurrentInput()`
Android
iOS
Web
Returns the currently-selected recording input. This method can only be called if the `Recording` has been prepared.
Returns:
`RecordingInput[](https://docs.expo.dev/versions/latest/sdk/audio/#recordinginput)`
A `Promise` that is fulfilled with a `RecordingInput` object.
### `getStatus()`
Android
iOS
Web
Status of the current recording.
Returns:
`RecorderState[](https://docs.expo.dev/versions/latest/sdk/audio/#recorderstate)`
### `pause()`
Android
iOS
Web
Pause the recording.
Returns:
`void`
### `prepareToRecordAsync(options)`
Android
iOS
Web
Parameter| Type  
---|---  
options(optional)| `Partial[](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)<>`  
Prepares the recording for recording.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `record()`
Android
iOS
Web
Starts the recording.
Returns:
`void`
### `recordForDuration(seconds)`
Android
iOS
Web
Parameter| Type| Description  
---|---|---  
seconds| `number`| The time in seconds to stop recording at.  
Stops the recording once the specified time has elapsed.
Returns:
`void`
### `setInput(inputUid)`
Android
iOS
Web
Parameter| Type| Description  
---|---|---  
inputUid| `string`| The uid of a `RecordingInput`.  
Sets the current recording input.
Returns:
`void`
A `Promise` that is resolved if successful or rejected if not.
### `startRecordingAtTime(seconds)`
Android
iOS
Web
Parameter| Type| Description  
---|---|---  
seconds| `number`| The time in seconds to start recording at.  
Starts the recording at the given time.
Returns:
`void`
### `stop()`
Android
iOS
Web
Stop the recording.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
## Methods
### `Audio.getRecordingPermissionsAsync()`
Android
iOS
Web
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/audio/#permissionresponse)>`
### `Audio.requestRecordingPermissionsAsync()`
Android
iOS
Web
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/audio/#permissionresponse)>`
### `Audio.setAudioModeAsync(mode)`
Android
iOS
Web
Parameter| Type  
---|---  
mode| `Partial[](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)<>`  
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `Audio.setIsAudioActiveAsync(active)`
Android
iOS
Web
Parameter| Type  
---|---  
active| `boolean`  
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
## Event Subscriptions
### `Audio.useAudioSampleListener(player, listener)`
Android
iOS
Web
Parameter| Type  
---|---  
player|   
listener| `(data: AudioSample[](https://docs.expo.dev/versions/latest/sdk/audio/#audiosample)) => void`  
Returns:
`void`
## Interfaces
### `PermissionResponse`
Android
iOS
Web
An object obtained by permissions get and request functions.
Property| Type| Description  
---|---|---  
canAskAgain| `boolean`| Indicates if user can be asked again for specific permission. If not, one should be directed to the Settings app in order to enable/disable the permission.  
expires| `PermissionExpiration[](https://docs.expo.dev/versions/latest/sdk/audio/#permissionexpiration)`| Determines time when the permission expires.  
granted| `boolean`| A convenience boolean that indicates if the permission is granted.  
status| `PermissionStatus[](https://docs.expo.dev/versions/latest/sdk/audio/#permissionstatus)`| Determines the status of the permission.  
## Types
### `AndroidAudioEncoder`
Android
iOS
Web
Literal Type: `string`
Acceptable values are: `'default'` | `'amr_nb'` | `'amr_wb'` | `'aac'` | `'he_aac'` | `'aac_eld'`
### `AndroidOutputFormat`
Android
iOS
Web
Literal Type: `string`
Acceptable values are: `'default'` | `'3gp'` | `'mpeg4'` | `'amrnb'` | `'amrwb'` | `'aac_adts'` | `'mpeg2ts'` | `'webm'`
### `AudioEvents`
Android
iOS
Web
Property| Type| Description  
---|---|---  
audioSampleUpdate| `(data: AudioSample[](https://docs.expo.dev/versions/latest/sdk/audio/#audiosample)) => void`  
playbackStatusUpdate| `(status: AudioStatus[](https://docs.expo.dev/versions/latest/sdk/audio/#audiostatus)) => void`  
### `AudioMode`
Android
iOS
Web
Property| Type| Description  
---|---|---  
allowsRecording| `boolean`  
interruptionMode| `InterruptionMode[](https://docs.expo.dev/versions/latest/sdk/audio/#interruptionmode)`  
playsInSilentMode| `boolean`  
shouldPlayInBackground| `boolean`  
shouldRouteThroughEarpiece| `boolean`  
### `AudioSample`
Android
iOS
Web
Property| Type| Description  
---|---|---  
channels| `AudioSampleChannel[][](https://docs.expo.dev/versions/latest/sdk/audio/#audiosamplechannel)`  
timestamp| `number`  
### `AudioSampleChannel`
Android
iOS
Web
Property| Type| Description  
---|---|---  
frames| `number[]`  
### `AudioSource`
Android
iOS
Web
Type: `string` or `null` or `object` shaped as below:
Property| Type| Description  
---|---|---  
headers(optional)| `Record<string, string>`| An object representing the HTTP headers to send along with the request for a remote audio source. On web requires the `Access-Control-Allow-Origin` header returned by the server to include the current domain.  
uri(optional)| `string`| A string representing the resource identifier for the audio, which could be an HTTPS address, a local file path, or the name of a static audio file resource.  
### `AudioStatus`
Android
iOS
Web
Property| Type| Description  
---|---|---  
currentTime| `number`  
duration| `number`  
id| `number`  
isBuffering| `boolean`  
isLoaded| `boolean`  
loop| `boolean`  
mute| `boolean`  
playbackRate| `number`  
playbackState| `string`  
playing| `boolean`  
reasonForWaitingToPlay| `string`  
shouldCorrectPitch| `boolean`  
timeControlStatus| `string`  
### `BitRateStrategy`
Android
iOS
Web
Literal Type: `string`
Acceptable values are: `'constant'` | `'longTermAverage'` | `'variableConstrained'` | `'variable'`
### `InterruptionMode`
Android
iOS
Web
Literal Type: `string`
Acceptable values are: `'mixWithOthers'` | `'doNotMix'` | `'duckOthers'`
### `PermissionExpiration`
Android
iOS
Web
Literal Type: `union`
Permission expiration time. Currently, all permissions are granted permanently.
Acceptable values are: `'never'` | `number`
### `PitchCorrectionQuality`
Android
iOS
Web
Literal Type: `string`
Acceptable values are: `'low'` | `'medium'` | `'high'`
### `RecorderState`
Android
iOS
Web
Property| Type| Description  
---|---|---  
canRecord| `boolean`  
durationMillis| `number`  
isRecording| `boolean`  
mediaServicesDidReset| `boolean`  
metering(optional)| `number`  
url| `string | null`  
### `RecordingEvents`
Android
iOS
Web
Property| Type| Description  
---|---|---  
recordingStatusUpdate| `(status: RecordingStatus[](https://docs.expo.dev/versions/latest/sdk/audio/#recordingstatus)) => void`  
### `RecordingInput`
Android
iOS
Web
Property| Type| Description  
---|---|---  
name| `string`  
type| `string`  
uid| `string`  
### `RecordingOptions`
Android
iOS
Web
Property| Type| Description  
---|---|---  
android| `RecordingOptionsAndroid[](https://docs.expo.dev/versions/latest/sdk/audio/#recordingoptionsandroid)`| Recording options for the Android platform.  
bitRate| `number`| The desired bit rate.Example`128000`  
extension| `string`| The desired file extension.Example`.caf`  
ios| `RecordingOptionsIos[](https://docs.expo.dev/versions/latest/sdk/audio/#recordingoptionsios)`| Recording options for the iOS platform.  
numberOfChannels| `number`| The desired number of channels.Example`2`  
sampleRate| `number`| The desired sample rate.Example`44100`  
web(optional)| `RecordingOptionsWeb[](https://docs.expo.dev/versions/latest/sdk/audio/#recordingoptionsweb)`| Recording options for the Web platform.  
### `RecordingOptionsAndroid`
Android
iOS
Web
Property| Type| Description  
---|---|---  
audioEncoder| `AndroidAudioEncoder[](https://docs.expo.dev/versions/latest/sdk/audio/#androidaudioencoder)`| The desired audio encoder. See the [`AndroidAudioEncoder`](https://docs.expo.dev/versions/latest/sdk/audio/#androidaudioencoder) enum for all valid values.  
extension(optional)| `string`| The desired file extension.Example`.caf`  
maxFileSize(optional)| `number`| The desired maximum file size in bytes, after which the recording will stop (but `stopAndUnloadAsync()` must still be called after this point).Example`65536`  
outputFormat| `AndroidOutputFormat[](https://docs.expo.dev/versions/latest/sdk/audio/#androidoutputformat)`| The desired file format. See the [`AndroidOutputFormat`](https://docs.expo.dev/versions/latest/sdk/audio/#androidoutputformat) enum for all valid values.  
sampleRate(optional)| `number`| The desired sample rate.Example`44100`  
### `RecordingOptionsIos`
Android
iOS
Web
Property| Type| Description  
---|---|---  
audioQuality| `number`| The desired audio quality. See the [`AudioQuality`](https://docs.expo.dev/versions/latest/sdk/audio/#audioquality) enum for all valid values.  
bitDepthHint(optional)| `number`| The desired bit depth hint.Example`16`  
bitRateStrategy(optional)| `number`| The desired bit rate strategy. See the next section for an enumeration of all valid values of `bitRateStrategy`.  
extension(optional)| `string`| The desired file extension.Example`.caf`  
linearPCMBitDepth(optional)| `number`| The desired PCM bit depth.Example`16`  
linearPCMIsBigEndian(optional)| `boolean`| A boolean describing if the PCM data should be formatted in big endian.  
linearPCMIsFloat(optional)| `boolean`| A boolean describing if the PCM data should be encoded in floating point or integral values.  
outputFormat(optional)| `string | number`| The desired file format. See the [`IOSOutputFormat`](https://docs.expo.dev/versions/latest/sdk/audio/#iosoutputformat) enum for all valid values.  
sampleRate(optional)| `number`| The desired sample rate.Example`44100`  
### `RecordingOptionsWeb`
Android
iOS
Web
Property| Type| Description  
---|---|---  
bitsPerSecond(optional)| `number`  
mimeType(optional)| `string`  
### `RecordingStatus`
Android
iOS
Web
Property| Type| Description  
---|---|---  
error| `string | null`  
hasError| `boolean`  
id| `number`  
isFinished| `boolean`  
url| `string | null`  
## Enums
### `AudioQuality`
Android
iOS
Web
#### `MIN`
`AudioQuality.MIN ＝ 0`
#### `LOW`
`AudioQuality.LOW ＝ 32`
#### `MEDIUM`
`AudioQuality.MEDIUM ＝ 64`
#### `HIGH`
`AudioQuality.HIGH ＝ 96`
#### `MAX`
`AudioQuality.MAX ＝ 127`
### `IOSOutputFormat`
Android
iOS
Web
#### `MPEGLAYER1`
`IOSOutputFormat.MPEGLAYER1 ＝ ".mp1"`
#### `MPEGLAYER2`
`IOSOutputFormat.MPEGLAYER2 ＝ ".mp2"`
#### `MPEGLAYER3`
`IOSOutputFormat.MPEGLAYER3 ＝ ".mp3"`
#### `MPEG4AAC`
`IOSOutputFormat.MPEG4AAC ＝ "aac "`
#### `MPEG4AAC_ELD`
`IOSOutputFormat.MPEG4AAC_ELD ＝ "aace"`
#### `MPEG4AAC_ELD_SBR`
`IOSOutputFormat.MPEG4AAC_ELD_SBR ＝ "aacf"`
#### `MPEG4AAC_ELD_V2`
`IOSOutputFormat.MPEG4AAC_ELD_V2 ＝ "aacg"`
#### `MPEG4AAC_HE`
`IOSOutputFormat.MPEG4AAC_HE ＝ "aach"`
#### `MPEG4AAC_LD`
`IOSOutputFormat.MPEG4AAC_LD ＝ "aacl"`
#### `MPEG4AAC_HE_V2`
`IOSOutputFormat.MPEG4AAC_HE_V2 ＝ "aacp"`
#### `MPEG4AAC_SPATIAL`
`IOSOutputFormat.MPEG4AAC_SPATIAL ＝ "aacs"`
#### `AC3`
`IOSOutputFormat.AC3 ＝ "ac-3"`
#### `AES3`
`IOSOutputFormat.AES3 ＝ "aes3"`
#### `APPLELOSSLESS`
`IOSOutputFormat.APPLELOSSLESS ＝ "alac"`
#### `ALAW`
`IOSOutputFormat.ALAW ＝ "alaw"`
#### `AUDIBLE`
`IOSOutputFormat.AUDIBLE ＝ "AUDB"`
#### `60958AC3`
`IOSOutputFormat.60958AC3 ＝ "cac3"`
#### `MPEG4CELP`
`IOSOutputFormat.MPEG4CELP ＝ "celp"`
#### `ENHANCEDAC3`
`IOSOutputFormat.ENHANCEDAC3 ＝ "ec-3"`
#### `MPEG4HVXC`
`IOSOutputFormat.MPEG4HVXC ＝ "hvxc"`
#### `ILBC`
`IOSOutputFormat.ILBC ＝ "ilbc"`
#### `APPLEIMA4`
`IOSOutputFormat.APPLEIMA4 ＝ "ima4"`
#### `LINEARPCM`
`IOSOutputFormat.LINEARPCM ＝ "lpcm"`
#### `MACE3`
`IOSOutputFormat.MACE3 ＝ "MAC3"`
#### `MACE6`
`IOSOutputFormat.MACE6 ＝ "MAC6"`
#### `AMR`
`IOSOutputFormat.AMR ＝ "samr"`
#### `AMR_WB`
`IOSOutputFormat.AMR_WB ＝ "sawb"`
#### `DVIINTELIMA`
`IOSOutputFormat.DVIINTELIMA ＝ 1836253201`
#### `MICROSOFTGSM`
`IOSOutputFormat.MICROSOFTGSM ＝ 1836253233`
#### `QUALCOMM`
`IOSOutputFormat.QUALCOMM ＝ "Qclp"`
#### `QDESIGN2`
`IOSOutputFormat.QDESIGN2 ＝ "QDM2"`
#### `QDESIGN`
`IOSOutputFormat.QDESIGN ＝ "QDMC"`
#### `MPEG4TWINVQ`
`IOSOutputFormat.MPEG4TWINVQ ＝ "twvq"`
#### `ULAW`
`IOSOutputFormat.ULAW ＝ "ulaw"`
### `PermissionStatus`
Android
iOS
Web
#### `DENIED`
`PermissionStatus.DENIED ＝ "denied"`
User has denied the permission.
#### `GRANTED`
`PermissionStatus.GRANTED ＝ "granted"`
User has granted the permission.
#### `UNDETERMINED`
`PermissionStatus.UNDETERMINED ＝ "undetermined"`
User hasn't granted or denied the permission yet.

