---
url: https://reactnative.dev/docs/next/debugging-native-code
title: https://reactnative.dev/docs/next/debugging-native-code
date: 2025-05-10T21:41:08.775980
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/next/debugging-native-code#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
This is unreleased documentation for React Native **Next** version.
For up-to-date documentation, see the (0.79).
Version: Next
On this page
### Projects with Native Code Only
The following section only applies to projects with native code exposed. If you are using the managed Expo workflow, see the guide on [prebuild](https://docs.expo.dev/workflow/prebuild/) to use this API.
## Accessing Logs[​](https://reactnative.dev/docs/next/debugging-native-code#accessing-logs "Direct link to Accessing Logs")
You can display the native logs for an iOS or Android app by using the following commands in a terminal while the app is running:
shell
```
# For Android:npx react-native log-android# Or, for iOS:npx react-native log-ios
```

You may also access these through Debug > Open System Log… in the iOS Simulator or by running `adb logcat "*:S" ReactNative:V ReactNativeJS:V` in a terminal while an Android app is running on a device or emulator.
**💡 Custom Native Logs**
If you are writing a Native Module and want to add custom logs to your module for debugging purposes, you can use the following method:
#### Android (Java/Kotlin)[​](https://reactnative.dev/docs/next/debugging-native-code#android-javakotlin "Direct link to Android \(Java/Kotlin\)")
In your native module, use the `Log` class to add logs that can be viewed in Logcat:
java
```
importandroid.util.Log;privatevoidlog(String message){Log.d("YourModuleName", message);
```

To view these logs in Logcat, use this command, replacing `YourModuleName` with your custom tag:
shell
```
adb logcat "*:S" ReactNative:V ReactNativeJS:V YourModuleName:D
```

#### iOS (Objective-C/Swift)[​](https://reactnative.dev/docs/next/debugging-native-code#ios-objective-cswift "Direct link to iOS \(Objective-C/Swift\)")
In your native module, use `NSLog` for custom logs:
objective-c
```
NSLog(@"YourModuleName: %@", message);
```

Or, in Swift:
swift
```
print("YourModuleName: \(message)")
```

These logs will appear in the Xcode console when running the app.
## Debugging in a Native IDE[​](https://reactnative.dev/docs/next/debugging-native-code#debugging-in-a-native-ide "Direct link to Debugging in a Native IDE")
When working with native code, such as when writing native modules, you can launch the app from Android Studio or Xcode and take advantage of the native debugging features (setting up breakpoints, etc.) as you would in case of building a standard native app.
Another option is to run your application using the React Native CLI and attach the native debugger of the native IDE (Android Studio or Xcode) to the process.
### Android Studio[​](https://reactnative.dev/docs/next/debugging-native-code#android-studio "Direct link to Android Studio")
On Android Studio you can do this by going on the "Run" option on the menu bar, clicking on "Attach to Process..." and selecting the running React Native app.
### Xcode[​](https://reactnative.dev/docs/next/debugging-native-code#xcode "Direct link to Xcode")
On Xcode click on "Debug" on the top menu bar, select the "Attach to process" option, and select the application in the list of "Likely Targets".
Is this page useful?
  * [Accessing Logs](https://reactnative.dev/docs/next/debugging-native-code#accessing-logs)
  * [Debugging in a Native IDE](https://reactnative.dev/docs/next/debugging-native-code#debugging-in-a-native-ide)
    * [Android Studio](https://reactnative.dev/docs/next/debugging-native-code#android-studio)



