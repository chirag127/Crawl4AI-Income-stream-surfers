---
url: https://developer.chrome.com/docs/extensions/ai
title: https://developer.chrome.com/docs/extensions/ai
date: 2025-05-11T16:51:40.974128
depth: 1
---

[ Skip to main content ](https://developer.chrome.com/docs/extensions/ai#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/extensions/ai?hl=es-419)






###  Extensions and AI 
AI can mean many things: machine learning, large language models, generative AI and more. Here you'll find resources built for understanding how to effectively use AI in Chrome extensions. 
###  Enhance the browsing experience with AI-powered extensions 
Extensions enable you to enhance your browsing experience by controlling web content and customizing the browser. With AI you can take this to the next level. 
  * web 
####  Control web content 
Use AI to help create and comprehend content on the web. 
  * favorite 
####  Make the browser more helpful 
Use the powerful extension APIs to enrich the bookmark experience, provide a better new tab page or make it easier to re-discover content from your browsing history. 
  * insert_emoticon 
####  Customize the browser 
Seamlessly embed your AI functionality into the browser via side panel, new-tab page, action bar or context menus. 


###  [ Use cases ](https://developers.googleblog.com/en/how-its-made-exploring-ai-x-learning-through-shiffbot-an-ai-experiment-powered-by-the-gemini-api/)
You can build AI-powered extensions that summarize text, help with translation, generate content, assist with coding, provide recommendations, personalize user interfaces, and so much more. Check out how the Google Creative Lab team used AI and extensions to build an interactive creative coding experience. 
computer 
###  Client-side AI 
Client-side AI is the latest offering for bringing powerful models to users, while protecting sensitive data and improving latency. Client-side AI cannot completely replace and replicate the work you do on the cloud, however, client-side AI can unlock great possibilities for your extensions such as ability to use purpose-built models, faster response times, offline availability and more. 
  * [Learn more about client-side AI](https://developer.chrome.com/docs/ai/client-side)


cloud 
###  Cloud AI 
Cloud AI offers a blend of power, scaleability and ease of integration. Cloud platforms provide access to cutting-edge hardware and software, ensuring high performance and continuous improvement through regular updates. The Gemini ecosystem brings together all Google's models, products and platforms. 
  * [Learn more about Gemini](https://ai.google/gemini-ecosystem)


###  [ Prompt API in Extensions ](https://developer.chrome.com/docs/extensions/ai/prompt-api)
Discover the infinite possibilities of the Prompt API in Chrome Extensions. 
###  [ Translator API ](https://developer.chrome.com/docs/ai/translator-api)
Live translate text in the browser using local AI models. Now, users can contribute in their first language. 
###  [ Language Detector API ](https://developer.chrome.com/docs/ai/language-detection)
Identify the language used in any given text with the Language Detector API. 
###  [ Summarizer API ](https://developer.chrome.com/docs/ai/summarizer-api)
Generate different types of summaries in varied lengths and formats, such as sentences, paragraphs, bullet point lists, and more. 
###  [ How to use the Gemini Cloud API in a Chrome extension ](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/functional-samples/ai.gemini-in-the-cloud)
Try out an extension that provides a chat interface for the Gemini API. Explore the code demonstrates how to use the Gemini Cloud API in a Chrome extension. 
###  [ How to use the Gemini Nano API in a Chrome extension ](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/functional-samples/ai.gemini-on-device)
This extension provides a chat interface using the prompt API with Chrome's experimental built-in Gemini Nano model. Try out the extension and explore the code. 
###  [ Client-side Summarization with Gemini Nano ](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/functional-samples/ai.gemini-on-device-summarization)
Try out an extension that summarizes the content of the currently open tab, built with the experimental Summarization API in Chrome. 
###  [ The Prompt API in Chrome Extensions ](https://developer.chrome.com/blog/prompt-api-origin-trial)
The Prompt API is now available in an origin trial for Extensions. You can build Chrome Extensions that use Gemini Nano, our most efficient language model, built in the browser. 
[Join the origin trial](https://developer.chrome.com/blog/prompt-api-origin-trial)
###  [ Participate in the built-in AI Early Preview Program ](https://docs.google.com/forms/d/e/1FAIpQLSfZXeiwj9KO9jMctffHPym88ln12xNWCrVkMY_u06WfSTulQg/viewform?resourcekey=0-dE0Rqy_GYXDEWSnU7Z0iHg)
We need your input to shape the APIs, ensure they fulfill your use cases, and inform our discussions with other browser vendors for standardization. Join our Early Preview Program to provide feedback on early-stage built-in AI ideas, and discover opportunities to test in-progress APIs through local prototyping. 
###  When possible, use smaller models 
For larger, client-side models, trigger the download after the extension is installed. Manage the life cycle of your model independently of your extension and your users won't have to download the model with every extension update. Note that models are not considered remote hosted code. 
###  Protect your API keys 
Never share your keys with Chrome Web Store. Ask users to provide an API key. Proxy calls through your own server. Fetch the API key from your server before using it. 
###  Protect user privacy 
If you're using cloud AI APIs or otherwise sharing user input with a server, update your privacy policy to include what information is shared. 
###  [ Join the Built-in AI Challenge ](https://developer.chrome.com/blog/ai-challenge)
You're invited to reimagine the web with built-in AI. Create innovative web applications and Chrome Extensions, using Chrome's integrated AI models and APIs. Prizes total $65,000 USD. 
###  [ What is AI? ](https://web.dev/articles/ai-overview)
Understand the basics and definitions of the various emerging technologies, often referred to as AI. 
[developer.chrome.com](https://developer.chrome.com/docs/extensions/develop)
###  [ Learn all about developing Chrome extensions ](https://developer.chrome.com/docs/extensions/develop)
Learn how Chrome extensions work, what they can do, and how to build them. 
[developer.chrome.com](https://developer.chrome.com/docs/ai)
###  [ AI on Chrome ](https://developer.chrome.com/docs/ai)
Discover how AI can make it easier for developers to build powerful experiences on the web. 

