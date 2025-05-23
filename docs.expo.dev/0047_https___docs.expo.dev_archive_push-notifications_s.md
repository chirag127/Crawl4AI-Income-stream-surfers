---
url: https://docs.expo.dev/archive/push-notifications/sending-notifications-custom-fcm-legacy
title: https://docs.expo.dev/archive/push-notifications/sending-notifications-custom-fcm-legacy
date: 2025-04-30T17:12:45.560855
depth: 2
---

[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Send notifications with FCM legacy server
Learn how to send notifications with FCM legacy server.
> This page is archived. See [Push Notifications guide](https://docs.expo.dev/push-notifications/overview) for up-to-date information.
> For documentation on communicating with the newer FCMv1 service, see [Send notifications with FCMv1 and APNs](https://docs.expo.dev/push-notifications/sending-notifications-custom). This guide is based on [Google's documentation](https://firebase.google.com/docs/cloud-messaging/http-server-ref), and this section covers the basics to get you started.
Communicating with FCM is done by sending a POST request. However, before sending or receiving any notifications, you'll need to follow the steps to [configure FCM](https://docs.expo.dev/push-notifications/push-notifications-setup#android) to configure FCM and get your `FCM-SERVER-KEY`.
```
await fetch('https://fcm.googleapis.com/fcm/send', {
 method: 'POST',
 headers: {
  'Content-Type': 'application/json',
  Authorization: `key=<FCM-SERVER-KEY>`,
 },
 body: JSON.stringify({
  to: '<NATIVE-DEVICE-PUSH-TOKEN>',
  priority: 'normal',
  data: {
   experienceId: '@yourExpoUsername/yourProjectSlug',
   scopeKey: '@yourExpoUsername/yourProjectSlug',
   title: "📧 You've got mail",
   message: 'Hello world! 🌐',
  },
 }),
});

```

The `experienceId` and `scopeKey` fields are required. Otherwise, your notifications will not go through to your app. FCM has a list of supported fields in the [notification payload](https://firebase.google.com/docs/cloud-messaging/http-server-ref#notification-payload-support), and you can see which ones are supported by `expo-notifications` on Android by looking at the [FirebaseRemoteMessage](https://docs.expo.dev/versions/latest/sdk/notifications#firebaseremotemessage).
FCM also provides some [server-side libraries in a few different languages](https://firebase.google.com/docs/cloud-messaging/send-message#node.js) you can use instead of raw `fetch` requests.
### How to find FCM server key
Your FCM server key can be found by making sure you've followed the [configuration steps](https://docs.expo.dev/push-notifications/push-notifications-setup#android), and instead of uploading your FCM key to Expo, you would use that key directly in your server (as the `FCM-SERVER-KEY` in the previous example).
## Payload format
```
{
 "token": native device token string,
 "collapse_key": string that identifies notification as collapsible,
 "priority": "normal" || "high",
 "data": {
  "experienceId": "@yourExpoUsername/yourProjectSlug",
  "scopeKey": "@yourExpoUsername/yourProjectSlug",
  "title": title of your message,
  "message": body of your message,
  "channelId": the android channel ID associated with this notification,
  "categoryId": the category associated with this notification,
  "icon": the icon to show with this notification,
  "link": the link this notification should open,
  "sound": boolean or the custom sound file you'd like to play,
  "vibrate": "true" | "false" | number[],
  "priority": AndroidNotificationPriority, // https://docs.expo.dev/versions/latest/sdk/notifications/#androidnotificationpriority
  "badge": the number to set the icon badge to,
  "body": { object of key-value pairs }
 }
}

Show More

```

### Firebase notification types
There are two types of Firebase Cloud Messaging messages: [notification and data messages](https://firebase.google.com/docs/cloud-messaging/concept-options#notifications_and_data_messages).
  1. Notification messages are only handled (and displayed) by the Firebase library. They don't necessarily wake the app, and `expo-notifications` will not be made aware that your app has received any notification.
  2. Data messages are not handled by the Firebase library. They are immediately handed off to your app for processing. That's where `expo-notifications` interprets the data payload and takes action based on that data. In almost all cases, this is the type of notification you have to send.


If you send a message of type notification instead of data directly through Firebase, you won't know if a user interacted with the notification (no `onNotificationResponse` event available), and you won't be able to parse the notification payload for any data in your notification event-related listeners.
> Using notification-type messages can be beneficial when you need a configuration option that is not yet exposed by `expo-notifications`. Generally, it may lead to less predictable situations than using data-type messages. However, you may need to report any issue you encounter directly to Google.
Below is an example of each type using Node.js Firebase Admin SDK to send data-type messages instead of notification-type:
```
const devicePushToken = /* ... */;
const options = /* ... */;
// ❌ The following payload has a root-level notification object and
// it will not trigger expo-notifications and may not work as expected.
admin.messaging().sendToDevice(
 devicePushToken,
 {
  notification: {
   title: "This is a notification-type message",
   body: "`expo-notifications` will never see this 😢",
  },
  data: {
   photoId: 42,
  },
 },
 options
);
// ✅ There is no "notification" key in the root level of the payload
// so the message is a "data" message, thus triggering expo-notifications.
admin.messaging().sendToDevice(
 devicePushToken,
 {
  data: {
   title: "This is a data-type message",
   message: "`expo-notifications` events will be triggered 🤗",
   // ⚠️ Notice the schema of this payload is different
   // than that of Firebase SDK. What is there called "body"
   // here is a "message". For more info see:
   // https://docs.expo.dev/versions/latest/sdk/notifications/#android-push-notification-payload-specification
   body:               // As per Android payload format specified above, the
    JSON.stringify({ photoId: 42 }), // additional "data" should be placed under "body" key.
  },
 },
 options
);

Show More

```


