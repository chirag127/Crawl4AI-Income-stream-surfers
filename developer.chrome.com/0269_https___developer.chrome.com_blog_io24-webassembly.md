---
url: https://developer.chrome.com/blog/io24-webassembly-webgpu-1
title: https://developer.chrome.com/blog/io24-webassembly-webgpu-1
date: 2025-05-11T16:56:30.290269
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/io24-webassembly-webgpu-1#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/io24-webassembly-webgpu-1?hl=es-419)




  * On this page
  * [AI inference on the web](https://developer.chrome.com/blog/io24-webassembly-webgpu-1#ai_inference_on_the_web)
    * [How AI workloads run on the web today](https://developer.chrome.com/blog/io24-webassembly-webgpu-1#how_ai_workloads_run_on_the_web_today)
    * [Machine learning workloads](https://developer.chrome.com/blog/io24-webassembly-webgpu-1#machine_learning_workloads)
  * [WebAssembly](https://developer.chrome.com/blog/io24-webassembly-webgpu-1#webassembly)
    * [Take a wholistic approach to your applications](https://developer.chrome.com/blog/io24-webassembly-webgpu-1#take_a_wholistic_approach_to_your_applications)
    * [Better web interop](https://developer.chrome.com/blog/io24-webassembly-webgpu-1#better_web_interop)
    * [Decide which backend is right for you](https://developer.chrome.com/blog/io24-webassembly-webgpu-1#decide_which_backend_is_right_for_you)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  WebAssembly and WebGPU enhancements for faster Web AI, part 1 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [AI inference on the web](https://developer.chrome.com/blog/io24-webassembly-webgpu-1#ai_inference_on_the_web)
    * [How AI workloads run on the web today](https://developer.chrome.com/blog/io24-webassembly-webgpu-1#how_ai_workloads_run_on_the_web_today)
    * [Machine learning workloads](https://developer.chrome.com/blog/io24-webassembly-webgpu-1#machine_learning_workloads)
  * [WebAssembly](https://developer.chrome.com/blog/io24-webassembly-webgpu-1#webassembly)
    * [Take a wholistic approach to your applications](https://developer.chrome.com/blog/io24-webassembly-webgpu-1#take_a_wholistic_approach_to_your_applications)
    * [Better web interop](https://developer.chrome.com/blog/io24-webassembly-webgpu-1#better_web_interop)
    * [Decide which backend is right for you](https://developer.chrome.com/blog/io24-webassembly-webgpu-1#decide_which_backend_is_right_for_you)


Learn how WebAssembly and WebGPU enhancements improve machine learning performance on the web.
Austin Eng 
[ GitHub ](https://github.com/austinEng)
Deepti Gandluri 
[ GitHub ](https://github.com/dtig)
François Beaufort 
[ GitHub ](https://github.com/beaufortfrancois)
## AI inference on the web
We've all heard the story: AI is transforming our world. The web is no exception.
This year Chrome added generative AI features, including custom theme creation and or [helping you write a first draft of text](https://blog.google/products/chrome/google-chrome-generative-ai-features-january-2024/#help-me-write). But AI is much more than that; AI can enrich web applications themselves.
Web pages can embed [intelligent components](https://mediapipe-studio.webapps.google.com/home) for vision, like picking out faces or recognizing gestures, for audio classification, or for language detection. In the last year, we've seen generative AI take off, including some really impressive demos of large language models on the web. Be sure to check out [Practical on-device AI for web developers](https://developer.chrome.com/docs/ai/why-on-device).
AI inference on the web is available today across a large section of devices, and AI processing can happen in the web page itself, leveraging the hardware on the user's device.
This is powerful for several reasons:
  * **Reduced costs** : Running inference on the browser client significantly reduces server costs, and this can be especially useful for GenAI queries, that can be an orders of magnitude more expensive than regular queries.
  * **Latency** : For applications that are particularly sensitive to latency, like audio, or video applications - having all your processing happen on the device leads to reduced latency.
  * **Privacy** : Running on the client side, also has the potential of unlocking a new class of applications that require increased privacy, where data cannot be sent to the server.


### How AI workloads run on the web today
Today, application developers and researchers build models using frameworks, models execute in the browser using a runtime like [Tensorflow.js](https://www.tensorflow.org/js) or [ONNX Runtime Web](https://onnxruntime.ai/docs/tutorials/web/), and runtimes make use of Web APIs for execution.
All those runtimes eventually bottom out into running on the CPU through JavaScript or WebAssembly or on the GPU through WebGL or WebGPU.
### Machine learning workloads
Machine learning (ML) workloads push tensors through a graph of computational nodes. [Tensors](https://developers.google.com/machine-learning/glossary#tensor) are the inputs and outputs of these nodes which perform a large amount of computation over the data.
This is important, because:
  * Tensors are very large data structures, performing computation on models which can have billions of [weights](https://developers.google.com/machine-learning/glossary#weight)
  * Scaling and inference can lead to [data parallelism](https://developers.google.com/machine-learning/glossary#data-parallelism). This means the same operations are performed across all the elements in the tensors.
  * ML doesn't require precision. You might need a 64-bit floating point number to land on the moon, but you might only need a sea of 8-bit numbers or less for facial recognition.


Fortunately, chip designers have added features to make models run faster, cooler, and even make it possible to run them at all.
Meanwhile, here on the WebAssembly and WebGPU teams, we're working to expose those new capabilities to web developers. If you're a web application developer, you're unlikely to use these low-level primitives frequently. We expect the toolchains or frameworks you're using will support new features and extensions, thus you can benefit with minimal changes to your infrastructure. But if you do like to manually tune your applications for performance, then these feature are relevant to your work.
## WebAssembly
WebAssembly (Wasm) is a compact, efficient byte code format that runtimes can understand and execute. It's designed to take advantage of underlying hardware capabilities, so it can execute at near native speeds. The code is validated and executes in a memory-safe, sandboxed environment.
Wasm module information is represented with a dense binary encoding. As compared to a text-based format, that means faster decoding, faster loading, reduced memory usage. It's portable in the sense that it doesn't make assumptions about the underlying architecture that are not already common to modern architectures.
The WebAssembly specification is iterative and is worked on in an open [W3C community group](https://www.w3.org/community/webassembly/).
The binary format makes no assumptions about the host environment, so it's designed to work well in non-web embeddings, too.
Your application can be compiled once, and run everywhere: a desktop, laptop, a phone, or any other device with a browser. Check out [Write once, run anywhere finally realized with WebAssembly](https://www.youtube.com/watch?v=c8hZFtl8EuQ) to learn more about this.
Most production applications that run AI inference on the web make use of WebAssembly, both for CPU compute and interfacing with special purpose compute. On native applications, you can access both general purpose and special purpose compute, as the application can access device capabilities.
On the web, for portability and security, we carefully evaluate what set of primitives are exposed. This balances the accessibility of the web with maximal performance provided by the hardware.
WebAssembly is a portable abstraction of CPUs, so all Wasm inference is run on the CPU. While this isn't the most performant choice, CPUs are widely available and work across most workloads, on most devices.
For smaller workloads, such as text or audio workloads, GPU would be expensive. There are a number of recent examples where Wasm is the right choice:
  * Adobe uses Tensorflow.js to [enhance Photoshop for the web](https://blog.tensorflow.org/2023/03/how-adobe-used-web-ml-with-tensorflowjs-to-enhance-photoshop-for-web.html).
  * [Google Meet added background blur](https://research.google/blog/background-features-in-google-meet-powered-by-web-ml/), one of the first Wasm-based video effects on the web.
  * [YouTube has several augmented reality effects](https://research.google/blog/real-time-ar-self-expression-with-machine-learning/).
  * [Google Photos allows online editing](https://twitter.com/googlephotos/status/1668316144019836929).


You can discover even more in open source demos, such as: [whisper-tiny](https://huggingface.co/openai/whisper-tiny), [llama.cpp](https://github.com/ggerganov/llama.cpp), and [Gemma2B running in the browser](https://developers.google.com/mediapipe/solutions/genai/llm_inference/index#gemma_2b).
### Take a wholistic approach to your applications
You should choose primitives based on the particular ML model, application infrastructure, and overall intended application experience for users
For example, in MediaPipe's face landmark detection, CPU inference and GPU inference are comparable (running on an Apple M1 device), but there are models where the variance could be significantly higher.
When it comes to ML workloads, we consider a wholistic application view, while listening to framework authors and application partners, to develop and ship the most requested enhancements. These broadly fall into three categories:
  * Expose CPU extensions critical to performance
  * Enable running larger models
  * Enable seamless interop with other Web APIs


### Faster compute
As it stands, the WebAssembly spec only includes a certain set of instructions that we expose to the web. But hardware continues to add newer instructions that increase the gap between native and WebAssembly performance.
Remember, ML models don't always require the high levels of precision. [Relaxed SIMD](https://github.com/WebAssembly/relaxed-simd/blob/main/proposals/relaxed-simd/Overview.md) is a proposal that reduces some of the strict, non-determinism requirements, leading to faster codegen for some vector operations that are hot spots for performance. Further, Relaxed SIMD introduces new dot product and FMA instructions that speed up existing workloads from 1.5 - 3 times. This was shipped in Chrome 114.
The [half-precision floating point format](https://github.com/WebAssembly/half-precision/blob/main/proposals/half-precision/Overview.md) uses 16-bits for IEEE FP16 instead of the 32-bits used for single precision values. Compared to single precision values, there are several advantages in using half-precision values, reduced memory requirements, which enable training and deployment of larger neural networks, reduced memory bandwidth. Reduced precision speeds up data transfer and math operations.
### Larger models
Pointers into Wasm linear memory are represented as 32-bit integers. This has two consequences: heap sizes are limited to 4GB (when computers have much more physical RAM than that), and application code that targets Wasm has to be be compatible with a 32-bit pointer size (which).
Especially with large models like we have today, loading these models into WebAssembly can be restrictive. The [Memory64](https://github.com/WebAssembly/memory64/blob/main/proposals/memory64/Overview.md) proposal removes these restrictions by linear memory to be larger than 4GB and matching the address space of native platforms.
We have a full working implementation in Chrome and is estimated to ship later this year. For now, you can [run experiments with the flag](https://developer.chrome.com/docs/web-platform/chrome-flags) `chrome://flags/#enable-experimental-webassembly-features`, and send us [feedback](https://github.com/WebAssembly/memory64/issues).
### Better web interop
WebAssembly could be the entry point for special purpose compute on the web.
WebAssembly can be used to bring GPU applications to the web. That means the same C++ application that can run on-device can also run on the web, with small modifications.
[Emscripten](https://emscripten.org/), the Wasm compiler toolchain, already has bindings for WebGPU. It's the entry point for AI inference on the web, so it's critical that Wasm can seamlessly interoperate with the rest of the web platform. We're working on a couple of different proposals in this space.
#### JavaScript promise integration (JSPI)
Typical C and C++ (as well as many other languages) applications are commonly written against a synchronous API. This means that the application would stop execution until the operation is completed. Such blocking applications are typically more intuitive to write than applications that are async-aware.
When expensive operations block the main thread, they can block I/O and the jank is visible to users. There's a mismatch between a synchronous programming model of native applications and the asynchronous model of the web. This is especially problematic for legacy applications, which would be expensive to port. Emscripten provides a way to do this with Asyncify, but this isn't always the best option - larger code size and not as efficient.
The following example is computing fibonacci, using JavaScript promises for addition.
```
longpromiseFib(longx){
if(x==0)
return0;
if(x==1)
return1;
returnpromiseAdd(promiseFib(x-1),promiseFib(x-2));
}
// promise an addition
EM_ASYNC_JS(long,promiseAdd,(longx,longy),{
returnPromise.resolve(x+y);
});

```
```
emcc-O3fib.c-ob.html-sASYNCIFY=2

```

In this example, pay attention to the following:
  * The `EM_ASYNC_JS` macro generates all the necessary glue code so that we can use JSPI to access the promise's result, just like it would for a normal function.
  * The special command line option, `-s ASYNCIFY=2`. This invokes the option to generate code that uses JSPI to interface with JavaScript imports that return promises.


For more on JSPI, how to use it, and its benefits, read [Introducing the WebAssembly JavaScript Promise Integration API on v8.dev](https://v8.dev/blog/jspi). Learn about the [current origin trial](https://developer.chrome.com/blog/webassembly-jspi-origin-trial).
#### Memory control
Developers have very little control over Wasm memory; the module owns its own memory. Any APIs that need to access this memory must copy in or copy out, and this usage can really add up. For example, a graphics application may need to copy in and copy out for each frame.
The [Memory control](https://github.com/WebAssembly/memory-control/blob/main/proposals/memory-control/Overview.md) proposal aims to provide finer grained control over Wasm linear memory and reduce the number of copies across the application pipeline. This proposal is in Phase 1, we're prototyping this in V8, Chrome's JavaScript engine, to inform the evolution of the standard.
### Decide which backend is right for you
While CPU is ubiquitous, it isn't always the best option. Special purpose compute on the GPU or accelerators can offer performance that is orders of magnitude higher, especially for larger models and on high-end devices. This is true for both native applications and web applications.
Which backend you choose is dependent on the application, framework or toolchain, as well as other factors that influence performance. That said, we're continuing to invest in proposals that enable core Wasm to work well with the rest of the web platform, and more specifically with WebGPU.
[Continue reading Part 2](https://developer.chrome.com/blog/io24-webassembly-webgpu-2)
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-05-16 UTC.

