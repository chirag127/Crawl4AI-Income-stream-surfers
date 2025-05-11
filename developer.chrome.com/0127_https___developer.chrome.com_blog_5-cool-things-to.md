---
url: https://developer.chrome.com/blog/5-cool-things-to-do-with-ai-assistance
title: https://developer.chrome.com/blog/5-cool-things-to-do-with-ai-assistance
date: 2025-05-11T16:53:32.385073
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/5-cool-things-to-do-with-ai-assistance#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/5-cool-things-to-do-with-ai-assistance?hl=es-419)




  * On this page
  * [1. Understand layouts](https://developer.chrome.com/blog/5-cool-things-to-do-with-ai-assistance#1_understand_layouts)
  * [2. Pair-programming](https://developer.chrome.com/blog/5-cool-things-to-do-with-ai-assistance#2_pair-programming)
  * [3. Accessibility advisor](https://developer.chrome.com/blog/5-cool-things-to-do-with-ai-assistance#3_accessibility_advisor)
  * [4. Make it yours](https://developer.chrome.com/blog/5-cool-things-to-do-with-ai-assistance#4_make_it_yours)
  * [5. Become an aircraft mechanic](https://developer.chrome.com/blog/5-cool-things-to-do-with-ai-assistance#aircraft)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  5 Cool Things To Do with DevTools AI Assistance 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [1. Understand layouts](https://developer.chrome.com/blog/5-cool-things-to-do-with-ai-assistance#1_understand_layouts)
  * [2. Pair-programming](https://developer.chrome.com/blog/5-cool-things-to-do-with-ai-assistance#2_pair-programming)
  * [3. Accessibility advisor](https://developer.chrome.com/blog/5-cool-things-to-do-with-ai-assistance#3_accessibility_advisor)
  * [4. Make it yours](https://developer.chrome.com/blog/5-cool-things-to-do-with-ai-assistance#4_make_it_yours)
  * [5. Become an aircraft mechanic](https://developer.chrome.com/blog/5-cool-things-to-do-with-ai-assistance#aircraft)


Matthias Rohmer 
[ GitHub ](https://github.com/matthiasrohmer) [ LinkedIn ](https://www.linkedin.com/in/matthias-rohmer-b09191b0) [ Bluesky ](https://bsky.app/profile/matthiasrohmer.bsky.social)
Published: October 21, 2024 
Last week we introduced a whole new panel to DevTools: [AI assistance](https://developer.chrome.com/docs/devtools/ai-assistance/styling) can help you debug styling issues with Gemini directly in DevTools.
Curious to see what it can do? Check out these 5 awesome ways this new feature can make styling your page easier - from understanding layouts to [_fixing airplanes_](https://developer.chrome.com/blog/5-cool-things-to-do-with-ai-assistance#aircraft).
A screen recording of how **AI assistance** helps implement a marquee effect using CSS animations
## 1. Understand layouts
When building websites you are not always starting from scratch. Often enough you need to build on top of existing code that you have no prior knowledge of - and in the worst case no one around you has either.
Ask AI about an element's layout and understand why it's displayed the way it is down to the last node - and why this `overflow: hidden;` on an element is actually there for a reason. 👀
**Prompt to try**
```
Give me a summary of how this element and its children are laid out and re-create the layout in ASCII.

```

## 2. Pair-programming
CSS really got powerful by now. With so many possibilities it's all okay to get confused sometimes: is it `align-items` that I need? Or `justify-items`? Or rather `justify-self` or `align-content`?
Sometimes you really know what you want to do but just can't get the right set of CSS properties. Next time you find yourself in this situation, explain your problem to AI and let it figure out things for you.
**AI assistance** will investigate your existing code and compare it to what you are trying to achieve, suggesting the required fixes for you to review, apply, and copy into your codebase.
## 3. Accessibility advisor
Making your website accessible and easy to use with assistive technology is important. Consider accessibility from the start of development, rather than as an afterthought and aim to follow the [Web Content Accessibility Guidelines](https://www.w3.org/WAI/standards-guidelines/wcag/) (WCAG) throughout your development process.
Use **AI assistance** to get tips on where a `<div>` could be replaced with a more semantic HTML element, how an additional `aria-*` attribute can be helpful, or how color contrast can be improved.
**Prompt to try**
```
What about color contrast in this element?

```

## 4. Make it yours
Trends come and go: there were gradients, shadows and harsh borders, followed by flat design, moving into today's design era with bright neon colors on dark backgrounds.
Bootstrap Button styles over time, from version 1 to 5, top to bottom.
But isn't it sometimes tiring how uniform things can look on the web? If it's one of those days for you, maybe ask AI assistance to switch things up and make the web a little more fun again - like on a theme park ride!
**Prompt to try**
```
This element looks a little boring. Can you make it look like a pirates theme park ride?

```

## 5. Become an aircraft mechanic
Explaining styling issues, helping to fix them, advising on accessibility and changing existing styles - there is already a bunch that AI assistance can support you with - and there is even more! Can you believe AI assistance even helps you fix airplanes? No previous experience required, put on your overall and [get your hands dirty in the **Chrome DevTools Hangar**](https://chrome.dev/devtools-hangar/)!
The [Chrome Devtools Hangar](https://chrome.dev/devtools-hangar/) - an interactive playground for AI assistance.
And make sure to let us know about your own experience in our [public issue tracker](https://crbug.com/364805393)!
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-10-21 UTC.

