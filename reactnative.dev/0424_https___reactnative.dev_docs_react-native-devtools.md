---
url: https://reactnative.dev/docs/react-native-devtools
title: https://reactnative.dev/docs/react-native-devtools
date: 2025-05-10T21:41:45.262008
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/react-native-devtools#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
React Native DevTools is our modern debugging experience for React Native. Purpose-built from the ground up, it aims to be fundamentally more integrated, correct, and reliable than previous debugging methods.
React Native DevTools is designed for debugging React app concerns, and not to replace native tools. If you want to inspect React Native’s underlying platform layers (for example, while developing a Native Module), please use the debugging tools available in Android Studio and Xcode (see [Debugging Native Code](https://reactnative.dev/docs/debugging-native-code)).
**💡 Compatibility** — released in 0.76
React Native DevTools supports all React Native apps running Hermes. It replaces the previous Flipper, Experimental Debugger, and Hermes debugger (Chrome) frontends.
It is not possible to set up React Native DevTools with any older versions of React Native.
  * **Chrome Browser DevTools — unsupported**
    * Connecting to React Native via `chrome://inspect` is no longer supported. Features may not work correctly, as the latest versions of Chrome DevTools (which are built to match the latest browser capabilities and APIs) have not been tested, and this frontend lacks our customisations. Instead, we ship a supported version with React Native DevTools.
  * **Visual Studio Code — unsupported** (pre-existing) 
    * Third party extensions such as [Expo Tools](https://github.com/expo/vscode-expo) and [Radon IDE](https://ide.swmansion.com/) may have improved compatibility, but are not directly supported by the React team.


**💡 Feedback & FAQs**
We want the tooling you use to debug React across all platforms to be reliable, familiar, simple, and cohesive. All the features described on this page are built with these principles in mind, and we also want to offer more capabilities in future.
We are actively iterating on the future of React Native DevTools, and have created a centralized [GitHub discussion](https://github.com/react-native-community/discussions-and-proposals/discussions/819) to keep track of issues, frequently asked questions, and feedback.
## Core features[​](https://reactnative.dev/docs/react-native-devtools#core-features "Direct link to Core features")
React Native DevTools is based on the Chrome DevTools frontend. If you have a web development background, its features should be familiar. As a starting point, we recommend browsing the [Chrome DevTools docs](https://developer.chrome.com/docs/devtools) which contain full guides as well as video resources.
### Console[​](https://reactnative.dev/docs/react-native-devtools#console "Direct link to Console")
The Console panel allows you to view and filter messages, evaluate JavaScript, inspect object properties, and more.
[Console features reference | Chrome DevTools](https://developer.chrome.com/docs/devtools/console/reference)
#### Useful tips[​](https://reactnative.dev/docs/react-native-devtools#useful-tips "Direct link to Useful tips")
  * If your app has a lot of logs, use the filter box or change the log levels that are shown.
  * Watch values over time with [Live Expressions](https://developer.chrome.com/docs/devtools/console/live-expressions).
  * Persist messages across reloads with [Preserve Logs](https://developer.chrome.com/docs/devtools/console/reference#persist).
  * Use `Ctrl` + `L` to clear the console view.


### Sources & breakpoints[​](https://reactnative.dev/docs/react-native-devtools#sources--breakpoints "Direct link to Sources & breakpoints")
The Sources panel allows you to view the source files in your app and register breakpoints. Use a breakpoint to define a line of code where your app should pause — allowing you to inspect the live state of the program and incrementally step through code.
[Pause your code with breakpoints | Chrome DevTools](https://developer.chrome.com/docs/devtools/javascript/breakpoints)
tip
#### Mini-guide[​](https://reactnative.dev/docs/react-native-devtools#mini-guide "Direct link to Mini-guide")
Breakpoints are a fundamental tool in your debugging toolkit!
  1. Navigate to a source file using the sidebar or `Cmd ⌘`+`P` / `Ctrl`+`P`.
  2. Click in the line number column next to a line of code to add a breakpoint.
  3. Use the navigation controls at the top right to [step through code](https://developer.chrome.com/docs/devtools/javascript/reference#stepping) when paused.


#### Useful tips[​](https://reactnative.dev/docs/react-native-devtools#useful-tips-1 "Direct link to Useful tips")
  * A "Paused in Debugger" overlay will appear when your app is paused. Tap it to resume.
  * Pay attention to the right hand side panels when on a breakpoint, which allow you to inspect the current scope and call stack, and set watch expressions.
  * Use a `debugger;` statement to quickly set a breakpoint from your text editor. This will reach the device immediately via Fast Refresh.
  * There are multiple kinds of breakpoints! For example, [Conditional Breakpoints and Logpoints](https://developer.chrome.com/docs/devtools/javascript/breakpoints#overview).


### Memory[​](https://reactnative.dev/docs/react-native-devtools#memory "Direct link to Memory")
The Memory panel allows you to take a heap snapshot and view the memory usage of your JavaScript code over time.
[Record heap snapshots | Chrome DevTools](https://developer.chrome.com/docs/devtools/memory-problems/heap-snapshots)
#### Useful tips[​](https://reactnative.dev/docs/react-native-devtools#useful-tips-2 "Direct link to Useful tips")
  * Use `Cmd ⌘`+`F` / `Ctrl`+`F` to filter for specific objects in the heap.
  * Taking an [allocation timeline report](https://developer.chrome.com/docs/devtools/memory-problems/allocation-profiler) can be useful to see memory usage over time as a graph, to identify possible memory leaks.


## React DevTools features[​](https://reactnative.dev/docs/react-native-devtools#react-devtools-features "Direct link to React DevTools features")
In the integrated Components and Profiler panels, you'll find all the features of the [React DevTools](https://react.dev/learn/react-developer-tools) browser extension. These work seamlessly in React Native DevTools.
### React Components[​](https://reactnative.dev/docs/react-native-devtools#react-components "Direct link to React Components")
The React Components panel allows you to inspect and update the rendered React component tree.
  * Hover or select an element in DevTools to highlight it on device.
  * To locate an element in DevTools, click the top-left "Select element" button, then tap any element in the app.


#### Useful tips[​](https://reactnative.dev/docs/react-native-devtools#useful-tips-3 "Direct link to Useful tips")
  * Props and state on a component can be viewed and modified at runtime using the right hand panel.
  * Components optimized with [React Compiler](https://react.dev/learn/react-compiler) will be annotated with a "Memo ✨" badge.


tip
#### Protip: Highlight re-renders[​](https://reactnative.dev/docs/react-native-devtools#protip-highlight-re-renders "Direct link to Protip: Highlight re-renders")
Re-renders can be a significant contributor to performance issues in React apps. DevTools can highlight component re-renders as they happen.
  * To enable, click the View Settings (`⚙︎`) icon and check "Highlight updates when components render".


### React Profiler[​](https://reactnative.dev/docs/react-native-devtools#react-profiler "Direct link to React Profiler")
The React Profiler panel allows you to record performance profiles to understand the timing of component renders and React commits.
For more info, see the [original 2018 guide](https://legacy.reactjs.org/blog/2018/09/10/introducing-the-react-profiler.html#reading-performance-data) (note that parts of this may be outdated).
## Reconnecting DevTools[​](https://reactnative.dev/docs/react-native-devtools#reconnecting-devtools "Direct link to Reconnecting DevTools")
Occasionally, DevTools might disconnect from the target device. This can happen if:
  * The app is closed.
  * The app is rebuilt (a new native build is installed).
  * The app has crashed on the native side.
  * The dev server (Metro) is quit.
  * A physical device is disconnected.


On disconnect, a dialog will be shown with the message "Debugging connection was closed".
From here, you can either:
  * **Dismiss** : Select the close (`×`) icon or click outside the dialog to return to the DevTools UI in the last state before disconnection.
  * **Reconnect** : Select "Reconnect DevTools", having addressed the reason for disconnection.


Is this page useful?
  * [Core features](https://reactnative.dev/docs/react-native-devtools#core-features)
    * [Sources & breakpoints](https://reactnative.dev/docs/react-native-devtools#sources--breakpoints)
  * [React DevTools features](https://reactnative.dev/docs/react-native-devtools#react-devtools-features)
    * [React Components](https://reactnative.dev/docs/react-native-devtools#react-components)
    * [React Profiler](https://reactnative.dev/docs/react-native-devtools#react-profiler)
  * [Reconnecting DevTools](https://reactnative.dev/docs/react-native-devtools#reconnecting-devtools)



