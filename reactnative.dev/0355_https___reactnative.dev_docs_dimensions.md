---
url: https://reactnative.dev/docs/dimensions
title: https://reactnative.dev/docs/dimensions
date: 2025-05-10T21:39:59.432665
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/dimensions#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
> [`useWindowDimensions`](https://reactnative.dev/docs/usewindowdimensions) is the preferred API for React components. Unlike `Dimensions`, it updates as the window's dimensions update. This works nicely with the React paradigm.
tsx
```
import{Dimensions}from'react-native';
```

You can get the application window's width and height using the following code:
tsx
```
const windowWidth =Dimensions.get('window').width;const windowHeight =Dimensions.get('window').height;
```

> Although dimensions are available immediately, they may change (e.g due to device rotation, foldable devices etc) so any rendering logic or styles that depend on these constants should try to call this function on every render, rather than caching the value (for example, using inline styles rather than setting a value in a `StyleSheet`).
If you are targeting foldable devices or devices which can change the screen size or app window size, you can use the event listener available in the Dimensions module as shown in the below example.
## Example[​](https://reactnative.dev/docs/dimensions#example "Direct link to Example")
# Reference
## Methods[​](https://reactnative.dev/docs/dimensions#methods "Direct link to Methods")
### `addEventListener()`[​](https://reactnative.dev/docs/dimensions#addeventlistener "Direct link to addeventlistener")
tsx
```
staticaddEventListener( type:'change',handler:({window,  screen,}:DimensionsValue)=>void,):EmitterSubscription;
```

Add an event handler. Supported events:
  * `change`: Fires when a property within the `Dimensions` object changes. The argument to the event handler is a [`DimensionsValue`](https://reactnative.dev/docs/dimensions#dimensionsvalue) type object.


### `get()`[​](https://reactnative.dev/docs/dimensions#get "Direct link to get")
tsx
```
staticget(dim:'window'|'screen'):ScaledSize;
```

Initial dimensions are set before `runApplication` is called so they should be available before any other require's are run, but may be updated later.
Example: `const {height, width} = Dimensions.get('window');`
**Parameters:**
Name| Type| Description  
---|---|---  
dim Required| string| Name of dimension as defined when calling `set`. Returns value for the dimension.  
> For Android the `window` dimension will exclude the size used by the `status bar` (if not translucent) and `bottom navigation bar`
## Type Definitions[​](https://reactnative.dev/docs/dimensions#type-definitions "Direct link to Type Definitions")
### DimensionsValue[​](https://reactnative.dev/docs/dimensions#dimensionsvalue "Direct link to DimensionsValue")
**Properties:**
Name| Type| Description  
---|---|---  
window| Size of the visible Application window.  
screen| Size of the device's screen.  
### ScaledSize[​](https://reactnative.dev/docs/dimensions#scaledsize "Direct link to ScaledSize")
Type  
---  
object  
**Properties:**
Name| Type  
---|---  
width| number  
height| number  
scale| number  
fontScale| number  
Is this page useful?
  * [Methods](https://reactnative.dev/docs/dimensions#methods)
    * [`addEventListener()`](https://reactnative.dev/docs/dimensions#addeventlistener)
  * [Type Definitions](https://reactnative.dev/docs/dimensions#type-definitions)
    * [DimensionsValue](https://reactnative.dev/docs/dimensions#dimensionsvalue)



