---
url: https://developer.chrome.com/blog/css-ui-ecommerce-sda
title: https://developer.chrome.com/blog/css-ui-ecommerce-sda
date: 2025-05-11T16:54:51.654725
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/css-ui-ecommerce-sda#main-content)
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


#  Scroll-driven animations case studies 
Stay organized with collections  Save and categorize content based on your preferences. 
Swetha Gopalakrishnan 
[ LinkedIn ](https://www.linkedin.com/in/swetha-gopalakrishnan-5ba92936)
Saurabh Rajpal 
[ LinkedIn ](https://www.linkedin.com/in/imsaurabhrajpal)
[Scroll-driven animations](https://developer.mozilla.org/docs/Web/CSS/animation-timeline) are a common UX pattern on the web. A scroll-driven animation is linked to the scroll position of a scroll container. This means that as you scroll up or down, the linked animation scrubs forward or backward in direct response. Examples of this are effects such as parallax background images or reading indicators which move as you scroll.
Developers have typically created scroll-driven animations by using JavaScript to respond to scroll events on the main thread. This makes it hard to create performant scroll-driven animations that are in sync with scrolling, due to scroll events being delivered asynchronously, and often leads to jank due to being on the main thread.
However, as part of the new [CSS and UI features landing in browsers](https://developer.chrome.com/blog/css-ui-ecommerce), you can now create declarative scroll-driven animations. With Scroll Timelines and View Timelines, new concepts that integrate with the existing [Web Animations API (WAAPI)](https://drafts.csswg.org/web-animations-1/) and [CSS Animations API](https://drafts.csswg.org/css-animations-1/), you can now have silky smooth scroll-driven animations running off the main thread, with just a few lines of code. In this case study, discover how Tokopedia, redBus, and Policybazaar are already benefiting from this new feature.
Browser Support
  * 115 
  * 115 


[Source](https://developer.mozilla.org/docs/Web/CSS/animation-timeline)
## Tokopedia
Tokopedia replaced their previous custom JavaScript implementations with Scroll-driven animations to optimize their page performance, and to enhance overall browsing experience across their ecommerce conversion funnel.
> We managed to reduce up to 80% of our lines of code compared to using conventional JavaScript scroll events and observed that the average CPU usage reduced from 50% to 2% while scrolling— [Andy Wihalim](https://www.linkedin.com/in/andy-wihalim-a4872512b), Senior Software Engineer, Tokopedia
Animated changing visibility of top sticky bar based on user scroll position.
### Code
The following implementation uses the `scroll()` function to set an _anonymous scroll progress timeline_ for controlling the progress of the CSS animation. The visibility of the top sticky bar changes based on the scroll position within the defined `animationRange`.
```
consttoggleBar=keyframes({
to:{height:48},
});
exportconstcssWrapper=css({
position:'fixed',
left:0,
width:'100vw',
pointerEvents:'none',
marginTop:120,
height:0,
overflow:'hidden',
display:'flex',
flexDirection:'column',
justifyContent:'flex-end',
animation:`${toggleBar} linear both`,
animationTimeline:'scroll()',
animationRange:'20px 70px',
});

```

## redBus
redBus has different animations for mobile and desktop on their [things-to-do](https://www.redbus.my/things-to-do) landing page, which is shown early in the conversion funnel to all users. With scroll-driven animations, they were able to replace these custom JavaScript implementations with CSS to achieve the same effect.
### Use cases
Photo Gallery with [Image Reveal](https://scroll-driven-animations.style/demos/image-reveal/css/) (for mobile) and [Cover Flow](https://scroll-driven-animations.style/demos/cover-flow/css/) (for Desktop).
Scroll-driven animation image reveal effect for loading images on redBus "Things To Do" photo gallery.
### Code (Mobile)
In the previous example, Tokopedia used the _anonymous scroll progress timeline_. In the following code, redBus uses the _named view progress timeline_. The animation changes the `opacity` and `clip-path` of the `<img>` element within the defined `animation-range` inside the element's nearest ancestor scroller, which is the photo gallery scroller in this case.
```
constreveal=keyframes`
  from {
    opacity: 0;
    clip-path: inset(45% 20% 45% 20%);
  }
  to {
    opacity: 1;
    clip-path: inset(0% 0% 0% 0%);
  }`
constCardImage=styled.div`
  width: 100%;
  height: 100%;
  img {
    border-top-left-radius: 0.75rem;
    border-top-right-radius: 0.75rem;
    height: 100%;
    width: 100%;
    object-fit: cover;
    view-timeline-name: --revealing-image;
    view-timeline-axis: block;
    /* Attach animation, linked to the View Timeline */
    animation: linear ${reveal} both;
    animation-timeline: --revealing-image;
    /* Tweak range when effect should run*/
    animation-range: entry 25% cover 50%;
  }
`;

```

> We are very happy to see this feature as it's a perfect blend of performance with better experience, boosting our Page Experience signals for SEO. On top of that, the minimal learning curve makes it a must-have for every ecommerce website. We also got positive feedback and support from other teams to leverage SDA for more user journeys.— [Amit Kumar](https://in.linkedin.com/in/amit-kumar-8385b734), Senior Engineering Manager, redBus.
## Policybazaar
Comparing insurance plans is a repeated key action taken by users to guide their decision making process. Using scroll-driven animations, Policybazaar shrank the size of low-priority elements in response to the user scrolling the table. This resulted in a graceful scrolling experience while improving readability.
> With scroll-driven animations, we were able maximize the viewport space for the user to compare plans, ensuring a focused and clutter-free reading experience.—[Rishabh Mehrotra](https://www.linkedin.com/in/rishabh-mehrotra-4483a274/), Head of Design for Life Insurance BU, PolicyBazaar.
Scroll-driven animation `animate-timeline` on compare-plan table in Investment and Life LOB (Line of Business).
### Code
Similar to the previous example from Tokopedia, Policybazaar is using the `scroll()` function to set an _anonymous scroll progress timeline_ for controlling the progress of the CSS animation. In this case shrinking the font size and fading the header based on the scroll position within the defined `animation-range`.
```
@supports(animation-timeline:scroll()){
.plan-comparison.inner-header{
animation:move-and-fade-headerlinearboth;
}
.plan-comparison.left-side{
animation:shrink-namelinearboth;
}
.plan-comparison.inner-header,.plan-comparison.left-side{
animation-timeline:scroll();
animation-range:0150px;
}
}
@keyframesmove-and-fade-header{
to{
translate:0%-5%;
top:103px;
}
}
@keyframesshrink-name{
to{
font-size:1.5rem;
}
}

```

## Scroll-driven animations as a common pattern across the user journey
All the featured ecommerce companies used Scroll-driven animations on pages with cards, animating cards to bring the user's attention to them . The following examples show scroll effects on cards in different parts of the user journey. This is typically achieved using an _anonymous view progress timeline_ for controlling the progress of the custom CSS animation, as shown in the following CSS snippet.
```
@keyframesanimate-in{
0%{opacity:0;transform:translateY(10%);}
100%{opacity:1;transform:translateY(0);}
}
@keyframesanimate-out{
0%{opacity:1;transform:translateY(0);}
100%{opacity:0;transform:translateY(-10%);}
}
.flyin_animate{
animation:animate-inlinearforwards;
animation-timeline:view();
animation-range:entry;
}

```

### redBus (Home page)
Scroll-driven animation fly-in effect for loading product cards on redBus "Things To Do" landing page.
### Policybazaar (Product Listing Page)
Scroll-driven animation fade-in, fade-out of product cards in Investment and Life LOB (Line of Business).
### Tokopedia (Product Details Page)
Fade-in, Fade-out animation while scrolling through the products listed.
## Things to consider when using the Scroll-driven Animations API
It's possible to polyfill scroll-driven animations for non-supporting browsers, for example with the [Scroll-timeline polyfill](https://github.com/flackr/scroll-timeline). If you do, this will require additional testing to make sure that it works well alongside your framework, and that browsers using the polyfill don't experience animation failure or janky experiences.
From CSS you can use `@supports` to test for support of animation-timeline before using scroll-driven animations. For example:
```
@supports(animation-timeline:scroll()){
}

```

## Resources
  * [Scroll-driven animations demos](https://scroll-driven-animations.style/)
  * [Animate elements on scroll with Scroll-driven animations](https://developer.chrome.com/docs/css-ui/scroll-driven-animations)
  * [Codelab: Getting started with scroll-driven animations in CSS](https://codelabs.developers.google.com/scroll-driven-animations#0)
  * [Chrome Extension: Scroll-driven animation debugger](https://chromewebstore.google.com/detail/scroll-driven-animations/ojihehfngalmpghicjgbfdmloiifhoce)
  * [Scroll-timeline Polyfill](https://github.com/flackr/scroll-timeline?tab=readme-ov-file#scroll-timeline-polyfill)
  * Do you want to report a bug or new feature? [We want to hear from you](https://issues.chromium.org/issues/new?component=1456613&template=0)!


Explore the other articles in this series which talks about how ecommerce companies benefited from using new CSS and UI features such as View Transitions, Popover, Container Queries and the `has()` selector.
  * [Why do Web UI Capabilities matter for your ecommerce site?](https://developer.chrome.com/blog/css-ui-ecommerce)
  * [View Transitions case studies](https://developer.chrome.com/blog/css-ui-ecommerce-vt)
  * [Popover API case studies](https://developer.chrome.com/blog/css-ui-ecommerce-popover)
  * [Container Queries case studies](https://developer.chrome.com/blog/css-ui-ecommerce-cq)
  * [:has() selector case studies](https://developer.chrome.com/blog/css-ui-ecommerce-has)


Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-05-07 UTC.

