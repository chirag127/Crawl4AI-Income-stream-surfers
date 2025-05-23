---
url: https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks
title: https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks
date: 2025-05-10T20:54:45.113045
depth: 2
---

[Skip to main content](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
Today we’re releasing 0.72!
This release adds highly requested features for Metro, better error handling, and other developer experience improvements. So much of this work was prioritized from your feedback on the [2022 community survey](https://github.com/react-native-community/discussions-and-proposals/discussions/528) -- thank you to all those that participated!
### Highlights[​](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#highlights "Direct link to Highlights")
  * [Developer Experience Improvements](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#developer-experience-improvements)
  * [Moving New Architecture Updates](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#moving-new-architecture-updates)


### Breaking Changes[​](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#breaking-changes "Direct link to Breaking Changes")
  * [Deprecated Component Removals](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#deprecated-component-removals)


## Highlights[​](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#highlights-1 "Direct link to Highlights")
### New Metro Features[​](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#new-metro-features "Direct link to New Metro Features")
#### Symlink Support (Beta)[​](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#symlink-support-beta "Direct link to Symlink Support \(Beta\)")
Symlink support continues to be one of the top-requested features in Metro and, in React Native 0.72, we are happy to announce beta support for it.
Symlink support enables React Native to work transparently with monorepo setups and pnpm, removing the need for workarounds. See [Enabling Beta Features](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#enabling-beta-features) to use in your app.
It is currently in beta to collect feedback on developer experience given varying workflows, see more details [here](https://twitter.com/robjhogan/status/1672293540632641554). We plan to default enable symlinks in 0.73.
#### Package Exports Support (Beta)[​](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#package-exports-support-beta "Direct link to Package Exports Support \(Beta\)")
[Package Exports](https://nodejs.org/api/packages.html#exports) is the modern alternative to the package.json `"main"` field and provides new capabilities for npm packages to define their public API and target React Native.
By enabling Package Exports support in your Metro config, your app will be compatible with the wider JavaScript ecosystem, including via the new ["react-native" community condition](https://nodejs.org/docs/latest-v19.x/api/packages.html#community-conditions-definitions). See [Enabling Beta Features](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#enabling-beta-features) to use in your app.
tip
See [Package Exports Support in React Native](https://reactnative.dev/blog/2023/06/21/package-exports-support) to learn more about this feature and our plans for stable rollout.
#### Enabling Beta Features[​](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#enabling-beta-features "Direct link to Enabling Beta Features")
To enable these features in your project, update your app’s `metro.config.js` file and set either the `resolver.unstable_enableSymlinks` or `resolver.unstable_enablePackageExports` options.
```
const config ={// ...resolver:{unstable_enableSymlinks:true,unstable_enablePackageExports:true,
```

#### New `metro.config.js` Setup[​](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#new-metroconfigjs-setup "Direct link to new-metroconfigjs-setup")
In React Native 0.72, we’ve changed the config loading setup for Metro in React Native CLI. Please update your project’s `metro.config.js` file to match the [template’s version](https://github.com/facebook/react-native/blob/76a42c292de838a0dd537935db792eaa81410b9b/packages/react-native/template/metro.config.js).
info
Please update your config file to the following [format](https://github.com/facebook/react-native/blob/76a42c292de838a0dd537935db792eaa81410b9b/packages/react-native/template/metro.config.js). You can also follow the [upgrade-helper](https://react-native-community.github.io/upgrade-helper/?from=0.71.8&to=0.72.0).
These format changes to `metro.config.js` will become required in 0.73. For 0.72, we will log a warning if not updated.
This moves control over extending the base React Native Metro config into your project, and we’ve cleaned up the leftover defaults. In addition, this means that standalone Metro CLI commands, such as `metro get-dependencies`, will now work.
### Developer Experience Improvements[​](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#developer-experience-improvements "Direct link to Developer Experience Improvements")
#### No more redboxes with invalid style properties[​](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#no-more-redboxes-with-invalid-style-properties "Direct link to No more redboxes with invalid style properties")
Prior to this release, providing an invalid style property in StyleSheet would result in a redbox. This is a high signal error that disrupts the developer workflow for a relatively low-risk error.
In 0.72, we’ve relaxed this expectation to fail silently, like providing an invalid CSS property in the browser, and have updated types such that some errors may be caught in build-time vs. run-time.
#### Better error readability for Hermes[​](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#better-error-readability-for-hermes "Direct link to Better error readability for Hermes")
Hermes has added a better error message when invoking an undefined callable.
```
var x =undefined;x();// Before: undefined is not a function// After: x is not a function (it is undefined)
```

In addition, LogBox stack traces now filter out internal Hermes bytecode frames that are not relevant to app users.
#### Improved error output of the React Native CLI[​](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#improved-error-output-of-the-react-native-cli "Direct link to Improved error output of the React Native CLI")
0.72 ships with React Native CLI v11 which includes improvements to reduce duplication, clarify wording, reduce verbose stack traces, and add deep links to relevant docs in the following commands `init`, `run-android`, and `run-ios`.
You can find other improvements in the [React Native CLI changelogs](https://github.com/react-native-community/cli/releases).
#### Faster Compilation and JSON Parsing in Hermes[​](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#faster-compilation-and-json-parsing-in-hermes "Direct link to Faster Compilation and JSON Parsing in Hermes")
Hermes has improved the compilation time of large object literals. For example, in one reported issue, [#852](https://github.com/facebook/hermes/issues/852), a user had an entire dataset written out as a large object literal. By improving the de-duplication algorithm Hermes uses, compilation sped up by 97% ([221c](https://github.com/facebook/hermes/commit/221ce21a209e2e32a3eaaa2d9e28ca81842fad20)). These improvements will benefit build times for apps that bundle many objects.
Multiple optimizations ([de9c](https://github.com/facebook/hermes/commit/de9cff2aa41fc1f297b568848143347823d73659), [6e2d](https://github.com/facebook/hermes/commit/6e2dd652c8d90c5d59737a81f66a259efffdcd00)) to JSON parsing have also landed, benefiting apps using libraries like redux-persist that rely heavily on JSON manipulation.
#### More ECMAScript Support in Hermes[​](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#more-ecmascript-support-in-hermes "Direct link to More ECMAScript Support in Hermes")
Support for the following specifications in Hermes has landed in React Native 0.72:
  * `prototype.at` support for [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/at), [TypedArray](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/at) and [String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/at). See [#823](https://github.com/facebook/hermes/issues/823) ([ebe2](https://github.com/facebook/hermes/commit/ebe2915ac386a6b73dec39c2af4ac7063e68cd99)).
  * Implement [well-formed JSON.stringify](https://github.com/tc39/proposal-well-formed-stringify) ([d41d](https://github.com/facebook/hermes/commit/d41decf244aa814b1e58827a9de982f3b71667de)) to prevent ill-formed Unicode strings
  * Implement [AggregateError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AggregateError) ([9b25](https://github.com/facebook/hermes/commit/9b25a2530eb515f6c4fbd397ae290b6c97c049b2)) that represents several errors wrapped in a single error. Useful for multiple errors like from [`Promise.any()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/any) when all promises passed to it reject.


For users on JSC, these features are already available.
### Moving New Architecture Updates[​](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#moving-new-architecture-updates "Direct link to Moving New Architecture Updates")
The New Architecture is currently experimental. To keep updates focused to their target audience, we are moving New Architecture updates in 0.72, and future releases, to the dedicated [working group](https://github.com/reactwg/react-native-new-architecture/discussions). This change will also allow for more frequent updates, such as work that ships in our nightlies.
You can read the 0.72 updates for the New Architecture [here](https://github.com/reactwg/react-native-new-architecture/discussions/136). Subscribe to the working group GitHub notifications to stay informed on our progress on the New Architecture.
## Breaking Changes[​](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#breaking-changes-1 "Direct link to Breaking Changes")
### Deprecated Component Removals[​](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#deprecated-component-removals "Direct link to Deprecated Component Removals")
The following packages have been removed from React Native in 0.72. Please migrate to the recommended community package:
  * [Slider](https://reactnative.dev/docs/0.72/slider) is superseded by [@react-native-community/slider](https://github.com/callstack/react-native-slider/tree/main/package)
  * [DatePickerIOS](https://reactnative.dev/docs/0.72/datepickerios) is superseded by [@react-native-community/datetimepicker](https://github.com/react-native-datetimepicker/datetimepicker)
  * [ProgressViewIOS](https://reactnative.dev/docs/0.72/progressviewios) is superseded by [@react-native-community/progress-view](https://github.com/react-native-progress-view/progress-view)


### Package Renames[​](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#package-renames "Direct link to Package Renames")
All packages published from the [`react-native`](https://github.com/facebook/react-native) core repository now live under `react-native/packages`, and are published under the [@react-native npm scope](https://www.npmjs.com/search?q=%40react-native) to ensure clear ownership.
There are no changes to the [react-native](https://www.npmjs.com/package/react-native) package.
Old Package Name| New Package Name  
---|---  
`@react-native-community/eslint-config`| `@react-native/eslint-config`  
`@react-native-community/eslint-plugin`| `@react-native/eslint-plugin`  
`@react-native/polyfills`| `@react-native/js-polyfills`  
`@react-native/normalize-color`| `@react-native/normalize-colors`  
`@react-native/assets`| `@react-native/assets-registry`  
`react-native-codegen`| `@react-native/codegen`  
`react-native-gradle-plugin`| `@react-native/gradle-plugin`  
This change will not affect you if you have no direct dependency on a renamed package. Otherwise, when upgrading to React Native 0.72, update any renamed dependency to its ~0.72 version.
You can read the motivation that led to these changes [in the dedicated RFC](https://github.com/react-native-community/discussions-and-proposals/pull/480).
## Acknowledgements[​](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#acknowledgements "Direct link to Acknowledgements")
A lot of this release came from the direct feedback from the community. From reports on [noisy redboxes](https://twitter.com/baconbrix/status/1623039650775371792), [bugs with Package Exports](https://github.com/facebook/metro/issues/965), [benchmarks for the New Architecture](https://github.com/reactwg/react-native-new-architecture/discussions/85) — all of it is valuable to hear and we appreciate the time it takes to share feedback.
0.72 contains over [1100 commits](https://github.com/facebook/react-native/compare/v0.71.8...v0.72.0) from 66 contributors. Thank you for all your hard work!
## Upgrade to 0.72[​](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#upgrade-to-072 "Direct link to Upgrade to 0.72")
Check out the list of needed changes in the [upgrade-helper](https://react-native-community.github.io/upgrade-helper/), or read the [upgrade documentation](https://reactnative.dev/docs/upgrading) for how to update your existing project, or create a new project with `npx react-native@latest init MyProject`.
If you use Expo, React Native version 0.72 will be supported in the Expo SDK 49 release.
info
0.72 is now the latest stable version of React Native and 0.69.x version moves now to unsupported. For more information see [React Native’s support policy](https://github.com/reactwg/react-native-releases#releases-support-policy).
  * [Breaking Changes](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#breaking-changes)
  * [Highlights](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#highlights-1)
    * [New Metro Features](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#new-metro-features)
    * [Developer Experience Improvements](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#developer-experience-improvements)
    * [Moving New Architecture Updates](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#moving-new-architecture-updates)
  * [Breaking Changes](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#breaking-changes-1)
    * [Deprecated Component Removals](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#deprecated-component-removals)
    * [Package Renames](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#package-renames)
  * [Acknowledgements](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#acknowledgements)
  * [Upgrade to 0.72](https://reactnative.dev/blog/2023/06/21/0.72-metro-package-exports-symlinks#upgrade-to-072)



