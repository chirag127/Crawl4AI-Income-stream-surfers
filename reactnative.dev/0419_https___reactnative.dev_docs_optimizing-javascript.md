---
url: https://reactnative.dev/docs/optimizing-javascript-loading
title: https://reactnative.dev/docs/optimizing-javascript-loading
date: 2025-05-10T21:41:43.308230
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/optimizing-javascript-loading#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
Parsing and running JavaScript code requires memory and time. Because of this, as your app grows, it's often useful to delay loading code until it's needed for the first time. React Native comes with some standard optimizations that are on by default, and there are techniques you can adopt in your own code to help React load your app more efficiently. There are also some advanced automatic optimizations (with their own tradeoffs) that are suitable for very large apps.
## Recommended: Use Hermes[​](https://reactnative.dev/docs/optimizing-javascript-loading#recommended-use-hermes "Direct link to Recommended: Use Hermes")
Hermes is the default engine for new React Native apps, and is highly optimized for efficient code loading. In release builds, JavaScript code is fully compiled to bytecode ahead of time. Bytecode is loaded to memory on-demand and does not need to be parsed like plain JavaScript does.
info
Read more about using Hermes in React Native [here](https://reactnative.dev/docs/hermes).
## Recommended: Lazy-load large components[​](https://reactnative.dev/docs/optimizing-javascript-loading#recommended-lazy-load-large-components "Direct link to Recommended: Lazy-load large components")
If a component with a lot of code/dependencies is not likely to be used when initially rendering your app, you can use React's [`lazy`](https://react.dev/reference/react/lazy) API to defer loading its code until it's rendered for the first time. Typically, you should consider lazy-loading screen-level components in your app, so that adding new screens to your app does not increase its startup time.
info
Read more about [lazy-loading components with Suspense ](https://react.dev/reference/react/lazy#suspense-for-code-splitting), including code examples, in React's documentation.
### Tip: Avoid module side effects[​](https://reactnative.dev/docs/optimizing-javascript-loading#tip-avoid-module-side-effects "Direct link to Tip: Avoid module side effects")
Lazy-loading components can change the behavior of your app if your component modules (or their dependencies) have _side effects_ , such as modifying global variables or subscribing to events outside of a component. Most modules in React apps should not have any side effects.
SideEffects.tsx
```
importLoggerfrom'./utils/Logger';// 🚩 🚩 🚩 Side effect! This must be executed before React can even begin to// render the SplashScreen component, and can unexpectedly break code elsewhere// in your app if you later decide to lazy-load SplashScreen.global.logger=newLogger();exportfunctionSplashScreen(){// ...
```

## Advanced: Call `require` inline[​](https://reactnative.dev/docs/optimizing-javascript-loading#advanced-call-require-inline "Direct link to advanced-call-require-inline")
Sometimes you may want to defer loading some code until you use it for the first time, without using `lazy` or an asynchronous `import()`. You can do this by using the [`require()`](https://metrobundler.dev/docs/module-api/#require) function where you would otherwise use a static `import` at the top of the file.
VeryExpensive.tsx
```
import{Component}from'react';import{Text}from'react-native';// ... import some very expensive modulesexportdefaultfunctionVeryExpensive(){// ... lots and lots of rendering logicreturn<Text>Very Expensive Component</Text>;
```

Optimized.tsx
```
import{useCallback, useState}from'react';import{TouchableOpacity,View,Text}from'react-native';// Usually we would write a static import:// import VeryExpensive from './VeryExpensive';letVeryExpensive=null;exportdefaultfunctionOptimize(){const[needsExpensive, setNeedsExpensive]=useState(false);const didPress =useCallback(()=>{if(VeryExpensive==null){VeryExpensive=require('./VeryExpensive').default;setNeedsExpensive(true);},[]);return(<Viewstyle={{marginTop:20}}><TouchableOpacityonPress={didPress}><Text>Load</Text></TouchableOpacity>{needsExpensive ?<VeryExpensive/>:null}</View>
```

## Advanced: Automatically inline `require` calls[​](https://reactnative.dev/docs/optimizing-javascript-loading#advanced-automatically-inline-require-calls "Direct link to advanced-automatically-inline-require-calls")
If you use the React Native CLI to build your app, `require` calls (but not `import`s) will automatically be inlined for you, both in your code and inside any third-party packages (`node_modules`) you use.
tsx
```
import{useCallback, useState}from'react';import{TouchableOpacity,View,Text}from'react-native';// This top-level require call will be evaluated lazily as part of the component below.constVeryExpensive=require('./VeryExpensive').default;exportdefaultfunctionOptimize(){const[needsExpensive, setNeedsExpensive]=useState(false);const didPress =useCallback(()=>{setNeedsExpensive(true);},[]);return(<Viewstyle={{marginTop:20}}><TouchableOpacityonPress={didPress}><Text>Load</Text></TouchableOpacity>{needsExpensive ?<VeryExpensive/>:null}</View>
```

info
Some React Native frameworks disable this behavior. In particular, in Expo projects, `require` calls are not inlined by default. You can enable this optimization by editing your project's Metro config and setting `inlineRequires: true` in [`getTransformOptions`](https://metrobundler.dev/docs/configuration#gettransformoptions).
### Pitfalls of inline `require`s[​](https://reactnative.dev/docs/optimizing-javascript-loading#pitfalls-of-inline-requires "Direct link to pitfalls-of-inline-requires")
Inlining `require` calls changes the order in which modules are evaluated, and can even cause some modules to _never_ be evaluated. This is usually safe to do automatically, because JavaScript modules are often written to be side-effect-free.
If one of your modules does have side effects - for example, if it initializes some logging mechanism, or patches a global API used by the rest of your code - then you might see unexpected behavior or even crashes. In those cases, you may want to exclude certain modules from this optimization, or disable it entirely.
To **disable all automatic inlining of`require` calls:**
Update your `metro.config.js` to set the `inlineRequires` transformer option to `false`:
metro.config.js
```
module.exports={ transformer:{asyncgetTransformOptions(){return{    transform:{     inlineRequires:false,
```

To only **exclude certain modules from`require` inlining:**
There are two relevant transformer options: `inlineRequires.blockList` and `nonInlinedRequires`. See the code snippet for examples of how to use each one.
metro.config.js
```
module.exports={ transformer:{asyncgetTransformOptions(){return{    transform:{     inlineRequires:{      blockList:{// require() calls in `DoNotInlineHere.js` will not be inlined.[require.resolve('./src/DoNotInlineHere.js')]:true,// require() calls anywhere else will be inlined, unless they// match any entry nonInlinedRequires (see below).     nonInlinedRequires:[// require('react') calls will not be inlined anywhere'react',
```

See the documentation for [`getTransformOptions` in Metro](https://metrobundler.dev/docs/configuration#gettransformoptions) for more details on setting up and fine-tuning your inline `require`s.
## Advanced: Use random access module bundles (non-Hermes)[​](https://reactnative.dev/docs/optimizing-javascript-loading#advanced-use-random-access-module-bundles-non-hermes "Direct link to Advanced: Use random access module bundles \(non-Hermes\)")
info
**Not supported when[using Hermes](https://reactnative.dev/docs/optimizing-javascript-loading#use-hermes).** Hermes bytecode is not compatible with the RAM bundle format, and provides the same (or better) performance in all use cases.
Random access module bundles (also known as RAM bundles) work in conjunction with the techniques mentioned above to limit the amount of JavaScript code that needs to be parsed and loaded into memory. Each module is stored as a separate string (or file) which is only parsed when the module needs to be executed.
RAM bundles may be physically split into separate files, or they may use the _indexed_ format, consisting of a lookup table of multiple modules in a single file.
  * Android
  * iOS


On Android enable the RAM format by editing your `android/app/build.gradle` file. Before the line `apply from: "../../node_modules/react-native/react.gradle"` add or amend the `project.ext.react` block:
```
project.ext.react=[ bundleCommand:"ram-bundle",
```

Use the following lines on Android if you want to use a single indexed file:
```
project.ext.react=[ bundleCommand:"ram-bundle", extraPackagerArgs:["--indexed-ram-bundle"]
```

On iOS, RAM bundles are always indexed ( = single file).
Enable the RAM format in Xcode by editing the build phase "Bundle React Native code and images". Before `../node_modules/react-native/scripts/react-native-xcode.sh` add `export BUNDLE_COMMAND="ram-bundle"`:
```
exportBUNDLE_COMMAND="ram-bundle"exportNODE_BINARY=node../node_modules/react-native/scripts/react-native-xcode.sh
```

See the documentation for [`getTransformOptions` in Metro](https://metrobundler.dev/docs/configuration#gettransformoptions) for more details on setting up and fine-tuning your RAM bundle build.
Is this page useful?
  * [Recommended: Use Hermes](https://reactnative.dev/docs/optimizing-javascript-loading#recommended-use-hermes)
  * [Recommended: Lazy-load large components](https://reactnative.dev/docs/optimizing-javascript-loading#recommended-lazy-load-large-components)
    * [Tip: Avoid module side effects](https://reactnative.dev/docs/optimizing-javascript-loading#tip-avoid-module-side-effects)
  * [Advanced: Call `require` inline](https://reactnative.dev/docs/optimizing-javascript-loading#advanced-call-require-inline)
  * [Advanced: Automatically inline `require` calls](https://reactnative.dev/docs/optimizing-javascript-loading#advanced-automatically-inline-require-calls)
    * [Pitfalls of inline `require`s](https://reactnative.dev/docs/optimizing-javascript-loading#pitfalls-of-inline-requires)
  * [Advanced: Use random access module bundles (non-Hermes)](https://reactnative.dev/docs/optimizing-javascript-loading#advanced-use-random-access-module-bundles-non-hermes)



