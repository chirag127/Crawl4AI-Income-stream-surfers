---
url: https://docs.expo.dev/archive/push-notifications/notification-channels
title: https://docs.expo.dev/archive/push-notifications/notification-channels
date: 2025-04-30T17:12:40.115285
depth: 2
---

[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Notification Channels
> This page is archived. See [Push Notifications guide](https://docs.expo.dev/push-notifications/overview) for up-to-date information.
Notification channels are a new feature in Android Oreo that give users more control over the notifications they receive. Starting in Android Oreo, every local and push notification must be assigned to a single channel. Users can see all notification channels in their OS Settings, and they can customize the behavior of alerts on a per-channel basis.
Notification channels have no effect and are ignored on all iOS devices.
## Designing channels
Channels give users more control over the various kinds of alerts they want to receive from your app. You should create a channel for each type of notification you might send, such as Alarms, Chat messages, Update notifications, or the like.
According to the Android developer documentation:
> You should create a channel for each distinct type of notification you need to send. You can also create notification channels to reflect choices made by users of your app. For example, you can set up separate notification channels for each conversation group created by a user in a messaging app.
When you create a channel, you can specify various settings for its notifications, such as priority, sound, and vibration. After you create the channel, control switches entirely to the user, who can then customize these settings to their own liking for each channel. Your app can no longer change any of the settings. Although it is possible for your app to programmatically delete channels, Android does not recommend this and keeps a relic on the user's device.
You can read more about notification channels on the [Android developer website](https://developer.android.com/training/notify-user/channels). It's a good idea to put some thought into designing channels that make sense and are useful customization tools for your users.
## Creating and using channels
Creating a channel is easy -- before you create a local notification (or receive a push notification), simply call the following method:
```
if (Platform.OS === 'android') {
 Notifications.createChannelAndroidAsync('chat-messages', {
  name: 'Chat messages',
  sound: true,
 });
}

```

Creating a channel that already exists is essentially a no-op, so it's safe to call this each time your app starts up. For example, the `componentDidMount` of your app's root component might be a good place for this. However, note that you cannot change any settings of a notification channel after it's been created -- only the user can do this. So be sure to plan your channels carefully.
Then, when you want to send a notification for a chat message, either add the `channelId: 'chat-messages'` field to your [push notification message](https://docs.expo.dev/archive/push-notifications#message-format), or create a local notification like this:
```
Notifications.presentLocalNotificationAsync({
 title: 'New Message',
 body: 'Message!!!!',
 android: {
  channelId: 'chat-messages',
 },
});

```

Expo will then present your notification to the user through the `chat-messages` channel, respecting all the user's settings for that channel.
If you create a notification and do not specify a `channelId`, Expo will automatically create a 'Default' channel for you and present the notification through that channel. If, however, you specify a `channelId` that has not yet been created on the device, the notification will not be shown on Android 8+ devices. Therefore, it's important to plan ahead and make sure that you create all the channels you may need before sending out notifications.
On devices with Android 7 and below, which don't support notification channels, Expo will remember the relevant settings you created the channel with (in this case, `sound: true`) and apply them directly to the individual notification before presenting it to the user.
## Updating an existing app to use channels
If you have an existing Android app that relies on `sound`, `vibrate`, or `priority` settings for notifications, you'll need to update it to take advantage of channels, as those settings no longer have any effect on individual notifications. If you do not rely on those settings, you may want to update it anyway to give users more control over the different types of notifications your app presents. (Note that the client-side `priority` setting involved here only affects the notification's UI behavior and is distinct from [the `priority` of a push notification](https://docs.expo.dev/archive/push-notifications#message-format), which is not affected by notification channels.)
To do this, first make sure you are using the latest minor update of `expo` for your SDK version. Notification channels are supported in SDKs 22 and above, so for example, if you're on SDK 27 you should `npm install`/`yarn add` `expo@^27.1.0`.
Next, plan out the notification channels your app will need. These may correspond to the different permutations of the `sound`, `vibrate` and `priority` settings you used on individual notifications.
Once you have decided on a set of channels, you need to add logic to your app to create them. We recommend simply creating all channels in `componentDidMount` of your app's root component; this way all users will be sure to get all channels and not miss any notifications.
For example, if this is your code before:
```
_createNotificationAsync = () => {
 Notifications.presentLocalNotificationAsync({
  title: 'Reminder',
  body: 'This is an important reminder!!!!',
  android: {
   priority: 'max',
   vibrate: [0, 250, 250, 250],
   color: '#FF0000',
  },
 });
};

```

You might change it to something like this:
```
componentDidMount() {
 // ...
 if (Platform.OS === 'android') {
  Notifications.createChannelAndroidAsync('reminders', {
   name: 'Reminders',
   priority: 'max',
   vibrate: [0, 250, 250, 250],
  });
 }
}
// ...
_createNotificationAsync = () => {
 Notifications.presentLocalNotificationAsync({
  title: 'Reminder',
  body: 'This is an important reminder!!!!',
  android: {
   channelId: 'reminders',
   color: '#FF0000',
  },
 });
}

Show More

```

This will create a channel called "Reminders" with default settings of `max` priority and the vibrate pattern `[0, 250, 250, 250]`. Android 8 users can change these settings whenever they want, or even turn off notifications completely for the "Reminders" channel. When `presentLocalNotificationAsync` is called, the OS will read the channel's settings and present the notification accordingly.
## Send channel notification with Expo API service
```
[
 {
  to: 'ExponentPushToken[xxxxxx]',
  title: 'test',
  priority: 'high',
  body: 'test',
  sound: 'default', // android 7.0 , 6, 5 , 4
  channelId: 'chat-messages', // android 8.0 later
 },
];

```


