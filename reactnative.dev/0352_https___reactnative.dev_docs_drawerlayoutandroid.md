---
url: https://reactnative.dev/docs/drawerlayoutandroid
title: https://reactnative.dev/docs/drawerlayoutandroid
date: 2025-05-10T21:39:59.422031
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/drawerlayoutandroid#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
React component that wraps the platform `DrawerLayout` (Android only). The Drawer (typically used for navigation) is rendered with `renderNavigationView` and direct children are the main view (where your content goes). The navigation view is initially not visible on the screen, but can be pulled in from the side of the window specified by the `drawerPosition` prop and its width can be set by the `drawerWidth` prop.
## Example[​](https://reactnative.dev/docs/drawerlayoutandroid#example "Direct link to Example")
  * TypeScript
  * JavaScript


# Reference
## Props[​](https://reactnative.dev/docs/drawerlayoutandroid#props "Direct link to Props")
### [View Props](https://reactnative.dev/docs/view#props)[​](https://reactnative.dev/docs/drawerlayoutandroid#view-props "Direct link to view-props")
Inherits [View Props](https://reactnative.dev/docs/view#props).
### `drawerBackgroundColor`[​](https://reactnative.dev/docs/drawerlayoutandroid#drawerbackgroundcolor "Direct link to drawerbackgroundcolor")
Specifies the background color of the drawer. The default value is `white`. If you want to set the opacity of the drawer, use rgba. Example:
tsx
```
return(<DrawerLayoutAndroiddrawerBackgroundColor="rgba(0,0,0,0.5)"/>
```

Type| Required  
---|---  
No  
### `drawerLockMode`[​](https://reactnative.dev/docs/drawerlayoutandroid#drawerlockmode "Direct link to drawerlockmode")
Specifies the lock mode of the drawer. The drawer can be locked in 3 states:
  * unlocked (default), meaning that the drawer will respond (open/close) to touch gestures.
  * locked-closed, meaning that the drawer will stay closed and not respond to gestures.
  * locked-open, meaning that the drawer will stay opened and not respond to gestures. The drawer may still be opened and closed programmatically (`openDrawer`/`closeDrawer`).

Type| Required  
---|---  
enum('unlocked', 'locked-closed', 'locked-open')| No  
### `drawerPosition`[​](https://reactnative.dev/docs/drawerlayoutandroid#drawerposition "Direct link to drawerposition")
Specifies the side of the screen from which the drawer will slide in. By default it is set to `left`.
Type| Required  
---|---  
enum('left', 'right')| No  
### `drawerWidth`[​](https://reactnative.dev/docs/drawerlayoutandroid#drawerwidth "Direct link to drawerwidth")
Specifies the width of the drawer, more precisely the width of the view that be pulled in from the edge of the window.
Type| Required  
---|---  
number| No  
### `keyboardDismissMode`[​](https://reactnative.dev/docs/drawerlayoutandroid#keyboarddismissmode "Direct link to keyboarddismissmode")
Determines whether the keyboard gets dismissed in response to a drag.
  * 'none' (the default), drags do not dismiss the keyboard.
  * 'on-drag', the keyboard is dismissed when a drag begins.

Type| Required  
---|---  
enum('none', 'on-drag')| No  
### `onDrawerClose`[​](https://reactnative.dev/docs/drawerlayoutandroid#ondrawerclose "Direct link to ondrawerclose")
Function called whenever the navigation view has been closed.
Type| Required  
---|---  
function| No  
### `onDrawerOpen`[​](https://reactnative.dev/docs/drawerlayoutandroid#ondraweropen "Direct link to ondraweropen")
Function called whenever the navigation view has been opened.
Type| Required  
---|---  
function| No  
### `onDrawerSlide`[​](https://reactnative.dev/docs/drawerlayoutandroid#ondrawerslide "Direct link to ondrawerslide")
Function called whenever there is an interaction with the navigation view.
Type| Required  
---|---  
function| No  
### `onDrawerStateChanged`[​](https://reactnative.dev/docs/drawerlayoutandroid#ondrawerstatechanged "Direct link to ondrawerstatechanged")
Function called when the drawer state has changed. The drawer can be in 3 states:
  * idle, meaning there is no interaction with the navigation view happening at the time
  * dragging, meaning there is currently an interaction with the navigation view
  * settling, meaning that there was an interaction with the navigation view, and the navigation view is now finishing its closing or opening animation

Type| Required  
---|---  
function| No  
### `renderNavigationView`[​](https://reactnative.dev/docs/drawerlayoutandroid#rendernavigationview "Direct link to rendernavigationview")
The navigation view that will be rendered to the side of the screen and can be pulled in.
Type| Required  
---|---  
function| Yes  
### `statusBarBackgroundColor`[​](https://reactnative.dev/docs/drawerlayoutandroid#statusbarbackgroundcolor "Direct link to statusbarbackgroundcolor")
Make the drawer take the entire screen and draw the background of the status bar to allow it to open over the status bar. It will only have an effect on API 21+.
Type| Required  
---|---  
No  
## Methods[​](https://reactnative.dev/docs/drawerlayoutandroid#methods "Direct link to Methods")
### `closeDrawer()`[​](https://reactnative.dev/docs/drawerlayoutandroid#closedrawer "Direct link to closedrawer")
tsx
```
closeDrawer();
```

Closes the drawer.
### `openDrawer()`[​](https://reactnative.dev/docs/drawerlayoutandroid#opendrawer "Direct link to opendrawer")
tsx
```
openDrawer();
```

Opens the drawer.
Is this page useful?
  * [Props](https://reactnative.dev/docs/drawerlayoutandroid#props)
    * [`drawerBackgroundColor`](https://reactnative.dev/docs/drawerlayoutandroid#drawerbackgroundcolor)
    * [`keyboardDismissMode`](https://reactnative.dev/docs/drawerlayoutandroid#keyboarddismissmode)
    * [`onDrawerStateChanged`](https://reactnative.dev/docs/drawerlayoutandroid#ondrawerstatechanged)
    * [`renderNavigationView`](https://reactnative.dev/docs/drawerlayoutandroid#rendernavigationview)
    * [`statusBarBackgroundColor`](https://reactnative.dev/docs/drawerlayoutandroid#statusbarbackgroundcolor)
  * [Methods](https://reactnative.dev/docs/drawerlayoutandroid#methods)



