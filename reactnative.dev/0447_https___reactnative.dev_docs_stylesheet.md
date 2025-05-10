---
url: https://reactnative.dev/docs/stylesheet
title: https://reactnative.dev/docs/stylesheet
date: 2025-05-10T21:42:15.597487
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/stylesheet#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
A StyleSheet is an abstraction similar to CSS StyleSheets.
Code quality tips:
  * By moving styles away from the render function, you're making the code easier to understand.
  * Naming the styles is a good way to add meaning to the low level components in the render function, and encourage reuse.
  * In most IDEs, using `StyleSheet.create()` will offer static type checking and suggestions to help you write valid styles.


# Reference
## Methods[​](https://reactnative.dev/docs/stylesheet#methods "Direct link to Methods")
### `compose()`[​](https://reactnative.dev/docs/stylesheet#compose "Direct link to compose")
tsx
```
staticcompose(style1:Object, style2:Object):Object|Object[];
```

Combines two styles such that `style2` will override any styles in `style1`. If either style is falsy, the other one is returned without allocating an array, saving allocations and maintaining reference equality for PureComponent checks.
### `create()`[​](https://reactnative.dev/docs/stylesheet#create "Direct link to create")
tsx
```
staticcreate(styles:ObjectextendsRecord<string, ViewStyle | ImageStyle | TextStyle>):Object;
```

An identity function for creating styles. The main practical benefit of creating styles inside `StyleSheet.create()` is static type checking against native style properties.
### `flatten()`[​](https://reactnative.dev/docs/stylesheet#flatten "Direct link to flatten")
tsx
```
staticflatten(style:Array<ObjectextendsRecord<string, ViewStyle | ImageStyle | TextStyle>>):Object;
```

Flattens an array of style objects, into one aggregated style object.
### `setStyleAttributePreprocessor()`[​](https://reactnative.dev/docs/stylesheet#setstyleattributepreprocessor "Direct link to setstyleattributepreprocessor")
> **WARNING: EXPERIMENTAL.** Breaking changes will probably happen a lot and will not be reliably announced. The whole thing might be deleted, who knows? Use at your own risk.
tsx
```
staticsetStyleAttributePreprocessor( property:string,process:(propValue:any)=>any,
```

Sets a function to use to pre-process a style property value. This is used internally to process color and transform values. You should not use this unless you really know what you are doing and have exhausted other options.
## Properties[​](https://reactnative.dev/docs/stylesheet#properties "Direct link to Properties")
### `absoluteFill`[​](https://reactnative.dev/docs/stylesheet#absolutefill "Direct link to absolutefill")
A very common pattern is to create overlays with position absolute and zero positioning (`position: 'absolute', left: 0, right: 0, top: 0, bottom: 0`), so `absoluteFill` can be used for convenience and to reduce duplication of these repeated styles. If you want, absoluteFill can be used to create a customized entry in a StyleSheet, e.g.:
### `absoluteFillObject`[​](https://reactnative.dev/docs/stylesheet#absolutefillobject "Direct link to absolutefillobject")
Sometimes you may want `absoluteFill` but with a couple tweaks - `absoluteFillObject` can be used to create a customized entry in a `StyleSheet`, e.g.:
### `hairlineWidth`[​](https://reactnative.dev/docs/stylesheet#hairlinewidth "Direct link to hairlinewidth")
This is defined as the width of a thin line on the platform. It can be used as the thickness of a border or division between two elements. Example:
This constant will always be a round number of pixels (so a line defined by it can look crisp) and will try to match the standard width of a thin line on the underlying platform. However, you should not rely on it being a constant size, because on different platforms and screen densities its value may be calculated differently.
A line with hairline width may not be visible if your simulator is downscaled.
Is this page useful?
  * [Methods](https://reactnative.dev/docs/stylesheet#methods)
    * [`setStyleAttributePreprocessor()`](https://reactnative.dev/docs/stylesheet#setstyleattributepreprocessor)
  * [Properties](https://reactnative.dev/docs/stylesheet#properties)
    * [`absoluteFillObject`](https://reactnative.dev/docs/stylesheet#absolutefillobject)



