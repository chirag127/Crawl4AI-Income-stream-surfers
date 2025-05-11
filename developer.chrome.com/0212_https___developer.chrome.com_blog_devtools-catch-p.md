---
url: https://developer.chrome.com/blog/devtools-catch-prediction?hl=en
title: https://developer.chrome.com/blog/devtools-catch-prediction?hl=en
date: 2025-05-11T16:55:15.682195
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/devtools-catch-prediction?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/devtools-catch-prediction?hl=es-419)

Sign in


  * On this page
  * [Why catch prediction matters ](https://developer.chrome.com/blog/devtools-catch-prediction?hl=en#why_catch_prediction_matters )
  * [How asynchronous code works](https://developer.chrome.com/blog/devtools-catch-prediction?hl=en#how_asynchronous_code_works)
  * [Methods for catch prediction](https://developer.chrome.com/blog/devtools-catch-prediction?hl=en#methods_for_catch_prediction)
  * [Acknowledgements](https://developer.chrome.com/blog/devtools-catch-prediction?hl=en#acknowledgements)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  Catch prediction in Chrome DevTools: Why it's hard and how to make it better 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Why catch prediction matters ](https://developer.chrome.com/blog/devtools-catch-prediction?hl=en#why_catch_prediction_matters )
  * [How asynchronous code works](https://developer.chrome.com/blog/devtools-catch-prediction?hl=en#how_asynchronous_code_works)
  * [Methods for catch prediction](https://developer.chrome.com/blog/devtools-catch-prediction?hl=en#methods_for_catch_prediction)
  * [Acknowledgements](https://developer.chrome.com/blog/devtools-catch-prediction?hl=en#acknowledgements)


Eric Leese 
[ GitHub ](https://github.com/ericsl)
Debugging exceptions in web applications seems simple: pause execution when something goes wrong and investigate. But the asynchronous nature of JavaScript makes this surprisingly complex. How can Chrome DevTools know when and where to pause when exceptions fly through promises and asynchronous functions?
This post dives into the challenges of _catch prediction_ – DevTools' ability to anticipate if an exception will be caught later in your code. We'll explore why it's so tricky and how recent improvements in V8 (the JavaScript engine powering Chrome) are making it more accurate, leading to a smoother debugging experience.
## Why catch prediction matters 
In Chrome DevTools, you have an option to pause code execution only for uncaught exceptions, skipping over ones that are caught. 
Behind the scenes, the debugger stops immediately when an exception occurs to preserve the context. It is a _prediction_ because, at this moment, it's impossible to know for sure whether the exception will be caught or not later in the code, especially in asynchronous scenarios. This uncertainty stems from the inherent difficulty of predicting program behavior, similar to the [Halting Problem](https://en.wikipedia.org/wiki/Halting_problem).
Consider the following example: where should the debugger pause? (Look for an answer in the next section.)
```
asyncfunctioninner(){
thrownewError();// Should the debugger pause here?
}
asyncfunctionouter(){
try{
constpromise=inner();
// ...
awaitpromise;
}catch(e){
// ... or should the debugger pause here?
}
}

```

Pausing on exceptions in a debugger can be disruptive and lead to frequent interruptions and jumps to unfamiliar code. To mitigate this, you can choose to only debug uncaught exceptions, which are more likely to signal actual bugs. However, this relies on the accuracy of catch prediction.
Incorrect predictions lead to frustration:
  * **False negatives (predicting "uncaught" when it will be caught)**. Unnecessary stops in the debugger.
  * **False positives (predicting "caught" when it will be uncaught)**. Missed opportunities to catch critical errors, potentially forcing you to debug all exceptions, including expected ones.


Another method to reduce debugging interruptions is by using the [ignore list](https://goo.gle/ignore-list), which prevents breaks on exceptions within specified third-party code. However, accurate catch prediction is still crucial here. If an exception originating in third-party code escapes and affects your own code, you'll want to be able to debug it.
## How asynchronous code works
Promises, `async` and `await`, and other asynchronous patterns can lead to scenarios in which an exception or rejection, before being handled, may take an execution path that is difficult to determine at the time an exception is thrown. This is because promises may not be awaited or have catch handlers added until after the exception has already occurred. Let's look at our previous example:
```
asyncfunctioninner(){
thrownewError();
}
asyncfunctionouter(){
try{
constpromise=inner();
// ...
awaitpromise;
}catch(e){
// ...
}
}

```

In this example, `outer()` first calls `inner()` which immediately throws an exception. From this the debugger can conclude that `inner()` will return a rejected promise but currently nothing is awaiting or otherwise handling that promise. The debugger can guess that `outer()` will probably await it and guess that it will do so in its current `try` block and therefore handle it but the debugger can't be certain of this until after the rejected promise is returned and the `await` statement is eventually reached.
The debugger can't offer any guarantees that catch predictions will be accurate but it uses a variety of heuristics for common coding patterns to predict correctly. To understand these patterns, it helps to learn how promises work.
In V8, a JavaScript `Promise` is represented as an object that can be in one of three states: fulfilled, rejected, or pending. If a promise is in the fulfilled state and you call the `.then()` method, a new pending promise is created and a new promise reaction task is scheduled which will run the handler and then set the promise to fulfilled with the result of the handler or set it to rejected if the handler throws an exception. The same happens if you call the `.catch()` method on a rejected promise. On the contrary, calling `.then()` on a rejected promise or `.catch()` on a fulfilled promise will return a promise in the same state and not run the handler. 
A pending promise contains a reaction list where each reaction object contains a fulfill handler or rejection handler (or both) and a reaction promise. So calling `.then()` on a pending promise will add a reaction with a fulfilled handler as well as a new pending promise for the reaction promise, which `.then()` will return. Calling `.catch()` will add a similar reaction but with a rejection handler. Calling `.then()` with two arguments creates a reaction with both handlers, and calling `.finally()` or awaiting the promise will add a reaction with two handlers that are built-in functions specific to implementing these features.
When the pending promise is eventually fulfilled or rejected, reaction jobs will be scheduled for either all of its fulfilled handlers or all of its rejected handlers. The corresponding reaction promises will then be updated, potentially triggering their own reaction jobs.
### Examples
Consider the following code:
```
returnnewPromise(()=>{thrownewError();})
.then(()=>console.log('Never happened'))
.catch(()=>console.log('Caught'));

```

It may not be obvious that this code involves three distinct `Promise` objects. The above code is equivalent to the following code:
```
constpromise1=newPromise(()=>{thrownewError();});
constpromise2=promise1.then(()=>console.log('Never happened'));
constpromise3=promise2.catch(()=>console.log('Caught'));
returnpromise3;

```

In this example, the following steps happen:
  1. The `Promise` constructor is called.
  2. A new pending `Promise` is created.
  3. The anonymous function is run.
  4. An exception is thrown. At this point, the debugger needs to decide whether to stop or not.
  5. The promise constructor catches this exception and then changes the state of its promise to `rejected` with its value set to the error that was thrown. It returns this promise, which is stored in `promise1`.
  6. `.then()` schedules no reaction job because `promise1` is in the `rejected` state. Instead, a new promise (`promise2`) is returned, which is also in the rejected state with the same error.
  7. `.catch()` schedules a reaction job with the provided handler and a new pending reaction promise, which is returned as `promise3`. At this point the debugger knows the error will be handled.
  8. When the reaction task runs, the handler returns normally and the state of `promise3` is changed to `fulfilled`.


The next example has a similar structure but the execution is quite different:
```
returnPromise.resolve()
.then(()=>{thrownewError();})
.then(()=>console.log('Never happened'))
.catch(()=>console.log('Caught'));

```

This is equivalent to:
```
constpromise1=Promise.resolve();
constpromise2=promise1.then(()=>{thrownewError();});
constpromise3=promise2.then(()=>console.log('Never happened'));
constpromise4=promise3.catch(()=>console.log('Caught'));
returnpromise4;

```

In this example, the following steps happen:
  1. A `Promise` is created in the `fulfilled` state and stored in `promise1`.
  2. A promise reaction task is scheduled with the first anonymous function and its `(pending)` reaction promise is returned as `promise2`.
  3. A reaction is added to `promise2` with a fulfilled handler and its reaction promise, which is returned as `promise3`.
  4. A reaction is added to `promise3` with a rejected handler and another reaction promise, which is returned as `promise4`.
  5. The reaction task scheduled in step 2 is run.
  6. The handler throws an exception. At this point the debugger needs to decide whether to stop or not. Currently the handler is your only running JavaScript code.
  7. Because the task ends with an exception, the associated reaction promise (`promise2`) is set to the rejected state with its value set to the error that was thrown.
  8. Because `promise2` had one reaction, and that reaction had no rejected handler, its reaction promise (`promise3`) is also set to `rejected` with the same error.
  9. Because `promise3` had one reaction, and that reaction did have a rejected handler, a promise reaction task is scheduled with that handler and its reaction promise (`promise4`).
  10. When that reaction task runs, the handler returns normally and the state of `promise4` is changed to fulfilled.


## Methods for catch prediction
There are two potential sources of information for catch prediction. One is the call stack. This is sound for synchronous exceptions: the debugger can walk the call stack in the same way the exception unwinding code will and stops if it finds a frame where it's in a `try...catch` block. For rejected promises or exceptions in promise constructors or in asynchronous functions that have never been suspended, the debugger also relies on the call stack but, in this case, its prediction can't be reliable in all cases. This is because instead of throwing an exception to the nearest handler, asynchronous code will return a rejected exception, and the debugger must make a few assumptions about what the caller will do with it.
First, the debugger assumes that a function that receives a returned promise is likely to return that promise or a derived promise so that asynchronous functions further up the stack will have a chance to await it. Second, the debugger assumes that if a promise is returned to an asynchronous function, it will soon await it without first entering or leaving a `try...catch` block. Neither of these assumptions are guaranteed to be correct but they are sufficient to make the correct predictions for the most common coding patterns with asynchronous functions. In Chrome version 125, we added another heuristic: the debugger checks if a callee is about to call `.catch()` on the value that will be returned (or `.then()` with two arguments, or a chain of calls to `.then()` or `.finally()` followed by a `.catch()` or a two-argument `.then()`). In this case, the debugger assumes that these are the methods on the promise we are tracing or one related to it, so the rejection will be caught.
The second source of information is the tree of promise reactions. The debugger starts with a root promise. Sometimes this is a promise for which its `reject()` method has just been called. More commonly, when an exception or rejection happens during a promise reaction job, and nothing on the call stack appears to catch it, the debugger traces from the promise associated with the reaction. The debugger looks at all reactions on the pending promise and sees if they have rejection handlers. If any reactions don't, it looks at the reaction promise and recursively traces from it. If all reactions ultimately lead to a rejection handler, the debugger considers the promise rejection to be caught. There are some special cases to cover, for example, not counting the built-in rejection handler for a `.finally()` call.
The promise reaction tree provides a usually reliable source of information if the information is there. In some cases, like a call to `Promise.reject()` or in a `Promise` constructor or in an async function that hasn't awaited anything yet, there will be no reactions to trace and the debugger has to rely on the call stack alone. In other cases, the promise reaction tree usually does contain the handlers necessary to infer catch prediction but it is always possible that more handlers will be added later that will change the exception from caught to uncaught or vice versa. There are also promises like those created by `Promise.all/any/race`, where other promises in the group may affect how a rejection is treated. For these methods, the debugger assumes a promise rejection will be forwarded if the promise is still pending.
Take a look at the following two examples:
While these two examples of caught exceptions look similar, they require quite different catch prediction heuristics. In the first example, a resolved promise is created, then a reaction job for `.then()` is scheduled that will throw an exception, then `.catch()` is called to attach a rejection handler to the reaction promise. When the reaction task is run, the exception will be thrown, and the promise reaction tree will contain the catch handler, so it will be detected as caught. In the second example, the promise is immediately rejected before the code to add a catch handler is run, so there are no rejection handlers in the promise's reaction tree. The debugger must look at the call stack but there are no `try...catch` blocks either. To correctly predict this, the debugger scans ahead of the current location in the code to find the call to `.catch()`, and assumes on that basis that the rejection will ultimately be handled.
## Summary
Hopefully, this explanation has shed light on how catch prediction works in Chrome DevTools, its strengths, and its limitations. If you encounter debugging issues due to incorrect predictions, consider these options:
  * Change the coding pattern to something more straightforward to predict, like using async functions.
  * Select to break on all exceptions if DevTools is failing to stop when it should.
  * Use a "Never pause here" breakpoint or conditional breakpoint if the debugger is stopping somewhere you don't want it to.


## Acknowledgements
Our deepest gratitude goes out to Sofia Emelianova and Jecelyn Yeen for their invaluable help editing this post!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-10-02 UTC.

