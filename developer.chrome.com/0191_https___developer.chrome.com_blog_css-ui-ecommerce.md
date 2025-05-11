---
url: https://developer.chrome.com/blog/css-ui-ecommerce-has?hl=en
title: https://developer.chrome.com/blog/css-ui-ecommerce-has?hl=en
date: 2025-05-11T16:54:51.651207
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/css-ui-ecommerce-has?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/css-ui-ecommerce-has?hl=es-419)




  * On this page
  * [Things to consider when using :has()](https://developer.chrome.com/blog/css-ui-ecommerce-has?hl=en#things_to_consider_when_using_has)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  :has() case studies 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Things to consider when using :has()](https://developer.chrome.com/blog/css-ui-ecommerce-has?hl=en#things_to_consider_when_using_has)


Swetha Gopalakrishnan 
[ LinkedIn ](https://www.linkedin.com/in/swetha-gopalakrishnan-5ba92936)
Saurabh Rajpal 
[ LinkedIn ](https://www.linkedin.com/in/imsaurabhrajpal)
CSS has notoriously lacked a way to directly select a parent element based on its children. This has been a top request by developers for many years. The `:has()` selector, now supported by all major browsers, solves this. Before `:has()`, you'd often chain long selectors or add classes for styling hooks. Now you can style based on an element's relationship with its descendants. Read more about the `:has()` selector in [CSS Wrapped 2023](https://developer.chrome.com/blog/css-wrapped-2023#has) and [5 CSS snippets every frontend developer should know](https://web.dev/articles/5-css-snippets-every-front-end-developer-should-know-in-2024).
Although this selector seems small, it can enable a huge number of use cases. This article shows some use cases that ecommerce companies unlocked with the `:has()` selector.
`:has()` is part of [Baseline Newly Available](https://web.dev/baseline).
Browser Support
  * 105 
  * 105 
  * 121 
  * 15.4 


[Source](https://developer.mozilla.org/docs/Web/CSS/:has)
Check out the [full series](https://developer.chrome.com/blog/css-ui-ecommerce) that this article is part of, which discusses how ecommerce companies enhanced their website using new CSS and UI features.
## Policybazaar
> With the `:has()` selector, we were able to eliminate JavaScript based validation of the user's selection and replace it with a CSS solution which is working seamlessly for us with the same experience as before.—[Aman Soni](https://www.linkedin.com/in/amansoni211/), Tech Lead, Policybazaar
Policybazaar's Investment team cleverly applied the `:has()` selector to provide a clear visual indication for users that are comparing plans. The following image shows two types of plans within the comparison UI (yellow and blue). Each plan can only be compared with its own type. By using `:has()`, when a user selects one type of plan the other plan type is unable to be selected.
Implementing `:has()` to style parent element and its children to create a category-bound selection functionality.
### Code
`:has()` gives you access to style parent elements and their children. The following code checks if a parent container has a `.disabled-group` class set. If it does, the card is greyed out, and the "Add" button is prevented from reacting to clicks by setting `pointer-events` to `none`.
```
.plan-group-container:has(.disabled-group){
opacity:0.5;
filter:grayscale(100%);
}
.plan-group-container:has(.disabled-section).button{
pointer-events:none;
border-color:#B5B5B5;
color:var(--text-primary-38-color);
background:var(--input-border-color);
}

```

The [health](https://health.policybazaar.com/) team at Policybazaar implemented a slightly different use case. They have an inline quiz for the user and use `:has()` to check the question checkbox status to see if the question was answered. If it was, an animation is applied to transition to the next question.
[health.policybazaar.com/](https://health.policybazaar.com/)
### Code
In the plan comparison example, `:has()` was used to check the presence of a class. You can also check the state of an input element such as a checkbox using `:has(input:checked)`. In the visual showing the quiz, each question in the purple banner is a checkbox. Policybazaar checks if the question has been answered using `:has(input:checked)` and if it has, trigger an animation using `animation: quesSlideOut 0.3s 0.3s linear forwards` to slide to the next question. See how this works in the following code.
```
.segment_banner__wrap__questions{
position:relative;
animation:quesSlideIn0.3slinearforwards;
}
.segment_banner__wrap__questions:has(input:checked){
animation:quesSlideOut0.3s0.3slinearforwards;
}

@keyframesquesSlideIn{
from{
transform:translateX(50px);
opacity:0;
}
to{
transform:translateX(0px);
opacity:1;
}
}
@keyframesquesSlideOut{
from{
transform:translateX(0px);
opacity:1;
}
to{
transform:translateX(-50px);
opacity:0;
}
}

```

## Tokopedia
Tokopedia used `:has()` to create an overlay image if the product thumbnail contains a video. If the product thumbnail contains a `.playIcon` class, a CSS overlay is added. Here, the :has() selector is used together with the `&` nesting selector within the overarching `.thumbnailWrapper` class which applies to all the thumbnails. This creates more modular and readable CSS.
Before and after using `:has()`.
### Code
The following code uses the [CSS selectors and combinators](https://developer.mozilla.org/docs/Web/CSS/CSS_selectors/Selectors_and_combinators#combinators) (`&` and `>`) and nesting with `:has()` to style the thumbnail. For non-supporting browsers, the regular additional CSS class rule is used as the fallback. The `@supports selector(:has(*))` rule is also used to check for browser support. Therefore, the overall experience is the same across the browser versions.
```
exportconstthumbnailWrapper=css`
 padding: 0;
 margin-right: 7px;
 border: none;
 outline: none;
 background: transparent;
 > div {
  width: 64px;
  height: 64px;
  overflow: hidden;
  cursor: pointer;
  border-color: ;
  position: relative;
  border: 2px solid ${NN0};
  border-radius: 8px;
  transition: border-color 0.25s;
  &.active {
   border-color: ${GN500};
  }
  @supports selector(:has(*)) {
   &:has(.playIcon) {
    &::after {
     content: '';
     display: block;
     background: rgba(0, 0, 0, 0.2);
     position: absolute;
     top: 0;
     left: 0;
     right: 0;
     bottom: 0;
    }
   }
  }
  & > .playIcon {
   position: absolute;
   top: 25%;
   left: 25%;
   width: 50%;
   height: 50%;
   text-align: center;
   z-index: 1;
  }
 }
`;

```

## Things to consider when using `:has()`
Combine `:has()` with other selectors to create a more complex condition. Check out some examples in [has() the family selector](https://developer.chrome.com/blog/has-m105#how-to-use-has).
## Resources:
  * [CSS Wrapped 2023](https://developer.chrome.com/blog/css-wrapped-2023#has)
  * [:has(): the family selector](https://developer.chrome.com/blog/has-m105)
  * Do you want to report a bug or request a new feature? [We want to hear from you](https://issues.chromium.org/issues/new?component=1456329&template=0)!


Explore the other articles in this series which talks about how ecommerce companies benefited from using new CSS and UI features such as Scroll-driven animations, view transitions, popover and container queries.
  * [Why do Web UI Capabilities matter for your ecommerce site?](https://developer.chrome.com/blog/css-ui-ecommerce)
  * [Scroll-driven animations case studies](https://developer.chrome.com/blog/css-ui-ecommerce-sda)
  * [View Transitions case studies](https://developer.chrome.com/blog/css-ui-ecommerce-vt)
  * [Popover case studies](https://developer.chrome.com/blog/css-ui-ecommerce-popover)
  * [Container queries case studies](https://developer.chrome.com/blog/css-ui-ecommerce-cq)


Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-05-07 UTC.

