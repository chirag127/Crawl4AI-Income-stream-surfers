---
url: https://reactnative.dev/docs/animatedvaluexy
title: https://reactnative.dev/docs/animatedvaluexy
date: 2025-05-10T21:39:24.610585
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/animatedvaluexy#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
2D Value for driving 2D animations, such as pan gestures. Almost identical API to normal [`Animated.Value`](https://reactnative.dev/docs/animatedvalue), but multiplexed. Contains two regular `Animated.Value`s under the hood.
## Example[​](https://reactnative.dev/docs/animatedvaluexy#example "Direct link to Example")
# Reference
## Methods[​](https://reactnative.dev/docs/animatedvaluexy#methods "Direct link to Methods")
### `setValue()`[​](https://reactnative.dev/docs/animatedvaluexy#setvalue "Direct link to setvalue")
tsx
```
setValue(value:{x:number; y:number});
```

Directly set the value. This will stop any animations running on the value and update all the bound properties.
**Parameters:**
Name| Type| Required| Description  
---|---|---|---  
value| `{x: number; y: number}`| Yes| Value  
### `setOffset()`[​](https://reactnative.dev/docs/animatedvaluexy#setoffset "Direct link to setoffset")
tsx
```
setOffset(offset:{x:number; y:number});
```

Sets an offset that is applied on top of whatever value is set, whether via `setValue`, an animation, or `Animated.event`. Useful for compensating things like the start of a pan gesture.
**Parameters:**
Name| Type| Required| Description  
---|---|---|---  
offset| `{x: number; y: number}`| Yes| Offset value  
### `flattenOffset()`[​](https://reactnative.dev/docs/animatedvaluexy#flattenoffset "Direct link to flattenoffset")
tsx
```
flattenOffset();
```

Merges the offset value into the base value and resets the offset to zero. The final output of the value is unchanged.
### `extractOffset()`[​](https://reactnative.dev/docs/animatedvaluexy#extractoffset "Direct link to extractoffset")
tsx
```
extractOffset();
```

Sets the offset value to the base value, and resets the base value to zero. The final output of the value is unchanged.
### `addListener()`[​](https://reactnative.dev/docs/animatedvaluexy#addlistener "Direct link to addlistener")
tsx
```
addListener(callback:(value:{x:number; y:number})=>void);
```

Adds an asynchronous listener to the value so you can observe updates from animations. This is useful because there is no way to synchronously read the value because it might be driven natively.
Returns a string that serves as an identifier for the listener.
**Parameters:**
Name| Type| Required| Description  
---|---|---|---  
callback| function| Yes| The callback function which will receive an object with a `value` key set to the new value.  
### `removeListener()`[​](https://reactnative.dev/docs/animatedvaluexy#removelistener "Direct link to removelistener")
tsx
```
removeListener(id:string);
```

Unregister a listener. The `id` param shall match the identifier previously returned by `addListener()`.
**Parameters:**
Name| Type| Required| Description  
---|---|---|---  
id| string| Yes| Id for the listener being removed.  
### `removeAllListeners()`[​](https://reactnative.dev/docs/animatedvaluexy#removealllisteners "Direct link to removealllisteners")
tsx
```
removeAllListeners();
```

Remove all registered listeners.
### `stopAnimation()`[​](https://reactnative.dev/docs/animatedvaluexy#stopanimation "Direct link to stopanimation")
tsx
```
stopAnimation(callback?:(value:{x:number; y:number})=>void);
```

Stops any running animation or tracking. `callback` is invoked with the final value after stopping the animation, which is useful for updating state to match the animation position with layout.
**Parameters:**
Name| Type| Required| Description  
---|---|---|---  
callback| function| No| A function that will receive the final value.  
### `resetAnimation()`[​](https://reactnative.dev/docs/animatedvaluexy#resetanimation "Direct link to resetanimation")
tsx
```
resetAnimation(callback?:(value:{x:number; y:number})=>void);
```

Stops any animation and resets the value to its original.
**Parameters:**
Name| Type| Required| Description  
---|---|---|---  
callback| function| No| A function that will receive the original value.  
### `getLayout()`[​](https://reactnative.dev/docs/animatedvaluexy#getlayout "Direct link to getlayout")
tsx
```
getLayout():{left:Animated.Value, top:Animated.Value};
```

Converts `{x, y}` into `{left, top}` for use in style, e.g.
tsx
```
style={this.state.anim.getLayout()}
```

### `getTranslateTransform()`[​](https://reactnative.dev/docs/animatedvaluexy#gettranslatetransform "Direct link to gettranslatetransform")
tsx
```
getTranslateTransform():[{translateX:Animated.Value},{translateY:Animated.Value},
```

Converts `{x, y}` into a useable translation transform, e.g.
tsx
```
style={{ transform:this.state.anim.getTranslateTransform()
```

Is this page useful?
  * [Methods](https://reactnative.dev/docs/animatedvaluexy#methods)
    * [`flattenOffset()`](https://reactnative.dev/docs/animatedvaluexy#flattenoffset)
    * [`extractOffset()`](https://reactnative.dev/docs/animatedvaluexy#extractoffset)
    * [`removeListener()`](https://reactnative.dev/docs/animatedvaluexy#removelistener)
    * [`removeAllListeners()`](https://reactnative.dev/docs/animatedvaluexy#removealllisteners)
    * [`stopAnimation()`](https://reactnative.dev/docs/animatedvaluexy#stopanimation)
    * [`resetAnimation()`](https://reactnative.dev/docs/animatedvaluexy#resetanimation)
    * [`getTranslateTransform()`](https://reactnative.dev/docs/animatedvaluexy#gettranslatetransform)



