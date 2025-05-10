---
url: https://reactnative.dev/blog/2019/11/18/react-native-doctor
title: https://reactnative.dev/blog/2019/11/18/react-native-doctor
date: 2025-05-10T21:34:05.847113
depth: 2
---

[Skip to main content](https://reactnative.dev/blog/2019/11/18/react-native-doctor#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
After over 20 pull requests from 6 contributors in the React Native Community, we're excited to launch `react-native doctor`, a new command to help you out with getting started, troubleshooting and automatically fixing errors with your development environment. The `doctor` command is heavily inspired by [Expo](https://expo.io/) and [Homebrew](https://brew.sh/)'s own doctor command with a pinch of UI inspired by [Jest](https://jestjs.io/).
Here it is in action:
## How it works[​](https://reactnative.dev/blog/2019/11/18/react-native-doctor#how-it-works "Direct link to How it works")
The `doctor` command currently supports most of the software and libraries that React Native relies on, such as CocoaPods, Xcode and Android SDK. With `doctor` we'll find issues with your development environment and give you the option to automatically fix them. If `doctor` is not able to fix an issue, it will display a message and a helpful link explaining how to fix it manually as the following:
## Try it now[​](https://reactnative.dev/blog/2019/11/18/react-native-doctor#try-it-now "Direct link to Try it now")
The `doctor` command is available as a part of React Native 0.62. However, you can try it without upgrading yet:
```
npx @react-native-community/cli doctor
```

## What checks are currently supported[​](https://reactnative.dev/blog/2019/11/18/react-native-doctor#what-checks-are-currently-supported "Direct link to What checks are currently supported")
`doctor` currently supports the following checks:
  * Node.js (>= 8.3)
  * yarn (>= 1.10)
  * npm (>= 4)
  * Watchman (>= 4), used for watching changes in the filesystem when in development mode.


Specific to the Android environment:
  * Android SDK (>= 26), the software runtime for Android.
  * Android NDK (>= 19), the native development toolkit for Android.
  * `ANDROID_HOME`, environment variable required by the Android SDK setup.


And to the iOS environment:
  * Xcode (>= 10), IDE for developing, building and shipping iOS applications.
  * CocoaPods, library dependency management tool for iOS applications.
  * ios-deploy (optional), library used internally by the CLI to install applications on a physical iOS device.


## Thanks[​](https://reactnative.dev/blog/2019/11/18/react-native-doctor#thanks "Direct link to Thanks")
Huge thanks for the React Native Community for working on this, in particular [@thymikee](https://github.com/thymikee), [@thib92](https://github.com/thib92), [@jmeistrich](https://github.com/jmeistrich), [@tido64](https://github.com/tido64) and [@rickhanlonii](https://github.com/rickhanlonii).
  * [What checks are currently supported](https://reactnative.dev/blog/2019/11/18/react-native-doctor#what-checks-are-currently-supported)



