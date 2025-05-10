---
url: https://reactnative.dev/blog/2021/03/12/version-0.64
title: https://reactnative.dev/blog/2021/03/12/version-0.64
date: 2025-05-10T20:54:13.325500
depth: 2
---

[Skip to main content](https://reactnative.dev/blog/2021/03/12/version-0.64#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
Today we’re releasing React Native 0.64 that ships with support for Hermes on iOS.
## Hermes opt-in on iOS[​](https://reactnative.dev/blog/2021/03/12/version-0.64#hermes-opt-in-on-ios "Direct link to Hermes opt-in on iOS")
[Hermes](https://hermesengine.dev) is an open source JavaScript engine optimized for running React Native. It improves performance by decreasing memory utilization, reducing download size and decreasing the time it takes for the app to become usable or “time to interactive” (TTI).
With this release, we are happy to announce that you can now use Hermes to build on iOS as well. To enable Hermes on iOS, set `hermes_enabled` to `true` in your `Podfile` and run `pod install`.
```
use_react_native!(:path=> config[:reactNativePath],# to enable hermes on iOS, change `false` to `true` and then install pods:hermes_enabled=>true
```

Please keep in mind that Hermes support on iOS is still early stage. We are keeping it as an opt-in as we are running further benchmarking. We encourage you to try it on your own applications and let us know how it is working out for you!
## Inline Requires enabled by default[​](https://reactnative.dev/blog/2021/03/12/version-0.64#inline-requires-enabled-by-default "Direct link to Inline Requires enabled by default")
Inline Requires is a Metro configuration option that improves startup time by delaying execution of JavaScript modules until they are used, instead of at startup.
This feature has existed and been recommended for a few years as an opt-in configuration option, listed in the [Performance section of our documentation](https://reactnative.dev/docs/performance). We are now enabling this option by default for new applications to help people have fast React Native applications without extra configuration.
Inline Requires is a Babel transform that takes module imports and converts them to be inline. As an example, Inline Requires transforms this module import call from being at the top of the file to where it is used.
**Before:**
```
import{MyFunction}from'my-module';constMyComponent=props=>{const result =MyFunction();return<Text>{result}</Text>;
```

**After:**
```
constMyComponent=props=>{const result =require('my-module').MyFunction();return<Text>{result}</Text>;
```

More information about Inline Requires is available in the [Performance documentation](https://reactnative.dev/docs/0.74/ram-bundles-inline-requires#inline-requires).
## View Hermes traces with Chrome[​](https://reactnative.dev/blog/2021/03/12/version-0.64#view-hermes-traces-with-chrome "Direct link to View Hermes traces with Chrome")
Over the last year Facebook has sponsored the [Major League Hacking fellowship](https://fellowship.mlh.io/), supporting contributions to React Native. [Jessie Nguyen](https://twitter.com/jessie_anh_ng) and [Saphal Patro](https://twitter.com/saphalinsaan) added the ability to use the Performance tab on Chrome DevTools to visualize the execution of your application when it is using Hermes.
For more information, check out the [new documentation page](https://reactnative-archive-august-2023.netlify.app/docs/0.64/profile-hermes#record-a-hermes-sampling-profile).
## Hermes with Proxy Support[​](https://reactnative.dev/blog/2021/03/12/version-0.64#hermes-with-proxy-support "Direct link to Hermes with Proxy Support")
We have added Proxy support to Hermes, enabling compatibility with popular community projects like react-native-firebase and mobx. If you have been using these packages you can now migrate to Hermes for your project.
We plan to make Hermes the default JavaScript engine for Android in a coming release so we are working to resolve the remaining issues people have when using Hermes. Please open an issue on the [Hermes GitHub repo](https://github.com/facebook/hermes) if there are remaining issues holding back your app from adopting Hermes.
## React 17[​](https://reactnative.dev/blog/2021/03/12/version-0.64#react-17 "Direct link to React 17")
React 17 does not include new developer-facing features or major breaking changes. For React Native applications, the main change is a [new JSX transform](https://reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html) enabling files to no longer need to import React to be able to use JSX.
More information about React 17 is available [on the React blog](https://reactjs.org/blog/2020/10/20/react-v17.html).
## Major Dependency Version Changes[​](https://reactnative.dev/blog/2021/03/12/version-0.64#major-dependency-version-changes "Direct link to Major Dependency Version Changes")
  * Dropped Android API levels 16-20. The Facebook app consistently drops support for Android versions with sufficiently low usage. As the Facebook app no longer supports these versions and is React Native’s main testing surface, React Native is dropping support as well.
  * Xcode 12 and CocoaPods 1.10 are required
  * Minimum Node support bumped from 10 to Node 12
  * Flipper bumped to 0.75.1


## Thanks[​](https://reactnative.dev/blog/2021/03/12/version-0.64#thanks "Direct link to Thanks")
Thank you to the hundreds of contributors that helped make 0.64 possible! The [0.64 changelog](https://github.com/facebook/react-native/blob/main/CHANGELOG.md#v0640) includes all of the changes included in this release.
  * [Hermes opt-in on iOS](https://reactnative.dev/blog/2021/03/12/version-0.64#hermes-opt-in-on-ios)
  * [Inline Requires enabled by default](https://reactnative.dev/blog/2021/03/12/version-0.64#inline-requires-enabled-by-default)
  * [View Hermes traces with Chrome](https://reactnative.dev/blog/2021/03/12/version-0.64#view-hermes-traces-with-chrome)
  * [Hermes with Proxy Support](https://reactnative.dev/blog/2021/03/12/version-0.64#hermes-with-proxy-support)
  * [Major Dependency Version Changes](https://reactnative.dev/blog/2021/03/12/version-0.64#major-dependency-version-changes)



