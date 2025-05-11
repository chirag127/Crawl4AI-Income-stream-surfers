---
url: https://developer.chrome.com/blog/how-we-introduced-gemini-to-devtools?hl=en
title: https://developer.chrome.com/blog/how-we-introduced-gemini-to-devtools?hl=en
date: 2025-05-11T16:56:25.762297
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/how-we-introduced-gemini-to-devtools?hl=en#main-content)
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Nederlands
  * Português – Brasil
  * Tiếng Việt
  * Русский
  * العربيّة
  * ภาษาไทย
  * 中文 – 简体
  * 中文 – 繁體

Sign in


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  How we introduced Gemini to Chrome DevTools 
Stay organized with collections  Save and categorize content based on your preferences. 
Alex Rudenko 
[ GitHub ](https://github.com/orkon)
Ergün Erdogmus 
Published: January 14, 2025 
At last year's Google I/O 2024 we launched [console insights](https://developer.chrome.com/docs/devtools/console/understand-messages), the first AI feature in Chrome DevTools. Console insights helps understand errors and warnings logged to the console by sending network data, source code and stack traces related to the log message to Gemini, Google's Large Language Model (LLM). Console insights sends a single prompt to Gemini that returns a single response without the possibility for developers to ask follow-up questions. While this single interaction flow works relatively well for explaining error messages, it does not scale to more complex debugging use cases inside DevTools where it is not clear what data from the inspected page an AI would require to help.
One such use case is debugging styling issues. A single web page can contain thousands of elements and CSS rules, with only a subset of them being relevant to debugging a specific scenario. Identifying the right code to debug can be challenging, even for humans. But with a prototype built during an AI hackathon at Google we learned that LLMs are actually pretty decent at it. So naturally, we wanted to bring that power to DevTools users, creating a tool that is able to investigate styling issues by interactively querying the page for additional context data. What we built launched as [AI assistance for styling](https://developer.chrome.com/docs/devtools/ai-assistance/styling) a few months later.
In this post we want to shine some light on challenges we faced while introducing AI to a loved product such as Chrome DevTools - which at its core, is a web app - and what you can adapt for your own AI features.
## Collecting the right data
Console insights is always using the same data points to respond to a predefined prompt. For AI assistance to be helpful with any user-defined prompt we need to dynamically determine what context data is important for the query at hand.
Therefore we implemented the ReAct ([Yao et al., 2022](https://arxiv.org/abs/2210.03629)) strategy. This prompting strategy empowers LLMs to reason autonomously and determine the subsequent action based on its reasoning.
This way AI assistance operates in a cycle of thought, action, and observation until it determines a suitable response to the user's query, at which point it concludes the cycle and provides an answer. This iterative process allows the LLM to gather the precise information needed to effectively debug styling issues.
A visual representation of the ReAct pattern as implemented for AI assistance. The prompt is sent to Gemini which returns a response including actions to apply to the inspected page through DevTools commands. The cycle repeats until the LLM determines a suitable response to the user's query.
To gather information, we have given only one tool to Gemini: running JavaScript on the inspected page. This allows Gemini through AI assistance to, for example:
  * **Access and analyze the DOM** : traverse the DOM tree, inspect element attributes, and understand the relationships between elements.
  * **Retrieve computed styles** : access computed styles for any element.
  * **Perform calculations and measurements** : execute JavaScript code to calculate distances, sizes, and positions of elements.


This makes AI assistance interactively act on only relevant code, improving response quality, response time and the use of computing resources, compared to sending the full HTML and CSS source code to Gemini.
## Running AI-generated code in user space
It may seem unexpected that for debugging styling issues we used JavaScript. There are two reasons for this:
  * Web APIs are very powerful and inherently cover many debugging use cases. While it might be tedious for a developer to use API calls manually to traverse the DOM or access computed styles for debugging, it is not a problem for an LLM to generate code calling them.
  * While it is possible to invent new APIs for an agent to use, reusing existing, public APIs often is the better choice, because they are already known to LLMs. Educating an LLM about a new API requires a lot of resources for fine-tuning and specific training data.


But running AI generated code in user space has risks. For AI assistance we needed to minimize the risk of destructive changes that the agent might do to the page. For that, we employed the side-effect checks that [V8, Chrome's JavaScript engine, exposes](https://chromedevtools.github.io/devtools-protocol/tot/Runtime/#method-callFunctionOn) through the Chrome DevTools Protocol. The same checks are used for the auto-complete functionality in the DevTools Console: it only runs JavaScript code as long as it does not modify any page state. The checks are performed while V8 executes the code and are based on an [allow list](https://source.chromium.org/chromium/chromium/src/+/main:v8/src/debug/debug-evaluate.cc;l=561;drc=c803f15380d8ce9f618aaf3f31a2adb527e9da68) of JavaScript built-ins that are known to have no side effects.
If the checks detect that generated code is modifying the inspected page, execution is paused, and the user is asked to review the code and confirm that it is okay to run.
Additionally, generated JavaScript is run in a so-called isolated ["world"](https://source.chromium.org/chromium/chromium/src/+/main:third_party/blink/renderer/bindings/core/v8/V8BindingDesign.md;l=133;drc=eb90eb0f510ccf69c0ac8043e8cfe608fea8f41b). That's similar to how extensions run sandbox scripts: the generated code is able to access the DOM and Web APIs but not able to access JavaScript code or state defined by the inspected page.
## Tracking changes done by the agent
In addition to investigating issues and answering debugging questions about the page, we also wanted to give the AI assistance agent the ability to fix styles on the page in a way that is traceable by developers.
To accomplish this, we implemented a binding called `setElementStyles` that we expose to the agent's execution context in addition to the default Web APIs.
To make Gemini aware of that new method, we instruct it to use it in the AI assistance preamble:
```
If you need to set styles on an HTML element, always call the \`async setElementStyles(el: Element, styles: object)\` function.

```

Despite being an API specifically designed for the agent, which comes with the previously mentioned challenges, even without fine-tuning Gemini quite reliably uses it when it needs to change styles on a given element.
On the DevTools side, when `setElementStyles` is called from the agent, AI assistance uses inspector stylesheets to record the change for the elements selector. CSS nesting is used to name the change and raise the specificity of the element's selector. An exemplary CSS rule created by the agent, thus, looks as following:
```
.ai-style-change-1{/* the ID is incremented for each change*/
.element-selector{/* Element selector is computed based on the element setElementStyles was called on. */
color:blue;
}
}

```

While this doesn't solve all possible style conflicts that can happen on the page, it works for the majority of the cases.
The benefit of using inspector stylesheets compared to inline styles is that this way changes performed by the agent also show up in the [**Changes** panel](https://developer.chrome.com/docs/devtools/changes), which makes it easier to track what changes to element styles have been made and what a developer needs to transfer to the underlying source code. The integration with the Changes panel also allows rolling back the changes if the change isn't needed anymore.
## Making agent actions observable for users
When adding agentic features to a product, it's important to make agent actions transparent for users, so that they have a chance to trace, understand and potentially intervene.
For AI assistance we therefore instruct Gemini to structure responses in a specific format with an addition to the preamble:
```
You are going to answer to the query in these steps:
*  THOUGHT
*  TITLE
*  ACTION
*  ANSWER
*  SUGGESTIONS
Use THOUGHT to explain why you take the ACTION. Use TITLE to provide a short summary of the thought.

```

This structure is then used to present Gemini's thought processes and actions as initially collapsed steps, preventing information overload while still allowing users to examine the underlying details or stop execution in case of unintended side effects.
Collapsed and a paused thinking steps in Chrome DevTools AI assistance.
This approach isn't just about observing the AI; it's about actively learning from it. By expanding these sections, users can analyze the data Gemini deemed relevant for debugging a specific issue and understand the process it followed. This transparency allows users to learn from the AI's debugging strategies, so they can apply similar techniques to future challenges, even when working without AI.
To further enhance the user experience, AI assistance also provides contextually relevant suggestions following the AI's answer. These suggestions streamline the conversation, offering ideas for the next debugging step or even allowing users to directly execute recommended fixes with a single click.
Exemplary suggested follow-up prompts in AI assistance, generated as part of the response.
Initially, to generate step titles and suggestions in AI assistance, we considered using a smaller, separate model specifically for summarization. However, we realized that the ReAct pattern, which structures the Gemini's reasoning into a loop of "Thoughts" and "Actions" can be effectively extended. So instead of introducing a second model, which would also come with additional latency, we modified our [prompt](https://source.chromium.org/chromium/chromium/src/+/main:third_party/devtools-frontend/src/front_end/panels/ai_assistance/agents/StylingAgent.ts;l=50;drc=f63da124ddddc34f8b2595fbff342c633e0b21d2) to instruct Gemini to generate not only its core "Thoughts" and "Actions," but also concise titles and helpful suggestions within the same ReAct loop.
## Eval driven development
The development of AI assistance for styling was driven by a rigorous evaluation process. To measure its performance and identify areas for improvement, we curated a comprehensive collection of real-world web debugging examples, touching on common overflow problems, web components, animations and more. This enabled us to map the breadth of the web debugging problem space and thoroughly understand the associated challenges. But that's a job never done: with new features being added to the web platform on a regular basis we need to keep those examples up to date in the future.
Those examples are fed into an automated evaluation pipeline, recording Gemini's responses. Data from those automated test runs are then made available in a custom-built tool in which we manually evaluate Gemini's performance for AI assistance against predefined rubrics, which inform our subsequent development efforts.
This evaluation-driven approach ensures that all changes, whether refining existing behaviors or introducing new capabilities, are carefully verified to both achieve their intended improvements and prevent regressions in existing functionality.
To further enhance our evaluation process, we are exploring automated verification methods, including:
  * Assertions to confirm correct application of fixes
  * Code-based checks to prevent undesired outputs from Gemini
  * Utilizing LLMs as judges, guided by specific rubrics, to semi-automate and accelerate our manual evaluations


While automated verification helps to scale, human feedback is important. We are collecting human feedback with voting controls under every response in AI assistance to learn how satisfied users are. An additional Report button allows users to give more exact feedback for disputable responses.
## Prompt injections
A well-known and documented limitation of LLMs is that they are prone to [prompt injections](https://developer.chrome.com/docs/devtools/ai-assistance#prompt-injection). Prompt injection is the technique of finding a way to overwrite the original system instructions of an LLM, making it output content not intended by the developers.
Most models by now have built-in mitigations for prompt injection, as does Gemini. For AI assistance in addition we also try to mitigate this in our preamble by including the following instruction:
```
If the user asks a question about religion, race, politics, sexuality, gender, or other sensitive topics, answer with "Sorry, I can't answer that. I'm best at questions about debugging web pages.

```

While this works for some explicit off-topic questions, it is not perfect. One drawback we noticed is that short and ambiguous queries might get classified as off-topic.
## Building off a solid foundation
When introducing AI to your product for the first time it's worthwhile to go step by step, rather than take a single big jump at once. That's also how we approached it for AI assistance. With everything we learned when building the styling agent we created a solid foundation to extend AI assistance into other areas of DevTools later on.
Having already solved most of the bigger challenges when working on the styling agent only a few months later we were able to introduce AI assistance for network, performance and sources and could focus on their individual challenges.
### Security implications when working with network requests
AI assistance for network allows users to discuss specific network requests with Gemini, using data from the request as context for the conversation. Specifically the following data is sent to Gemini:
  * **Request Headers** : A subset of headers sent by the browser to the server.
  * **Response Headers** : A subset of headers returned by the server.
  * **Response Status** : The HTTP status code indicating the server's response (for example 200, 404).
  * **Timings** : Detailed timing information covering various phases of the request, such as connection setup and data transfer.
  * **Request Initiator Chain** : The sequence of actions and scripts that initiated the request.


While headers are important to fully understand how a request comes together, they bear a security risk: they might contain credentials like API keys, session tokens or even plain passwords. To protect such sensitive information, we don't transmit all headers to Gemini. Instead, we maintain an allow list of permitted headers. Values of headers not on the allowlist are replaced with `<redacted>`. This approach ensures that Gemini receives the necessary context while protecting user data.
### Adapting to various data formats
AI assistance for sources lets developers ask questions about a source file in the Sources panel, for example, "What is this file for?".
The data about the file, including the filename, file content and whether it is source-mapped is all sent in a single prompt. This works well because it's just plain text. But large text files or binary files pose a challenge for LLMs. For binary files, we decided to indicate that the content is binary in the prompt and not send any actual content. For large text files, we only send a smaller part of the content taken from the beginning of the file.
For AI assistance for performance, which allows developers to ask questions about a particular task from a recorded performance profile, there is a similar challenge to create a representation that fits into Gemini's context window and also can be interpreted to provide additional insights.
To create such a presentation from a performance profile, we created a dedicated serializer called [`AiCallTree`](https://source.chromium.org/chromium/chromium/src/+/main:third_party/devtools-frontend/src/front_end/panels/timeline/utils/AICallTree.ts;l=22;drc=1f1d642265eb4be3d20beca43b0bd259a8f33a9d) which formats the call tree for a task in a way that an LLM can process. Going forward we are going to explore the ReAct strategy here too, to minimize the amount of data that needs to be sent to Gemini upfront.
## AI assistance in the future
The result of all this work is now available starting with Chrome 132, which includes AI assistance for styling, network, sources and performance. We hope you enjoy using it as much as we did building it.
To get an idea where to start, check the comprehensive [AI assistance quickstart guide](https://developer.chrome.com/docs/devtools/ai-assistance/quickstart) with plenty of demo prompts to try on your own pages and make sure to let us know what you think in our open [discussion bug](https://crbug.com/364805393).
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-01-14 UTC.

