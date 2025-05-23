---
url: https://reactnative.dev/blog/2022/03/30/version-068
title: https://reactnative.dev/blog/2022/03/30/version-068
date: 2025-05-10T20:54:51.431637
depth: 2
---

[Skip to main content](https://reactnative.dev/blog/2022/03/30/version-068#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
Hello everyone! Today we are announcing the 0.68.0 release of React Native, with opt-in to the New React Native Architecture, bug fixes and more.
### Sections[​](https://reactnative.dev/blog/2022/03/30/version-068#sections "Direct link to Sections")
  * [Highlights of 0.68](https://reactnative.dev/blog/2022/03/30/version-068#highlights-of-068)
  * [Opting in to the New Architecture](https://reactnative.dev/blog/2022/03/30/version-068#opting-in-to-the-new-architecture)
  * [Interested in helping React Native stabilise new releases?](https://reactnative.dev/blog/2022/03/30/version-068#interested-in-helping-react-native-stabilize-new-releases)


## Highlights of 0.68[​](https://reactnative.dev/blog/2022/03/30/version-068#highlights-of-068 "Direct link to Highlights of 0.68")
[Andrei Calazans](https://twitter.com/Andrei_Calazans) helped us selecting the most relevant changes that 0.68 brings along:
### Breaking changes and version bumps[​](https://reactnative.dev/blog/2022/03/30/version-068#breaking-changes-and-version-bumps "Direct link to Breaking changes and version bumps")
This version brings along a few breaking changes:
  * React Native has been updated to Node 16, the latest LTS. Since on CI we test for LTS and the previous LTS, this change means that users are now required to use a version of Node >= 14.
  * Android Gradle Plugin was updated to 7.0.1, enforcing JDK 11 for Android builds, so make sure to upgrade your configurations (we recommend you use the `zulu11` JDK flavor for both Intel and M1 Macs)
  * Removed `fallbackResource` from `RCTBundleURLProvider` API on iOS. This parameter can be safely removed from the method call without replacement.


Tooling has also been updated - here are the main bumps:
  * @react-native-community/cli to 7.0.3
  * Metro to 0.67
  * react-devtools-core dependency to 4.23.0
  * Flipper to 0.125.0
  * react-native-codegen to 0.0.9
  * Kotlin to 1.6.10
  * Soloader to 0.10.3
  * Gradle to 7.3
  * Android compile and target SDK to 31


Also, thanks to [this commit](https://github.com/facebook/react-native/commit/bd7caa64f5d6ee5ea9484e92c3629c9ce711f73c) by [Nicola Corti](https://github.com/cortinico) the Android Gradle Plugin will download the default version of NDK by itself, so you don’t have to specify and install it separately anymore.
### Other improvements[​](https://reactnative.dev/blog/2022/03/30/version-068#other-improvements "Direct link to Other improvements")
There are a lot of other changes and fixes landed in this release, but here’s a small selection that you might be interested in:
  * [Gijs Weterings](https://github.com/GijsWeterings) [fixed Forwarding testID to RCTModalHostView](https://github.com/facebook/react-native/commit/5050e7eaa17cb417baf7c20eb5c4406cce6790a5) for easier E2E targeting of Modals.
  * [Liam Jones](https://github.com/liamjones) [fixed an issue](https://github.com/facebook/react-native/commit/9d2df5b8ae9) where calling `console.error` caused the RedBox to appear alongside the LogBox.
  * [Sam Kline](https://github.com/samkline) [fixed the empty blank screen](https://github.com/facebook/react-native/commit/c8d823b9bd9619dfa1f5851af003cc24ba2e8830) after a BundleDownloader failure in dev mode on Android.
  * [Jeffrey Hyer](https://github.com/JeffreyHyer) [fixed an issue](https://github.com/facebook/react-native/commit/9c5e177a79c) where the KeyboardAvoidingView didn't work as expected with the `onLayout` prop.


If you are interested in the full list of changes, you can read it in the changelog [at the link here](https://github.com/facebook/react-native/blob/main/CHANGELOG.md#0680).
### Acknowledgements[​](https://reactnative.dev/blog/2022/03/30/version-068#acknowledgements "Direct link to Acknowledgements")
This release includes 614 commits by 68 contributors! Thank you all!
We wanted to also thank the release testers and supporters who helped us catch regressions before the stable 0.68.0 release: you are incredibly valuable to the success of this release!
If you, your app or your company is interested in joining the “Release Tester” program, you can [sign up here](https://forms.gle/fPuPE1MZRDGWNqpd6).
## Opting in to the New Architecture[​](https://reactnative.dev/blog/2022/03/30/version-068#opting-in-to-the-new-architecture "Direct link to Opting in to the New Architecture")
As briefly mentioned above, React Native 0.68 is the first version with opt-in support for the Fabric Renderer and the TurboModule system. This marks a crucial milestone for the rollout of the New React Native Architecture. To help you get up to speed with the changes, we added [the Architecture section](https://reactnative.dev/architecture/overview) to the website, where you can find several in-depth guides about internals of the new systems.
At the same time, we added the [migration guide](https://github.com/reactwg/react-native-new-architecture#guides) to the documentation and launched [a working group](https://github.com/reactwg/react-native-new-architecture) dedicated to the New Architecture. You can find more information, including how to opt in, in [the previous blog post](https://reactnative.dev/blog/2022/03/15/an-update-on-the-new-architecture-rollout).
Please note that the New Architecture still needs some fine tuning. Some of the third-party libraries that you depend on might not be migrated yet, and you may encounter issues that we haven’t discovered yet. If you do so, please report them to our [New Architecture Working Group](https://github.com/reactwg/react-native-new-architecture).
**About React 18:** React 18's new rendering engine is not supported by React Native 0.68, this will happen in a future version. This is because React 18 relies on the New Architecture to benefit from the new capabilities presented in [the React 18 announcement blog post](https://reactjs.org/blog/2022/03/29/react-v18.html). For more information, see the [React Conf keynote here](https://www.youtube.com/watch?v=FZ0cG47msEk&t=1530s).
## Website updates[​](https://reactnative.dev/blog/2022/03/30/version-068#website-updates "Direct link to Website updates")
Along with improvements to the main codebase, with the help of [Simek](https://github.com/Simek), [Megatron4537](https://github.com/Megatron4537) and [slorber](https://github.com/slorber) there have been quite a few improvements landing on the website too! In particular, you will now be able to learn how to contribute to React Native via the new section in the top toolbar. Moreover, the “Contributing” section and the new “Architecture” section are now unversioned — there is now only one copy of these sections, rather than one for each React Native version.
  * [Highlights of 0.68](https://reactnative.dev/blog/2022/03/30/version-068#highlights-of-068)
    * [Breaking changes and version bumps](https://reactnative.dev/blog/2022/03/30/version-068#breaking-changes-and-version-bumps)
    * [Other improvements](https://reactnative.dev/blog/2022/03/30/version-068#other-improvements)
    * [Acknowledgements](https://reactnative.dev/blog/2022/03/30/version-068#acknowledgements)
  * [Opting in to the New Architecture](https://reactnative.dev/blog/2022/03/30/version-068#opting-in-to-the-new-architecture)
  * [Website updates](https://reactnative.dev/blog/2022/03/30/version-068#website-updates)



