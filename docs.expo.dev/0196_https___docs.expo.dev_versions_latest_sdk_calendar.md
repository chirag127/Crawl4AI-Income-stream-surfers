---
url: https://docs.expo.dev/versions/latest/sdk/calendar
title: https://docs.expo.dev/versions/latest/sdk/calendar
date: 2025-04-30T17:15:47.405918
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo Calendar
A library that provides an API for interacting with the device's system calendars, events, reminders, and associated records.
Android
iOS
Bundled version:
~14.0.6
`expo-calendar` provides an API for interacting with the device's system calendars, events, reminders, and associated records.
Additionally, it provides methods to launch the [system-provided calendar UI](https://docs.expo.dev/versions/latest/sdk/calendar#launching-system-provided-calendar-dialogs) to allow user view or edit events. On Android, these methods start the system calendar app using an Intent. On iOS, they present either [`EKEventViewController`](https://developer.apple.com/documentation/eventkitui/ekeventviewcontroller) or [`EKEventEditViewController`](https://developer.apple.com/documentation/eventkitui/ekeventeditviewcontroller) as a modal.
## Installation
Terminal
Copy
`- ``npx expo install expo-calendar`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Configuration in app config
You can configure `expo-calendar` using its built-in [config plugin](https://docs.expo.dev/config-plugins/introduction) if you use config plugins in your project ([EAS Build](https://docs.expo.dev/build/introduction) or `npx expo run:[android|ios]`). The plugin allows you to configure various properties that cannot be set at runtime and require building a new app binary to take effect.
### Example app.json with config plugin
app.json
Copy
```
{
 "expo": {
  "plugins": [
   [
    "expo-calendar",
    {
     "calendarPermission": "The app needs to access your calendar."
    }
   ]
  ]
 }
}

```

### Configurable properties
Name| Default| Description  
---|---|---  
`calendarPermission`| `"Allow $(PRODUCT_NAME) to access your calendar"`| Only for: iOSA string to set the [`NSCalendarsUsageDescription`](https://docs.expo.dev/versions/latest/sdk/calendar/#ios) permission message.  
`remindersPermission`| `"Allow $(PRODUCT_NAME) to access your reminders"`| Only for: iOSA string to set the [`NSRemindersUsageDescription`](https://docs.expo.dev/versions/latest/sdk/calendar/#ios) permission message.  
Are you using this library in an existing React Native app?
If you're not using Continuous Native Generation ([CNG](https://docs.expo.dev/workflow/continuous-native-generation)) (you're using native android and ios projects manually), then you need to configure following permissions in your native projects:
  * For Android, add `android.permission.READ_CALENDAR` and `android.permission.WRITE_CALENDAR` permissions to your project's android/app/src/main/AndroidManifest.xml:
```
<uses-permission android:name="android.permission.READ_CALENDAR" />
<uses-permission android:name="android.permission.WRITE_CALENDAR" />

```

  * For iOS, add `NSCalendarsUsageDescription` and `NSRemindersUsageDescription` to your project's ios/[app]/Info.plist:
```
<key>NSCalendarsUsageDescription</key>
<string>Allow $(PRODUCT_NAME) to access your calendar</string>
<key>NSRemindersUsageDescription</key>
<string>Allow $(PRODUCT_NAME) to access your reminders</string>

```



## Usage
Basic Calendar usage
```
import { useEffect } from 'react';
import { StyleSheet, View, Text, Button, Platform } from 'react-native';
import * as Calendar from 'expo-calendar';
export default function App() {
 useEffect(() => {
  (async () => {
   const { status } = await Calendar.requestCalendarPermissionsAsync();
   if (status === 'granted') {
    const calendars = await Calendar.getCalendarsAsync(Calendar.EntityTypes.EVENT);
    console.log('Here are all your calendars:');
    console.log({ calendars });
   }
  })();
 }, []);
 return (
  <View style={styles.container}><Text>Calendar Module Example</Text><Button title="Create a new calendar" onPress={createCalendar} /></View>
 );
}
async function getDefaultCalendarSource() {
 const defaultCalendar = await Calendar.getDefaultCalendarAsync();
 return defaultCalendar.source;
}
async function createCalendar() {
 const defaultCalendarSource =
  Platform.OS === 'ios'
   ? await getDefaultCalendarSource()
   : { isLocalAccount: true, name: 'Expo Calendar' };
 const newCalendarID = await Calendar.createCalendarAsync({
  title: 'Expo Calendar',
  color: 'blue',
  entityType: Calendar.EntityTypes.EVENT,
  sourceId: defaultCalendarSource.id,
  source: defaultCalendarSource,
  name: 'internalCalendarName',
  ownerAccount: 'personal',
  accessLevel: Calendar.CalendarAccessLevel.OWNER,
 });
 console.log(`Your new calendar ID is: ${newCalendarID}`);
}
const styles = StyleSheet.create({
 container: {
  flex: 1,
  backgroundColor: '#fff',
  alignItems: 'center',
  justifyContent: 'space-around',
 },
});

Show More

```

## API
```
import * as Calendar from 'expo-calendar';

```

## Launching system-provided calendar dialogs
### `createEventInCalendarAsync(eventData, presentationOptions)`
Android
iOS
Parameter| Type| Description  
---|---|---  
eventData(optional)| `Omit[](https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys)<Partial[](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)<>, 'id'>`| A map of details for the event to be created.Default:`{}`  
presentationOptions(optional)| `PresentationOptions[](https://docs.expo.dev/versions/latest/sdk/calendar/#presentationoptions)`| Configuration that influences how the calendar UI is presented.  
Launches the calendar UI provided by the OS to create a new event.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<DialogEventResult[](https://docs.expo.dev/versions/latest/sdk/calendar/#dialogeventresult)>`
A promise which resolves with information about the dialog result.
### `editEventInCalendarAsync(params, presentationOptions)`
Android
iOS
Parameter| Type  
---|---  
params| `CalendarDialogParams[](https://docs.expo.dev/versions/latest/sdk/calendar/#calendardialogparams)`  
presentationOptions(optional)| `PresentationOptions[](https://docs.expo.dev/versions/latest/sdk/calendar/#presentationoptions)`  
Launches the calendar UI provided by the OS to edit or delete an event. On Android, this is the same as `openEventInCalendarAsync`.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<DialogEventResult[](https://docs.expo.dev/versions/latest/sdk/calendar/#dialogeventresult)>`
A promise which resolves with information about the dialog result.
> Deprecated Use [`openEventInCalendarAsync`](https://docs.expo.dev/versions/latest/sdk/calendar/#openeventincalendarasyncparams-presentationoptions) instead.
### `openEventInCalendar(id)`
Android
Parameter| Type| Description  
---|---|---  
id| `string`| ID of the event to open.  
Sends an intent to open the specified event in the OS Calendar app.
Returns:
`void`
### `openEventInCalendarAsync(params, presentationOptions)`
Android
iOS
Parameter| Type  
---|---  
params| `CalendarDialogParams[](https://docs.expo.dev/versions/latest/sdk/calendar/#calendardialogparams)`  
presentationOptions(optional)| `OpenEventPresentationOptions[](https://docs.expo.dev/versions/latest/sdk/calendar/#openeventpresentationoptions)`  
Launches the calendar UI provided by the OS to preview an event.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<OpenEventDialogResult[](https://docs.expo.dev/versions/latest/sdk/calendar/#openeventdialogresult)>`
A promise which resolves with information about the dialog result.
## Hooks
### `useCalendarPermissions(options)`
Android
iOS
Parameter| Type  
---|---  
options(optional)| `PermissionHookOptions[](https://docs.expo.dev/versions/latest/sdk/calendar/#permissionhookoptions)<object>`  
Check or request permissions to access the calendar. This uses both `getCalendarPermissionsAsync` and `requestCalendarPermissionsAsync` to interact with the permissions.
Returns:
`[null | PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/calendar/#permissionresponse), RequestPermissionMethod<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/calendar/#permissionresponse)>, GetPermissionMethod<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/calendar/#permissionresponse)>]`
Example
```
const [status, requestPermission] = Calendar.useCalendarPermissions();

```

### `useRemindersPermissions(options)`
Android
iOS
Parameter| Type  
---|---  
options(optional)| `PermissionHookOptions[](https://docs.expo.dev/versions/latest/sdk/calendar/#permissionhookoptions)<object>`  
Check or request permissions to access reminders. This uses both `getRemindersPermissionsAsync` and `requestRemindersPermissionsAsync` to interact with the permissions.
Returns:
`[null | PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/calendar/#permissionresponse), RequestPermissionMethod<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/calendar/#permissionresponse)>, GetPermissionMethod<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/calendar/#permissionresponse)>]`
Example
```
const [status, requestPermission] = Calendar.useRemindersPermissions();

```

## Methods
### `Calendar.createAttendeeAsync(eventId, details)`
Android
Parameter| Type| Description  
---|---|---  
eventId| `string`| ID of the event to add this attendee to.  
details(optional)| `Partial[](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)<>`| A map of details for the attendee to be created.Default:`{}`  
Creates a new attendee record and adds it to the specified event. Note that if `eventId` specifies a recurring event, this will add the attendee to every instance of the event.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<string>`
A string representing the ID of the newly created attendee record.
### `Calendar.createCalendarAsync(details)`
Android
iOS
Parameter| Type| Description  
---|---|---  
details(optional)| `Partial[](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)<>`| A map of details for the calendar to be created.Default:`{}`  
Creates a new calendar on the device, allowing events to be added later and displayed in the OS Calendar app.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<string>`
A string representing the ID of the newly created calendar.
### `Calendar.createEventAsync(calendarId, eventData)`
Android
iOS
Parameter| Type| Description  
---|---|---  
calendarId| `string`| ID of the calendar to create this event in.  
eventData(optional)| `Omit[](https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys)<Partial[](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)<>, 'id'>`| A map of details for the event to be created.Default:`{}`  
Creates a new event on the specified calendar.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<string>`
A promise which fulfils with a string representing the ID of the newly created event.
### `Calendar.createReminderAsync(calendarId, reminder)`
iOS
Parameter| Type| Description  
---|---|---  
calendarId| `null | string`| ID of the calendar to create this reminder in (or `null` to add the calendar to the OS-specified default calendar for reminders).  
reminder(optional)| | A map of details for the reminder to be createdDefault:`{}`  
Creates a new reminder on the specified calendar.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<string>`
A promise which fulfils with a string representing the ID of the newly created reminder.
### `Calendar.deleteAttendeeAsync(id)`
Android
Parameter| Type| Description  
---|---|---  
id| `string`| ID of the attendee to delete.  
Deletes an existing attendee record from the device. Use with caution.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `Calendar.deleteCalendarAsync(id)`
Android
iOS
Parameter| Type| Description  
---|---|---  
id| `string`| ID of the calendar to delete.  
Deletes an existing calendar and all associated events/reminders/attendees from the device. Use with caution.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `Calendar.deleteEventAsync(id, recurringEventOptions)`
Android
iOS
Parameter| Type| Description  
---|---|---  
id| `string`| ID of the event to be deleted.  
recurringEventOptions(optional)| `RecurringEventOptions[](https://docs.expo.dev/versions/latest/sdk/calendar/#recurringeventoptions)`| A map of options for recurring events.Default:`{}`  
Deletes an existing event from the device. Use with caution.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `Calendar.deleteReminderAsync(id)`
iOS
Parameter| Type| Description  
---|---|---  
id| `string`| ID of the reminder to be deleted.  
Deletes an existing reminder from the device. Use with caution.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `Calendar.getAttendeesForEventAsync(id, recurringEventOptions)`
Android
iOS
Parameter| Type| Description  
---|---|---  
id| `string`| ID of the event to return attendees for.  
recurringEventOptions(optional)| `RecurringEventOptions[](https://docs.expo.dev/versions/latest/sdk/calendar/#recurringeventoptions)`| A map of options for recurring events.Default:`{}`  
Gets all attendees for a given event (or instance of a recurring event).
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
A promise which fulfils with an array of [`Attendee`](https://docs.expo.dev/versions/latest/sdk/calendar/#attendee) associated with the specified event.
### `Calendar.getCalendarPermissionsAsync()`
Android
iOS
Checks user's permissions for accessing user's calendars.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/calendar/#permissionresponse)>`
A promise that resolves to an object of type [`PermissionResponse`](https://docs.expo.dev/versions/latest/sdk/calendar/#permissionresponse).
### `Calendar.getCalendarsAsync(entityType)`
Android
iOS
Parameter| Type| Description  
---|---|---  
entityType(optional)| `string`| iOS Only. Not required, but if defined, filters the returned calendars to a specific entity type. Possible values are `Calendar.EntityTypes.EVENT` (for calendars shown in the Calendar app) and `Calendar.EntityTypes.REMINDER` (for the Reminders app).
> Note: If not defined, you will need both permissions: CALENDAR and REMINDERS.  
Gets an array of calendar objects with details about the different calendars stored on the device.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
An array of [calendar objects](https://docs.expo.dev/versions/latest/sdk/calendar/#calendar) matching the provided entity type (if provided).
### `Calendar.getDefaultCalendarAsync()`
iOS
Gets an instance of the default calendar object.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
A promise resolving to the [Calendar](https://docs.expo.dev/versions/latest/sdk/calendar/#calendar) object that is the user's default calendar.
### `Calendar.getEventAsync(id, recurringEventOptions)`
Android
iOS
Parameter| Type| Description  
---|---|---  
id| `string`| ID of the event to return.  
recurringEventOptions(optional)| `RecurringEventOptions[](https://docs.expo.dev/versions/latest/sdk/calendar/#recurringeventoptions)`| A map of options for recurring events.Default:`{}`  
Returns a specific event selected by ID. If a specific instance of a recurring event is desired, the start date of this instance must also be provided, as instances of recurring events do not have their own unique and stable IDs on either iOS or Android.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
A promise which fulfils with an [`Event`](https://docs.expo.dev/versions/latest/sdk/calendar/#event) object matching the provided criteria, if one exists.
### `Calendar.getEventsAsync(calendarIds, startDate, endDate)`
Android
iOS
Parameter| Type| Description  
---|---|---  
calendarIds| `string[]`| Array of IDs of calendars to search for events in.  
startDate| | Beginning of time period to search for events in.  
endDate| | End of time period to search for events in.  
Returns all events in a given set of calendars over a specified time period. The filtering has slightly different behavior per-platform - on iOS, all events that overlap at all with the `[startDate, endDate]` interval are returned, whereas on Android, only events that begin on or after the `startDate` and end on or before the `endDate` will be returned.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
A promise which fulfils with an array of [`Event`](https://docs.expo.dev/versions/latest/sdk/calendar/#event) objects matching the search criteria.
### `Calendar.getReminderAsync(id)`
iOS
Parameter| Type| Description  
---|---|---  
id| `string`| ID of the reminder to return.  
Returns a specific reminder selected by ID.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
A promise which fulfils with a [`Reminder`](https://docs.expo.dev/versions/latest/sdk/calendar/#reminder) matching the provided ID, if one exists.
### `Calendar.getRemindersAsync(calendarIds, status, startDate, endDate)`
iOS
Parameter| Type| Description  
---|---|---  
calendarIds| `(null | string)[]`| Array of IDs of calendars to search for reminders in.  
status| `null | `| One of `Calendar.ReminderStatus.COMPLETED` or `Calendar.ReminderStatus.INCOMPLETE`.  
startDate| | Beginning of time period to search for reminders in. Required if `status` is defined.  
endDate| | End of time period to search for reminders in. Required if `status` is defined.  
Returns a list of reminders matching the provided criteria. If `startDate` and `endDate` are defined, returns all reminders that overlap at all with the [startDate, endDate] interval - i.e. all reminders that end after the `startDate` or begin before the `endDate`.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
A promise which fulfils with an array of [`Reminder`](https://docs.expo.dev/versions/latest/sdk/calendar/#reminder) objects matching the search criteria.
### `Calendar.getRemindersPermissionsAsync()`
iOS
Checks user's permissions for accessing user's reminders.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/calendar/#permissionresponse)>`
A promise that resolves to an object of type [`PermissionResponse`](https://docs.expo.dev/versions/latest/sdk/calendar/#permissionresponse).
### `Calendar.getSourceAsync(id)`
iOS
Parameter| Type| Description  
---|---|---  
id| `string`| ID of the source to return.  
Returns a specific source selected by ID.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
A promise which fulfils with an array of [`Source`](https://docs.expo.dev/versions/latest/sdk/calendar/#source) object matching the provided ID, if one exists.
### `Calendar.getSourcesAsync()`
iOS
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
A promise which fulfils with an array of [`Source`](https://docs.expo.dev/versions/latest/sdk/calendar/#source) objects all sources for calendars stored on the device.
### `Calendar.isAvailableAsync()`
Android
iOS
Returns whether the Calendar API is enabled on the current device. This does not check the app permissions.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
Async `boolean`, indicating whether the Calendar API is available on the current device. Currently, this resolves `true` on iOS and Android only.
### `Calendar.requestCalendarPermissionsAsync()`
Android
iOS
Asks the user to grant permissions for accessing user's calendars.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/calendar/#permissionresponse)>`
A promise that resolves to an object of type [`PermissionResponse`](https://docs.expo.dev/versions/latest/sdk/calendar/#permissionresponse).
> Deprecated Use [`requestCalendarPermissionsAsync()`](https://docs.expo.dev/versions/latest/sdk/calendar/#calendarrequestcalendarpermissionsasync) instead.
### `Calendar.requestPermissionsAsync()`
Android
iOS
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/calendar/#permissionresponse)>`
### `Calendar.requestRemindersPermissionsAsync()`
iOS
Asks the user to grant permissions for accessing user's reminders.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/calendar/#permissionresponse)>`
A promise that resolves to an object of type [`PermissionResponse`](https://docs.expo.dev/versions/latest/sdk/calendar/#permissionresponse).
### `Calendar.updateAttendeeAsync(id, details)`
Android
Parameter| Type| Description  
---|---|---  
id| `string`| ID of the attendee record to be updated.  
details(optional)| `Partial[](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)<>`| A map of properties to be updated.Default:`{}`  
Updates an existing attendee record. To remove a property, explicitly set it to `null` in `details`.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<string>`
### `Calendar.updateCalendarAsync(id, details)`
Android
iOS
Parameter| Type| Description  
---|---|---  
id| `string`| ID of the calendar to update.  
details(optional)| `Partial[](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)<>`| A map of properties to be updated.Default:`{}`  
Updates the provided details of an existing calendar stored on the device. To remove a property, explicitly set it to `null` in `details`.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<string>`
### `Calendar.updateEventAsync(id, details, recurringEventOptions)`
Android
iOS
Parameter| Type| Description  
---|---|---  
id| `string`| ID of the event to be updated.  
details(optional)| `Omit[](https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys)<Partial[](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)<>, 'id'>`| A map of properties to be updated.Default:`{}`  
recurringEventOptions(optional)| `RecurringEventOptions[](https://docs.expo.dev/versions/latest/sdk/calendar/#recurringeventoptions)`| A map of options for recurring events.Default:`{}`  
Updates the provided details of an existing calendar stored on the device. To remove a property, explicitly set it to `null` in `details`.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<string>`
### `Calendar.updateReminderAsync(id, details)`
iOS
Parameter| Type| Description  
---|---|---  
id| `string`| ID of the reminder to be updated.  
details(optional)| | A map of properties to be updated.Default:`{}`  
Updates the provided details of an existing reminder stored on the device. To remove a property, explicitly set it to `null` in `details`.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<string>`
## Interfaces
### `PermissionResponse`
Android
iOS
An object obtained by permissions get and request functions.
Property| Type| Description  
---|---|---  
canAskAgain| `boolean`| Indicates if user can be asked again for specific permission. If not, one should be directed to the Settings app in order to enable/disable the permission.  
expires| `PermissionExpiration[](https://docs.expo.dev/versions/latest/sdk/calendar/#permissionexpiration)`| Determines time when the permission expires.  
granted| `boolean`| A convenience boolean that indicates if the permission is granted.  
status| `PermissionStatus[](https://docs.expo.dev/versions/latest/sdk/calendar/#permissionstatus)`| Determines the status of the permission.  
## Types
### `Alarm`
Android
iOS
A method for having the OS automatically remind the user about a calendar item.
Property| Type| Description  
---|---|---  
absoluteDate(optional)| `string`| Only for: iOSDate object or string representing an absolute time the alarm should occur. Overrides `relativeOffset` and `structuredLocation` if specified alongside either.  
method(optional)| | Only for: AndroidMethod of alerting the user that this alarm should use. On iOS this is always a notification.  
relativeOffset(optional)| `number`| Number of minutes from the `startDate` of the calendar item that the alarm should occur. Use negative values to have the alarm occur before the `startDate`.  
structuredLocation(optional)| `AlarmLocation[](https://docs.expo.dev/versions/latest/sdk/calendar/#alarmlocation)`  
### `AlarmLocation`
Android
iOS
Property| Type| Description  
---|---|---  
coords(optional)| `{  latitude: number,   longitude: number }`  
proximity(optional)| `string`  
radius(optional)| `number`  
title(optional)| `string`  
### `Attendee`
Android
iOS
A person or entity that is associated with an event by being invited or fulfilling some other role.
Property| Type| Description  
---|---|---  
email(optional)| `string`| Only for: AndroidEmail address of the attendee.  
id(optional)| `string`| Only for: AndroidInternal ID that represents this attendee on the device.  
isCurrentUser(optional)| `boolean`| Only for: iOSIndicates whether or not this attendee is the current OS user.  
name| `string`| Displayed name of the attendee.  
role| | Role of the attendee at the event.  
status| `AttendeeStatus[](https://docs.expo.dev/versions/latest/sdk/calendar/#attendeestatus)`| Status of the attendee in relation to the event.  
type| | Type of the attendee.  
url(optional)| `string`| Only for: iOSURL for the attendee.  
### `Calendar`
Android
iOS
A calendar record upon which events (or, on iOS, reminders) can be stored. Settings here apply to the calendar as a whole and how its events are displayed in the OS calendar app.
Property| Type| Description  
---|---|---  
accessLevel(optional)| `CalendarAccessLevel[](https://docs.expo.dev/versions/latest/sdk/calendar/#calendaraccesslevel)`| Only for: AndroidLevel of access that the user has for the calendar.  
allowedAttendeeTypes(optional)| `AttendeeType[][](https://docs.expo.dev/versions/latest/sdk/calendar/#attendeetype)`| Only for: AndroidAttendee types that this calendar supports.  
allowedAvailabilities| `Availability[][](https://docs.expo.dev/versions/latest/sdk/calendar/#availability)`| Availability types that this calendar supports.  
allowedReminders(optional)| `AlarmMethod[][](https://docs.expo.dev/versions/latest/sdk/calendar/#alarmmethod)`| Only for: AndroidAlarm methods that this calendar supports.  
allowsModifications| `boolean`| Boolean value that determines whether this calendar can be modified.  
color| `string`| Color used to display this calendar's events.  
entityType(optional)| | Only for: iOSWhether the calendar is used in the Calendar or Reminders OS app.  
id| `string`| Internal ID that represents this calendar on the device.  
isPrimary(optional)| `boolean`| Only for: AndroidBoolean value indicating whether this is the device's primary calendar.  
isSynced(optional)| `boolean`| Only for: AndroidIndicates whether this calendar is synced and its events stored on the device. Unexpected behavior may occur if this is not set to `true`.  
isVisible(optional)| `boolean`| Only for: AndroidIndicates whether the OS displays events on this calendar.  
name(optional)| `string | null`| Only for: AndroidInternal system name of the calendar.  
ownerAccount(optional)| `string`| Only for: AndroidName for the account that owns this calendar.  
source| | Object representing the source to be used for the calendar.  
sourceId(optional)| `string`| Only for: iOSID of the source to be used for the calendar. Likely the same as the source for any other locally stored calendars.  
timeZone(optional)| `string`| Only for: AndroidTime zone for the calendar.  
title| `string`| Visible name of the calendar.  
type(optional)| | Only for: iOSType of calendar this object represents.  
### `CalendarDialogParams`
Android
iOS
Property| Type| Description  
---|---|---  
id| `string`| ID of the event to be presented in the calendar UI.  
instanceStartDate(optional)| `string | `| Only for: iOSDate object representing the start time of the desired instance, if looking for a single instance of a recurring event. If this is not provided and id represents a recurring event, the first instance of that event will be returned by default.  
### `DaysOfTheWeek`
iOS
Property| Type| Description  
---|---|---  
dayOfTheWeek| | Sunday to Saturday - `DayOfTheWeek` enum.  
weekNumber(optional)| `number`| `-53` to `53` (`0` ignores this field, and a negative indicates a value from the end of the range).  
### `DialogEventResult`
Android
iOS
The result of presenting a calendar dialog for creating or editing an event.
Property| Type| Description  
---|---|---  
action| `Extract[](https://www.typescriptlang.org/docs/handbook/utility-types.html#extracttype-union)<CalendarDialogResultActions[](https://docs.expo.dev/versions/latest/sdk/calendar/#calendardialogresultactions), 'done' | 'saved' | 'canceled' | 'deleted'>`| How user responded to the dialog. On Android, this is always `done` (Android doesn't provide enough information to determine the user's action - the user may have canceled the dialog, saved or deleted the event). On iOS, it can be `saved`, `canceled` or `deleted`.  
id| `string | null`| The ID of the event that was created or edited. On Android, this is always `null`. On iOS, this is a string when user confirms the creation or editing of an event. Otherwise, it's `null`.  
### `Event`
Android
iOS
An event record, or a single instance of a recurring event. On iOS, used in the Calendar app.
Property| Type| Description  
---|---|---  
accessLevel(optional)| `EventAccessLevel[](https://docs.expo.dev/versions/latest/sdk/calendar/#eventaccesslevel)`| Only for: AndroidUser's access level for the event.  
alarms| | Array of Alarm objects which control automated reminders to the user.  
allDay| `boolean`| Whether the event is displayed as an all-day event on the calendar  
availability| | The availability setting for the event.  
calendarId| `string`| ID of the calendar that contains this event.  
creationDate(optional)| `string | `| Only for: iOSDate when the event record was created.  
endDate| `string | `| Date object or string representing the time when the event ends.  
endTimeZone(optional)| `string`| Only for: AndroidTime zone for the event end time.  
guestsCanInviteOthers(optional)| `boolean`| Only for: AndroidWhether invited guests can invite other guests.  
guestsCanModify(optional)| `boolean`| Only for: AndroidWhether invited guests can modify the details of the event.  
guestsCanSeeGuests(optional)| `boolean`| Only for: AndroidWhether invited guests can see other guests.  
id| `string`| Internal ID that represents this event on the device.  
instanceId(optional)| `string`| Only for: AndroidFor instances of recurring events, volatile ID representing this instance. Not guaranteed to always refer to the same instance.  
isDetached(optional)| `boolean`| Only for: iOSBoolean value indicating whether or not the event is a detached (modified) instance of a recurring event.  
lastModifiedDate(optional)| `string | `| Only for: iOSDate when the event record was last modified.  
location| `string`| Location field of the event.  
notes| `string`| Description or notes saved with the event.  
organizer(optional)| `string`| Only for: iOSOrganizer of the event.  
organizerEmail(optional)| `string`| Only for: AndroidEmail address of the organizer of the event.  
originalId(optional)| `string`| Only for: AndroidFor detached (modified) instances of recurring events, the ID of the original recurring event.  
originalStartDate(optional)| `string | `| Only for: iOSFor recurring events, the start date for the first (original) instance of the event.  
recurrenceRule| `null`| Object representing rules for recurring or repeating events. Set to `null` for one-time events.  
startDate| `string | `| Date object or string representing the time when the event starts.  
status| | Status of the event.  
timeZone| `string`| Time zone the event is scheduled in.  
title| `string`| Visible name of the event.  
url(optional)| `string`| Only for: iOSURL for the event.  
### `OpenEventDialogResult`
Android
iOS
The result of presenting the calendar dialog for opening (viewing) an event.
Property| Type| Description  
---|---|---  
action| `Extract[](https://www.typescriptlang.org/docs/handbook/utility-types.html#extracttype-union)<CalendarDialogResultActions[](https://docs.expo.dev/versions/latest/sdk/calendar/#calendardialogresultactions), 'done' | 'canceled' | 'deleted' | 'responded'>`| Indicates how user responded to the dialog. On Android, the `action` is always `done`. On iOS, it can be `done`, `canceled`, `deleted` or `responded`.  
### `OpenEventPresentationOptions`
Android
iOS
Type: `PresentationOptions[](https://docs.expo.dev/versions/latest/sdk/calendar/#presentationoptions)` extended by:
Property| Type| Description  
---|---|---  
allowsCalendarPreview(optional)| `boolean`| Only for: iOSDetermines whether event can be shown in calendar day view preview. This property applies only to invitations.Default:`false`  
allowsEditing(optional)| `boolean`| Only for: iOSWhether to allow the user to edit the previewed event. This property applies only to events in calendars created by the user. Note that if the user edits the event, the returned action is the one that user performs last. For example, when user previews the event, confirms some edits and finally dismisses the dialog, the event is edited, but response is `canceled`.Default:`false`  
### `PermissionExpiration`
Android
iOS
Literal Type: `union`
Permission expiration time. Currently, all permissions are granted permanently.
Acceptable values are: `'never'` | `number`
### `PermissionHookOptions`
Android
iOS
Literal Type: `union`
Acceptable values are: `PermissionHookBehavior` | `Options`
### `PresentationOptions`
Android
iOS
Property| Type| Description  
---|---|---  
startNewActivityTask(optional)| `boolean`| Only for: AndroidWhether to launch the Activity as a new [task](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_NEW_TASK). If `true`, the promise resolves with `'done'` action immediately after opening the calendar activity.Default:`true`  
### `RecurrenceRule`
Android
iOS
A recurrence rule for events or reminders, allowing the same calendar item to recur multiple times. This type is based on [the iOS interface](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/1507320-initrecurrencewithfrequency) which is in turn based on [the iCal RFC](https://tools.ietf.org/html/rfc5545#section-3.8.5.3) so you can refer to those to learn more about this potentially complex interface.
Not all the combinations make sense. For example, when frequency is `DAILY`, setting `daysOfTheMonth` makes no sense.
Property| Type| Description  
---|---|---  
daysOfTheMonth(optional)| `number[]`| Only for: iOSThe days of the month this event occurs on. `-31` to `31` (not including `0`). Negative indicates a value from the end of the range. This field is only valid for `Calendar.Frequency.Monthly`.  
daysOfTheWeek(optional)| `DaysOfTheWeek[][](https://docs.expo.dev/versions/latest/sdk/calendar/#daysoftheweek)`| Only for: iOSThe days of the week the event should recur on. An array of [`DaysOfTheWeek`](https://docs.expo.dev/versions/latest/sdk/calendar/#daysoftheweek) object.  
daysOfTheYear(optional)| `number[]`| Only for: iOSThe days of the year this event occurs on. `-366` to `366` (not including `0`). Negative indicates a value from the end of the range. This field is only valid for `Calendar.Frequency.Yearly`.  
endDate(optional)| `string | `| Date on which the calendar item should stop recurring; overrides `occurrence` if both are specified.  
frequency| | How often the calendar item should recur.  
interval(optional)| `number`| Interval at which the calendar item should recur. For example, an `interval: 2` with `frequency: DAILY` would yield an event that recurs every other day.Default:`1`  
monthsOfTheYear(optional)| `MonthOfTheYear[][](https://docs.expo.dev/versions/latest/sdk/calendar/#monthoftheyear)`| Only for: iOSThe months this event occurs on. This field is only valid for `Calendar.Frequency.Yearly`.  
occurrence(optional)| `number`| Number of times the calendar item should recur before stopping.  
setPositions(optional)| `number[]`| Only for: iOSTAn array of numbers that filters which recurrences to include. For example, for an event that recurs every Monday, passing 2 here will make it recur every other Monday. `-366` to `366` (not including `0`). Negative indicates a value from the end of the range. This field is only valid for `Calendar.Frequency.Yearly`.  
weeksOfTheYear(optional)| `number[]`| Only for: iOSThe weeks of the year this event occurs on. `-53` to `53` (not including `0`). Negative indicates a value from the end of the range. This field is only valid for `Calendar.Frequency.Yearly`.  
### `RecurringEventOptions`
iOS
Property| Type| Description  
---|---|---  
futureEvents(optional)| `boolean`| Whether future events in the recurring series should also be updated. If `true`, will apply the given changes to the recurring instance specified by `instanceStartDate` and all future events in the series. If `false`, will only apply the given changes to the instance specified by `instanceStartDate`.  
instanceStartDate(optional)| `string | `| Date object representing the start time of the desired instance, if looking for a single instance of a recurring event. If this is not provided and id represents a recurring event, the first instance of that event will be returned by default.  
### `Reminder`
iOS
A reminder record, used in the iOS Reminders app. No direct analog on Android.
Property| Type| Description  
---|---|---  
alarms(optional)| | Array of Alarm objects which control automated alarms to the user about the task.  
calendarId(optional)| `string`| ID of the calendar that contains this reminder.  
completed(optional)| `boolean`| Indicates whether or not the task has been completed.  
completionDate(optional)| `string | `| Date object or string representing the date of completion, if `completed` is `true`. Setting this property of a nonnull `Date` will automatically set the reminder's `completed` value to `true`.  
creationDate(optional)| `string | `| Date when the reminder record was created.  
dueDate(optional)| `string | `| Date object or string representing the time when the reminder task is due.  
id(optional)| `string`| Internal ID that represents this reminder on the device.  
lastModifiedDate(optional)| `string | `| Date when the reminder record was last modified.  
location(optional)| `string`| Location field of the reminder  
notes(optional)| `string`| Description or notes saved with the reminder.  
recurrenceRule(optional)| `null`| Object representing rules for recurring or repeated reminders. `null` for one-time tasks.  
startDate(optional)| `string | `| Date object or string representing the start date of the reminder task.  
timeZone(optional)| `string`| Time zone the reminder is scheduled in.  
title(optional)| `string`| Visible name of the reminder.  
url(optional)| `string`| URL for the reminder.  
### `Source`
Android
iOS
A source account that owns a particular calendar. Expo apps will typically not need to interact with `Source` objects.
Property| Type| Description  
---|---|---  
id(optional)| `string`| Only for: iOSInternal ID that represents this source on the device.  
isLocalAccount(optional)| `boolean`| Only for: AndroidWhether this source is the local phone account. Must be `true` if `type` is `undefined`.  
name| `string`| Name for the account that owns this calendar and was used to sync the calendar to the device.  
type| `string | `| Type of the account that owns this calendar and was used to sync it to the device. If `isLocalAccount` is falsy then this must be defined, and must match an account on the device along with `name`, or the OS will delete the calendar. On iOS, one of [`SourceType`](https://docs.expo.dev/versions/latest/sdk/calendar/#sourcetype)s.  
## Enums
### `AlarmMethod`
Android
#### `ALARM`
`AlarmMethod.ALARM ＝ "alarm"`
#### `ALERT`
`AlarmMethod.ALERT ＝ "alert"`
#### `DEFAULT`
`AlarmMethod.DEFAULT ＝ "default"`
#### `EMAIL`
`AlarmMethod.EMAIL ＝ "email"`
#### `SMS`
`AlarmMethod.SMS ＝ "sms"`
### `AttendeeRole`
Android
iOS
#### `ATTENDEE`
Android
`AttendeeRole.ATTENDEE ＝ "attendee"`
#### `CHAIR`
iOS
`AttendeeRole.CHAIR ＝ "chair"`
#### `NONE`
Android
`AttendeeRole.NONE ＝ "none"`
#### `NON_PARTICIPANT`
iOS
`AttendeeRole.NON_PARTICIPANT ＝ "nonParticipant"`
#### `OPTIONAL`
iOS
`AttendeeRole.OPTIONAL ＝ "optional"`
#### `ORGANIZER`
Android
`AttendeeRole.ORGANIZER ＝ "organizer"`
#### `PERFORMER`
Android
`AttendeeRole.PERFORMER ＝ "performer"`
#### `REQUIRED`
iOS
`AttendeeRole.REQUIRED ＝ "required"`
#### `SPEAKER`
Android
`AttendeeRole.SPEAKER ＝ "speaker"`
#### `UNKNOWN`
iOS
`AttendeeRole.UNKNOWN ＝ "unknown"`
### `AttendeeStatus`
Android
iOS
#### `ACCEPTED`
`AttendeeStatus.ACCEPTED ＝ "accepted"`
#### `COMPLETED`
iOS
`AttendeeStatus.COMPLETED ＝ "completed"`
#### `DECLINED`
`AttendeeStatus.DECLINED ＝ "declined"`
#### `DELEGATED`
iOS
`AttendeeStatus.DELEGATED ＝ "delegated"`
#### `IN_PROCESS`
iOS
`AttendeeStatus.IN_PROCESS ＝ "inProcess"`
#### `INVITED`
Android
`AttendeeStatus.INVITED ＝ "invited"`
#### `NONE`
Android
`AttendeeStatus.NONE ＝ "none"`
#### `PENDING`
iOS
`AttendeeStatus.PENDING ＝ "pending"`
#### `TENTATIVE`
`AttendeeStatus.TENTATIVE ＝ "tentative"`
#### `UNKNOWN`
iOS
`AttendeeStatus.UNKNOWN ＝ "unknown"`
### `AttendeeType`
Android
iOS
#### `GROUP`
iOS
`AttendeeType.GROUP ＝ "group"`
#### `NONE`
Android
`AttendeeType.NONE ＝ "none"`
#### `OPTIONAL`
Android
`AttendeeType.OPTIONAL ＝ "optional"`
#### `PERSON`
iOS
`AttendeeType.PERSON ＝ "person"`
#### `REQUIRED`
Android
`AttendeeType.REQUIRED ＝ "required"`
#### `RESOURCE`
`AttendeeType.RESOURCE ＝ "resource"`
#### `ROOM`
iOS
`AttendeeType.ROOM ＝ "room"`
#### `UNKNOWN`
iOS
`AttendeeType.UNKNOWN ＝ "unknown"`
### `Availability`
Android
iOS
#### `BUSY`
`Availability.BUSY ＝ "busy"`
#### `FREE`
`Availability.FREE ＝ "free"`
#### `NOT_SUPPORTED`
iOS
`Availability.NOT_SUPPORTED ＝ "notSupported"`
#### `TENTATIVE`
`Availability.TENTATIVE ＝ "tentative"`
#### `UNAVAILABLE`
iOS
`Availability.UNAVAILABLE ＝ "unavailable"`
### `CalendarAccessLevel`
Android
#### `CONTRIBUTOR`
`CalendarAccessLevel.CONTRIBUTOR ＝ "contributor"`
#### `EDITOR`
`CalendarAccessLevel.EDITOR ＝ "editor"`
#### `FREEBUSY`
`CalendarAccessLevel.FREEBUSY ＝ "freebusy"`
#### `NONE`
`CalendarAccessLevel.NONE ＝ "none"`
#### `OVERRIDE`
`CalendarAccessLevel.OVERRIDE ＝ "override"`
#### `OWNER`
`CalendarAccessLevel.OWNER ＝ "owner"`
#### `READ`
`CalendarAccessLevel.READ ＝ "read"`
#### `RESPOND`
`CalendarAccessLevel.RESPOND ＝ "respond"`
#### `ROOT`
`CalendarAccessLevel.ROOT ＝ "root"`
### `CalendarDialogResultActions`
Android
iOS
Enum containing all possible user responses to the calendar UI dialogs. Depending on what dialog is presented, a subset of the values applies.
#### `canceled`
iOS
`CalendarDialogResultActions.canceled ＝ "canceled"`
The user canceled or dismissed the dialog.
#### `deleted`
iOS
`CalendarDialogResultActions.deleted ＝ "deleted"`
The user deleted the event.
#### `done`
`CalendarDialogResultActions.done ＝ "done"`
On Android, this is the only possible result because the OS doesn't provide enough information to determine the user's action - the user may have canceled the dialog, modified the event, or deleted it.
On iOS, this means the user simply closed the dialog.
#### `responded`
iOS
`CalendarDialogResultActions.responded ＝ "responded"`
The user responded to and saved a pending event invitation.
#### `saved`
iOS
`CalendarDialogResultActions.saved ＝ "saved"`
The user saved a new event or modified an existing one.
### `CalendarType`
iOS
#### `BIRTHDAYS`
`CalendarType.BIRTHDAYS ＝ "birthdays"`
#### `CALDAV`
`CalendarType.CALDAV ＝ "caldav"`
#### `EXCHANGE`
`CalendarType.EXCHANGE ＝ "exchange"`
#### `LOCAL`
`CalendarType.LOCAL ＝ "local"`
#### `SUBSCRIBED`
`CalendarType.SUBSCRIBED ＝ "subscribed"`
#### `UNKNOWN`
`CalendarType.UNKNOWN ＝ "unknown"`
### `DayOfTheWeek`
iOS
#### `Sunday`
`DayOfTheWeek.Sunday ＝ 1`
#### `Monday`
`DayOfTheWeek.Monday ＝ 2`
#### `Tuesday`
`DayOfTheWeek.Tuesday ＝ 3`
#### `Wednesday`
`DayOfTheWeek.Wednesday ＝ 4`
#### `Thursday`
`DayOfTheWeek.Thursday ＝ 5`
#### `Friday`
`DayOfTheWeek.Friday ＝ 6`
#### `Saturday`
`DayOfTheWeek.Saturday ＝ 7`
### `EntityTypes`
Android
iOS
platform ios
#### `EVENT`
`EntityTypes.EVENT ＝ "event"`
#### `REMINDER`
`EntityTypes.REMINDER ＝ "reminder"`
### `EventAccessLevel`
Android
#### `CONFIDENTIAL`
`EventAccessLevel.CONFIDENTIAL ＝ "confidential"`
#### `DEFAULT`
`EventAccessLevel.DEFAULT ＝ "default"`
#### `PRIVATE`
`EventAccessLevel.PRIVATE ＝ "private"`
#### `PUBLIC`
`EventAccessLevel.PUBLIC ＝ "public"`
### `EventStatus`
Android
iOS
#### `CANCELED`
`EventStatus.CANCELED ＝ "canceled"`
#### `CONFIRMED`
`EventStatus.CONFIRMED ＝ "confirmed"`
#### `NONE`
`EventStatus.NONE ＝ "none"`
#### `TENTATIVE`
`EventStatus.TENTATIVE ＝ "tentative"`
### `Frequency`
Android
iOS
#### `DAILY`
`Frequency.DAILY ＝ "daily"`
#### `MONTHLY`
`Frequency.MONTHLY ＝ "monthly"`
#### `WEEKLY`
`Frequency.WEEKLY ＝ "weekly"`
#### `YEARLY`
`Frequency.YEARLY ＝ "yearly"`
### `MonthOfTheYear`
iOS
#### `January`
`MonthOfTheYear.January ＝ 1`
#### `February`
`MonthOfTheYear.February ＝ 2`
#### `March`
`MonthOfTheYear.March ＝ 3`
#### `April`
`MonthOfTheYear.April ＝ 4`
#### `May`
`MonthOfTheYear.May ＝ 5`
#### `June`
`MonthOfTheYear.June ＝ 6`
#### `July`
`MonthOfTheYear.July ＝ 7`
#### `August`
`MonthOfTheYear.August ＝ 8`
#### `September`
`MonthOfTheYear.September ＝ 9`
#### `October`
`MonthOfTheYear.October ＝ 10`
#### `November`
`MonthOfTheYear.November ＝ 11`
#### `December`
`MonthOfTheYear.December ＝ 12`
### `PermissionStatus`
Android
iOS
#### `DENIED`
`PermissionStatus.DENIED ＝ "denied"`
User has denied the permission.
#### `GRANTED`
`PermissionStatus.GRANTED ＝ "granted"`
User has granted the permission.
#### `UNDETERMINED`
`PermissionStatus.UNDETERMINED ＝ "undetermined"`
User hasn't granted or denied the permission yet.
### `ReminderStatus`
iOS
#### `COMPLETED`
`ReminderStatus.COMPLETED ＝ "completed"`
#### `INCOMPLETE`
`ReminderStatus.INCOMPLETE ＝ "incomplete"`
### `SourceType`
iOS
#### `BIRTHDAYS`
`SourceType.BIRTHDAYS ＝ "birthdays"`
#### `CALDAV`
`SourceType.CALDAV ＝ "caldav"`
#### `EXCHANGE`
`SourceType.EXCHANGE ＝ "exchange"`
#### `LOCAL`
`SourceType.LOCAL ＝ "local"`
#### `MOBILEME`
`SourceType.MOBILEME ＝ "mobileme"`
#### `SUBSCRIBED`
`SourceType.SUBSCRIBED ＝ "subscribed"`
## Permissions
### Android
If you only intend to use the [system-provided calendar UI](https://docs.expo.dev/versions/latest/sdk/calendar#launching-system-provided-calendar-dialogs), you don't need to request any permissions.
Otherwise, you must add the following permissions to your app.json inside the [`expo.android.permissions`](https://docs.expo.dev/versions/latest/config/app#permissions) array.
Android Permission| Description  
---|---  
`READ_CALENDAR`| Allows an application to read the user's calendar data.  
`WRITE_CALENDAR`| Allows an application to write the user's calendar data.  
### iOS
The following usage description keys are used by this library:
Info.plist Key| Description  
---|---  
`NSCalendarsUsageDescription`| A message that tells the user why the app is requesting access to the user’s calendar data.  
`NSRemindersUsageDescription`| A message that tells the user why the app is requesting access to the user’s reminders.

