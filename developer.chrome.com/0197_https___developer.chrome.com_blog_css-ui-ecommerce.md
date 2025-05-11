---
url: https://developer.chrome.com/blog/css-ui-ecommerce-cq?hl=en
title: https://developer.chrome.com/blog/css-ui-ecommerce-cq?hl=en
date: 2025-05-11T16:54:58.386036
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/css-ui-ecommerce-cq?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/css-ui-ecommerce-cq?hl=es-419)




  * On this page
  * [Things to consider when using container queries](https://developer.chrome.com/blog/css-ui-ecommerce-cq?hl=en#things_to_consider_when_using_container_queries)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  Container queries case studies 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Things to consider when using container queries](https://developer.chrome.com/blog/css-ui-ecommerce-cq?hl=en#things_to_consider_when_using_container_queries)


Swetha Gopalakrishnan 
[ LinkedIn ](https://www.linkedin.com/in/swetha-gopalakrishnan-5ba92936)
Saurabh Rajpal 
[ LinkedIn ](https://www.linkedin.com/in/imsaurabhrajpal)
[Container queries](https://developer.mozilla.org/docs/Web/CSS/CSS_containment/Container_queries) offer a highly dynamic and flexible approach to responsive design. Container queries use the `@container` at-rule. This works in a similar way to a media query with `@media`, but instead, `@container` queries a parent container for styling information rather than the viewport and user agent.
Container queries are part of [Baseline Newly Available](https://web.dev/baseline).
Browser Support
  * 105 
  * 105 
  * 110 
  * 16 


[Source](https://developer.mozilla.org/docs/Web/CSS/@container)
By responding to the container size, container queries allow components to adapt to their location in an interface. For example, a card component can adapt its size and styles according to the container it's placed in, be it a sidebar, hero section, or a grid within the main body of a page.
As shown in the following illustration, you can combine media queries for macro layouts, container queries for micro layouts, with user-preference based media queries to create a powerful responsive design system. Read [more about container queries](https://web.dev/blog/cq-stable) and the [new responsive design](https://web.dev/articles/new-responsive#conclusion).
[web.dev—The New Responsive.](https://web.dev/articles/new-responsive#conclusion)
This article [is part of a series](https://developer.chrome.com/blog/css-ui-ecommerce) discussing how ecommerce companies enhanced their websites using new CSS and UI features. This time, we dive into how some companies used and benefited from container queries.
## redBus
redBus maintains and serves different code for its mobile and desktop versions. After implementing container queries on their [Things-to-do](https://www.redbus.my/things-to-do/) and [cargo](https://www.redbus.pe/cargo) pages, they were able to unify this code into a single codebase for these sites. This made them responsive and saved development time. The following example demonstrates this using the cargo page:
### Code
In the following example, `.bpdpCardWrapper` is the parent container, named as `bpdpSection`.
If the container `bpdpSection` has a minimum width of 744px, the `font-size` and `line-height` for the components selected by `.bpdpCardContainer` and `.subTxt, .bpdpAddress` is updated.
```
//CodeforContainerQueries
.bpdpCardWrapper{
container-type:inline-size;
container-name:bpdpSection;
}
@containerbpdpSection(min-width:744px){
.bpdpCardContainer{
font-size:1rem;
line-height:1.5rem;
}
.subTxt,.bpdpAddress{
font-size:0.875rem;
line-height:1.25rem;
}
}

```

### Impact
**Before**(multiple code base) | **After**(single code base)  
---|---  
Infrastructure | Separate infrastructure (high cost). | Same infrastructure (reduced cost).  
Design | Separate UI but poor consistency. | Challenging to solve but possible.  
Performance | Easy to handle as the system is separate but duplicates effort of improving performance. | This is page and feature specific but redBus [PageSpeedInsights](https://pagespeed.web.dev/) score is above 80.  
Development | Separate developer teams. | 30% - 40% reduction in time.  
## Tokopedia
Tokopedia's Product Detail Pages (PDP) contain multiple tabs for the shop and product information. Previously, the layout of this page was divided into three columns and sometimes the product name on the left was cut off for smaller screen sizes (see the following "Before" video).
To solve this layout problem, they easily and quickly adopted container queries. After this implementation, they were able to have a flexible layout where the product name was always fully visible (see the following "After" video).
### Before
Before implementing container queries, the words "ISKU 10 in 1 Obeng satu.." on the top left are cut off for smaller screen sizes.
### After
Implementing container queries adjusts the layout keeping the text within the viewport.
### Code
The following code queries the size of the parent container named `infowrapper`. If the maximum width of the `infowrapper` is 360px, the child components' `width`, `margin,` and `padding` are adjusted.
Setting the `container-type` to `inline-size` queries the inline-direction size of the parent. In latin languages like English, this would be the width of the parent container, since the text flows inline from left to right.
```
exportconststyCredibilityContainer=css`
 container-name: infowrapper;
 container-type: inline-size;
`;
exportconststyBtnShopFollow=css`
 margin-left: auto;
 width: 98px;
 @container infowrapper (max-width: 360px) {
  width: 100%;
  margin-top: 2px;
  margin-bottom: 8px;
  padding-left: 60px;
 }
`;
exportconststyBottomRow=css`
 margin-top: 4px;
 padding-left: 60px;
 display: flex;
 align-items: center;
 @container infowrapper (max-width: 360px) {
  padding-left: 0px;
 }
 > div {
  text-align: left;
  margin-top: 0 !important;
 }
`;

```

## Things to consider when using container queries
Tokopedia found their use case by looking out for text ellipsis on their site. This indicated containers that might be too small, causing the content to be cut off for the user.
Another good use case for container queries for ecommerce sites is to look out for reused components. For example, the **Add to cart** button might be shown differently based on the parent container (for example, only the icon if it's in the product card and icon with text if it's a primary CTA on the page). The button could be a good candidate for container queries.
You can choose to do incremental improvements to your site. For example, you could start with smaller use cases like the ellipse example from Tokopedia, and implement container queries there. Then, progressively find more cases and improve the CSS.
## Resources:
  * [Container queries land in stable browsers](https://web.dev/blog/cq-stable)
  * [Container queries-Designing in the Browser](https://web.dev/shows/designing-in-the-browser/gCNMyYr7F6w/)
  * [Container query demos](https://codepen.io/collection/rxLQrE?cursor=eyJwYWdlIjoxfQ==)
  * [Demo: container query cards](https://web.dev/patterns/layout/container-query-card)
  * [Video: What's new in Web UI - I/O 2023](https://youtu.be/buChHSdsF9A?si=isnXkJrdtJXjRkkJ&t=75)
  * Do you want to report a bug or request a new feature? [We want to hear from you](https://issues.chromium.org/issues/new?component=1456329&template=0).


Explore the other articles in this series that talk about how ecommerce companies benefited from using new CSS and UI features such as Scroll-driven animations, popover, container queries and the `has()` selector.
  * [Why do Web UI Capabilities matter for your ecommerce site?](https://developer.chrome.com/blog/css-ui-ecommerce)
  * [Scroll-driven animations case studies](https://developer.chrome.com/blog/css-ui-ecommerce-sda)
  * [View Transitions case studies](https://developer.chrome.com/blog/css-ui-ecommerce-vt)
  * [Popover case studies](https://developer.chrome.com/blog/css-ui-ecommerce-popover)
  * [:has() selector case studies](https://developer.chrome.com/blog/css-ui-ecommerce-has)


Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-05-07 UTC.

