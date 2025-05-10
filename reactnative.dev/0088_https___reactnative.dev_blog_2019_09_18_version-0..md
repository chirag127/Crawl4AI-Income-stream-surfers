---
url: https://reactnative.dev/blog/2019/09/18/version-0.61
title: https://reactnative.dev/blog/2019/09/18/version-0.61
date: 2025-05-10T20:54:13.303523
depth: 2
---

[Skip to main content](https://reactnative.dev/blog/2019/09/18/version-0.61#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
We’re excited to announce React Native 0.61, which includes a new reloading experience we’re calling Fast Refresh.
## Fast Refresh[​](https://reactnative.dev/blog/2019/09/18/version-0.61#fast-refresh "Direct link to Fast Refresh")
When we asked the React Native community about [common pain points](https://github.com/react-native-community/discussions-and-proposals/issues/64), one of the top answers was that the “hot reloading” feature was broken. It didn’t work reliably for function components, often failed to update the screen, and wasn’t resilient to typos and mistakes. We heard that most people turned it off because it was too unreliable.
In React Native 0.61, **we’re unifying the existing “live reloading” (reload on save) and “hot reloading” features into a single new feature called “Fast Refresh”**. Fast Refresh was implemented from scratch with the following principles:
  * Fast Refresh **fully supports modern React** , including function components and Hooks.
  * Fast Refresh **gracefully recovers after typos** and other mistakes, and falls back to a full reload when needed.
  * Fast Refresh **doesn’t perform invasive code transformations** so it’s reliable enough to be on by default.


To see Fast Refresh in action, check out this video:
Give it a try, and let us know what you think! If you prefer, you can turn it off in the Dev Menu (Cmd+D on iOS, Cmd+M or Ctrl+M on Android). Turning it on and off is instant so you can do it any time.
Here are a few Fast Refresh tips:
  * Fast Refresh preserves React local state in function components (and Hooks!) by default.
  * If you need to reset the React state on every edit, you can add a special `// @refresh reset` comment to the file with that component.
  * Fast Refresh always remounts class components without preserving state. This ensures it works reliably.
  * We all make mistakes in the code! Fast Refresh automatically retries rendering after you save a file. You don't need to reload the app manually after fixing a syntax or a runtime error.
  * Adding a `console.log` or a `debugger` statement during edits is a neat debugging technique.


Please report any issues with Fast Refresh on GitHub, and we’ll look into them.
## Other Improvements[​](https://reactnative.dev/blog/2019/09/18/version-0.61#other-improvements "Direct link to Other Improvements")
  * **Fixed use_frameworks! CocoaPods support.** In 0.60 we made some updates to integrate CocoaPods by default. Unfortunately, this broke builds using [use_frameworks!](https://guides.cocoapods.org/syntax/podfile.html#use_frameworks_bang). This is [fixed in 0.61](https://github.com/facebook/react-native/pull/25619), making it easier to integrate React Native into your iOS projects that require building with dynamic frameworks.
  * **Add useWindowDimensions Hook.** This new Hook automatically provides and subscribes to dimension updates, and can be used instead of the Dimensions API in most cases.
  * **React was upgraded to 16.9.** This version deprecates old names for the UNSAFE_ lifecycle methods, contains improvements to `act`, and more. See the [React 16.9 blog post](https://reactjs.org/blog/2019/08/08/react-v16.9.0.html) for an automated migration script and more information.


## Breaking Changes[​](https://reactnative.dev/blog/2019/09/18/version-0.61#breaking-changes "Direct link to Breaking Changes")
  * **Remove React .xcodeproj.** In 0.60, we introduced auto-linking support via CocoaPods. We have also integrated CocoaPods into the e2e tests runs, so that from now on, we have a unified standard way of integrating RN into iOS apps. This effectively deprecates the React .xcodeproj support, and the file has been removed starting 0.61. Note: if you use 0.60 auto-linking already, you shouldn't be affected.


## Thanks[​](https://reactnative.dev/blog/2019/09/18/version-0.61#thanks "Direct link to Thanks")
Thanks to all of the contributors that helped make 0.61 possible!
To see all the updates, take a look at the [0.61 changelog](https://github.com/facebook/react-native/blob/main/CHANGELOG.md#v0610).
  * [Other Improvements](https://reactnative.dev/blog/2019/09/18/version-0.61#other-improvements)
  * [Breaking Changes](https://reactnative.dev/blog/2019/09/18/version-0.61#breaking-changes)



