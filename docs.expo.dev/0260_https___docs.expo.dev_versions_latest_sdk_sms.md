---
url: https://docs.expo.dev/versions/latest/sdk/sms
title: https://docs.expo.dev/versions/latest/sdk/sms
date: 2025-04-30T17:17:28.192760
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo SMS
A library that provides access to the system's UI/app for sending SMS messages.
Android
iOS
Bundled version:
~13.0.1
`expo-sms` provides access to the system's UI/app for sending SMS messages.
## Installation
Terminal
Copy
`- ``npx expo install expo-sms`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## API
```
import * as SMS from 'expo-sms';

```

## Methods
### `SMS.isAvailableAsync()`
Android
iOS
Determines whether SMS is available. Always returns `false` in the iOS simulator, and in browser.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
Returns a promise that fulfils with a `boolean`, indicating whether SMS is available on this device.
Example
```
const isAvailable = await SMS.isAvailableAsync();
if (isAvailable) {
 // do your SMS stuff here
} else {
 // misfortune... there's no SMS available on this device
}

```

### `SMS.sendSMSAsync(addresses, message, options)`
Android
iOS
Parameter| Type| Description  
---|---|---  
addresses| `string | string[]`| An array of addresses (phone numbers) or single address passed as strings. Those would appear as recipients of the prepared message.  
message| `string`| Message to be sent.  
options(optional)| | A `SMSOptions` object defining additional SMS configuration options.  
Opens the default UI/app for sending SMS messages with prefilled addresses and message.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
Returns a Promise that fulfils with the SMS action is invoked by the user, with corresponding result:
  * If the user cancelled the SMS sending process: `{ result: 'cancelled' }`.
  * If the user has sent/scheduled message for sending: `{ result: 'sent' }`.
  * If the status of the SMS message cannot be determined: `{ result: 'unknown' }`.


Android does not provide information about the status of the SMS message, so on Android devices the Promise will always resolve with `{ result: 'unknown' }`.
> Note: The only feedback collected by this module is whether any message has been sent. That means we do not check actual content of message nor recipients list.
Example
```
const { result } = await SMS.sendSMSAsync(
 ['0123456789', '9876543210'],
 'My sample HelloWorld message',
 {
  attachments: {
   uri: 'path/myfile.png',
   mimeType: 'image/png',
   filename: 'myfile.png',
  },
 }
);

```

## Types
### `SMSAttachment`
Android
iOS
An object that is used to describe an attachment that is included with a SMS message.
Property| Type| Description  
---|---|---  
filename| `string`| The filename of the attachment.  
mimeType| `string`| The mime type of the attachment such as `image/png`.  
uri| `string`| The content URI of the attachment. The URI needs be a content URI so that it can be accessed by other applications outside of Expo. See [FileSystem.getContentUriAsync](https://docs.expo.dev/versions/latest/sdk/filesystem#filesystemgetcontenturiasyncfileuri)).  
### `SMSOptions`
Android
iOS
Property| Type| Description  
---|---|---  
attachments(optional)| ``  
### `SMSResponse`
Android
iOS
Property| Type| Description  
---|---|---  
result| `'unknown' | 'sent' | 'cancelled'`| Status of SMS action invoked by the user.

