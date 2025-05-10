---
url: https://reactnative.dev/docs/the-new-architecture/what-is-codegen
title: https://reactnative.dev/docs/the-new-architecture/what-is-codegen
date: 2025-05-10T20:52:47.330367
depth: 1
---

[Skip to main content](https://reactnative.dev/docs/the-new-architecture/what-is-codegen#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
**Codegen** is a tool to avoid writing a lot of repetitive code. Using Codegen **is not mandatory** : you can write all the generated manually. However, **Codegen** generates scaffolding code that could save you a lot of time.
React Native invokes **Codegen** automatically every time an iOS or Android app is built. Occasionally, you would like to manually run the **Codegen** scripts to know which types and files are actually generated: this is a common scenario when developing Turbo Native Modules and Fabric Native Components.
## How does Codegen works[​](https://reactnative.dev/docs/the-new-architecture/what-is-codegen#how-does-codegen-works "Direct link to How does Codegen works")
**Codegen** is a process that is tightly coupled with a React Native app. The **Codegen** scripts live inside the `react-native` NPM package and the apps call those scripts at build time.
**Codegen** crawls the folders in your project, starting from a directory you specify in your `package.json`, looking for some specific JS files that contains the specification (or specs) for your custom modules and components. Spec files are JS files written in a typed dialect: React Native currently supports Flow and TypeScript.
Every time **Codegen** finds a spec file, it generates the boilerplate code associated to it. **Codegen** generates some C++ glue-code and then it generates platform-specific code, using Java for Android and Objective-C++ for iOS.
Is this page useful?
  * [How does Codegen works](https://reactnative.dev/docs/the-new-architecture/what-is-codegen#how-does-codegen-works)



