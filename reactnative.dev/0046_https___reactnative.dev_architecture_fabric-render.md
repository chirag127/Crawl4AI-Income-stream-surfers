---
url: https://reactnative.dev/architecture/fabric-renderer
title: https://reactnative.dev/architecture/fabric-renderer
date: 2025-05-10T20:53:18.950070
depth: 2
---

[Skip to main content](https://reactnative.dev/architecture/fabric-renderer#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
Fabric is React Native's new rendering system, a conceptual evolution of the legacy render system. The core principles are to unify more render logic in C++, improve interoperability with [host platforms](https://reactnative.dev/architecture/glossary#host-platform), and to unlock new capabilities for React Native. Development began in 2018 and in 2021, React Native in the Facebook app is backed by the new renderer.
This documentation provides an overview of the [new renderer](https://reactnative.dev/architecture/glossary#fabric-render) and its concepts. It avoids platform specifics and doesn’t contain any code snippets or pointers. This documentation covers key concepts, motivation, benefits, and an overview of the render pipeline in different scenarios.
## Motivations and Benefits of the new renderer[​](https://reactnative.dev/architecture/fabric-renderer#motivations-and-benefits-of-the-new-renderer "Direct link to Motivations and Benefits of the new renderer")
The render architecture was created to unlock better user experiences that weren’t possible with the legacy architecture. Some examples include:
  * With improved interoperability between [host views](https://reactnative.dev/architecture/glossary#host-view-tree-and-host-view) and React views, the renderer is able to measure and render React surfaces synchronously. In the legacy architecture, React Native layout was asynchronous which led to a layout “jump” issue when embedding a React Native rendered view in a _host view_.
  * With support of multi-priority and synchronous events, the renderer can prioritize certain user interactions to ensure they are handled in a timely manner.
  * [Integration with React Suspense](https://reactjs.org/blog/2019/11/06/building-great-user-experiences-with-concurrent-mode-and-suspense.html) which allows for more intuitive design of data fetching in React apps.
  * Enable React [Concurrent Features](https://github.com/reactwg/react-18/discussions/4) on React Native.
  * Easier to implement server side rendering for React Native.


The new architecture also provides benefits in code quality, performance, and extensibility:
  * **Type safety:** code generation to ensure type safety across the JS and [host platforms](https://reactnative.dev/architecture/glossary#host-platform). The code generation uses JavaScript component declarations as source of truth to generate C++ structs to hold the props. Mismatch between JavaScript and host component props triggers a build error.
  * **Shared C++ core** : the renderer is implemented in C++ and the core is shared among platforms. This increases consistency and makes it easier to adopt React Native on new platforms.
  * **Better Host Platform Interoperability** : Synchronous and thread-safe layout calculation improves user experiences when embedding host components into React Native, which means easier integration with host platform frameworks that require synchronous APIs.
  * **Improved Performance** : With the new cross-platform implementation of the renderer system, every platform benefits from performance improvements that may have been motivated by limitations of one platform. For example, view flattening was originally a performance solution for Android and is now provided by default on both Android and iOS.
  * **Consistency** : The new render system is cross-platform, it is easier to keep consistency among different platforms.
  * **Faster Startup** : Host components are lazily initialized by default.
  * **Less serialization of data between JS and host platform** : React used to transfer data between JavaScript and _host platform_ as serialized JSON. The new renderer improves the transfer of data by accessing JavaScript values directly using [JavaScript Interfaces (JSI)](https://reactnative.dev/architecture/glossary#javascript-interfaces-jsi).


Is this page useful?
  * [Motivations and Benefits of the new renderer](https://reactnative.dev/architecture/fabric-renderer#motivations-and-benefits-of-the-new-renderer)



