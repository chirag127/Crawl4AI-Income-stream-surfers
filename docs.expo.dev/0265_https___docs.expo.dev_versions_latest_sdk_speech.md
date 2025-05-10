---
url: https://docs.expo.dev/versions/latest/sdk/speech
title: https://docs.expo.dev/versions/latest/sdk/speech
date: 2025-04-30T17:17:28.202926
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo Speech
A library that provides access to text-to-speech functionality.
Android
iOS
Web
Bundled version:
~13.0.1
`expo-speech` provides an API that allows you to utilize Text-to-speech functionality in your app.
## Installation
Terminal
Copy
`- ``npx expo install expo-speech`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Usage
Speech
```
import { View, StyleSheet, Button } from 'react-native';
import * as Speech from 'expo-speech';
export default function App() {
 const speak = () => {
  const thingToSay = '1';
  Speech.speak(thingToSay);
 };
 return (
  <View style={styles.container}><Button title="Press to hear some words" onPress={speak} /></View>
 );
}
const styles = StyleSheet.create({
 container: {
  flex: 1,
  justifyContent: 'center',
  backgroundColor: '#ecf0f1',
  padding: 8,
 },
});

Show More

```

## API
```
import * as Speech from 'expo-speech';

```

## Constants
### `Speech.maxSpeechInputLength`
Android
iOS
Web
Type: `number`
Maximum possible text length acceptable by `Speech.speak()` method. It is platform-dependent. On iOS, this returns `Number.MAX_VALUE`.
## Methods
### `Speech.getAvailableVoicesAsync()`
Android
iOS
Web
Returns list of all available voices.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
List of `Voice` objects.
### `Speech.isSpeakingAsync()`
Android
iOS
Web
Determine whether the Text-to-speech utility is currently speaking. Will return `true` if speaker is paused.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
Returns a Promise that fulfils with a boolean, `true` if speaking, `false` if not.
### `Speech.pause()`
Android
iOS
Web
Pauses current speech. This method is not available on Android.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `Speech.resume()`
Android
iOS
Web
Resumes speaking previously paused speech or does nothing if there's none. This method is not available on Android.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `Speech.speak(text, options)`
Android
iOS
Web
Parameter| Type| Description  
---|---|---  
text| `string`| The text to be spoken. Cannot be longer than [`Speech.maxSpeechInputLength`](https://docs.expo.dev/versions/latest/sdk/speech/#speechmaxspeechinputlength).  
options(optional)| `SpeechOptions[](https://docs.expo.dev/versions/latest/sdk/speech/#speechoptions)`| A `SpeechOptions` object.Default:`{}`  
Speak out loud the text given options. Calling this when another text is being spoken adds an utterance to queue.
Returns:
`void`
### `Speech.stop()`
Android
iOS
Web
Interrupts current speech and deletes all in queue.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
## Types
### `SpeechEventCallback(this, ev)`
Android
iOS
Web
Parameter| Type  
---|---  
this| `SpeechSynthesisUtterance[](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesisUtterance)`  
ev| `SpeechSynthesisEvent[](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesisEvent)`  
Returns:
`any`
### `SpeechOptions`
Android
iOS
Web
Property| Type| Description  
---|---|---  
_voiceIndex(optional)| `number`  
language(optional)| `string`| The code of a language that should be used to read the `text`, refer to IETF BCP 47 to see valid codes.  
onBoundary(optional)| `NativeBoundaryEventCallback[](https://docs.expo.dev/versions/latest/sdk/speech/#nativeboundaryeventcallback) | SpeechEventCallback[](https://docs.expo.dev/versions/latest/sdk/speech/#speecheventcallback) | null`| A callback that is invoked when the spoken utterance reaches a word.  
onDone(optional)| `() => void | SpeechEventCallback[](https://docs.expo.dev/versions/latest/sdk/speech/#speecheventcallback)`| A callback that is invoked when speaking finishes.  
onError(optional)| `(error: Error[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)) => void | SpeechEventCallback[](https://docs.expo.dev/versions/latest/sdk/speech/#speecheventcallback)`| Only for: AndroidiOSA callback that is invoked when an error occurred while speaking.  
onMark(optional)| `SpeechEventCallback[](https://docs.expo.dev/versions/latest/sdk/speech/#speecheventcallback) | null`  
onPause(optional)| `SpeechEventCallback[](https://docs.expo.dev/versions/latest/sdk/speech/#speecheventcallback) | null`  
onResume(optional)| `SpeechEventCallback[](https://docs.expo.dev/versions/latest/sdk/speech/#speecheventcallback) | null`  
onStart(optional)| `() => void | SpeechEventCallback[](https://docs.expo.dev/versions/latest/sdk/speech/#speecheventcallback)`| A callback that is invoked when speaking starts.  
onStopped(optional)| `() => void | SpeechEventCallback[](https://docs.expo.dev/versions/latest/sdk/speech/#speecheventcallback)`| A callback that is invoked when speaking is stopped by calling `Speech.stop()`.  
pitch(optional)| `number`| Pitch of the voice to speak `text`. `1.0` is the normal pitch.  
rate(optional)| `number`| Rate of the voice to speak `text`. `1.0` is the normal rate.  
voice(optional)| `string`| Voice identifier.  
volume(optional)| `number`| Only for: WebVolume of the voice to speak `text`. A number between `0.0` (muted) and `1.0` (max volume)Default:`1.0`  
### `Voice`
Android
iOS
Web
Object describing the available voices on the device.
Property| Type| Description  
---|---|---  
identifier| `string`| Voice unique identifier.  
language| `string`| Voice language.  
name| `string`| Voice name.  
quality| | Voice quality.  
### `WebVoice`
Android
iOS
Web
Type: extended by:
Property| Type| Description  
---|---|---  
isDefault| `boolean`  
localService| `boolean`  
name| `string`  
voiceURI| `string`  
## Enums
### `VoiceQuality`
Android
iOS
Web
Enum representing the voice quality.
#### `Default`
`VoiceQuality.Default ＝ "Default"`
#### `Enhanced`
`VoiceQuality.Enhanced ＝ "Enhanced"`

