---
url: https://reactnative.dev/docs/interactionmanager
title: https://reactnative.dev/docs/interactionmanager
date: 2025-05-10T21:40:32.384420
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/interactionmanager#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
InteractionManager allows long-running work to be scheduled after any interactions/animations have completed. In particular, this allows JavaScript animations to run smoothly.
Applications can schedule tasks to run after interactions with the following:
tsx
```
InteractionManager.runAfterInteractions(()=>{// ...long-running synchronous task...});
```

Compare this to other scheduling alternatives:
  * `requestAnimationFrame()` for code that animates a view over time.
  * `setImmediate/setTimeout()` run code later, note this may delay animations.
  * `runAfterInteractions()` run code later, without delaying active animations.


The touch handling system considers one or more active touches to be an 'interaction' and will delay `runAfterInteractions()` callbacks until all touches have ended or been cancelled.
InteractionManager also allows applications to register animations by creating an interaction 'handle' on animation start, and clearing it upon completion:
tsx
```
const handle =InteractionManager.createInteractionHandle();// run animation... (`runAfterInteractions` tasks are queued)// later, on animation completion:InteractionManager.clearInteractionHandle(handle);// queued tasks run if all handles were cleared
```

`runAfterInteractions` takes either a plain callback function, or a `PromiseTask` object with a `gen` method that returns a `Promise`. If a `PromiseTask` is supplied, then it is fully resolved (including asynchronous dependencies that also schedule more tasks via `runAfterInteractions`) before starting on the next task that might have been queued up synchronously earlier.
By default, queued tasks are executed together in a loop in one `setImmediate` batch. If `setDeadline` is called with a positive number, then tasks will only be executed until the deadline (in terms of js event loop run time) approaches, at which point execution will yield via setTimeout, allowing events such as touches to start interactions and block queued tasks from executing, making apps more responsive.
## Example[​](https://reactnative.dev/docs/interactionmanager#example "Direct link to Example")
### Basic[​](https://reactnative.dev/docs/interactionmanager#basic "Direct link to Basic")
  * TypeScript
  * JavaScript


### Advanced[​](https://reactnative.dev/docs/interactionmanager#advanced "Direct link to Advanced")
  * TypeScript
  * JavaScript


# Reference
## Methods[​](https://reactnative.dev/docs/interactionmanager#methods "Direct link to Methods")
### `runAfterInteractions()`[​](https://reactnative.dev/docs/interactionmanager#runafterinteractions "Direct link to runafterinteractions")
tsx
```
staticrunAfterInteractions(task?:(()=>any)|SimpleTask|PromiseTask);
```

Schedule a function to run after all interactions have completed. Returns a cancellable "promise".
### `createInteractionHandle()`[​](https://reactnative.dev/docs/interactionmanager#createinteractionhandle "Direct link to createinteractionhandle")
tsx
```
staticcreateInteractionHandle():Handle;
```

Notify manager that an interaction has started.
### `clearInteractionHandle()`[​](https://reactnative.dev/docs/interactionmanager#clearinteractionhandle "Direct link to clearinteractionhandle")
tsx
```
staticclearInteractionHandle(handle:Handle);
```

Notify manager that an interaction has completed.
### `setDeadline()`[​](https://reactnative.dev/docs/interactionmanager#setdeadline "Direct link to setdeadline")
tsx
```
staticsetDeadline(deadline:number);
```

A positive number will use setTimeout to schedule any tasks after the eventLoopRunningTime hits the deadline value, otherwise all tasks will be executed in one setImmediate batch (default).
Is this page useful?
  * [Example](https://reactnative.dev/docs/interactionmanager#example)
  * [Methods](https://reactnative.dev/docs/interactionmanager#methods)
    * [`runAfterInteractions()`](https://reactnative.dev/docs/interactionmanager#runafterinteractions)
    * [`createInteractionHandle()`](https://reactnative.dev/docs/interactionmanager#createinteractionhandle)
    * [`clearInteractionHandle()`](https://reactnative.dev/docs/interactionmanager#clearinteractionhandle)



