---
url: https://docs.expo.dev/versions/latest/sdk/intent-launcher
title: https://docs.expo.dev/versions/latest/sdk/intent-launcher
date: 2025-04-30T17:16:24.895062
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo IntentLauncher
A library that provides an API to launch Android intents.
Android
Bundled version:
~12.0.2
`expo-intent-launcher` provides a way to launch Android intents. For example, you can use this API to open a specific settings screen.
## Installation
Terminal
Copy
`- ``npx expo install expo-intent-launcher`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Usage
```
import { startActivityAsync, ActivityAction } from 'expo-intent-launcher';
// Open location settings
startActivityAsync(ActivityAction.LOCATION_SOURCE_SETTINGS);

```

## API
```
import * as IntentLauncher from 'expo-intent-launcher';

```

## Methods
### `IntentLauncher.startActivityAsync(activityAction, params)`
Android
Parameter| Type| Description  
---|---|---  
activityAction| `string`| The action to be performed, e.g. `IntentLauncher.ActivityAction.WIRELESS_SETTINGS`. There are a few pre-defined constants you can use for this parameter. You can find them at [expo-intent-launcher/src/IntentLauncher.ts](https://github.com/expo/expo/blob/main/packages/expo-intent-launcher/src/IntentLauncher.ts).  
params(optional)| `IntentLauncherParams[](https://docs.expo.dev/versions/latest/sdk/intent-launcher/#intentlauncherparams)`| An object of intent parameters.Default:`{}`  
Starts the specified activity. The method will return a promise which resolves when the user returns to the app.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<IntentLauncherResult[](https://docs.expo.dev/versions/latest/sdk/intent-launcher/#intentlauncherresult)>`
A promise which fulfils with `IntentLauncherResult` object.
## Interfaces
### `IntentLauncherParams`
Android
Property| Type| Description  
---|---|---  
category(optional)| `string`| Category provides more details about the action the intent performs. See [Intent.addCategory](https://developer.android.com/reference/android/content/Intent.html#addCategory\(java.lang.String\)).  
className(optional)| `string`| Class name of the ComponentName.  
data(optional)| `string`| A URI specifying the data that the intent should operate upon. (_Note:_ Android requires the URI scheme to be lowercase, unlike the formal RFC.)  
extra(optional)| `Record<string, any>`| A map specifying additional key-value pairs which are passed with the intent as `extras`. The keys must include a package prefix, for example the app `com.android.contacts` would use names like `com.android.contacts.ShowAll`.  
flags(optional)| `number`| Bitmask of flags to be used. See [Intent.setFlags](https://developer.android.com/reference/android/content/Intent.html#setFlags\(int\)) for more details.  
packageName(optional)| `string`| Package name used as an identifier of ComponentName. Set this only if you want to explicitly set the component to handle the intent.  
type(optional)| `string`| A string specifying the MIME type of the data represented by the data parameter. Ignore this argument to allow Android to infer the correct MIME type.  
### `IntentLauncherResult`
Android
Property| Type| Description  
---|---|---  
data(optional)| `string`| Optional data URI that can be returned by the activity.  
extra(optional)| `object`| Optional extras object that can be returned by the activity.  
resultCode| | Result code returned by the activity.  
## Enums
### `ActivityAction`
Android
Constants are from the source code of [Settings provider](https://developer.android.com/reference/android/provider/Settings).
#### `ACCESSIBILITY_SETTINGS`
`ActivityAction.ACCESSIBILITY_SETTINGS ＝ "android.settings.ACCESSIBILITY_SETTINGS"`
#### `APP_NOTIFICATION_REDACTION`
`ActivityAction.APP_NOTIFICATION_REDACTION ＝ "android.settings.ACTION_APP_NOTIFICATION_REDACTION"`
#### `CONDITION_PROVIDER_SETTINGS`
`ActivityAction.CONDITION_PROVIDER_SETTINGS ＝ "android.settings.ACTION_CONDITION_PROVIDER_SETTINGS"`
#### `NOTIFICATION_LISTENER_SETTINGS`
`ActivityAction.NOTIFICATION_LISTENER_SETTINGS ＝ "android.settings.ACTION_NOTIFICATION_LISTENER_SETTINGS"`
#### `PRINT_SETTINGS`
`ActivityAction.PRINT_SETTINGS ＝ "android.settings.ACTION_PRINT_SETTINGS"`
#### `ADD_ACCOUNT_SETTINGS`
`ActivityAction.ADD_ACCOUNT_SETTINGS ＝ "android.settings.ADD_ACCOUNT_SETTINGS"`
#### `AIRPLANE_MODE_SETTINGS`
`ActivityAction.AIRPLANE_MODE_SETTINGS ＝ "android.settings.AIRPLANE_MODE_SETTINGS"`
#### `APN_SETTINGS`
`ActivityAction.APN_SETTINGS ＝ "android.settings.APN_SETTINGS"`
#### `APP_NOTIFICATION_SETTINGS`
`ActivityAction.APP_NOTIFICATION_SETTINGS ＝ "android.settings.APP_NOTIFICATION_SETTINGS"`
#### `APP_OPS_SETTINGS`
`ActivityAction.APP_OPS_SETTINGS ＝ "android.settings.APP_OPS_SETTINGS"`
#### `APPLICATION_DETAILS_SETTINGS`
`ActivityAction.APPLICATION_DETAILS_SETTINGS ＝ "android.settings.APPLICATION_DETAILS_SETTINGS"`
#### `APPLICATION_DEVELOPMENT_SETTINGS`
`ActivityAction.APPLICATION_DEVELOPMENT_SETTINGS ＝ "android.settings.APPLICATION_DEVELOPMENT_SETTINGS"`
#### `APPLICATION_SETTINGS`
`ActivityAction.APPLICATION_SETTINGS ＝ "android.settings.APPLICATION_SETTINGS"`
#### `BATTERY_SAVER_SETTINGS`
`ActivityAction.BATTERY_SAVER_SETTINGS ＝ "android.settings.BATTERY_SAVER_SETTINGS"`
#### `BLUETOOTH_SETTINGS`
`ActivityAction.BLUETOOTH_SETTINGS ＝ "android.settings.BLUETOOTH_SETTINGS"`
#### `CAPTIONING_SETTINGS`
`ActivityAction.CAPTIONING_SETTINGS ＝ "android.settings.CAPTIONING_SETTINGS"`
#### `CAST_SETTINGS`
`ActivityAction.CAST_SETTINGS ＝ "android.settings.CAST_SETTINGS"`
#### `DATA_ROAMING_SETTINGS`
`ActivityAction.DATA_ROAMING_SETTINGS ＝ "android.settings.DATA_ROAMING_SETTINGS"`
#### `DATE_SETTINGS`
`ActivityAction.DATE_SETTINGS ＝ "android.settings.DATE_SETTINGS"`
#### `DEVICE_INFO_SETTINGS`
`ActivityAction.DEVICE_INFO_SETTINGS ＝ "android.settings.DEVICE_INFO_SETTINGS"`
#### `DEVICE_NAME`
`ActivityAction.DEVICE_NAME ＝ "android.settings.DEVICE_NAME"`
#### `DISPLAY_SETTINGS`
`ActivityAction.DISPLAY_SETTINGS ＝ "android.settings.DISPLAY_SETTINGS"`
#### `DREAM_SETTINGS`
`ActivityAction.DREAM_SETTINGS ＝ "android.settings.DREAM_SETTINGS"`
#### `HARD_KEYBOARD_SETTINGS`
`ActivityAction.HARD_KEYBOARD_SETTINGS ＝ "android.settings.HARD_KEYBOARD_SETTINGS"`
#### `HOME_SETTINGS`
`ActivityAction.HOME_SETTINGS ＝ "android.settings.HOME_SETTINGS"`
#### `IGNORE_BACKGROUND_DATA_RESTRICTIONS_SETTINGS`
`ActivityAction.IGNORE_BACKGROUND_DATA_RESTRICTIONS_SETTINGS ＝ "android.settings.IGNORE_BACKGROUND_DATA_RESTRICTIONS_SETTINGS"`
#### `IGNORE_BATTERY_OPTIMIZATION_SETTINGS`
`ActivityAction.IGNORE_BATTERY_OPTIMIZATION_SETTINGS ＝ "android.settings.IGNORE_BATTERY_OPTIMIZATION_SETTINGS"`
#### `INPUT_METHOD_SETTINGS`
`ActivityAction.INPUT_METHOD_SETTINGS ＝ "android.settings.INPUT_METHOD_SETTINGS"`
#### `INPUT_METHOD_SUBTYPE_SETTINGS`
`ActivityAction.INPUT_METHOD_SUBTYPE_SETTINGS ＝ "android.settings.INPUT_METHOD_SUBTYPE_SETTINGS"`
#### `INTERNAL_STORAGE_SETTINGS`
`ActivityAction.INTERNAL_STORAGE_SETTINGS ＝ "android.settings.INTERNAL_STORAGE_SETTINGS"`
#### `LOCALE_SETTINGS`
`ActivityAction.LOCALE_SETTINGS ＝ "android.settings.LOCALE_SETTINGS"`
#### `LOCATION_SOURCE_SETTINGS`
`ActivityAction.LOCATION_SOURCE_SETTINGS ＝ "android.settings.LOCATION_SOURCE_SETTINGS"`
#### `MANAGE_ALL_APPLICATIONS_SETTINGS`
`ActivityAction.MANAGE_ALL_APPLICATIONS_SETTINGS ＝ "android.settings.MANAGE_ALL_APPLICATIONS_SETTINGS"`
#### `MANAGE_APPLICATIONS_SETTINGS`
`ActivityAction.MANAGE_APPLICATIONS_SETTINGS ＝ "android.settings.MANAGE_APPLICATIONS_SETTINGS"`
#### `MANAGE_DEFAULT_APPS_SETTINGS`
`ActivityAction.MANAGE_DEFAULT_APPS_SETTINGS ＝ "android.settings.MANAGE_DEFAULT_APPS_SETTINGS"`
#### `MEMORY_CARD_SETTINGS`
`ActivityAction.MEMORY_CARD_SETTINGS ＝ "android.settings.MEMORY_CARD_SETTINGS"`
#### `MONITORING_CERT_INFO`
`ActivityAction.MONITORING_CERT_INFO ＝ "android.settings.MONITORING_CERT_INFO"`
#### `NETWORK_OPERATOR_SETTINGS`
`ActivityAction.NETWORK_OPERATOR_SETTINGS ＝ "android.settings.NETWORK_OPERATOR_SETTINGS"`
#### `NFC_PAYMENT_SETTINGS`
`ActivityAction.NFC_PAYMENT_SETTINGS ＝ "android.settings.NFC_PAYMENT_SETTINGS"`
#### `NFC_SETTINGS`
`ActivityAction.NFC_SETTINGS ＝ "android.settings.NFC_SETTINGS"`
#### `NFCSHARING_SETTINGS`
`ActivityAction.NFCSHARING_SETTINGS ＝ "android.settings.NFCSHARING_SETTINGS"`
#### `NIGHT_DISPLAY_SETTINGS`
`ActivityAction.NIGHT_DISPLAY_SETTINGS ＝ "android.settings.NIGHT_DISPLAY_SETTINGS"`
#### `NOTIFICATION_POLICY_ACCESS_SETTINGS`
`ActivityAction.NOTIFICATION_POLICY_ACCESS_SETTINGS ＝ "android.settings.NOTIFICATION_POLICY_ACCESS_SETTINGS"`
#### `NOTIFICATION_SETTINGS`
`ActivityAction.NOTIFICATION_SETTINGS ＝ "android.settings.NOTIFICATION_SETTINGS"`
#### `PAIRING_SETTINGS`
`ActivityAction.PAIRING_SETTINGS ＝ "android.settings.PAIRING_SETTINGS"`
#### `PRIVACY_SETTINGS`
`ActivityAction.PRIVACY_SETTINGS ＝ "android.settings.PRIVACY_SETTINGS"`
#### `QUICK_LAUNCH_SETTINGS`
`ActivityAction.QUICK_LAUNCH_SETTINGS ＝ "android.settings.QUICK_LAUNCH_SETTINGS"`
#### `REQUEST_IGNORE_BATTERY_OPTIMIZATIONS`
`ActivityAction.REQUEST_IGNORE_BATTERY_OPTIMIZATIONS ＝ "android.settings.REQUEST_IGNORE_BATTERY_OPTIMIZATIONS"`
#### `SECURITY_SETTINGS`
`ActivityAction.SECURITY_SETTINGS ＝ "android.settings.SECURITY_SETTINGS"`
#### `SETTINGS`
`ActivityAction.SETTINGS ＝ "android.settings.SETTINGS"`
#### `SHOW_ADMIN_SUPPORT_DETAILS`
`ActivityAction.SHOW_ADMIN_SUPPORT_DETAILS ＝ "android.settings.SHOW_ADMIN_SUPPORT_DETAILS"`
#### `SHOW_INPUT_METHOD_PICKER`
`ActivityAction.SHOW_INPUT_METHOD_PICKER ＝ "android.settings.SHOW_INPUT_METHOD_PICKER"`
#### `SHOW_REGULATORY_INFO`
`ActivityAction.SHOW_REGULATORY_INFO ＝ "android.settings.SHOW_REGULATORY_INFO"`
#### `SHOW_REMOTE_BUGREPORT_DIALOG`
`ActivityAction.SHOW_REMOTE_BUGREPORT_DIALOG ＝ "android.settings.SHOW_REMOTE_BUGREPORT_DIALOG"`
#### `SOUND_SETTINGS`
`ActivityAction.SOUND_SETTINGS ＝ "android.settings.SOUND_SETTINGS"`
#### `STORAGE_MANAGER_SETTINGS`
`ActivityAction.STORAGE_MANAGER_SETTINGS ＝ "android.settings.STORAGE_MANAGER_SETTINGS"`
#### `SYNC_SETTINGS`
`ActivityAction.SYNC_SETTINGS ＝ "android.settings.SYNC_SETTINGS"`
#### `SYSTEM_UPDATE_SETTINGS`
`ActivityAction.SYSTEM_UPDATE_SETTINGS ＝ "android.settings.SYSTEM_UPDATE_SETTINGS"`
#### `TETHER_PROVISIONING_UI`
`ActivityAction.TETHER_PROVISIONING_UI ＝ "android.settings.TETHER_PROVISIONING_UI"`
#### `TRUSTED_CREDENTIALS_USER`
`ActivityAction.TRUSTED_CREDENTIALS_USER ＝ "android.settings.TRUSTED_CREDENTIALS_USER"`
#### `USAGE_ACCESS_SETTINGS`
`ActivityAction.USAGE_ACCESS_SETTINGS ＝ "android.settings.USAGE_ACCESS_SETTINGS"`
#### `USER_DICTIONARY_INSERT`
`ActivityAction.USER_DICTIONARY_INSERT ＝ "android.settings.USER_DICTIONARY_INSERT"`
#### `USER_DICTIONARY_SETTINGS`
`ActivityAction.USER_DICTIONARY_SETTINGS ＝ "android.settings.USER_DICTIONARY_SETTINGS"`
#### `USER_SETTINGS`
`ActivityAction.USER_SETTINGS ＝ "android.settings.USER_SETTINGS"`
#### `VOICE_CONTROL_AIRPLANE_MODE`
`ActivityAction.VOICE_CONTROL_AIRPLANE_MODE ＝ "android.settings.VOICE_CONTROL_AIRPLANE_MODE"`
#### `VOICE_CONTROL_BATTERY_SAVER_MODE`
`ActivityAction.VOICE_CONTROL_BATTERY_SAVER_MODE ＝ "android.settings.VOICE_CONTROL_BATTERY_SAVER_MODE"`
#### `VOICE_CONTROL_DO_NOT_DISTURB_MODE`
`ActivityAction.VOICE_CONTROL_DO_NOT_DISTURB_MODE ＝ "android.settings.VOICE_CONTROL_DO_NOT_DISTURB_MODE"`
#### `VOICE_INPUT_SETTINGS`
`ActivityAction.VOICE_INPUT_SETTINGS ＝ "android.settings.VOICE_INPUT_SETTINGS"`
#### `VPN_SETTINGS`
`ActivityAction.VPN_SETTINGS ＝ "android.settings.VPN_SETTINGS"`
#### `VR_LISTENER_SETTINGS`
`ActivityAction.VR_LISTENER_SETTINGS ＝ "android.settings.VR_LISTENER_SETTINGS"`
#### `WEBVIEW_SETTINGS`
`ActivityAction.WEBVIEW_SETTINGS ＝ "android.settings.WEBVIEW_SETTINGS"`
#### `WIFI_IP_SETTINGS`
`ActivityAction.WIFI_IP_SETTINGS ＝ "android.settings.WIFI_IP_SETTINGS"`
#### `WIFI_SETTINGS`
`ActivityAction.WIFI_SETTINGS ＝ "android.settings.WIFI_SETTINGS"`
#### `WIRELESS_SETTINGS`
`ActivityAction.WIRELESS_SETTINGS ＝ "android.settings.WIRELESS_SETTINGS"`
#### `ZEN_MODE_AUTOMATION_SETTINGS`
`ActivityAction.ZEN_MODE_AUTOMATION_SETTINGS ＝ "android.settings.ZEN_MODE_AUTOMATION_SETTINGS"`
#### `ZEN_MODE_EVENT_RULE_SETTINGS`
`ActivityAction.ZEN_MODE_EVENT_RULE_SETTINGS ＝ "android.settings.ZEN_MODE_EVENT_RULE_SETTINGS"`
#### `ZEN_MODE_EXTERNAL_RULE_SETTINGS`
`ActivityAction.ZEN_MODE_EXTERNAL_RULE_SETTINGS ＝ "android.settings.ZEN_MODE_EXTERNAL_RULE_SETTINGS"`
#### `ZEN_MODE_PRIORITY_SETTINGS`
`ActivityAction.ZEN_MODE_PRIORITY_SETTINGS ＝ "android.settings.ZEN_MODE_PRIORITY_SETTINGS"`
#### `ZEN_MODE_SCHEDULE_RULE_SETTINGS`
`ActivityAction.ZEN_MODE_SCHEDULE_RULE_SETTINGS ＝ "android.settings.ZEN_MODE_SCHEDULE_RULE_SETTINGS"`
#### `ZEN_MODE_SETTINGS`
`ActivityAction.ZEN_MODE_SETTINGS ＝ "android.settings.ZEN_MODE_SETTINGS"`
### `ResultCode`
Android
#### `Success`
`ResultCode.Success ＝ -1`
Indicates that the activity operation succeeded.
#### `Canceled`
`ResultCode.Canceled ＝ 0`
Means that the activity was canceled, e.g. by tapping on the back button.
#### `FirstUser`
`ResultCode.FirstUser ＝ 1`
First custom, user-defined value that can be returned by the activity.

