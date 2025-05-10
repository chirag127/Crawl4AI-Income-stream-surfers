---
url: https://reactnative.dev/docs/0.72/javascript-environment
title: https://reactnative.dev/docs/0.72/javascript-environment
date: 2025-05-10T21:37:05.443883
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/0.72/javascript-environment#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
This is documentation for React Native **0.72** , which is no longer in active development.
For up-to-date documentation, see the (0.79).
Version: 0.72
On this page
## JavaScript Runtime[​](https://reactnative.dev/docs/0.72/javascript-environment#javascript-runtime "Direct link to JavaScript Runtime")
When using React Native, you're going to be running your JavaScript code in up to three environments:
  * In most cases, React Native will use [Hermes](https://reactnative.dev/docs/0.72/hermes), an open-source JavaScript engine optimized for React Native.
  * If Hermes is disabled, React Native will use [JavaScriptCore](http://trac.webkit.org/wiki/JavaScriptCore), the JavaScript engine that powers Safari. Note that on iOS, JavaScriptCore does not use JIT due to the absence of writable executable memory in iOS apps.
  * When using Chrome debugging, all JavaScript code runs within Chrome itself, communicating with native code via WebSockets. Chrome uses [V8](https://v8.dev/) as its JavaScript engine.


While these environments are very similar, you may end up hitting some inconsistencies. It is best to avoid relying on specifics of any runtime.
## JavaScript Syntax Transformers[​](https://reactnative.dev/docs/0.72/javascript-environment#javascript-syntax-transformers "Direct link to JavaScript Syntax Transformers")
Syntax transformers make writing code more enjoyable by allowing you to use new JavaScript syntax without having to wait for support on all interpreters.
React Native ships with the [Babel JavaScript compiler](https://babeljs.io). Check [Babel documentation](https://babeljs.io/docs/plugins/#transform-plugins) on its supported transformations for more details.
A full list of React Native's enabled transformations can be found in [@react-native/babel-preset](https://github.com/facebook/react-native/tree/main/packages/react-native-babel-preset).
Transformation| Code  
---|---  
ECMAScript 5  
Reserved Words| ```
promise.catch(function(){...});
```
  
ECMAScript 2015 (ES6)  
```
<ConPress={()=>this.setState({pressed:true})}/>
```
  
```
let greeting ='hi';
```
  
```
Math.max(...array);
```
  
```
classCextendsReact.Component{render(){return<View/>;}}
```
  
```
const key ='abc';const obj ={[key]:10};
```
  
```
const answer =42;
```
  
```
const{isActive, style}=this.props;
```
  
```
for(var num of[1,2,3]){...};
```
  
```
letnumber= x => x;
```
  
```
const b =0b11;const o =0o7;const u ='Hello\u{000A}\u{0009}!';
```
  
```
importReact,{Component}from'react';
```
  
[Object Concise Method](http://babeljs.io/docs/learn-es2015/#enhanced-object-literals)| ```
const obj ={method(){return10;}};
```
  
[Object Short Notation](http://babeljs.io/docs/learn-es2015/#enhanced-object-literals)| ```
const name ='vjeux';const obj ={name};
```
  
```
functiontest(x ='hello',{a, b},...args){}
```
  
```
function(type,...args){};
```
  
[Shorthand Properties](https://babeljs.io/docs/en/babel-plugin-transform-shorthand-properties)| ```
const o ={a, b, c};
```
  
```
const a =/o+/y;
```
  
```
const who ='world';const str =`Hello ${who}`;
```
  
```
conststring='foo💩bar';const match =string.match(/foo(.)bar/u);
```
  
ECMAScript 2016 (ES7)  
[Exponentiation Operator](https://babeljs.io/docs/en/babel-plugin-transform-exponentiation-operator)| ```
let x =10**2;
```
  
ECMAScript 2017 (ES8)  
```
asyncfunctiondoStuffAsync(){const foo =awaitdoOtherStuffAsync();};
```
  
[Function Trailing Comma](https://github.com/jeffmo/es-trailing-function-commas)| ```
functionf(a, b, c,){};
```
  
ECMAScript 2018 (ES9)  
```
const extended ={...obj, a:10};
```
  
ECMAScript 2019 (ES10)  
[Optional Catch Binding](https://babeljs.io/docs/en/babel-plugin-proposal-optional-catch-binding)| ```
try{throw0;}catch{doSomethingWhichDoesNotCareAboutTheValueThrown();}
```
  
ECMAScript 2020 (ES11)  
```
constpackage=awaitimport('package');package.function()
```
  
[Nullish Coalescing Operator](https://babeljs.io/docs/en/babel-plugin-proposal-nullish-coalescing-operator)| ```
const foo = object.foo??'default';
```
  
```
const name = obj.user?.name;
```
  
ECMAScript 2022 (ES13)  
```
classBork{static a ='foo';static b; x ='bar'; y;}
```
  
Stage 1 Proposal  
```
export v from'mod';
```
  
Miscellaneous  
```
template(`const %%importName%% = require(%%source%%);`);
```
  
```
functionfoo(x:?number):string{};
```
  
```
exportdefault42;
```
  
```
<Viewstyle={{color:'red'}}/>
```
  
```
Object.assign(a, b);
```
  
```
const bar =createReactClass({});
```
  
```
functionfoo(x:{hello:true, target:'react native!'}):string{};
```
  
## Polyfills[​](https://reactnative.dev/docs/0.72/javascript-environment#polyfills "Direct link to Polyfills")
Many standard functions are also available on all the supported JavaScript runtimes.
#### Browser[​](https://reactnative.dev/docs/0.72/javascript-environment#browser "Direct link to Browser")
  * [CommonJS `require`](https://nodejs.org/docs/latest/api/modules.html)
  * `console.{log, warn, error, info, debug, trace, table, group, groupCollapsed, groupEnd}[](https://developer.chrome.com/devtools/docs/console-api)`
  * [`XMLHttpRequest`, `fetch`](https://reactnative.dev/docs/0.72/network#content)
  * [`{set, clear}{Timeout, Interval, Immediate}, {request, cancel}AnimationFrame`](https://reactnative.dev/docs/0.72/timers#content)


#### ECMAScript 2015 (ES6)[​](https://reactnative.dev/docs/0.72/javascript-environment#ecmascript-2015-es6 "Direct link to ECMAScript 2015 \(ES6\)")
  * `Array.prototype.{find[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find), findIndex[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findIndex)}`
  * `String.prototype.{startsWith[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/startsWith), endsWith[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/endsWith), repeat[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/repeat), includes[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/includes)}`


#### ECMAScript 2016 (ES7)[​](https://reactnative.dev/docs/0.72/javascript-environment#ecmascript-2016-es7 "Direct link to ECMAScript 2016 \(ES7\)")
  * `Array.prototype.includes[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes)`


#### ECMAScript 2017 (ES8)[​](https://reactnative.dev/docs/0.72/javascript-environment#ecmascript-2017-es8 "Direct link to ECMAScript 2017 \(ES8\)")
  * `Object.{entries[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries), values[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/values)}`


#### Specific[​](https://reactnative.dev/docs/0.72/javascript-environment#specific "Direct link to Specific")
  * `__DEV__`


Is this page useful?
  * [JavaScript Runtime](https://reactnative.dev/docs/0.72/javascript-environment#javascript-runtime)
  * [JavaScript Syntax Transformers](https://reactnative.dev/docs/0.72/javascript-environment#javascript-syntax-transformers)



