---
url: https://reactnative.dev/docs/next/fabric-native-components-introduction
title: https://reactnative.dev/docs/next/fabric-native-components-introduction
date: 2025-05-10T21:41:07.220101
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/next/fabric-native-components-introduction#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
This is unreleased documentation for React Native **Next** version.
For up-to-date documentation, see the (0.79).
Version: Next
On this page
If you want to build _new_ React Native Components that wrap around a [Host Component](https://reactnative.dev/architecture/glossary#host-view-tree-and-host-view) like a unique kind of [CheckBox](https://developer.android.com/reference/androidx/appcompat/widget/AppCompatCheckBox) on Android, or a [UIButton](https://developer.apple.com/documentation/uikit/uibutton?language=objc) on iOS, you should use a Fabric Native Component.
This guide will show you how to build Fabric Native Components, by implementing a web view component. The steps to doing this are:
  1. Define a JavaScript specification using Flow or TypeScript.
  2. Configure the dependencies management system to generate code from the provided spec and to be auto-linked.
  3. Implement the Native code.
  4. Use the Component in an App.


You're going to need a plain template generated application to use the component:
bash
```
npx @react-native-community/cli@latest init Demo --install-pods false
```

## Creating a WebView Component[​](https://reactnative.dev/docs/next/fabric-native-components-introduction#creating-a-webview-component "Direct link to Creating a WebView Component")
This guide will show you how to create a Web View component. We will be creating the component by using the Android's [`WebView`](https://developer.android.com/reference/android/webkit/WebView) component, and the iOS [`WKWebView`](https://developer.apple.com/documentation/webkit/wkwebview?language=objc) component.
Let's start by creating the folders structure to hold our component's code:
bash
```
mkdir-p Demo/{specs,android/app/src/main/java/com/webview}
```

This gives you the following layout where you'll working:
```
Demo├── android/app/src/main/java/com/webview└── ios└── specs
```

  * The `android/app/src/main/java/com/webview` folder is the folder that will contain our Android code.
  * The `ios` folder is the folder that will contain our iOS code.
  * The `specs` folder is the folder that will contain the Codegen's specification file.


## 1. Define Specification for Codegen[​](https://reactnative.dev/docs/next/fabric-native-components-introduction#1-define-specification-for-codegen "Direct link to 1. Define Specification for Codegen")
Your specification must be defined in either [TypeScript](https://www.typescriptlang.org/) or [Flow](https://flow.org/) (see [Codegen](https://reactnative.dev/docs/next/the-new-architecture/what-is-codegen) documentation for more details). This is used by Codegen to generate the C++, Objective-C++ and Java to connect your platform code to the JavaScript runtime that React runs in.
The specification file must be named `<MODULE_NAME>NativeComponent.{ts|js}` to work with Codegen. The suffix `NativeComponent` is not only a convention, it is actually used by Codegen to detect a spec file.
Use this specification for our WebView Component:
  * TypeScript
  * Flow


Demo/specs/WebViewNativeComponent.ts
```
importtype{ CodegenTypes, HostComponent, ViewProps,}from'react-native';import{codegenNativeComponent}from'react-native';typeWebViewScriptLoadedEvent={ result:'success'|'error';exportinterfaceNativePropsextendsViewProps{ sourceURL?:string; onScriptLoaded?: CodegenTypes.BubblingEventHandler<WebViewScriptLoadedEvent>|null;exportdefaultcodegenNativeComponent<NativeProps>('CustomWebView',)as HostComponent<NativeProps>;
```

Demo/RCTWebView/js/RCTWebViewNativeComponent.js
```
// @flow strict-localimporttype{CodegenTypes, HostComponent, ViewProps}from'react-native';import{codegenNativeComponent}from'react-native';typeWebViewScriptLoadedEvent= $ReadOnly<{| result:"success"|"error",|}>;typeNativeProps= $ReadOnly<{|...ViewProps, sourceURL?:string; onScriptLoaded?: CodegenTypes.BubblingEventHandler<WebViewScriptLoadedEvent>?;|}>;exportdefault(codegenNativeComponent<NativeProps>('CustomWebView',): HostComponent<NativeProps>);
```

This specification is composed of three main parts, excluding the imports:
  * The `WebViewScriptLoadedEvent` is a supporting data type for the data the event needs to pass from native to JavaScript.
  * The `NativeProps` is a definition of the props that we can set on the component.
  * The `codegenNativeComponent` statement allows us to codegenerate the code for the custom component and that defines a name for the component used to match the native implementations.


As with Native Modules, you can have multiple specification files in the `specs/` directory. For more information about the types you can use, and the platform types these map to, see the [appendix](https://reactnative.dev/docs/next/appendix#codegen-typings).
## 2. Configure Codegen to run[​](https://reactnative.dev/docs/next/fabric-native-components-introduction#2-configure-codegen-to-run "Direct link to 2. Configure Codegen to run")
The specification is used by the React Native's Codegen tools to generate platform specific interfaces and boilerplate for us. To do this, Codegen needs to know where to find our specification and what to do with it. Update your `package.json` to include:
json
```
"start":"react-native start","test":"jest""codegenConfig":{"name":"AppSpec","type":"components","jsSrcsDir":"specs","android":{"javaPackageName":"com.webview""ios":{"componentProvider":{"CustomWebView":"RCTWebView""dependencies":{
```

With everything wired up for Codegen, we need to prepare our native code to hook into our generated code.
Note that for iOS, we are declaratively mapping the name of the JS component that is exported by the spec (`CustomWebView`) with the iOS class that will implement the component natively.
## 2. Building your Native Code[​](https://reactnative.dev/docs/next/fabric-native-components-introduction#2-building-your-native-code "Direct link to 2. Building your Native Code")
Now it's time to write the native platform code so that when React requires to render a view, the platform can create the right native view and can render it on screen.
You should work through both the Android and iOS platforms.
note
This guide shows you how to create a Native Component that only works with the New Architecture. If you need to support both the New Architecture and the Legacy Architecture, please refer to our [backwards compatibility guide](https://github.com/reactwg/react-native-new-architecture/blob/main/docs/backwards-compat.md).
  * Android
  * iOS


Now it's time to write some Android platform code to be able to render the web view. The steps you need to follow are:
  * Running Codegen
  * Write the code for the `ReactWebView`
  * Write the code for the `ReactWebViewManager`
  * Write the code for the `ReactWebViewPackage`
  * Register the `ReactWebViewPackage` in the application


### 1. Run Codegen through Gradle[​](https://reactnative.dev/docs/next/fabric-native-components-introduction#1-run-codegen-through-gradle "Direct link to 1. Run Codegen through Gradle")
Run this once to generate boilerplate that your IDE of choice can use.
Demo/
```
cd android./gradlew generateCodegenArtifactsFromSchema
```

Codegen will generate the `ViewManager` interface you need to implement and the `ViewManager` delegate for the web view.
### 2. Write the `ReactWebView`[​](https://reactnative.dev/docs/next/fabric-native-components-introduction#2-write-the-reactwebview "Direct link to 2-write-the-reactwebview")
The `ReactWebView` is the component that wraps the Android native view that React Native will render when using our custom Component.
Create a `ReactWebView.java` or a `ReactWebView.kt` file in the `android/src/main/java/com/webview` folder with this code:
  * Java
  * Kotlin


Demo/android/src/main/java/com/webview/ReactWebView.java
```
packagecom.webview;importandroid.content.Context;importandroid.util.AttributeSet;importandroid.webkit.WebView;importandroid.webkit.WebViewClient;importcom.facebook.react.bridge.Arguments;importcom.facebook.react.bridge.WritableMap;importcom.facebook.react.bridge.ReactContext;importcom.facebook.react.uimanager.UIManagerHelper;importcom.facebook.react.uimanager.events.Event;publicclassReactWebViewextendsWebView{publicReactWebView(Context context){super(context);configureComponent();publicReactWebView(Context context,AttributeSet attrs){super(context, attrs);configureComponent();publicReactWebView(Context context,AttributeSet attrs,int defStyleAttr){super(context, attrs, defStyleAttr);configureComponent();privatevoidconfigureComponent(){this.setLayoutParams(newLayoutParams(LayoutParams.MATCH_PARENT,LayoutParams.MATCH_PARENT));this.setWebViewClient(newWebViewClient(){@OverridepublicvoidonPageFinished(WebView view,String url){emitOnScriptLoaded(OnScriptLoadedEventResult.success);});publicvoidemitOnScriptLoaded(OnScriptLoadedEventResult result){ReactContext reactContext =(ReactContext) context;int surfaceId =UIManagerHelper.getSurfaceId(reactContext);EventDispatcher eventDispatcher =UIManagerHelper.getEventDispatcherForReactTag(reactContext,getId());WritableMap payload =Arguments.createMap();  payload.putString("result", result.name());OnScriptLoadedEvent event =newOnScriptLoadedEvent(surfaceId,getId(), payload);if(eventDispatcher !=null){   eventDispatcher.dispatchEvent(event);publicenumOnScriptLoadedEventResult{  success,  errorprivateclassOnScriptLoadedEventextendsEvent<OnScriptLoadedEvent>{privatefinalWritableMap payload;OnScriptLoadedEvent(int surfaceId,int viewId,WritableMap payload){super(surfaceId, viewId);this.payload = payload;@OverridepublicStringgetEventName(){return"onScriptLoaded";@OverridepublicWritableMapgetEventData(){return payload;
```

Demo/android/src/main/java/com/webview/ReactWebView.kt
```
package com.webviewimport android.content.Contextimport android.util.AttributeSetimport android.webkit.WebViewimport android.webkit.WebViewClientimport com.facebook.react.bridge.Argumentsimport com.facebook.react.bridge.WritableMapimport com.facebook.react.bridge.ReactContextimport com.facebook.react.uimanager.UIManagerHelperimport com.facebook.react.uimanager.events.Eventclass ReactWebView: WebView {constructor(context: Context):super(context){configureComponent()constructor(context: Context, attrs: AttributeSet?):super(context, attrs){configureComponent()constructor(context: Context, attrs: AttributeSet?, defStyleAttr: Int):super(context, attrs, defStyleAttr){configureComponent()privatefunconfigureComponent(){this.layoutParams =LayoutParams(LayoutParams.MATCH_PARENT, LayoutParams.MATCH_PARENT)this.webViewClient =object:WebViewClient(){overridefunonPageFinished(view: WebView, url: String){emitOnScriptLoaded(OnScriptLoadedEventResult.success)funemitOnScriptLoaded(result: OnScriptLoadedEventResult){val reactContext = context as ReactContextval surfaceId = UIManagerHelper.getSurfaceId(reactContext)val eventDispatcher = UIManagerHelper.getEventDispatcherForReactTag(reactContext, id)val payload =    Arguments.createMap().apply{putString("result", result.name)val event =OnScriptLoadedEvent(surfaceId, id, payload)  eventDispatcher?.dispatchEvent(event)enumclass OnScriptLoadedEventResult {  success,  error;innerclassOnScriptLoadedEvent(   surfaceId: Int,   viewId: Int,privateval payload: WritableMap): Event<OnScriptLoadedEvent>(surfaceId, viewId){overridefungetEventName()="onScriptLoaded"overridefungetEventData()= payload
```

The `ReactWebView` extends the Android `WebView` so you can reuse all the properties already defined by the platform with ease.
The class defines the three Android constructors but defers their actual implementation to the private `configureComponent` function. This function takes care of initializing all the components specific properties: in this case you are setting the layout of the `WebView` and you are defining the `WebClient` that you use to customize the behavior of the `WebView`. In this code, the `ReactWebView` emits an event when the page finishes loading, by implementing the `WebClient`'s `onPageFinished` method.
The code then defines a helper function to actually emit an event. To emit an event, you have to:
  * grab a reference to the `ReactContext`;
  * retrieve the `surfaceId` of the view that you are presenting;
  * grab a reference to the `eventDispatcher` associated with the view;
  * build the payload for the event using a `WritableMap` object;
  * create the event object that you need to send to JavaScript;
  * call the `eventDispatcher.dispatchEvent` to send the event.


The last part of the file contains the definition of the data types you need to send the event:
  * The `OnScriptLoadedEventResult`, with the possible outcomes of the `OnScriptLoaded` event.
  * The actual `OnScriptLoadedEvent` that needs to extend the React Native's `Event` class.


### 3. Write the `WebViewManager`[​](https://reactnative.dev/docs/next/fabric-native-components-introduction#3-write-the-webviewmanager "Direct link to 3-write-the-webviewmanager")
The `WebViewManager` is the class that connects the React Native runtime with the native view.
When React receives the instruction from the app to render a specific component, React uses the registered view manager to create the view and to pass all the required properties.
This is the code of the `ReactWebViewManager`.
  * Java
  * Kotlin


Demo/android/src/main/java/com/webview/ReactWebViewManager.java
```
packagecom.webview;importcom.facebook.react.bridge.ReactApplicationContext;importcom.facebook.react.module.annotations.ReactModule;importcom.facebook.react.uimanager.SimpleViewManager;importcom.facebook.react.uimanager.ThemedReactContext;importcom.facebook.react.uimanager.ViewManagerDelegate;importcom.facebook.react.uimanager.annotations.ReactProp;importcom.facebook.react.viewmanagers.CustomWebViewManagerInterface;importcom.facebook.react.viewmanagers.CustomWebViewManagerDelegate;importjava.util.HashMap;importjava.util.Map;@ReactModule(name =ReactWebViewManager.REACT_CLASS)classReactWebViewManagerextendsSimpleViewManager<ReactWebView>implementsCustomWebViewManagerInterface<ReactWebView>{privatefinalCustomWebViewManagerDelegate<ReactWebView,ReactWebViewManager> delegate =newCustomWebViewManagerDelegate<>(this);@OverridepublicViewManagerDelegate<ReactWebView>getDelegate(){return delegate;@OverridepublicStringgetName(){returnREACT_CLASS;@OverridepublicReactWebViewcreateViewInstance(ThemedReactContext context){returnnewReactWebView(context);@ReactProp(name ="sourceUrl")@OverridepublicvoidsetSourceURL(ReactWebView view,String sourceURL){if(sourceURL ==null){   view.emitOnScriptLoaded(ReactWebView.OnScriptLoadedEventResult.error);return;  view.loadUrl(sourceURL,newHashMap<>());publicstaticfinalStringREACT_CLASS="CustomWebView";@OverridepublicMap<String,Object>getExportedCustomBubblingEventTypeConstants(){Map<String,Object> map =newHashMap<>();Map<String,Object> bubblingMap =newHashMap<>();  bubblingMap.put("phasedRegistrationNames",newHashMap<String,String>(){{put("bubbled","onScriptLoaded");put("captured","onScriptLoadedCapture");}});  map.put("onScriptLoaded", bubblingMap);return map;
```

Demo/android/src/main/java/com/webview/ReactWebViewManager.kt
```
package com.webviewimport com.facebook.react.bridge.ReactApplicationContext;import com.facebook.react.module.annotations.ReactModule;import com.facebook.react.uimanager.SimpleViewManager;import com.facebook.react.uimanager.ThemedReactContext;import com.facebook.react.uimanager.ViewManagerDelegate;import com.facebook.react.uimanager.annotations.ReactProp;import com.facebook.react.viewmanagers.CustomWebViewManagerInterface;import com.facebook.react.viewmanagers.CustomWebViewManagerDelegate;@ReactModule(name = ReactWebViewManager.REACT_CLASS)classReactWebViewManager(context: ReactApplicationContext): SimpleViewManager<ReactWebView>(), CustomWebViewManagerInterface<ReactWebView>{privateval delegate: CustomWebViewManagerDelegate<ReactWebView, ReactWebViewManager>=CustomWebViewManagerDelegate(this)overridefungetDelegate(): ViewManagerDelegate<ReactWebView>= delegateoverridefungetName(): String = REACT_CLASSoverridefuncreateViewInstance(context: ThemedReactContext): ReactWebView =ReactWebView(context)@ReactProp(name ="sourceUrl")overridefunsetSourceURL(view: ReactWebView, sourceURL: String?){if(sourceURL ==null){   view.emitOnScriptLoaded(ReactWebView.OnScriptLoadedEventResult.error)return;  view.loadUrl(sourceURL,emptyMap())companionobject{constval REACT_CLASS ="CustomWebView"overridefungetExportedCustomBubblingEventTypeConstants(): Map<String, Any>=mapOf("onScriptLoaded"tomapOf("phasedRegistrationNames"tomapOf("bubbled"to"onScriptLoaded","captured"to"onScriptLoadedCapture")))
```

The `ReactWebViewManager` extends the `SimpleViewManager` class from React and implements the `CustomWebViewManagerInterface`, generated by Codegen.
It holds a reference of the `CustomWebViewManagerDelegate`, another element generated by Codegen.
It then overrides the `getName` function, which must return the same name used in the spec's `codegenNativeComponent` function call.
The `createViewInstance` function is responsible to instantiate a new `ReactWebView`.
Then, the ViewManager needs to define how all the React's components props will update the native view. In the example, you need to decide how to handle the `sourceURL` property that React will set on the `WebView`.
Finally, if the component can emit an event, you need to map the event name by overriding the `getExportedCustomBubblingEventTypeConstants` for bubbling events, or the `getExportedCustomDirectEventTypeConstants` for direct events.
### 4. Write the `ReactWebViewPackage`[​](https://reactnative.dev/docs/next/fabric-native-components-introduction#4-write-the-reactwebviewpackage "Direct link to 4-write-the-reactwebviewpackage")
As you do with Native Modules, Native Components also need to implement the `ReactPackage` class. This is an object that you can use to register the component in the React Native runtime.
This is the code for the `ReactWebViewPackage`:
  * Java
  * Kotlin


Demo/android/src/main/java/com/webview/ReactWebViewPackage.java
```
packagecom.webview;importcom.facebook.react.BaseReactPackage;importcom.facebook.react.bridge.NativeModule;importcom.facebook.react.bridge.ReactApplicationContext;importcom.facebook.react.module.model.ReactModuleInfo;importcom.facebook.react.module.model.ReactModuleInfoProvider;importcom.facebook.react.uimanager.ViewManager;importjava.util.Collections;importjava.util.HashMap;importjava.util.List;importjava.util.Map;publicclassReactWebViewPackageextendsBaseReactPackage{@OverridepublicList<ViewManager<?,?>>createViewManagers(ReactApplicationContext reactContext){returnCollections.singletonList(newReactWebViewManager(reactContext));@OverridepublicNativeModulegetModule(String s,ReactApplicationContext reactApplicationContext){if(ReactWebViewManager.REACT_CLASS.equals(s)){returnnewReactWebViewManager(reactApplicationContext);returnnull;@OverridepublicReactModuleInfoProvidergetReactModuleInfoProvider(){returnnewReactModuleInfoProvider(){@OverridepublicMap<String,ReactModuleInfo>getReactModuleInfos(){Map<String,ReactModuleInfo> map =newHashMap<>();    map.put(ReactWebViewManager.REACT_CLASS,newReactModuleInfo(ReactWebViewManager.REACT_CLASS,// nameReactWebViewManager.REACT_CLASS,// classNamefalse,// canOverrideExistingModulefalse,// needsEagerInitfalse,// isCxxModuletrue// isTurboModule));return map;
```

Demo/android/src/main/java/com/webview/ReactWebViewPackage.kt
```
package com.webviewimport com.facebook.react.BaseReactPackageimport com.facebook.react.bridge.NativeModuleimport com.facebook.react.bridge.ReactApplicationContextimport com.facebook.react.module.model.ReactModuleInfoimport com.facebook.react.module.model.ReactModuleInfoProviderimport com.facebook.react.uimanager.ViewManagerclass ReactWebViewPackage :BaseReactPackage(){overridefuncreateViewManagers(reactContext: ReactApplicationContext): List<ViewManager<*,*>>{returnlistOf(ReactWebViewManager(reactContext))overridefungetModule(s: String, reactApplicationContext: ReactApplicationContext): NativeModule?{when(s){   ReactWebViewManager.REACT_CLASS ->ReactWebViewManager(reactApplicationContext)returnnulloverridefungetReactModuleInfoProvider(): ReactModuleInfoProvider = ReactModuleInfoProvider {mapOf(ReactWebViewManager.REACT_CLASS toReactModuleInfo(   _name = ReactWebViewManager.REACT_CLASS,   _className = ReactWebViewManager.REACT_CLASS,   _canOverrideExistingModule =false,   _needsEagerInit =false,   isCxxModule =false,   isTurboModule =true,
```

The `ReactWebViewPackage` extends the `BaseReactPackage` and implements all the methods required to properly register our component.
  * the `createViewManagers` method is the factory method that creates the `ViewManager` that manage the custom views.
  * the `getModule` method returns the proper ViewManager depending on the View that React Native needs to render.
  * the `getReactModuleInfoProvider` provides all the information required when registering the module in the runtime,


### 5. Register the `ReactWebViewPackage` in the application[​](https://reactnative.dev/docs/next/fabric-native-components-introduction#5-register-the-reactwebviewpackage-in-the-application "Direct link to 5-register-the-reactwebviewpackage-in-the-application")
Finally, you need to register the `ReactWebViewPackage` in the application. We do that by modifying the `MainApplication` file by adding the `ReactWebViewPackage` to the list of packages returned by the `getPackages` function.
Demo/app/src/main/java/com/demo/MainApplication.kt
```
package com.demoimport android.app.Applicationimport com.facebook.react.PackageListimport com.facebook.react.ReactApplicationimport com.facebook.react.ReactHostimport com.facebook.react.ReactNativeHostimport com.facebook.react.ReactPackageimport com.facebook.react.defaults.DefaultNewArchitectureEntryPoint.loadimport com.facebook.react.defaults.DefaultReactHost.getDefaultReactHostimport com.facebook.react.defaults.DefaultReactNativeHostimport com.facebook.react.soloader.OpenSourceMergedSoMappingimport com.facebook.soloader.SoLoaderimport com.webview.ReactWebViewPackageclass MainApplication :Application(), ReactApplication {overrideval reactNativeHost: ReactNativeHost =object:DefaultReactNativeHost(this){overridefungetPackages(): List<ReactPackage>=PackageList(this).packages.apply{add(ReactWebViewPackage())overridefungetJSMainModuleName(): String ="index"overridefungetUseDeveloperSupport(): Boolean = BuildConfig.DEBUGoverrideval isNewArchEnabled: Boolean = BuildConfig.IS_NEW_ARCHITECTURE_ENABLEDoverrideval isHermesEnabled: Boolean = BuildConfig.IS_HERMES_ENABLEDoverrideval reactHost: ReactHostget()=getDefaultReactHost(applicationContext, reactNativeHost)overridefunonCreate(){super.onCreate()  SoLoader.init(this, OpenSourceMergedSoMapping)if(BuildConfig.IS_NEW_ARCHITECTURE_ENABLED){load()
```

Now it's time to write some iOS platform code to be able to render the web view. The steps you need to follow are:
  * Run Codegen.
  * Write the code for the `RCTWebView`
  * Register the `RCTWebView` in the application


### 1. Run Codegen[​](https://reactnative.dev/docs/next/fabric-native-components-introduction#1-run-codegen "Direct link to 1. Run Codegen")
You can [manually run](https://reactnative.dev/docs/next/the-new-architecture/codegen-cli) the Codegen, however it's simpler to use the application you're going to demo the component in to do this for you.
bash
```
cd iosbundle installbundle exec pod install
```

Importantly you will see logging output from Codegen, which we're going to use in Xcode to build our WebView native component.
warning
You should be careful about committing generated code to your repository. Generated code is specific to each version of React Native. Use npm [peerDependencies](https://nodejs.org/en/blog/npm/peer-dependencies) to restrict compatibility with version of React Native.
### 3. Write the `RCTWebView`[​](https://reactnative.dev/docs/next/fabric-native-components-introduction#3-write-the-rctwebview "Direct link to 3-write-the-rctwebview")
We need to prepare your iOS project using Xcode by completing these **5 steps** :
  1. Open the CocoPods generated Xcode Workspace:


bash
```
cd iosopen Demo.xcworkspace
```

  1. Right click on app and select `New Group`, call the new group `WebView`.


  1. In the `WebView` group, create `New`→`File from Template`.


  1. Use the `Objective-C File` template, and name it `RCTWebView`.


  1. Repeat step 4 and create a header file named `RCTWebView.h`.
  2. Rename `RCTWebView.m` → `RCTWebView.mm` making it an Objective-C++ file.


Demo/ios
```
Podfile...Demo├── AppDelegate.swift...├── RCTWebView.h└── RCTWebView.mm
```

After creating the header file and the implementation file, you can start implementing them.
This is the code for the `RCTWebView.h` file, which declares the component interface.
Demo/RCTWebView/RCTWebView.h
```
#import<React/RCTViewComponentView.h>#import<UIKit/UIKit.h>NS_ASSUME_NONNULL_BEGIN@interface RCTWebView : RCTViewComponentView// You would declare native methods you'd want to access from the view here@endNS_ASSUME_NONNULL_END
```

This class defines an `RCTWebView` which extends the `RCTViewComponentView` class. This is the base class for all the native components and it is provided by React Native.
The code for the implementation file (`RCTWebView.mm`) is the following:
Demo/RCTWebView/RCTWebView.mm
```
#import"RCTWebView.h"#import<react/renderer/components/AppSpec/ComponentDescriptors.h>#import<react/renderer/components/AppSpec/EventEmitters.h>#import<react/renderer/components/AppSpec/Props.h>#import<react/renderer/components/AppSpec/RCTComponentViewHelpers.h>#import<WebKit/WebKit.h>using namespace facebook::react;@interfaceRCTWebView()<RCTCustomWebViewViewProtocol, WKNavigationDelegate>@end@implementation RCTWebView { NSURL * _sourceURL; WKWebView * _webView;-(instancetype)initif(self=[super init]){  _webView =[WKWebView new];  _webView.navigationDelegate =self;[self addSubview:_webView];returnself;-(void)updateProps:(Props::Shared const&)props oldProps:(Props::Shared const&)oldPropsconstauto&oldViewProps =*std::static_pointer_cast<CustomWebViewProps const>(_props);constauto&newViewProps =*std::static_pointer_cast<CustomWebViewProps const>(props);// Handle your props hereif(oldViewProps.sourceURL != newViewProps.sourceURL){  NSString *urlString =[NSString stringWithCString:newViewProps.sourceURL.c_str() encoding:NSUTF8StringEncoding];  _sourceURL =[NSURL URLWithString:urlString];if([self urlIsValid:newViewProps.sourceURL]){[_webView loadRequest:[NSURLRequest requestWithURL:_sourceURL]];[super updateProps:props oldProps:oldProps];-(void)layoutSubviews[super layoutSubviews]; _webView.frame =self.bounds;#pragmamark - WKNavigationDelegate-(void)webView:(WKWebView *)webView didFinishNavigation:(WKNavigation *)navigation CustomWebViewEventEmitter::OnScriptLoaded result = CustomWebViewEventEmitter::OnScriptLoaded{CustomWebViewEventEmitter::OnScriptLoadedResult::Success};self.eventEmitter.onScriptLoaded(result);-(BOOL)urlIsValid:(std::string)propStringif(propString.length()>0&&!_sourceURL){  CustomWebViewEventEmitter::OnScriptLoaded result = CustomWebViewEventEmitter::OnScriptLoaded{CustomWebViewEventEmitter::OnScriptLoadedResult::Error};self.eventEmitter.onScriptLoaded(result);return NO;return YES;// Event emitter convenience method-(const CustomWebViewEventEmitter &)eventEmitterreturn static_cast<const CustomWebViewEventEmitter &>(*_eventEmitter);+(ComponentDescriptorProvider)componentDescriptorProviderreturn concreteComponentDescriptorProvider<CustomWebViewComponentDescriptor>();@end
```

This code is written in Objective-C++ and contains various details:
  * the `@interface` implements two protocols: 
    * `RCTCustomWebViewViewProtocol`, generated by Codegen;
    * `WKNavigationDelegate`, provided by the WebKit framework to handle the web view navigation events;
  * the `init` method that instantiates the `WKWebView`, adds it to the subviews and that sets the `navigationDelegate`;
  * the `updateProps` method that is called by React Native when the component's props change;
  * the `layoutSubviews` method that describes how the custom view needs to be laid out;
  * the `webView:didFinishNavigation:` method that lets you handle what to do when the `WKWebView` finishes loading the page;
  * the `urlIsValid:(std::string)propString` method that checks whether the URL received as prop is valid;
  * the `eventEmitter` method which is a utility to retrieve a strongly typed `eventEmitter` instance
  * the `componentDescriptorProvider` which returns the `ComponentDescriptor` generated by Codegen;


#### Add WebKit framework[​](https://reactnative.dev/docs/next/fabric-native-components-introduction#add-webkit-framework "Direct link to Add WebKit framework")
note
This step is only required because we are creating a Web view. Web components on iOS needs to be linked against the WebKit framework provided by Apple. If your component doesn't need to access web-specific features, you can skip this step.
A web view requires access to some features that Apple provides through one of the frameworks shipped with Xcode and the devices: WebKit. You can see it in the native code by the `#import <WebKit/WebKit.h>` line added in the `RCTWebView.mm`.
To link the WebKit framework in your app, follow these steps:
  1. In Xcode, Click on your project
  2. Select the app target
  3. Select the General tab
  4. Scroll down until you find the _"Frameworks, Libraries, and Embedded Contents"_ section, and press the `+` button


  1. In the search bar, filter for WebKit
  2. Select the WebKit framework
  3. Click on Add.


## 3. Use your Native Component[​](https://reactnative.dev/docs/next/fabric-native-components-introduction#3-use-your-native-component "Direct link to 3. Use your Native Component")
Finally, you can use the new component in your app. Update your generated `App.tsx` to:
Demo/App.tsx
```
importReactfrom'react';import{Alert,StyleSheet,View}from'react-native';importWebViewfrom'./specs/WebViewNativeComponent';functionApp():React.JSX.Element{return(<View style={styles.container}><WebView    sourceURL="https://react.dev/"    style={styles.webview}    onScriptLoaded={()=>{Alert.alert('Page Loaded');</View>const styles =StyleSheet.create({container:{flex:1,alignItems:'center',alignContent:'center',webview:{width:'100%',height:'100%',});exportdefaultApp;
```

This code creates an app that uses the new `WebView` component we created to load the `react.dev` website.
The app also shows an alert when the web page is loaded.
## 4. Run your App using the WebView Component[​](https://reactnative.dev/docs/next/fabric-native-components-introduction#4-run-your-app-using-the-webview-component "Direct link to 4. Run your App using the WebView Component")
  * Android
  * iOS


bash
```
yarn run android
```

bash
```
yarn run ios
```

Android| iOS  
---|---  
Is this page useful?
  * [Creating a WebView Component](https://reactnative.dev/docs/next/fabric-native-components-introduction#creating-a-webview-component)
  * [1. Define Specification for Codegen](https://reactnative.dev/docs/next/fabric-native-components-introduction#1-define-specification-for-codegen)
  * [2. Configure Codegen to run](https://reactnative.dev/docs/next/fabric-native-components-introduction#2-configure-codegen-to-run)
  * [2. Building your Native Code](https://reactnative.dev/docs/next/fabric-native-components-introduction#2-building-your-native-code)
  * [3. Use your Native Component](https://reactnative.dev/docs/next/fabric-native-components-introduction#3-use-your-native-component)
  * [4. Run your App using the WebView Component](https://reactnative.dev/docs/next/fabric-native-components-introduction#4-run-your-app-using-the-webview-component)



