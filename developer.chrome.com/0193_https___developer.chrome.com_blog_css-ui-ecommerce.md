---
url: https://developer.chrome.com/blog/css-ui-ecommerce-vt?hl=en
title: https://developer.chrome.com/blog/css-ui-ecommerce-vt?hl=en
date: 2025-05-11T16:54:58.342411
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/css-ui-ecommerce-vt?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/css-ui-ecommerce-vt?hl=es-419)




  * On this page
  * [Things to consider when using the View Transition API](https://developer.chrome.com/blog/css-ui-ecommerce-vt?hl=en#things_to_consider_when_using_the_view_transition_api)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  View transitions case studies 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Things to consider when using the View Transition API](https://developer.chrome.com/blog/css-ui-ecommerce-vt?hl=en#things_to_consider_when_using_the_view_transition_api)


Swetha Gopalakrishnan 
[ LinkedIn ](https://www.linkedin.com/in/swetha-gopalakrishnan-5ba92936)
Saurabh Rajpal 
[ LinkedIn ](https://www.linkedin.com/in/imsaurabhrajpal)
View transitions are animated and seamless transitions between different states of a web page or application's UI. The [View Transition API](https://developer.mozilla.org/docs/Web/API/View_Transitions_API) has been designed to let you create these effects in a more straightforward and performant way than has been possible before. The API offers multiple benefits over previous JavaScript approaches including:
  * **Improved user experience:** Smooth transitions and visual cues guide users through changes in UI, making navigation feel natural and less jarring.
  * **Visual continuity:** Maintaining a sense of continuity between views reduces cognitive load and helps users stay oriented within the application.
  * **Performance:** The API tries to use as few main thread resources as possible which creates smoother animations.
  * **Modern aesthetic:** The improved transitions contribute to a polished and engaging user experience.


Browser Support
  * 111 
  * 111 
  * 18 


[Source](https://developer.mozilla.org/docs/Web/API/Document/startViewTransition)
This post [is part of a series](https://developer.chrome.com/blog/css-ui-ecommerce) discussing how ecommerce companies enhanced their website using new CSS and UI features. In this article, discover how some companies implemented and benefited from the View Transition API.
## redBus
> redBus has always tried to create as much parity between their native and web experiences as possible. Prior to the View Transition API, implementing these animations on our web assets was challenging. But with the API, we have found it intuitive to create transitions across multiple user journeys to make the web experience more app-like. All this coupled with performance benefits makes it a must have feature for all websites.—[Amit Kumar](https://in.linkedin.com/in/amit-kumar-8385b734), Senior Engineering Manager, redBus.
The team has implemented view transitions in multiple places. Here's an example of a combination of fade in and slide in animation on the login icon on the home page.
Fade and slide in view transitions when the user clicks the login icon on the redBus home page.
### Code
This implementation uses multiple`view-transition-name`and custom animations (`scale-down`and `scale-up`). Using `view-transition-name`with a unique value separates the sign in component from the rest of the page to animate it separately. Creating a new unique `view-transition-name` also creates a new `::view-transition-group`in the pseudo-element tree (shown in the following code), allowing it to be manipulated separately from the default `::view-transition-group(root)`.
```
::view-transition
├─::view-transition-group(root)
│ └─…
├─::view-transition-group(signin)
│ └─…
└─::view-transition-group(signinclose)  
└─…

```
```
//Code for VT for login
if(!document.startViewTransition){
this.setState(
{
closeSigninModal:condition?true:false
},
()=>{
if(closeSigninCb){
closeSigninCb();
}
}
);
}else{
consttransition=document.startViewTransition();
transition.ready.finally(()=>{
setTimeout(()=>{
this.setState(
{
closeSigninModal:condition?true:false
},
()=>{
if(closeSigninCb){
closeSigninCb();
}
}
);
},500);
});
}
.signin_open{
view-transition-name:signin;
}
.signin_close{
view-transition-name:signinclose;
}
::view-transition-group(signin),
::view-transition-group(signinclose){
animation-duration:0.5s;
}
::view-transition-old(signin){
animation-name:-ua-view-transition-fade-out,scale-down;
}
::view-transition-new(signin){
animation-name:-ua-view-transition-fade-in,scale-up;
}
::view-transition-new(signinclose){
animation-name:-ua-view-transition-fade-out,scale-down;
}
@keyframesscale-down{
to{
scale:0;
}
}
@keyframesscale-up{
from{
scale:0;
}
}

```

## Tokopedia
The team used view transitions to add a fading animation when the user switches between product thumbnails.
> The implementation is so easy, by using `startViewTransition` we immediately get a more pleasant fading transition compared to the previous implementation without any effects—[Andy Wihalim](https://www.linkedin.com/in/andy-wihalim-a4872512b), Senior Software Engineer, Tokopedia.
### Before
### After
### Code
The following code uses a React framework and includes framework-specific code, such as `flushSync.`Read more about [working with frameworks to implement view transitions](https://developer.chrome.com/docs/web-platform/view-transitions#working_with_frameworks). This is a basic implementation which checks if the browser supports `startViewTransition` and if so, does the transition. Otherwise, it falls back to default behavior.
```
consthandleClick=
({url,index})=>
()=>{
if('startViewTransition'indocument){//check if browser supports VT
document.startViewTransition(()=>{
flushSync(()=>{
setDisplayImage({url,index});
setActiveImageIndex(index);
});
});
}else{//if VT is not supported, fall back to default behavior
setDisplayImage({url,index});
setActiveImageIndex(index);
}
};
...
<ThumbnailonClick={handleClick({url,index})}/>

```

## Policybazaar
Policybazaar's [investment](https://investmentlife.policybazaar.com/prequote-ulip-lite) vertical has used the View Transition API on help tip elements like "why buy", making them visually appealing and improving usage of such features.
> By incorporating View Transitions, we eliminated repetitive CSS and JavaScript code responsible for managing animations across various states. This saved development effort and significantly enhanced the user experience.—[Aman Soni](https://www.linkedin.com/in/amansoni211/), Tech Lead, Policybazaar.
View transitions animation on the "Why buy from Policybazaar" CTA on an investment listing page.
### Code
The following code is similar to the previous examples. One thing to note is the ability to override the default styles and animations of `::view-transition-old(root)`and`::view-transition-new(root)`. In this case, the default `animation-duration` was updated to 0.4s.
```
togglePBAdvantagePopup(state:boolean){
this.showPBAdvantagePopup=state;
if(!document.startViewTransition){
changeState();
return;
}
document.startViewTransition(()=>{changeState();});
functionchangeState(){
document.querySelector('.block_section').classList.toggle('hide');
document.querySelector('.righttoggle_box').classList.toggle('show');
}
}

```
```
.righttoggle_box{
view-transition-name:advantage-transition;
}
.block_section{
view-transition-name:advantage-transition;
}
::view-transition-old(root),::view-transition-new(root){
animation-duration:0.4s;
}

```

## Things to consider when using the View Transition API
When using multiple view transition effects on the same page, ensure that you have a different view-transition-name for each effect or section to prevent conflicts.
While a view transition is active (transitioning), it will add a new layer on top of the rest of the UI. So, avoid triggering the transition on hover, because the `mouseLeave` event will be triggered unexpectedly (when the actual cursor is still not moving yet).
## Resources
  * [Smooth and simple transitions with the View Transition API](https://developer.chrome.com/docs/web-platform/view-transitions)
  * [Explainer: View Transitions for MPA](https://github.com/WICG/view-transitions/blob/main/cross-doc-explainer.md)
  * [Case Study: Seamless navigation made possible with View Transitions](https://developer.chrome.com/blog/view-transitions-case-studies)
  * [Case Study: The Web Can Do What!? | Deliver app-like navigations](https://thewebshowcase.withgoogle.com/deliver-app-like-navigations)
  * [Interop Proposal: Make View Transitions available across browsers](https://github.com/web-platform-tests/interop/issues/437)
  * Do you want to report a bug or request a new feature? We want to hear from you for [SPA](https://issues.chromium.org/issues/new?component=1456906&template=0) and [MPA](https://issues.chromium.org/issues/new?component=1456205&template=0).


Explore the other articles in this series that talk about how ecommerce companies benefited from using new CSS and UI features such as Scroll-driven animations, popover, container queries and the `has()` selector.
  * [Why do Web UI Capabilities matter for your ecommerce site?](https://developer.chrome.com/blog/css-ui-ecommerce)
  * [Scroll-driven animations case studies](https://developer.chrome.com/blog/css-ui-ecommerce-sda)
  * [Popover API case studies](https://developer.chrome.com/blog/css-ui-ecommerce-popover)
  * [Container Queries case studies](https://developer.chrome.com/blog/css-ui-ecommerce-cq)
  * [:has() selector case studies](https://developer.chrome.com/blog/css-ui-ecommerce-has)


Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-05-07 UTC.

