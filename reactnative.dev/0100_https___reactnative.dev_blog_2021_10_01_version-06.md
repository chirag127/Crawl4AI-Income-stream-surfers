---
url: https://reactnative.dev/blog/2021/10/01/version-066
title: https://reactnative.dev/blog/2021/10/01/version-066
date: 2025-05-10T21:34:14.638982
depth: 2
---

[Skip to main content](https://reactnative.dev/blog/2021/10/01/version-066#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
Today we’re releasing React Native v0.66 for Android 12 and iOS 15 support alongside fixes and general updates.
## Highlights[​](https://reactnative.dev/blog/2021/10/01/version-066#highlights "Direct link to Highlights")
  * [Handle taps on views outside parent bounds on Android](https://reactnative.dev/blog/2021/10/01/version-066#handle-taps-on-child-views-outside-parent-boundaries-on-android)
  * [New Bluetooth Permissions on Android](https://reactnative.dev/blog/2021/10/01/version-066#new-bluetooth-permissions-on-android)
  * [Better Support for Apple Silicon, Xcode 13, and iOS 15](https://reactnative.dev/blog/2021/10/01/version-066#better-support-for-apple-silicon-xcode-13-and-ios-15)
  * [Nightly and “Commitly” Releases](https://reactnative.dev/blog/2021/10/01/version-066#nightly-and-commitly-releases)


### Handle taps on child views outside parent boundaries on Android[​](https://reactnative.dev/blog/2021/10/01/version-066#handle-taps-on-child-views-outside-parent-boundaries-on-android "Direct link to Handle taps on child views outside parent boundaries on Android")
Thanks to [@hsource](https://github.com/hsource) for adding interaction support for children rendered outside of parent view boundaries via `overflow: visible`. This is a common use-case and aligns React Native on Android more closely with web standards.
Find more details on the [pull request](https://github.com/facebook/react-native/pull/29039).
### New Bluetooth Permissions on Android[​](https://reactnative.dev/blog/2021/10/01/version-066#new-bluetooth-permissions-on-android "Direct link to New Bluetooth Permissions on Android")
We’ve added support for [new Bluetooth permissions](https://developer.android.com/about/versions/12/features/bluetooth-permissions) in preparation for Android 12 and we plan to update the `targetSDKVersion` to 31 in the next release.
### Better Support for Apple Silicon, Xcode 13, and iOS 15[​](https://reactnative.dev/blog/2021/10/01/version-066#better-support-for-apple-silicon-xcode-13-and-ios-15 "Direct link to Better Support for Apple Silicon, Xcode 13, and iOS 15")
This release provides a number of solutions to make Xcode builds for iOS on Apple Silicon (M1) Mac machines more reliable.
Notably, the new app template now includes a CocoaPods workaround (thanks to [@mikehardy](https://github.com/MikeHardy)!). To apply, make sure your app’s Podfile has `__apply_Xcode_12_5_M1_post_install_workaround(installer)` added in the `post_install` step.
In addition `RCT-Folly.podspec` has been [updated to prevent arm64 linker failure](https://github.com/facebook/react-native/commit/8b6d7fddd65a9b5caf599e8ff7b090a176a6f11f).
Check out this [post](https://reactnative.dev/blog/2021/09/01/preparing-your-app-for-iOS-15-and-android-12) we shared on preparing your app for iOS 15 and Android 12.
### Hermes 0.9.0[​](https://reactnative.dev/blog/2021/10/01/version-066#hermes-090 "Direct link to Hermes 0.9.0")
Hermes 0.9.0 is primarily about closing the gap between Hermes release cut point and this React Native release.
Among ~400 commits, there have been general bug fixes alongside memory and size wins.
See [Hermes 0.9.0 release issue](https://github.com/facebook/hermes/issues/586) for more details
### Nightly and “Commitly” Releases[​](https://reactnative.dev/blog/2021/10/01/version-066#nightly-and-commitly-releases "Direct link to Nightly and “Commitly” Releases")
In a [recent blog post](https://reactnative.dev/blog/2021/08/19/h2-2021) we shared that one of our goals in the second half of 2021 is to improve our release process to be faster and more stable. As part of this effort we are working to make React Native more stable on main and to reduce the bugs identified during our Release Candidate process.
While we have been publishing nightly releases of React Native for over a year, these releases haven’t been effectively used by most projects. They are now easier to access and we hope to use them as release candidates going forward. Nightly releases are published to npm under the “nightly” tag.
To improve the process of testing individual commits, React Native’s CI will now create a tarball artifact for each commit on the main and release branches as well as for each PR. We refer to them as commitlies. These commitlies will not be published to npm, but they can be downloaded directly from CircleCI. See instructions below.
Want to help get a PR merged? By trying out the related commitly and verifying the change, you will be providing valuable signal to help get the change landed!
#### Using Nightly Releases (Nightlies)[​](https://reactnative.dev/blog/2021/10/01/version-066#using-nightly-releases-nightlies "Direct link to Using Nightly Releases \(Nightlies\)")
The process for migrating your project to a React Native nightly release is very similar to the one you would follow when upgrading to a regular version, with the exception that tools like the Upgrade Helper do not currently work with nightlies. With that in mind, we recommend that you first upgrade your project to the most recent stable release if you have not done so yet. Then, run `yarn upgrade react-native@nightly` to install the most recent nightly release. Note that there may be additional changes that are needed for your project to work properly on a nightly release.
#### Using Commitly Releases (Commitlies)[​](https://reactnative.dev/blog/2021/10/01/version-066#using-commitly-releases-commitlies "Direct link to Using Commitly Releases \(Commitlies\)")
Find the "build_npm_package-1" job related to a commit and head to the "Artifacts" panel to download the tarball for the commitly.
Just like with a nightly release, first make sure that your project has been upgraded to the most recent stable version. Then, go to the [`react-native` dashboard on Circle CI](https://app.circleci.com/pipelines/github/facebook/react-native) and look up the workflow that was triggered by the commit in question. There, you should see a job named `build_npm_package`. That job will have an “Artifacts” panel which will provide a link that you may use to download a tarball file. You can then run the following:
```
# Update your react-native dependency to the tarball# using your preferred package manager$ yarnadd<path to tarball>$ npmadd<path to tarball>
```

### Acknowledgements[​](https://reactnative.dev/blog/2021/10/01/version-066#acknowledgements "Direct link to Acknowledgements")
This release includes **621 commits** with **92 contributors**! Thank you to all our contributors new and old! You can find the [full changelog here](https://github.com/facebook/react-native/blob/main/CHANGELOG.md#v0660).
As well, thank you to the following contributors for their support in preparing, testing and unblocking this release!


  * [Highlights](https://reactnative.dev/blog/2021/10/01/version-066#highlights)
    * [Handle taps on child views outside parent boundaries on Android](https://reactnative.dev/blog/2021/10/01/version-066#handle-taps-on-child-views-outside-parent-boundaries-on-android)
    * [New Bluetooth Permissions on Android](https://reactnative.dev/blog/2021/10/01/version-066#new-bluetooth-permissions-on-android)
    * [Better Support for Apple Silicon, Xcode 13, and iOS 15](https://reactnative.dev/blog/2021/10/01/version-066#better-support-for-apple-silicon-xcode-13-and-ios-15)
    * [Hermes 0.9.0](https://reactnative.dev/blog/2021/10/01/version-066#hermes-090)
    * [Nightly and “Commitly” Releases](https://reactnative.dev/blog/2021/10/01/version-066#nightly-and-commitly-releases)
    * [Acknowledgements](https://reactnative.dev/blog/2021/10/01/version-066#acknowledgements)



