---
url: https://reactnative.dev/docs/hermes
title: https://reactnative.dev/docs/hermes
date: 2025-05-10T21:40:20.493591
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/hermes#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
[Hermes](https://hermesengine.dev) is an open-source JavaScript engine optimized for React Native. For many apps, using Hermes will result in improved start-up time, decreased memory usage, and smaller app size when compared to JavaScriptCore. Hermes is used by default by React Native and no additional configuration is required to enable it.
## Bundled Hermes[​](https://reactnative.dev/docs/hermes#bundled-hermes "Direct link to Bundled Hermes")
React Native comes with a **bundled version** of Hermes. We are building a version of Hermes for you whenever we release a new version of React Native. This will make sure you're consuming a version of Hermes which is fully compatible with the version of React Native you're using.
This change is fully transparent to users of React Native. You can still disable Hermes using the command described in this page. You can [read more about the technical implementation on this page](https://reactnative.dev/architecture/bundled-hermes).
## Confirming Hermes is in use[​](https://reactnative.dev/docs/hermes#confirming-hermes-is-in-use "Direct link to Confirming Hermes is in use")
If you've recently created a new app from scratch, you should see if Hermes is enabled in the welcome view:
A `HermesInternal` global variable will be available in JavaScript that can be used to verify that Hermes is in use:
jsx
```
constisHermes=()=>!!global.HermesInternal;
```

caution
If you are using a non-standard way of loading the JS bundle, it is possible that the `HermesInternal` variable is available but you aren't using the highly optimised pre-compiled bytecode. Confirm that you are using the `.hbc` file and also benchmark the before/after as detailed below.
To see the benefits of Hermes, try making a release build/deployment of your app to compare. For example; from the root of your project:
  * Android
  * iOS


  * npm
  * Yarn


shell
```
npm run android -- --mode="release"
```

shell
```
yarn android --mode release
```

  * npm
  * Yarn


shell
```
npm run ios -- --mode="Release"
```

shell
```
yarn ios --mode Release
```

This will compile JavaScript to Hermes Bytecode during build time which will improve your app's startup speed on device.
## Switching back to JavaScriptCore[​](https://reactnative.dev/docs/hermes#switching-back-to-javascriptcore "Direct link to Switching back to JavaScriptCore")
React Native also supports using JavaScriptCore as the [JavaScript engine](https://reactnative.dev/docs/javascript-environment). Follow these instructions to opt-out of Hermes.
### Android[​](https://reactnative.dev/docs/hermes#android "Direct link to Android")
Edit your `android/gradle.properties` file and flip `hermesEnabled` back to false:
diff
```
# Use this property to enable or disable the Hermes JS engine.# If set to false, you will be using JSC instead.hermesEnabled=false
```

### iOS[​](https://reactnative.dev/docs/hermes#ios "Direct link to iOS")
Edit your `ios/Podfile` file and make the change illustrated below:
diff
```
 use_react_native!(  :path => config[:reactNativePath],+  :hermes_enabled => false,  # An absolute path to your application root.  :app_path => "#{Pod::Config.instance.installation_root}/.."
```

Is this page useful?
  * [Bundled Hermes](https://reactnative.dev/docs/hermes#bundled-hermes)
  * [Confirming Hermes is in use](https://reactnative.dev/docs/hermes#confirming-hermes-is-in-use)
  * [Switching back to JavaScriptCore](https://reactnative.dev/docs/hermes#switching-back-to-javascriptcore)



