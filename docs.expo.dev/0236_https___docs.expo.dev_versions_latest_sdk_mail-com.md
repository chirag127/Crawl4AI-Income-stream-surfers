---
url: https://docs.expo.dev/versions/latest/sdk/mail-composer
title: https://docs.expo.dev/versions/latest/sdk/mail-composer
date: 2025-04-30T17:16:54.572470
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo MailComposer
A library that provides functionality to compose and send emails with the system's specific UI.
Android
iOS (device only)
Web
Bundled version:
~14.0.2
`expo-mail-composer` allows you to compose and send emails quickly and easily using the OS UI. This module can't be used on iOS Simulators since you can't sign into a mail account on them.
## Installation
Terminal
Copy
`- ``npx expo install expo-mail-composer`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## API
```
import * as MailComposer from 'expo-mail-composer';

```

## Methods
### `MailComposer.composeAsync(options)`
Android
iOS
Web
Parameter| Type  
---|---  
options| `MailComposerOptions[](https://docs.expo.dev/versions/latest/sdk/mail-composer/#mailcomposeroptions)`  
Opens a mail modal for iOS and a mail app intent for Android and fills the fields with provided data. On iOS you will need to be signed into the Mail app.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<MailComposerResult[](https://docs.expo.dev/versions/latest/sdk/mail-composer/#mailcomposerresult)>`
A promise fulfilled with an object containing a `status` field that specifies whether an email was sent, saved, or cancelled. Android does not provide this info, so the status is always set as if the email were sent.
### `MailComposer.isAvailableAsync()`
Android
iOS
Web
Determine if the `MailComposer` API can be used in this app.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
A promise resolves to `true` if the API can be used, and `false` otherwise.
  * Returns `true` on iOS when the device has a default email setup for sending mail.
  * Can return `false` on iOS if an MDM profile is setup to block outgoing mail. If this is the case, you may want to use the Linking API instead.
  * Always returns `true` in the browser and on Android.


## Types
### `MailComposerOptions`
Android
iOS
Web
A map defining the data to fill the mail.
Property| Type| Description  
---|---|---  
attachments(optional)| `string[]`| An array of app's internal file URIs to attach.  
bccRecipients(optional)| `string[]`| An array of e-mail addresses of the BCC recipients.  
body(optional)| `string`| Body of the e-mail.  
ccRecipients(optional)| `string[]`| An array of e-mail addresses of the CC recipients.  
isHtml(optional)| `boolean`| Whether the body contains HTML tags so it could be formatted properly. Not working perfectly on Android.  
recipients(optional)| `string[]`| An array of e-mail addresses of the recipients.  
subject(optional)| `string`| Subject of the e-mail.  
### `MailComposerResult`
Android
iOS
Web
Property| Type| Description  
---|---|---  
status| `MailComposerStatus[](https://docs.expo.dev/versions/latest/sdk/mail-composer/#mailcomposerstatus)`  
## Enums
### `MailComposerStatus`
Android
iOS
Web
#### `CANCELLED`
`MailComposerStatus.CANCELLED ＝ "cancelled"`
#### `SAVED`
`MailComposerStatus.SAVED ＝ "saved"`
#### `SENT`
`MailComposerStatus.SENT ＝ "sent"`
#### `UNDETERMINED`
`MailComposerStatus.UNDETERMINED ＝ "undetermined"`

