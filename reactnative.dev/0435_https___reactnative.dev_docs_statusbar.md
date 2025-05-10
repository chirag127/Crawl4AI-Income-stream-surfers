---
url: https://reactnative.dev/docs/statusbar
title: https://reactnative.dev/docs/statusbar
date: 2025-05-10T21:42:04.429318
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/statusbar#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
Component to control the app's status bar. The status bar is the zone, typically at the top of the screen, that displays the current time, Wi-Fi and cellular network information, battery level and/or other status icons.
### Usage with Navigator[​](https://reactnative.dev/docs/statusbar#usage-with-navigator "Direct link to Usage with Navigator")
It is possible to have multiple `StatusBar` components mounted at the same time. The props will be merged in the order the `StatusBar` components were mounted.
  * TypeScript
  * JavaScript


### Imperative API[​](https://reactnative.dev/docs/statusbar#imperative-api "Direct link to Imperative API")
For cases where using a component is not ideal, there is also an imperative API exposed as static functions on the component. It is however not recommended to use the static API and the component for the same prop because any value set by the static API will get overridden by the one set by the component in the next render.
# Reference
## Constants[​](https://reactnative.dev/docs/statusbar#constants "Direct link to Constants")
### `currentHeight`
Android
[​](https://reactnative.dev/docs/statusbar#currentheight-android "Direct link to currentheight-android")
The height of the status bar, which includes the notch height, if present.
## Props[​](https://reactnative.dev/docs/statusbar#props "Direct link to Props")
### `animated`[​](https://reactnative.dev/docs/statusbar#animated "Direct link to animated")
If the transition between status bar property changes should be animated. Supported for `backgroundColor`, `barStyle` and `hidden` properties.
Type| Required| Default  
---|---|---  
boolean| No| `false`  
### `backgroundColor`
Android
[​](https://reactnative.dev/docs/statusbar#backgroundcolor-android "Direct link to backgroundcolor-android")
The background color of the status bar.
warning
Due to edge-to-edge enforcement introduced in Android 15, setting background color of the status bar is deprecated in API level 35.
Type| Required| Default  
---|---|---  
No| default system StatusBar background color, or `'black'` if not defined  
### `barStyle`[​](https://reactnative.dev/docs/statusbar#barstyle "Direct link to barstyle")
Sets the color of the status bar text.
On Android, this will only have an impact on API versions 23 and above.
Type| Required| Default  
---|---|---  
No| `'default'`  
### `hidden`[​](https://reactnative.dev/docs/statusbar#hidden "Direct link to hidden")
If the status bar is hidden.
Type| Required| Default  
---|---|---  
boolean| No| `false`  
### `networkActivityIndicatorVisible`
iOS
[​](https://reactnative.dev/docs/statusbar#networkactivityindicatorvisible-ios "Direct link to networkactivityindicatorvisible-ios")
If the network activity indicator should be visible.
Type| Default  
---|---  
boolean| `false`  
### `showHideTransition`
iOS
[​](https://reactnative.dev/docs/statusbar#showhidetransition-ios "Direct link to showhidetransition-ios")
The transition effect when showing and hiding the status bar using the `hidden` prop.
Type| Default  
---|---  
[StatusBarAnimation](https://reactnative.dev/docs/statusbar#statusbaranimation)| `'fade'`  
### `translucent`
Android
[​](https://reactnative.dev/docs/statusbar#translucent-android "Direct link to translucent-android")
If the status bar is translucent. When translucent is set to `true`, the app will draw under the status bar. This is useful when using a semi transparent status bar color.
Type| Default  
---|---  
boolean| `false`  
## Methods[​](https://reactnative.dev/docs/statusbar#methods "Direct link to Methods")
### `popStackEntry()`[​](https://reactnative.dev/docs/statusbar#popstackentry "Direct link to popstackentry")
tsx
```
staticpopStackEntry(entry:StatusBarProps);
```

Get and remove the last StatusBar entry from the stack.
**Parameters:**
Name| Type| Description  
---|---|---  
entry Required| any| Entry returned from `pushStackEntry`.  
### `pushStackEntry()`[​](https://reactnative.dev/docs/statusbar#pushstackentry "Direct link to pushstackentry")
tsx
```
staticpushStackEntry(props:StatusBarProps):StatusBarProps;
```

Push a StatusBar entry onto the stack. The return value should be passed to `popStackEntry` when complete.
**Parameters:**
Name| Type| Description  
---|---|---  
props Required| any| Object containing the StatusBar props to use in the stack entry.  
### `replaceStackEntry()`[​](https://reactnative.dev/docs/statusbar#replacestackentry "Direct link to replacestackentry")
tsx
```
staticreplaceStackEntry( entry:StatusBarProps, props:StatusBarProps):StatusBarProps;
```

Replace an existing StatusBar stack entry with new props.
**Parameters:**
Name| Type| Description  
---|---|---  
entry Required| any| Entry returned from `pushStackEntry` to replace.  
props Required| any| Object containing the StatusBar props to use in the replacement stack entry.  
### `setBackgroundColor()`
Android
[​](https://reactnative.dev/docs/statusbar#setbackgroundcolor-android "Direct link to setbackgroundcolor-android")
tsx
```
staticsetBackgroundColor(color:ColorValue, animated?:boolean);
```

Set the background color for the status bar.
warning
Due to edge-to-edge enforcement introduced in Android 15, setting background color of the status bar is deprecated in API level 35.
**Parameters:**
Name| Type| Description  
---|---|---  
color Required| string| Background color.  
animated| boolean| Animate the style change.  
### `setBarStyle()`[​](https://reactnative.dev/docs/statusbar#setbarstyle "Direct link to setbarstyle")
tsx
```
staticsetBarStyle(style:StatusBarStyle, animated?:boolean);
```

Set the status bar style.
**Parameters:**
Name| Type| Description  
---|---|---  
style Required| Status bar style to set.  
animated| boolean| Animate the style change.  
### `setHidden()`[​](https://reactnative.dev/docs/statusbar#sethidden "Direct link to sethidden")
tsx
```
staticsetHidden(hidden:boolean, animation?:StatusBarAnimation);
```

Show or hide the status bar.
**Parameters:**
Name| Type| Description  
---|---|---  
hidden Required| boolean| Hide the status bar.  
animation iOS| [StatusBarAnimation](https://reactnative.dev/docs/statusbar#statusbaranimation)| Animation when changing the status bar hidden property.  
### `setNetworkActivityIndicatorVisible()`
iOS
[​](https://reactnative.dev/docs/statusbar#setnetworkactivityindicatorvisible-ios "Direct link to setnetworkactivityindicatorvisible-ios")
tsx
```
staticsetNetworkActivityIndicatorVisible(visible:boolean);
```

Control the visibility of the network activity indicator.
**Parameters:**
Name| Type| Description  
---|---|---  
visible Required| boolean| Show the indicator.  
### `setTranslucent()`
Android
[​](https://reactnative.dev/docs/statusbar#settranslucent-android "Direct link to settranslucent-android")
tsx
```
staticsetTranslucent(translucent:boolean);
```

Control the translucency of the status bar.
**Parameters:**
Name| Type| Description  
---|---|---  
translucent Required| boolean| Set as translucent.  
## Type Definitions[​](https://reactnative.dev/docs/statusbar#type-definitions "Direct link to Type Definitions")
### StatusBarAnimation[​](https://reactnative.dev/docs/statusbar#statusbaranimation "Direct link to StatusBarAnimation")
Status bar animation type for transitions on the iOS.
Type  
---  
enum  
**Constants:**
Value| Type| Description  
---|---|---  
`'fade'`| string| Fade animation  
`'slide'`| string| Slide animation  
`'none'`| string| No animation  
### StatusBarStyle[​](https://reactnative.dev/docs/statusbar#statusbarstyle "Direct link to StatusBarStyle")
Status bar style type.
Type  
---  
enum  
**Constants:**
Value| Type| Description  
---|---|---  
`'default'`| string| Default status bar style (dark for iOS, light for Android)  
`'light-content'`| string| White texts and icons  
`'dark-content'`| string| Dark texts and icons (requires API>=23 on Android)  
Is this page useful?
  * [Usage with Navigator](https://reactnative.dev/docs/statusbar#usage-with-navigator)
  * [Imperative API](https://reactnative.dev/docs/statusbar#imperative-api)
  * [Constants](https://reactnative.dev/docs/statusbar#constants)
    * [`currentHeight` Android](https://reactnative.dev/docs/statusbar#currentheight-android)
  * [Props](https://reactnative.dev/docs/statusbar#props)
    * [`backgroundColor` Android](https://reactnative.dev/docs/statusbar#backgroundcolor-android)
    * [`networkActivityIndicatorVisible` iOS](https://reactnative.dev/docs/statusbar#networkactivityindicatorvisible-ios)
    * [`showHideTransition` iOS](https://reactnative.dev/docs/statusbar#showhidetransition-ios)
    * [`translucent` Android](https://reactnative.dev/docs/statusbar#translucent-android)
  * [Methods](https://reactnative.dev/docs/statusbar#methods)
    * [`popStackEntry()`](https://reactnative.dev/docs/statusbar#popstackentry)
    * [`pushStackEntry()`](https://reactnative.dev/docs/statusbar#pushstackentry)
    * [`replaceStackEntry()`](https://reactnative.dev/docs/statusbar#replacestackentry)
    * [`setBackgroundColor()` Android](https://reactnative.dev/docs/statusbar#setbackgroundcolor-android)
    * [`setNetworkActivityIndicatorVisible()` iOS](https://reactnative.dev/docs/statusbar#setnetworkactivityindicatorvisible-ios)
    * [`setTranslucent()` Android](https://reactnative.dev/docs/statusbar#settranslucent-android)
  * [Type Definitions](https://reactnative.dev/docs/statusbar#type-definitions)
    * [StatusBarAnimation](https://reactnative.dev/docs/statusbar#statusbaranimation)
    * [StatusBarStyle](https://reactnative.dev/docs/statusbar#statusbarstyle)



