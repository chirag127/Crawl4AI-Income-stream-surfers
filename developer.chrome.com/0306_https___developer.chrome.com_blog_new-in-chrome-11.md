---
url: https://developer.chrome.com/blog/new-in-chrome-117?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-117?hl=en
date: 2025-05-11T16:57:17.075872
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-117?hl=en#main-content)


  * On this page
  * [New CSS features for entry and exit animations.](https://developer.chrome.com/blog/new-in-chrome-117?hl=en#exit-entry-animations)
  * [Local overrides streamlined in DevTools.](https://developer.chrome.com/blog/new-in-chrome-117?hl=en#local-overrides)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  New in Chrome 117 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [New CSS features for entry and exit animations.](https://developer.chrome.com/blog/new-in-chrome-117?hl=en#exit-entry-animations)
  * [Local overrides streamlined in DevTools.](https://developer.chrome.com/blog/new-in-chrome-117?hl=en#local-overrides)


Adriana Jara 
[ GitHub ](https://github.com/tropicadri) [ LinkedIn ](https://www.linkedin.com/in/adrianajara) [ Mastodon ](https://hachyderm.io/@tropicadri)
Here's what you need to know:
  * [Three new CSS features](https://developer.chrome.com/blog/new-in-chrome-117?hl=en#exit-entry-animations) make it easy to add smooth entry and exit animations.
  * Compute higher order datasets with [array grouping](https://developer.chrome.com/blog/new-in-chrome-117?hl=en#array-grouping).
  * DevTools makes [local overrides easier](https://developer.chrome.com/blog/new-in-chrome-117?hl=en#local-overrides).
  * And there’s plenty [more](https://developer.chrome.com/blog/new-in-chrome-117?hl=en#more).


I’m Adriana Jara. Let’s dive in and see what’s new for developers in Chrome 117.
## New CSS features for entry and exit animations.
These three new CSS features complete the set to easily add entry and exit animations, and smoothly animate to and from the top layer dismissible elements such as dialogs and popovers.
The first feature is `transition-behavior`. To transition discrete properties, like `display`, use the `allow-discrete` value for `transition-behavior`.
```
.card{
transition:opacity0.25s,display0.25s;
transition-behavior:allow-discrete;/* Note: be sure to write this after the shorthand */
}
.card.fade-out{
opacity:0;
display:none;
}

```

Then the `@starting-style` rule is used to animate entry effects from `display: none` and into the top-layer. Use `@starting-style` to apply a style that the browser can look up before the element is open on the page.
```
/* 0. IS-OPEN STATE  */
/* The state at which the element is open + transition logic */
.item{
height:3rem;
display:grid;
overflow:hidden;
transition:opacity0.5s,transform0.5s,height0.5s,display0.5sallow-discrete;
}
/* 1. BEFORE-OPEN STATE  */
/* Starting point for the transition */
@starting-style{
.item{
opacity:0;
height:0;
}
}
/* 2. EXITING STATE  */
/* While it is deleting, before DOM removal in JS, apply this
  transformation for height, opacity, and a transform which
  skews the element and moves it to the left before setting
  it to display: none */
.is-deleting{
opacity:0;
height:0;
display:none;
transform:skewX(50deg)translateX(-25vw);
}

```

Finally, to fade out a `popover` or `dialog` from the top layer, add the `overlay` property to your list of transitions. Include overlay in the transition or animation to animate overlay along with the rest of the features and ensure it stays in the top layer when animating. This will look much smoother.
```
[open]{
transition:opacity1s,display1sallow-discrete;
}

```
```
[open]{
transition:opacity1s,display1sallow-discrete,overlay1sallow-discrete;
}

```

Checkout [Four new CSS features for smooth entry and exit animations](https://developer.chrome.com/blog/entry-exit-animations) for details on how to use these features for improving your user experience with motion.
## Array grouping
In programming, array grouping is an extremely common operation, seen most often when we use SQL's GROUP BY clause and MapReduce programming (which is better thought of as map-group-reduce).
The ability to combine data into groups allows developers to compute higher order datasets. For example, the average age of a cohort, or daily LCP values for a webpage.
Array grouping enables these scenarios by adding the `Object.groupBy` and `Map.groupBy` static methods.
`groupBy` calls a provided callback function once for each element in an iterable. The callback function should return a string or symbol that indicates the group of the associated element.
In the following example, from the [MDN documentation](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object/groupBy), there is an array of products with the `groupBy` method used to return them grouped by their type.
```
constinventory=[
{name:"asparagus",type:"vegetables",quantity:5},
{name:"bananas",type:"fruit",quantity:0},
{name:"goat",type:"meat",quantity:23},
{name:"cherries",type:"fruit",quantity:5},
{name:"fish",type:"meat",quantity:22},
];
constresult=Object.groupBy(inventory,({type})=>type);
/* Result is:
{
 vegetables: [
  { name: 'asparagus', type: 'vegetables', quantity: 5 },
 ],
 fruit: [
  { name: "bananas", type: "fruit", quantity: 0 },
  { name: "cherries", type: "fruit", quantity: 5 }
 ],
 meat: [
  { name: "goat", type: "meat", quantity: 23 },
  { name: "fish", type: "meat", quantity: 22 }
 ]
}
*/

```

For more details check out the [`groupBy` documentation](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object/groupBy).
## Local overrides streamlined in DevTools.
The [local overrides](https://developer.chrome.com/docs/devtools/overrides) feature is now streamlined, so you can easily mock response headers and web content of remote resources from the **Network** panel without access to them.
To override web content, open the **Network** panel, right-click a request, and select **Override content**.
If you have local overrides set up but disabled, DevTools enables them. If you haven't set them up yet, DevTools prompts you in the action bar at the top. Select a folder to store the overrides in and allow DevTools access to it.
Once the overrides are set up, DevTools then takes you to **Sources** > **Overrides** > **Editor** to let you [override web content](https://developer.chrome.com/docs/devtools/overrides#make-changes).
Note that the overridden resources are indicated with in the **Network** panel. Hover over the icon to see what's overridden.
Check out [what’s new in DevTools](https://developer.chrome.com/blog/new-in-devtools-117) for all the details and more information on DevTools in Chrome 117.
## And more!
Of course there’s plenty more.
  * The much anticipated [`subgrid`](https://developer.mozilla.org/docs/Web/CSS/CSS_grid_layout/Subgrid) value for `grid-template-columns` and `grid-template-rows` is now implemented in Chrome.
  * There is a [`WebSQL` deprecation trial](https://developer.chrome.com/blog/deprecating-web-sql) and a developer trial for the [`unload` event deprecation](https://developer.chrome.com/docs/web-platform/deprecating-unload).


## Further reading
This covers only some key highlights. Check the links below for additional changes in Chrome 117.
  * [What's new in Chrome DevTools (117)](https://developer.chrome.com/blog/new-in-devtools-117)
  * [Chrome 117 deprecations and removals](https://developer.chrome.com/blog/deps-rems-117)
  * [ChromeStatus.com updates for Chrome 117](https://chromestatus.com/features#milestone%3D117)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/116.0.5845.171..117.0.5938.57)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
Yo soy Adriana Jara, and as soon as Chrome 117 is released, I'll be right here to tell you what's new in Chrome!
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2023-09-12 UTC.

