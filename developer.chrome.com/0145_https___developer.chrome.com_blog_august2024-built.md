---
url: https://developer.chrome.com/blog/august2024-built-in-ai?hl=en
title: https://developer.chrome.com/blog/august2024-built-in-ai?hl=en
date: 2025-05-11T16:53:55.240116
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/august2024-built-in-ai?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/august2024-built-in-ai?hl=es-419)




  * On this page
  * [Why are we running this experiment?](https://developer.chrome.com/blog/august2024-built-in-ai?hl=en#why_are_we_running_this_experiment)
  * [What are we building?](https://developer.chrome.com/blog/august2024-built-in-ai?hl=en#what_are_we_building)
    * [Prompt API in Chrome Extensions](https://developer.chrome.com/blog/august2024-built-in-ai?hl=en#prompt_api_in_chrome_extensions)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  Participate in the Chrome built-in AI experiment 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Why are we running this experiment?](https://developer.chrome.com/blog/august2024-built-in-ai?hl=en#why_are_we_running_this_experiment)
  * [What are we building?](https://developer.chrome.com/blog/august2024-built-in-ai?hl=en#what_are_we_building)
    * [Prompt API in Chrome Extensions](https://developer.chrome.com/blog/august2024-built-in-ai?hl=en#prompt_api_in_chrome_extensions)


Kenji Baheux 
Alexandra Klepper 
[ GitHub ](https://github.com/alexandrascript) [ LinkedIn ](https://www.linkedin.com/in/alexandraklepper) [ Bluesky ](https://bsky.app/profile/alexandrascript.com)
Published: August 5, 2024 
The Chrome team is excited to see the enthusiasm around the Prompt API in Chrome, part of the [built-in AI](https://developer.chrome.com/docs/ai/built-in) effort. We announced this experiment at Google I/O this past May, along with the chance to sign up for the [Early Preview Program (EPP)](https://developer.chrome.com/docs/ai/join-epp). By signing up, you can try early stage APIs, such as the Prompt API, and gain the opportunity to share your feedback on how you're using these APIs in local prototypes.
It's still early days for built-in AI and the Prompt API. We hope you'll continue to be this excited throughout this experiment, as we change the API and its implementation to address your feedback and make it easier to use.
## Why are we running this experiment?
We have a lot to learn. What are your business needs that may benefit from AI? Are there features you want to offer your users, but can't due to prohibitive cost, privacy constraints, or latency concerns? How can we make it easier for you to start using this technology without significant investment or deep AI knowledge?
One of the best ways to learn is through experimentation. So, we're proposing and building APIs to give you access to new, experimental capabilities offered by on-device LLMs, such as Gemini Nano.
Chrome offers a variety of experimental APIs for developers. These APIs are accessible with [Chrome flags](https://developer.chrome.com/docs/web-platform/chrome-flags), which are essentially switches that enable or disable specific browser functions. Flags are a way for us to test our hypotheses and gather feedback from developers, as you build prototypes and experiment. The APIs may change frequently based on this feedback, and there's no guarantee they'll ship. We may discontinue a flag if it doesn't meet expectations, or we may find we need to solve a different problem than initially thought.
The development of new APIs is a long process, and these experimental flags help us learn, adapt and innovate effectively.
For built-in AI, we need your feedback to ensure we build features that have real, practical use cases and meet your performance and quality expectations. That's why we're inviting you to join the Early Preview Program—help us build AI APIs you're enthusiastic to use.
## What are we building?
We are building two types of APIs for built-in AI:
  * Task APIs that allow developers to access built-in AI capabilities, such as a translation API or a summarization API. Task APIs are designed to run inference against well-established models for the assignment.
  * Exploratory APIs that are primarily intended for local prototyping. With these APIs, we intend to ask for feedback, confirm assumptions, and determine what task APIs we build in the future. As such, exploratory APIs may never launch.


Our EPP members can now experiment with the Prompt API, to send natural language requests to Gemini Nano in Chrome. The [Prompt API explainer](https://github.com/explainers-by-googlers/prompt-api/blob/main/chrome-implementation-differences.md) differs from the current implementation, as there are additional methods and enhancements we hope to implement over time.
Based on valuable feedback from EPP members, we've learned that a dedicated task API might not be the best solution for every use case. Early preview participants are seeing potential for focused task APIs and the more versatile Prompt API. To explore this further, we are determining if it's possible to make the Prompt API available in Chrome extensions.
### Prompt API in Chrome Extensions
Chrome Extensions would allow you to experiment in a real environment, and would allow us to gain deeper insights. Based on the findings, we can refine the API to better address real-world use cases.
Our goal is to use this simpler scope to test some ideas, learn more effectively than from isolated prototypes, which would ultimately support a higher quality API.
This proposal is still in review, so we don't yet have a detailed timeline for when the Prompt API would be available in Chrome Extensions.
## What's next?
We have more work to do in the EPP, and eventually, we'll create [origin trials](https://developer.chrome.com/docs/web-platform/origin-trials) to gather even more valuable feedback from the web platform, and offer additional experimental APIs, in accordance with Chromium's [launch process](https://www.chromium.org/blink/launching-features/). We're collaborating with other browser vendors, so we can work to standardize as many built-in APIs as possible.
When we have a timeline, we'll share it on the [Chrome for Developers blog](https://developer.chrome.com/blog) and with the [mailing list](https://groups.google.com/a/chromium.org/g/chrome-ai-dev-public-announce). Sign up to make sure you see these announcements.
There's so much innovation happening, and we're excited for the growing presence of web-first AI. Built-in AI is just one piece of that story. Our goal is to learn as much as possible, ensuring that we meet your needs and expectations 
We understand that you may want more details. We highly recommend signing up for our [Early Preview Program](https://developer.chrome.com/docs/ai/join-epp) and the [Chrome AI developer public announcements mailing list](https://groups.google.com/a/chromium.org/g/chrome-ai-dev-public-announce).
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-08-05 UTC.

