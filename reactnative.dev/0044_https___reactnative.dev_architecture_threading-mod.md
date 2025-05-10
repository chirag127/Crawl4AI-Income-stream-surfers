---
url: https://reactnative.dev/architecture/threading-model
title: https://reactnative.dev/architecture/threading-model
date: 2025-05-10T20:53:14.565810
depth: 2
---

[Skip to main content](https://reactnative.dev/architecture/threading-model#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
caution
This document refers to the [New Architecture](https://reactnative.dev/architecture/fabric-renderer), that is in active roll-out.
#### The React Native renderer distributes the work of the [render pipeline](https://reactnative.dev/architecture/render-pipeline) across multiple threads.[​](https://reactnative.dev/architecture/threading-model#the-react-native-renderer-distributes-the-work-of-the-render-pipeline-across-multiple-threads "Direct link to the-react-native-renderer-distributes-the-work-of-the-render-pipeline-across-multiple-threads")
Here we define the threading model and provide some examples to illustrate thread usage of the render pipeline.
React Native renderer is designed to be thread safe. At a high level thread safety is guaranteed by using immutable data structures in the internals of the framework (enforced by C++ “const correctness” feature). This means that every update in React creates or clones new objects in the renderer instead of updating data structures. This allows the framework to expose thread safe and synchronous APIs to React.
The renderer uses two different threads:
  * **UI thread** (often called main): The only thread that can manipulate host views.
  * **JavaScript thread** : This is where React’s render phase, as well as layout, are executed.


Let’s review the supported scenarios of execution for each phase:
## Render Scenarios[​](https://reactnative.dev/architecture/threading-model#render-scenarios "Direct link to Render Scenarios")
### Render in a JS Thread[​](https://reactnative.dev/architecture/threading-model#render-in-a-js-thread "Direct link to Render in a JS Thread")
This is the most common scenario where most of the render pipeline happens on JavaScript thread.
### Render in the UI Thread[​](https://reactnative.dev/architecture/threading-model#render-in-the-ui-thread "Direct link to Render in the UI Thread")
When there is a high priority event on the UI Thread, the renderer is able to execute all the render pipeline synchronously on the UI thread.
### Default or continuous event interruption[​](https://reactnative.dev/architecture/threading-model#default-or-continuous-event-interruption "Direct link to Default or continuous event interruption")
This scenario shows the interruption of the render phase by a low priority event in the UI thread. React and the React Native renderer are able to interrupt the render phase and merge its state with a low priority event that is executed on the UI thread. In this case the render process continues executing in the JS thread.
### Discrete event interruption[​](https://reactnative.dev/architecture/threading-model#discrete-event-interruption "Direct link to Discrete event interruption")
The render phase is interruptible. This scenario shows the interruption of the render phase by a high priority event in the UI thread. React and the renderer are able to interrupt the render phase and merge its state with a high priority event that was executed on the UI thread. The render phase executes synchronously on the UI thread.
### C++ State update[​](https://reactnative.dev/architecture/threading-model#c-state-update "Direct link to C++ State update")
Update originating on UI thread and skips rendering phase. See [React Native Renderer State Updates](https://reactnative.dev/architecture/render-pipeline#react-native-renderer-state-updates) for more details.
Is this page useful?
  * [Render Scenarios](https://reactnative.dev/architecture/threading-model#render-scenarios)
    * [Render in a JS Thread](https://reactnative.dev/architecture/threading-model#render-in-a-js-thread)
    * [Render in the UI Thread](https://reactnative.dev/architecture/threading-model#render-in-the-ui-thread)
    * [Default or continuous event interruption](https://reactnative.dev/architecture/threading-model#default-or-continuous-event-interruption)
    * [Discrete event interruption](https://reactnative.dev/architecture/threading-model#discrete-event-interruption)
    * [C++ State update](https://reactnative.dev/architecture/threading-model#c-state-update)



