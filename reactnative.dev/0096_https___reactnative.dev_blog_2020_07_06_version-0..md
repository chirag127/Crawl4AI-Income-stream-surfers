---
url: https://reactnative.dev/blog/2020/07/06/version-0.63
title: https://reactnative.dev/blog/2020/07/06/version-0.63
date: 2025-05-10T21:34:05.859203
depth: 2
---

[Skip to main content](https://reactnative.dev/blog/2020/07/06/version-0.63#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
Today we’re releasing React Native 0.63 that ships with LogBox turned on by default.
## LogBox[​](https://reactnative.dev/blog/2020/07/06/version-0.63#logbox "Direct link to LogBox")
We’ve heard frequent feedback from the community that errors and warnings are difficult to debug in React Native. To address these issues we took a look at the entire error, warning, and log system in React Native and redesigned it [from the ground up](https://www.youtube.com/watch?v=Y8brBH5O-bQ&feature=youtu.be).
LogBox is a completely redesigned redbox, yellowbox, and logging experience in React Native. In 0.62 we introduced LogBox as an opt-in. In this release, we’re launching LogBox as the default experience in all of React Native.
LogBox addresses complaints that errors and warnings were too verbose, poorly formatted, or unactionable by focusing on three primary goals:
  * **Concise** : Logs should provide the minimum amount of information necessary to debug an issue.
  * **Formatted** : Logs should be formatted so that you can quickly find the information you need.
  * **Actionable** : Logs should be actionable, so you can fix the issue and move on.


To achieve these goals, LogBox includes:
  * **Log notifications** : We’ve redesigned the warning notifications and added support for errors so that all console.warn and console.log messages show up as notifications instead of covering your app.
  * **Code Frames** : Every error and warning now includes a code frame that shows the source code of the log right inside the app, allowing you to quickly identify the source of your issue.
  * **Component Stacks** : All component stacks are now stripped from error messages and put into their own section with the top three frames visible. This gives you a single, consistent space to expect stack frame information that doesn’t clutter the log message.
  * **Stack Frame Collapsing** : By default we now collapse call stack frames not related to your application’s code so you can quickly see the issue in your app and not sift through React Native internals.
  * **Syntax Error Formatting** : We’ve improved the formatting for syntax errors and added codeframes with syntax highlighting so you can see the source of the error, fix it, and continue coding without React Native getting in your way.


We’ve wrapped all of these features into an improved visual design that’s consistent between errors and warnings and allows paginating through all logs in one enjoyable UI.
With this change we’re also deprecating YellowBox in favor of LogBox APIs:
  * `LogBox.ignoreLogs()`: This function replaces `YellowBox.ignoreLogs([])` as a way to silence any logs that match the given strings or regexes.
  * `LogBox.ignoreAllLogs()`: This function replaces `console.disableYellowBox` as a way to turn off error or warning notifications. Note: this only disables notifications, uncaught errors will still open a full screen LogBox.


In 0.63, we will warn when using these deprecated modules or methods. Please update your call sites off of these APIs before they are removed in 0.64.
For more information on LogBox and debugging react native, see the docs [here](https://reactnative.dev/docs/debugging#in-app-errors-and-warnings).
## Pressable[​](https://reactnative.dev/blog/2020/07/06/version-0.63#pressable "Direct link to Pressable")
React Native is built to enable applications to meet user’s expectations of the platform. This includes avoiding “tells”—little things that give away that the experience was built with React Native. One major source of these tells has been the Touchable components: `Button`, `TouchableWithoutFeedback`, `TouchableHighlight`, `TouchableOpacity`, `TouchableNativeFeedback`, and `TouchableBounce`. These components make your application interactive by allowing you to provide visual feedback to user interactions. However, because they include built-in styles and effects that don’t match the platform interaction, users can tell when experiences are written with React Native.
Further, as React Native has grown and our bar for high-quality applications has gone up, these components haven't grown with it. React Native now supports platforms like Web, Desktop, and TV, but support for additional input modalities has been lacking. React Native needs to support high-quality interaction experiences on all platforms.
To address these problems, we are shipping a new core component called `Pressable`. This component can be used to detect various types of interactions. The API was designed to provide direct access to the current state of interaction without having to maintain state manually in a parent component. It was also designed to enable platforms to extend it's capabilities to include hover, blur, focus, and more. We expect that most people will build and share components utilizing `Pressable` under the hood instead of relying on the default experience of something like `TouchableOpacity`.
```
import{Pressable,Text}from'react-native';<PressableonPress={()=>{console.log('pressed');style={({pressed})=>({backgroundColor: pressed ?'lightskyblue':'white',})}><Textstyle={styles.text}>Press Me!</Text></Pressable>;
```

A simple example of a Pressable component in action
You can learn more about it from [the documentation](https://reactnative.dev/docs/pressable).
## Native Colors (PlatformColor, DynamicColorIOS)[​](https://reactnative.dev/blog/2020/07/06/version-0.63#native-colors-platformcolor-dynamiccolorios "Direct link to Native Colors \(PlatformColor, DynamicColorIOS\)")
Every native platform has the concept of system-defined colors. Colors that automatically respond to system theme settings such as Light or Dark mode, accessibility settings such as a High Contrast mode, and even its context within the app such as the traits of a containing view or window.
While it is possible to detect some of these settings via the [`Appearance`](https://reactnative.dev/docs/appearance#getcolorscheme) API and/or [`AccessibilityInfo`](https://reactnative.dev/docs/accessibilityinfo#isgrayscaleenabled) and set your styles accordingly, such abstractions are not only costly to develop but are approximating the appearance of native colors. These inconsistencies are particularly noticeable when working on a hybrid application, where React Native elements co-exist next to the native ones.
React Native now provides an out-of-the-box solution to use these system colors. `PlatformColor()` is a new API that can be used like any other color in React Native.
For example, on iOS, the [system provides a color called `labelColor`](https://developer.apple.com/documentation/uikit/uicolor/ui_element_colors?language=objc). That can be used in React Native with `PlatformColor` like this:
```
import{Text,PlatformColor}from'react-native';<Textstyle={{color:PlatformColor('labelColor')}}> This is a label</Text>;
```

Sets the color of the Text component to labelColor as defined by iOS.
Android, on the other hand, [provides colors like colorButtonNormal](https://developer.android.com/reference/android/R.attr#colorButtonNormal). You can use this color in React Native with:
```
import{View,Text,PlatformColor}from'react-native';<Viewstyle={{backgroundColor:PlatformColor('?attr/colorButtonNormal'),}}><Text>This is colored like a button!</Text></View>;
```

Sets the background color of the View component to colorButtonNormal as defined by Android.
You can learn more about `PlatformColor` from [the documentation](https://reactnative.dev/docs/platformcolor). You can also check the actual [code examples present in the RNTester](https://github.com/facebook/react-native/blob/master/packages/rn-tester/js/examples/PlatformColor/PlatformColorExample.js).
`DynamicColorIOS` is an iOS only API that lets you define which color to use in light and dark mode. Similar to `PlatformColor`, this can be used anywhere you can use colors. `DynamicColorIOS` uses iOS’s `colorWithDynamicProvider` under the hood.
```
import{Text,DynamicColorIOS}from'react-native';const customDynamicTextColor =DynamicColorIOS({dark:'lightskyblue',light:'midnightblue',});<Textstyle={{color: customDynamicTextColor}}> This color changes automatically based on the system theme!</Text>;
```

Changes the text color based on the system theme
You can learn more about `DynamicColorIOS` from [the documentation](https://reactnative.dev/docs/dynamiccolorios).
## Dropping iOS 9 and Node.js 8 support[​](https://reactnative.dev/blog/2020/07/06/version-0.63#dropping-ios-9-and-nodejs-8-support "Direct link to Dropping iOS 9 and Node.js 8 support")
After over four years from its release, we are dropping support for iOS 9. This change will allow us to move faster by being able to reduce the number of compatibility checks that need to be placed in the native code to detect whether a given feature was supported on a certain iOS version. With its [market share of 1%](https://david-smith.org/iosversionstats/), it shouldn’t have much negative impact on your customers.
At the same time, we are dropping support for Node 8. [Its LTS maintenance cycle expired in December 2019](https://nodejs.org/fr/blog/release/v8.9.0/). The current LTS is Node 10 and it is now the version that we are targeting. If you are still using Node 8 for the development of React Native applications, we encourage you to upgrade in order to receive all the latest security fixes and updates.
## Other notable improvements[​](https://reactnative.dev/blog/2020/07/06/version-0.63#other-notable-improvements "Direct link to Other notable improvements")
  * **Support rendering`<View />` in `<Text />` without explicit size**: You can now render any `<View />` inside any `<Text />` component without setting its width and height explicitly, which wasn’t always possible. On previous releases of React Native, this would result in a RedBox.
  * **Changed iOS LaunchScreen from`xib` to `storyboard`**: Starting April 30, 2020, all apps submitted to the App Store must use an Xcode storyboard to provide the app’s launch screen and all iPhone apps must support all iPhone screens. This commit adjusts the default React Native template to be compatible with this requirement.


## Thanks[​](https://reactnative.dev/blog/2020/07/06/version-0.63#thanks "Direct link to Thanks")
Thank you to the hundreds of contributors that helped make 0.63 possible!
> Special thanks to [Rick Hanlon](https://twitter.com/rickhanlonii) for authoring the section on `LogBox` and [Eli White](https://twitter.com/Eli_White) for authoring the `Pressable` part of this article.
To see all the updates, take a look at the [0.63 changelog](https://github.com/facebook/react-native/blob/main/CHANGELOG.md#v0630).
  * [Native Colors (PlatformColor, DynamicColorIOS)](https://reactnative.dev/blog/2020/07/06/version-0.63#native-colors-platformcolor-dynamiccolorios)
  * [Dropping iOS 9 and Node.js 8 support](https://reactnative.dev/blog/2020/07/06/version-0.63#dropping-ios-9-and-nodejs-8-support)
  * [Other notable improvements](https://reactnative.dev/blog/2020/07/06/version-0.63#other-notable-improvements)



