---
url: https://reactnative.dev/docs/legacy/native-modules-android
title: https://reactnative.dev/docs/legacy/native-modules-android
date: 2025-05-10T21:40:25.792367
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/legacy/native-modules-android#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
info
Native Module and Native Components are our stable technologies used by the legacy architecture. They will be deprecated in the future when the New Architecture will be stable. The New Architecture uses [Turbo Native Module](https://github.com/reactwg/react-native-new-architecture/blob/main/docs/turbo-modules.md) and [Fabric Native Components](https://github.com/reactwg/react-native-new-architecture/blob/main/docs/fabric-native-components.md) to achieve similar results.
Welcome to Native Modules for Android. Please start by reading the [Native Modules Intro](https://reactnative.dev/docs/legacy/native-modules-intro) for an intro to what native modules are.
## Create a Calendar Native Module[​](https://reactnative.dev/docs/legacy/native-modules-android#create-a-calendar-native-module "Direct link to Create a Calendar Native Module")
In the following guide you will create a native module, `CalendarModule`, that will allow you to access Android’s calendar APIs from JavaScript. By the end, you will be able to call `CalendarModule.createCalendarEvent('Dinner Party', 'My House');` from JavaScript, invoking a Java/Kotlin method that creates a calendar event.
### Setup[​](https://reactnative.dev/docs/legacy/native-modules-android#setup "Direct link to Setup")
To get started, open up the Android project within your React Native application in Android Studio. You can find your Android project here within a React Native app:
Image of where you can find your Android project
We recommend using Android Studio to write your native code. Android studio is an IDE built for Android development and using it will help you resolve minor issues like code syntax errors quickly.
We also recommend enabling [Gradle Daemon](https://docs.gradle.org/2.9/userguide/gradle_daemon.html) to speed up builds as you iterate on Java/Kotlin code.
### Create A Custom Native Module File[​](https://reactnative.dev/docs/legacy/native-modules-android#create-a-custom-native-module-file "Direct link to Create A Custom Native Module File")
The first step is to create the (`CalendarModule.java` or `CalendarModule.kt`) Java/Kotlin file inside `android/app/src/main/java/com/your-app-name/` folder (the folder is the same for both Kotlin and Java). This Java/Kotlin file will contain your native module Java/Kotlin class.
Image of how to add the CalendarModuleClass
Then add the following content:
  * Java
  * Kotlin


java
```
packagecom.your-apps-package-name;// replace your-apps-package-name with your app’s package nameimportcom.facebook.react.bridge.NativeModule;importcom.facebook.react.bridge.ReactApplicationContext;importcom.facebook.react.bridge.ReactContext;importcom.facebook.react.bridge.ReactContextBaseJavaModule;importcom.facebook.react.bridge.ReactMethod;importjava.util.Map;importjava.util.HashMap;publicclassCalendarModuleextendsReactContextBaseJavaModule{CalendarModule(ReactApplicationContext context){super(context);
```

kotlin
```
package com.your-apps-package-name;// replace your-apps-package-name with your app’s package nameimport com.facebook.react.bridge.NativeModuleimport com.facebook.react.bridge.ReactApplicationContextimport com.facebook.react.bridge.ReactContextimport com.facebook.react.bridge.ReactContextBaseJavaModuleimport com.facebook.react.bridge.ReactMethodclassCalendarModule(reactContext: ReactApplicationContext):ReactContextBaseJavaModule(reactContext){...}
```

As you can see, your `CalendarModule` class extends the `ReactContextBaseJavaModule` class. For Android, Java/Kotlin native modules are written as classes that extend `ReactContextBaseJavaModule` and implement the functionality required by JavaScript.
> It is worth noting that technically Java/Kotlin classes only need to extend the `BaseJavaModule` class or implement the `NativeModule` interface to be considered a Native Module by React Native.
> However we recommend that you use `ReactContextBaseJavaModule`, as shown above. `ReactContextBaseJavaModule` gives access to the `ReactApplicationContext` (RAC), which is useful for Native Modules that need to hook into activity lifecycle methods. Using `ReactContextBaseJavaModule` will also make it easier to make your native module type-safe in the future. For native module type-safety, which is coming in future releases, React Native looks at each native module's JavaScript spec and generates an abstract base class that extends `ReactContextBaseJavaModule`.
### Module Name[​](https://reactnative.dev/docs/legacy/native-modules-android#module-name "Direct link to Module Name")
All Java/Kotlin native modules in Android need to implement the `getName()` method. This method returns a string, which represents the name of the native module. The native module can then be accessed in JavaScript using its name. For example, in the below code snippet, `getName()` returns `"CalendarModule"`.
  * Java
  * Kotlin


java
```
// add to CalendarModule.java@OverridepublicStringgetName(){return"CalendarModule";
```

kotlin
```
// add to CalendarModule.ktoverridefungetName()="CalendarModule"
```

The native module can then be accessed in JS like this:
tsx
```
const{CalendarModule}=ReactNative.NativeModules;
```

### Export a Native Method to JavaScript[​](https://reactnative.dev/docs/legacy/native-modules-android#export-a-native-method-to-javascript "Direct link to Export a Native Method to JavaScript")
Next you will need to add a method to your native module that will create calendar events and can be invoked in JavaScript. All native module methods meant to be invoked from JavaScript must be annotated with `@ReactMethod`.
Set up a method `createCalendarEvent()` for `CalendarModule` that can be invoked in JS through `CalendarModule.createCalendarEvent()`. For now, the method will take in a name and location as strings. Argument type options will be covered shortly.
  * Java
  * Kotlin


java
```
@ReactMethodpublicvoidcreateCalendarEvent(String name,String location){
```

kotlin
```
@ReactMethodfuncreateCalendarEvent(name: String, location: String){}
```

Add a debug log in the method to confirm it has been invoked when you call it from your application. Below is an example of how you can import and use the [Log](https://developer.android.com/reference/android/util/Log) class from the Android util package:
  * Java
  * Kotlin


java
```
importandroid.util.Log;@ReactMethodpublicvoidcreateCalendarEvent(String name,String location){Log.d("CalendarModule","Create event called with name: "+ name+" and location: "+ location);
```

kotlin
```
import android.util.Log@ReactMethodfuncreateCalendarEvent(name: String, location: String){  Log.d("CalendarModule","Create event called with name: $name and location: $location")
```

Once you finish implementing the native module and hook it up in JavaScript, you can follow [these steps](https://developer.android.com/studio/debug/am-logcat.html) to view the logs from your app.
### Synchronous Methods[​](https://reactnative.dev/docs/legacy/native-modules-android#synchronous-methods "Direct link to Synchronous Methods")
You can pass `isBlockingSynchronousMethod = true` to a native method to mark it as a synchronous method.
  * Java
  * Kotlin


java
```
@ReactMethod(isBlockingSynchronousMethod =true)
```

kotlin
```
@ReactMethod(isBlockingSynchronousMethod =true)
```

At the moment, we do not recommend this, since calling methods synchronously can have strong performance penalties and introduce threading-related bugs to your native modules. Additionally, please note that if you choose to enable `isBlockingSynchronousMethod`, your app can no longer use the Google Chrome debugger. This is because synchronous methods require the JS VM to share memory with the app. For the Google Chrome debugger, React Native runs inside the JS VM in Google Chrome, and communicates asynchronously with the mobile devices via WebSockets.
### Register the Module (Android Specific)[​](https://reactnative.dev/docs/legacy/native-modules-android#register-the-module-android-specific "Direct link to Register the Module \(Android Specific\)")
Once a native module is written, it needs to be registered with React Native. In order to do so, you need to add your native module to a `ReactPackage` and register the `ReactPackage` with React Native. During initialization, React Native will loop over all packages, and for each `ReactPackage`, register each native module within.
React Native invokes the method `createNativeModules()` on a `ReactPackage` in order to get the list of native modules to register. For Android, if a module is not instantiated and returned in createNativeModules it will not be available from JavaScript.
To add your Native Module to `ReactPackage`, first create a new Java/Kotlin Class named (`MyAppPackage.java` or `MyAppPackage.kt`) that implements `ReactPackage` inside the `android/app/src/main/java/com/your-app-name/` folder:
Then add the following content:
  * Java
  * Kotlin


java
```
packagecom.your-app-name;// replace your-app-name with your app’s nameimportcom.facebook.react.ReactPackage;importcom.facebook.react.bridge.NativeModule;importcom.facebook.react.bridge.ReactApplicationContext;importcom.facebook.react.uimanager.ViewManager;importjava.util.ArrayList;importjava.util.Collections;importjava.util.List;publicclassMyAppPackageimplementsReactPackage{@OverridepublicList<ViewManager>createViewManagers(ReactApplicationContext reactContext){returnCollections.emptyList();@OverridepublicList<NativeModule>createNativeModules(ReactApplicationContext reactContext){List<NativeModule> modules =newArrayList<>();    modules.add(newCalendarModule(reactContext));return modules;
```

kotlin
```
package com.your-app-name // replace your-app-name with your app’s nameimport android.view.Viewimport com.facebook.react.ReactPackageimport com.facebook.react.bridge.NativeModuleimport com.facebook.react.bridge.ReactApplicationContextimport com.facebook.react.uimanager.ReactShadowNodeimport com.facebook.react.uimanager.ViewManagerclass MyAppPackage : ReactPackage {overridefuncreateViewManagers(    reactContext: ReactApplicationContext): MutableList<ViewManager<View, ReactShadowNode<*>>>=mutableListOf()overridefuncreateNativeModules(    reactContext: ReactApplicationContext): MutableList<NativeModule>=listOf(CalendarModule(reactContext)).toMutableList()
```

This file imports the native module you created, `CalendarModule`. It then instantiates `CalendarModule` within the `createNativeModules()` function and returns it as a list of `NativeModules` to register. If you add more native modules down the line, you can also instantiate them and add them to the list returned here.
> It is worth noting that this way of registering native modules eagerly initializes all native modules when the application starts, which adds to the startup time of an application. You can use [TurboReactPackage](https://github.com/facebook/react-native/blob/main/packages/react-native/ReactAndroid/src/main/java/com/facebook/react/TurboReactPackage.java) as an alternative. Instead of `createNativeModules`, which return a list of instantiated native module objects, TurboReactPackage implements a `getModule(String name, ReactApplicationContext rac)` method that creates the native module object, when required. TurboReactPackage is a bit more complicated to implement at the moment. In addition to implementing a `getModule()` method, you have to implement a `getReactModuleInfoProvider()` method, which returns a list of all the native modules the package can instantiate along with a function that instantiates them, example [here](https://github.com/facebook/react-native/blob/8ac467c51b94c82d81930b4802b2978c85539925/ReactAndroid/src/main/java/com/facebook/react/CoreModulesPackage.java#L86-L165). Again, using TurboReactPackage will allow your application to have a faster startup time, but it is currently a bit cumbersome to write. So proceed with caution if you choose to use TurboReactPackages.
To register the `CalendarModule` package, you must add `MyAppPackage` to the list of packages returned in ReactNativeHost's `getPackages()` method. Open up your `MainApplication.java` or `MainApplication.kt` file, which can be found in the following path: `android/app/src/main/java/com/your-app-name/`.
Locate ReactNativeHost’s `getPackages()` method and add your package to the packages list `getPackages()` returns:
  * Java
  * Kotlin


java
```
@OverrideprotectedList<ReactPackage>getPackages(){List<ReactPackage> packages =newPackageList(this).getPackages();// Packages that cannot be autolinked yet can be added manually here, for example:// packages.add(new MyReactNativePackage());  packages.add(newMyAppPackage());return packages;
```

kotlin
```
overridefungetPackages(): List<ReactPackage>=PackageList(this).packages.apply{// Packages that cannot be autolinked yet can be added manually here, for example:// add(MyReactNativePackage())add(MyAppPackage())
```

You have now successfully registered your native module for Android!
### Test What You Have Built[​](https://reactnative.dev/docs/legacy/native-modules-android#test-what-you-have-built "Direct link to Test What You Have Built")
At this point, you have set up the basic scaffolding for your native module in Android. Test that out by accessing the native module and invoking its exported method in JavaScript.
Find a place in your application where you would like to add a call to the native module’s `createCalendarEvent()` method. Below is an example of a component, `NewModuleButton` you can add in your app. You can invoke the native module inside `NewModuleButton`'s `onPress()` function.
tsx
```
importReactfrom'react';import{NativeModules,Button}from'react-native';constNewModuleButton=()=>{constonPress=()=>{console.log('We will invoke the native module here!');return(<Buttontitle="Click to invoke your native module!"color="#841584"onPress={onPress}/>exportdefaultNewModuleButton;
```

In order to access your native module from JavaScript you need to first import `NativeModules` from React Native:
tsx
```
import{NativeModules}from'react-native';
```

You can then access the `CalendarModule` native module off of `NativeModules`.
tsx
```
const{CalendarModule}=NativeModules;
```

Now that you have the CalendarModule native module available, you can invoke your native method `createCalendarEvent()`. Below it is added to the `onPress()` method in `NewModuleButton`:
tsx
```
constonPress=()=>{CalendarModule.createCalendarEvent('testName','testLocation');
```

The final step is to rebuild the React Native app so that you can have the latest native code (with your new native module!) available. In your command line, where the react native application is located, run the following:
  * npm
  * Yarn


shell
```
npm run android
```

shell
```
yarn android
```

### Building as You Iterate[​](https://reactnative.dev/docs/legacy/native-modules-android#building-as-you-iterate "Direct link to Building as You Iterate")
As you work through these guides and iterate on your native module, you will need to do a native rebuild of your application to access your most recent changes from JavaScript. This is because the code that you are writing sits within the native part of your application. While React Native’s metro bundler can watch for changes in JavaScript and rebuild on the fly for you, it will not do so for native code. So if you want to test your latest native changes you need to rebuild by using the above command.
### Recap✨[​](https://reactnative.dev/docs/legacy/native-modules-android#recap "Direct link to Recap✨")
You should now be able to invoke your `createCalendarEvent()` method on your native module in the app. In our example this occurs by pressing the `NewModuleButton`. You can confirm this by viewing the log you set up in your `createCalendarEvent()` method. You can follow [these steps](https://developer.android.com/studio/debug/am-logcat.html) to view ADB logs in your app. You should then be able to search for your `Log.d` message (in our example “Create event called with name: testName and location: testLocation”) and see your message logged each time you invoke your native module method.
Image of ADB logs in Android Studio
At this point you have created an Android native module and invoked its native method from JavaScript in your React Native application. You can read on to learn more about things like argument types available to a native module method and how to setup callbacks and promises.
## Beyond a Calendar Native Module[​](https://reactnative.dev/docs/legacy/native-modules-android#beyond-a-calendar-native-module "Direct link to Beyond a Calendar Native Module")
### Better Native Module Export[​](https://reactnative.dev/docs/legacy/native-modules-android#better-native-module-export "Direct link to Better Native Module Export")
Importing your native module by pulling it off of `NativeModules` like above is a bit clunky.
To save consumers of your native module from needing to do that each time they want to access your native module, you can create a JavaScript wrapper for the module. Create a new JavaScript file named `CalendarModule.js` with the following content:
tsx
```
/*** This exposes the native CalendarModule module as a JS module. This has a* function 'createCalendarEvent' which takes the following parameters:* 1. String name: A string representing the name of the event* 2. String location: A string representing the location of the event*/import{NativeModules}from'react-native';const{CalendarModule}=NativeModules;exportdefaultCalendarModule;
```

This JavaScript file also becomes a good location for you to add any JavaScript side functionality. For example, if you use a type system like TypeScript you can add type annotations for your native module here. While React Native does not yet support Native to JS type safety, all your JS code will be type safe. Doing so will also make it easier for you to switch to type-safe native modules down the line. Below is an example of adding type safety to the CalendarModule:
tsx
```
/** * This exposes the native CalendarModule module as a JS module. This has a * function 'createCalendarEvent' which takes the following parameters: * 1. String name: A string representing the name of the event * 2. String location: A string representing the location of the event */import{NativeModules}from'react-native';const{CalendarModule}=NativeModules;interfaceCalendarInterface{createCalendarEvent(name:string,location:string):void;exportdefaultCalendarModuleasCalendarInterface;
```

In your other JavaScript files you can access the native module and invoke its method like this:
tsx
```
importCalendarModulefrom'./CalendarModule';CalendarModule.createCalendarEvent('foo','bar');
```

> This assumes that the place you are importing `CalendarModule` is in the same hierarchy as `CalendarModule.js`. Please update the relative import as necessary.
### Argument Types[​](https://reactnative.dev/docs/legacy/native-modules-android#argument-types "Direct link to Argument Types")
When a native module method is invoked in JavaScript, React Native converts the arguments from JS objects to their Java/Kotlin object analogues. So for example, if your Java Native Module method accepts a double, in JS you need to call the method with a number. React Native will handle the conversion for you. Below is a list of the argument types supported for native module methods and the JavaScript equivalents they map to.
Java| Kotlin| JavaScript  
---|---|---  
Boolean| Boolean| ?boolean  
boolean| boolean  
Double| Double| ?number  
double| number  
String| String| string  
Callback| Callback| Function  
Promise| Promise| Promise  
ReadableMap| ReadableMap| Object  
ReadableArray| ReadableArray| Array  
> The following types are currently supported but will not be supported in TurboModules. Please avoid using them:
>   * Integer Java/Kotlin -> ?number
>   * Float Java/Kotlin -> ?number
>   * int Java -> number
>   * float Java -> number
> 

For argument types not listed above, you will need to handle the conversion yourself. For example, in Android, `Date` conversion is not supported out of the box. You can handle the conversion to the `Date` type within the native method yourself like so:
  * Java
  * Kotlin


java
```
String dateFormat ="yyyy-MM-dd";SimpleDateFormat sdf =newSimpleDateFormat(dateFormat);Calendar eStartDate =Calendar.getInstance();try{    eStartDate.setTime(sdf.parse(startDate));
```

kotlin
```
val dateFormat ="yyyy-MM-dd"val sdf =SimpleDateFormat(dateFormat, Locale.US)val eStartDate = Calendar.getInstance()try{    sdf.parse(startDate)?.let{      eStartDate.time = it
```

### Exporting Constants[​](https://reactnative.dev/docs/legacy/native-modules-android#exporting-constants "Direct link to Exporting Constants")
A native module can export constants by implementing the native method `getConstants()`, which is available in JS. Below you will implement `getConstants()` and return a Map that contains a `DEFAULT_EVENT_NAME` constant you can access in JavaScript:
  * Java
  * Kotlin


java
```
@OverridepublicMap<String,Object>getConstants(){finalMap<String,Object> constants =newHashMap<>();  constants.put("DEFAULT_EVENT_NAME","New Event");return constants;
```

kotlin
```
overridefungetConstants(): MutableMap<String, Any>=hashMapOf("DEFAULT_EVENT_NAME"to"New Event")
```

The constant can then be accessed by invoking `getConstants` on the native module in JS:
tsx
```
const{DEFAULT_EVENT_NAME}=CalendarModule.getConstants();console.log(DEFAULT_EVENT_NAME);
```

Technically it is possible to access constants exported in `getConstants()` directly off the native module object. This will no longer be supported with TurboModules, so we encourage the community to switch to the above approach to avoid necessary migration down the line.
> That currently constants are exported only at initialization time, so if you change getConstants values at runtime it won't affect the JavaScript environment. This will change with Turbomodules. With Turbomodules, `getConstants()` will become a regular native module method, and each invocation will hit the native side.
### Callbacks[​](https://reactnative.dev/docs/legacy/native-modules-android#callbacks "Direct link to Callbacks")
Native modules also support a unique kind of argument: a callback. Callbacks are used to pass data from Java/Kotlin to JavaScript for asynchronous methods. They can also be used to asynchronously execute JavaScript from the native side.
In order to create a native module method with a callback, first import the `Callback` interface, and then add a new parameter to your native module method of type `Callback`. There are a couple of nuances with callback arguments that will soon be lifted with TurboModules. First off, you can only have two callbacks in your function arguments- a successCallback and a failureCallback. In addition, the last argument to a native module method call, if it's a function, is treated as the successCallback, and the second to last argument to a native module method call, if it's a function, is treated as the failure callback.
  * Java
  * Kotlin


java
```
importcom.facebook.react.bridge.Callback;@ReactMethodpublicvoidcreateCalendarEvent(String name,String location,Callback callBack){
```

kotlin
```
import com.facebook.react.bridge.Callback@ReactMethodfuncreateCalendarEvent(name: String, location: String, callback: Callback){}
```

You can invoke the callback in your Java/Kotlin method, providing whatever data you want to pass to JavaScript. Please note that you can only pass serializable data from native code to JavaScript. If you need to pass back a native object you can use `WriteableMaps`, if you need to use a collection use `WritableArrays`. It is also important to highlight that the callback is not invoked immediately after the native function completes. Below the ID of an event created in an earlier call is passed to the callback.
  * Java
  * Kotlin


java
```
@ReactMethodpublicvoidcreateCalendarEvent(String name,String location,Callback callBack){Integer eventId =...    callBack.invoke(eventId);
```

kotlin
```
@ReactMethodfuncreateCalendarEvent(name: String, location: String, callback: Callback){val eventId =...   callback.invoke(eventId)
```

This method could then be accessed in JavaScript using:
tsx
```
constonPress=()=>{CalendarModule.createCalendarEvent('Party','My House',  eventId =>{console.log(`Created a new event with id ${eventId}`);
```

Another important detail to note is that a native module method can only invoke one callback, one time. This means that you can either call a success callback or a failure callback, but not both, and each callback can only be invoked at most one time. A native module can, however, store the callback and invoke it later.
There are two approaches to error handling with callbacks. The first is to follow Node’s convention and treat the first argument passed to the callback as an error object.
  * Java
  * Kotlin


java
```
@ReactMethodpublicvoidcreateCalendarEvent(String name,String location,Callback callBack){Integer eventId =...    callBack.invoke(null, eventId);
```

kotlin
```
@ReactMethodfuncreateCalendarEvent(name: String, location: String, callback: Callback){val eventId =...   callback.invoke(null, eventId)
```

In JavaScript, you can then check the first argument to see if an error was passed through:
tsx
```
constonPress=()=>{CalendarModule.createCalendarEvent('testName','testLocation',(error, eventId)=>{if(error){console.error(`Error found! ${error}`);console.log(`event id ${eventId} returned`);
```

Another option is to use an onSuccess and onFailure callback:
  * Java
  * Kotlin


java
```
@ReactMethodpublicvoidcreateCalendarEvent(String name,String location,Callback myFailureCallback,Callback mySuccessCallback){
```

kotlin
```
@ReactMethodfuncreateCalendarEvent(   name: String,   location: String,   myFailureCallback: Callback,   mySuccessCallback: Callback){}
```

Then in JavaScript you can add a separate callback for error and success responses:
tsx
```
constonPress=()=>{CalendarModule.createCalendarEvent('testName','testLocation',  error =>{console.error(`Error found! ${error}`);  eventId =>{console.log(`event id ${eventId} returned`);
```

### Promises[​](https://reactnative.dev/docs/legacy/native-modules-android#promises "Direct link to Promises")
Native modules can also fulfill a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), which can simplify your JavaScript, especially when using ES2016's [async/await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function) syntax. When the last parameter of a native module Java/Kotlin method is a Promise, its corresponding JS method will return a JS Promise object.
Refactoring the above code to use a promise instead of callbacks looks like this:
  * Java
  * Kotlin


java
```
importcom.facebook.react.bridge.Promise;@ReactMethodpublicvoidcreateCalendarEvent(String name,String location,Promise promise){try{Integer eventId =...    promise.resolve(eventId);}catch(Exception e){    promise.reject("Create Event Error", e);
```

kotlin
```
import com.facebook.react.bridge.Promise@ReactMethodfuncreateCalendarEvent(name: String, location: String, promise: Promise){try{val eventId =...    promise.resolve(eventId)}catch(e: Throwable){    promise.reject("Create Event Error", e)
```

> Similar to callbacks, a native module method can either reject or resolve a promise (but not both) and can do so at most once. This means that you can either call a success callback or a failure callback, but not both, and each callback can only be invoked at most one time. A native module can, however, store the callback and invoke it later.
The JavaScript counterpart of this method returns a Promise. This means you can use the `await` keyword within an async function to call it and wait for its result:
tsx
```
constonSubmit=async()=>{try{const eventId =awaitCalendarModule.createCalendarEvent('Party','My House',console.log(`Created a new event with id ${eventId}`);}catch(e){console.error(e);
```

The reject method takes different combinations of the following arguments:
  * Java
  * Kotlin


java
```
String code,String message,WritableMap userInfo,Throwable throwable
```

kotlin
```
code: String, message: String, userInfo: WritableMap, throwable: Throwable
```

For more detail, you can find the `Promise.java` interface [here](https://github.com/facebook/react-native/blob/main/packages/react-native/ReactAndroid/src/main/java/com/facebook/react/bridge/Promise.java). If `userInfo` is not provided, ReactNative will set it to null. For the rest of the parameters React Native will use a default value. The `message` argument provides the error `message` shown at the top of an error call stack. Below is an example of the error message shown in JavaScript from the following reject call in Java/Kotlin.
Java/Kotlin reject call:
  * Java
  * Kotlin


java
```
promise.reject("Create Event error","Error parsing date", e);
```

kotlin
```
promise.reject("Create Event error","Error parsing date", e)
```

Error message in React Native App when promise is rejected:
Image of error message
### Sending Events to JavaScript[​](https://reactnative.dev/docs/legacy/native-modules-android#sending-events-to-javascript "Direct link to Sending Events to JavaScript")
Native modules can signal events to JavaScript without being invoked directly. For example, you might want to signal to JavaScript a reminder that a calendar event from the native Android calendar app will occur soon. The easiest way to do this is to use the `RCTDeviceEventEmitter` which can be obtained from the `ReactContext` as in the code snippet below.
  * Java
  * Kotlin


java
```
...importcom.facebook.react.modules.core.DeviceEventManagerModule;importcom.facebook.react.bridge.WritableMap;importcom.facebook.react.bridge.Arguments;...privatevoidsendEvent(ReactContext reactContext,String eventName,@NullableWritableMap params){ reactContext.getJSModule(DeviceEventManagerModule.RCTDeviceEventEmitter.class).emit(eventName, params);privateint listenerCount =0;@ReactMethodpublicvoidaddListener(String eventName){if(listenerCount ==0){// Set up any upstream listeners or background tasks as necessary listenerCount +=1;@ReactMethodpublicvoidremoveListeners(Integer count){ listenerCount -= count;if(listenerCount ==0){// Remove upstream listeners, stop unnecessary background tasks...WritableMap params =Arguments.createMap();params.putString("eventProperty","someValue");...sendEvent(reactContext,"EventReminder", params);
```

kotlin
```
...import com.facebook.react.bridge.WritableMapimport com.facebook.react.bridge.Argumentsimport com.facebook.react.modules.core.DeviceEventManagerModule...privatefunsendEvent(reactContext: ReactContext, eventName: String, params: WritableMap?){  reactContext.getJSModule(DeviceEventManagerModule.RCTDeviceEventEmitter::class.java).emit(eventName, params)privatevar listenerCount =0@ReactMethodfunaddListener(eventName: String){if(listenerCount ==0){// Set up any upstream listeners or background tasks as necessary listenerCount +=1@ReactMethodfunremoveListeners(count: Int){ listenerCount -= countif(listenerCount ==0){// Remove upstream listeners, stop unnecessary background tasks...val params = Arguments.createMap().apply{putString("eventProperty","someValue")...sendEvent(reactContext,"EventReminder", params)
```

JavaScript modules can then register to receive events by `addListener` on the [NativeEventEmitter](https://github.com/facebook/react-native/blob/main/packages/react-native/Libraries/EventEmitter/NativeEventEmitter.js) class.
tsx
```
import{NativeEventEmitter,NativeModules}from'react-native';...useEffect(()=>{const eventEmitter =newNativeEventEmitter(NativeModules.ToastExample);let eventListener = eventEmitter.addListener('EventReminder', event =>{console.log(event.eventProperty)// "someValue"});// Removes the listener once unmountedreturn()=>{   eventListener.remove();},[]);
```

### Getting Activity Result from startActivityForResult[​](https://reactnative.dev/docs/legacy/native-modules-android#getting-activity-result-from-startactivityforresult "Direct link to Getting Activity Result from startActivityForResult")
You'll need to listen to `onActivityResult` if you want to get results from an activity you started with `startActivityForResult`. To do this, you must extend `BaseActivityEventListener` or implement `ActivityEventListener`. The former is preferred as it is more resilient to API changes. Then, you need to register the listener in the module's constructor like so:
  * Java
  * Kotlin


java
```
reactContext.addActivityEventListener(mActivityResultListener);
```

kotlin
```
reactContext.addActivityEventListener(mActivityResultListener);
```

Now you can listen to `onActivityResult` by implementing the following method:
  * Java
  * Kotlin


java
```
@OverridepublicvoidonActivityResult(finalActivity activity,finalint requestCode,finalint resultCode,finalIntent intent){// Your logic here
```

kotlin
```
overridefunonActivityResult(  activity: Activity?,  requestCode: Int,  resultCode: Int,  intent: Intent?// Your logic here
```

Let's implement a basic image picker to demonstrate this. The image picker will expose the method `pickImage` to JavaScript, which will return the path of the image when called.
  * Java
  * Kotlin


kotlin
```
publicclass ImagePickerModule extends ReactContextBaseJavaModule {private static final int IMAGE_PICKER_REQUEST =1;private static final String E_ACTIVITY_DOES_NOT_EXIST ="E_ACTIVITY_DOES_NOT_EXIST";private static final String E_PICKER_CANCELLED ="E_PICKER_CANCELLED";private static final String E_FAILED_TO_SHOW_PICKER ="E_FAILED_TO_SHOW_PICKER";private static final String E_NO_IMAGE_DATA_FOUND ="E_NO_IMAGE_DATA_FOUND";private Promise mPickerPromise;privatefinal ActivityEventListener mActivityEventListener = new BaseActivityEventListener(){@Overridepublic void onActivityResult(Activity activity, int requestCode, int resultCode, Intent intent){if(requestCode == IMAGE_PICKER_REQUEST){if(mPickerPromise !=null){if(resultCode == Activity.RESULT_CANCELED){      mPickerPromise.reject(E_PICKER_CANCELLED,"Image picker was cancelled");}elseif(resultCode == Activity.RESULT_OK){      Uri uri = intent.getData();if(uri ==null){       mPickerPromise.reject(E_NO_IMAGE_DATA_FOUND,"No image data found");}else{       mPickerPromise.resolve(uri.toString());     mPickerPromise =null;ImagePickerModule(ReactApplicationContext reactContext){super(reactContext);// Add the listener for `onActivityResult`  reactContext.addActivityEventListener(mActivityEventListener);@Overridepublic String getName(){return"ImagePickerModule";@ReactMethodpublic void pickImage(final Promise promise){  Activity currentActivity =getCurrentActivity();if(currentActivity ==null){   promise.reject(E_ACTIVITY_DOES_NOT_EXIST,"Activity doesn't exist");return;// Store the promise to resolve/reject when picker returns data  mPickerPromise = promise;try{final Intent galleryIntent = new Intent(Intent.ACTION_PICK);   galleryIntent.setType("image/*");   final Intent chooserIntent = Intent.createChooser(galleryIntent, "Pick an image");   currentActivity.startActivityForResult(chooserIntent, IMAGE_PICKER_REQUEST);  } catch (Exception e) {   mPickerPromise.reject(E_FAILED_TO_SHOW_PICKER, e);   mPickerPromise = null;
```

kotlin
```
classImagePickerModule(reactContext: ReactApplicationContext):ReactContextBaseJavaModule(reactContext){privatevar pickerPromise: Promise?=nullprivateval activityEventListener =object:BaseActivityEventListener(){overridefunonActivityResult(        activity: Activity?,        requestCode: Int,        resultCode: Int,        intent: Intent?if(requestCode == IMAGE_PICKER_REQUEST){          pickerPromise?.let{ promise ->when(resultCode){              Activity.RESULT_CANCELED ->                promise.reject(E_PICKER_CANCELLED,"Image picker was cancelled")              Activity.RESULT_OK ->{val uri = intent?.data                uri?.let{ promise.resolve(uri.toString())}?: promise.reject(E_NO_IMAGE_DATA_FOUND,"No image data found")            pickerPromise =nullinit{    reactContext.addActivityEventListener(activityEventListener)overridefungetName()="ImagePickerModule"@ReactMethodfunpickImage(promise: Promise){val activity = currentActivityif(activity ==null){      promise.reject(E_ACTIVITY_DOES_NOT_EXIST,"Activity doesn't exist")return    pickerPromise = promisetry{val galleryIntent =Intent(Intent.ACTION_PICK).apply{ type ="image\/*"}val chooserIntent = Intent.createChooser(galleryIntent,"Pick an image")      activity.startActivityForResult(chooserIntent, IMAGE_PICKER_REQUEST)}catch(t: Throwable){      pickerPromise?.reject(E_FAILED_TO_SHOW_PICKER, t)      pickerPromise =nullcompanionobject{constval IMAGE_PICKER_REQUEST =1constval E_ACTIVITY_DOES_NOT_EXIST ="E_ACTIVITY_DOES_NOT_EXIST"constval E_PICKER_CANCELLED ="E_PICKER_CANCELLED"constval E_FAILED_TO_SHOW_PICKER ="E_FAILED_TO_SHOW_PICKER"constval E_NO_IMAGE_DATA_FOUND ="E_NO_IMAGE_DATA_FOUND"
```

### Listening to Lifecycle Events[​](https://reactnative.dev/docs/legacy/native-modules-android#listening-to-lifecycle-events "Direct link to Listening to Lifecycle Events")
Listening to the activity's LifeCycle events such as `onResume`, `onPause` etc. is very similar to how `ActivityEventListener` was implemented. The module must implement `LifecycleEventListener`. Then, you need to register a listener in the module's constructor like so:
  * Java
  * Kotlin


java
```
reactContext.addLifecycleEventListener(this);
```

kotlin
```
reactContext.addLifecycleEventListener(this)
```

Now you can listen to the activity's LifeCycle events by implementing the following methods:
  * Java
  * Kotlin


java
```
@OverridepublicvoidonHostResume(){// Activity `onResume`@OverridepublicvoidonHostPause(){// Activity `onPause`@OverridepublicvoidonHostDestroy(){// Activity `onDestroy`
```

kotlin
```
overridefunonHostResume(){// Activity `onResume`overridefunonHostPause(){// Activity `onPause`overridefunonHostDestroy(){// Activity `onDestroy`
```

### Threading[​](https://reactnative.dev/docs/legacy/native-modules-android#threading "Direct link to Threading")
To date, on Android, all native module async methods execute on one thread. Native modules should not have any assumptions about what thread they are being called on, as the current assignment is subject to change in the future. If a blocking call is required, the heavy work should be dispatched to an internally managed worker thread, and any callbacks distributed from there.
Is this page useful?
  * [Create a Calendar Native Module](https://reactnative.dev/docs/legacy/native-modules-android#create-a-calendar-native-module)
    * [Create A Custom Native Module File](https://reactnative.dev/docs/legacy/native-modules-android#create-a-custom-native-module-file)
    * [Export a Native Method to JavaScript](https://reactnative.dev/docs/legacy/native-modules-android#export-a-native-method-to-javascript)
    * [Synchronous Methods](https://reactnative.dev/docs/legacy/native-modules-android#synchronous-methods)
    * [Register the Module (Android Specific)](https://reactnative.dev/docs/legacy/native-modules-android#register-the-module-android-specific)
    * [Test What You Have Built](https://reactnative.dev/docs/legacy/native-modules-android#test-what-you-have-built)
    * [Building as You Iterate](https://reactnative.dev/docs/legacy/native-modules-android#building-as-you-iterate)
  * [Beyond a Calendar Native Module](https://reactnative.dev/docs/legacy/native-modules-android#beyond-a-calendar-native-module)
    * [Better Native Module Export](https://reactnative.dev/docs/legacy/native-modules-android#better-native-module-export)
    * [Argument Types](https://reactnative.dev/docs/legacy/native-modules-android#argument-types)
    * [Exporting Constants](https://reactnative.dev/docs/legacy/native-modules-android#exporting-constants)
    * [Sending Events to JavaScript](https://reactnative.dev/docs/legacy/native-modules-android#sending-events-to-javascript)
    * [Getting Activity Result from startActivityForResult](https://reactnative.dev/docs/legacy/native-modules-android#getting-activity-result-from-startactivityforresult)
    * [Listening to Lifecycle Events](https://reactnative.dev/docs/legacy/native-modules-android#listening-to-lifecycle-events)



