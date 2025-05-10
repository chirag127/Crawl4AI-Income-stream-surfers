---
url: https://reactnative.dev/docs/next/native-platform
title: https://reactnative.dev/docs/next/native-platform
date: 2025-05-10T21:41:08.762486
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/next/native-platform#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
This is unreleased documentation for React Native **Next** version.
For up-to-date documentation, see the **[latest version](https://reactnative.dev/docs/native-platform)** (0.79).
Version: Next
Your application may need access to platform features that aren’t directly available from react-native or one of the hundreds of [third-party libraries](https://reactnative.directory/) maintained by the community. Maybe you want to reuse some existing Objective-C, Swift, Java, Kotlin or C++ code from the JavaScript runtime. Whatever your reason, React Native exposes a powerful set of API to connect your native code to your JavaScript application code.
This guide introduces:
  * **Native Modules:** native libraries that have no User Interface (UI) for the user. Examples would be persistent storage, notifications, network events. These are accessible to your user as JavaScript functions and objects.
  * **Native Component:** native platform views, widgets and controllers that are available to your application's JavaScript code through React Components.


note
You might have previously been familiar with:
  * [Legacy Native Modules](https://reactnative.dev/docs/next/legacy/native-modules-intro);
  * [Legacy Native Components](https://reactnative.dev/docs/next/legacy/native-components-android);


These are our deprecated native module and component API. You can still use many of these legacy libraries with the New Architecture thanks to our interop layers. You should consider:
  * using alternative libraries,
  * upgrading to newer library versions that have first-class support for the New Architecture, or
  * port these libraries yourself to Turbo Native Modules or Fabric Native Components.


  1. Native Modules 
     * [Cross-Platform with C++](https://reactnative.dev/docs/next/the-new-architecture/pure-cxx-modules)
     * [Advanced: Custom C++ Types](https://reactnative.dev/docs/next/the-new-architecture/custom-cxx-types)
  2. Fabric Native Components 


Is this page useful?

