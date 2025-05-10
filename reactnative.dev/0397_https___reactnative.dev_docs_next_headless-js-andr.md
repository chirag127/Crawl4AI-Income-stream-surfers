---
url: https://reactnative.dev/docs/next/headless-js-android
title: https://reactnative.dev/docs/next/headless-js-android
date: 2025-05-10T21:41:07.215935
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/next/headless-js-android#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
This is unreleased documentation for React Native **Next** version.
For up-to-date documentation, see the (0.79).
Version: Next
On this page
Headless JS is a way to run tasks in JavaScript while your app is in the background. It can be used, for example, to sync fresh data, handle push notifications, or play music.
## The JS API[​](https://reactnative.dev/docs/next/headless-js-android#the-js-api "Direct link to The JS API")
A task is an async function that you register on `AppRegistry`, similar to registering React applications:
tsx
```
import{AppRegistry}from'react-native';AppRegistry.registerHeadlessTask('SomeTaskName',()=>require('SomeTaskName'),
```

Then, in `SomeTaskName.js`:
tsx
```
module.exports=async taskData =>{// do stuff
```

You can do anything in your task such as network requests, timers and so on, as long as it doesn't touch UI. Once your task completes (i.e. the promise is resolved), React Native will go into "paused" mode (unless there are other tasks running, or there is a foreground app).
## The Platform API[​](https://reactnative.dev/docs/next/headless-js-android#the-platform-api "Direct link to The Platform API")
Yes, this does still require some native code, but it's pretty thin. You need to extend `HeadlessJsTaskService` and override `getTaskConfig`, e.g.:
  * Java
  * Kotlin


java
```
packagecom.your_application_name;importandroid.content.Intent;importandroid.os.Bundle;importcom.facebook.react.HeadlessJsTaskService;importcom.facebook.react.bridge.Arguments;importcom.facebook.react.jstasks.HeadlessJsTaskConfig;importjavax.annotation.Nullable;publicclassMyTaskServiceextendsHeadlessJsTaskService{@Overrideprotected@NullableHeadlessJsTaskConfiggetTaskConfig(Intent intent){Bundle extras = intent.getExtras();if(extras !=null){returnnewHeadlessJsTaskConfig("SomeTaskName",Arguments.fromBundle(extras),5000,// timeout in milliseconds for the taskfalse// optional: defines whether or not the task is allowed in foreground. Default is falsereturnnull;
```

kotlin
```
package com.your_application_name;import android.content.Intentimport com.facebook.react.HeadlessJsTaskServiceimport com.facebook.react.bridge.Argumentsimport com.facebook.react.jstasks.HeadlessJsTaskConfigclass MyTaskService :HeadlessJsTaskService(){overridefungetTaskConfig(intent: Intent?): HeadlessJsTaskConfig?{return intent.extras?.let{HeadlessJsTaskConfig("SomeTaskName",        Arguments.fromBundle(it),5000,// timeout for the taskfalse// optional: defines whether or not the task is allowed in foreground.// Default is false
```

Then add the service to your `AndroidManifest.xml` file inside the `application` tag:
xml
```
<serviceandroid:name="com.example.MyTaskService"/>
```

