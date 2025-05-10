---
url: https://reactnative.dev/docs/modal
title: https://reactnative.dev/docs/modal
date: 2025-05-10T21:41:01.598315
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/modal#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
The Modal component is a basic way to present content above an enclosing view.
## Example[​](https://reactnative.dev/docs/modal#example "Direct link to Example")
# Reference
## Props[​](https://reactnative.dev/docs/modal#props "Direct link to Props")
### [View Props](https://reactnative.dev/docs/view#props)[​](https://reactnative.dev/docs/modal#view-props "Direct link to view-props")
Inherits [View Props](https://reactnative.dev/docs/view#props).
### `animated`[​](https://reactnative.dev/docs/modal#animated "Direct link to animated")
> **Deprecated.** Use the [`animationType`](https://reactnative.dev/docs/modal#animationtype) prop instead.
### `animationType`[​](https://reactnative.dev/docs/modal#animationtype "Direct link to animationtype")
The `animationType` prop controls how the modal animates.
Possible values:
  * `slide` slides in from the bottom
  * `fade` fades into view
  * `none` appears without an animation

Type| Default  
---|---  
enum(`'none'`, `'slide'`, `'fade'`)| `none`  
### `backdropColor`[​](https://reactnative.dev/docs/modal#backdropcolor "Direct link to backdropcolor")
The `backdropColor` of the modal (or background color of the modal's container.) Defaults to `white` if not provided and transparent is `false`. Ignored if `transparent` is `true`.
Type| Default  
---|---  
white  
### `hardwareAccelerated`
Android
[​](https://reactnative.dev/docs/modal#hardwareaccelerated-android "Direct link to hardwareaccelerated-android")
The `hardwareAccelerated` prop controls whether to force hardware acceleration for the underlying window.
Type| Default  
---|---  
bool| `false`  
### `navigationBarTranslucent`
Android
[​](https://reactnative.dev/docs/modal#navigationbartranslucent-android "Direct link to navigationbartranslucent-android")
The `navigationBarTranslucent` prop determines whether your modal should go under the system navigation bar. However, `statusBarTranslucent` also needs to be set to `true` to make navigation bar translucent.
Type| Default  
---|---  
bool| `false`  
### `onDismiss`
iOS
[​](https://reactnative.dev/docs/modal#ondismiss-ios "Direct link to ondismiss-ios")
The `onDismiss` prop allows passing a function that will be called once the modal has been dismissed.
Type  
---  
function  
### `onOrientationChange`
iOS
[​](https://reactnative.dev/docs/modal#onorientationchange-ios "Direct link to onorientationchange-ios")
The `onOrientationChange` callback is called when the orientation changes while the modal is being displayed. The orientation provided is only 'portrait' or 'landscape'. This callback is also called on initial render, regardless of the current orientation.
Type  
---  
function  
### `onRequestClose`[​](https://reactnative.dev/docs/modal#onrequestclose "Direct link to onrequestclose")
The `onRequestClose` callback is called when the user taps the hardware back button on Android or the menu button on Apple TV. Because of this required prop, be aware that `BackHandler` events will not be emitted as long as the modal is open. On iOS, this callback is called when a Modal is being dismissed using a drag gesture when `presentationStyle` is `pageSheet or formSheet`
Type  
---  
function RequiredAndroidTVfunction iOS  
### `onShow`[​](https://reactnative.dev/docs/modal#onshow "Direct link to onshow")
The `onShow` prop allows passing a function that will be called once the modal has been shown.
Type  
---  
function  
### `presentationStyle`
iOS
[​](https://reactnative.dev/docs/modal#presentationstyle-ios "Direct link to presentationstyle-ios")
The `presentationStyle` prop controls how the modal appears (generally on larger devices such as iPad or plus-sized iPhones). See <https://developer.apple.com/reference/uikit/uimodalpresentationstyle> for details.
Possible values:
  * `fullScreen` covers the screen completely
  * `pageSheet` covers portrait-width view centered (only on larger devices)
  * `formSheet` covers narrow-width view centered (only on larger devices)
  * `overFullScreen` covers the screen completely, but allows transparency

Type| Default  
---|---  
enum(`'fullScreen'`, `'pageSheet'`, `'formSheet'`, `'overFullScreen'`)| `fullScreen` if `transparent={false}``overFullScreen` if `transparent={true}`  
### `statusBarTranslucent`
Android
[​](https://reactnative.dev/docs/modal#statusbartranslucent-android "Direct link to statusbartranslucent-android")
The `statusBarTranslucent` prop determines whether your modal should go under the system statusbar.
Type| Default  
---|---  
bool| `false`  
### `supportedOrientations`
iOS
[​](https://reactnative.dev/docs/modal#supportedorientations-ios "Direct link to supportedorientations-ios")
The `supportedOrientations` prop allows the modal to be rotated to any of the specified orientations. On iOS, the modal is still restricted by what's specified in your app's Info.plist's UISupportedInterfaceOrientations field.
> When using `presentationStyle` of `pageSheet` or `formSheet`, this property will be ignored by iOS.
Type| Default  
---|---  
array of enums(`'portrait'`, `'portrait-upside-down'`, `'landscape'`, `'landscape-left'`, `'landscape-right'`)| `['portrait']`  
### `transparent`[​](https://reactnative.dev/docs/modal#transparent "Direct link to transparent")
The `transparent` prop determines whether your modal will fill the entire view. Setting this to `true` will render the modal over a transparent background.
Type| Default  
---|---  
bool| `false`  
### `visible`[​](https://reactnative.dev/docs/modal#visible "Direct link to visible")
The `visible` prop determines whether your modal is visible.
Type| Default  
---|---  
bool| `true`  
Is this page useful?
  * [Props](https://reactnative.dev/docs/modal#props)
    * [`hardwareAccelerated` Android](https://reactnative.dev/docs/modal#hardwareaccelerated-android)
    * [`navigationBarTranslucent` Android](https://reactnative.dev/docs/modal#navigationbartranslucent-android)
    * [`onDismiss` iOS](https://reactnative.dev/docs/modal#ondismiss-ios)
    * [`onOrientationChange` iOS](https://reactnative.dev/docs/modal#onorientationchange-ios)
    * [`presentationStyle` iOS](https://reactnative.dev/docs/modal#presentationstyle-ios)
    * [`statusBarTranslucent` Android](https://reactnative.dev/docs/modal#statusbartranslucent-android)
    * [`supportedOrientations` iOS](https://reactnative.dev/docs/modal#supportedorientations-ios)



