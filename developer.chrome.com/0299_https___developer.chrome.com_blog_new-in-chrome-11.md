---
url: https://developer.chrome.com/blog/new-in-chrome-111?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-111?hl=en
date: 2025-05-11T16:57:06.087264
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-111?hl=en#main-content)
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


#  New in Chrome 111 
Stay organized with collections  Save and categorize content based on your preferences. 
Adriana Jara 
[ GitHub ](https://github.com/tropicadri) [ LinkedIn ](https://www.linkedin.com/in/adrianajara) [ Mastodon ](https://hachyderm.io/@tropicadri)
Here's what you need to know:
  * Create polished transitions in your single page app with the [View Transitions API](https://developer.chrome.com/blog/new-in-chrome-111?hl=en#view-transitions-api).
  * Bring colors to the next level with support for [CSS Color Level 4](https://developer.chrome.com/blog/new-in-chrome-111?hl=en#css-color-level4).
  * Discover [new tools](https://developer.chrome.com/blog/new-in-chrome-111?hl=en#devtools-color) in the style panel to make the most of new color functionality.
  * And there’s plenty [more](https://developer.chrome.com/blog/new-in-chrome-111?hl=en#more).


I’m Adriana Jara. Let’s dive in and see what’s new for developers in Chrome 111.
## View Transitions API.
Creating smooth transitions on the web is a complex task. The View Transitions API is here to make the creation of polished transitions simpler by snapshotting views and allowing the DOM to change without any overlap between states.
Transitions created with the View Transition API. [Try the demo site](https://http203-playlist.netlify.app/)–Requires Chrome 111+.
The default view transition is a cross fade, the following snippet implements this experience.
```
functionspaNavigate(data){
// Fallback for browsers that don't support this API:
if(!document.startViewTransition){
updateTheDOMSomehow(data);
return;
}
// With a transition:
document.startViewTransition(()=>updateTheDOMSomehow(data));
}

```

When `.startViewTransition()` is called, the API captures the current state of the page.
Once that's complete, the `callback` passed to `.startViewTransition()` is called. That's where the DOM is changed. Then, the API captures the new state of the page.
Note that the API is launched for Single-Page Apps (SPAs) but support for other models is being implemented too.
There are many details to this API, learn more [in our article containing samples and details](https://developer.chrome.com/docs/web-platform/view-transitions), or explore the [View Transitions documentation on MDN](https://developer.mozilla.org/docs/Web/API/View_Transitions_API).
## CSS Color Level 4.
With CSS color level 4, CSS now supports high definition displays, specifying colors from HD gamuts while also offering color spaces with specializations.
In a nutshell it means 50% more colors to pick from! You thought 16 million colors sounded like a lot. I thought so too.
A series of images are shown transitioning between wide and narrow color gamuts, illustrating color vividness and its effects. [Try it for yourself](https://ciechanow.ski/color-spaces/#:~:text=you%20can%20drag%20the%20slider%20to%20see%20how%20the%20extent%20of%20the%20chromaticity%20triangle%20corresponds%20to%20the%20representable%20colors.)
The implementation includes the [`color()`](https://developer.mozilla.org/docs/Web/CSS/color_value/color) function; it can be used for any color space that specifies colors with R, G, and B channels. `color()` takes a color space parameter first, then a series of channel values for RGB and optionally some alpha.
Here are some examples of using the color function with different color spaces.
```
.valid-css-color-function-colors{
--srgb:color(srgb111);
--srgb-linear:color(srgb-linear100%100%100%/50%);
--display-p3:color(display-p3111);
--rec2020:color(rec2020000);
--a98-rgb:color(a98-rgb111/25%);
--prophoto:color(prophoto-rgb0%0%0%);
--xyz:color(xyz111);
}

```

Checkout [this article](https://developer.chrome.com/docs/css-ui/high-definition-css-color-guide) for more documentation to take full advantage of high definition colors using CSS.
## New color devtools.
Devtools has new features to support the css color level 4 specification.
The **Styles** pane now supports the 12 new color spaces and 7 new gamuts outlined in the spec. Here are examples of CSS color definitions with color(), lch(), oklab() and color-mix().
When using `color-mix()`, which enables mixing a percentage of one color into another, you can view the final color output in the **Computed** pane 
Also the color picker supports all the new color spaces with more features. For example, click on the color swatch of color(display-p3 1 0 1). A gamut boundary line has also been added, distinguishing between the sRGB and display-p3 gamuts for a clearer understanding of your selected color's gamut. 
The color picker also supports converting colors between color formats.
Checkout [this post](https://developer.chrome.com/blog/new-in-devtools-111) for more information on debugging color and other new features in devtools.
## And more!
Of course there’s plenty more.
  * CSS added trigonometric functions, additional root font units and [extended the n-th child](https://developer.chrome.com/articles/css-nth-child-of-s) pseudo selector.
  * The [Document Picture in Picture API](https://developer.chrome.com/docs/web-platform/document-picture-in-picture) is in origin trial
  * `previousslide` and `nextslide` actions are now part of the [Media Session API](https://web.dev/media-session). Checkout the demo [here](https://googlechrome.github.io/samples/media-session/slides.html).


## Further reading
This covers only some key highlights. Check the links below for additional changes in Chrome 111.
  * [What's new in Chrome DevTools (111)](https://developer.chrome.com/blog/new-in-devtools-111)
  * [Chrome 111 deprecations and removals](https://developer.chrome.com/blog/deps-rems-111)
  * [ChromeStatus.com updates for Chrome 111](https://www.chromestatus.com/features#milestone%3D111)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/110.0.5481.186..111.0.5563.53)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
I’m Adriana Jara, and as soon as Chrome 112 is released, I'll be right here to tell you what's new in Chrome!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2023-03-07 UTC.

