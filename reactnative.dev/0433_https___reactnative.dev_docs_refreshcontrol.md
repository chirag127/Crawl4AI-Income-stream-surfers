---
url: https://reactnative.dev/docs/refreshcontrol
title: https://reactnative.dev/docs/refreshcontrol
date: 2025-05-10T21:42:02.611305
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/refreshcontrol#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
This component is used inside a ScrollView or ListView to add pull to refresh functionality. When the ScrollView is at `scrollY: 0`, swiping down triggers an `onRefresh` event.
## Example[​](https://reactnative.dev/docs/refreshcontrol#example "Direct link to Example")
> Note: `refreshing` is a controlled prop, this is why it needs to be set to `true` in the `onRefresh` function otherwise the refresh indicator will stop immediately.
# Reference
## Props[​](https://reactnative.dev/docs/refreshcontrol#props "Direct link to Props")
### [View Props](https://reactnative.dev/docs/view#props)[​](https://reactnative.dev/docs/refreshcontrol#view-props "Direct link to view-props")
Inherits [View Props](https://reactnative.dev/docs/view#props).
### 
Required
**`refreshing`**[​](https://reactnative.dev/docs/refreshcontrol#requiredrefreshing "Direct link to requiredrefreshing")
Whether the view should be indicating an active refresh.
Type  
---  
boolean  
### `colors`
Android
[​](https://reactnative.dev/docs/refreshcontrol#colors-android "Direct link to colors-android")
The colors (at least one) that will be used to draw the refresh indicator.
Type  
---  
array of [colors](https://reactnative.dev/docs/colors)  
### `enabled`
Android
[​](https://reactnative.dev/docs/refreshcontrol#enabled-android "Direct link to enabled-android")
Whether the pull to refresh functionality is enabled.
Type| Default  
---|---  
boolean| `true`  
### `onRefresh`[​](https://reactnative.dev/docs/refreshcontrol#onrefresh "Direct link to onrefresh")
Called when the view starts refreshing.
Type  
---  
function  
### `progressBackgroundColor`
Android
[​](https://reactnative.dev/docs/refreshcontrol#progressbackgroundcolor-android "Direct link to progressbackgroundcolor-android")
The background color of the refresh indicator.
Type  
---  
### `progressViewOffset`[​](https://reactnative.dev/docs/refreshcontrol#progressviewoffset "Direct link to progressviewoffset")
Progress view top offset.
Type| Default  
---|---  
number  
### `size`
Android
[​](https://reactnative.dev/docs/refreshcontrol#size-android "Direct link to size-android")
Size of the refresh indicator.
Type| Default  
---|---  
enum(`'default'`, `'large'`)| `'default'`  
### `tintColor`
iOS
[​](https://reactnative.dev/docs/refreshcontrol#tintcolor-ios "Direct link to tintcolor-ios")
The color of the refresh indicator.
Type  
---  
### `title`
iOS
[​](https://reactnative.dev/docs/refreshcontrol#title-ios "Direct link to title-ios")
The title displayed under the refresh indicator.
Type  
---  
string  
### `titleColor`
iOS
[​](https://reactnative.dev/docs/refreshcontrol#titlecolor-ios "Direct link to titlecolor-ios")
The color of the refresh indicator title.
Type  
---  
Is this page useful?
  * [Props](https://reactnative.dev/docs/refreshcontrol#props)
    * [Required**`refreshing`**](https://reactnative.dev/docs/refreshcontrol#requiredrefreshing)
    * [`colors` Android](https://reactnative.dev/docs/refreshcontrol#colors-android)
    * [`enabled` Android](https://reactnative.dev/docs/refreshcontrol#enabled-android)
    * [`progressBackgroundColor` Android](https://reactnative.dev/docs/refreshcontrol#progressbackgroundcolor-android)
    * [`progressViewOffset`](https://reactnative.dev/docs/refreshcontrol#progressviewoffset)
    * [`size` Android](https://reactnative.dev/docs/refreshcontrol#size-android)
    * [`tintColor` iOS](https://reactnative.dev/docs/refreshcontrol#tintcolor-ios)
    * [`title` iOS](https://reactnative.dev/docs/refreshcontrol#title-ios)
    * [`titleColor` iOS](https://reactnative.dev/docs/refreshcontrol#titlecolor-ios)



