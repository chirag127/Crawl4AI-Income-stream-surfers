---
url: https://docs.expo.dev/push-notifications/receiving-notifications
title: https://docs.expo.dev/push-notifications/receiving-notifications
date: 2025-04-30T17:14:23.273393
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Handle incoming notifications
Learn how to respond to a notification received by your app and take action based on the event.
The [`expo-notifications`](https://docs.expo.dev/versions/latest/sdk/notifications) library contains event listeners that handle how your app responds when receiving a notification.
## Notification event listeners
The [`addNotificationReceivedListener`](https://docs.expo.dev/versions/latest/sdk/notifications#addnotificationreceivedlistenerlistener) and [`addNotificationResponseReceivedListener`](https://docs.expo.dev/versions/latest/sdk/notifications#addnotificationresponsereceivedlistenerlistener) event listeners receive an object when a notification is received or interacted with.
These listeners allow you to add behavior when notifications are received while your app is open and foregrounded and when your app is backgrounded or closed and the user taps on the notification.
```
useEffect(() => {
 registerForPushNotificationsAsync().then(token => setExpoPushToken(token));
 notificationListener.current = Notifications.addNotificationReceivedListener(notification => {
  setNotification(notification);
 });
 responseListener.current = Notifications.addNotificationResponseReceivedListener(response => {
  console.log(response);
 });
 return () => {
  Notifications.removeNotificationSubscription(notificationListener.current);
  Notifications.removeNotificationSubscription(responseListener.current);
 };
}, []);

```
Android notification object example from `addNotificationReceivedListener`
Sample of the `notification` object received by the callback function when using `Notifications.addNotificationReceivedListener`:
```
// console.log(notification);
{
 "request": {
  "trigger": {
   "remoteMessage": {
    "originalPriority": 2,
    "sentTime": 1724782348210,
    "notification": {
     "usesDefaultVibrateSettings": false,
     "color": null,
     "channelId": null,
     "visibility": null,
     "sound": null,
     "tag": null,
     "bodyLocalizationArgs": null,
     "imageUrl": null,
     "title": "Chat App",
     "ticker": null,
     "eventTime": null,
     "body": "New message from John Doe",
     "titleLocalizationKey": null,
     "notificationPriority": null,
     "icon": null,
     "usesDefaultLightSettings": false,
     "sticky": false,
     "link": null,
     "titleLocalizationArgs": null,
     "bodyLocalizationKey": null,
     "usesDefaultSound": false,
     "clickAction": null,
     "localOnly": false,
     "lightSettings": null,
     "notificationCount": null
    },
    "data": {
     "channelId": "default",
     "message": "New message from John Doe",
     "title": "Chat App",
     "body": "{\"senderId\":\"user123\",\"senderName\":\"John Doe\",\"messageId\":\"msg789\",\"conversationId\":\"conversation-456\",\"messageType\":\"text\",\"timestamp\":1724766427}",
     "scopeKey": "@betoatexpo/expo-notifications-app",
     "experienceId": "@betoatexpo/expo-notifications-app",
     "projectId": "51092087-87a4-4b12-8008-145625477434"
    },
    "to": null,
    "ttl": 0,
    "collapseKey": "dev.expo.notificationsapp",
    "messageType": null,
    "priority": 2,
    "from": "115310547649",
    "messageId": "0:1724782348220771%0f02879c0f02879c"
   },
   "channelId": "default",
   "type": "push"
  },
  "content": {
   "autoDismiss": true,
   "title": "Chat App",
   "badge": null,
   "sticky": false,
   "sound": "default",
   "body": "New message from John Doe",
   "subtitle": null,
   "data": {
    "senderId": "user123",
    "senderName": "John Doe",
    "messageId": "msg789",
    "conversationId": "conversation-456",
    "messageType": "text",
    "timestamp": 1724766427
   }
  },
  "identifier": "0:1724782348220771%0f02879c0f02879c"
 },
 "date": 1724782348210
}

Show More

```

You can directly access the notification custom data by logging the `notification.request.content.data` object:
```
// console.log(notification.request.content.data);
{
 "senderId": "user123",
 "senderName": "John Doe",
 "messageId": "msg789",
 "conversationId": "conversation-456",
 "messageType": "text",
 "timestamp": 1724766427
}

```

iOS notification object example from `addNotificationReceivedListener`
Sample of the `notification` object received by the callback function when using `Notifications.addNotificationReceivedListener`:
```
// console.log(notification);
{
 "request": {
  "trigger": {
   "class": "UNPushNotificationTrigger",
   "type": "push",
   "payload": {
    "experienceId": "@betoatexpo/expo-notifications-app",
    "projectId": "51092087-87a4-4b12-8008-145625477434",
    "scopeKey": "@betoatexpo/expo-notifications-app",
    "aps": {
     "thread-id": "",
     "category": "",
     "badge": 1,
     "alert": {
      "subtitle": "Hey there! How's your day going?",
      "title": "Chat App",
      "launch-image": "",
      "body": "New message from John Doe"
     },
     "sound": "default"
    },
    "body": {
     "messageId": "msg789",
     "timestamp": 1724766427,
     "messageType": "text",
     "senderId": "user123",
     "senderName": "John Doe",
     "conversationId": "conversation-456"
    }
   }
  },
  "identifier": "3AEB849E-9059-4D09-BC3B-9A0B104CF062",
  "content": {
   "body": "New message from John Doe",
   "sound": "default",
   "launchImageName": "",
   "badge": 1,
   "subtitle": "Hey there! How's your day going?",
   "title": "Chat App",
   "data": {
    "conversationId": "conversation-456",
    "senderName": "John Doe",
    "senderId": "user123",
    "messageType": "text",
    "timestamp": 1724766427,
    "messageId": "msg789"
   },
   "summaryArgument": null,
   "categoryIdentifier": "",
   "attachments": [],
   "interruptionLevel": "active",
   "threadIdentifier": "",
   "targetContentIdentifier": null,
   "summaryArgumentCount": 0
  }
 },
 "date": 1724798493.0589335
}

Show More

```

You can directly access the notification custom data by logging the `notification.request.content.data` object:
```
// console.log(notification.request.content.data);
{
 "senderId": "user123",
 "senderName": "John Doe",
 "messageId": "msg789",
 "conversationId": "conversation-456",
 "messageType": "text",
 "timestamp": 1724766427
}

```

For more information on these objects, see [`Notification`](https://docs.expo.dev/versions/latest/sdk/notifications#notification) documentation.
## Foreground notification behavior
To handle the behavior when notifications are received when your app is foregrounded, use [`Notifications.setNotificationHandler`](https://docs.expo.dev/versions/latest/sdk/notifications#handling-incoming-notifications-when-the-app-is) with the `handleNotification()` callback to set the following options:
  * `shouldShowAlert`
  * `shouldPlaySound`
  * `shouldSetBadge`

```
Notifications.setNotificationHandler({
 handleNotification: async () => ({
  shouldShowAlert: true,
  shouldPlaySound: false,
  shouldSetBadge: false,
 }),
});

```

## Closed notification behavior
On Android, users can set certain OS-level settings, usually revolving around performance and battery optimization, that can prevent notifications from being delivered when the app is closed. For example, one such setting is the Deep Clear option on OnePlus devices using Android 9 and lower versions.