Now, whenever you [start your service](https://developer.android.com/reference/android/content/Context.html#startService\(android.content.Intent\)), e.g. as a periodic task or in response to some system event / broadcast, JS will spin up, run your task, then spin down.
Example:
  * Java
  * Kotlin


java
```
Intent service =newIntent(getApplicationContext(),MyTaskService.class);Bundle bundle =newBundle();bundle.putString("foo","bar");service.putExtras(bundle);getApplicationContext().startForegroundService(service);
```

kotlin
```
val service =Intent(applicationContext, MyTaskService::class.java)val bundle =Bundle()bundle.putString("foo","bar")service.putExtras(bundle)applicationContext.startForegroundService(service)
```

## Retries[​](https://reactnative.dev/docs/next/headless-js-android#retries "Direct link to Retries")
By default, the headless JS task will not perform any retries. In order to do so, you need to create a `HeadlessJsRetryPolicy` and throw a specific `Error`.
`LinearCountingRetryPolicy` is an implementation of `HeadlessJsRetryPolicy` that allows you to specify a maximum number of retries with a fixed delay between each attempt. If that does not suit your needs then you can implement your own `HeadlessJsRetryPolicy`. These policies can be passed as an extra argument to the `HeadlessJsTaskConfig` constructor, e.g.
  * Java
  * Kotlin


java
```
HeadlessJsRetryPolicy retryPolicy =newLinearCountingRetryPolicy(3,// Max number of retry attempts1000// Delay between each retry attemptreturnnewHeadlessJsTaskConfig( 'SomeTaskName',Arguments.fromBundle(extras),5000,false, retryPolicy
```

kotlin
```
val retryPolicy: HeadlessJsTaskRetryPolicy =LinearCountingRetryPolicy(3,// Max number of retry attempts1000// Delay between each retry attemptreturnHeadlessJsTaskConfig("SomeTaskName", Arguments.fromBundle(extras),5000,false, retryPolicy)
```

A retry attempt will only be made when a specific `Error` is thrown. Inside a headless JS task, you can import the error and throw it when a retry attempt is required.
Example:
tsx
```
import{HeadlessJsTaskError}from'HeadlessJsTask';module.exports=async taskData =>{const condition =...;if(!condition){thrownewHeadlessJsTaskError();
```

If you wish all errors to cause a retry attempt, you will need to catch them and throw the above error.
## Caveats[​](https://reactnative.dev/docs/next/headless-js-android#caveats "Direct link to Caveats")
  * By default, your app will crash if you try to run a task while the app is in the foreground. This is to prevent developers from shooting themselves in the foot by doing a lot of work in a task and slowing the UI. You can pass a fourth `boolean` argument to control this behaviour.
  * If you start your service from a `BroadcastReceiver`, make sure to call `HeadlessJsTaskService.acquireWakeLockNow()` before returning from `onReceive()`.


## Example Usage[​](https://reactnative.dev/docs/next/headless-js-android#example-usage "Direct link to Example Usage")
Service can be started from Java API. First you need to decide when the service should be started and implement your solution accordingly. Here is an example that reacts to network connection change.
Following lines shows part of Android manifest file for registering broadcast receiver.
xml
```
<receiverandroid:name=".NetworkChangeReceiver"><intent-filter><actionandroid:name="android.net.conn.CONNECTIVITY_CHANGE"/></intent-filter></receiver>
```

Broadcast receiver then handles intent that was broadcasted in onReceive function. This is a great place to check whether your app is on foreground or not. If app is not on foreground we can prepare our intent to be started, with no information or additional information bundled using `putExtra` (keep in mind bundle can handle only parcelable values). In the end service is started and wakelock is acquired.
  * Java
  * Kotlin


java
```
importandroid.app.ActivityManager;importandroid.content.BroadcastReceiver;importandroid.content.Context;importandroid.content.Intent;importandroid.net.ConnectivityManager;importandroid.net.Network;importandroid.net.NetworkCapabilities;importandroid.net.NetworkInfo;importandroid.os.Build;importcom.facebook.react.HeadlessJsTaskService;publicclassNetworkChangeReceiverextendsBroadcastReceiver{@OverridepublicvoidonReceive(finalContext context,finalIntent intent){/**     This part will be called every time network connection is changed     e.g. Connected -> Not Connected     **/if(!isAppOnForeground((context))){/**       We will start our service and send extra info about       network connections       **/boolean hasInternet =isNetworkAvailable(context);Intent serviceIntent =newIntent(context,MyTaskService.class);      serviceIntent.putExtra("hasInternet", hasInternet);      context.startForegroundService(serviceIntent);HeadlessJsTaskService.acquireWakeLockNow(context);privatebooleanisAppOnForeground(Context context){/**     We need to check if app is in foreground otherwise the app will crash.     https://stackoverflow.com/questions/8489993/check-android-application-is-in-foreground-or-not     **/ActivityManager activityManager =(ActivityManager) context.getSystemService(Context.ACTIVITY_SERVICE);List<ActivityManager.RunningAppProcessInfo> appProcesses =        activityManager.getRunningAppProcesses();if(appProcesses ==null){returnfalse;finalString packageName = context.getPackageName();for(ActivityManager.RunningAppProcessInfo appProcess : appProcesses){if(appProcess.importance ==ActivityManager.RunningAppProcessInfo.IMPORTANCE_FOREGROUND&&          appProcess.processName.equals(packageName)){returntrue;returnfalse;publicstaticbooleanisNetworkAvailable(Context context){ConnectivityManager cm =(ConnectivityManager)        context.getSystemService(Context.CONNECTIVITY_SERVICE);if(Build.VERSION.SDK_INT>=Build.VERSION_CODES.M){Network networkCapabilities = cm.getActiveNetwork();if(networkCapabilities ==null){returnfalse;NetworkCapabilities actNw = cm.getNetworkCapabilities(networkCapabilities);if(actNw ==null){returnfalse;if(actNw.hasTransport(NetworkCapabilities.TRANSPORT_WIFI)|| actNw.hasTransport(NetworkCapabilities.TRANSPORT_CELLULAR)|| actNw.hasTransport(NetworkCapabilities.TRANSPORT_ETHERNET)){returntrue;returnfalse;// deprecated in API level 29NetworkInfo netInfo = cm.getActiveNetworkInfo();return(netInfo !=null&& netInfo.isConnected());
```

kotlin
```
import android.app.ActivityManagerimport android.app.ActivityManager.RunningAppProcessInfoimport android.content.BroadcastReceiverimport android.content.Contextimport android.content.Intentimport android.net.ConnectivityManagerimport android.net.NetworkCapabilitiesimport android.os.Buildimport com.facebook.react.HeadlessJsTaskServiceclass NetworkChangeReceiver :BroadcastReceiver(){overridefunonReceive(context: Context, intent: Intent?){/**     * This part will be called every time network connection is changed e.g. Connected -> Not     * Connected     */if(!isAppOnForeground(context)){/** We will start our service and send extra info about network connections */val hasInternet =isNetworkAvailable(context)val serviceIntent =Intent(context, MyTaskService::class.java)      serviceIntent.putExtra("hasInternet", hasInternet)      context.startForegroundService(serviceIntent)      HeadlessJsTaskService.acquireWakeLockNow(context)privatefunisAppOnForeground(context: Context): Boolean {/**     * We need to check if app is in foreground otherwise the app will crash.     * https://stackoverflow.com/questions/8489993/check-android-application-is-in-foreground-or-not     */val activityManager = context.getSystemService(Context.ACTIVITY_SERVICE)as ActivityManagerval appProcesses = activityManager.runningAppProcesses ?:returnfalseval packageName: String = context.getPackageName()for(appProcess in appProcesses){if(appProcess.importance == RunningAppProcessInfo.IMPORTANCE_FOREGROUND &&          appProcess.processName == packageNamereturntruereturnfalsecompanionobject{funisNetworkAvailable(context: Context): Boolean {val cm = context.getSystemService(Context.CONNECTIVITY_SERVICE)as ConnectivityManagervar result =falseif(Build.VERSION.SDK_INT >= Build.VERSION_CODES.M){val networkCapabilities = cm.activeNetwork ?:returnfalseval actNw = cm.getNetworkCapabilities(networkCapabilities)?:returnfalse        result =when{            actNw.hasTransport(NetworkCapabilities.TRANSPORT_WIFI)->true            actNw.hasTransport(NetworkCapabilities.TRANSPORT_CELLULAR)->true            actNw.hasTransport(NetworkCapabilities.TRANSPORT_ETHERNET)->trueelse->falsereturn result}else{        cm.run{// deprecated in API level 29          cm.activeNetworkInfo?.run{            result =when(type){                ConnectivityManager.TYPE_WIFI ->true                ConnectivityManager.TYPE_MOBILE ->true                ConnectivityManager.TYPE_ETHERNET ->trueelse->falsereturn result
```

Is this page useful?
  * [The Platform API](https://reactnative.dev/docs/next/headless-js-android#the-platform-api)
  * [Example Usage](https://reactnative.dev/docs/next/headless-js-android#example-usage)



