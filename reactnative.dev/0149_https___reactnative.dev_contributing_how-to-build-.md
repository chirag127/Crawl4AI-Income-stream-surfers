---
url: https://reactnative.dev/contributing/how-to-build-from-source
title: https://reactnative.dev/contributing/how-to-build-from-source
date: 2025-05-10T21:35:38.278795
depth: 2
---

[Skip to main content](https://reactnative.dev/contributing/how-to-build-from-source#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
You will need to build React Native from source if you want to work on a new feature/bug fix, try out the latest features which are not released yet, or maintain your own fork with patches that cannot be merged to the core.
## Android[​](https://reactnative.dev/contributing/how-to-build-from-source#android "Direct link to Android")
### Prerequisites[​](https://reactnative.dev/contributing/how-to-build-from-source#prerequisites "Direct link to Prerequisites")
To build from source, you need to have the Android SDK installed. If you followed the [Setting up the development environment](https://reactnative.dev/docs/environment-setup) guide, you should already be set up.
There is no need to install other tools like specific version of NDK or CMake as the Android SDK will **automatically download** whatever is needed for the build from source.
### Point your project to a nightly[​](https://reactnative.dev/contributing/how-to-build-from-source#point-your-project-to-a-nightly "Direct link to Point your project to a nightly")
To use the latest fixes and features of React Native, you can update your project to use a nightly version of React Native with:
```
yarn add react-native@nightly
```

This will update your project to use a nightly version of React Native that gets released every night with the latest changes.
### Update your project to build from source[​](https://reactnative.dev/contributing/how-to-build-from-source#update-your-project-to-build-from-source "Direct link to Update your project to build from source")
Both with stable releases and nightlies, you will be consuming **precompiled** artifacts. If instead you want to switch to building from source, so you can test your changes to the framework directly, you will have to edit the `android/settings.gradle` file as follows:
diff
```
 // ... include ':app' includeBuild('../node_modules/@react-native/gradle-plugin')+ includeBuild('../node_modules/react-native') {+   dependencySubstitution {+     substitute(module("com.facebook.react:react-android")).using(project(":packages:react-native:ReactAndroid"))+     substitute(module("com.facebook.react:react-native")).using(project(":packages:react-native:ReactAndroid"))+     substitute(module("com.facebook.react:hermes-android")).using(project(":packages:react-native:ReactAndroid:hermes-engine"))+     substitute(module("com.facebook.react:hermes-engine")).using(project(":packages:react-native:ReactAndroid:hermes-engine"))
```

### Additional notes[​](https://reactnative.dev/contributing/how-to-build-from-source#additional-notes "Direct link to Additional notes")
Building from source can take a long time, especially for the first build, as it needs to download ~200 MB of artifacts and compile the native code.
Every time you update the `react-native` version from your repo, the build directory may get deleted, and all the files are re-downloaded. To avoid this, you might want to change your build directory path by editing the `~/.gradle/init.gradle` file:
groovy
```
gradle.projectsLoaded {  rootProject.allprojects {    buildDir ="/path/to/build/directory/${rootProject.name}/${project.name}"
```

## Rationale[​](https://reactnative.dev/contributing/how-to-build-from-source#rationale "Direct link to Rationale")
The recommended approach to working with React Native is to always update to the latest version. The support we provide for older versions is [described in our support policy](https://github.com/reactwg/react-native-releases/#releases-support-policy).
The build from source approach should be used to end-to-end test a fix before submitting a pull request to React Native, and we're not encouraging its usages in the long run. Especially forking React Native or switching your setup to always use a build from source, will result in projects that are harder to update and generally a worse developer experience.
Is this page useful?
  * [Android](https://reactnative.dev/contributing/how-to-build-from-source#android)
    * [Prerequisites](https://reactnative.dev/contributing/how-to-build-from-source#prerequisites)
    * [Point your project to a nightly](https://reactnative.dev/contributing/how-to-build-from-source#point-your-project-to-a-nightly)
    * [Update your project to build from source](https://reactnative.dev/contributing/how-to-build-from-source#update-your-project-to-build-from-source)
    * [Additional notes](https://reactnative.dev/contributing/how-to-build-from-source#additional-notes)



