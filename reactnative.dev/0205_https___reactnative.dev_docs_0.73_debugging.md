---
url: https://reactnative.dev/docs/0.73/debugging
title: https://reactnative.dev/docs/0.73/debugging
date: 2025-05-10T21:37:07.522076
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/0.73/debugging#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
This is documentation for React Native **0.73** , which is no longer in active development.
For up-to-date documentation, see the **[latest version](https://reactnative.dev/docs/debugging)** (0.79).
Version: 0.73
On this page
## Accessing the Dev Menu[​](https://reactnative.dev/docs/0.73/debugging#accessing-the-dev-menu "Direct link to Accessing the Dev Menu")
React Native provides an in-app developer menu which offers several debugging options. You can access the Dev Menu by shaking your device or via keyboard shortcuts:
  * iOS Simulator: `Cmd ⌘` + `D` (or Device > Shake)
  * Android emulators: `Cmd ⌘` + `M` (macOS) or `Ctrl` + `M` (Windows and Linux)


Alternatively for Android devices and emulators, you can run `adb shell input keyevent 82` in your terminal.
note
The Dev Menu is disabled in release (production) builds.
## Opening the Debugger[​](https://reactnative.dev/docs/0.73/debugging#opening-the-debugger "Direct link to Opening the Debugger")
The debugger allows you to understand and debug how your JavaScript code is running, similar to a web browser.
info
**In Expo projects** , press `j` in the CLI to directly open the Hermes Debugger.
  * Hermes Debugger / Expo
  * Flipper
  * New Debugger (Experimental)


Hermes supports the Chrome debugger by implementing the Chrome DevTools Protocol. This means Chrome's tools can be used to directly debug JavaScript running on Hermes, on an emulator or on a physical device.
  1. In a Chrome browser window, navigate to `chrome://inspect`.
  2. Use the "Configure..." button to add the dev server address (typically `localhost:8081`).
  3. You should now see a "Hermes React Native" target with an **"inspect"** link. Click this to open the debugger.


[Flipper](https://fbflipper.com/) is a native debugging tool which provides JavaScript debugging capabilities for React Native via an embedded Chrome DevTools panel.
To debug JavaScript code in Flipper, select **"Open Debugger"** from the Dev Menu. Learn more about Flipper [here](https://fbflipper.com/docs/features/react-native/).
info
To debug using Flipper, the Flipper app must be [installed on your system](https://fbflipper.com/docs/getting-started/).
warning
Debugging React Native apps with Flipper is [deprecated in React Native 0.73](https://github.com/react-native-community/discussions-and-proposals/pull/641). We will eventually remove out-of-the box support for JS debugging via Flipper.
note
**This is an experimental feature** and several features may not work reliably today. When this feature does launch in future, we intend for it to work more completely than the current debugging methods.
The React Native team is working on a new JavaScript debugger experience, intended to replace Flipper, with a preview available as of React Native 0.73.
The new debugger can be enabled via React Native CLI. This will also enable `j` to debug.
sh
```
npx react-native start --experimental-debugger
```

When selecting **"Open Debugger"** in the Dev Menu, this will launch the new debugger using Google Chrome or Microsoft Edge.
## React DevTools[​](https://reactnative.dev/docs/0.73/debugging#react-devtools "Direct link to React DevTools")
You can use React DevTools to inspect the React element tree, props, and state.
sh
```
npx react-devtools
```

tip
**Learn how to use React DevTools!**
  * [React DevTools guide](https://reactnative.dev/docs/0.73/react-devtools)
  * [React Developer Tools on react.dev](https://react.dev/learn/react-developer-tools)


## LogBox[​](https://reactnative.dev/docs/0.73/debugging#logbox "Direct link to LogBox")
Errors and warnings in development builds are displayed in LogBox inside your app.
note
LogBox is disabled in release (production) builds.
### Console Errors and Warnings[​](https://reactnative.dev/docs/0.73/debugging#console-errors-and-warnings "Direct link to Console Errors and Warnings")
Console errors and warnings are displayed as on-screen notifications with a red or yellow badge, and a notification count. To see more about an error or warning, tap the notification to see an expanded view and to paginate through other logs.
LogBox notifications can be disabled using `LogBox.ignoreAllLogs()`. This can be useful when giving product demos, for example. Additionally, notifications can be disabled on a per-log basis via `LogBox.ignoreLogs()`. This can be useful for noisy warnings or those that cannot be fixed, e.g. in a third-party dependency.
info
Ignore logs as a last resort and create a task to fix any logs that are ignored.
js
```
import{LogBox}from'react-native';// Ignore log notification by messageLogBox.ignoreLogs([// Exact message'Warning: componentWillReceiveProps has been renamed',// Substring or regex match/GraphQL error:.*/,]);// Ignore all log notificationsLogBox.ignoreAllLogs();
```

### Syntax Errors[​](https://reactnative.dev/docs/0.73/debugging#syntax-errors "Direct link to Syntax Errors")
When a JavaScript syntax error occurs, LogBox will open with the location of the error. In this state, LogBox is not dismissable since your code cannot be executed. LogBox will automatically dismiss once the syntax error is fixed — either via Fast Refresh or after a manual reload.
## Performance Monitor[​](https://reactnative.dev/docs/0.73/debugging#performance-monitor "Direct link to Performance Monitor")
On Android and iOS, an in-app performance overlay can be toggled during development by selecting **"Perf Monitor"** in the Dev Menu. Learn more about this feature [here](https://reactnative.dev/docs/performance).
info
The Performance Monitor runs in-app and is a guide. We recommend investigating the native tooling under Android Studio and Xcode for accurate performance measurements.
  * [Accessing the Dev Menu](https://reactnative.dev/docs/0.73/debugging#accessing-the-dev-menu)
  * [Opening the Debugger](https://reactnative.dev/docs/0.73/debugging#opening-the-debugger)
  * [React DevTools](https://reactnative.dev/docs/0.73/debugging#react-devtools)
  * [LogBox](https://reactnative.dev/docs/0.73/debugging#logbox)
    * [Console Errors and Warnings](https://reactnative.dev/docs/0.73/debugging#console-errors-and-warnings)
    * [Syntax Errors](https://reactnative.dev/docs/0.73/debugging#syntax-errors)
  * [Performance Monitor](https://reactnative.dev/docs/0.73/debugging#performance-monitor)



