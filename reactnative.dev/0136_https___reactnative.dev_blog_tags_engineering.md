---
url: https://reactnative.dev/blog/tags/engineering
title: https://reactnative.dev/blog/tags/engineering
date: 2025-05-10T21:34:58.816342
depth: 2
---

[Skip to main content](https://reactnative.dev/blog/tags/engineering#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
Today we are excited to release React Native 0.79!
This release ships with performance improvements on various fronts, as well as several bugfixes. First, Metro is now faster to start thanks to deferred hashing, and has stable support for package exports. Startup time in Android will also be improved thanks to changes in the JS bundle compressions and much more.
### Highlights[​](https://reactnative.dev/blog/tags/engineering#highlights "Direct link to Highlights")
  * [JSC moving to a Community Package](https://reactnative.dev/blog/2025/04/08/react-native-0.79#jsc-moving-to-community-package)
  * [iOS: Swift-Compatible Native Modules registration](https://reactnative.dev/blog/2025/04/08/react-native-0.79#ios-swift-compatible-native-modules-registration)
  * [Android: Faster App Startup](https://reactnative.dev/blog/2025/04/08/react-native-0.79#android-faster-app-startup)
  * [Removal of Remote JS Debugging](https://reactnative.dev/blog/2025/04/08/react-native-0.79#removal-of-remote-js-debugging)


Today we are excited to release React Native 0.78!
This release ships React 19 in React Native and some other relevant features like native support for Android Vector drawables and better brownfield integration for iOS.
### Highlights[​](https://reactnative.dev/blog/tags/engineering#highlights "Direct link to Highlights")
  * [Towards smaller and faster releases](https://reactnative.dev/blog/2025/02/19/react-native-0.78#towards-smaller-and-faster-releases)
  * [Opt-in for JavaScript logs in Metro](https://reactnative.dev/blog/2025/02/19/react-native-0.78#opt-in-for-javascript-logs-in-metro)
  * [Added support for Android XML drawables](https://reactnative.dev/blog/2025/02/19/react-native-0.78#added-support-for-android-xml-drawables)
  * [ReactNativeFactory on iOS](https://reactnative.dev/blog/2025/02/19/react-native-0.78#reactnativefactory-on-ios)


Every year, the core contributors in the React Native Community get together with the React Native team to collaboratively shape the direction of this project.
Last year was no different—with small exception. We usually meet a day before [React Universe Conf](https://www.reactuniverseconf.com) (formerly React Native EU) at [Callstack](https://www.callstack.com/open-source) HQ in Wrocław. In 2024, learning from past experiences, we hosted the Summit for two consecutive days, so that we can have more unstructured time together.
Today we are excited to release React Native 0.77!
This release ships several features: new styling capabilities such as support for `display: contents`, `boxSizing`, `mixBlendMode`, and `outline`-related properties to provide a more powerful layout options; Android 16KB page support to be compatible with the newer Android devices. We are also modernizing the community template by migrating it to Swift, while continuing to support and maintain compatibility with Objective-C for developers who prefer it.
Today we are excited to release React Native 0.75!
This release ships several features, such as Yoga 3.1 with support for `%` values, several stabilization fixes for the New Architecture, and the introduction of the recommendation for users to use a React Native Framework.
### Highlights[​](https://reactnative.dev/blog/tags/engineering#highlights "Direct link to Highlights")
  * [Yoga 3.1 and Layout Improvements](https://reactnative.dev/blog/2024/08/12/release-0.75#yoga-31-and-layout-improvements)
  * [New Architecture Stabilization](https://reactnative.dev/blog/2024/08/12/release-0.75#new-architecture-stabilization)


### Breaking Changes[​](https://reactnative.dev/blog/tags/engineering#breaking-changes "Direct link to Breaking Changes")
  * [Touchables in TypeScript can’t be used as types in Generic expressions anymore](https://reactnative.dev/blog/2024/08/12/release-0.75#touchables-in-typescript-cant-be-used-as-types-in-generic-expressions-anymore)
  * [Last version supporting minSdk 23 and minIOSVersion 13.4](https://reactnative.dev/blog/2024/08/12/release-0.75#last-version-supporting-minsdk-23-and-miniosversion-134)
  * [Android: JSIModule has been deleted](https://reactnative.dev/blog/2024/08/12/release-0.75#android-jsimodule-has-been-deleted)
  * [Android: PopUp Menu removed from core](https://reactnative.dev/blog/2024/08/12/release-0.75#android-popup-menu-moved-to-separate-package)
  * [iOS: Finalized Push Notifications deprecation work](https://reactnative.dev/blog/2024/08/12/release-0.75#ios-finalized-pushnotificationios-deprecation-work)
  * [Community CLI: Removal of ram-bundle and profile-hermes commands](https://reactnative.dev/blog/2024/08/12/release-0.75#community-cli-removal-of-ram-bundle-and-profile-hermes-commands)


Now that 0.71 is [available](https://reactnative.dev/blog/2023/01/12/version-071), we want to share some key information about the incident that broke Android builds for all React Native versions while releasing the first 0.71 release candidate for React Native & Expo Android builds on November 4th, 2022.
The contributors who helped tackle the incident recently attended a post-mortem meeting to discuss in detail what happened, what we all learned from it, and what actions we are going to take to avoid similar outages in the future.
With the release of 0.71, React Native is investing in the TypeScript experience with the following changes:
  * [New app template is TypeScript by default](https://reactnative.dev/blog/2023/01/03/typescript-first#new-app-template-is-typescript-by-default)
  * [TypeScript declarations shipped with React Native](https://reactnative.dev/blog/2023/01/03/typescript-first#declarations-shipped-with-react-native)
  * [React Native documentation is TypeScript First](https://reactnative.dev/blog/2023/01/03/typescript-first#documentation-is-typescript-first)


In this post we’ll cover what these changes mean for you as a TypeScript or Flow user.
Hello everyone!
With new mobile OS versions releasing late this year, we recommend preparing your React Native apps beforehand to avoid regressions when the releases become generally available.
For a long time now, Apple has discouraged using UIWebViews in favor of WKWebView. In iOS 12, which will be released in the upcoming months, [UIWebViews will be formally deprecated](https://developer.apple.com/videos/play/wwdc2018/234/?time=104). React Native's iOS WebView implementation relies heavily on the UIWebView class. Therefore, in light of these developments, we've built a new native iOS backend to the WebView React Native component that uses WKWebView.
The tail end of these changes were landed in [this commit](https://github.com/facebook/react-native/commit/33b353c97c31190439a22febbd3d2a9ead49d3c9), and will become available in the 0.57 release.
To opt into this new implementation, please use the [`useWebKit`](https://reactnative.dev/docs/0.63/webview#usewebkit) prop:
```
<WebView useWebKit={true} source={{url:'https://www.google.com'}}
```

## Improvements[​](https://reactnative.dev/blog/tags/engineering#improvements "Direct link to Improvements")
`UIWebView` had no legitimate way to facilitate communication between the JavaScript running in the WebView, and React Native. When messages were sent from the WebView, we relied on a hack to deliver them to React Native. Succinctly, we encoded the message data into a url with a special scheme, and navigated the WebView to it. On the native side, we intercepted and cancelled this navigation, parsed the data from the url, and finally called into React Native. This implementation was error prone and insecure. I'm glad to announce that we've leveraged `WKWebView` features to completely replace it.
Other benefits of WKWebView over UIWebView include faster JavaScript execution, and a multi-process architecture. Please see this [2014 WWDC](https://developer.apple.com/videos/play/wwdc2014/206) for more details.
## Caveats[​](https://reactnative.dev/blog/tags/engineering#caveats "Direct link to Caveats")
If your components use the following props, then you may experience problems when switching to WKWebView. For the time being, we suggest that you avoid using these props:
**Inconsistent behavior:**
`automaticallyAdjustContentInsets` and `contentInsets` ([commit](https://github.com/facebook/react-native/commit/bacfd9297657569006bab2b1f024ad1f289b1b27))
When you add contentInsets to a `WKWebView`, it doesn't change the `WKWebView`'s viewport. The viewport remains the same size as the frame. With `UIWebView`, the viewport size actually changes (gets smaller, if the content insets are positive).
`backgroundColor` ([commit](https://github.com/facebook/react-native/commit/215fa14efc2a817c7e038075163491c8d21526fd))
With the new iOS implementation of WebView, there's a chance that your background color will flicker into view if you use this property. Furthermore, `WKWebView` renders transparent backgrounds differently from `UIWebview`. Please look at the commit description for more details.
**Not supported:**
`scalesPageToFit` ([commit](https://github.com/facebook/react-native/commit/b18fddadfeae5512690a0a059a4fa80c864f43a3))
WKWebView didn't support the scalesPageToFit prop, so we couldn't implement this on the WebView React Native component.
## Motivation[​](https://reactnative.dev/blog/tags/engineering#motivation "Direct link to Motivation")
As technology advances and mobile apps become increasingly important to everyday life, the necessity of creating accessible applications has likewise grown in importance.
React Native's limited Accessibility API has always been a huge pain point for developers, so we've made a few updates to the Accessibility API to make it easier to create inclusive mobile applications.
## Problems With the Existing API[​](https://reactnative.dev/blog/tags/engineering#problems-with-the-existing-api "Direct link to Problems With the Existing API")
### Problem One: Two Completely Different Yet Similar Props - accessibilityComponentType (Android) and accessibilityTraits (iOS)[​](https://reactnative.dev/blog/tags/engineering#problem-one-two-completely-different-yet-similar-props---accessibilitycomponenttype-android-and-accessibilitytraits-ios "Direct link to Problem One: Two Completely Different Yet Similar Props - accessibilityComponentType \(Android\) and accessibilityTraits \(iOS\)")
`accessibilityComponentType` and `accessibilityTraits` are two properties that are used to tell TalkBack on Android and VoiceOver on iOS what kind of UI element the user is interacting with. The two biggest problems with these properties are that:
  1. **They are two different properties with different usage methods, yet have the same purpose.** In the previous API, these are two separate properties (one for each platform), which was not only inconvenient, but also confusing to many developers. `accessibilityTraits` on iOS allows 17 different values while `accessibilityComponentType` on Android allows only 4 values. Furthermore, the values for the most part had no overlap. Even the input types for these two properties are different. `accessibilityTraits` allows either an array of traits to be passed in or a single trait, while `accessibilityComponentType` allows only a single value.
  2. **There is very limited functionality on Android.** With the old property, the only UI elements that Talkback were able to recognize were “button,” “radiobutton_checked,” and “radiobutton_unchecked.”


### Problem Two: Non-existent Accessibility Hints:[​](https://reactnative.dev/blog/tags/engineering#problem-two-non-existent-accessibility-hints "Direct link to Problem Two: Non-existent Accessibility Hints:")
Accessibility Hints help users using TalkBack or VoiceOver understand what will happen when they perform an action on an accessibility element that is not apparent by only the accessibility label. These hints can be turned on and off in the settings panel. Previously, React Native's API did not support accessibility hints at all.
### Problem Three: Ignoring Inverted Colors:[​](https://reactnative.dev/blog/tags/engineering#problem-three-ignoring-inverted-colors "Direct link to Problem Three: Ignoring Inverted Colors:")
Some users with vision loss use inverted colors on their mobile phones to have greater screen contrast. Apple provided an API for iOS which allows developers to ignore certain views. This way, images and videos aren't distorted when a user has the inverted colors setting on. This API is currently unsupported by React Native.
## Design of the New API[​](https://reactnative.dev/blog/tags/engineering#design-of-the-new-api "Direct link to Design of the New API")
### Solution One: Combining accessibilityComponentType (Android) and accessibilityTraits (iOS)[​](https://reactnative.dev/blog/tags/engineering#solution-one-combining-accessibilitycomponenttype-android-and-accessibilitytraits-ios "Direct link to Solution One: Combining accessibilityComponentType \(Android\) and accessibilityTraits \(iOS\)")
In order to solve the confusion between `accessibilityComponentType` and `accessibilityTraits`, we decided to merge them into a single property. This made sense because they technically had the same intended functionality and by merging them, developers no longer had to worry about platform specific intricacies when building accessibility features.
**Background**
On iOS, `UIAccessibilityTraits` is a property that can be set on any NSObject. Each of the 17 traits passed in through the javascript property to native is mapped to a `UIAccessibilityTraits` element in Objective-C. Traits are each represented by a long int, and every trait that is set is ORed together.
On Android however, `AccessibilityComponentType` is a concept that was made up by React Native, and doesn't directly map to any properties in Android. Accessibility is handled by an accessibility delegate. Each view has a default accessibility delegate. If you want to customize any accessibility actions, you have to create a new accessibility delegate, override specific methods you want to customize, and then set the accessibility delegate of the view you are handling to be associated with the new delegate. When a developer set `AccessibilityComponentType`, the native code created a new delegate based off of the component that was passed in, and set the view to have that accessibility delegate.
**Changes Made**
For our new property, we wanted to create a superset of the two properties. We decided to keep the new property modeled mostly after the existing property `accessibilityTraits`, since `accessibilityTraits` has significantly more values. The functionality of Android for these traits would be polyfilled in by modifying the Accessibility Delegate.
There are 17 values of UIAccessibilityTraits that `accessibilityTraits` on iOS can be set to. However, we didn't include all of them as possible values to our new property. This is because the effect of setting some of these traits is actually not very well known, and many of these values are virtually never used.
The values UIAccessibilityTraits were set to generally took on one of two purposes. They either described a role that UI element had, or they described the state a UI element was in. Most uses of the previous properties we observed usually used one value that represented a role and combined it with either “state selected,” “state disabled,” or both. Therefore, we decided to create two new accessibility properties: `accessibilityRole` and `accessibilityState`.
**`accessibilityRole`**
The new property, `accessibilityRole`, is used to tell Talkback or Voiceover the role of a UI Element. This new property can take on one of the following values:
  * `none`
  * `button`
  * `link`
  * `search`
  * `image`
  * `keyboardkey`
  * `text`
  * `adjustable`
  * `header`
  * `summary`
  * `imagebutton`


This property only allows one value to be passed in because UI elements generally don't logically take on more than one of these. The exception is image and button, so we've added a role imagebutton that is a combination of both.
**`accessibilityStates`**
The new property, `accessibilityStates`, is used to tell Talkback or Voiceover the state a UI Element is in. This property takes on an Array containing one or both of the following values:
  * `selected`
  * `disabled`


### Solution Two: Adding Accessibility Hints[​](https://reactnative.dev/blog/tags/engineering#solution-two-adding-accessibility-hints "Direct link to Solution Two: Adding Accessibility Hints")
For this, we added a new property, `accessibilityHint`. Setting this property will allow Talkback or Voiceover to recite the hint to users.
**`accessibilityHint`**
This property takes in the accessibility hint to be read in the form of a String.
On iOS, setting this property will set the corresponding native property AccessibilityHint on the view. The hint will then be read by Voiceover if Accessibility Hints are turned on in the iPhone.
On Android, setting this property appends the value of the hint to the end of the accessibility label. The upside to this implementation is that it mimics the behavior of hints on iOS, but the downside to this implementation is that these hints cannot be turned off in the settings on Android the way they can be on iOS.
The reason we made this decision on Android is because normally, accessibility hints correspond with a specific action (e.g. click), and we wanted to keep behaviors consistent across platforms.
### Solution to Problem Three[​](https://reactnative.dev/blog/tags/engineering#solution-to-problem-three "Direct link to Solution to Problem Three")
**`accessibilityIgnoresInvertColors`**
We exposed Apple's api AccessibilityIgnoresInvertColors to JavaScript, so now when you have a view where you don't want colors to be inverted (e.g image), you can set this property to true, and it won't be inverted.
## New Usage[​](https://reactnative.dev/blog/tags/engineering#new-usage "Direct link to New Usage")
These new properties will become available in the React Native 0.57 release.
### How to Upgrade[​](https://reactnative.dev/blog/tags/engineering#how-to-upgrade "Direct link to How to Upgrade")
If you are currently using `accessibilityComponentType` and `accessibilityTraits`, here are the steps you can take to upgrade to the new properties.
#### 1. Using jscodeshift[​](https://reactnative.dev/blog/tags/engineering#1-using-jscodeshift "Direct link to 1. Using jscodeshift")
The most simple use cases can be replaced by running a jscodeshift script.
This [script](https://gist.github.com/ziqichen6/246e5778617224d2b4aff198dab0305d) replaces the following instances:
```
accessibilityTraits=“trait”accessibilityTraits={[“trait”]}
```

With
```
accessibilityRole= “trait”
```

This script also removes instances of `AccessibilityComponentType` (assuming everywhere you set `AccessibilityComponentType`, you would also set `AccessibilityTraits`).
#### 2. Using a manual codemod[​](https://reactnative.dev/blog/tags/engineering#2-using-a-manual-codemod "Direct link to 2. Using a manual codemod")
For the cases that used `AccessibilityTraits` that don't have a corresponding value for `AccessibilityRole`, and the cases where multiple traits were passed into `AccessibilityTraits`, a manual codemod would have to be done.
In general,
```
accessibilityTraits={[“button”, “selected”]}
```

would be manually replaced with
```
accessibilityRole=“button”accessibilityStates={[“selected”]}
```

These properties are already being used in Facebook's codebase. The codemod for Facebook was surprisingly simple. The jscodeshift script fixed about half of our instances, and the other half was fixed manually. Overall, the entire process took less than a few hours.
Hopefully you will find the updated API useful! And please continue making apps accessible! #inclusion

