---
url: https://reactnative.dev/docs/layoutanimation
title: https://reactnative.dev/docs/layoutanimation
date: 2025-05-10T21:40:35.109255
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/layoutanimation#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
Automatically animates views to their new positions when the next layout happens.
A common way to use this API is to call it before updating the state hook in functional components and calling `setState` in class components.
Note that in order to get this to work on **Android** you need to set the following flags via `UIManager`:
js
```
if(Platform.OS==='android'){if(UIManager.setLayoutAnimationEnabledExperimental){UIManager.setLayoutAnimationEnabledExperimental(true);
```

## Example[​](https://reactnative.dev/docs/layoutanimation#example "Direct link to Example")
# Reference
## Methods[​](https://reactnative.dev/docs/layoutanimation#methods "Direct link to Methods")
### `configureNext()`[​](https://reactnative.dev/docs/layoutanimation#configurenext "Direct link to configurenext")
tsx
```
staticconfigureNext( config:LayoutAnimationConfig, onAnimationDidEnd?:()=>void, onAnimationDidFail?:()=>void,
```

Schedules an animation to happen on the next layout.
#### Parameters:[​](https://reactnative.dev/docs/layoutanimation#parameters "Direct link to Parameters:")
Name| Type| Required| Description  
---|---|---|---  
config| object| Yes| See config description below.  
onAnimationDidEnd| function| No| Called when the animation finished.  
onAnimationDidFail| function| No| Called when the animation failed.  
The `config` parameter is an object with the keys below. [`create`](https://reactnative.dev/docs/layoutanimation#create) returns a valid object for `config`, and the [`Presets`](https://reactnative.dev/docs/layoutanimation#presets) objects can also all be passed as the `config`.
  * `duration` in milliseconds
  * `create`, optional config for animating in new views
  * `update`, optional config for animating views that have been updated
  * `delete`, optional config for animating views as they are removed


The config that's passed to `create`, `update`, or `delete` has the following keys:
  * `type`, the [animation type](https://reactnative.dev/docs/layoutanimation#types) to use
  * `property`, the [layout property](https://reactnative.dev/docs/layoutanimation#properties) to animate (optional, but recommended for `create` and `delete`)
  * `springDamping` (number, optional and only for use with `type: Type.spring`)
  * `initialVelocity` (number, optional)
  * `delay` (number, optional)
  * `duration` (number, optional)


### `create()`[​](https://reactnative.dev/docs/layoutanimation#create "Direct link to create")
tsx
```
staticcreate(duration, type, creationProp)
```

Helper that creates an object (with `create`, `update`, and `delete` fields) to pass into [`configureNext`](https://reactnative.dev/docs/layoutanimation#configurenext). The `type` parameter is an [animation type](https://reactnative.dev/docs/layoutanimation#types), and the `creationProp` parameter is a [layout property](https://reactnative.dev/docs/layoutanimation#properties).
**Example:**
## Properties[​](https://reactnative.dev/docs/layoutanimation#properties "Direct link to Properties")
### Types[​](https://reactnative.dev/docs/layoutanimation#types "Direct link to Types")
An enumeration of animation types to be used in the [`create`](https://reactnative.dev/docs/layoutanimation#create) method, or in the `create`/`update`/`delete` configs for [`configureNext`](https://reactnative.dev/docs/layoutanimation#configurenext). (example usage: `LayoutAnimation.Types.easeIn`)
Types  
---  
spring  
linear  
easeInEaseOut  
easeIn  
easeOut  
keyboard  
### Properties[​](https://reactnative.dev/docs/layoutanimation#properties-1 "Direct link to Properties")
An enumeration of layout properties to be animated to be used in the [`create`](https://reactnative.dev/docs/layoutanimation#create) method, or in the `create`/`update`/`delete` configs for [`configureNext`](https://reactnative.dev/docs/layoutanimation#configurenext). (example usage: `LayoutAnimation.Properties.opacity`)
Properties  
---  
opacity  
scaleX  
scaleY  
scaleXY  
### Presets[​](https://reactnative.dev/docs/layoutanimation#presets "Direct link to Presets")
A set of predefined animation configs to pass into [`configureNext`](https://reactnative.dev/docs/layoutanimation#configurenext).
Presets| Value  
---|---  
easeInEaseOut| `create(300, 'easeInEaseOut', 'opacity')`  
linear| `create(500, 'linear', 'opacity')`  
spring| `{duration: 700, create: {type: 'linear', property: 'opacity'}, update: {type: 'spring', springDamping: 0.4}, delete: {type: 'linear', property: 'opacity'} }`  
### `easeInEaseOut`[​](https://reactnative.dev/docs/layoutanimation#easeineaseout "Direct link to easeineaseout")
Calls `configureNext()` with `Presets.easeInEaseOut`.
### `linear`[​](https://reactnative.dev/docs/layoutanimation#linear "Direct link to linear")
Calls `configureNext()` with `Presets.linear`.
### `spring`[​](https://reactnative.dev/docs/layoutanimation#spring "Direct link to spring")
Calls `configureNext()` with `Presets.spring`.
**Example:**
Is this page useful?
  * [Methods](https://reactnative.dev/docs/layoutanimation#methods)
    * [`configureNext()`](https://reactnative.dev/docs/layoutanimation#configurenext)
  * [Properties](https://reactnative.dev/docs/layoutanimation#properties)



