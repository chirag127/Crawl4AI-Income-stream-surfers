---
url: https://developer.chrome.com/blog/advanced-attr?hl=en
title: https://developer.chrome.com/blog/advanced-attr?hl=en
date: 2025-05-11T16:53:35.054491
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/advanced-attr?hl=en#main-content)
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


#  CSS attr() gets an upgrade 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Bramus 
[ GitHub ](https://github.com/bramus) [ Mastodon ](https://front-end.social/@bramus) [ Bluesky ](https://bsky.app/profile/bram.us) [ Homepage ](https://www.bram.us/)
Published: Jan 15, 2025 
## The redesigned `attr()` function
With CSS `attr()` you can use the value of an HTML attribute in your CSS. Until now `attr()` only worked within the `content` property of pseudo-elements and could only parse values into a CSS `<string>`.
[The redesigned `attr()` function](https://drafts.csswg.org/css-values-5/#attr-notation), available from Chrome 133, unlocks more capabilities. You can now use `attr()` with _any_ CSS property—including custom properties—and it can parse values into data types other than `<string>`.
## Examples
In the following example the value of the `color` property for `div` uses the value from the `data-color` attribute. This attribute value is parsed into a `<color>` using `attr()` and `type()`. The fallback value is set to `red`.
```
<div data-foo="blue">test</div>

```
```
div{
color:attr(data-footype(<color>),red);
}

```

In the next example the `view-transition-name` property is determined by the `id` attribute of the element. The attribute gets parsed into a `<custom-ident>` which is the required type for `view-transition-name`. Without `attr()` you had to declare a `view-transition-name` for each card, whereas now you can do it it one go.
```
<div class="cards">
 <div class="card" id="card-1"></div>
 <div class="card" id="card-2"></div>
 <div class="card" id="card-3"></div>
 <div class="card" id="card-4"></div>
</div>

```
```
.card{
view-transition-name:attr(idtype(<custom-ident>),none);/* card-1, card-2, card-3, etc. */
view-transition-class:card;
}

```

You can also parse values into a length by setting the type to any identifier that matches a CSS dimension unit or the `%` character. In the following example the `data-size` attribute gets parsed into a pixel value.
```
<div data-size="10">test</div>

```
```
div{
font-size:attr(data-sizepx);
}

```

When using `attr()` without any type it parses the attribute to a CSS string, which is the same as the previous behavior.
## Learn More
Find more information about `attr()` in [the specification](https://drafts.csswg.org/css-values-5/#attr-notation) and on [MDN](https://developer.mozilla.org/docs/Web/CSS/attr).
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-01-15 UTC.

