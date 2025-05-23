---
url: https://docs.expo.dev/versions/latest/sdk/contacts
title: https://docs.expo.dev/versions/latest/sdk/contacts
date: 2025-04-30T17:15:53.860723
depth: 2
---

Search
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo Contacts
A library that provides access to the phone's system contacts.
Android
iOS
Bundled version:
~14.0.5
`expo-contacts` provides access to the device's system contacts, allowing you to get contact information as well as adding, editing, or removing contacts.
On iOS, contacts have a multi-layered grouping system that you can also access through this API.
## Installation
Terminal
Copy
`- ``npx expo install expo-contacts`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Configuration in app config
You can configure `expo-contacts` using its built-in [config plugin](https://docs.expo.dev/config-plugins/introduction) if you use config plugins in your project ([EAS Build](https://docs.expo.dev/build/introduction) or `npx expo run:[android|ios]`). The plugin allows you to configure various properties that cannot be set at runtime and require building a new app binary to take effect.
### Example app.json with config plugin
app.json
Copy
```
{
 "expo": {
  "plugins": [
   [
    "expo-contacts",
    {
     "contactsPermission": "Allow $(PRODUCT_NAME) to access your contacts."
    }
   ]
  ]
 }
}

```

### Configurable properties
Name| Default| Description  
---|---|---  
`contactsPermission`| `"Allow $(PRODUCT_NAME) to access your contacts"`| Only for: iOSA string to set the [`NSContactsUsageDescription`](https://docs.expo.dev/versions/latest/sdk/contacts/#ios) permission message.  
Are you using this library in an existing React Native app?
If you're not using Continuous Native Generation ([CNG](https://docs.expo.dev/workflow/continuous-native-generation)) (you're using native android and ios projects manually), then you need to configure following permissions in your native projects:
  * For Android, add `android.permission.READ_CONTACTS` and `android.permission.WRITE_CONTACTS` permissions to your project's android/app/src/main/AndroidManifest.xml:
```
<uses-permission android:name="android.permission.READ_CONTACTS" />
<uses-permission android:name="android.permission.WRITE_CONTACTS" />

```

  * For iOS, add the `NSContactsUsageDescription` key to your project's ios/[app]/Info.plist:
```
<key>NSContactsUsageDescription</key>
<string>Allow $(PRODUCT_NAME) to access your contacts</string>

```



## Usage
Basic Contacts Usage
```
import { useEffect } from 'react';
import { StyleSheet, View, Text } from 'react-native';
import * as Contacts from 'expo-contacts';
export default function App() {
 useEffect(() => {
  (async () => {
   const { status } = await Contacts.requestPermissionsAsync();
   if (status === 'granted') {
    const { data } = await Contacts.getContactsAsync({
     fields: [Contacts.Fields.Emails],
    });
    if (data.length > 0) {
     const contact = data[0];
     console.log(contact);
    }
   }
  })();
 }, []);
 return (
  <View style={styles.container}><Text>Contacts Module Example</Text></View>
 );
}
const styles = StyleSheet.create({
 container: {
  flex: 1,
  backgroundColor: '#fff',
  alignItems: 'center',
  justifyContent: 'center',
 },
});

```

## API
```
import * as Contacts from 'expo-contacts';

```

## Methods
### `Contacts.addContactAsync(contact, containerId)`
Android
iOS
Parameter| Type| Description  
---|---|---  
contact| | A contact with the changes you wish to persist. The `id` parameter will not be used.  
containerId(optional)| `string`| Only for: iOSThe container that will parent the contact.  
Creates a new contact and adds it to the system.
> Note: For Android users, the Expo Go app does not have the required `WRITE_CONTACTS` permission to write to Contacts. You will need to create a [development build](https://docs.expo.dev/develop/development-builds/create-a-build) and add permission in there manually to use this method.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<string>`
A promise that fulfills with ID of the new system contact.
Example
```
const contact = {
 [Contacts.Fields.FirstName]: 'Bird',
 [Contacts.Fields.LastName]: 'Man',
 [Contacts.Fields.Company]: 'Young Money',
};
const contactId = await Contacts.addContactAsync(contact);

```

### `Contacts.addExistingContactToGroupAsync(contactId, groupId)`
iOS
Parameter| Type| Description  
---|---|---  
contactId| `string`| ID of the contact you want to edit.  
groupId| `string`| ID for the group you want to add membership to.  
Add a contact as a member to a group. A contact can be a member of multiple groups.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<any>`
Example
```
await Contacts.addExistingContactToGroupAsync(
 '665FDBCFAE55-D614-4A15-8DC6-161A368D',
 '161A368D-D614-4A15-8DC6-665FDBCFAE55'
);

```

### `Contacts.addExistingGroupToContainerAsync(groupId, containerId)`
iOS
Parameter| Type| Description  
---|---|---  
groupId| `string`| The group you want to target.  
containerId| `string`| The container you want to add membership to.  
Add a group to a container.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<any>`
Example
```
await Contacts.addExistingGroupToContainerAsync(
 '161A368D-D614-4A15-8DC6-665FDBCFAE55',
 '665FDBCFAE55-D614-4A15-8DC6-161A368D'
);

```

### `Contacts.createGroupAsync(name, containerId)`
iOS
Parameter| Type| Description  
---|---|---  
name(optional)| `string`| Name of the new group.  
containerId(optional)| `string`| The container you to add membership to.  
Create a group with a name, and add it to a container. If the container is `undefined`, the default container will be targeted.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<string>`
A promise that fulfills with ID of the new group.
Example
```
const groupId = await Contacts.createGroupAsync('Sailor Moon');

```

### `Contacts.getContactByIdAsync(id, fields)`
Android
iOS
Parameter| Type| Description  
---|---|---  
id| `string`| The ID of a system contact.  
fields(optional)| | If specified, the fields defined will be returned. When skipped, all fields will be returned.  
Used for gathering precise data about a contact. Returns a contact matching the given `id`.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<undefined>`
A promise that fulfills with `Contact` object with ID matching the input ID, or `undefined` if there is no match.
Example
```
const contact = await Contacts.getContactByIdAsync('161A368D-D614-4A15-8DC6-665FDBCFAE55');
if (contact) {
 console.log(contact);
}

```

### `Contacts.getContactsAsync(contactQuery)`
Android
iOS
Parameter| Type| Description  
---|---|---  
contactQuery(optional)| | Object used to query contacts.Default:`{}`  
Return a list of contacts that fit a given criteria. You can get all of the contacts by passing no criteria.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
A promise that fulfills with `ContactResponse` object returned from the query.
Example
```
const { data } = await Contacts.getContactsAsync({
 fields: [Contacts.Fields.Emails],
});
if (data.length > 0) {
 const contact = data[0];
 console.log(contact);
}

```

### `Contacts.getContainersAsync(containerQuery)`
iOS
Parameter| Type| Description  
---|---|---  
containerQuery| `ContainerQuery[](https://docs.expo.dev/versions/latest/sdk/contacts/#containerquery)`| Information used to gather containers.  
Query a list of system containers.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
A promise that fulfills with array of containers that fit the query.
Example
```
const allContainers = await Contacts.getContainersAsync({
 contactId: '665FDBCFAE55-D614-4A15-8DC6-161A368D',
});

```

### `Contacts.getDefaultContainerIdAsync()`
iOS
Get the default container's ID.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<string>`
A promise that fulfills with default container ID.
Example
```
const containerId = await Contacts.getDefaultContainerIdAsync();

```

### `Contacts.getGroupsAsync(groupQuery)`
iOS
Parameter| Type| Description  
---|---|---  
groupQuery| | Information regarding which groups you want to get.  
Query and return a list of system groups.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
A promise that fulfills with array of groups that fit the query.
Example
```
const groups = await Contacts.getGroupsAsync({ groupName: 'sailor moon' });
const allGroups = await Contacts.getGroupsAsync({});

```

### `Contacts.getPagedContactsAsync(contactQuery)`
Android
iOS
Parameter| Type  
---|---  
contactQuery(optional)|   
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
### `Contacts.getPermissionsAsync()`
Android
iOS
Checks user's permissions for accessing contacts data.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/contacts/#permissionresponse)>`
A promise that resolves to a [PermissionResponse](https://docs.expo.dev/versions/latest/sdk/contacts/#permissionresponse) object.
### `Contacts.isAvailableAsync()`
Android
iOS
Returns whether the Contacts API is enabled on the current device. This method does not check the app permissions.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
A promise that fulfills with a `boolean`, indicating whether the Contacts API is available on the current device. It always resolves to `false` on web.
### `Contacts.presentContactPickerAsync()`
Android
iOS
Presents a native contact picker to select a single contact from the system. On Android, the `READ_CONTACTS` permission is required. You can obtain this permission by calling the [`Contacts.requestPermissionsAsync()`](https://docs.expo.dev/versions/latest/sdk/contacts/#contactsrequestpermissionsasync) method. On iOS, no permissions are required to use this method.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<null>`
A promise that fulfills with a single `Contact` object if a contact is selected or `null` if no contact is selected (when selection is canceled).
### `Contacts.presentFormAsync(contactId, contact, formOptions)`
Android
iOS
Parameter| Type| Description  
---|---|---  
contactId(optional)| `null | string`| The ID of a system contact.  
contact(optional)| `null | `| A contact with the changes you want to persist.  
formOptions(optional)| | Options for the native editor.Default:`{}`  
Present a native form for manipulating contacts.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<any>`
Example
```
await Contacts.presentFormAsync('161A368D-D614-4A15-8DC6-665FDBCFAE55');

```

### `Contacts.removeContactAsync(contactId)`
iOS
Parameter| Type| Description  
---|---|---  
contactId| `string`| ID of the contact you want to delete.  
Delete a contact from the system.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<any>`
Example
```
await Contacts.removeContactAsync('161A368D-D614-4A15-8DC6-665FDBCFAE55');

```

### `Contacts.removeContactFromGroupAsync(contactId, groupId)`
iOS
Parameter| Type| Description  
---|---|---  
contactId| `string`| ID of the contact you want to remove.  
groupId| `string`| ID for the group you want to remove membership of.  
Remove a contact's membership from a given group. This will not delete the contact.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<any>`
Example
```
await Contacts.removeContactFromGroupAsync(
 '665FDBCFAE55-D614-4A15-8DC6-161A368D',
 '161A368D-D614-4A15-8DC6-665FDBCFAE55'
);

```

### `Contacts.removeGroupAsync(groupId)`
iOS
Parameter| Type| Description  
---|---|---  
groupId| `string`| ID of the group you want to remove.  
Delete a group from the device.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<any>`
Example
```
await Contacts.removeGroupAsync('161A368D-D614-4A15-8DC6-665FDBCFAE55');

```

### `Contacts.requestPermissionsAsync()`
Android
iOS
Asks the user to grant permissions for accessing contacts data.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<PermissionResponse[](https://docs.expo.dev/versions/latest/sdk/contacts/#permissionresponse)>`
A promise that resolves to a [PermissionResponse](https://docs.expo.dev/versions/latest/sdk/contacts/#permissionresponse) object.
### `Contacts.shareContactAsync(contactId, message, shareOptions)`
Android
iOS
Parameter| Type  
---|---  
contactId| `string`  
message| `string`  
shareOptions(optional)|   
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<any>`
### `Contacts.updateContactAsync(contact)`
iOS
Parameter| Type| Description  
---|---|---  
contact| | A contact object including the wanted changes.  
Mutate the information of an existing contact. Due to an iOS bug, `nonGregorianBirthday` field cannot be modified.
> On Android, you can use [`presentFormAsync`](https://docs.expo.dev/versions/latest/sdk/contacts/#contactspresentformasynccontactid-contact-formoptions) to make edits to contacts.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<string>`
A promise that fulfills with ID of the updated system contact if mutation was successful.
Example
```
const contact = {
 id: '161A368D-D614-4A15-8DC6-665FDBCFAE55',
 [Contacts.Fields.FirstName]: 'Drake',
 [Contacts.Fields.Company]: 'Young Money',
};
await Contacts.updateContactAsync(contact);

```

### `Contacts.updateGroupNameAsync(groupName, groupId)`
iOS
Parameter| Type| Description  
---|---|---  
groupName| `string`| New name for an existing group.  
groupId| `string`| ID of the group you want to edit.  
Change the name of an existing group.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<any>`
Example
```
await Contacts.updateGroupName('Expo Friends', '161A368D-D614-4A15-8DC6-665FDBCFAE55');

```

### `Contacts.writeContactToFileAsync(contactQuery)`
Android
iOS
Parameter| Type| Description  
---|---|---  
contactQuery(optional)| | Used to query contact you want to write.Default:`{}`  
Query a set of contacts and write them to a local URI that can be used for sharing.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<string | undefined>`
A promise that fulfills with shareable local URI, or `undefined` if there was no match.
Example
```
const localUri = await Contacts.writeContactToFileAsync({
 id: '161A368D-D614-4A15-8DC6-665FDBCFAE55',
});
Share.share({ url: localUri, message: 'Call me!' });

```

## Interfaces
### `PermissionResponse`
Android
iOS
An object obtained by permissions get and request functions.
Property| Type| Description  
---|---|---  
canAskAgain| `boolean`| Indicates if user can be asked again for specific permission. If not, one should be directed to the Settings app in order to enable/disable the permission.  
expires| `PermissionExpiration[](https://docs.expo.dev/versions/latest/sdk/contacts/#permissionexpiration)`| Determines time when the permission expires.  
granted| `boolean`| A convenience boolean that indicates if the permission is granted.  
status| `PermissionStatus[](https://docs.expo.dev/versions/latest/sdk/contacts/#permissionstatus)`| Determines the status of the permission.  
## Types
### `Address`
Android
iOS
Property| Type| Description  
---|---|---  
city(optional)| `string`| City name.  
country(optional)| `string`| Country name  
id(optional)| `string`| Unique ID. This value will be generated by the OS.  
isoCountryCode(optional)| `string`| [Standard country code](https://www.iso.org/iso-3166-country-codes.html).  
label| `string`| Localized display name.  
neighborhood(optional)| `string`| Neighborhood name.  
poBox(optional)| `string`| P.O. Box.  
postalCode(optional)| `string`| Local post code.  
region(optional)| `string`| Region or state name.  
street(optional)| `string`| Street name.  
### `CalendarFormatType`
Android
iOS
Literal Type: `union`
Acceptable values are: `CalendarFormats[](https://docs.expo.dev/versions/latest/sdk/contacts/#calendarformats)` | `{CalendarFormats}`
### `Contact`
Android
iOS
A set of fields that define information about a single contact entity.
Property| Type| Description  
---|---|---  
addresses(optional)| | Locations.  
birthday(optional)| | Birthday information in Gregorian format.  
company(optional)| `string`| Organization the entity belongs to.  
contactType| | Denoting a person or company.  
dates(optional)| | A labeled list of other relevant user dates in Gregorian format.  
department(optional)| `string`| Job department.  
emails(optional)| | Email addresses.  
firstName(optional)| `string`| Given name.  
id(optional)| `string`| Immutable identifier used for querying and indexing. This value will be generated by the OS when the contact is created.  
image(optional)| | Thumbnail image. On iOS it size is set to 320×320px, on Android it may vary.  
imageAvailable(optional)| `boolean`| Used for efficient retrieval of images.  
instantMessageAddresses(optional)| `InstantMessageAddress[][](https://docs.expo.dev/versions/latest/sdk/contacts/#instantmessageaddress)`| Instant messaging connections.  
jobTitle(optional)| `string`| Job description.  
lastName(optional)| `string`| Last name.  
maidenName(optional)| `string`| Maiden name.  
middleName(optional)| `string`| Middle name  
name| `string`| Full name with proper format.  
namePrefix(optional)| `string`| Dr., Mr., Mrs., and so on.  
nameSuffix(optional)| `string`| Jr., Sr., an so on.  
nickname(optional)| `string`| An alias to the proper name.  
nonGregorianBirthday(optional)| | Only for: iOSBirthday that doesn't conform to the Gregorian calendar format, interpreted based on the [calendar `format`](https://docs.expo.dev/versions/latest/sdk/contacts/#date) setting.  
note(optional)| `string`| Additional information.
> The `note` field [requires your app to request additional entitlements](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_developer_contacts_notes). The Expo Go app does not contain those entitlements, so in order to test this feature you will need to [request the entitlement from Apple](https://developer.apple.com/contact/request/contact-note-field), set the [`ios.accessesContactNotes`](https://docs.expo.dev/versions/latest/config/app#accessescontactnotes) field in app config to `true`, and [create your development build](https://docs.expo.dev/develop/development-builds/create-a-build).  
phoneNumbers(optional)| `PhoneNumber[][](https://docs.expo.dev/versions/latest/sdk/contacts/#phonenumber)`| Phone numbers.  
phoneticFirstName(optional)| `string`| Pronunciation of the first name.  
phoneticLastName(optional)| `string`| Pronunciation of the last name.  
phoneticMiddleName(optional)| `string`| Pronunciation of the middle name.  
rawImage(optional)| | Raw image without cropping, usually large.  
relationships(optional)| `Relationship[][](https://docs.expo.dev/versions/latest/sdk/contacts/#relationship)`| Names of other relevant user connections.  
socialProfiles(optional)| `SocialProfile[][](https://docs.expo.dev/versions/latest/sdk/contacts/#socialprofile)`| Only for: iOSSocial networks.  
urlAddresses(optional)| `UrlAddress[][](https://docs.expo.dev/versions/latest/sdk/contacts/#urladdress)`| Associated web URLs.  
### `ContactQuery`
Android
iOS
Used to query contacts from the user's device.
Property| Type| Description  
---|---|---  
containerId(optional)| `string`| Only for: iOSGet all contacts that belong to the container matching this ID.  
fields(optional)| | If specified, the defined fields will be returned. If skipped, all fields will be returned.  
groupId(optional)| `string`| Only for: iOSGet all contacts that belong to the group matching this ID.  
id(optional)| `string | string[]`| Get contacts with a matching ID or array of IDs.  
name(optional)| `string`| Get all contacts whose name contains the provided string (not case-sensitive).  
pageOffset(optional)| `number`| The number of contacts to skip before gathering contacts.  
pageSize(optional)| `number`| The max number of contacts to return. If skipped or set to `0` all contacts will be returned.  
rawContacts(optional)| `boolean`| Only for: iOSPrevent unification of contacts when gathering.Default:`false`  
sort(optional)| | Sort method used when gathering contacts.  
### `ContactResponse`
Android
iOS
The return value for queried contact operations like `getContactsAsync`.
Property| Type| Description  
---|---|---  
data| | An array of contacts that match a particular query.  
hasNextPage| `boolean`| This will be `true` if there are more contacts to retrieve beyond what is returned.  
hasPreviousPage| `boolean`| This will be `true` if there are previous contacts that weren't retrieved due to `pageOffset` limit.  
### `ContactSort`
Android
iOS
String union of values.
### `ContactType`
Android
iOS
Literal Type: `union`
Acceptable values are:  | `{ContactTypes}`
### `Container`
Android
iOS
Property| Type| Description  
---|---|---  
id| `string`  
name| `string`  
type| `ContainerType[](https://docs.expo.dev/versions/latest/sdk/contacts/#containertype)`  
### `ContainerQuery`
iOS
Used to query native contact containers.
Property| Type| Description  
---|---|---  
contactId(optional)| `string`| Query all the containers that parent a contact.  
containerId(optional)| `string | string[]`| Query all the containers that matches ID or an array od IDs.  
groupId(optional)| `string`| Query all the containers that parent a group.  
### `ContainerType`
Android
iOS
Literal Type: `union`
Acceptable values are: `ContainerTypes[](https://docs.expo.dev/versions/latest/sdk/contacts/#containertypes)` | `{ContainerTypes}`
### `Date`
Android
iOS
Property| Type| Description  
---|---|---  
day| `number`| Day.  
format(optional)| `CalendarFormatType[](https://docs.expo.dev/versions/latest/sdk/contacts/#calendarformattype)`| Format for the date. This is provided by the OS, do not set this manually.  
id(optional)| `string`| Unique ID. This value will be generated by the OS.  
label(optional)| `string`| Localized display name.  
month| `number`| Month - adjusted for JavaScript `Date` which starts at `0`.  
year(optional)| `number`| Year.  
### `Email`
Android
iOS
Property| Type| Description  
---|---|---  
email(optional)| `string`| Email address.  
id(optional)| `string`| Unique ID. This value will be generated by the OS.  
isPrimary(optional)| `boolean`| Flag signifying if it is a primary email address.  
label| `string`| Localized display name.  
### `FieldType`
Android
iOS
Literal Type: `union`
Acceptable values are:  | `{Fields}`
### `FormOptions`
Android
iOS
Denotes the functionality of a native contact form.
Property| Type| Description  
---|---|---  
allowsActions(optional)| `boolean`| Actions like share, add, create.  
allowsEditing(optional)| `boolean`| Allows for contact mutation.  
alternateName(optional)| `string`| Used if contact doesn't have a name defined.  
cancelButtonTitle(optional)| `string`| The name of the left bar button.  
displayedPropertyKeys(optional)| | The properties that will be displayed. On iOS those properties does nothing while in editing mode.  
groupId(optional)| `string`| The parent group for a new contact.  
isNew(optional)| `boolean`| Present the new contact controller. If set to `false` the unknown controller will be shown.  
message(optional)| `string`| Controller title.  
preventAnimation(optional)| `boolean`| Prevents the controller from animating in.  
shouldShowLinkedContacts(optional)| `boolean`| Show or hide the similar contacts.  
### `Group`
iOS
A parent to contacts. A contact can belong to multiple groups. Here are some query operations you can perform:
  * Child Contacts: `getContactsAsync({ groupId })`
  * Groups From Container: `getGroupsAsync({ containerId })`
  * Groups Named: `getContainersAsync({ groupName })`


Property| Type| Description  
---|---|---  
id(optional)| `string`| The editable name of a group.  
name(optional)| `string`| Immutable id representing the group.  
### `GroupQuery`
iOS
Used to query native contact groups.
Property| Type| Description  
---|---|---  
containerId(optional)| `string`| Query all groups that belong to a certain container.  
groupId(optional)| `string`| Query the group with a matching ID.  
groupName(optional)| `string`| Query all groups matching a name.  
### `Image`
Android
iOS
Information regarding thumbnail images.
> On Android you can get dimensions using [`Image.getSize`](https://reactnative.dev/docs/image#getsize) method.
Property| Type| Description  
---|---|---  
base64(optional)| `string`| Image as Base64 string.  
height(optional)| `number`| Only for: iOSImage height  
uri(optional)| `string`| A local image URI.
> Note: If you have a remote URI, download it first using [`FileSystem.downloadAsync`](https://docs.expo.dev/versions/latest/sdk/filesystem#filesystemdownloadasyncuri-fileuri-options).  
width(optional)| `number`| Only for: iOSImage width.  
### `InstantMessageAddress`
Android
iOS
Property| Type| Description  
---|---|---  
id(optional)| `string`| Unique ID. This value will be generated by the OS.  
label| `string`| Localized display name.  
localizedService(optional)| `string`| Localized name of app.  
service(optional)| `string`| Name of instant messaging app.  
username(optional)| `string`| Username in IM app.  
### `PermissionExpiration`
Android
iOS
Literal Type: `union`
Permission expiration time. Currently, all permissions are granted permanently.
Acceptable values are: `'never'` | `number`
### `PhoneNumber`
Android
iOS
Property| Type| Description  
---|---|---  
countryCode(optional)| `string`| Country code.Example`us`  
digits(optional)| `string`| Phone number without format.Example`8674305`  
id(optional)| `string`| Unique ID. This value will be generated by the OS.  
isPrimary(optional)| `boolean`| Flag signifying if it is a primary phone number.  
label| `string`| Localized display name.  
number(optional)| `string`| Phone number.  
### `Relationship`
Android
iOS
Property| Type| Description  
---|---|---  
id(optional)| `string`| Unique ID. This value will be generated by the OS.  
label| `string`| Localized display name.  
name(optional)| `string`| Name of related contact.  
### `SocialProfile`
iOS
Property| Type| Description  
---|---|---  
id(optional)| `string`| Unique ID. This value will be generated by the OS.  
label| `string`| Localized display name.  
localizedProfile(optional)| `string`| Localized profile name.  
service(optional)| `string`| Name of social app.  
url(optional)| `string`| Web URL.  
userId(optional)| `string`| Username ID in social app.  
username(optional)| `string`| Username in social app.  
### `UrlAddress`
Android
iOS
Property| Type| Description  
---|---|---  
id(optional)| `string`| Unique ID. This value will be generated by the OS.  
label| `string`| Localized display name.  
url(optional)| `string`| Web URL.  
## Enums
### `CalendarFormats`
Android
iOS
This format denotes the common calendar format used to specify how a date is calculated in `nonGregorianBirthday` fields.
#### `Buddhist`
iOS
`CalendarFormats.Buddhist ＝ "buddhist"`
#### `Chinese`
iOS
`CalendarFormats.Chinese ＝ "chinese"`
#### `Coptic`
iOS
`CalendarFormats.Coptic ＝ "coptic"`
#### `EthiopicAmeteAlem`
iOS
`CalendarFormats.EthiopicAmeteAlem ＝ "ethiopicAmeteAlem"`
#### `EthiopicAmeteMihret`
iOS
`CalendarFormats.EthiopicAmeteMihret ＝ "ethiopicAmeteMihret"`
#### `Gregorian`
`CalendarFormats.Gregorian ＝ "gregorian"`
#### `Hebrew`
iOS
`CalendarFormats.Hebrew ＝ "hebrew"`
#### `Indian`
iOS
`CalendarFormats.Indian ＝ "indian"`
#### `Islamic`
iOS
`CalendarFormats.Islamic ＝ "islamic"`
#### `IslamicCivil`
iOS
`CalendarFormats.IslamicCivil ＝ "islamicCivil"`
#### `IslamicTabular`
iOS
`CalendarFormats.IslamicTabular ＝ "islamicTabular"`
#### `IslamicUmmAlQura`
iOS
`CalendarFormats.IslamicUmmAlQura ＝ "islamicUmmAlQura"`
#### `ISO8601`
iOS
`CalendarFormats.ISO8601 ＝ "iso8601"`
#### `Japanese`
iOS
`CalendarFormats.Japanese ＝ "japanese"`
#### `Persian`
iOS
`CalendarFormats.Persian ＝ "persian"`
#### `RepublicOfChina`
iOS
`CalendarFormats.RepublicOfChina ＝ "republicOfChina"`
### `ContactTypes`
Android
iOS
#### `Company`
`ContactTypes.Company ＝ "company"`
Contact is group or company.
#### `Person`
`ContactTypes.Person ＝ "person"`
Contact is a human.
### `ContainerTypes`
iOS
#### `CardDAV`
`ContainerTypes.CardDAV ＝ "cardDAV"`
With cardDAV protocol used for sharing.
#### `Exchange`
`ContainerTypes.Exchange ＝ "exchange"`
In association with email server.
#### `Local`
`ContainerTypes.Local ＝ "local"`
A local non-iCloud container.
#### `Unassigned`
`ContainerTypes.Unassigned ＝ "unassigned"`
Unknown container.
### `Fields`
Android
iOS
Possible fields to retrieve for a contact.
#### `Addresses`
`Fields.Addresses ＝ "addresses"`
#### `Birthday`
`Fields.Birthday ＝ "birthday"`
#### `Company`
`Fields.Company ＝ "company"`
#### `ContactType`
`Fields.ContactType ＝ "contactType"`
#### `Dates`
`Fields.Dates ＝ "dates"`
#### `Department`
`Fields.Department ＝ "department"`
#### `Emails`
`Fields.Emails ＝ "emails"`
#### `ExtraNames`
`Fields.ExtraNames ＝ "extraNames"`
#### `FirstName`
`Fields.FirstName ＝ "firstName"`
#### `ID`
`Fields.ID ＝ "id"`
#### `Image`
`Fields.Image ＝ "image"`
#### `ImageAvailable`
`Fields.ImageAvailable ＝ "imageAvailable"`
#### `InstantMessageAddresses`
`Fields.InstantMessageAddresses ＝ "instantMessageAddresses"`
#### `JobTitle`
`Fields.JobTitle ＝ "jobTitle"`
#### `LastName`
`Fields.LastName ＝ "lastName"`
#### `MaidenName`
`Fields.MaidenName ＝ "maidenName"`
#### `MiddleName`
`Fields.MiddleName ＝ "middleName"`
#### `Name`
`Fields.Name ＝ "name"`
#### `NamePrefix`
`Fields.NamePrefix ＝ "namePrefix"`
#### `NameSuffix`
`Fields.NameSuffix ＝ "nameSuffix"`
#### `Nickname`
`Fields.Nickname ＝ "nickname"`
#### `NonGregorianBirthday`
iOS
`Fields.NonGregorianBirthday ＝ "nonGregorianBirthday"`
#### `Note`
`Fields.Note ＝ "note"`
#### `PhoneNumbers`
`Fields.PhoneNumbers ＝ "phoneNumbers"`
#### `PhoneticFirstName`
`Fields.PhoneticFirstName ＝ "phoneticFirstName"`
#### `PhoneticLastName`
`Fields.PhoneticLastName ＝ "phoneticLastName"`
#### `PhoneticMiddleName`
`Fields.PhoneticMiddleName ＝ "phoneticMiddleName"`
#### `RawImage`
`Fields.RawImage ＝ "rawImage"`
#### `Relationships`
`Fields.Relationships ＝ "relationships"`
#### `SocialProfiles`
iOS
`Fields.SocialProfiles ＝ "socialProfiles"`
#### `UrlAddresses`
`Fields.UrlAddresses ＝ "urlAddresses"`
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
### `SortTypes`
Android
iOS
#### `FirstName`
`SortTypes.FirstName ＝ "firstName"`
Sort by first name in ascending order.
#### `LastName`
`SortTypes.LastName ＝ "lastName"`
Sort by last name in ascending order.
#### `None`
`SortTypes.None ＝ "none"`
No sorting should be applied.
#### `UserDefault`
Android
`SortTypes.UserDefault ＝ "userDefault"`
The user default method of sorting.
## Permissions
### Android
This library automatically adds `READ_CONTACTS` and `WRITE_CONTACTS` permissions to your app:
Android Permission| Description  
---|---  
`READ_CONTACTS`| Allows an application to read the user's contacts data.  
`WRITE_CONTACTS`| Allows an application to write the user's contacts data.  
### iOS
The following usage description keys are used by this library:
Info.plist Key| Description  
---|---  
`NSContactsUsageDescription`| A message that tells the user why the app is requesting access to the user’s contacts.

