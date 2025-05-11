---
url: https://developer.chrome.com/blog/devtools-css-value-parsing?hl=en
title: https://developer.chrome.com/blog/devtools-css-value-parsing?hl=en
date: 2025-05-11T16:55:15.685203
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/devtools-css-value-parsing?hl=en#main-content)
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


#  Beyond regular expressions: Enhancing CSS value parsing in Chrome DevTools 
Stay organized with collections  Save and categorize content based on your preferences. 
Philip Pfaffe 
[ GitHub ](https://github.com/pfaffe)
Ergün Erdogmus 
Have you noticed the CSS properties in Chrome DevTools' **Styles** tab looking a bit more polished lately? These updates, rolled out between Chrome 121 and 128, are the result of a significant improvement in how we parse and present CSS values. In this article, we'll walk you through the technical details of this transformation—moving from a regular expressions matching system to a more robust parser.
Let us compare the current DevTools with the previous version:
Quite a difference, right? Here's a break down of the key enhancements:
  * `color-mix`. A handy preview visually representing the two color arguments within the `color-mix` function.
  * `pink`. A clickable [color preview](https://developer.chrome.com/docs/devtools/css/color#change-colors) for the named color `pink`. Click it to open a color picker for easy adjustments.
  * `var(--undefined, [fallback value])`. Improved handling of undefined variables, with the undefined variable [grayed out](https://developer.chrome.com/docs/devtools/css/issues#inactive) and the active fallback value (in this case, an HSL color) displayed with a clickable color preview.
  * `hsl(…)`: Another clickable color preview for the `hsl` color function, providing quick access to the color picker.
  * `177deg`: A clickable [angle clock](https://developer.chrome.com/docs/devtools/css/reference#angle-clock) that lets you interactively drag and modify the angle value.
  * `var(--saturation, …)`: A [clickable link](https://developer.chrome.com/docs/devtools/css/reference#links) to the custom property definition, making it easy to jump to the relevant declaration.


The difference is striking. To achieve this, we had to teach DevTools to understand CSS property values a lot better than it did before.
### Weren't these previews already available?
While these preview icons may seem familiar, they haven't always been consistently displayed, especially in complex CSS syntax like the example above. Even in cases where they did work, significant effort was often required to make them function correctly.
The reason for that is that the system for analyzing values has been growing organically since the first days of DevTools. However, it hasn't been able to keep up with the recent amazing new features we're getting from CSS, and the corresponding increase in language complexity. The system required a full redesign to keep up with evolution and that's exactly what we did!
## How CSS property values are processed
In DevTools, the process of rendering and decorating property declarations in the **Styles** tab is split into two distinct phases:
  1. Structural analysis. This initial phase dissects the property declaration to identify its underlying components and their relationships. For example, in the declaration `border: 1px solid red`, it would recognize `1px` as a length, `solid` as a string, and `red` as a color.
  2. Rendering. Building upon the structural analysis, the rendering phase transforms these components into an HTML representation. This enriches the displayed property text with interactive elements and visual cues. For example, the color value `red` is rendered with a clickable color icon that, when clicked, reveals a color picker for easy modification.


## Regular expressions
Previously, we relied on regular expressions (regexes) to dissect the property values for structural analysis. We maintained a list of regexes to match the bits of property values that we considered decorating. For example, there were expressions that matched CSS colors, lengths, angles, more complicated sub-expressions such as `var` function calls, and so forth. We scanned the text from left to right to do value analysis, continuously looking for the first expression from the list that matches the next piece of the text.
While this worked fine most of the time, the number of cases where it didn't kept growing. Over the years we've received a good number of bug reports where the matching didn't quite get it right. As we fixed them – some fixes simple, others quite elaborate – we had to rethink our approach to keep our technical debt at bay. Let's take a look at some of the issues!
### Matching `color-mix()`
The regex we used for the `color-mix()` function [was](https://source.chromium.org/chromium/_/chromium/devtools/devtools-frontend/+/234d846cbaa82c0417b3f540062087a8c95813b9:front_end/core/common/Color.ts;l=2187;bpv=1;bpt=0) the following:
```
/color-mix\(.*,\s*(?<firstColor>.+)\s*,\s*(?<secondColor>.+)\s*\)/g

```

Which matches its syntax:
```
color-mix(<color-interpolation-method>,[<color> && <percentage[0,100]>?]#{2})

```

Try running the following example to visualize the matches.
```
constre=/color-mix\(.*,\s*(?<firstColor>.+)\s*,\s*(?<secondColor>.+)\s*\)/g;
//itworks-simplerexample
constsimpler=re.exec('color-mix(in srgb, pink, hsl(127deg 100% 50%))');
console.table(simpler.groups);
re.exec('');
//itdoesn't work - complex example
const complex = re.exec('color-mix(insrgb,pink,var(--undefined,hsl(127degvar(--saturation,100%)50%)))');
console.table(complex.groups);

```

The simpler example works fine. However, in the more complex example, the `<firstColor>` match is `hsl(177deg var(--saturation` and `<secondColor>` match is `100%) 50%))`, which is completely meaningless.
We knew this was a problem. After all, CSS as a formal language isn't [regular](https://en.wikipedia.org/wiki/Regular_language), so we already included [special handling](https://source.chromium.org/chromium/chromium/src/+/refs/tags/121.0.6167.90:third_party/devtools-frontend/src/front_end/panels/elements/StylePropertyTreeElement.ts;l=447) to deal with more complicated function arguments, such as `var` functions. However, as you can see in the [first screenshot](https://developer.chrome.com/blog/devtools-css-value-parsing?hl=en#color-mix-example), that still didn't work in all cases.
### Matching `tan()`
One of the more hilarious [reported](https://crbug.com/40945106) bugs was about the trigonometric `tan()` function . The regex we were using for matching colors included a sub-expression `\b[a-zA-Z]+\b(?!-)` for matching named colors such as the `red` keyword. Then we checked if the matched part is actually a named color, and guess what, `tan` is a named color too! So, we wrongly interpreted `tan()` expressions as colors.
### Matching `var()`
Let's take a look at another example, `var()` functions with a fallback containing other `var()` references: `var(--non-existent, var(--margin-vertical))`.
Our regex for `var()` would happily match this value. Except, it would _stop_ matching at the first closing parenthesis. So the above text is matched as `var(--non-existent, var(--margin-vertical)`. This is a textbook limitation of regular expression matching. Languages that require matching parenthesis are fundamentally not regular.
## Transition to a CSS parser
When text analysis using regular expressions stops working (because the analyzed language isn't regular) there's a canonical next step: use a parser for a higher-type grammar. For CSS, that means a parser for context-free languages. In fact, such a parser system already existed in the DevTools codebase: CodeMirror's [Lezer](https://lezer.codemirror.net/), which is the foundation for, for example, syntax highlighting in CodeMirror, the editor you find in the **Sources** panel. Lezer's CSS parser let us produce (non-abstract) syntax trees for CSS rules and was ready for us to use. Victory.
Except, out of the box, we found it infeasible to migrate from regex-based matching to parser-based matching directly: the two approaches work from opposing directions. When matching pieces of values with regular expressions, DevTools would scan the input from left to right, repeatedly trying to find the earliest match from an ordered list of patterns. With a syntax tree, matching would start from the bottom up, for example, analyzing the arguments of a call first, before trying to match the function call. Think of it as evaluating an arithmetic expression, where you would first consider parenthesized expressions, then multiplicative operators, then additive operators. In this framing, the regex-based matching corresponds to evaluating the arithmetic expression from left to right. We really didn't want to rewrite the entire matching system from scratch: There were [15](https://source.chromium.org/chromium/chromium/src/+/refs/tags/121.0.6167.90:third_party/devtools-frontend/src/front_end/panels/elements/StylesSidebarPane.ts;l=2313) different matchers and renderer pairs, with thousands of lines of code to them, which made it unlikely that we could ship it in a single milestone.
So we came up with a solution that allowed us to make incremental changes, which we'll describe below in more detail. In short, we kept the two-phase approach, but in the first phase we try to match sub-expressions bottom-up (thus breaking with the regex flow), and in the second phase we render top-down. In both phases, we could use the existing regex-based matchers and renders, practically unchanged, and were thus able to migrate them one by one.
### Phase 1: Bottom-up matching
The first phase more or less exactly and exclusively does what it says on the cover. We traverse the tree in order from bottom to top and try to match sub-expressions at each syntax tree node that we visit. To match a specific sub-expression, a matcher could use regex just like it did in the existing system. As of version 128 we actually still do in a few cases, for example, for [matching lengths](https://source.chromium.org/chromium/chromium/src/+/main:third_party/devtools-frontend/src/front_end/panels/elements/PropertyMatchers.ts;drc=6d89bba2a5678aba11c34af338b74e565b9d9691;l=467). Alternatively, a matcher can analyze the structure of the subtree rooted at the current node. This allows it to catch syntax errors and record structural information at the same time.
Consider the syntax tree example from above:
For this tree, our matchers would apply in the following order:
  1. `hsl(``177deg``var(--saturation, 100%) 50%)`: First, we discover the first argument of the `hsl` function call, the hue angle. We match it with an angle matcher, so that we can decorate the angle value with the angle icon.
  2. `hsl(177deg``var(--saturation, 100%)``50%)`: Second, we discover the `var` function call with a var matcher. For such calls we mainly want to do two things: 
     * Look up the variable's declaration and compute its value, and add a link and a popover to the variable name to connect to them, respectively.
     * Decorate the call with a color icon if the computed value is a color. There's actually a third thing, but we'll talk about that later.
  3. `hsl(177deg var(--saturation, 100%) 50%)`: Lastly, we match the call expression for the `hsl` function, so that we can decorate it with the color icon.


In addition to searching for sub-expressions we'd like to decorate, there's actually a second feature we're running as part of the matching process. Note that in step #2 we said we look up the computed value for a variable name. In fact, we take that one step further and propagate the results up the tree. And not just for the variable, but also for the fallback value! It's guaranteed that when visiting a `var` function node, its children have been visited beforehand, so we already know the results of any `var` functions that might appear in the fallback value. Therefore we're able to easily and cheaply substitute `var` functions with their results on the fly, which lets us trivially answer questions like "Is the result of this `var` call a color?", as we did in step #2.
### Phase 2: Top-down rendering
For the second phase, we reverse direction. Taking the match results from phase 1, we render the tree into HTML by traversing it in order from top to bottom. For each visited node, we check whether it matched and if so, call the matcher's corresponding renderer. We avoid the need for special handling for nodes that contain just text (like the `NumberLiteral` "50%") by including a default matcher and renderer for text nodes. Renderers simply output HTML nodes, which, when put together, produce the representation of the property value including its decorations.
For the example tree, here's the order in which the property value is rendered:
  1. Visit the `hsl` function call. It matched, so call the color function renderer. It does two things: 
     * Computes the actual color value using the on-the-fly substitution mechanism for any `var` arguments, then draws a color icon.
     * Recursively renders the children of the `CallExpression`. This automatically takes care of rendering the function name, parentheses, and commas, which are just text.
  2. Visit the first argument of the `hsl` call. It matched, so call the angle renderer, which draws the angle icon and the angle's text.
  3. Visit the second argument, which is the `var` call. It matched, so call the var [renderer](https://source.chromium.org/chromium/chromium/src/+/5615800ef3afa2bc100f7041c77e1305641caea0:third_party/devtools-frontend/src/front_end/panels/elements/StylePropertyTreeElement.ts;l=154), which outputs the following: 
     * The text `var(` at the start.
     * The variable name and decorates it either with a link to the variable's definition or with a gray text color to indicate it was undefined It also adds a popover to the variable to show information about its value.
     * The comma and then recursively renders the fallback value.
     * A closing parenthesis.
  4. Visit the last argument of the `hsl` call. It didn't match, so just output its text contents.


Did you notice that in this algorithm, a render fully controls how the children of a matched node are rendered? Recursively rendering the children is proactive. This trick is what enabled a step-wise migration from regex-based rendering to syntax tree-based rendering. For nodes matched with a legacy regex-matcher, the corresponding renderer could be used in its original form. In syntax tree terms, it would take responsibility for rendering the entire subtree, and its result (an HTML node) could be plugged cleanly into the surrounding rendering process. This gave us the option to port matchers and renderers in pairs, and swap them out one by one.
Another cool feature of renderers controlling the rendering of their matched node's children is that it gives us the ability to reason about dependencies between the icons that we're adding. In the example above, the color produced by the `hsl` function obviously depends on its hue value. That means the color shown by the color icon depends on the angle shown by the angle icon. If the user opens the angle editor through that icon and modifies the angle, we are now able to update the color icon's color in real time:
As you can see in the example above, we use this mechanism for other icon pairings as well, such as for `color-mix()` and its two color channels, or `var` functions that return a color from its fallback.
## Performance impact
When diving into this problem for improving reliability and fixing long standing issues, we were expecting some performance regression considering that we started running a fully fledged parser. For testing this out, we have created a benchmark that renders about 3.5k property declarations and profiled both the regex-based and parser-based versions with 6x throttling on an M1 machine.
As we expected, the parsing-based approach turned out to be 27% slower than the regex-based approach for that case. The regex-based approach took 11s to render and parser-based approach took 15s to render.
Considering the wins we get from the new approach, we decided to move forward with it.
## Acknowledgements
Our deepest gratitude goes out to Sofia Emelianova and Jecelyn Yeen for their invaluable help editing this post!
## Download the preview channels
Consider using the Chrome [Canary](https://www.google.com/chrome/canary/), [Dev](https://www.google.com/chrome/dev/), or [Beta](https://www.google.com/chrome/beta/) as your default development browser. These preview channels give you access to the latest DevTools features, let you test cutting-edge web platform APIs, and help you find issues on your site before your users do!
## Get in touch with the Chrome DevTools team
Use the following options to discuss the new features, updates, or anything else related to DevTools.
  * Submit feedback and feature requests to us at [crbug.com](https://crbug.com).
  * Report a DevTools issue using the more_vert **More options** > **Help** > **Report a DevTools issue** in DevTools.
  * Tweet at [@ChromeDevTools](https://twitter.com/intent/tweet?text=@ChromeDevTools).
  * Leave comments on [What's new in DevTools YouTube videos](https://goo.gle/devtools-youtube) or [DevTools Tips YouTube videos](https://goo.gle/devtools-tips).


Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-08-01 UTC.

