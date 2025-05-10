---
url: https://reactnative.dev/docs/animatedvalue
title: https://reactnative.dev/docs/animatedvalue
date: 2025-05-10T21:39:24.636167
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/animatedvalue#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
Standard value for driving animations. One `Animated.Value` can drive multiple properties in a synchronized fashion, but can only be driven by one mechanism at a time. Using a new mechanism (e.g. starting a new animation, or calling `setValue`) will stop any previous ones.
Typically initialized with `useAnimatedValue(0);` or `new Animated.Value(0);` in class components.
# Reference
## Methods[​](https://reactnative.dev/docs/animatedvalue#methods "Direct link to Methods")
### `setValue()`[​](https://reactnative.dev/docs/animatedvalue#setvalue "Direct link to setvalue")
tsx
```
setValue(value:number);
```

Directly set the value. This will stop any animations running on the value and update all the bound properties.
**Parameters:**
Name| Type| Required| Description  
---|---|---|---  
value| number| Yes| Value  
### `setOffset()`[​](https://reactnative.dev/docs/animatedvalue#setoffset "Direct link to setoffset")
tsx
```
setOffset(offset:number);
```

Sets an offset that is applied on top of whatever value is set, whether via `setValue`, an animation, or `Animated.event`. Useful for compensating things like the start of a pan gesture.
**Parameters:**
Name| Type| Required| Description  
---|---|---|---  
offset| number| Yes| Offset value  
### `flattenOffset()`[​](https://reactnative.dev/docs/animatedvalue#flattenoffset "Direct link to flattenoffset")
tsx
```
flattenOffset();
```

Merges the offset value into the base value and resets the offset to zero. The final output of the value is unchanged.
### `extractOffset()`[​](https://reactnative.dev/docs/animatedvalue#extractoffset "Direct link to extractoffset")
tsx
```
extractOffset();
```

Sets the offset value to the base value, and resets the base value to zero. The final output of the value is unchanged.
### `addListener()`[​](https://reactnative.dev/docs/animatedvalue#addlistener "Direct link to addlistener")
tsx
```
addListener(callback:(state:{value:number})=>void):string;
```

Adds an asynchronous listener to the value so you can observe updates from animations. This is useful because there is no way to synchronously read the value because it might be driven natively.
Returns a string that serves as an identifier for the listener.
**Parameters:**
Name| Type| Required| Description  
---|---|---|---  
callback| function| Yes| The callback function which will receive an object with a `value` key set to the new value.  
### `removeListener()`[​](https://reactnative.dev/docs/animatedvalue#removelistener "Direct link to removelistener")
tsx
```
removeListener(id:string);
```

Unregister a listener. The `id` param shall match the identifier previously returned by `addListener()`.
**Parameters:**
Name| Type| Required| Description  
---|---|---|---  
id| string| Yes| Id for the listener being removed.  
### `removeAllListeners()`[​](https://reactnative.dev/docs/animatedvalue#removealllisteners "Direct link to removealllisteners")
tsx
```
removeAllListeners();
```

Remove all registered listeners.
### `stopAnimation()`[​](https://reactnative.dev/docs/animatedvalue#stopanimation "Direct link to stopanimation")
tsx
```
stopAnimation(callback?:(value:number)=>void);
```

Stops any running animation or tracking. `callback` is invoked with the final value after stopping the animation, which is useful for updating state to match the animation position with layout.
**Parameters:**
Name| Type| Required| Description  
---|---|---|---  
callback| function| No| A function that will receive the final value.  
### `resetAnimation()`[​](https://reactnative.dev/docs/animatedvalue#resetanimation "Direct link to resetanimation")
tsx
```
resetAnimation(callback?:(value:number)=>void);
```

Stops any animation and resets the value to its original.
**Parameters:**
Name| Type| Required| Description  
---|---|---|---  
callback| function| No| A function that will receive the original value.  
### `interpolate()`[​](https://reactnative.dev/docs/animatedvalue#interpolate "Direct link to interpolate")
tsx
```
interpolate(config:InterpolationConfigType);
```

Interpolates the value before updating the property, e.g. mapping 0-1 to 0-10.
See `AnimatedInterpolation.js`
**Parameters:**
Name| Type| Required| Description  
---|---|---|---  
config| object| Yes| See below.  
The `config` object is composed of the following keys:
  * `inputRange`: an array of numbers
  * `outputRange`: an array of numbers or strings
  * `easing` (optional): a function that returns a number, given an input number
  * `extrapolate` (optional): a string such as 'extend', 'identity', or 'clamp'
  * `extrapolateLeft` (optional): a string such as 'extend', 'identity', or 'clamp'
  * `extrapolateRight` (optional): a string such as 'extend', 'identity', or 'clamp'


### `animate()`[​](https://reactnative.dev/docs/animatedvalue#animate "Direct link to animate")
tsx
```
animate(animation, callback);
```

Typically only used internally, but could be used by a custom Animation class.
**Parameters:**
Name| Type| Required| Description  
---|---|---|---  
animation| Animation| Yes| See `Animation.js`.  
callback| function| Yes| Callback function.  
Is this page useful?
  * [Methods](https://reactnative.dev/docs/animatedvalue#methods)
    * [`flattenOffset()`](https://reactnative.dev/docs/animatedvalue#flattenoffset)
    * [`extractOffset()`](https://reactnative.dev/docs/animatedvalue#extractoffset)
    * [`removeListener()`](https://reactnative.dev/docs/animatedvalue#removelistener)
    * [`removeAllListeners()`](https://reactnative.dev/docs/animatedvalue#removealllisteners)
    * [`stopAnimation()`](https://reactnative.dev/docs/animatedvalue#stopanimation)
    * [`resetAnimation()`](https://reactnative.dev/docs/animatedvalue#resetanimation)



