---
url: https://reactnative.dev/docs/0.70/integration-with-existing-apps
title: https://reactnative.dev/docs/0.70/integration-with-existing-apps
date: 2025-05-10T21:36:20.583709
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/0.70/integration-with-existing-apps#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
This is documentation for React Native **0.70** , which is no longer in active development.
For up-to-date documentation, see the (0.79).
Version: 0.70
React Native is great when you are starting a new mobile app from scratch. However, it also works well for adding a single view or user flow to existing native applications. With a few steps, you can add new React Native based features, screens, views, etc.
The specific steps are different depending on what platform you're targeting.
  * Android (Kotlin)
  * Android (Java)
  * iOS (Objective-C)
  * iOS (Swift)


## Key Concepts[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#key-concepts "Direct link to Key Concepts")
The keys to integrating React Native components into your Android application are to:
  1. Set up React Native dependencies and directory structure.
  2. Develop your React Native components in JavaScript.
  3. Add a `ReactRootView` to your Android app. This view will serve as the container for your React Native component.
  4. Start the React Native server and run your native application.
  5. Verify that the React Native aspect of your application works as expected.


## Prerequisites[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#prerequisites "Direct link to Prerequisites")
Follow the React Native CLI Quickstart in the [environment setup guide](https://reactnative.dev/docs/0.70/environment-setup) to configure your development environment for building React Native apps for Android.
### 1. Set up directory structure[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#1-set-up-directory-structure "Direct link to 1. Set up directory structure")
To ensure a smooth experience, create a new folder for your integrated React Native project, then copy your existing Android project to an `/android` subfolder.
### 2. Install JavaScript dependencies[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#2-install-javascript-dependencies "Direct link to 2. Install JavaScript dependencies")
Go to the root directory for your project and create a new `package.json` file with the following contents:
```
"name":"MyReactNativeApp","version":"0.0.1","private":true,"scripts":{"start":"yarn react-native start"
```

Next, make sure you have [installed the yarn package manager](https://yarnpkg.com/lang/en/docs/install/).
Install the `react` and `react-native` packages. Open a terminal or command prompt, then navigate to the directory with your `package.json` file and run:
shell
```
$ yarnadd react-native
```

This will print a message similar to the following (scroll up in the yarn output to see it):
> warning "react-native@0.52.2" has unmet peer dependency "react@16.2.0".
This is OK, it means we also need to install React:
shell
```
$ yarnadd react@version_printed_above
```

Yarn has created a new `/node_modules` folder. This folder stores all the JavaScript dependencies required to build your project.
Add `node_modules/` to your `.gitignore` file.
## Adding React Native to your app[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#adding-react-native-to-your-app "Direct link to Adding React Native to your app")
### Configuring maven[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#configuring-maven "Direct link to Configuring maven")
Add the React Native and JSC dependency to your app's `build.gradle` file:
gradle
```
dependencies {  implementation "com.android.support:appcompat-v7:27.1.1"  ...  implementation "com.facebook.react:react-native:+" // From node_modules  implementation "org.webkit:android-jsc:+"
```

> If you want to ensure that you are always using a specific React Native version in your native build, replace `+` with an actual React Native version you've downloaded from `npm`.
Add an entry for the local React Native and JSC maven directories to the top-level `settings.gradle`. Be sure to add it to the “dependencyResolutionManagement” block, above other maven repositories:
gradle
```
dependencyResolutionManagement {  ...  repositories {    ...    maven {      url "$rootDir/../node_modules/react-native/android"    maven {      url("$rootDir/../node_modules/jsc-android/dist")
```

> If your project has the dependency repositories configured in the top-level `build.gradle`, be sure to add the entries to the “allprojects” block above other maven repositories:
gradle
```
allprojects {  repositories {    maven {      // All of React Native (JS, Android binaries) is installed from npm      url "$rootDir/../node_modules/react-native/android"    maven {      // Android JSC is installed from npm      url("$rootDir/../node_modules/jsc-android/dist")    ...  ...
```

> Make sure that the path is correct! You shouldn’t run into any “Failed to resolve: com.facebook.react:react-native:0.x.x" errors after running Gradle sync in Android Studio.
### Enable native modules autolinking[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#enable-native-modules-autolinking "Direct link to Enable native modules autolinking")
To use the power of [autolinking](https://github.com/react-native-community/cli/blob/master/docs/autolinking.md), we have to apply it a few places. First add the following entry to `settings.gradle`:
gradle
```
apply from: file("../node_modules/@react-native-community/cli-platform-android/native_modules.gradle"); applyNativeModulesSettingsGradle(settings)
```

Next add the following entry at the very bottom of the `app/build.gradle`:
gradle
```
apply from: file("../../node_modules/@react-native-community/cli-platform-android/native_modules.gradle"); applyNativeModulesAppBuildGradle(project)
```

### Configuring permissions[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#configuring-permissions "Direct link to Configuring permissions")
Next, make sure you have the Internet permission in your `AndroidManifest.xml`:
If you need to access to the `DevSettingsActivity` add to your `AndroidManifest.xml`:
This is only used in dev mode when reloading JavaScript from the development server, so you can strip this in release builds if you need to.
### Cleartext Traffic (API level 28+)[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#cleartext-traffic-api-level-28 "Direct link to Cleartext Traffic \(API level 28+\)")
> Starting with Android 9 (API level 28), cleartext traffic is disabled by default; this prevents your application from connecting to the [Metro bundler](https://metrobundler.dev/). The changes below allow cleartext traffic in debug builds.
#### 1. Apply the `usesCleartextTraffic` option to your Debug `AndroidManifest.xml`[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#1-apply-the-usescleartexttraffic-option-to-your-debug-androidmanifestxml "Direct link to 1-apply-the-usescleartexttraffic-option-to-your-debug-androidmanifestxml")
xml
```
<!-- ... --><applicationandroid:usesCleartextTraffic="true"tools:targetApi="28"><!-- ... --></application><!-- ... -->
```

This is not required for Release builds.
To learn more about Network Security Config and the cleartext traffic policy [see this link](https://developer.android.com/training/articles/security-config#CleartextTrafficPermitted).
### Code integration[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#code-integration "Direct link to Code integration")
Now we will actually modify the native Android application to integrate React Native.
#### The React Native component[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#the-react-native-component "Direct link to The React Native component")
The first bit of code we will write is the actual React Native code for the new "High Score" screen that will be integrated into our application.
##### 1. Create a `index.js` file[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#1-create-a-indexjs-file "Direct link to 1-create-a-indexjs-file")
First, create an empty `index.js` file in the root of your React Native project.
`index.js` is the starting point for React Native applications, and it is always required. It can be a small file that `require`s other file that are part of your React Native component or application, or it can contain all the code that is needed for it. In our case, we will put everything in `index.js`.
##### 2. Add your React Native code[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#2-add-your-react-native-code "Direct link to 2. Add your React Native code")
In your `index.js`, create your component. In our sample here, we will add a `<Text>` component within a styled `<View>`:
jsx
```
importReactfrom'react';import{AppRegistry,StyleSheet,Text,View}from'react-native';constHelloWorld=()=>{return(<Viewstyle={styles.container}><Textstyle={styles.hello}>Hello, World</Text></View>var styles =StyleSheet.create({container:{flex:1,justifyContent:'center',hello:{fontSize:20,textAlign:'center',margin:10,});AppRegistry.registerComponent('MyReactNativeApp',()=>HelloWorld,
```

##### 3. Configure permissions for development error overlay[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#3-configure-permissions-for-development-error-overlay "Direct link to 3. Configure permissions for development error overlay")
If your app is targeting the Android `API level 23` or greater, make sure you have the permission `android.permission.SYSTEM_ALERT_WINDOW` enabled for the development build. You can check this with `Settings.canDrawOverlays(this)`. This is required in dev builds because React Native development errors must be displayed above all the other windows. Due to the new permissions system introduced in the API level 23 (Android M), the user needs to approve it. This can be achieved by adding the following code to your Activity's in `onCreate()` method.
kotlin
```
companionobject{constval OVERLAY_PERMISSION_REQ_CODE =1// Choose any value...if(Build.VERSION.SDK_INT >= Build.VERSION_CODES.M){if(!Settings.canDrawOverlays(this)){val intent =Intent(Settings.ACTION_MANAGE_OVERLAY_PERMISSION,                  Uri.parse("package: $packageName"))startActivityForResult(intent, OVERLAY_PERMISSION_REQ_CODE);
```

Finally, the `onActivityResult()` method (as shown in the code below) has to be overridden to handle the permission Accepted or Denied cases for consistent UX. Also, for integrating Native Modules which use `startActivityForResult`, we need to pass the result to the `onActivityResult` method of our `ReactInstanceManager` instance.
kotlin
```
overridefunonActivityResult(requestCode: Int, resultCode: Int,data: Intent?){if(requestCode == OVERLAY_PERMISSION_REQ_CODE){if(Build.VERSION.SDK_INT >= Build.VERSION_CODES.M){if(!Settings.canDrawOverlays(this)){// SYSTEM_ALERT_WINDOW permission not granted  reactInstanceManager?.onActivityResult(this, requestCode, resultCode,data)
```

#### The Magic: `ReactRootView`[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#the-magic-reactrootview "Direct link to the-magic-reactrootview")
Let's add some native code in order to start the React Native runtime and tell it to render our JS component. To do this, we're going to create an `Activity` that creates a `ReactRootView`, starts a React application inside it and sets it as the main content view.
> If you are targeting Android version <5, use the `AppCompatActivity` class from the `com.android.support:appcompat` package instead of `Activity`.
kotlin
```
class MyReactActivity :Activity(), DefaultHardwareBackBtnHandler {privatelateinitvar reactRootView: ReactRootViewprivatelateinitvar reactInstanceManager: ReactInstanceManageroverridefunonCreate(savedInstanceState: Bundle?){super.onCreate(savedInstanceState)    SoLoader.init(this,false)    reactRootView =ReactRootView(this)val packages: List<ReactPackage>=PackageList(application).packages// Packages that cannot be autolinked yet can be added manually here, for example:// packages.add(MyReactNativePackage())// Remember to include them in `settings.gradle` and `app/build.gradle` too.    reactInstanceManager = ReactInstanceManager.builder().setApplication(application).setCurrentActivity(this).setBundleAssetName("index.android.bundle").setJSMainModulePath("index").addPackages(packages).setUseDeveloperSupport(BuildConfig.DEBUG).setInitialLifecycleState(LifecycleState.RESUMED).build()// The string here (e.g. "MyReactNativeApp") has to match// the string in AppRegistry.registerComponent() in index.js    reactRootView?.startReactApplication(reactInstanceManager,"MyReactNativeApp",null)setContentView(reactRootView)overridefuninvokeDefaultOnBackPressed(){super.onBackPressed()
```

> If you are using a starter kit for React Native, replace the "HelloWorld" string with the one in your index.js file (it’s the first argument to the `AppRegistry.registerComponent()` method).
Perform a “Sync Project files with Gradle” operation.
If you are using Android Studio, use `Alt + Enter` to add all missing imports in your MyReactActivity class. Be careful to use your package’s `BuildConfig` and not the one from the `facebook` package.
We need set the theme of `MyReactActivity` to `Theme.AppCompat.Light.NoActionBar` because some React Native UI components rely on this theme.
xml
```
<activityandroid:name=".MyReactActivity"android:label="@string/app_name"android:theme="@style/Theme.AppCompat.Light.NoActionBar"></activity>
```

> A `ReactInstanceManager` can be shared by multiple activities and/or fragments. You will want to make your own `ReactFragment` or `ReactActivity` and have a singleton _holder_ that holds a `ReactInstanceManager`. When you need the `ReactInstanceManager` (e.g., to hook up the `ReactInstanceManager` to the lifecycle of those Activities or Fragments) use the one provided by the singleton.
Next, we need to pass some activity lifecycle callbacks to the `ReactInstanceManager` and `ReactRootView`:
kotlin
```
overridefunonPause(){super.onPause()  reactInstanceManager.onHostPause(this)overridefunonResume(){super.onResume()  reactInstanceManager.onHostResume(this,this)overridefunonDestroy(){super.onDestroy()  reactInstanceManager.onHostDestroy(this)  reactRootView.unmountReactApplication()
```

We also need to pass back button events to React Native:
kotlin
```
overridefunonBackPressed(){  reactInstanceManager.onBackPressed()super.onBackPressed()
```

This allows JavaScript to control what happens when the user presses the hardware back button (e.g. to implement navigation). When JavaScript doesn't handle the back button press, your `invokeDefaultOnBackPressed` method will be called. By default this finishes your `Activity`.
Finally, we need to hook up the dev menu. By default, this is activated by (rage) shaking the device, but this is not very useful in emulators. So we make it show when you press the hardware menu button (use `Ctrl + M` if you're using Android Studio emulator):
kotlin
```
overridefunonKeyUp(keyCode: Int, event: KeyEvent?): Boolean {if(keyCode == KeyEvent.KEYCODE_MENU && reactInstanceManager !=null){    reactInstanceManager.showDevOptionsDialog()returntruereturnsuper.onKeyUp(keyCode, event)
```

Now your activity is ready to run some JavaScript code.
### Test your integration[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#test-your-integration "Direct link to Test your integration")
You have now done all the basic steps to integrate React Native with your current application. Now we will start the [Metro bundler](https://metrobundler.dev/) to build the `index.bundle` package and the server running on localhost to serve it.
##### 1. Run the packager[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#1-run-the-packager "Direct link to 1. Run the packager")
To run your app, you need to first start the development server. To do this, run the following command in the root directory of your React Native project:
shell
```
$ yarn start
```

##### 2. Run the app[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#2-run-the-app "Direct link to 2. Run the app")
Now build and run your Android app as normal.
Once you reach your React-powered activity inside the app, it should load the JavaScript code from the development server and display:
### Creating a release build in Android Studio[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#creating-a-release-build-in-android-studio "Direct link to Creating a release build in Android Studio")
You can use Android Studio to create your release builds too! It’s as quick as creating release builds of your previously-existing native Android app. There’s one additional step, which you’ll have to do before every release build. You need to execute the following to create a React Native bundle, which will be included with your native Android app:
shell
```
$ npx react-native bundle --platform android --devfalse --entry-file index.js --bundle-output android/com/your-company-name/app-package-name/src/main/assets/index.android.bundle --assets-dest android/com/your-company-name/app-package-name/src/main/res/
```

> Don’t forget to replace the paths with correct ones and create the assets folder if it doesn’t exist.
Now, create a release build of your native app from within Android Studio as usual and you should be good to go!
### Now what?[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#now-what "Direct link to Now what?")
At this point you can continue developing your app as usual. Refer to our [debugging](https://reactnative.dev/docs/0.70/debugging) and [deployment](https://reactnative.dev/docs/0.70/running-on-device) docs to learn more about working with React Native.
## Key Concepts[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#key-concepts "Direct link to Key Concepts")
The keys to integrating React Native components into your Android application are to:
  1. Set up React Native dependencies and directory structure.
  2. Develop your React Native components in JavaScript.
  3. Add a `ReactRootView` to your Android app. This view will serve as the container for your React Native component.
  4. Start the React Native server and run your native application.
  5. Verify that the React Native aspect of your application works as expected.


## Prerequisites[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#prerequisites "Direct link to Prerequisites")
Follow the React Native CLI Quickstart in the [environment setup guide](https://reactnative.dev/docs/0.70/environment-setup) to configure your development environment for building React Native apps for Android.
### 1. Set up directory structure[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#1-set-up-directory-structure "Direct link to 1. Set up directory structure")
To ensure a smooth experience, create a new folder for your integrated React Native project, then copy your existing Android project to an `/android` subfolder.
### 2. Install JavaScript dependencies[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#2-install-javascript-dependencies "Direct link to 2. Install JavaScript dependencies")
Go to the root directory for your project and create a new `package.json` file with the following contents:
```
"name":"MyReactNativeApp","version":"0.0.1","private":true,"scripts":{"start":"yarn react-native start"
```

Next, make sure you have [installed the yarn package manager](https://yarnpkg.com/lang/en/docs/install/).
Install the `react` and `react-native` packages. Open a terminal or command prompt, then navigate to the directory with your `package.json` file and run:
shell
```
$ yarnadd react-native
```

This will print a message similar to the following (scroll up in the yarn output to see it):
> warning "react-native@0.52.2" has unmet peer dependency "react@16.2.0".
This is OK, it means we also need to install React:
shell
```
$ yarnadd react@version_printed_above
```

Yarn has created a new `/node_modules` folder. This folder stores all the JavaScript dependencies required to build your project.
Add `node_modules/` to your `.gitignore` file.
## Adding React Native to your app[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#adding-react-native-to-your-app "Direct link to Adding React Native to your app")
### Configuring maven[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#configuring-maven "Direct link to Configuring maven")
Add the React Native and JSC dependency to your app's `build.gradle` file:
gradle
```
dependencies {  implementation "com.android.support:appcompat-v7:27.1.1"  ...  implementation "com.facebook.react:react-native:+" // From node_modules  implementation "org.webkit:android-jsc:+"
```

> If you want to ensure that you are always using a specific React Native version in your native build, replace `+` with an actual React Native version you've downloaded from `npm`.
Add an entry for the local React Native and JSC maven directories to the top-level `build.gradle`. Be sure to add it to the “allprojects” block, above other maven repositories:
gradle
```
allprojects {  repositories {    maven {      // All of React Native (JS, Android binaries) is installed from npm      url "$rootDir/../node_modules/react-native/android"    maven {      // Android JSC is installed from npm      url("$rootDir/../node_modules/jsc-android/dist")    ...  ...
```

> Make sure that the path is correct! You shouldn’t run into any “Failed to resolve: com.facebook.react:react-native:0.x.x" errors after running Gradle sync in Android Studio.
### Enable native modules autolinking[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#enable-native-modules-autolinking "Direct link to Enable native modules autolinking")
To use the power of [autolinking](https://github.com/react-native-community/cli/blob/master/docs/autolinking.md), we have to apply it a few places. First add the following entry to `settings.gradle`:
gradle
```
apply from: file("../node_modules/@react-native-community/cli-platform-android/native_modules.gradle"); applyNativeModulesSettingsGradle(settings)
```

Next add the following entry at the very bottom of the `app/build.gradle`:
gradle
```
apply from: file("../../node_modules/@react-native-community/cli-platform-android/native_modules.gradle"); applyNativeModulesAppBuildGradle(project)
```

### Configuring permissions[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#configuring-permissions "Direct link to Configuring permissions")
Next, make sure you have the Internet permission in your `AndroidManifest.xml`:
If you need to access to the `DevSettingsActivity` add to your `AndroidManifest.xml`:
This is only used in dev mode when reloading JavaScript from the development server, so you can strip this in release builds if you need to.
### Cleartext Traffic (API level 28+)[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#cleartext-traffic-api-level-28 "Direct link to Cleartext Traffic \(API level 28+\)")
> Starting with Android 9 (API level 28), cleartext traffic is disabled by default; this prevents your application from connecting to the [Metro bundler](https://metrobundler.dev/). The changes below allow cleartext traffic in debug builds.
#### 1. Apply the `usesCleartextTraffic` option to your Debug `AndroidManifest.xml`[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#1-apply-the-usescleartexttraffic-option-to-your-debug-androidmanifestxml "Direct link to 1-apply-the-usescleartexttraffic-option-to-your-debug-androidmanifestxml")
xml
```
<!-- ... --><applicationandroid:usesCleartextTraffic="true"tools:targetApi="28"><!-- ... --></application><!-- ... -->
```

This is not required for Release builds.
To learn more about Network Security Config and the cleartext traffic policy [see this link](https://developer.android.com/training/articles/security-config#CleartextTrafficPermitted).
### Code integration[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#code-integration "Direct link to Code integration")
Now we will actually modify the native Android application to integrate React Native.
#### The React Native component[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#the-react-native-component "Direct link to The React Native component")
The first bit of code we will write is the actual React Native code for the new "High Score" screen that will be integrated into our application.
##### 1. Create a `index.js` file[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#1-create-a-indexjs-file "Direct link to 1-create-a-indexjs-file")
First, create an empty `index.js` file in the root of your React Native project.
`index.js` is the starting point for React Native applications, and it is always required. It can be a small file that `require`s other file that are part of your React Native component or application, or it can contain all the code that is needed for it. In our case, we will put everything in `index.js`.
##### 2. Add your React Native code[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#2-add-your-react-native-code "Direct link to 2. Add your React Native code")
In your `index.js`, create your component. In our sample here, we will add a `<Text>` component within a styled `<View>`:
jsx
```
importReactfrom'react';import{AppRegistry,StyleSheet,Text,View}from'react-native';constHelloWorld=()=>{return(<Viewstyle={styles.container}><Textstyle={styles.hello}>Hello, World</Text></View>var styles =StyleSheet.create({container:{flex:1,justifyContent:'center',hello:{fontSize:20,textAlign:'center',margin:10,});AppRegistry.registerComponent('MyReactNativeApp',()=>HelloWorld,
```

##### 3. Configure permissions for development error overlay[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#3-configure-permissions-for-development-error-overlay "Direct link to 3. Configure permissions for development error overlay")
If your app is targeting the Android `API level 23` or greater, make sure you have the permission `android.permission.SYSTEM_ALERT_WINDOW` enabled for the development build. You can check this with `Settings.canDrawOverlays(this);`. This is required in dev builds because React Native development errors must be displayed above all the other windows. Due to the new permissions system introduced in the API level 23 (Android M), the user needs to approve it. This can be achieved by adding the following code to your Activity's in `onCreate()` method.
java
```
privatefinalintOVERLAY_PERMISSION_REQ_CODE=1;// Choose any value...if(Build.VERSION.SDK_INT>=Build.VERSION_CODES.M){if(!Settings.canDrawOverlays(this)){Intent intent =newIntent(Settings.ACTION_MANAGE_OVERLAY_PERMISSION,Uri.parse("package:"+getPackageName()));startActivityForResult(intent,OVERLAY_PERMISSION_REQ_CODE);
```

Finally, the `onActivityResult()` method (as shown in the code below) has to be overridden to handle the permission Accepted or Denied cases for consistent UX. Also, for integrating Native Modules which use `startActivityForResult`, we need to pass the result to the `onActivityResult` method of our `ReactInstanceManager` instance.
java
```
@OverrideprotectedvoidonActivityResult(int requestCode,int resultCode,Intent data){if(requestCode ==OVERLAY_PERMISSION_REQ_CODE){if(Build.VERSION.SDK_INT>=Build.VERSION_CODES.M){if(!Settings.canDrawOverlays(this)){// SYSTEM_ALERT_WINDOW permission not granted  mReactInstanceManager.onActivityResult(this, requestCode, resultCode, data );
```

#### The Magic: `ReactRootView`[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#the-magic-reactrootview "Direct link to the-magic-reactrootview")
Let's add some native code in order to start the React Native runtime and tell it to render our JS component. To do this, we're going to create an `Activity` that creates a `ReactRootView`, starts a React application inside it and sets it as the main content view.
> If you are targeting Android version <5, use the `AppCompatActivity` class from the `com.android.support:appcompat` package instead of `Activity`.
java
```
publicclassMyReactActivityextendsActivityimplementsDefaultHardwareBackBtnHandler{privateReactRootView mReactRootView;privateReactInstanceManager mReactInstanceManager;@OverrideprotectedvoidonCreate(Bundle savedInstanceState){super.onCreate(savedInstanceState);SoLoader.init(this,false);    mReactRootView =newReactRootView(this);List<ReactPackage> packages =newPackageList(getApplication()).getPackages();// Packages that cannot be autolinked yet can be added manually here, for example:// packages.add(new MyReactNativePackage());// Remember to include them in `settings.gradle` and `app/build.gradle` too.    mReactInstanceManager =ReactInstanceManager.builder().setApplication(getApplication()).setCurrentActivity(this).setBundleAssetName("index.android.bundle").setJSMainModulePath("index").addPackages(packages).setUseDeveloperSupport(BuildConfig.DEBUG).setInitialLifecycleState(LifecycleState.RESUMED).build();// The string here (e.g. "MyReactNativeApp") has to match// the string in AppRegistry.registerComponent() in index.js    mReactRootView.startReactApplication(mReactInstanceManager,"MyReactNativeApp",null);setContentView(mReactRootView);@OverridepublicvoidinvokeDefaultOnBackPressed(){super.onBackPressed();
```

> If you are using a starter kit for React Native, replace the "HelloWorld" string with the one in your index.js file (it’s the first argument to the `AppRegistry.registerComponent()` method).
Perform a “Sync Project files with Gradle” operation.
If you are using Android Studio, use `Alt + Enter` to add all missing imports in your MyReactActivity class. Be careful to use your package’s `BuildConfig` and not the one from the `facebook` package.
We need set the theme of `MyReactActivity` to `Theme.AppCompat.Light.NoActionBar` because some React Native UI components rely on this theme.
xml
```
<activityandroid:name=".MyReactActivity"android:label="@string/app_name"android:theme="@style/Theme.AppCompat.Light.NoActionBar"></activity>
```

> A `ReactInstanceManager` can be shared by multiple activities and/or fragments. You will want to make your own `ReactFragment` or `ReactActivity` and have a singleton _holder_ that holds a `ReactInstanceManager`. When you need the `ReactInstanceManager` (e.g., to hook up the `ReactInstanceManager` to the lifecycle of those Activities or Fragments) use the one provided by the singleton.
Next, we need to pass some activity lifecycle callbacks to the `ReactInstanceManager` and `ReactRootView`:
java
```
@OverrideprotectedvoidonPause(){super.onPause();if(mReactInstanceManager !=null){    mReactInstanceManager.onHostPause(this);@OverrideprotectedvoidonResume(){super.onResume();if(mReactInstanceManager !=null){    mReactInstanceManager.onHostResume(this,this);@OverrideprotectedvoidonDestroy(){super.onDestroy();if(mReactInstanceManager !=null){    mReactInstanceManager.onHostDestroy(this);if(mReactRootView !=null){    mReactRootView.unmountReactApplication();
```

We also need to pass back button events to React Native:
java
```
@OverridepublicvoidonBackPressed(){if(mReactInstanceManager !=null){    mReactInstanceManager.onBackPressed();}else{super.onBackPressed();
```

This allows JavaScript to control what happens when the user presses the hardware back button (e.g. to implement navigation). When JavaScript doesn't handle the back button press, your `invokeDefaultOnBackPressed` method will be called. By default this finishes your `Activity`.
Finally, we need to hook up the dev menu. By default, this is activated by (rage) shaking the device, but this is not very useful in emulators. So we make it show when you press the hardware menu button (use `Ctrl + M` if you're using Android Studio emulator):
java
```
@OverridepublicbooleanonKeyUp(int keyCode,KeyEvent event){if(keyCode ==KeyEvent.KEYCODE_MENU&& mReactInstanceManager !=null){    mReactInstanceManager.showDevOptionsDialog();returntrue;returnsuper.onKeyUp(keyCode, event);
```

Now your activity is ready to run some JavaScript code.
### Test your integration[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#test-your-integration "Direct link to Test your integration")
You have now done all the basic steps to integrate React Native with your current application. Now we will start the [Metro bundler](https://metrobundler.dev/) to build the `index.bundle` package and the server running on localhost to serve it.
##### 1. Run the packager[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#1-run-the-packager "Direct link to 1. Run the packager")
To run your app, you need to first start the development server. To do this, run the following command in the root directory of your React Native project:
shell
```
$ yarn start
```

##### 2. Run the app[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#2-run-the-app "Direct link to 2. Run the app")
Now build and run your Android app as normal.
Once you reach your React-powered activity inside the app, it should load the JavaScript code from the development server and display:
### Creating a release build in Android Studio[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#creating-a-release-build-in-android-studio "Direct link to Creating a release build in Android Studio")
You can use Android Studio to create your release builds too! It’s as quick as creating release builds of your previously-existing native Android app. There’s one additional step, which you’ll have to do before every release build. You need to execute the following to create a React Native bundle, which will be included with your native Android app:
shell
```
$ npx react-native bundle --platform android --devfalse --entry-file index.js --bundle-output android/com/your-company-name/app-package-name/src/main/assets/index.android.bundle --assets-dest android/com/your-company-name/app-package-name/src/main/res/
```

> Don’t forget to replace the paths with correct ones and create the assets folder if it doesn’t exist.
Now, create a release build of your native app from within Android Studio as usual and you should be good to go!
### Now what?[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#now-what "Direct link to Now what?")
At this point you can continue developing your app as usual. Refer to our [debugging](https://reactnative.dev/docs/0.70/debugging) and [deployment](https://reactnative.dev/docs/0.70/running-on-device) docs to learn more about working with React Native.
## Key Concepts[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#key-concepts "Direct link to Key Concepts")
The keys to integrating React Native components into your iOS application are to:
  1. Set up React Native dependencies and directory structure.
  2. Understand what React Native components you will use in your app.
  3. Add these components as dependencies using CocoaPods.
  4. Develop your React Native components in JavaScript.
  5. Add a `RCTRootView` to your iOS app. This view will serve as the container for your React Native component.
  6. Start the React Native server and run your native application.
  7. Verify that the React Native aspect of your application works as expected.


## Prerequisites[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#prerequisites "Direct link to Prerequisites")
Follow the React Native CLI Quickstart in the [environment setup guide](https://reactnative.dev/docs/0.70/environment-setup) to configure your development environment for building React Native apps for iOS.
### 1. Set up directory structure[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#1-set-up-directory-structure "Direct link to 1. Set up directory structure")
To ensure a smooth experience, create a new folder for your integrated React Native project, then copy your existing iOS project to a `/ios` subfolder.
### 2. Install JavaScript dependencies[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#2-install-javascript-dependencies "Direct link to 2. Install JavaScript dependencies")
Go to the root directory for your project and create a new `package.json` file with the following contents:
```
"name":"MyReactNativeApp","version":"0.0.1","private":true,"scripts":{"start":"yarn react-native start"
```

Next, make sure you have [installed the yarn package manager](https://yarnpkg.com/lang/en/docs/install/).
Install the `react` and `react-native` packages. Open a terminal or command prompt, then navigate to the directory with your `package.json` file and run:
  * npm
  * Yarn


shell
```
npminstall react-native
```

shell
```
yarnadd react-native
```

This will print a message similar to the following (scroll up in the yarn output to see it):
> warning "react-native@0.52.2" has unmet peer dependency "react@16.2.0".
This is OK, it means we also need to install React:
  * npm
  * Yarn


shell
```
npminstall react@version_printed_above
```

shell
```
yarnadd react@version_printed_above
```

Installation process has created a new `/node_modules` folder. This folder stores all the JavaScript dependencies required to build your project.
Add `node_modules/` to your `.gitignore` file.
### 3. Install CocoaPods[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#3-install-cocoapods "Direct link to 3. Install CocoaPods")
[CocoaPods](http://cocoapods.org) is a package management tool for iOS and macOS development. We use it to add the actual React Native framework code locally into your current project.
We recommend installing CocoaPods using [Homebrew](http://brew.sh/).
shell
```
brew install cocoapods
```

> It is technically possible not to use CocoaPods, but that would require manual library and linker additions that would overly complicate this process.
## Adding React Native to your app[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#adding-react-native-to-your-app "Direct link to Adding React Native to your app")
Assume the [app for integration](https://github.com/JoelMarcey/iOS-2048) is a [2048](https://en.wikipedia.org/wiki/2048_%28video_game%29) game. Here is what the main menu of the native application looks like without React Native.
### Command Line Tools for Xcode[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#command-line-tools-for-xcode "Direct link to Command Line Tools for Xcode")
Install the Command Line Tools. Choose "Preferences..." in the Xcode menu. Go to the Locations panel and install the tools by selecting the most recent version in the Command Line Tools dropdown.
### Configuring CocoaPods dependencies[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#configuring-cocoapods-dependencies "Direct link to Configuring CocoaPods dependencies")
Before you integrate React Native into your application, you will want to decide what parts of the React Native framework you would like to integrate. We will use CocoaPods to specify which of these "subspecs" your app will depend on.
The list of supported `subspec`s is available in [`/node_modules/react-native/React.podspec`](https://github.com/facebook/react-native/blob/0.70-stable/React.podspec). They are generally named by functionality. For example, you will generally always want the `Core` `subspec`. That will get you the `AppRegistry`, `StyleSheet`, `View` and other core React Native libraries. If you want to add the React Native `Text` library (e.g., for `<Text>` elements), then you will need the `RCTText` `subspec`. If you want the `Image` library (e.g., for `<Image>` elements), then you will need the `RCTImage` `subspec`.
You can specify which `subspec`s your app will depend on in a `Podfile` file. The easiest way to create a `Podfile` is by running the CocoaPods `init` command in the `/ios` subfolder of your project:
shell
```
pod init
```

The `Podfile` will contain a boilerplate setup that you will tweak for your integration purposes.
> The `Podfile` version changes depending on your version of `react-native`. Refer to <https://react-native-community.github.io/upgrade-helper/> for the specific version of `Podfile` you should be using.
Ultimately, your `Podfile` should look something similar to this:
```
# The target name is most likely the name of your project.target'NumberTileGame'do # Your'node_modules' directory is probably in the root of your project, # but if not, adjust the `:path` accordingly pod 'FBLazyVector',:path =>"../node_modules/react-native/Libraries/FBLazyVector" pod 'FBReactNativeSpec',:path =>"../node_modules/react-native/Libraries/FBReactNativeSpec" pod 'RCTRequired',:path =>"../node_modules/react-native/Libraries/RCTRequired" pod 'RCTTypeSafety',:path =>"../node_modules/react-native/Libraries/TypeSafety" pod 'React',:path =>'../node_modules/react-native/' pod 'React-Core',:path =>'../node_modules/react-native/' pod 'React-CoreModules',:path =>'../node_modules/react-native/React/CoreModules' pod 'React-Core/DevSupport',:path =>'../node_modules/react-native/' pod 'React-RCTActionSheet',:path =>'../node_modules/react-native/Libraries/ActionSheetIOS' pod 'React-RCTAnimation',:path =>'../node_modules/react-native/Libraries/NativeAnimation' pod 'React-RCTBlob',:path =>'../node_modules/react-native/Libraries/Blob' pod 'React-RCTImage',:path =>'../node_modules/react-native/Libraries/Image' pod 'React-RCTLinking',:path =>'../node_modules/react-native/Libraries/LinkingIOS' pod 'React-RCTNetwork',:path =>'../node_modules/react-native/Libraries/Network' pod 'React-RCTSettings',:path =>'../node_modules/react-native/Libraries/Settings' pod 'React-RCTText',:path =>'../node_modules/react-native/Libraries/Text' pod 'React-RCTVibration',:path =>'../node_modules/react-native/Libraries/Vibration' pod 'React-Core/RCTWebSocket',:path =>'../node_modules/react-native/' pod 'React-cxxreact',:path =>'../node_modules/react-native/ReactCommon/cxxreact' pod 'React-jsi',:path =>'../node_modules/react-native/ReactCommon/jsi' pod 'React-jsiexecutor',:path =>'../node_modules/react-native/ReactCommon/jsiexecutor' pod 'React-jsinspector',:path =>'../node_modules/react-native/ReactCommon/jsinspector' pod 'ReactCommon/callinvoker',:path =>"../node_modules/react-native/ReactCommon" pod 'ReactCommon/turbomodule/core',:path =>"../node_modules/react-native/ReactCommon" pod 'Yoga',:path =>'../node_modules/react-native/ReactCommon/yoga' pod 'DoubleConversion',:podspec =>'../node_modules/react-native/third-party-podspecs/DoubleConversion.podspec' pod 'glog',:podspec =>'../node_modules/react-native/third-party-podspecs/glog.podspec' pod 'Folly',:podspec =>'../node_modules/react-native/third-party-podspecs/Folly.podspec'end
```

After you have created your `Podfile`, you are ready to install the React Native pod.
shell
```
$ pod install
```

You should see output such as:
```
Analyzing dependenciesFetching podspec for`React`from`../node_modules/react-native`Downloading dependenciesInstallingReact(0.62.0)GeneratingPods projectIntegrating client projectSending statsPod installation complete!There are 3 dependencies from the Podfile and 1 total pod installed.
```

> If this fails with errors mentioning `xcrun`, make sure that in Xcode in **Preferences > Locations** the Command Line Tools are assigned.
### Code integration[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#code-integration "Direct link to Code integration")
Now we will actually modify the native iOS application to integrate React Native. For our 2048 sample app, we will add a "High Score" screen in React Native.
#### The React Native component[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#the-react-native-component "Direct link to The React Native component")
The first bit of code we will write is the actual React Native code for the new "High Score" screen that will be integrated into our application.
##### 1. Create a `index.js` file[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#1-create-a-indexjs-file "Direct link to 1-create-a-indexjs-file")
First, create an empty `index.js` file in the root of your React Native project.
`index.js` is the starting point for React Native applications, and it is always required. It can be a small file that `require`s other file that are part of your React Native component or application, or it can contain all the code that is needed for it. In our case, we will put everything in `index.js`.
##### 2. Add your React Native code[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#2-add-your-react-native-code "Direct link to 2. Add your React Native code")
In your `index.js`, create your component. In our sample here, we will add a `<Text>` component within a styled `<View>`
jsx
```
importReactfrom'react';import{AppRegistry,StyleSheet,Text,View}from'react-native';constRNHighScores=({scores})=>{const contents = scores.map(score=>(<Textkey={score.name}>{score.name}:{score.value}{'\n'}</Text>));return(<Viewstyle={styles.container}><Textstyle={styles.highScoresTitle}>    2048 High Scores!</Text><Textstyle={styles.scores}>{contents}</Text></View>const styles =StyleSheet.create({container:{flex:1,justifyContent:'center',alignItems:'center',backgroundColor:'#FFFFFF',highScoresTitle:{fontSize:20,textAlign:'center',margin:10,scores:{textAlign:'center',color:'#333333',marginBottom:5,});// Module nameAppRegistry.registerComponent('RNHighScores',()=>RNHighScores);
```

> `RNHighScores` is the name of your module that will be used when you add a view to React Native from within your iOS application.
#### The Magic: `RCTRootView`[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#the-magic-rctrootview "Direct link to the-magic-rctrootview")
Now that your React Native component is created via `index.js`, you need to add that component to a new or existing `ViewController`. The easiest path to take is to optionally create an event path to your component and then add that component to an existing `ViewController`.
We will tie our React Native component with a new native view in the `ViewController` that will actually contain it called `RCTRootView` .
##### 1. Create an Event Path[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#1-create-an-event-path "Direct link to 1. Create an Event Path")
You can add a new link on the main game menu to go to the "High Score" React Native page.
##### 2. Event Handler[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#2-event-handler "Direct link to 2. Event Handler")
We will now add an event handler from the menu link. A method will be added to the main `ViewController` of your application. This is where `RCTRootView` comes into play.
When you build a React Native application, you use the [Metro bundler](https://metrobundler.dev/) to create an `index.bundle` that will be served by the React Native server. Inside `index.bundle` will be our `RNHighScore` module. So, we need to point our `RCTRootView` to the location of the `index.bundle` resource (via `NSURL`) and tie it to the module.
We will, for debugging purposes, log that the event handler was invoked. Then, we will create a string with the location of our React Native code that exists inside the `index.bundle`. Finally, we will create the main `RCTRootView`. Notice how we provide `RNHighScores` as the `moduleName` that we created [above](https://reactnative.dev/docs/0.70/integration-with-existing-apps#the-react-native-component) when writing the code for our React Native component.
First `import` the `RCTRootView` header.
objectivec
```
#import<React/RCTRootView.h>
```

> The `initialProperties` are here for illustration purposes so we have some data for our high score screen. In our React Native component, we will use `this.props` to get access to that data.
objectivec
```
-(IBAction)highScoreButtonPressed:(id)sender {NSLog(@"High Score Button Pressed");  NSURL *jsCodeLocation =[NSURL URLWithString:@"http://localhost:8081/index.bundle?platform=ios"];  RCTRootView *rootView =[[RCTRootView alloc] initWithBundleURL: jsCodeLocation                 moduleName:@"RNHighScores"              initialProperties:@"scores":@[@"name":@"Alex",@"value":@"42"@"name":@"Joel",@"value":@"10"                launchOptions: nil];  UIViewController *vc =[[UIViewController alloc] init];  vc.view = rootView;[self presentViewController:vc animated:YES completion:nil];
```

> Note that `RCTRootView initWithBundleURL` starts up a new JSC VM. To save resources and simplify the communication between RN views in different parts of your native app, you can have multiple views powered by React Native that are associated with a single JS runtime. To do that, instead of using `[RCTRootView alloc] initWithBundleURL`, use [`RCTBridge initWithBundleURL`](https://github.com/facebook/react-native/blob/0.70-stable/React/Base/RCTBridge.h#L93) to create a bridge and then use `RCTRootView initWithBridge`.
> When moving your app to production, the `NSURL` can point to a pre-bundled file on disk via something like `[[NSBundle mainBundle] URLForResource:@"main" withExtension:@"jsbundle"];`. You can use the `react-native-xcode.sh` script in `node_modules/react-native/scripts/` to generate that pre-bundled file.
##### 3. Wire Up[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#3-wire-up "Direct link to 3. Wire Up")
Wire up the new link in the main menu to the newly added event handler method.
> One of the easier ways to do this is to open the view in the storyboard and right click on the new link. Select something such as the `Touch Up Inside` event, drag that to the storyboard and then select the created method from the list provided.
### Test your integration[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#test-your-integration "Direct link to Test your integration")
You have now done all the basic steps to integrate React Native with your current application. Now we will start the [Metro bundler](https://metrobundler.dev/) to build the `index.bundle` package and the server running on `localhost` to serve it.
##### 1. Add App Transport Security exception[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#1-add-app-transport-security-exception "Direct link to 1. Add App Transport Security exception")
Apple has blocked implicit cleartext HTTP resource loading. So we need to add the following our project's `Info.plist` (or equivalent) file.
xml
```
<key>NSAppTransportSecurity</key><dict><key>NSExceptionDomains</key><dict><key>localhost</key><dict><key>NSTemporaryExceptionAllowsInsecureHTTPLoads</key><true/></dict></dict></dict>
```

> App Transport Security is good for your users. Make sure to re-enable it prior to releasing your app for production.
##### 2. Run the packager[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#2-run-the-packager "Direct link to 2. Run the packager")
To run your app, you need to first start the development server. To do this, run the following command in the root directory of your React Native project:
  * npm
  * Yarn


shell
```
npm start
```

shell
```
yarn start
```

##### 3. Run the app[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#3-run-the-app "Direct link to 3. Run the app")
If you are using Xcode or your favorite editor, build and run your native iOS application as normal. Alternatively, you can run the app from the command line using:
```
# From the root of your project$ npx react-native run-ios
```

In our sample application, you should see the link to the "High Scores" and then when you click on that you will see the rendering of your React Native component.
Here is the _native_ application home screen:
Here is the _React Native_ high score screen:
> If you are getting module resolution issues when running your application please see [this GitHub issue](https://github.com/facebook/react-native/issues/4968) for information and possible resolution. [This comment](https://github.com/facebook/react-native/issues/4968#issuecomment-220941717) seemed to be the latest possible resolution.
### Now what?[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#now-what "Direct link to Now what?")
At this point you can continue developing your app as usual. Refer to our [debugging](https://reactnative.dev/docs/0.70/debugging) and [deployment](https://reactnative.dev/docs/0.70/running-on-device) docs to learn more about working with React Native.
## Key Concepts[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#key-concepts "Direct link to Key Concepts")
The keys to integrating React Native components into your iOS application are to:
  1. Set up React Native dependencies and directory structure.
  2. Understand what React Native components you will use in your app.
  3. Add these components as dependencies using CocoaPods.
  4. Develop your React Native components in JavaScript.
  5. Add a `RCTRootView` to your iOS app. This view will serve as the container for your React Native component.
  6. Start the React Native server and run your native application.
  7. Verify that the React Native aspect of your application works as expected.


## Prerequisites[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#prerequisites "Direct link to Prerequisites")
Follow the React Native CLI Quickstart in the [environment setup guide](https://reactnative.dev/docs/0.70/environment-setup) to configure your development environment for building React Native apps for iOS.
### 1. Set up directory structure[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#1-set-up-directory-structure "Direct link to 1. Set up directory structure")
To ensure a smooth experience, create a new folder for your integrated React Native project, then copy your existing iOS project to a `/ios` subfolder.
### 2. Install JavaScript dependencies[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#2-install-javascript-dependencies "Direct link to 2. Install JavaScript dependencies")
Go to the root directory for your project and create a new `package.json` file with the following contents:
```
"name":"MyReactNativeApp","version":"0.0.1","private":true,"scripts":{"start":"yarn react-native start"
```

Next, make sure you have [installed the yarn package manager](https://yarnpkg.com/lang/en/docs/install/).
Install the `react` and `react-native` packages. Open a terminal or command prompt, then navigate to the directory with your `package.json` file and run:
shell
```
$ yarnadd react-native
```

This will print a message similar to the following (scroll up in the yarn output to see it):
> warning "react-native@0.52.2" has unmet peer dependency "react@16.2.0".
This is OK, it means we also need to install React:
shell
```
$ yarnadd react@version_printed_above
```

Yarn has created a new `/node_modules` folder. This folder stores all the JavaScript dependencies required to build your project.
Add `node_modules/` to your `.gitignore` file.
### 3. Install CocoaPods[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#3-install-cocoapods "Direct link to 3. Install CocoaPods")
[CocoaPods](http://cocoapods.org) is a package management tool for iOS and macOS development. We use it to add the actual React Native framework code locally into your current project.
We recommend installing CocoaPods using [Homebrew](http://brew.sh/).
shell
```
$ brew install cocoapods
```

> It is technically possible not to use CocoaPods, but that would require manual library and linker additions that would overly complicate this process.
## Adding React Native to your app[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#adding-react-native-to-your-app "Direct link to Adding React Native to your app")
Assume the [app for integration](https://github.com/JoelMarcey/swift-2048) is a [2048](https://en.wikipedia.org/wiki/2048_%28video_game%29) game. Here is what the main menu of the native application looks like without React Native.
### Command Line Tools for Xcode[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#command-line-tools-for-xcode "Direct link to Command Line Tools for Xcode")
Install the Command Line Tools. Choose "Preferences..." in the Xcode menu. Go to the Locations panel and install the tools by selecting the most recent version in the Command Line Tools dropdown.
### Configuring CocoaPods dependencies[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#configuring-cocoapods-dependencies "Direct link to Configuring CocoaPods dependencies")
Before you integrate React Native into your application, you will want to decide what parts of the React Native framework you would like to integrate. We will use CocoaPods to specify which of these "subspecs" your app will depend on.
The list of supported `subspec`s is available in [`/node_modules/react-native/React.podspec`](https://github.com/facebook/react-native/blob/0.70-stable/React.podspec). They are generally named by functionality. For example, you will generally always want the `Core` `subspec`. That will get you the `AppRegistry`, `StyleSheet`, `View` and other core React Native libraries. If you want to add the React Native `Text` library (e.g., for `<Text>` elements), then you will need the `RCTText` `subspec`. If you want the `Image` library (e.g., for `<Image>` elements), then you will need the `RCTImage` `subspec`.
You can specify which `subspec`s your app will depend on in a `Podfile` file. The easiest way to create a `Podfile` is by running the CocoaPods `init` command in the `/ios` subfolder of your project:
shell
```
$ pod init
```

The `Podfile` will contain a boilerplate setup that you will tweak for your integration purposes.
> The `Podfile` version changes depending on your version of `react-native`. Refer to <https://react-native-community.github.io/upgrade-helper/> for the specific version of `Podfile` you should be using.
Ultimately, your `Podfile` should look something similar to this:
```
source 'https://github.com/CocoaPods/Specs.git'# RequiredforSwift appsplatform :ios,'8.0'use_frameworks!# The target name is most likely the name of your project.target'swift-2048'do # Your'node_modules' directory is probably in the root of your project, # but if not, adjust the `:path` accordingly pod 'React',:path =>'../node_modules/react-native',:subspecs =>['Core','CxxBridge', # IncludethisforRN>=0.47'DevSupport', # Includethis to enable In-AppDevmenuifRN>=0.43'RCTText','RCTNetwork','RCTWebSocket', # needed for debugging  # Addany other subspecs you want to use in your project # Explicitly include Yogaif you are using RN>=0.42.0 pod "Yoga",:path =>"../node_modules/react-native/ReactCommon/yoga" # Third party deps podspec link pod 'DoubleConversion',:podspec =>'../node_modules/react-native/third-party-podspecs/DoubleConversion.podspec' pod 'glog',:podspec =>'../node_modules/react-native/third-party-podspecs/glog.podspec' pod 'Folly',:podspec =>'../node_modules/react-native/third-party-podspecs/Folly.podspec'end
```

After you have created your `Podfile`, you are ready to install the React Native pod.
shell
```
$ pod install
```

You should see output such as:
```
Analyzing dependenciesFetching podspec for`React`from`../node_modules/react-native`Downloading dependenciesInstallingReact(0.62.0)GeneratingPods projectIntegrating client projectSending statsPod installation complete!There are 3 dependencies from the Podfile and 1 total pod installed.
```

> If this fails with errors mentioning `xcrun`, make sure that in Xcode in **Preferences > Locations** the Command Line Tools are assigned.
> If you get a warning such as "_The`swift-2048 [Debug]` target overrides the `FRAMEWORK_SEARCH_PATHS` build setting defined in `Pods/Target Support Files/Pods-swift-2048/Pods-swift-2048.debug.xcconfig`. This can lead to problems with the CocoaPods installation_", then make sure the `Framework Search Paths` in `Build Settings` for both `Debug` and `Release` only contain `$(inherited)`.
### Code integration[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#code-integration "Direct link to Code integration")
Now we will actually modify the native iOS application to integrate React Native. For our 2048 sample app, we will add a "High Score" screen in React Native.
#### The React Native component[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#the-react-native-component "Direct link to The React Native component")
The first bit of code we will write is the actual React Native code for the new "High Score" screen that will be integrated into our application.
##### 1. Create a `index.js` file[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#1-create-a-indexjs-file "Direct link to 1-create-a-indexjs-file")
First, create an empty `index.js` file in the root of your React Native project.
`index.js` is the starting point for React Native applications, and it is always required. It can be a small file that `require`s other file that are part of your React Native component or application, or it can contain all the code that is needed for it. In our case, we will put everything in `index.js`.
##### 2. Add your React Native code[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#2-add-your-react-native-code "Direct link to 2. Add your React Native code")
In your `index.js`, create your component. In our sample here, we will add a `<Text>` component within a styled `<View>`
jsx
```
importReactfrom'react';import{AppRegistry,StyleSheet,Text,View}from'react-native';constRNHighScores=({scores})=>{const contents = scores.map(score=>(<Textkey={score.name}>{score.name}:{score.value}{'\n'}</Text>));return(<Viewstyle={styles.container}><Textstyle={styles.highScoresTitle}>    2048 High Scores!</Text><Textstyle={styles.scores}>{contents}</Text></View>const styles =StyleSheet.create({container:{flex:1,justifyContent:'center',alignItems:'center',backgroundColor:'#FFFFFF',highScoresTitle:{fontSize:20,textAlign:'center',margin:10,scores:{textAlign:'center',color:'#333333',marginBottom:5,});// Module nameAppRegistry.registerComponent('RNHighScores',()=>RNHighScores);
```

> `RNHighScores` is the name of your module that will be used when you add a view to React Native from within your iOS application.
#### The Magic: `RCTRootView`[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#the-magic-rctrootview "Direct link to the-magic-rctrootview")
Now that your React Native component is created via `index.js`, you need to add that component to a new or existing `ViewController`. The easiest path to take is to optionally create an event path to your component and then add that component to an existing `ViewController`.
We will tie our React Native component with a new native view in the `ViewController` that will actually contain it called `RCTRootView` .
##### 1. Create an Event Path[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#1-create-an-event-path "Direct link to 1. Create an Event Path")
You can add a new link on the main game menu to go to the "High Score" React Native page.
##### 2. Event Handler[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#2-event-handler "Direct link to 2. Event Handler")
We will now add an event handler from the menu link. A method will be added to the main `ViewController` of your application. This is where `RCTRootView` comes into play.
When you build a React Native application, you use the [Metro bundler](https://metrobundler.dev/) to create an `index.bundle` that will be served by the React Native server. Inside `index.bundle` will be our `RNHighScore` module. So, we need to point our `RCTRootView` to the location of the `index.bundle` resource (via `NSURL`) and tie it to the module.
We will, for debugging purposes, log that the event handler was invoked. Then, we will create a string with the location of our React Native code that exists inside the `index.bundle`. Finally, we will create the main `RCTRootView`. Notice how we provide `RNHighScores` as the `moduleName` that we created [above](https://reactnative.dev/docs/0.70/integration-with-existing-apps#the-react-native-component) when writing the code for our React Native component.
First `import` the `React` library.
jsx
```
importReact
```

> The `initialProperties` are here for illustration purposes so we have some data for our high score screen. In our React Native component, we will use `this.props` to get access to that data.
swift
```
@IBActionfunchighScoreButtonTapped(sender :UIButton){NSLog("Hello")let jsCodeLocation =URL(string:"http://localhost:8081/index.bundle?platform=ios")let mockData:NSDictionary=["scores":["name":"Alex","value":"42"],["name":"Joel","value":"10"]let rootView =RCTRootView(   bundleURL: jsCodeLocation,   moduleName:"RNHighScores",   initialProperties: mockData as[NSObject:AnyObject],   launchOptions:nillet vc =UIViewController() vc.view = rootViewself.present(vc, animated:true, completion:nil)
```

> Note that `RCTRootView bundleURL` starts up a new JSC VM. To save resources and simplify the communication between RN views in different parts of your native app, you can have multiple views powered by React Native that are associated with a single JS runtime. To do that, instead of using `RCTRootView bundleURL`, use [`RCTBridge initWithBundleURL`](https://github.com/facebook/react-native/blob/0.70-stable/React/Base/RCTBridge.h#L89) to create a bridge and then use `RCTRootView initWithBridge`.
> When moving your app to production, the `NSURL` can point to a pre-bundled file on disk via something like `let mainBundle = NSBundle(URLForResource: "main" withExtension:"jsbundle")`. You can use the `react-native-xcode.sh` script in `node_modules/react-native/scripts/` to generate that pre-bundled file.
##### 3. Wire Up[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#3-wire-up "Direct link to 3. Wire Up")
Wire up the new link in the main menu to the newly added event handler method.
> One of the easier ways to do this is to open the view in the storyboard and right click on the new link. Select something such as the `Touch Up Inside` event, drag that to the storyboard and then select the created method from the list provided.
### Test your integration[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#test-your-integration "Direct link to Test your integration")
You have now done all the basic steps to integrate React Native with your current application. Now we will start the [Metro bundler](https://metrobundler.dev/) to build the `index.bundle` package and the server running on `localhost` to serve it.
##### 1. Add App Transport Security exception[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#1-add-app-transport-security-exception "Direct link to 1. Add App Transport Security exception")
Apple has blocked implicit cleartext HTTP resource loading. So we need to add the following our project's `Info.plist` (or equivalent) file.
xml
```
<key>NSAppTransportSecurity</key><dict><key>NSExceptionDomains</key><dict><key>localhost</key><dict><key>NSTemporaryExceptionAllowsInsecureHTTPLoads</key><true/></dict></dict></dict>
```

> App Transport Security is good for your users. Make sure to re-enable it prior to releasing your app for production.
##### 2. Run the packager[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#2-run-the-packager "Direct link to 2. Run the packager")
To run your app, you need to first start the development server. To do this, run the following command in the root directory of your React Native project:
shell
```
$ npm start
```

##### 3. Run the app[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#3-run-the-app "Direct link to 3. Run the app")
If you are using Xcode or your favorite editor, build and run your native iOS application as normal. Alternatively, you can run the app from the command line using:
```
# From the root of your project$ npx react-native run-ios
```

In our sample application, you should see the link to the "High Scores" and then when you click on that you will see the rendering of your React Native component.
Here is the _native_ application home screen:
Here is the _React Native_ high score screen:
> If you are getting module resolution issues when running your application please see [this GitHub issue](https://github.com/facebook/react-native/issues/4968) for information and possible resolution. [This comment](https://github.com/facebook/react-native/issues/4968#issuecomment-220941717) seemed to be the latest possible resolution.
### Now what?[​](https://reactnative.dev/docs/0.70/integration-with-existing-apps#now-what "Direct link to Now what?")
At this point you can continue developing your app as usual. Refer to our [debugging](https://reactnative.dev/docs/0.70/debugging) and [deployment](https://reactnative.dev/docs/0.70/running-on-device) docs to learn more about working with React Native.
Is this page useful?

