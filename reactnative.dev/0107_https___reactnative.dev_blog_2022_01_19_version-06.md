---
url: https://reactnative.dev/blog/2022/01/19/version-067
title: https://reactnative.dev/blog/2022/01/19/version-067
date: 2025-05-10T20:54:37.601532
depth: 2
---

[Skip to main content](https://reactnative.dev/blog/2022/01/19/version-067#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
Happy new year everyone! Today we are announcing the latest release of React Native, 0.67.0, along with some updates on the release process that we have been working on in the past few months.
### Sections[​](https://reactnative.dev/blog/2022/01/19/version-067#sections "Direct link to Sections")
  * [Highlights of 0.67](https://reactnative.dev/blog/2022/01/19/version-067#highlights-of-067)
  * [Improvements to Release Process](https://reactnative.dev/blog/2022/01/19/version-067#improvements-to-release-process)
  * [Interested in helping React Native stabilise new releases?](https://reactnative.dev/blog/2022/01/19/version-067#interested-in-helping-react-native-stabilise-new-releases)


## Highlights of 0.67[​](https://reactnative.dev/blog/2022/01/19/version-067#highlights-of-067 "Direct link to Highlights of 0.67")
As mentioned in Meta's [H2 2021 plans](https://reactnative.dev/blog/2021/08/19/h2-2021), React Native is attempting more frequent releases for a shorter turnaround time for new features and fixes (like the new architecture) to land in the community. Naturally, many releases will focus on fixes and improvements.
Here are some notable changes coming in 0.67.0:
  * Lean-core removals: [DatePickerAndroid](https://github.com/facebook/react-native/commit/7a770526c626e6659a12939f8c61057a688aa623#diff-e727e4bdf3657fd1d798edcd6b099d6e092f8573cba266154583a746bba0f346)
  * Bump Gradle version to 7.2, Bump Kotlin version to 1.5.31 [Bump Kotlin and Gradle versions (#32319)](https://github.com/facebook/react-native/commit/9ae3367431428748f5486c782199beb4f9c6b477)
  * A notable callout: 0.67 continues to depend on Hermes 0.9.0, unchanged from 0.66


You can find the [full changelog here](https://github.com/facebook/react-native/blob/main/CHANGELOG.md#v0670).
You can participate in the conversation on the status of this release at [this discussion](https://github.com/reactwg/react-native-releases/discussions/10) - and, as always, to help you upgrade to this version, you can use the [upgrade helper](https://react-native-community.github.io/upgrade-helper/) ⚛️
### Acknowledgements[​](https://reactnative.dev/blog/2022/01/19/version-067#acknowledgements "Direct link to Acknowledgements")
This release includes [379 commits with 74 contributors](https://github.com/facebook/react-native/compare/0.66-stable...0.67-stable)! Thank you, to all our contributors (old and new)! You can find the [full changelog here](https://github.com/facebook/react-native/blob/main/CHANGELOG.md#v0670).
We wanted to also thank the release testers who helped us make sure that 0.67.0 could reach your codebases without any massive regression. Specifically, we wanted to thank:
  * Marc Rousavy ([@mrousavy](https://github.com/mrousavy)) from [Margelo](https://margelo.io/), that surfaced a [regression for Hermes 0.10](https://github.com/facebook/hermes/issues/649) (that would have never been caught on CI testing) which will be fixed in Hermes 0.11 in the 0.68 release of React Native.
  * The Reanimated team for quickly preparing a [0.67 compatible version](https://github.com/software-mansion/react-native-reanimated/releases/tag/2.2.4) of their lib early in the 0.67 RC phase.
  * Elias Nahum ([@enahum](https://github.com/enahum)) from [Mattermost](https://mattermost.com/)
  * Mike Hardy ([@mikeHardy](https://github.com/mikeHardy)) working with [Invertase](https://invertase.io/)


We appreciate also [Rainbow](https://rainbow.me/), [Comm](https://comm.app/) and [Ledger Live](https://www.ledger.com/ledger-live) for also being part of the pilot of the "Release Tester" program (more details below).
## Improvements to Release Process[​](https://reactnative.dev/blog/2022/01/19/version-067#improvements-to-release-process "Direct link to Improvements to Release Process")
As mentioned, React Native has been restructuring the release pipeline to allow for more frequent releases such that new features and fixes can roll out faster to the community.
Over the last few months we tackled some issues that delay releases.
### Coordination and Knowledge Sharing[​](https://reactnative.dev/blog/2022/01/19/version-067#coordination-and-knowledge-sharing "Direct link to Coordination and Knowledge Sharing")
We invested in our documentation of releases to cover how to run a release, FAQs, coordination of release issues, etc – all of which can be found in this section of the [react-native wiki](https://github.com/facebook/react-native/wiki/Releases). By documentation, releases are no longer blocked on any individual or tribal knowledge.
In addition to documentation, we have also revamped the coordination of releases and have moved discussion of pre-release status and patches to a dedicated discussion group: [react-wg/react-native-releases](https://github.com/reactwg/react-native-releases/discussions).
### Clarity of responsibility[​](https://reactnative.dev/blog/2022/01/19/version-067#clarity-of-responsibility "Direct link to Clarity of responsibility")
Following more documentation, release work can scale such that no one person is critical to running a release.
A React Native release is susceptible to a broad spectrum of potential points of failure and has a lot of dependencies and follow-up. Considering that usage of React Native varies across the community, it’s essential to have stakeholders involved in releases. We have defined a set of [roles and responsibilities in supporting a release](https://github.com/facebook/react-native/wiki/Release-Roles-and-Responsibilities).
### Release candidate signal[​](https://reactnative.dev/blog/2022/01/19/version-067#release-candidate-signal "Direct link to Release candidate signal")
Another issue with releases is getting a good signal that a release will not suffer from build regressions. This can be addressed with growing investment in testing build variants, etc. but signal from adoption will continue to be useful for some time.
In the 0.67 release we piloted a “Release Tester” program where React Native developers working on Open Source apps [commit to testing release candidates](https://github.com/facebook/react-native/wiki/Release-Roles-and-Responsibilities#release-tester-responsibilities) on their apps. Prior, there was no formal expectation that the community will test out release candidates to raise any potential issues. This program helps us get faster signal to ensure a level of stability of the release.
Open source React Native apps are particularly useful due to availability of source code to help debug any regressions. With this program in place, a release tester surfaced a regression in 0.67 and we were able to resolve it without thrashing the larger community with a faulty release.
## Interested in helping React Native stabilise new releases?[​](https://reactnative.dev/blog/2022/01/19/version-067#interested-in-helping-react-native-stabilise-new-releases "Direct link to Interested in helping React Native stabilise new releases?")
A great way to help us catch regressions is to integrate the React Native pre-release version [`react-native@next`](https://www.npmjs.com/package/react-native) or [`react-native@nightly`](https://www.npmjs.com/package/react-native) to your CI. For any regressions, you can [file a release issue](https://github.com/facebook/react-native/issues/new?assignees=&labels=Needs%3A+Triage+%3Amag%3A%2CType%3A+Upgrade+Issue&template=upgrade-regression-form.yml) and notify the appropriate discussion.
If your app or company is interested in joining the “Release Tester” program, head to the dedicated section at the bottom of the [Release Roles and Responsibilities wiki](https://github.com/facebook/react-native/wiki/Release-Roles-and-Responsibilities#release-tester-responsibilities) to learn more.
Lastly any help on trying our release candidates or helping unblock release issues is much appreciated!
  * [Highlights of 0.67](https://reactnative.dev/blog/2022/01/19/version-067#highlights-of-067)
    * [Acknowledgements](https://reactnative.dev/blog/2022/01/19/version-067#acknowledgements)
  * [Improvements to Release Process](https://reactnative.dev/blog/2022/01/19/version-067#improvements-to-release-process)
    * [Coordination and Knowledge Sharing](https://reactnative.dev/blog/2022/01/19/version-067#coordination-and-knowledge-sharing)
    * [Clarity of responsibility](https://reactnative.dev/blog/2022/01/19/version-067#clarity-of-responsibility)
    * [Release candidate signal](https://reactnative.dev/blog/2022/01/19/version-067#release-candidate-signal)
  * [Interested in helping React Native stabilise new releases?](https://reactnative.dev/blog/2022/01/19/version-067#interested-in-helping-react-native-stabilise-new-releases)



