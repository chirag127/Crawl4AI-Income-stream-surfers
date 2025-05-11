---
url: https://developer.chrome.com/blog/css-ui-ecommerce-popover?hl=en
title: https://developer.chrome.com/blog/css-ui-ecommerce-popover?hl=en
date: 2025-05-11T16:54:58.388907
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/css-ui-ecommerce-popover?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/css-ui-ecommerce-popover?hl=es-419)




  * On this page
  * [Things to consider when using the Popover API](https://developer.chrome.com/blog/css-ui-ecommerce-popover?hl=en#things_to_consider_when_using_the_popover_api)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  Popover case studies 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Things to consider when using the Popover API](https://developer.chrome.com/blog/css-ui-ecommerce-popover?hl=en#things_to_consider_when_using_the_popover_api)


Swetha Gopalakrishnan 
[ LinkedIn ](https://www.linkedin.com/in/swetha-gopalakrishnan-5ba92936)
Saurabh Rajpal 
[ LinkedIn ](https://www.linkedin.com/in/imsaurabhrajpal)
Popovers are everywhere on the web. You can see them in menus, toggletips, and dialogs, used for features such as account settings, disclosure widgets, and product card previews. Despite how prevalent these components are, building them in browsers is still surprisingly cumbersome. To resolve this, a new set of declarative HTML APIs for building popovers are coming to browsers, the first of these being the [Popover API](https://developer.mozilla.org/docs/Web/API/Popover_API).
Popover is part of [Baseline Newly Available](https://web.dev/baseline).
Browser Support
  * 114 
  * 114 
  * 125 
  * 17 


[Source](https://developer.mozilla.org/docs/Web/API/HTMLButtonElement/popoverTargetAction)
A popover is commonly confused with a dialog. However there are some key differences in their behavior. A `dialog` element opened with `dialog.showModal` (a modal dialog), is an experience which requires explicit user interaction to close the modal. A `popover` supports light-dismiss. A modal `dialog` does not. A modal dialog makes the rest of the page inert. A `popover` does not. [Read more about the differences](https://hidde.blog/dialog-modal-popover-differences/).
This article is [is part of a series](https://developer.chrome.com/blog/css-ui-ecommerce) which discusses how ecommerce companies enhanced their website using new CSS and UI features. In this article, discover how Tokopedia implemented and benefited from the Popover API.
## Tokopedia
> Using popover attributes reduced up to 70% lines of code in React. The modal can be natively controlled by HTML instead of requiring event handling in JavaScript and using `React.createPortal` for moving the modal DOM to the end of `document.body`. We are also able to use `@starting-style` to animate the opening and closing of the popover.—[Andy Wihalim](https://www.linkedin.com/in/andy-wihalim-a4872512b), Senior Software Engineer, Tokopedia.
Tokopedia's Product Detail Pages (PDP) contain multiple product images for each product. When the product thumbnail is clicked, a modal is opened to show the enlarged image. This is a common pattern used in ecommerce websites.
### Code
Tokopedia uses React for their frontend development. Before implementing the popover API for this modal, they used a DOM modal and a button. The button changed the React state to open the modal. With the popover API, they specify a `popovertarget` attribute in the element which opens the popover with a value that is the same as the ID of the popover element.
With this basic implementation, the popover works but appears and disappears without any animation. To create a smooth entry and exit animation for the popover, use `:popover-open` and `@starting-style` and allow animation of discrete properties. In the following code example, the popover scales in and out using the `transform: 'scale()'`property.
This [code example](https://codepen.io/web-dot-dev/pen/OJBoLNb) shows how to implement entry and exit animations for the popover API.
```
<Thumbnail popovertarget="medialightbox" />
<MediaLightbox popover id="medialightbox" />

```
```
exportconstcssModalWrapper=css({
background:NN0,
border:'none',
borderRadius:'.625rem',
width:1024,
padding:24,
'&::backdrop':{
opacity:0,
transitionProperty:'opacity, display',
transition:'.25s ease-out',
transitionBehavior:'allow-discrete',
},
transitionProperty:'transform, opacity, display',
transition:'.25s ease-out',
transitionBehavior:'allow-discrete',
transform:'scale(0.8)',
opacity:0,
'@starting-style':{
transform:'scale(1)',
opacity:1,
},
'&:popover-open':{
transform:'scale(1)',
opacity:1,
'@starting-style':{
transform:'scale(0.8)',
opacity:0,
},
},
});

```

To cater to browsers that don't support the popover API, Tokopedia implemented the [popover-polyfill](https://github.com/oddbird/popover-polyfill) by oddbird, which is only 3.2 KB with gzip compression. They were satisfied with the polyfill as it worked well and did not cause performance regressions. Overall, they were able to reduce up to 70% lines of code in React with the popover API.
## Things to consider when using the Popover API
Tokopedia uses React, and the team achieved code splitting by unmounting the popover component for pages which don't use it, then doing a code split for the popover content. This way, they reduced the size of their initial request.
Consider combining popovers with CSS anchor positioning ([coming soon to Chrome](https://chromestatus.com/feature/5124922471874560)) to position them relative to other elements. This is helpful for menus and tooltips for example.
## Resources
  * [Introducing the popover API](https://developer.chrome.com/blog/introducing-popover-api)
  * [The difference between a popover and a dialog](https://developer.chrome.com/blog/introducing-popover-api#the_difference_between_a_popover_and_a_dialog)
  * Do you want to report a bug or request a new feature? [We want to hear from you](https://issues.chromium.org/issues/new?component=1456565&template=0).


Explore the other articles in this series that talk about how ecommerce companies benefited from using new CSS and UI features such as Scroll-driven animations, popover, container queries and the `has()` selector.
  * [Why do Web UI Capabilities matter for your ecommerce site?](https://developer.chrome.com/blog/css-ui-ecommerce)
  * [Scroll-driven animations case studies](https://developer.chrome.com/blog/css-ui-ecommerce-sda)
  * [View Transitions case studies](https://developer.chrome.com/blog/css-ui-ecommerce-vt)
  * [Container Queries case studies](https://developer.chrome.com/blog/css-ui-ecommerce-cq)
  * [:has() selector case studies](https://developer.chrome.com/blog/css-ui-ecommerce-has)


Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-04-24 UTC.

