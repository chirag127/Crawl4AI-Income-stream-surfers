---
url: https://reactnative.dev/blog/2019/03/12/releasing-react-native-059
title: https://reactnative.dev/blog/2019/03/12/releasing-react-native-059
date: 2025-05-10T20:54:13.307185
depth: 2
---

[Skip to main content](https://reactnative.dev/blog/2019/03/12/releasing-react-native-059#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
Welcome to the 0.59 release of React Native! This is another big release with 644 commits by 88 contributors. Contributions also come in other forms, so _thank you_ for maintaining issues, fostering communities, and teaching people about React Native. This month brings a number of highly anticipated changes, and we hope you enjoy them.
## 🎣 Hooks are here[​](https://reactnative.dev/blog/2019/03/12/releasing-react-native-059#-hooks-are-here "Direct link to 🎣 Hooks are here")
React Hooks are part of this release, which let you reuse stateful logic across components. There is a lot of buzz about hooks, but if you haven't heard, take a look at some of the wonderful resources below:
>   * [Introducing Hooks](https://reactjs.org/docs/hooks-intro.html) explains why we’re adding Hooks to React.
>   * [Hooks at a Glance](https://reactjs.org/docs/hooks-overview.html) is a fast-paced overview of the built-in Hooks.
>   * [Building Your Own Hooks](https://reactjs.org/docs/hooks-custom.html) demonstrates code reuse with custom Hooks.
>   * [Making Sense of React Hooks](https://medium.com/@dan_abramov/making-sense-of-react-hooks-fdbde8803889) explores the new possibilities unlocked by Hooks.
>   * [useHooks.com](https://usehooks.com/) showcases community-maintained Hooks recipes and demos.
> 

Be sure to give this a try in your apps. We hope that you find the reuse as exciting as we do.
## 📱 Updated JSC means performance gains and 64-bit support on Android[​](https://reactnative.dev/blog/2019/03/12/releasing-react-native-059#-updated-jsc-means-performance-gains-and-64-bit-support-on-android "Direct link to 📱 Updated JSC means performance gains and 64-bit support on Android")
React Native uses JSC ([JavaScriptCore](https://webkit.org/)) to power your application. JSC on Android was a few years old, which meant that a lot of modern JavaScript features weren't supported. Even worse, it performed poorly compared iOS's modern JSC. With this release, that all changes.
Thanks to some awesome work by [@DanielZlotin](https://github.com/danielzlotin), [@dulmandakh](https://github.com/dulmandakh), [@gengjiawen](https://github.com/gengjiawen), [@kmagiera](https://github.com/kmagiera), and [@kudo](https://github.com/kudo) JSC has caught up with the past few years. This brings with it 64-bit support, modern JavaScript support, and [big performance improvements](https://github.com/react-native-community/jsc-android-buildscripts/tree/master/measure). Kudos for also making this a maintainable process now so that we can take advantage of future WebKit improvements without so much legwork, and thank you Software Mansion and Expo for making this work possible.
## 💨 Faster app launches with inline requires[​](https://reactnative.dev/blog/2019/03/12/releasing-react-native-059#-faster-app-launches-with-inline-requires "Direct link to 💨 Faster app launches with inline requires")
We want to help people have performant React Native apps by default and are working to bring Facebook's optimizations to the community. Applications load resources as needed rather than slowing down launch. This feature is called "inline requires", as it lets Metro identify components to be lazy loaded. Apps with a deep and varied component architecture will see the most improvement.
We need the community to let us know how it works before we turn it on by default. When you upgrade to 0.59, there will be a new `metro.config.js` file; flip the options to true and give us [your feedback](https://twitter.com/hashtag/inline-requires)! Read more about inline requires [in the performance docs](https://reactnative.dev/docs/performance#inline-requires) to benchmark your app.
## 🚅 Lean core is underway[​](https://reactnative.dev/blog/2019/03/12/releasing-react-native-059#-lean-core-is-underway "Direct link to 🚅 Lean core is underway")
React Native is a large and complex project with a complicated repository. This makes the codebase less approachable to contributors, difficult to test, and bloated as a dev dependency. [Lean Core](https://github.com/react-native-community/discussions-and-proposals/issues/6) is our effort to address these issues by migrating code to separate libraries for better management. The past few releases have seen the first steps of this, but [let's get serious](https://www.youtube.com/watch?v=FMLKb4or8yg).
You may notice that additional components are now officially deprecated. This is great news, as there are now owners for these features actively maintaining them. Heed the warning messages and migrate to the new libraries for these features, because they will be removed in a future release. Below is a table indicating the component, its status, and where you may migrate your use to.
Component| Deprecated?| New home  
---|---|---  
**AsyncStorage**|  0.59| [@react-native-community/react-native-async-storage](https://github.com/react-native-community/react-native-async-storage)  
**ImageStore**|  0.59| [expo-file-system](https://github.com/expo/expo/tree/master/packages/expo-file-system) or [react-native-fs](https://github.com/itinance/react-native-fs)  
**MaskedViewIOS**|  0.59| [@react-native-community/react-native-masked-view](https://github.com/react-native-community/react-native-masked-view)  
**NetInfo**|  0.59| [@react-native-community/react-native-netinfo](https://github.com/react-native-community/react-native-netinfo)  
**Slider**|  0.59| [@react-native-community/react-native-slider](https://github.com/react-native-community/react-native-slider)  
**ViewPagerAndroid**|  0.59| [@react-native-community/react-native-viewpager](https://github.com/react-native-community/react-native-viewpager)  
Over the coming months, there will be many more components following this path to a leaner core. We're looking for help with this — head over to the [lean core umbrella](https://github.com/facebook/react-native/issues/23313) to pitch in.
## 👩🏽‍💻 CLI improvements[​](https://reactnative.dev/blog/2019/03/12/releasing-react-native-059#-cli-improvements "Direct link to 👩🏽‍💻 CLI improvements")
React Native's command line tools are developer's entry point to the ecosystem, but they had long-standing issues and lacked official support. The CLI tools have been moved to a [new repository](https://github.com/react-native-community/react-native-cli), and a [dedicated group of maintainers](https://blog.callstack.io/the-react-native-cli-has-a-new-home-79b63838f0e6) have already made some exciting improvements.
Logs are formatted much better now. Commands now run nearly instantly — you'll immediately notice a difference:
## 🚀 Upgrading to 0.59[​](https://reactnative.dev/blog/2019/03/12/releasing-react-native-059#-upgrading-to-059 "Direct link to 🚀 Upgrading to 0.59")
We heard your feedback regarding the [React Native upgrade process](https://github.com/react-native-community/discussions-and-proposals/issues/68) and we are taking steps to improve the experience in [future releases](https://github.com/react-native-community/discussions-and-proposals/issues/64#issuecomment-444775432). To upgrade to 0.59, we recommend using [`rn-diff-purge`](https://github.com/react-native-community/rn-diff-purge) to determine what has changed between your current React Native version and 0.59, then applying those changes manually. Once you've upgraded your project to 0.59, you will be able to use the newly improved `react-native upgrade` command (based on `rn-diff-purge`!) to upgrade to 0.60 and beyond as newer releases become available.
## 🔨 Breaking Changes[​](https://reactnative.dev/blog/2019/03/12/releasing-react-native-059#-breaking-changes "Direct link to 🔨 Breaking Changes")
Android support in 0.59 has been cleaned up following Google's latest recommendations, which may result in potential breakage of existing apps. This issue might present as a runtime crash and a message, "You need to use a Theme.AppCompat theme (or descendant) with this activity". We recommend updating your project's `AndroidManifest.xml` file, making sure that the `android:theme` value is an `AppCompat` theme (such as `@style/Theme.AppCompat.Light.NoActionBar`).
The `react-native-git-upgrade` command has been removed in 0.59, in favor of the newly improved `react-native upgrade` command.
## 🤗 Thanks[​](https://reactnative.dev/blog/2019/03/12/releasing-react-native-059#-thanks "Direct link to 🤗 Thanks")
Lots of new contributors helped with [enabling generation of native code from flow types](https://github.com/facebook/react-native/issues/22990) and [resolving Xcode warnings](https://github.com/facebook/react-native/issues/22609) - these are a great way to learn how React Native works and contributing to the greater good. Thank you! Look out for similar issues in the future.
While these are the highlights that we noted, there are many others to be excited about. To see all of the updates, take a look at the [changelog](https://github.com/react-native-community/react-native-releases/blob/master/CHANGELOG.md). 0.59 is a huge release – we can't wait for you to try it out.
We have even more improvements coming throughout the rest of the year. Stay tuned!
[Ryan](https://github.com/turnrye) and the whole [React Native core team](https://twitter.com/reactnative)
  * [🎣 Hooks are here](https://reactnative.dev/blog/2019/03/12/releasing-react-native-059#-hooks-are-here)
  * [📱 Updated JSC means performance gains and 64-bit support on Android](https://reactnative.dev/blog/2019/03/12/releasing-react-native-059#-updated-jsc-means-performance-gains-and-64-bit-support-on-android)
  * [💨 Faster app launches with inline requires](https://reactnative.dev/blog/2019/03/12/releasing-react-native-059#-faster-app-launches-with-inline-requires)
  * [🚅 Lean core is underway](https://reactnative.dev/blog/2019/03/12/releasing-react-native-059#-lean-core-is-underway)
  * [👩🏽‍💻 CLI improvements](https://reactnative.dev/blog/2019/03/12/releasing-react-native-059#-cli-improvements)
  * [🚀 Upgrading to 0.59](https://reactnative.dev/blog/2019/03/12/releasing-react-native-059#-upgrading-to-059)
  * [🔨 Breaking Changes](https://reactnative.dev/blog/2019/03/12/releasing-react-native-059#-breaking-changes)



