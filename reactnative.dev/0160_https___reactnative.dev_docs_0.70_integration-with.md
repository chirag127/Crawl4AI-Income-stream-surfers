---
url: https://reactnative.dev/docs/0.70/integration-with-android-fragment
title: https://reactnative.dev/docs/0.70/integration-with-android-fragment
date: 2025-05-10T21:35:57.150366
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/0.70/integration-with-android-fragment#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
This is documentation for React Native **0.70** , which is no longer in active development.
For up-to-date documentation, see the (0.79).
Version: 0.70
On this page
The guide for [Integration with Existing Apps](https://reactnative.dev/docs/integration-with-existing-apps) details how to integrate a full-screen React Native app into an existing Android app as an Activity. To use React Native components within Fragments in an existing app requires some additional setup. The benefit of this is that it allows for a native app to integrate React Native components alongside native fragments in an Activity.
### 1. Add React Native to your app[​](https://reactnative.dev/docs/0.70/integration-with-android-fragment#1-add-react-native-to-your-app "Direct link to 1. Add React Native to your app")
Follow the guide for [Integration with Existing Apps](https://reactnative.dev/docs/integration-with-existing-apps) until the Code integration section. Continue to follow Step 1. Create an `index.android.js` file and Step 2. Add your React Native code from this section.
### 2. Integrating your App with a React Native Fragment[​](https://reactnative.dev/docs/0.70/integration-with-android-fragment#2-integrating-your-app-with-a-react-native-fragment "Direct link to 2. Integrating your App with a React Native Fragment")
You can render your React Native component into a Fragment instead of a full screen React Native Activity. The component may be termed a "screen" or "fragment" and it will function in the same manner as an Android fragment, likely containing child components. These components can be placed in a `/fragments` folder and the child components used to compose the fragment can be placed in a `/components` folder.
You will need to implement the `ReactApplication` interface in your main Application Java/Kotlin class. If you have created a new project from Android Studio with a default activity, you will need to create a new class (e.g. `MyReactApplication.java` or `MyReactApplication.kt`). If it is an existing class you can find this main class in your `AndroidManifest.xml` file. Under the `<application />` tag you should see a property `android:name` e.g. `android:name=".MyReactApplication"`. This value is the class you want to implement and provide the required methods to.
Ensure your main Application class implements ReactApplication:
  * Java
  * Kotlin


kotlin
```
class MyReactApplication:Application(), ReactApplication {...}
```

java
```
publicclassMyReactApplicationextendsApplicationimplementsReactApplication{...}
```

Override the required methods `getUseDeveloperSupport`, `getPackages` and `getReactNativeHost`:
  * Java
  * Kotlin


kotlin
```
class MyReactApplication :Application(), ReactApplication {overridefunonCreate(){super.onCreate()    SoLoader.init(this,false)privateval reactNativeHost =object:ReactNativeHost(this){overridefungetUseDeveloperSupport()= BuildConfig.DEBUGoverridefungetPackages(): List<ReactPackage>{val packages =PackageList(this).getPackages().toMutableList()// Packages that cannot be autolinked yet can be added manually herereturn packagesoverridefungetReactNativeHost(): ReactNativeHost = reactNativeHost
```

java
```
publicclassMyReactApplicationextendsApplicationimplementsReactApplication{@OverridepublicvoidonCreate(){super.onCreate();SoLoader.init(this,false);privatefinalReactNativeHost mReactNativeHost =newReactNativeHost(this){@OverridepublicbooleangetUseDeveloperSupport(){returnBuildConfig.DEBUG;protectedList<ReactPackage>getPackages(){List<ReactPackage> packages =newPackageList(this).getPackages();// Packages that cannot be autolinked yet can be added manually herereturn packages;@OverridepublicReactNativeHostgetReactNativeHost(){return mReactNativeHost;
```

If you are using Android Studio, use Alt + Enter to add all missing imports in your class. Alternatively these are the required imports to include manually:
  * Java
  * Kotlin


kotlin
```
import android.app.Applicationimport com.facebook.react.PackageListimport com.facebook.react.ReactApplicationimport com.facebook.react.ReactNativeHostimport com.facebook.react.ReactPackageimport com.facebook.soloader.SoLoader
```

java
```
importandroid.app.Application;importcom.facebook.react.PackageList;importcom.facebook.react.ReactApplication;importcom.facebook.react.ReactNativeHost;importcom.facebook.react.ReactPackage;importcom.facebook.soloader.SoLoader;importjava.util.List;
```

Perform a "Sync Project files with Gradle" operation.
### Step 3. Add a FrameLayout for the React Native Fragment[​](https://reactnative.dev/docs/0.70/integration-with-android-fragment#step-3-add-a-framelayout-for-the-react-native-fragment "Direct link to Step 3. Add a FrameLayout for the React Native Fragment")
You will now add your React Native Fragment to an Activity. For a new project this Activity will be `MainActivity` but it could be any Activity and more fragments can be added to additional Activities as you integrate more React Native components into your app.
First add the React Native Fragment to your Activity's layout. For example `main_activity.xml` in the `res/layouts` folder.
Add a `<FrameLayout>` with an id, width and height. This is the layout you will find and render your React Native Fragment into.
xml
```
<FrameLayoutxmlns:android="http://schemas.android.com/apk/res/android"android:id="@+id/reactNativeFragment"android:layout_width="match_parent"android:layout_height="match_parent"/>
```

### Step 4. Add a React Native Fragment to the FrameLayout[​](https://reactnative.dev/docs/0.70/integration-with-android-fragment#step-4-add-a-react-native-fragment-to-the-framelayout "Direct link to Step 4. Add a React Native Fragment to the FrameLayout")
To add your React Native Fragment to your layout you need to have an Activity. As mentioned in a new project this will be `MainActivity`. In this Activity add a button and an event listener. On button click you will render your React Native Fragment.
Modify your Activity layout to add the button:
xml
```
<Buttonandroid:layout_margin="10dp"android:id="@+id/button"android:layout_width="match_parent"android:layout_height="wrap_content"android:text="Show react fragment"/>
```

Now in your Activity class (e.g. `MainActivity.java` or `MainActivity.kt`) you need to add an `OnClickListener` for the button, instantiate your `ReactFragment` and add it to the frame layout.
Add the button field to the top of your Activity:
  * Java
  * Kotlin


kotlin
```
privatelateinitvar button: Button
```

java
```
privateButton mButton;
```

Update your Activity's `onCreate` method as follows:
  * Java
  * Kotlin


kotlin
```
overridefunonCreate(savedInstanceState: Bundle){super.onCreate(savedInstanceState)setContentView(R.layout.main_activity)  button = findViewById<Button>(R.id.button)  button.setOnClickListener{val reactNativeFragment = ReactFragment.Builder().setComponentName("HelloWorld").setLaunchOptions(getLaunchOptions("test message")).build()getSupportFragmentManager().beginTransaction().add(R.id.reactNativeFragment, reactNativeFragment).commit()
```

java
```
@OverrideprotectedvoidonCreate(Bundle savedInstanceState){super.onCreate(savedInstanceState);setContentView(R.layout.main_activity);  mButton =findViewById(R.id.button);  mButton.setOnClickListener(newView.OnClickListener(){publicvoidonClick(View v){Fragment reactNativeFragment =newReactFragment.Builder().setComponentName("HelloWorld").setLaunchOptions(getLaunchOptions("test message")).build();getSupportFragmentManager().beginTransaction().add(R.id.reactNativeFragment, reactNativeFragment).commit();});
```

In the code above `Fragment reactNativeFragment = new ReactFragment.Builder()` creates the ReactFragment and `getSupportFragmentManager().beginTransaction().add()` adds the Fragment to the Frame Layout.
If you are using a starter kit for React Native, replace the "HelloWorld" string with the one in your `index.js` or `index.android.js` file (it’s the first argument to the AppRegistry.registerComponent() method).
Add the `getLaunchOptions` method which will allow you to pass props through to your component. This is optional and you can remove `setLaunchOptions` if you don't need to pass any props.
  * Java
  * Kotlin


kotlin
```
privatefungetLaunchOptions(message: String)=Bundle().apply{putString("message", message)
```

java
```
privateBundlegetLaunchOptions(String message){Bundle initialProperties =newBundle();  initialProperties.putString("message", message);return initialProperties;
```

Add all missing imports in your Activity class. Be careful to use your package’s BuildConfig and not the one from the facebook package! Alternatively these are the required imports to include manually:
  * Java
  * Kotlin


kotlin
```
import android.app.Applicationimport com.facebook.react.ReactApplicationimport com.facebook.react.ReactNativeHostimport com.facebook.react.ReactPackageimport com.facebook.react.shell.MainReactPackageimport com.facebook.soloader.SoLoader
```

java
```
importandroid.app.Application;importcom.facebook.react.ReactApplication;importcom.facebook.react.ReactNativeHost;importcom.facebook.react.ReactPackage;importcom.facebook.react.shell.MainReactPackage;importcom.facebook.soloader.SoLoader;
```

Perform a "Sync Project files with Gradle" operation.
### Step 5. Test your integration[​](https://reactnative.dev/docs/0.70/integration-with-android-fragment#step-5-test-your-integration "Direct link to Step 5. Test your integration")
Make sure you run `yarn` to install your react-native dependencies and run `yarn native` to start the metro bundler. Run your android app in Android Studio and it should load the JavaScript code from the development server and display it in your React Native Fragment in the Activity.
### Step 6. Additional setup - Native modules[​](https://reactnative.dev/docs/0.70/integration-with-android-fragment#step-6-additional-setup---native-modules "Direct link to Step 6. Additional setup - Native modules")
You may need to call out to existing Java/Kotlin code from your react component. Native modules allow you to call out to native code and run methods in your native app. Follow the setup here [native-modules-android](https://reactnative.dev/docs/0.70/native-modules-android)
Is this page useful?
  * [1. Add React Native to your app](https://reactnative.dev/docs/0.70/integration-with-android-fragment#1-add-react-native-to-your-app)
  * [2. Integrating your App with a React Native Fragment](https://reactnative.dev/docs/0.70/integration-with-android-fragment#2-integrating-your-app-with-a-react-native-fragment)
  * [Step 3. Add a FrameLayout for the React Native Fragment](https://reactnative.dev/docs/0.70/integration-with-android-fragment#step-3-add-a-framelayout-for-the-react-native-fragment)
  * [Step 4. Add a React Native Fragment to the FrameLayout](https://reactnative.dev/docs/0.70/integration-with-android-fragment#step-4-add-a-react-native-fragment-to-the-framelayout)
  * [Step 5. Test your integration](https://reactnative.dev/docs/0.70/integration-with-android-fragment#step-5-test-your-integration)
  * [Step 6. Additional setup - Native modules](https://reactnative.dev/docs/0.70/integration-with-android-fragment#step-6-additional-setup---native-modules)



