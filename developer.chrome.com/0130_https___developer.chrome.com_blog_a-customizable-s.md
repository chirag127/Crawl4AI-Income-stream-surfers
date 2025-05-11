---
url: https://developer.chrome.com/blog/a-customizable-select?hl=en
title: https://developer.chrome.com/blog/a-customizable-select?hl=en
date: 2025-05-11T16:53:33.449322
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/a-customizable-select?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/a-customizable-select?hl=es-419)




  * On this page
  * [Meet appearance: base-select](https://developer.chrome.com/blog/a-customizable-select?hl=en#meet_appearance_base-select)
    * [A <select> can now include rich HTML content](https://developer.chrome.com/blog/a-customizable-select?hl=en#a_select_can_now_include_rich_html_content)
    * [Completely customizable](https://developer.chrome.com/blog/a-customizable-select?hl=en#completely_customizable)
    * [Unchanged JavaScript interfaces](https://developer.chrome.com/blog/a-customizable-select?hl=en#unchanged_javascript_interfaces)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  The <select> element can now be customized with CSS 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Meet appearance: base-select](https://developer.chrome.com/blog/a-customizable-select?hl=en#meet_appearance_base-select)
    * [A <select> can now include rich HTML content](https://developer.chrome.com/blog/a-customizable-select?hl=en#a_select_can_now_include_rich_html_content)
    * [Completely customizable](https://developer.chrome.com/blog/a-customizable-select?hl=en#completely_customizable)
    * [Unchanged JavaScript interfaces](https://developer.chrome.com/blog/a-customizable-select?hl=en#unchanged_javascript_interfaces)


Adam Argyle 
[ GitHub ](https://github.com/argyleink) [ Glitch ](https://glitch.com/@argyleink) [ Homepage ](https://nerdy.dev)
Published: March 24, 2025 
From Chrome 135, web developers and designers can finally unite on an accessible, standardized and CSS styleable `<select>` element on the web. This has been many years in the making, many hours of engineering and collaborative specification work, and the result is an incredibly rich and powerful component that won't break in older browsers.
Here's a video of customized selects using these new features:
Featuring demos by [Una](https://codepen.io/una/full/MWMmYxb), [Brecht](https://codepen.io/utilitybend/full/ZEPBGGR), and [Adam](https://cdpn.io/pen/debug/wvYrZEV).
If you've been following along closely, you'll notice a few spec names and features have changed since [Una](https://una.im/)'s [request for community feedback](https://developer.chrome.com/blog/rfc-customizable-select). Luckily, if you worked from that post and are interested in [what's changed, Una's also got you covered](https://una.im/select-updates/).
There's also shiny new [documentation on MDN for customizable select](https://developer.mozilla.org/docs/Learn_web_development/Extensions/Forms/Customizable_select), packed with details.
## Meet `appearance: base-select`
A new CSS property `appearance: base-select` that puts the `<select>` element into a new, configurable and styleable state to be commonly referred to as "base" styles:
```
.custom-select{
&,&::picker(select){
appearance:base-select;
}
}

```

Using `base-select` **unlocks** a number of new features and behaviors:
  * [Changes the browsers HTML parser](https://open-ui.org/components/customizableselect/#html-parser-changes) for the contents inside the `<select>`.
  * Changes the [rendered internals](https://open-ui.org/components/customizableselect/#anatomy-of-the-customizable-select-element) of the `<select>`.
  * Exposes new internal parts and states for the `<select>`.
  * A new minimal look, optimized for customization.
  * Shown [options](https://developer.mozilla.org/docs/Web/HTML/Element/option) are in the top-layer, like a popover.
  * Shown options positioned with [`anchor()`](https://developer.mozilla.org/docs/Web/CSS/anchor).


Using `base-select` **loses** a number of features and behaviors:
  * The `<select>` doesn't render outside the browser pane.
  * It doesn't trigger built-in mobile operating system components.
  * The `<select>` stops taking the width of the longest [`<option>`](https://developer.mozilla.org/docs/Web/HTML/Element/option).


### A `<select>` can now include rich HTML content
Before you could customize a `<select>`, if you put things like an image or SVG into the `<option>` element, the browser would ignore them.
Consider the following HTML, the browser would read it as you authored it:
```
<select class="custom-select">
 <option>
  <svg aria-hidden>…</svg>
  <span>HTML</span>
 </option>
 <option>
  <svg aria-hidden>…</svg>
  <span>CSS</span>
 </option>
 <option>
  <svg aria-hidden>…</svg>
  <span>JavaScript</span>
 </option>
 <option>
  <svg aria-hidden>…</svg>
  <span>WASM</span>
 </option>
</select>

```

However the used DOM wouldn't include the `<svg>`:
```
<select class="custom-select">
 <option>
  <span>HTML</span>
 </option>
 <option>
  <span>CSS</span>
 </option>
 <option>
  <span>JavaScript</span>
 </option>
 <option>
  <span>WASM</span>
 </option>
</select>

```

Here's (from left to right) Chrome, Safari, and Firefox rendering the preceding HTML. If the browser supports `appearance: base-select` then the SVG will appear in the option, otherwise it won't.
[Try it in this Codepen](https://codepen.io/web-dot-dev/pen/zxYaXzZ).
There's risk in breaking existing websites with customizable select, due to the parser changes. Chrome has the features behind a [Finch experiment](https://developer.chrome.com/docs/web-platform/chrome-finch) in case there is an emergency need to turn it off. If things go well, the experiment will end and the code will be shipped permanently into the source.
### Completely customizable
[Every part of a `base-select`](https://una.im/select-updates/) can be swapped out, customized and animated. Here's a demo that uses every new feature to create recognizable and meaningful select experiences.
[Try it in this Codepen](https://codepen.io/web-dot-dev/pen/gbOKyRZ).
Find many more examples in the resources section at the end of this post.
### Unchanged JavaScript interfaces
There's no risks to your existing JavaScript interactions with a `<select>` element.
However, if you do begin adding rich HTML into your [`<option>`](https://developer.mozilla.org/docs/Web/HTML/Element/option) elements, you should test the selected values, as the browser does still parse and ignore images and SVG. The logic has changed though, for determining the selected content string, and depending on what you have in your options, you may need to make adjustments.
If you're using the `value` attribute on an `<option>` you have nothing to worry about.
## Resources
Chrome is first to implement `base-select`, but every browser participated in the specifications, and there's more "base" elements yet to be completed. This is just a start.
Stay tuned as we'll be continuing to add guidance, examples and resources on customizing select elements. Until then, checkout the following links for more information.
  * Web Standards 
    * [HTML spec pull request](https://github.com/whatwg/html/issues/9799)
  * Chrome 
    * [Request for Comments and awesome Una explainer](https://developer.chrome.com/blog/rfc-customizable-select)
    * [Request for Comments Results](https://developer.chrome.com/blog/rfc-customizable-select-findings)
    * [Use `<hr>` in a `<select>`](https://developer.chrome.com/blog/hr-in-select)
    * [Una explaining parts and pieces](https://una.im/select-updates/)
    * [Una Codepen collection](https://codepen.io/collection/BNZjPe)
  * Community 
    * [Brecht De Ruyte Codepen Collection](https://codepen.io/collection/qOGape)
    * [CSS Tricks on native versus custom selects](https://css-tricks.com/striking-a-balance-between-native-and-custom-select-elements/)
    * [Open Props UI-`<select>`](https://open-props-ui.netlify.app/components/inputs/select.html)
    * [Custom select with transition animations example](https://codepen.io/argyleink/pen/QWXexXK)


**Special thanks to all those who were involved in making this happen!**
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-03-24 UTC.

