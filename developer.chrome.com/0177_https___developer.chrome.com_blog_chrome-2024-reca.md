---
url: https://developer.chrome.com/blog/chrome-2024-recap?hl=en
title: https://developer.chrome.com/blog/chrome-2024-recap?hl=en
date: 2025-05-11T16:54:27.532533
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/chrome-2024-recap?hl=en#main-content)


  * On this page
  * [Built-in AI in Chrome helps developers deliver powerful features with Gemini](https://developer.chrome.com/blog/chrome-2024-recap?hl=en#built-in_ai_in_chrome_helps_developers_deliver_powerful_features_with_gemini)
  * [On-device AI gets a boost with WebAssembly (Wasm) and WebGPU enhancements](https://developer.chrome.com/blog/chrome-2024-recap?hl=en#on-device_ai_gets_a_boost_with_webassembly_wasm_and_webgpu_enhancements)
  * [View Transition API makes sites feel more connected than ever with frictionless navigation](https://developer.chrome.com/blog/chrome-2024-recap?hl=en#view_transition_api_makes_sites_feel_more_connected_than_ever_with_frictionless_navigation)
  * [CSS popover and anchor positioning enables interactive overlays without JavaScript](https://developer.chrome.com/blog/chrome-2024-recap?hl=en#css_popover_and_anchor_positioning_enables_interactive_overlays_without_javascript)
  * [Speculation Rules API unlocks near-instant navigation by prerendering pages](https://developer.chrome.com/blog/chrome-2024-recap?hl=en#speculation_rules_api_unlocks_near-instant_navigation_by_prerendering_pages)
  * [Interaction to Next Paint (INP) becomes a Core Web Vital](https://developer.chrome.com/blog/chrome-2024-recap?hl=en#interaction_to_next_paint_inp_becomes_a_core_web_vital)
  * [Autofill lets you delight users with smoother online checkouts](https://developer.chrome.com/blog/chrome-2024-recap?hl=en#autofill_lets_you_delight_users_with_smoother_online_checkouts)
  * [Chrome DevTools levels up with AI-powered solutions](https://developer.chrome.com/blog/chrome-2024-recap?hl=en#chrome_devtools_levels_up_with_ai-powered_solutions)
  * [Baseline 2024 brings developers new cross-browser web features](https://developer.chrome.com/blog/chrome-2024-recap?hl=en#baseline_2024_brings_developers_new_cross-browser_web_features)
  * [Major browsers make more features Baseline with Interop 2024](https://developer.chrome.com/blog/chrome-2024-recap?hl=en#major_browsers_make_more_features_baseline_with_interop_2024)
  * [Shaping the web's growth together in the new year](https://developer.chrome.com/blog/chrome-2024-recap?hl=en#shaping_the_webs_growth_together_in_the_new_year)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  Chrome's 2024 recap for devs: Re-imagining the web with AI in DevTools, built-in Gemini, and new UI capabilities 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Built-in AI in Chrome helps developers deliver powerful features with Gemini](https://developer.chrome.com/blog/chrome-2024-recap?hl=en#built-in_ai_in_chrome_helps_developers_deliver_powerful_features_with_gemini)
  * [On-device AI gets a boost with WebAssembly (Wasm) and WebGPU enhancements](https://developer.chrome.com/blog/chrome-2024-recap?hl=en#on-device_ai_gets_a_boost_with_webassembly_wasm_and_webgpu_enhancements)
  * [View Transition API makes sites feel more connected than ever with frictionless navigation](https://developer.chrome.com/blog/chrome-2024-recap?hl=en#view_transition_api_makes_sites_feel_more_connected_than_ever_with_frictionless_navigation)
  * [CSS popover and anchor positioning enables interactive overlays without JavaScript](https://developer.chrome.com/blog/chrome-2024-recap?hl=en#css_popover_and_anchor_positioning_enables_interactive_overlays_without_javascript)
  * [Speculation Rules API unlocks near-instant navigation by prerendering pages](https://developer.chrome.com/blog/chrome-2024-recap?hl=en#speculation_rules_api_unlocks_near-instant_navigation_by_prerendering_pages)
  * [Interaction to Next Paint (INP) becomes a Core Web Vital](https://developer.chrome.com/blog/chrome-2024-recap?hl=en#interaction_to_next_paint_inp_becomes_a_core_web_vital)
  * [Autofill lets you delight users with smoother online checkouts](https://developer.chrome.com/blog/chrome-2024-recap?hl=en#autofill_lets_you_delight_users_with_smoother_online_checkouts)
  * [Chrome DevTools levels up with AI-powered solutions](https://developer.chrome.com/blog/chrome-2024-recap?hl=en#chrome_devtools_levels_up_with_ai-powered_solutions)
  * [Baseline 2024 brings developers new cross-browser web features](https://developer.chrome.com/blog/chrome-2024-recap?hl=en#baseline_2024_brings_developers_new_cross-browser_web_features)
  * [Major browsers make more features Baseline with Interop 2024](https://developer.chrome.com/blog/chrome-2024-recap?hl=en#major_browsers_make_more_features_baseline_with_interop_2024)
  * [Shaping the web's growth together in the new year](https://developer.chrome.com/blog/chrome-2024-recap?hl=en#shaping_the_webs_growth_together_in_the_new_year)


Paul Kinlan 
[ GitHub ](https://github.com/PaulKinlan) [ Glitch ](https://glitch.com/@PaulKinlan) [ LinkedIn ](https://www.linkedin.com/in/paulkinlan) [ Mastodon ](https://status.kinlan.me/@paul) [ Bluesky ](https://bsky.app/profile/paul.kinlan.me) [ Homepage ](https://paul.kinlan.me/)
Natalia Gvak 
[ LinkedIn ](https://www.linkedin.com/in/natalia-g-13b4a0)
Bradford Lee 
[ LinkedIn ](https://www.linkedin.com/in/bradfordlee)
Published: December 13, 2024 
Being online when the web was just starting off meant waiting patiently through slow dial-up and twiddling with bits of Perl and HTML. But the web has evolved exponentially in what feels like an instant. Whether you're getting last-minute grocery deliveries or using AI to summarize a ton of long articles, a link is now a portal to endless possibilities.
It's why so many of us love the web. To help you captivate more people around the world, we've been launching new tools for all web developers—whether you're frontend or full stack, novice or pro.
Check out our 2024 roundup of innovative capabilities that let you build more imaginative web experiences with less lift.
## Built-in AI in Chrome helps developers deliver powerful features with Gemini
At Google I/O 2024, we announced how we're using AI to supercharge the web with Gemini Nano built directly in Chrome. To date, more than 13,000 of you have joined the [early preview program](https://docs.google.com/forms/d/e/1FAIpQLSfZXeiwj9KO9jMctffHPym88ln12xNWCrVkMY_u06WfSTulQg/viewform?resourcekey=0-dE0Rqy_GYXDEWSnU7Z0iHg) to help us shape the future of the web. We're so grateful for your contributions, and we can't wait for all the innovative AI experiences you'll build.
To help you make the most of AI, we've launched several [built-in APIs](https://developer.chrome.com/docs/ai/built-in-apis) into origin trials—such as the experimental [Prompt API](https://developer.chrome.com/docs/extensions/ai/prompt-api), [Translator API](https://developer.chrome.com/docs/ai/translator-api), [Summarizer API](https://developer.chrome.com/docs/ai/summarizer-api), and [Language Detector API](https://developer.chrome.com/docs/ai/language-detection). All of them let you run AI-powered tasks in the browser without server calls, and there's no need to manage and deploy your own AI models. Over 8,600 developers registered for the [Google Chrome Built-in AI Challenge](https://googlechromeai.devpost.com/?linkId=11071015) to build a web app or Chrome Extension using these APIs. We'll be announcing the winners in mid-January, so stay tuned.
PolicyBazaar uses the Language Detector API to detect the language when a customer switches languages during the conversation. 
## On-device AI gets a boost with WebAssembly (Wasm) and WebGPU enhancements
We believe the web is the best runtime for you to build AI-enabled apps that can reach everyone. To complement our work on built-in AI APIs, we've also made improvements to two technologies that enable you to bring your own AI models to the web and run them at speed: WebGPU and Wasm.
We've introduced [16-bit floating point values in WebGPU](https://developer.chrome.com/blog/new-in-webgpu-120#support_for_16-bit_floating-point_values_in_wgsl) and [packed integer dot products](https://developer.chrome.com/blog/io24-webassembly-webgpu-2#packed_integer_dot_products), which unlock more flexible use of a device's GPU with compute shaders. Future improvements planned for WebGPU include [subgroups and subgroup matrices](https://developer.chrome.com/blog/next-for-webgpu). These features will let apps communicate quickly between GPU threads and make the most of fixed-size matrix multiplication. We'll also be introducing [Memory64](https://github.com/WebAssembly/memory64/blob/main/proposals/memory64/Overview.md) to Wasm in 2025 to let larger AI models be addressed in memory.
The WebGPU Benchmark from Transformers.js shows WebGPU is 32.51 times faster than Wasm. 
## View Transition API makes sites feel more connected than ever with frictionless navigation
With new capabilities such as [cross-document view transitions](https://developer.chrome.com/docs/web-platform/view-transitions/cross-document), you can create seamless, fluid navigation across multiple pages. All it takes is a few lines of CSS to get rid of those pesky reload "blinks." The resulting fluid, native-like navigation helps you deliver more immersive experiences while keeping the benefits of multi-page architectures.
View transitions enable fluid cross-page navigations. [See the view transitions demo.](https://view-transitions.chrome.dev/off-the-beaten-path/mpa/)
## CSS popover and anchor positioning enables interactive overlays without JavaScript
You can now create tooltips, menus, and other overlays with `popover` and visually connect them to their trigger elements with the [CSS Anchor Positioning API](https://developer.chrome.com/docs/css-ui/anchor-positioning-api). All you need is a bit of CSS and HTML to make sure overlays stay anchored and visible even as people scroll or resize windows. Your users get a more reliable, dynamic web experience, and you're freed from z-index management and complicated JavaScript positioning math. It's a win-win.
## Speculation Rules API unlocks near-instant navigation by prerendering pages
Page load times went from fast to nearly instant this year with the [Speculation Rules API](https://developer.chrome.com/docs/web-platform/prerender-pages). This API, which just takes a few lines of JSON to implement, allows pages to be prerendered fully in the background so they're ready to go whenever your users are.
It takes web.dev 1.6 seconds to load without prerendering and 0.2 seconds with it.
## Interaction to Next Paint (INP) becomes a Core Web Vital
[INP](https://web.dev/inp/) replaced First Input Delay as a Core Web Vital in March to help you measure page responsiveness more comprehensively beyond the first user input. Since then, there's been a [9% increase in the number of sites having "good" INP on mobile](https://httparchive.org/reports/chrome-ux-report?start=2024_03_01&end=2024_10_01&view=list#cruxFastInp)—which translates to faster, more enjoyable user experiences across the web.
## Autofill lets you delight users with smoother online checkouts
Enabling [autofill](https://developer.chrome.com/docs/identity/autofill), which lets browsers automatically fill in form fields with users' saved information, can encourage people to finish submitting forms. When the Chrome team analyzed anonymous, aggregated data across thousands of online forms, they found form abandonment reduced by an average of 75% when autofill was used. Although many factors contribute to a positive checkout experience, the data suggests autofill can play a helpful role.
Autofill is particularly useful for ecommerce checkout flows. At [Shopify,](https://shopify.dev/) guest checkouts using autofill have a 45% higher checkout conversion rate than guest checkouts without autofill.
## Chrome DevTools levels up with AI-powered solutions
You might remember we introduced Gemini to Chrome DevTools with [console insights](https://developer.chrome.com/docs/devtools/console/understand-messages), enabling you to access AI-powered debugging for more efficient troubleshooting. Since Google I/O 2024, this feature has become available globally.
We've also launched the [AI assistance panel](https://developer.chrome.com/docs/devtools/ai-assistance/quickstart), which uses Gemini to help you understand your page's technical details such as styling, network requests, sources, and performance.
Console insights and the AI assistance panel are two of many DevTools improvements in 2024. 
You might've noticed the Performance panel got a lot of improvements this year too, including the ability [to monitor Core Web Vitals](https://developer.chrome.com/blog/devtools-realtime-cwv) in real time and [add annotations](https://developer.chrome.com/blog/devtools-annotations). Additionally, we brought the power of Lighthouse into the Performance panel with [performance insights](https://developer.chrome.com/blog/new-in-devtools-131#insights).
With these AI-enabled enhancements, Performance panel improvements, and dozens of quality of life updates such as [scroll badges](https://developer.chrome.com/blog/swe-devtools-scroll-badge), Chrome DevTools is more helpful than ever. Even more improvements, such as upgraded performance with the new Gemini 2.0 models, [are coming in 2025.](https://developers.googleblog.com/en/the-next-chapter-of-the-gemini-era-for-developers/)
## Baseline 2024 brings developers new cross-browser web features
From gradient interpolation to registered custom properties, [Baseline 2024](https://webstatus.dev/?q=baseline_date%3A2024-01-01..2024-12-31) includes 39 new, cross-browser web features so far. You shouldn't need to worry about interoperability once a feature has been a part of Baseline for at least 30 months. But if you're trying to decide whether using a new feature is worth potentially losing some reach, check out Akamai's [RUM Archive Insights](https://rumarchive.com/insights) for the features of each Baseline version and global user share.
Our favorite Baseline announcement of the year is the [Web Platform Status dashboard](https://webstatus.dev/), which lays out all the web features along with their level of cross-browser support. What's even more exciting is that the data that powers the Web Platform Status dashboard is [open and available](https://www.npmjs.com/package/web-features) for you to use and integrate into your own tooling. A great example of this is the [Baseline banner](https://github.com/web-platform-dx/baseline-status).
## Major browsers make more features Baseline with Interop 2024
To help bring more features to Baseline, we've once again been working with our partners on [Interop 2024](https://web.dev/blog/interop-2024). This year's target features include popover, CSS nesting, font-size-adjust, and relative color syntax.
Interop also outlines scores for experimental and stable browser releases. The overall Interop score for stable browsers is currently at 87, and Chrome Stable has a score of 98 as we approach the end of the year. You can keep up with browsers' progress on the [Interop Dashboard](https://wpt.fyi/interop-2024). We're already planning for Interop 2025, which we'll be announcing in February.
## Shaping the web's growth together in the new year
As exciting as our 2024 progress is, we know the future is even brighter. And that's all thanks to the collective passion, feedback, and innovation from you—our developer community. At events all around the world, from the [BrazilJS Conference](https://conf.braziljs.org/) and [DevFest Paris](https://devfest.gdgparis.fr/) to [Google I/O 2024](https://io.google/2024/) and the [first-ever Web AI Summit](https://developers.googleblog.com/en/web-ai-summit-2024-recap/), one thing was clear to us time and time again: All of you believe in the web's power and potential just as much as we do.
You've got bolder ideas than ever. We're dedicated to helping you bring them to life. So stay connected with us on [X](https://twitter.com/ChromiumDev), [YouTube](https://www.youtube.com/user/ChromeDevelopers), and [LinkedIn](https://www.linkedin.com/showcase/chrome-for-developers/) for our latest updates—and let's [re-imagine the power of the web](https://www.youtube.com/playlist?list=PLNYkxOF6rcIA7z8m5u91ekf81ZXDjTMIZ) together.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-12-13 UTC.

