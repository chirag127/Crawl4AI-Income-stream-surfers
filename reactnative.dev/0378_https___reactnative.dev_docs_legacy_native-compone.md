---
url: https://reactnative.dev/docs/legacy/native-components-android
title: https://reactnative.dev/docs/legacy/native-components-android
date: 2025-05-10T21:40:32.386530
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/legacy/native-components-android#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
info
Native Module and Native Components are our stable technologies used by the legacy architecture. They will be deprecated in the future when the New Architecture will be stable. The New Architecture uses [Turbo Native Module](https://github.com/reactwg/react-native-new-architecture/blob/main/docs/turbo-modules.md) and [Fabric Native Components](https://github.com/reactwg/react-native-new-architecture/blob/main/docs/fabric-native-components.md) to achieve similar results.
There are tons of native UI widgets out there ready to be used in the latest apps - some of them are part of the platform, others are available as third-party libraries, and still more might be in use in your very own portfolio. React Native has several of the most critical platform components already wrapped, like `ScrollView` and `TextInput`, but not all of them, and certainly not ones you might have written yourself for a previous app. Fortunately, we can wrap up these existing components for seamless integration with your React Native application.
Like the native module guide, this too is a more advanced guide that assumes you are somewhat familiar with Android SDK programming. This guide will show you how to build a native UI component, walking you through the implementation of a subset of the existing `ImageView` component available in the core React Native library.
info
You can also setup local library containing native component with one command. Read the guide to [Local libraries setup](https://reactnative.dev/docs/legacy/local-library-setup) for more details.
## ImageView example[​](https://reactnative.dev/docs/legacy/native-components-android#imageview-example "Direct link to ImageView example")
For this example we are going to walk through the implementation requirements to allow the use of ImageViews in JavaScript.
Native views are created and manipulated by extending `ViewManager` or more commonly `SimpleViewManager` . A `SimpleViewManager` is convenient in this case because it applies common properties such as background color, opacity, and Flexbox layout.
These subclasses are essentially singletons - only one instance of each is created by the bridge. They send native views to the `NativeViewHierarchyManager`, which delegates back to them to set and update the properties of the views as necessary. The `ViewManagers` are also typically the delegates for the views, sending events back to JavaScript via the bridge.
To send a view:
  1. Create the ViewManager subclass.
  2. Implement the `createViewInstance` method
  3. Expose view property setters using `@ReactProp` (or `@ReactPropGroup`) annotation
  4. Register the manager in `createViewManagers` of the applications package.
  5. Implement the JavaScript module


### 1. Create the `ViewManager` subclass[​](https://reactnative.dev/docs/legacy/native-components-android#1-create-the-viewmanager-subclass "Direct link to 1-create-the-viewmanager-subclass")
In this example we create view manager class `ReactImageManager` that extends `SimpleViewManager` of type `ReactImageView`. `ReactImageView` is the type of object managed by the manager, this will be the custom native view. Name returned by `getName` is used to reference the native view type from JavaScript.
  * Java
  * Kotlin


kotlin
```
classReactImageManager(privateval callerContext: ReactApplicationContext): SimpleViewManager<ReactImageView>(){overridefungetName()= REACT_CLASScompanionobject{constval REACT_CLASS ="RCTImageView"
```

java
```
publicclassReactImageManagerextendsSimpleViewManager<ReactImageView>{publicstaticfinalStringREACT_CLASS="RCTImageView";ReactApplicationContext mCallerContext;publicReactImageManager(ReactApplicationContext reactContext){  mCallerContext = reactContext;@OverridepublicStringgetName(){returnREACT_CLASS;
```

### 2. Implement method `createViewInstance`[​](https://reactnative.dev/docs/legacy/native-components-android#2-implement-method-createviewinstance "Direct link to 2-implement-method-createviewinstance")
Views are created in the `createViewInstance` method, the view should initialize itself in its default state, any properties will be set via a follow up call to `updateView.`
  * Java
  * Kotlin


kotlin
```
overridefuncreateViewInstance(context: ThemedReactContext)=ReactImageView(context, Fresco.newDraweeControllerBuilder(),null, callerContext)
```

java
```
@OverridepublicReactImageViewcreateViewInstance(ThemedReactContext context){returnnewReactImageView(context,Fresco.newDraweeControllerBuilder(),null, mCallerContext);
```

### 3. Expose view property setters using `@ReactProp` (or `@ReactPropGroup`) annotation[​](https://reactnative.dev/docs/legacy/native-components-android#3-expose-view-property-setters-using-reactprop-or-reactpropgroup-annotation "Direct link to 3-expose-view-property-setters-using-reactprop-or-reactpropgroup-annotation")
Properties that are to be reflected in JavaScript needs to be exposed as setter method annotated with `@ReactProp` (or `@ReactPropGroup`). Setter method should take view to be updated (of the current view type) as a first argument and property value as a second argument. Setter should be public and not return a value (i.e. return type should be `void` in Java or `Unit` in Kotlin). Property type sent to JS is determined automatically based on the type of value argument of the setter. The following type of values are currently supported (in Java): `boolean`, `int`, `float`, `double`, `String`, `Boolean`, `Integer`, `ReadableArray`, `ReadableMap`. The corresponding types in Kotlin are `Boolean`, `Int`, `Float`, `Double`, `String`, `ReadableArray`, `ReadableMap`.
Annotation `@ReactProp` has one obligatory argument `name` of type `String`. Name assigned to the `@ReactProp` annotation linked to the setter method is used to reference the property on JS side.
Except from `name`, `@ReactProp` annotation may take following optional arguments: `defaultBoolean`, `defaultInt`, `defaultFloat`. Those arguments should be of the corresponding type (accordingly `boolean`, `int`, `float` in Java and `Boolean`, `Int`, `Float` in Kotlin) and the value provided will be passed to the setter method in case when the property that the setter is referencing has been removed from the component. Note that "default" values are only provided for primitive types, in case when setter is of some complex type, `null` will be provided as a default value in case when corresponding property gets removed.
Setter declaration requirements for methods annotated with `@ReactPropGroup` are different than for `@ReactProp`, please refer to the `@ReactPropGroup` annotation class docs for more information about it. **IMPORTANT!** in ReactJS updating the property value will result in setter method call. Note that one of the ways we can update component is by removing properties that have been set before. In that case setter method will be called as well to notify view manager that property has changed. In that case "default" value will be provided (for primitive types "default" value can be specified using `defaultBoolean`, `defaultFloat`, etc. arguments of `@ReactProp` annotation, for complex types setter will be called with value set to `null`).
  * Java
  * Kotlin


kotlin
```
@ReactProp(name ="src")funsetSrc(view: ReactImageView, sources: ReadableArray?){  view.setSource(sources)@ReactProp(name ="borderRadius", defaultFloat =0f)overridefunsetBorderRadius(view: ReactImageView, borderRadius: Float){  view.setBorderRadius(borderRadius)@ReactProp(name = ViewProps.RESIZE_MODE)funsetResizeMode(view: ReactImageView, resizeMode: String?){  view.setScaleType(ImageResizeMode.toScaleType(resizeMode))
```

java
```
@ReactProp(name ="src")publicvoidsetSrc(ReactImageView view,@NullableReadableArray sources){  view.setSource(sources);@ReactProp(name ="borderRadius", defaultFloat =0f)publicvoidsetBorderRadius(ReactImageView view,float borderRadius){  view.setBorderRadius(borderRadius);@ReactProp(name =ViewProps.RESIZE_MODE)publicvoidsetResizeMode(ReactImageView view,@NullableString resizeMode){  view.setScaleType(ImageResizeMode.toScaleType(resizeMode));
```

### 4. Register the `ViewManager`[​](https://reactnative.dev/docs/legacy/native-components-android#4-register-the-viewmanager "Direct link to 4-register-the-viewmanager")
The final step is to register the ViewManager to the application, this happens in a similar way to [Native Modules](https://reactnative.dev/docs/legacy/native-modules-android), via the applications package member function `createViewManagers`.
  * Java
  * Kotlin


kotlin
```
overridefuncreateViewManagers(   reactContext: ReactApplicationContext)=listOf(ReactImageManager(reactContext))
```

java
```
@OverridepublicList<ViewManager>createViewManagers(ReactApplicationContext reactContext){returnArrays.<ViewManager>asList(newReactImageManager(reactContext)
```

### 5. Implement the JavaScript module[​](https://reactnative.dev/docs/legacy/native-components-android#5-implement-the-javascript-module "Direct link to 5. Implement the JavaScript module")
The very final step is to create the JavaScript module that defines the interface layer between Java/Kotlin and JavaScript for the users of your new view. It is recommended for you to document the component interface in this module (e.g. using TypeScript, Flow, or plain old comments).
ImageView.tsx
```
import{requireNativeComponent}from'react-native';/** * Composes `View`. * - src: Array<{url: string}> * - borderRadius: number * - resizeMode: 'cover' | 'contain' | 'stretch' */exportdefaultrequireNativeComponent('RCTImageView');
```

The `requireNativeComponent` function takes the name of the native view. Note that if your component needs to do anything more sophisticated (e.g. custom event handling), you should wrap the native component in another React component. This is illustrated in the `MyCustomView` example below.
## Events[​](https://reactnative.dev/docs/legacy/native-components-android#events "Direct link to Events")
So now we know how to expose native view components that we can control freely from JS, but how do we deal with events from the user, like pinch-zooms or panning? When a native event occurs the native code should issue an event to the JavaScript representation of the View, and the two views are linked with the value returned from the `getId()` method.
  * Java
  * Kotlin


kotlin
```
classMyCustomView(context: Context):View(context){...funonReceiveNativeEvent(){val event = Arguments.createMap().apply{putString("message","MyMessage")val reactContext = context as ReactContext  reactContext.getJSModule(RCTEventEmitter::class.java).receiveEvent(id,"topChange", event)
```

java
```
classMyCustomViewextendsView{...publicvoidonReceiveNativeEvent(){WritableMap event =Arguments.createMap();   event.putString("message","MyMessage");ReactContext reactContext =(ReactContext)getContext();   reactContext.getJSModule(RCTEventEmitter.class).receiveEvent(getId(),"topChange", event);
```

To map the `topChange` event name to the `onChange` callback prop in JavaScript, register it by overriding the `getExportedCustomBubblingEventTypeConstants` method in your `ViewManager`:
  * Java
  * Kotlin


kotlin
```
class ReactImageManager : SimpleViewManager<MyCustomView>(){...overridefungetExportedCustomBubblingEventTypeConstants(): Map<String, Any>{returnmapOf("topChange"tomapOf("phasedRegistrationNames"tomapOf("bubbled"to"onChange"
```

java
```
publicclassReactImageManagerextendsSimpleViewManager<MyCustomView>{...publicMapgetExportedCustomBubblingEventTypeConstants(){returnMapBuilder.builder().put("topChange",MapBuilder.of("phasedRegistrationNames",MapBuilder.of("bubbled","onChange")).build();
```

This callback is invoked with the raw event, which we typically process in the wrapper component to make a simpler API:
MyCustomView.tsx
```
import{useCallback}from'react';import{requireNativeComponent}from'react-native';constRCTMyCustomView=requireNativeComponent('RCTMyCustomView');exportdefaultfunctionMyCustomView(props:{// .../**  * Callback that is called continuously when the user is dragging the map.  */onChangeMessage:(message:string)=>unknown;}){const onChange =useCallback(  event =>{   props.onChangeMessage?.(event.nativeEvent.message);[props.onChangeMessage],return<RCTMyCustomView{...props}onChange={props.onChange}/>;
```

## Integration with an Android Fragment example[​](https://reactnative.dev/docs/legacy/native-components-android#integration-with-an-android-fragment-example "Direct link to Integration with an Android Fragment example")
In order to integrate existing Native UI elements to your React Native app, you might need to use Android Fragments to give you a more granular control over your native component than returning a `View` from your `ViewManager`. You will need this if you want to add custom logic that is tied to your view with the help of [lifecycle methods](https://developer.android.com/guide/fragments/lifecycle), such as `onViewCreated`, `onPause`, `onResume`. The following steps will show you how to do it:
### 1. Create an example custom view[​](https://reactnative.dev/docs/legacy/native-components-android#1-create-an-example-custom-view "Direct link to 1. Create an example custom view")
First, let's create a `CustomView` class which extends `FrameLayout` (the content of this view can be any view that you'd like to render)
  * Java
  * Kotlin


CustomView.kt
```
// replace with your packagepackage com.mypackageimport android.content.Contextimport android.graphics.Colorimport android.widget.FrameLayoutimport android.widget.TextViewclassCustomView(context: Context):FrameLayout(context){init{// set padding and background colorsetPadding(16,16,16,16)setBackgroundColor(Color.parseColor("#5FD3F3"))// add default text viewaddView(TextView(context).apply{   text ="Welcome to Android Fragments with React Native."
```

CustomView.java
```
// replace with your packagepackagecom.mypackage;importandroid.content.Context;importandroid.graphics.Color;importandroid.widget.FrameLayout;importandroid.widget.ImageView;importandroid.widget.TextView;importandroidx.annotation.NonNull;publicclassCustomViewextendsFrameLayout{publicCustomView(@NonNullContext context){super(context);// set padding and background colorthis.setPadding(16,16,16,16);this.setBackgroundColor(Color.parseColor("#5FD3F3"));// add default text viewTextView text =newTextView(context);  text.setText("Welcome to Android Fragments with React Native.");this.addView(text);
```

### 2. Create a `Fragment`[​](https://reactnative.dev/docs/legacy/native-components-android#2-create-a-fragment "Direct link to 2-create-a-fragment")
  * Java
  * Kotlin


MyFragment.kt
```
// replace with your packagepackage com.mypackageimport android.os.Bundleimport android.view.LayoutInflaterimport android.view.Viewimport android.view.ViewGroupimport androidx.fragment.app.Fragment// replace with your view's importimport com.mypackage.CustomViewclass MyFragment :Fragment(){privatelateinitvar customView: CustomViewoverridefunonCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {super.onCreateView(inflater, container, savedInstanceState)  customView =CustomView(requireNotNull(context))return customView // this CustomView could be any view that you want to renderoverridefunonViewCreated(view: View, savedInstanceState: Bundle?){super.onViewCreated(view, savedInstanceState)// do any logic that should happen in an `onCreate` method, e.g:// customView.onCreate(savedInstanceState);overridefunonPause(){super.onPause()// do any logic that should happen in an `onPause` method// e.g.: customView.onPause();overridefunonResume(){super.onResume()// do any logic that should happen in an `onResume` method// e.g.: customView.onResume();overridefunonDestroy(){super.onDestroy()// do any logic that should happen in an `onDestroy` method// e.g.: customView.onDestroy();
```

MyFragment.java
```
// replace with your packagepackagecom.mypackage;importandroid.os.Bundle;importandroid.view.LayoutInflater;importandroid.view.View;importandroid.view.ViewGroup;importandroidx.fragment.app.Fragment;// replace with your view's importimportcom.mypackage.CustomView;publicclassMyFragmentextendsFragment{CustomView customView;@OverridepublicViewonCreateView(LayoutInflater inflater,ViewGroup parent,Bundle savedInstanceState){super.onCreateView(inflater, parent, savedInstanceState);    customView =newCustomView(this.getContext());return customView;// this CustomView could be any view that you want to render@OverridepublicvoidonViewCreated(View view,Bundle savedInstanceState){super.onViewCreated(view, savedInstanceState);// do any logic that should happen in an `onCreate` method, e.g:// customView.onCreate(savedInstanceState);@OverridepublicvoidonPause(){super.onPause();// do any logic that should happen in an `onPause` method// e.g.: customView.onPause();@OverridepublicvoidonResume(){super.onResume();// do any logic that should happen in an `onResume` method// e.g.: customView.onResume();@OverridepublicvoidonDestroy(){super.onDestroy();// do any logic that should happen in an `onDestroy` method// e.g.: customView.onDestroy();
```

### 3. Create the `ViewManager` subclass[​](https://reactnative.dev/docs/legacy/native-components-android#3-create-the-viewmanager-subclass "Direct link to 3-create-the-viewmanager-subclass")
  * Java
  * Kotlin


MyViewManager.kt
```
// replace with your packagepackage com.mypackageimport android.view.Choreographerimport android.view.Viewimport android.view.ViewGroupimport android.widget.FrameLayoutimport androidx.fragment.app.FragmentActivityimport com.facebook.react.bridge.ReactApplicationContextimport com.facebook.react.bridge.ReadableArrayimport com.facebook.react.uimanager.ThemedReactContextimport com.facebook.react.uimanager.ViewGroupManagerimport com.facebook.react.uimanager.annotations.ReactPropGroupclassMyViewManager(privateval reactContext: ReactApplicationContext): ViewGroupManager<FrameLayout>(){privatevar propWidth: Int?=nullprivatevar propHeight: Int?=nulloverridefungetName()= REACT_CLASS/**  * Return a FrameLayout which will later hold the Fragment  */overridefuncreateViewInstance(reactContext: ThemedReactContext)=FrameLayout(reactContext)/**  * Map the "create" command to an integer  */overridefungetCommandsMap()=mapOf("create"to COMMAND_CREATE)/**  * Handle "create" command (called from JS) and call createFragment method  */overridefunreceiveCommand(   root: FrameLayout,   commandId: String,   args: ReadableArray?super.receiveCommand(root, commandId, args)val reactNativeViewId =requireNotNull(args).getInt(0)when(commandId.toInt()){   COMMAND_CREATE ->createFragment(root, reactNativeViewId)@ReactPropGroup(names =["width","height"], customType ="Style")funsetStyle(view: FrameLayout, index: Int, value: Int){if(index ==0) propWidth = valueif(index ==1) propHeight = value/**  * Replace your React Native view with a custom fragment  */funcreateFragment(root: FrameLayout, reactNativeViewId: Int){val parentView = root.findViewById<ViewGroup>(reactNativeViewId)setupLayout(parentView)val myFragment =MyFragment()val activity = reactContext.currentActivity as FragmentActivity  activity.supportFragmentManager.beginTransaction().replace(reactNativeViewId, myFragment, reactNativeViewId.toString()).commit()funsetupLayout(view: View){  Choreographer.getInstance().postFrameCallback(object: Choreographer.FrameCallback{overridefundoFrame(frameTimeNanos: Long){manuallyLayoutChildren(view)    view.viewTreeObserver.dispatchOnGlobalLayout()    Choreographer.getInstance().postFrameCallback(this)/**  * Layout all children properly  */privatefunmanuallyLayoutChildren(view: View){// propWidth and propHeight coming from react-native propsval width =requireNotNull(propWidth)val height =requireNotNull(propHeight)  view.measure(    View.MeasureSpec.makeMeasureSpec(width, View.MeasureSpec.EXACTLY),    View.MeasureSpec.makeMeasureSpec(height, View.MeasureSpec.EXACTLY))  view.layout(0,0, width, height)companionobject{privateconstval REACT_CLASS ="MyViewManager"privateconstval COMMAND_CREATE =1
```

MyViewManager.java
```
// replace with your packagepackagecom.mypackage;importandroid.view.Choreographer;importandroid.view.View;importandroid.view.ViewGroup;importandroid.widget.FrameLayout;importandroidx.annotation.NonNull;importandroidx.annotation.Nullable;importandroidx.fragment.app.FragmentActivity;importcom.facebook.react.bridge.ReactApplicationContext;importcom.facebook.react.bridge.ReadableArray;importcom.facebook.react.common.MapBuilder;importcom.facebook.react.uimanager.annotations.ReactProp;importcom.facebook.react.uimanager.annotations.ReactPropGroup;importcom.facebook.react.uimanager.ViewGroupManager;importcom.facebook.react.uimanager.ThemedReactContext;importjava.util.Map;publicclassMyViewManagerextendsViewGroupManager<FrameLayout>{publicstaticfinalStringREACT_CLASS="MyViewManager";publicfinalintCOMMAND_CREATE=1;privateint propWidth;privateint propHeight;ReactApplicationContext reactContext;publicMyViewManager(ReactApplicationContext reactContext){this.reactContext = reactContext;@OverridepublicStringgetName(){returnREACT_CLASS;/**  * Return a FrameLayout which will later hold the Fragment  */@OverridepublicFrameLayoutcreateViewInstance(ThemedReactContext reactContext){returnnewFrameLayout(reactContext);/**  * Map the "create" command to an integer  */@Nullable@OverridepublicMap<String,Integer>getCommandsMap(){returnMapBuilder.of("create",COMMAND_CREATE);/**  * Handle "create" command (called from JS) and call createFragment method  */@OverridepublicvoidreceiveCommand(@NonNullFrameLayout root,String commandId,@NullableReadableArray argssuper.receiveCommand(root, commandId, args);int reactNativeViewId = args.getInt(0);int commandIdInt =Integer.parseInt(commandId);switch(commandIdInt){caseCOMMAND_CREATE:createFragment(root, reactNativeViewId);break;default:{}@ReactPropGroup(names ={"width","height"}, customType ="Style")publicvoidsetStyle(FrameLayout view,int index,Integer value){if(index ==0){   propWidth = value;if(index ==1){   propHeight = value;/**  * Replace your React Native view with a custom fragment  */publicvoidcreateFragment(FrameLayout root,int reactNativeViewId){ViewGroup parentView =(ViewGroup) root.findViewById(reactNativeViewId);setupLayout(parentView);finalMyFragment myFragment =newMyFragment();FragmentActivity activity =(FragmentActivity) reactContext.getCurrentActivity();  activity.getSupportFragmentManager().beginTransaction().replace(reactNativeViewId, myFragment,String.valueOf(reactNativeViewId)).commit();publicvoidsetupLayout(View view){Choreographer.getInstance().postFrameCallback(newChoreographer.FrameCallback(){@OverridepublicvoiddoFrame(long frameTimeNanos){manuallyLayoutChildren(view);    view.getViewTreeObserver().dispatchOnGlobalLayout();Choreographer.getInstance().postFrameCallback(this);});/**  * Layout all children properly  */publicvoidmanuallyLayoutChildren(View view){// propWidth and propHeight coming from react-native propsint width = propWidth;int height = propHeight;   view.measure(View.MeasureSpec.makeMeasureSpec(width,View.MeasureSpec.EXACTLY),View.MeasureSpec.makeMeasureSpec(height,View.MeasureSpec.EXACTLY));   view.layout(0,0, width, height);
```

### 4. Register the `ViewManager`[​](https://reactnative.dev/docs/legacy/native-components-android#4-register-the-viewmanager-1 "Direct link to 4-register-the-viewmanager-1")
  * Java
  * Kotlin


MyPackage.kt
```
// replace with your packagepackage com.mypackageimport com.facebook.react.ReactPackageimport com.facebook.react.bridge.ReactApplicationContextimport com.facebook.react.uimanager.ViewManagerclass MyPackage : ReactPackage {...overridefuncreateViewManagers(   reactContext: ReactApplicationContext)=listOf(MyViewManager(reactContext))
```

MyPackage.java
```
// replace with your packagepackagecom.mypackage;importcom.facebook.react.ReactPackage;importcom.facebook.react.bridge.ReactApplicationContext;importcom.facebook.react.uimanager.ViewManager;importjava.util.Arrays;importjava.util.List;publicclassMyPackageimplementsReactPackage{@OverridepublicList<ViewManager>createViewManagers(ReactApplicationContext reactContext){returnArrays.<ViewManager>asList(newMyViewManager(reactContext)
```

### 5. Register the `Package`[​](https://reactnative.dev/docs/legacy/native-components-android#5-register-the-package "Direct link to 5-register-the-package")
  * Java
  * Kotlin


MainApplication.kt
```
overridefungetPackages(): List<ReactPackage>=PackageList(this).packages.apply{// Packages that cannot be autolinked yet can be added manually here, for example:// add(MyReactNativePackage())add(MyAppPackage())
```

MainApplication.java
```
@OverrideprotectedList<ReactPackage>getPackages(){List<ReactPackage> packages =newPackageList(this).getPackages();// Packages that cannot be autolinked yet can be added manually here, for example:// packages.add(new MyReactNativePackage());  packages.add(newMyAppPackage());return packages;
```

### 6. Implement the JavaScript module[​](https://reactnative.dev/docs/legacy/native-components-android#6-implement-the-javascript-module "Direct link to 6. Implement the JavaScript module")
I. Start with custom View manager:
MyViewManager.tsx
```
import{requireNativeComponent}from'react-native';exportconstMyViewManager=requireNativeComponent('MyViewManager');
```

II. Then implement custom View calling the `create` method:
MyView.tsx
```
importReact,{useEffect, useRef}from'react';import{PixelRatio,UIManager, findNodeHandle,}from'react-native';import{MyViewManager}from'./my-view-manager';constcreateFragment= viewId =>UIManager.dispatchViewManagerCommand(  viewId,// we are calling the 'create' commandUIManager.MyViewManager.Commands.create.toString(),[viewId],exportconstMyView=()=>{const ref =useRef(null);useEffect(()=>{const viewId =findNodeHandle(ref.current);createFragment(viewId);},[]);return(<MyViewManagerstyle={{// converts dpi to px, provide desired height    height:PixelRatio.getPixelSizeForLayoutSize(200),// converts dpi to px, provide desired width    width:PixelRatio.getPixelSizeForLayoutSize(200),ref={ref}/>
```

If you want to expose property setters using `@ReactProp` (or `@ReactPropGroup`) annotation see the [ImageView example](https://reactnative.dev/docs/legacy/native-components-android#imageview-example) above.
Is this page useful?
  * [ImageView example](https://reactnative.dev/docs/legacy/native-components-android#imageview-example)
    * [1. Create the `ViewManager` subclass](https://reactnative.dev/docs/legacy/native-components-android#1-create-the-viewmanager-subclass)
    * [2. Implement method `createViewInstance`](https://reactnative.dev/docs/legacy/native-components-android#2-implement-method-createviewinstance)
    * [3. Expose view property setters using `@ReactProp` (or `@ReactPropGroup`) annotation](https://reactnative.dev/docs/legacy/native-components-android#3-expose-view-property-setters-using-reactprop-or-reactpropgroup-annotation)
    * [4. Register the `ViewManager`](https://reactnative.dev/docs/legacy/native-components-android#4-register-the-viewmanager)
    * [5. Implement the JavaScript module](https://reactnative.dev/docs/legacy/native-components-android#5-implement-the-javascript-module)
  * [Integration with an Android Fragment example](https://reactnative.dev/docs/legacy/native-components-android#integration-with-an-android-fragment-example)
    * [1. Create an example custom view](https://reactnative.dev/docs/legacy/native-components-android#1-create-an-example-custom-view)
    * [2. Create a `Fragment`](https://reactnative.dev/docs/legacy/native-components-android#2-create-a-fragment)
    * [3. Create the `ViewManager` subclass](https://reactnative.dev/docs/legacy/native-components-android#3-create-the-viewmanager-subclass)
    * [4. Register the `ViewManager`](https://reactnative.dev/docs/legacy/native-components-android#4-register-the-viewmanager-1)
    * [5. Register the `Package`](https://reactnative.dev/docs/legacy/native-components-android#5-register-the-package)
    * [6. Implement the JavaScript module](https://reactnative.dev/docs/legacy/native-components-android#6-implement-the-javascript-module)



