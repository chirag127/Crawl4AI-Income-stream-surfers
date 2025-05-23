---
url: https://reactnative.dev/docs/alert
title: https://reactnative.dev/docs/alert
date: 2025-05-10T21:39:24.580339
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/alert#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
Launches an alert dialog with the specified title and message.
Optionally provide a list of buttons. Tapping any button will fire the respective onPress callback and dismiss the alert. By default, the only button will be an 'OK' button.
This is an API that works both on Android and iOS and can show static alerts. Alert that prompts the user to enter some information is available on iOS only.
## Example[​](https://reactnative.dev/docs/alert#example "Direct link to Example")
## iOS[​](https://reactnative.dev/docs/alert#ios "Direct link to iOS")
On iOS you can specify any number of buttons. Each button can optionally specify a style or be emphasized, available options are represented by the [AlertButtonStyle](https://reactnative.dev/docs/alert#alertbuttonstyle-ios) enum and the `isPreferred` field on [AlertButton](https://reactnative.dev/docs/alert#alertbutton).
## Android[​](https://reactnative.dev/docs/alert#android "Direct link to Android")
On Android at most three buttons can be specified. Android has a concept of a neutral, negative and a positive button:
  * If you specify one button, it will be the 'positive' one (such as 'OK')
  * Two buttons mean 'negative', 'positive' (such as 'Cancel', 'OK')
  * Three buttons mean 'neutral', 'negative', 'positive' (such as 'Later', 'Cancel', 'OK')


Alerts on Android can be dismissed by tapping outside of the alert box. It is disabled by default and can be enabled by providing an optional [AlertOptions](https://reactnative.dev/docs/alert#alertoptions) parameter with the cancelable property set to `true` i.e.`{cancelable: true}`.
The cancel event can be handled by providing an `onDismiss` callback property inside the `options` parameter.
### Example 
Android
[​](https://reactnative.dev/docs/alert#example-android "Direct link to example-android")
# Reference
## Methods[​](https://reactnative.dev/docs/alert#methods "Direct link to Methods")
### `alert()`[​](https://reactnative.dev/docs/alert#alert "Direct link to alert")
tsx
```
staticalert( title:string, message?:string, buttons?:AlertButton[], options?:AlertOptions,
```

**Parameters:**
Name| Type| Description  
---|---|---  
title Required| string| The dialog's title. Passing `null` or empty string will hide the title.  
message| string| An optional message that appears below the dialog's title.  
buttons| [AlertButton](https://reactnative.dev/docs/alert#alertbutton)[]| An optional array containing buttons configuration.  
options| An optional Alert configuration.  
### `prompt()`
iOS
[​](https://reactnative.dev/docs/alert#prompt-ios "Direct link to prompt-ios")
tsx
```
static prompt:( title:string, message?:string, callbackOrButtons?:((text:string)=>void)|AlertButton[], type?:AlertType, defaultValue?:string, keyboardType?:string,
```

Create and display a prompt to enter some text in form of Alert.
**Parameters:**
Name| Type| Description  
---|---|---  
title Required| string| The dialog's title.  
message| string| An optional message that appears above the text input.  
callbackOrButtons| function[AlertButton](https://reactnative.dev/docs/alert#alertButton)[]| If passed a function, it will be called with the prompt's value`(text: string) => void`, when the user taps 'OK'.If passed an array, buttons will be configured based on the array content.  
type| This configures the text input.  
defaultValue| string| The default text in text input.  
keyboardType| string| The keyboard type of first text field (if exists). One of TextInput [keyboardTypes](https://reactnative.dev/docs/textinput#keyboardtype).  
options| An optional Alert configuration.  
## Type Definitions[​](https://reactnative.dev/docs/alert#type-definitions "Direct link to Type Definitions")
### AlertButtonStyle 
iOS
[​](https://reactnative.dev/docs/alert#alertbuttonstyle-ios "Direct link to alertbuttonstyle-ios")
An iOS Alert button style.
Type  
---  
enum  
**Constants:**
Value| Description  
---|---  
`'default'`| Default button style.  
`'cancel'`| Cancel button style.  
`'destructive'`| Destructive button style.  
### AlertType 
iOS
[​](https://reactnative.dev/docs/alert#alerttype-ios "Direct link to alerttype-ios")
An iOS Alert type.
Type  
---  
enum  
**Constants:**
Value| Description  
---|---  
`'default'`| Default alert with no inputs  
`'plain-text'`| Plain text input alert  
`'secure-text'`| Secure text input alert  
`'login-password'`| Login and password alert  
### AlertButton[​](https://reactnative.dev/docs/alert#alertbutton "Direct link to AlertButton")
An object describing the configuration of a button in the alert.
Type  
---  
array of objects  
**Objects properties:**
Name| Type| Description  
---|---|---  
text| string| Button label.  
onPress| function| Callback function when button is pressed.  
style iOS| [AlertButtonStyle](https://reactnative.dev/docs/alert#alertbuttonstyle-ios)| Button style, on Android this property will be ignored.  
isPreferred iOS| boolean| Whether button should be emphasized, on Android this property will be ignored.  
### AlertOptions[​](https://reactnative.dev/docs/alert#alertoptions "Direct link to AlertOptions")
Type  
---  
object  
**Properties:**
Name| Type| Description  
---|---|---  
cancelable Android| boolean| Defines if alert can be dismissed by tapping outside of the alert box.  
userInterfaceStyle iOS| string| The interface style used for the alert, can be set to `light` or `dark`, otherwise the default system style will be used.  
onDismiss Android| function| Callback function fired when alert has been dismissed.  
Is this page useful?
  * [Android](https://reactnative.dev/docs/alert#android)
    * [Example Android](https://reactnative.dev/docs/alert#example-android)
  * [Methods](https://reactnative.dev/docs/alert#methods)
    * [`prompt()` iOS](https://reactnative.dev/docs/alert#prompt-ios)
  * [Type Definitions](https://reactnative.dev/docs/alert#type-definitions)
    * [AlertButtonStyle iOS](https://reactnative.dev/docs/alert#alertbuttonstyle-ios)
    * [AlertType iOS](https://reactnative.dev/docs/alert#alerttype-ios)



