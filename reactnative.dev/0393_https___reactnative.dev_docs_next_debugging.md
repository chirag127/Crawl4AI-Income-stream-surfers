---
url: https://reactnative.dev/docs/next/debugging
title: https://reactnative.dev/docs/next/debugging
date: 2025-05-10T21:41:01.608822
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/next/debugging#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
This is unreleased documentation for React Native **Next** version.
For up-to-date documentation, see the **[latest version](https://reactnative.dev/docs/debugging)** (0.79).
Version: Next
On this page
note
Debugging features, such as the Dev Menu, LogBox, and React Native DevTools are disabled in release (production) builds.
## Opening the Dev Menu[​](https://reactnative.dev/docs/next/debugging#opening-the-dev-menu "Direct link to Opening the Dev Menu")
React Native provides an in-app developer menu providing access to debugging features. You can access the Dev Menu by shaking your device or via keyboard shortcuts:
  * iOS Simulator: `Ctrl` + `Cmd ⌘` + `Z` (or Device > Shake)
  * Android emulators: `Cmd ⌘` + `M` (macOS) or `Ctrl` + `M` (Windows and Linux)


Alternative (Android): `adb shell input keyevent 82`.
## Opening DevTools[​](https://reactnative.dev/docs/next/debugging#opening-devtools "Direct link to Opening DevTools")
[React Native DevTools](https://reactnative.dev/docs/next/react-native-devtools) is our built-in debugger for React Native. It allows you to inspect and understand how your JavaScript code is running, similar to a web browser.
To open DevTools, either:
  * Select "Open DevTools" in the Dev Menu.
  * Press `j` from the CLI (`npx react-native start`).


On first launch, DevTools will open to a welcome panel, along with an open console drawer where you can view logs and interact with the JavaScript runtime. From the top of the window, you can navigate to other panels, including the integrated React Components Inspector and Profiler.
React Native DevTools is powered by a dedicated debugging architecture built into React Native and uses a customized build of the [Chrome DevTools](https://developer.chrome.com/docs/devtools) frontend. This enables us to offer familiar, browser-aligned debugging features that are deeply integrated and built for end-to-end reliability.
Learn more in our [React Native DevTools guide](https://reactnative.dev/docs/next/react-native-devtools).
note
React Native DevTools is only available with the Hermes engine, and requires either Google Chrome or Microsoft Edge installed.
info
#### Flipper and alternative debugging tools[​](https://reactnative.dev/docs/next/debugging#flipper-and-alternative-debugging-tools "Direct link to Flipper and alternative debugging tools")
React Native DevTools replaces the previous Flipper, Experimental Debugger, and Hermes debugger (Chrome) frontends. If you are on an older version of React Native, please go to the docs [for your version](https://reactnative.dev/versions).
For apps using JavaScriptCore instead of Hermes, Direct JSC Debugging is still available (see [Other Debugging Methods](https://reactnative.dev/docs/next/other-debugging-methods)).
React Native DevTools is designed for debugging React app concerns, and not to replace native tools. If you want to inspect React Native’s underlying platform layers (for example, while developing a Native Module), please use the debugging tools available in Xcode and Android Studio (see [Debugging Native Code](https://reactnative.dev/docs/next/debugging-native-code)).
Other useful links:
  * [Why you don’t need Flipper in your React Native app … and how to get by without it ↗](https://shift.infinite.red/why-you-dont-need-flipper-in-your-react-native-app-and-how-to-get-by-without-it-3af461955109)


## LogBox[​](https://reactnative.dev/docs/next/debugging#logbox "Direct link to LogBox")
LogBox is an in-app tool that displays when warnings or errors are logged by your app.
### Fatal Errors[​](https://reactnative.dev/docs/next/debugging#fatal-errors "Direct link to Fatal Errors")
When an unrecoverable error occurs, such as a JavaScript syntax error, LogBox will open with the location of the error. In this state, LogBox is not dismissable since your code cannot be executed. LogBox will automatically dismiss once the syntax error is fixed — either via Fast Refresh or after a manual reload.
### Console Errors and Warnings[​](https://reactnative.dev/docs/next/debugging#console-errors-and-warnings "Direct link to Console Errors and Warnings")
Console errors and warnings are displayed as on-screen notifications with a red or yellow badge.
  * **Errors** will display with a notification count. Tap the notification to see an expanded view and to paginate through other logs.
  * **Warnings** will display a notification banner without details, prompting you to open React Native DevTools.


When React Native DevTools is open, all errors except fatal errors will be hidden to LogBox. We recommend using the Console panel within React Native DevTools as a source of truth, due to various LogBox options which can hide or adjust the level of certain logs.
**💡 Ignoring logs**
LogBox can be configured via the `LogBox` API.
js
```
import{LogBox}from'react-native';
```

#### Ignore all logs[​](https://reactnative.dev/docs/next/debugging#ignore-all-logs "Direct link to Ignore all logs")
LogBox notifications can be disabled using `LogBox.ignoreAllLogs()`. This can be useful in situations such as giving product demos.
js
```
LogBox.ignoreAllLogs();
```

#### Ignore specific logs[​](https://reactnative.dev/docs/next/debugging#ignore-specific-logs "Direct link to Ignore specific logs")
Notifications can be disabled on a per-log basis via `LogBox.ignoreLogs()`. This can be useful for noisy warnings or those that cannot be fixed, e.g. in a third-party dependency.
js
```
LogBox.ignoreLogs([// Exact message'Warning: componentWillReceiveProps has been renamed',// Substring or regex match/GraphQL error:.*/,]);
```

note
LogBox will treat certain errors from React as warnings, which will mean they don't display as an in-app error notification. Advanced users can change this behaviour by customising LogBox's warning filter using [`LogBoxData.setWarningFilter()`](https://github.com/facebook/react-native/blob/d334f4d77eea538dff87fdcf2ebc090246cfdbb0/packages/react-native/Libraries/LogBox/Data/LogBoxData.js#L338).
## Performance Monitor[​](https://reactnative.dev/docs/next/debugging#performance-monitor "Direct link to Performance Monitor")
On Android and iOS, an in-app performance overlay can be toggled during development by selecting **"Perf Monitor"** in the Dev Menu. Learn more about this feature [here](https://reactnative.dev/docs/performance).
info
The Performance Monitor runs in-app and is a guide. We recommend investigating the native tooling under Android Studio and Xcode for accurate performance measurements.
Is this page useful?
  * [Opening the Dev Menu](https://reactnative.dev/docs/next/debugging#opening-the-dev-menu)
  * [Opening DevTools](https://reactnative.dev/docs/next/debugging#opening-devtools)
  * [LogBox](https://reactnative.dev/docs/next/debugging#logbox)
    * [Console Errors and Warnings](https://reactnative.dev/docs/next/debugging#console-errors-and-warnings)
  * [Performance Monitor](https://reactnative.dev/docs/next/debugging#performance-monitor)



