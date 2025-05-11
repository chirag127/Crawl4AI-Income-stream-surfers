---
url: https://developer.chrome.com/blog/carousels-with-css?hl=en
title: https://developer.chrome.com/blog/carousels-with-css?hl=en
date: 2025-05-11T16:54:05.827532
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/carousels-with-css?hl=en#main-content)
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


#  Carousels with CSS 
Stay organized with collections  Save and categorize content based on your preferences. 
Adam Argyle 
[ GitHub ](https://github.com/argyleink) [ Glitch ](https://glitch.com/@argyleink) [ Homepage ](https://nerdy.dev)
Published: March 20, 2025 
From Chrome 135, you can use features from the [CSS Overflow 5 specification](https://drafts.csswg.org/css-overflow-5/) that have been designed to create scroll and carousel experiences.
This post is an overview of [many different scroll and carousel experiences](https://chrome.dev/carousel/) made using these new features, and without JavaScript. Watch the following video and get excited for what can now be achieved.
Shown in the video is a harmony of scroll buttons, scroll markers, scroll driven animation, scroll-state() queries, :has(), grid, anchor and so much more.
Even more impressive is the accessibility story. 
Carousel best practices are handled by the browser, thanks to the engineering and accessibility teams working together. It'd be very difficult to make a more accessible carousel than this.
Screenshot of Chrome DevTools carousel [accessibility tree](https://developer.chrome.com/blog/full-accessibility-tree)— [Demo](https://codepen.io/web-dot-dev/pen/azbYEGR)
## Meet `::scroll-button()` and `::scroll-marker()`
A carousel is a scroll area with up to two added UI affordances—buttons and markers.
In version one of CSS carousel features, the buttons and markers are created from CSS. The browser places the elements as siblings, with the proper roles, in the proper tab order, and maintains their state. This makes developing an accessible carousel easier.
  * [Scroll Buttons](https://developer.chrome.com/blog/carousels-with-css?hl=en#add_scroll_buttons_with_scroll-button) Browser provided, stateful, and interactive scroll affordance `<button>` elements that aids in content access and scroll 85% of a scroll area when pressed.
  * [Scroll Markers](https://developer.chrome.com/blog/carousels-with-css?hl=en#add_scroll_markers_with_scroll-marker) Browser provided, stateful navigation `<a>` elements that aid in content access for any requested item in the scroll area.


The rest of this post demonstrates how to build up a carousel using these new features.
### Start with a scroller
You can add buttons and markers to any scroll area on your site.
The following CSS creates a basic scroll area for use in later steps to add buttons and markers to. Scroll snapping is not required for a carousel, but in this example it is used. Carousels also work for vertical scrollers and bidirectional scrollers.
```
.carousel{
overflow-x:auto;
scroll-snap-type:xmandatory;
li{
scroll-snap-align:center;
}
}

```
A scroll area shown with no affordances or clues other than content being cut off. 
### Add scroll buttons with `::scroll-button()`
Depending on your operating system, there may already be scroll buttons around your scrollbars. Built in scrollbar buttons tend to nudge a scroll area, while [CSS scroll buttons](https://flackr.github.io/carousel/#scroll-buttons) page 85% of the scroll area.
Browser Support
  * 135 
  * 135 


[Source](https://developer.mozilla.org/docs/Web/CSS/::scroll-button)
For carousels that only show one full width item at a time with [scroll snap points](https://developer.mozilla.org/docs/Web/CSS/CSS_scroll_snap), this will feel like an item by item amount. For long lists of items where more than one are in view at a time, it scrolls almost a full page.
To add scroll buttons with CSS:
  1. Add them like other pseudo-elements, with a selector: `.carousel::scroll-button(right)` for a button to scroll right.
  2. Specify `content` with optional [accessible fallback alt text](https://developer.chrome.com/blog/chrome-127-beta#multi-argument_alt_text_in_css_generated_content).


The browser will create real buttons, with your content inside, as siblings to the scroller. You're now free to lay these buttons out, style them or [`anchor()`](https://developer.chrome.com/docs/css-ui/anchor-positioning-api) them as you need. This following CSS creates two, one for a scroll left button and one for a scroll right button.
```
.carousel{
…
&::scroll-button(left){
content:"⬅"/"Scroll Left";
}
&::scroll-button(right){
content:"⮕"/"Scroll Right";
}
&::scroll-button(*):focus-visible{
outline-offset:5px;
}
}

```

### Add scroll markers with `::scroll-marker()`
Similar to the scrollbar thumb element, [CSS scroll markers](https://flackr.github.io/carousel/#scroll-markers) can hint to the size of the carousel while also providing the affordance to move quickly to the end or beginning. A CSS scroll marker is different from the scrollbar because each marker is a link that can represent **any item in the scroller**.
Browser Support
  * 135 
  * 135 


[Source](https://developer.mozilla.org/docs/Web/CSS/::scroll-marker)
An example of this distinction, consider the seasons of a TV series. Instead of making a marker for each of the 10 episodes, create 2 markers that go to the beginning of the chapter.
Notice these markers aren't dots, they're using the `content: "Season 1"` property of their pseudo-element. Markers can also be thumbnails, commonly used for gallery carousels in e-commerce or photo focused websites.
Markers are like in-page `<a>` links, but do have some special features:
  1. They include a `:target-current` state for when the marker is in view or snapped.
  2. Keyboard navigation is included, and behaves like a [focusgroup](https://open-ui.org/components/focusgroup.explainer/).
  3. Screen reader experience is included, and reports like a tablist.


Add markers to meaningful points of interest in your scroller with the following steps:
  1. Define placement of the `scroll-marker-group` as `before` or `after`.
  2. Select the points of interest with a selector `.carousel .point-of-interest::scroll-marker`.
  3. Specify `content` with optional [accessible fallback alt text](https://developer.chrome.com/blog/chrome-127-beta#multi-argument_alt_text_in_css_generated_content); numbers, text, empty, or an image.


The browser creates all the markers and puts them into the marker group container. This example makes an empty marker for each `<li>`, to create a marker dot for each item.
```
.carousel{
…
scroll-marker-group:after;
li::scroll-marker{
content:' ';
}
li::scroll-marker:target-current{
background:var(--accent);
}
}

```

The containing element of the markers is called a `::scroll-marker-group` and it is created as a sibling of the scroller, just like the scroll buttons. This container can be styled and placed wherever you need.
### Markers and buttons at the same time
Put the two together and experience looks like a carousel but have the following benefits:
  * Works with JavaScript disabled.
  * No hydration or lazy sizing (reduce CLS).
  * Ready for all kinds of scroll animation and triggers.
  * Accessibility is included.
  * Touch, mouse, and keyboard friendly.


**Do less, reach more, faster.**
## Resources
This post mostly refers to these features as "carousel," but their capabilities and usefulness extend far beyond carousel use cases. For a full picture of the potential of these new features, try the Carousel Gallery and see other components like: scrollspy, tabs, and slides.
  * Web Standards 
    * [Carousel Explainer](https://flackr.github.io/carousel/)
  * Chrome 
    * [Carousel Gallery](https://chrome.dev/carousel/)
    * [Carousel Configurator](https://chrome.dev/carousel-configurator/)


### Carousel Configurator
For visual and interactive learners, try the [Carousel Configurator](https://chrome.dev/carousel-configurator/).
It offers switches, for say scroll buttons, and when enabled the shown carousel immediately has buttons appear plus the associated CSS used.
<https://chrome.dev/carousel-configurator/>
It also includes examples of more advanced concepts that are carousel adjacent:
  * [scroll driven animation](https://developer.chrome.com/docs/css-ui/scroll-driven-animations)
  * and [scroll snap columns](https://flackr.github.io/carousel/fragmentation/)


### Carousel Gallery
A **showcase space** for those curious about how far you can take these features, answering questions like "can it do X?". Each demo is based on a use case found around the internet. Each demo shows how to orchestrate these buttons and markers with [scroll driven animation](https://developer.chrome.com/docs/css-ui/scroll-driven-animations), [scroll-state()](https://developer.chrome.com/blog/css-scroll-state-queries) queries, and much more.
Fun fact, the entire site is JavaScriptless.
<https://chrome.dev/carousel/>
The examples range from delightfully simple to fantastically robust and feature rich. Browsing the gallery should be inspirational, reassuring, and of course be inspectable for code to take. Find and inspect `@layer utilities` for utilities that can help you make carousels.
## Further work
We're proud of how well these features integrate with all of HTML and CSS. The accessibility of a CSS carousel is top-notch. The performance of a CSS carousel is better than any JavaScript solution. The user experience of a CSS carousel is natural, smooth and rich. However, there are ways to improve.
### Bring your own elements
Work is already being done to let you add your own components for scroll buttons and markers. This means you could supply your own `<a>` tags that have rich content like icons. You could also bring your own multi-layered buttons built with [Tailwind](https://tailwindcss.com/).
### Cyclical scrolling
Many carousels wrap around on themselves when they get to the end, like a carousel ride at a fair may have. This is on our radar and we intend to provide a platform solution for it.
We hope you enjoy this feature. We look forward to all the "JavaScript disabled" web users who will get a nice scrollable experience now and all the CLS reductions to be gained from the better timed lifecycle of a built-in carousel.
**Less for you to do, great user experiences, better performance.**
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-03-20 UTC.

