---
url: https://reactnative.dev/docs/next/turbo-native-modules-introduction
title: https://reactnative.dev/docs/next/turbo-native-modules-introduction
date: 2025-05-10T21:41:43.310094
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/next/turbo-native-modules-introduction#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
This is unreleased documentation for React Native **Next** version.
For up-to-date documentation, see the (0.79).
Version: Next
On this page
Your React Native application code may need to interact with native platform APIs that aren't provided by React Native or an existing library. You can write the integration code yourself using a **Turbo Native Module**. This guide will show you how to write one.
The basic steps are:
  1. **define a typed JavaScript specification** using one of the most popular JavaScript type annotation languages: Flow or TypeScript;
  2. **configure your dependency management system to run Codegen** , which converts the specification into native language interfaces;
  3. **write your application code** using your specification; and
  4. **write your native platform code using the generated interfaces** to write and hook your native code into the React Native runtime environment.


Lets work through each of these steps by building an example Turbo Native Module. The rest of this guide assume that you have created your application running the command:
shell
```
npx @react-native-community/cli@latest init TurboModuleExample --version0.76.0
```

## Native Persistent Storage[​](https://reactnative.dev/docs/next/turbo-native-modules-introduction#native-persistent-storage "Direct link to Native Persistent Storage")
This guide will show you how to write an implementation of the [Web Storage API](https://html.spec.whatwg.org/multipage/webstorage.html#dom-localstorage-dev): `localStorage`. The API is relatable to a React developer who might be writing application code on your project.
To make this work on mobile, we need to use Android and iOS APIs:
  * Android: [SharedPreferences](https://developer.android.com/reference/android/content/SharedPreferences), and
  * iOS: [NSUserDefaults](https://developer.apple.com/documentation/foundation/nsuserdefaults).


### 1. Declare Typed Specification[​](https://reactnative.dev/docs/next/turbo-native-modules-introduction#1-declare-typed-specification "Direct link to 1. Declare Typed Specification")
React Native provides a tool called [Codegen](https://reactnative.dev/docs/next/the-new-architecture/what-is-codegen), which takes a specification written in TypeScript or Flow and generates platform specific code for Android and iOS. The specification declares the methods and data types that will pass back and forth between your native code and the React Native JavaScript runtime. A Turbo Native Module is both your specification, the native code you write, and the Codegen interfaces generated from your specification.
To create a specs file:
  1. Inside the root folder of your app, create a new folder called `specs`.
  2. Create a new file called `NativeLocalStorage.ts`.


info
You can see all of the types you can use in your specification and the native types that are generated in the [Appendix](https://reactnative.dev/docs/next/appendix) documentation.
Here is an implementation of the `localStorage` specification:
  * TypeScript
  * Flow


specs/NativeLocalStorage.ts
```
importtype{TurboModule}from'react-native';import{TurboModuleRegistry}from'react-native';exportinterfaceSpecextendsTurboModule{setItem(value:string, key:string):void;getItem(key:string):string|null;removeItem(key:string):void;clear():void;exportdefault TurboModuleRegistry.getEnforcing<Spec>('NativeLocalStorage',
```

NativeLocalStorage.js
```
importtype{TurboModule}from'react-native';import{TurboModule,TurboModuleRegistry}from'react-native';exportinterfaceSpecextendsTurboModule{setItem(value:string,key:string):void;getItem(key:string):?string;removeItem(key:string):void;clear():void;
```

### 2. Configure Codegen to run[​](https://reactnative.dev/docs/next/turbo-native-modules-introduction#2-configure-codegen-to-run "Direct link to 2. Configure Codegen to run")
The specification is used by the React Native Codegen tools to generate platform specific interfaces and boilerplate for us. To do this, Codegen needs to know where to find our specification and what to do with it. Update your `package.json` to include:
package.json
```
"start":"react-native start","test":"jest""codegenConfig":{"name":"NativeLocalStorageSpec","type":"modules","jsSrcsDir":"specs","android":{"javaPackageName":"com.nativelocalstorage""dependencies":{
```

With everything wired up for Codegen, we need to prepare our native code to hook into our generated code.
  * Android
  * iOS


Codegen is executed through the `generateCodegenArtifactsFromSchema` Gradle task:
bash
```
cd android./gradlew generateCodegenArtifactsFromSchemaBUILD SUCCESSFUL in 837ms14 actionable tasks: 3 executed, 11 up-to-date
```

This is automatically run when you build your Android application.
Codegen is run as part of the script phases that's automatically added to the project generated by CocoaPods.
bash
```
cd iosbundle installbundle exec pod install
```

The output will look like this:
shell
```
...Framework build type is static library[Codegen] Adding script_phases to ReactCodegen.[Codegen] Generating ./build/generated/ios/ReactCodegen.podspec.json[Codegen] Analyzing /Users/me/src/TurboModuleExample/package.json[Codegen] Searching for codegen-enabled libraries in the app.[Codegen] Found TurboModuleExample[Codegen] Searching for codegen-enabled libraries in the project dependencies.[Codegen] Found react-native...
```

### 3. Write Application Code using the Turbo Native Module[​](https://reactnative.dev/docs/next/turbo-native-modules-introduction#3-write-application-code-using-the-turbo-native-module "Direct link to 3. Write Application Code using the Turbo Native Module")
Using `NativeLocalStorage`, here’s a modified `App.tsx` that includes some text we want persisted, an input field and some buttons to update this value.
The `TurboModuleRegistry` supports 2 modes of retrieving a Turbo Native Module:
  * `get<T>(name: string): T | null` which will return `null` if the Turbo Native Module is unavailable.
  * `getEnforcing<T>(name: string): T` which will throw an exception if the Turbo Native Module is unavailable. This assumes the module is always available.


App.tsx
```
importReactfrom'react';import{SafeAreaView,StyleSheet,Text,TextInput,Button,}from'react-native';importNativeLocalStoragefrom'./specs/NativeLocalStorage';constEMPTY='<empty>';functionApp():React.JSX.Element{const[value, setValue]=React.useState<string|null>(null);const[editingValue, setEditingValue]=React.useState<string|null>(null);React.useEffect(()=>{const storedValue =NativeLocalStorage?.getItem('myKey');setValue(storedValue ??'');},[]);functionsaveValue(){NativeLocalStorage?.setItem(editingValue ??EMPTY,'myKey');setValue(editingValue);functionclearAll(){NativeLocalStorage?.clear();setValue('');functiondeleteValue(){NativeLocalStorage?.removeItem('myKey');setValue('');return(<SafeAreaViewstyle={{flex:1}}><Textstyle={styles.text}>    Current stored value is: {value ??'No Value'}</Text><TextInputplaceholder="Enter the text you want to store"style={styles.textInput}onChangeText={setEditingValue}/><Buttontitle="Save"onPress={saveValue}/><Buttontitle="Delete"onPress={deleteValue}/><Buttontitle="Clear"onPress={clearAll}/></SafeAreaView>const styles =StyleSheet.create({ text:{  margin:10,  fontSize:20, textInput:{  margin:10,  height:40,  borderColor:'black',  borderWidth:1,  paddingLeft:5,  paddingRight:5,  borderRadius:5,});exportdefaultApp;
```

### 4. Write your Native Platform code[​](https://reactnative.dev/docs/next/turbo-native-modules-introduction#4-write-your-native-platform-code "Direct link to 4. Write your Native Platform code")
With everything prepared, we're going to start writing native platform code. We do this in 2 parts:
note
This guide shows you how to create a Turbo Native Module that only works with the New Architecture. If you need to support both the New Architecture and the Legacy Architecture, please refer to our [backwards compatibility guide](https://github.com/reactwg/react-native-new-architecture/blob/main/docs/backwards-compat.md).
  * Android
  * iOS


Now it's time to write some Android platform code to make sure `localStorage` survives after the application is closed.
The first step is to implement the generated `NativeLocalStorageSpec` interface:
  * Java
  * Kotlin


android/app/src/main/java/com/nativelocalstorage/NativeLocalStorageModule.java
```
packagecom.nativelocalstorage;importandroid.content.Context;importandroid.content.SharedPreferences;importcom.nativelocalstorage.NativeLocalStorageSpec;importcom.facebook.react.bridge.ReactApplicationContext;publicclassNativeLocalStorageModuleextendsNativeLocalStorageSpec{publicstaticfinalStringNAME="NativeLocalStorage";publicNativeLocalStorageModule(ReactApplicationContext reactContext){super(reactContext);@OverridepublicStringgetName(){returnNAME;@OverridepublicvoidsetItem(String value,String key){SharedPreferences sharedPref =getReactApplicationContext().getSharedPreferences("my_prefs",Context.MODE_PRIVATE);SharedPreferences.Editor editor = sharedPref.edit();  editor.putString(key, value);  editor.apply();@OverridepublicStringgetItem(String key){SharedPreferences sharedPref =getReactApplicationContext().getSharedPreferences("my_prefs",Context.MODE_PRIVATE);String username = sharedPref.getString(key,null);return username;@OverridepublicvoidremoveItem(String key){SharedPreferences sharedPref =getReactApplicationContext().getSharedPreferences("my_prefs",Context.MODE_PRIVATE);  sharedPref.edit().remove(key).apply();
```

android/app/src/main/java/com/nativelocalstorage/NativeLocalStorageModule.kt
```
package com.nativelocalstorageimport android.content.Contextimport android.content.SharedPreferencesimport com.nativelocalstorage.NativeLocalStorageSpecimport com.facebook.react.bridge.ReactApplicationContextclassNativeLocalStorageModule(reactContext: ReactApplicationContext):NativeLocalStorageSpec(reactContext){overridefungetName()= NAMEoverridefunsetItem(value: String, key: String){val sharedPref =getReactApplicationContext().getSharedPreferences("my_prefs", Context.MODE_PRIVATE)val editor = sharedPref.edit()  editor.putString(key, value)  editor.apply()overridefungetItem(key: String): String?{val sharedPref =getReactApplicationContext().getSharedPreferences("my_prefs", Context.MODE_PRIVATE)val username = sharedPref.getString(key,null)return username.toString()overridefunremoveItem(key: String){val sharedPref =getReactApplicationContext().getSharedPreferences("my_prefs", Context.MODE_PRIVATE)val editor = sharedPref.edit()  editor.remove(key)  editor.apply()overridefunclear(){val sharedPref =getReactApplicationContext().getSharedPreferences("my_prefs", Context.MODE_PRIVATE)val editor = sharedPref.edit()  editor.clear()  editor.apply()companionobject{constval NAME ="NativeLocalStorage"
```

Next we need to create `NativeLocalStoragePackage`. It provides an object to register our Module in the React Native runtime, by wrapping it as a Base Native Package:
  * Java
  * Kotlin


android/app/src/main/java/com/nativelocalstorage/NativeLocalStoragePackage.java
```
packagecom.nativelocalstorage;importcom.facebook.react.BaseReactPackage;importcom.facebook.react.bridge.NativeModule;importcom.facebook.react.bridge.ReactApplicationContext;importcom.facebook.react.module.model.ReactModuleInfo;importcom.facebook.react.module.model.ReactModuleInfoProvider;importjava.util.HashMap;importjava.util.Map;publicclassNativeLocalStoragePackageextendsBaseReactPackage{@OverridepublicNativeModulegetModule(String name,ReactApplicationContext reactContext){if(name.equals(NativeLocalStorageModule.NAME)){returnnewNativeLocalStorageModule(reactContext);}else{returnnull;@OverridepublicReactModuleInfoProvidergetReactModuleInfoProvider(){returnnewReactModuleInfoProvider(){@OverridepublicMap<String,ReactModuleInfo>getReactModuleInfos(){Map<String,ReactModuleInfo> map =newHashMap<>();    map.put(NativeLocalStorageModule.NAME,newReactModuleInfo(NativeLocalStorageModule.NAME,// nameNativeLocalStorageModule.NAME,// classNamefalse,// canOverrideExistingModulefalse,// needsEagerInitfalse,// isCXXModuletrue// isTurboModule));return map;
```

android/app/src/main/java/com/nativelocalstorage/NativeLocalStoragePackage.kt
```
package com.nativelocalstorageimport com.facebook.react.BaseReactPackageimport com.facebook.react.bridge.NativeModuleimport com.facebook.react.bridge.ReactApplicationContextimport com.facebook.react.module.model.ReactModuleInfoimport com.facebook.react.module.model.ReactModuleInfoProviderclass NativeLocalStoragePackage :BaseReactPackage(){overridefungetModule(name: String, reactContext: ReactApplicationContext): NativeModule?=if(name == NativeLocalStorageModule.NAME){NativeLocalStorageModule(reactContext)}else{nulloverridefungetReactModuleInfoProvider()= ReactModuleInfoProvider {mapOf(   NativeLocalStorageModule.NAME toReactModuleInfo(    name = NativeLocalStorageModule.NAME,    className = NativeLocalStorageModule.NAME,    canOverrideExistingModule =false,    needsEagerInit =false,    isCxxModule =false,    isTurboModule =true
```

Finally, we need to tell the React Native in our main application how to find this `Package`. We call this "registering" the package in React Native.
In this case, you add it to be returned by the [getPackages](https://github.com/facebook/react-native/blob/8d8b8c343e62115a5509e1aed62047053c2f6e39/packages/react-native/ReactAndroid/src/main/java/com/facebook/react/ReactNativeHost.java#L233) method.
info
Later you’ll learn how to distribute your Native Modules as [npm packages](https://reactnative.dev/docs/next/the-new-architecture/create-module-library#publish-the-library-on-npm), which our build tooling will autolink for you.
  * Java
  * Kotlin


android/app/src/main/java/com/turobmoduleexample/MainApplication.java
```
packagecom.inappmodule;importandroid.app.Application;importcom.facebook.react.PackageList;importcom.facebook.react.ReactApplication;importcom.facebook.react.ReactHost;importcom.facebook.react.ReactNativeHost;importcom.facebook.react.ReactPackage;importcom.facebook.react.defaults.DefaultNewArchitectureEntryPoint;importcom.facebook.react.defaults.DefaultReactHost;importcom.facebook.react.defaults.DefaultReactNativeHost;importcom.facebook.soloader.SoLoader;importcom.nativelocalstorage.NativeLocalStoragePackage;importjava.util.ArrayList;importjava.util.List;publicclassMainApplicationextendsApplicationimplementsReactApplication{privatefinalReactNativeHost reactNativeHost =newDefaultReactNativeHost(this){@OverridepublicList<ReactPackage>getPackages(){List<ReactPackage> packages =newPackageList(this).getPackages();// Packages that cannot be autolinked yet can be added manually here, for example:// packages.add(new MyReactNativePackage());   packages.add(newNativeLocalStoragePackage());return packages;@OverridepublicStringgetJSMainModuleName(){return"index";@OverridepublicbooleangetUseDeveloperSupport(){returnBuildConfig.DEBUG;@OverridepublicbooleanisNewArchEnabled(){returnBuildConfig.IS_NEW_ARCHITECTURE_ENABLED;@OverridepublicbooleanisHermesEnabled(){returnBuildConfig.IS_HERMES_ENABLED;@OverridepublicReactHostgetReactHost(){returnDefaultReactHost.getDefaultReactHost(getApplicationContext(), reactNativeHost);@OverridepublicvoidonCreate(){super.onCreate();SoLoader.init(this,false);if(BuildConfig.IS_NEW_ARCHITECTURE_ENABLED){// If you opted-in for the New Architecture, we load the native entry point for this app.DefaultNewArchitectureEntryPoint.load();
```

android/app/src/main/java/com/turobmoduleexample/MainApplication.kt
```
package com.inappmoduleimport android.app.Applicationimport com.facebook.react.PackageListimport com.facebook.react.ReactApplicationimport com.facebook.react.ReactHostimport com.facebook.react.ReactNativeHostimport com.facebook.react.ReactPackageimport com.facebook.react.defaults.DefaultNewArchitectureEntryPoint.loadimport com.facebook.react.defaults.DefaultReactHost.getDefaultReactHostimport com.facebook.react.defaults.DefaultReactNativeHostimport com.facebook.soloader.SoLoaderimport com.nativelocalstorage.NativeLocalStoragePackageclass MainApplication :Application(), ReactApplication {overrideval reactNativeHost: ReactNativeHost =object:DefaultReactNativeHost(this){overridefungetPackages(): List<ReactPackage>=PackageList(this).packages.apply{// Packages that cannot be autolinked yet can be added manually here, for example:// add(MyReactNativePackage())add(NativeLocalStoragePackage())overridefungetJSMainModuleName(): String ="index"overridefungetUseDeveloperSupport(): Boolean = BuildConfig.DEBUGoverrideval isNewArchEnabled: Boolean = BuildConfig.IS_NEW_ARCHITECTURE_ENABLEDoverrideval isHermesEnabled: Boolean = BuildConfig.IS_HERMES_ENABLEDoverrideval reactHost: ReactHostget()=getDefaultReactHost(applicationContext, reactNativeHost)overridefunonCreate(){super.onCreate()  SoLoader.init(this,false)if(BuildConfig.IS_NEW_ARCHITECTURE_ENABLED){// If you opted-in for the New Architecture, we load the native entry point for this app.load()
```

You can now build and run your code on an emulator:
  * npm
  * Yarn


bash
```
npm run android
```

bash
```
yarn run android
```

Now it's time to write some iOS platform code to make sure `localStorage` survives after the application is closed.
## Prepare your Xcode Project[​](https://reactnative.dev/docs/next/turbo-native-modules-introduction#prepare-your-xcode-project "Direct link to Prepare your Xcode Project")
We need to prepare your iOS project using Xcode. After completing these **6 steps** you'll have `RCTNativeLocalStorage` that implements the generated `NativeLocalStorageSpec` interface.
  1. Open the CocoPods generated Xcode Workspace:


bash
```
cd iosopen TurboModuleExample.xcworkspace
```

  1. Right click on app and select `New Group`, call the new group `NativeLocalStorage`.


  1. In the `NativeLocalStorage` group, create `New`→`File from Template`.


  1. Use the `Cocoa Touch Class`.


  1. Name the Cocoa Touch Class `RCTNativeLocalStorage` with the `Objective-C` language.


  1. Rename `RCTNativeLocalStorage.m` → `RCTNativeLocalStorage.mm` making it an Objective-C++ file.


## Implement localStorage with NSUserDefaults[​](https://reactnative.dev/docs/next/turbo-native-modules-introduction#implement-localstorage-with-nsuserdefaults "Direct link to Implement localStorage with NSUserDefaults")
Start by updating `RCTNativeLocalStorage.h`:
NativeLocalStorage/RCTNativeLocalStorage.h
```
// RCTNativeLocalStorage.h// TurboModuleExample#import<Foundation/Foundation.h>#import<NativeLocalStorageSpec/NativeLocalStorageSpec.h>NS_ASSUME_NONNULL_BEGIN@interface RCTNativeLocalStorage : NSObject@interface RCTNativeLocalStorage : NSObject <NativeLocalStorageSpec>@end
```

Then update our implementation to use `NSUserDefaults` with a custom [suite name](https://developer.apple.com/documentation/foundation/nsuserdefaults/1409957-initwithsuitename).
NativeLocalStorage/RCTNativeLocalStorage.mm
```
// RCTNativeLocalStorage.m// TurboModuleExample#import"RCTNativeLocalStorage.h"static NSString *const RCTNativeLocalStorageKey =@"local-storage";@interfaceRCTNativeLocalStorage()@property(strong, nonatomic) NSUserDefaults *localStorage;@end@implementation RCTNativeLocalStorage-(id) init {if(self=[super init]){  _localStorage =[[NSUserDefaults alloc] initWithSuiteName:RCTNativeLocalStorageKey];returnself;-(std::shared_ptr<facebook::react::TurboModule>)getTurboModule:(const facebook::react::ObjCTurboModule::InitParams &)params {return std::make_shared<facebook::react::NativeLocalStorageSpecJSI>(params);-(NSString * _Nullable)getItem:(NSString *)key {return[self.localStorage stringForKey:key];-(void)setItem:(NSString *)value     key:(NSString *)key {[self.localStorage setObject:value forKey:key];-(void)removeItem:(NSString *)key {[self.localStorage removeObjectForKey:key];-(void)clear { NSDictionary *keys =[self.localStorage dictionaryRepresentation];for(NSString *key in keys){[self removeItem:key];+(NSString *)moduleNamereturn@"NativeLocalStorage";@end
```

Important things to note:
  * You can use Xcode to jump to the Codegen `@protocol NativeLocalStorageSpec`. You can also use Xcode to generate stubs for you.


## Register the Native Module in your app[​](https://reactnative.dev/docs/next/turbo-native-modules-introduction#register-the-native-module-in-your-app "Direct link to Register the Native Module in your app")
The last step consist in updating the `package.json` to tell React Native about the link between the JS specs of the Native Module and the concrete implementation of those specs in native code.
Modify the `package.json` as it follows:
package.json
```
"start":"react-native start","test":"jest""codegenConfig":{"name":"AppSpecs","type":"modules","jsSrcsDir":"specs","android":{"javaPackageName":"com.sampleapp.specs""ios":"modulesProvider":{"NativeLocalStorage":"RCTNativeLocalStorage""dependencies":{
```

At this point, you need to re-install the pods to make sure that codegen runs again to generate the new files:
bash
```
# from the ios folderbundle exec pod installopen SampleApp.xcworkspace
```

If you now build your application from Xcode, you should be able to build successfully.
## Build and run your code on a Simulator[​](https://reactnative.dev/docs/next/turbo-native-modules-introduction#build-and-run-your-code-on-a-simulator "Direct link to Build and run your code on a Simulator")
  * npm
  * Yarn


bash
```
npm run ios
```

bash
```
yarn run ios
```

Is this page useful?
  * [Native Persistent Storage](https://reactnative.dev/docs/next/turbo-native-modules-introduction#native-persistent-storage)
    * [1. Declare Typed Specification](https://reactnative.dev/docs/next/turbo-native-modules-introduction#1-declare-typed-specification)
    * [2. Configure Codegen to run](https://reactnative.dev/docs/next/turbo-native-modules-introduction#2-configure-codegen-to-run)
    * [3. Write Application Code using the Turbo Native Module](https://reactnative.dev/docs/next/turbo-native-modules-introduction#3-write-application-code-using-the-turbo-native-module)
    * [4. Write your Native Platform code](https://reactnative.dev/docs/next/turbo-native-modules-introduction#4-write-your-native-platform-code)



