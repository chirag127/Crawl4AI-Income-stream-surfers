---
url: https://developer.chrome.com/blog/io24-web-ai-wrapup?hl=en
title: https://developer.chrome.com/blog/io24-web-ai-wrapup?hl=en
date: 2025-05-11T16:56:30.282940
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/io24-web-ai-wrapup?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/io24-web-ai-wrapup?hl=es-419)




  * On this page
  * [LLMs in the browser](https://developer.chrome.com/blog/io24-web-ai-wrapup?hl=en#llms-browser)
  * [Build faster prototypes with Visual Blocks](https://developer.chrome.com/blog/io24-web-ai-wrapup?hl=en#build-faster)
  * [Use JavaScript for Web AI at scale with Chrome](https://developer.chrome.com/blog/io24-web-ai-wrapup?hl=en#use-js)
  * [Start testing Web AI models with headless Chrome](https://developer.chrome.com/blog/io24-web-ai-wrapup?hl=en#test-with-headless-chrome)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  I/O 2024 Web AI wrap up: New models, tools, and APIs for your next web app 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [LLMs in the browser](https://developer.chrome.com/blog/io24-web-ai-wrapup?hl=en#llms-browser)
  * [Build faster prototypes with Visual Blocks](https://developer.chrome.com/blog/io24-web-ai-wrapup?hl=en#build-faster)
  * [Use JavaScript for Web AI at scale with Chrome](https://developer.chrome.com/blog/io24-web-ai-wrapup?hl=en#use-js)
  * [Start testing Web AI models with headless Chrome](https://developer.chrome.com/blog/io24-web-ai-wrapup?hl=en#test-with-headless-chrome)


Jason Mayes 
[ GitHub ](https://github.com/jasonmayes) [ LinkedIn ](https://www.linkedin.com/in/webai)
Alexandra Klepper 
[ GitHub ](https://github.com/alexandrascript) [ LinkedIn ](https://www.linkedin.com/in/alexandraklepper) [ Bluesky ](https://bsky.app/profile/alexandrascript.com)
A lot has changed in Web AI over the last year. In case you missed it, we gave a talk at I/O 2024 about the new models, tools, and APIs for your next web app.
Web AI is a set of technologies and techniques to use machine learning (ML) models, client-side in a web browser running on a device's CPU or GPU. This can be built with JavaScript and other web technologies, such as [WebAssembly and WebGPU](https://developer.chrome.com/blog/io24-webassembly-webgpu-1). This is unlike server-side AI or "Cloud AI," where the model executes on a server and is accessed with an API.
In this talk, we shared:
  * How to run our new large language models (LLMs) in the browser and the impact of running models client-side;
  * A look into the future of [Visual Blocks](https://goo.gle/VisualBlocks), to prototype faster;
  * And how web developers can use JavaScript in Chrome to work with Web AI, at scale.


## LLMs in the browser
Gemma Web is a new open model from Google that can run in the browser on a user's device, built from the same research and technology we used to create Gemini.
By bringing an LLM on-device, there is significant potential for cost savings as compared to running on a cloud server for inference, along with enhanced user privacy and reduced latency. Generative AI in the browser is still in its early stages, but as hardware continues to improve (with higher CPU and GPU RAM), we expect more models to become available.
Businesses can reimagine what you can do on a web page, especially for task-specific use cases, where the weights of smaller LLMs (2 to 8 billion parameters) can be tuned to run on consumer hardware.
[Gemma 2B](https://goo.gle/Gemma2b) is available to download on Kaggle Models, and comes in a format that is compatible with our [Web LLM inference API](https://developers.google.com/mediapipe/solutions/genai/llm_inference/web_js). Other supported architectures include [Microsoft Phi-2](https://goo.gle/Phi2), [Falcon RW 1B](https://goo.gle/FalconRW1B), and [Stable LM 3B](https://goo.gle/StableLM3B), which you can convert to a format that the runtime can use, using our [converter library](https://goo.gle/MPWebLLMConvert).
## Build faster prototypes with Visual Blocks
_With Visual Blocks, you can run depth estimation in the client, with no code._
We're collaborating with Hugging Face, who have created 16 brand new custom nodes for [Visual Blocks](https://goo.gle/VisualBlocks). This brings [Transformers.js](https://huggingface.co/docs/transformers.js/en/index) and the wider Hugging Face ecosystem to Visual Blocks.
Eight of these new nodes run entirely client side, with Web AI, including:
  * [Image segmentation](https://goo.gle/HFImageSeg)
  * [Token classification](https://goo.gle/HFTokens)
  * [Object detection](https://goo.gle/HFImageClassify)
  * [Text classification](https://goo.gle/HFTextClassify)
  * [Background removal](https://goo.gle/HFBgRemove)
  * [Depth estimation](https://goo.gle/HFDepth)


Additionally, there are seven server-side ML tasks from Hugging Face that allow you to run thousands of models with APIs in Visual Blocks. Check out the [Hugging Face Visual Blocks collection](https://goo.gle/hf-visualblocks).
## Use JavaScript for Web AI at scale with Chrome
In the previous instances, such as with Gemma, the model is loaded and run within the web page itself. Chrome is working on [built-in, on-device AI](https://developer.chrome.com/docs/ai/built-in), where you could access models with standardized, task-specific JavaScript APIs.
And that's not all. Chrome has also updated [WebGPU](https://developer.chrome.com/blog/io24-webassembly-webgpu-2) with support for 16 bit floating point values.
WebAssembly has a new proposal, [Memory64](https://goo.gle/WASM-prop), to support 64 bit memory indexes, which would allow you to load larger AI models than before.
## Start testing Web AI models with headless Chrome
You can now test client-side AI (or any application that needs WebGL or WebGPU support) using Headless Chrome, while making use of server-side GPUs for acceleration such as an NVIDIA T4 or P100 Learn more:
  * [Run it in Google Colab](https://goo.gle/WebAITestingColab)
  * [Read a testing deep dive](https://goo.gle/WebAITestingBlog)
  * And check out the [example code on GitHub](https://goo.gle/WebAITesting)


Remember, when you share what you create, add #WebAI so the wider community can see your work. Share your findings and suggestions on X, LinkedIn, or the social platform you prefer.
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-05-16 UTC.

