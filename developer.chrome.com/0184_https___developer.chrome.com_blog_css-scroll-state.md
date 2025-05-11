---
url: https://developer.chrome.com/blog/css-scroll-state-queries?hl=en
title: https://developer.chrome.com/blog/css-scroll-state-queries?hl=en
date: 2025-05-11T16:54:40.952639
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/css-scroll-state-queries?hl=en#main-content)
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


#  CSS scroll-state() 
Stay organized with collections  Save and categorize content based on your preferences. 
Like container queries; but for stuck, snapped, and overflowing queries.
Adam Argyle 
[ GitHub ](https://github.com/argyleink) [ Bluesky ](https://bsky.app/profile/nerdy.dev)
Published: Jan 15, 2025 
Chrome 133 builds upon container queries by introducing scroll state container queries. The browser managed state for sticky positioning, scroll snap points, and scrollable elements can now be queried and adapted to from CSS.
## Overview
Before scroll state queries, you’d need to use JavaScript to understand if an element was stuck, snapped, or scrollable. Now there's a more performant method [on the standards track](https://www.w3.org/TR/css-conditional-5/#scroll-state-container) for knowing this information and adapting accordingly. There's also a new way to trigger animations, unlocking scroll triggered animation from CSS.
Here's an overview of the state queries available from Chrome 133: 

[Stuck state](https://developer.chrome.com/blog/css-scroll-state-queries?hl=en#stuck):
    Trigger style changes when an element is stuck to an edge. 

[Snapped state](https://developer.chrome.com/blog/css-scroll-state-queries?hl=en#snapped):
    Trigger style changes when an element is snapped on an axis. 

[Scrollable state](https://developer.chrome.com/blog/css-scroll-state-queries?hl=en#scrollable):
    Trigger style changes when an element is overflowing.
The good news is that everything you've learned from container queries will help you work with scroll state queries.
There's also uncharted territory between [scroll driven animations](https://developer.chrome.com/docs/css-ui/scroll-driven-animations) and scroll state container queries; we need to experiment with the timing and context to uncover whether a scroll driven animation or a scroll triggered scroll-state animation will be best. The following video and demo illustrate the predicament; a sticky triggered animation compared against a scroll driven animation.
(left) scroll-state() triggered animation, (right) scroll-driven animation <https://codepen.io/web-dot-dev/pen/emOrBaV>
### First scroll-state query
The **first step** is to define the container, using a new value for the `container-type` property. As with a container query, the element you want to query is the one you give the `container-type` and optionally a `container-name`. With scroll state queries, you give the element that is snapping, stuck or has overflow `container-type: scroll-state`.
```
.stuck-top{
container-type:scroll-state;
position:sticky;
top:0px;
}

```

The **second step** is to select the child of that container which will respond to the state, as with container queries this can't be the same element that has the `container-type` on it.
```
.stuck-top{
container-type:scroll-state;
position:sticky;
top:0px;
nav{
@containerscroll-state(stuck:top){
background:Highlight;
color:HighlightText;
}
}
}

```

The **third step** is to try it out. The following CSS example will style the background red when the `.stuck-top` element sticks to the top at `0`. With a few extra lines to the CSS we would have already written and an extra containing element that proxies the browser state, our components are much smarter about their surroundings.
<https://codepen.io/web-dot-dev/pen/ByBxpwR>
### Progressive Enhancement
The `@supports` at-rule and nesting can let you add progressive enhancement or conditional feature usage in just a couple of additional lines of code:
```
.stuck-top{
container-type:scroll-state;
position:sticky;
top:0px;
@supports(container-type:scroll-state){
nav{
@containerscroll-state(stuck:top){
background:Highlight;
color:HighlightText;
}
}
}
}

```

Also, remember to use `@media (prefers-reduced-motion: no-preference) {}` around your motion, if you end up animating elements around the page with scroll-state queries.
## Use Cases
### Stuck
Perhaps this section should be called "sticky situations?" This a small collection of sticky state use cases, plus a bonus section of ideas that need to be built.
```
@containerscroll-state(stuck:top){}
@containerscroll-state(stuck:bottom){}

```

[Full syntax list](https://www.w3.org/TR/css-conditional-5/#stuck)
#### Add a shadow when stuck
One of the most common use cases for a stuck query is for navigation bars that want to add `box-shadow` when stuck, so they can appear to float over the content they overlay.
<https://codepen.io/web-dot-dev/pen/GgKdryj> ```
.stuck-top{
container-type:scroll-state;
position:sticky;
top:0px;
nav{
transition:box-shadow.3sease;
@containerscroll-state(stuck:top){
box-shadow:var(--shadow-5);
}
}
}

```

#### Activate the current stuck header
Another common sticky UI feedback scenario is highlighting the currently stuck element. In a list of alphabetized bands, this can be super helpful and supportive to the experience.
<https://codepen.io/web-dot-dev/pen/pvzVRaK> ```
.sticky-slide{
dt{
container-type:scroll-state;
position:sticky;
inset-block-start:0;
inset-inline:0;
header{
transition:
background.3sease,
box-shadow.5sease;
@containerscroll-state(stuck:top){
background:hsl(265100%27%);
box-shadow:05px5px#0003;
}
}
}
}

```

Here's another variant, where the headers are on the side of the list items. Lots of possibilities! 
<https://codepen.io/web-dot-dev/pen/azoGpGg>
#### Idea overflow
Here's a list of sticky demos that might inspire you to add a little spice to the demo, or remove their JavaScript, with scroll state queries. I suggest trying to build one that you like, it'll help the syntax and ideas stick 😏.
  * <https://codepen.io/BlogFire/pen/PoGMjaX> - sticky sticky notes variant
  * <https://codepen.io/mikegolus/pen/jOZzRzw> - add shadows to a table when they stick
  * <https://codepen.io/MarcRay/pen/PomBeP> - under header navbar appear on trigger
  * <https://codepen.io/kevinpowell/pen/OqKJjK> - footer navbar reveal
  * <https://codepen.io/abhisekz-the-decoder/pen/eKaLRd> - sticky card headers
  * <https://codepen.io/tutsplus/pen/abojPjP> - pricing header shadow on trigger
  * <https://codepen.io/kevinpowell/pen/KEjMEv> - sticky section sidebar titles


### Snapped
With snapped state queries we can remove some of the responsibility from JavaScript and [Snap Events](https://developer.chrome.com/blog/scroll-snap-events), and move the handling to CSS.
```
@containerscroll-state(snapped:x){}
@containerscroll-state(snapped:y){}
@containerscroll-state(snapped:inline){}
@containerscroll-state(snapped:block){}

```

[Full syntax list](https://www.w3.org/TR/css-conditional-5/#snapped)
A small reminder, in case you skipped the section [First scroll-state query](https://developer.chrome.com/blog/css-scroll-state-queries?hl=en#first_scroll-state_query), the container for a snap query is the element with `scroll-snap-align` on it, and the element that can adapt must be a child of that element. This means there's three elements needed to set this up:
```
a scroll container with `scroll-snap-type`
⤷ a snap target with both `scroll-snap-align` and `container-type: scroll-state`
  ⤷ a child of the snap target that can query the container for snap state

```

#### Visually boost the snapped item
It's very common with a center snapped scroller to highlight or feature the center snapped item. In this example of testimonials, the [`not`](https://css-tricks.com/logic-in-css-media-queries/#aa-not) keyword is used so all unsnapped testimonials have low opacity, while the snapped rests in its natural presentation state.
<https://codepen.io/web-dot-dev/pen/NPKMdBX> ```
.demo{
overflow:autohidden;
scroll-snap-type:xmandatory;
article{
container-type:scroll-state;
scroll-snap-align:center;
@supports(container-type:scroll-state){
*{
transition:opacity.5sease;
@containernotscroll-state(snapped:x){
opacity:.25;
}
}
}
}
}

```

#### Show the caption for the snapped item
This is a good example of how scroll state queries enable scroll triggered animation. It's also a good example of when respecting reduced motion is valuable in the CSS.
<https://codepen.io/web-dot-dev/pen/XJrqpBG> ```
.demo{
overflow-x:auto;
scroll-behavior-x:contain;
scroll-snap-type:xmandatory;
.card{
container-type:scroll-state;
scroll-snap-align:center;
@supports(container-type:scroll-state){
@media(prefers-reduced-motion:no-preference){
figcaption{
transform:translateY(100%);
@containerscroll-state(snapped:x){
transform:translateY(0);
}
}
}
}
}
}

```

#### Animating in slide elements
It's really common to animate elements of a slide show or presentation when giving a talk. It used to be pretty annoying to write an intersection observer for this, which all it did was set a class on the slide. Now we don't need any JavaScript.
<https://codepen.io/web-dot-dev/pen/dPbeNqY> ```
html{
scroll-snap-type:ymandatory;
}
section{
container-type:scroll-state;
scroll-snap-align:start;
scroll-snap-stop:always;
@supports(container-type:scroll-state){
@media(prefers-reduced-motion:no-preference){
h1{
transition:opacity.5sease,transform.5svar(--ease-spring-3);
transition-delay:.5s;
opacity:0;
transform:scale(1.25);
@containerscroll-state(snapped:block){
opacity:1;
transform:scale(1);
}
}
}
}
}

```

You might notice that all of the snapped CSS state queries behave like `scrollsnapchanging`, as opposed to `scrollsnapchange`. This gives you the earliest hook possible for providing visual feedback of the snapped element. If it's too eager, consider the JavaScript event.
### Scrollable
The scrollable state query is going to be very helpful in showing visual affordances for when a scroll area can actually be scrolled. Until scroll state queries, this was [difficult information to know](https://www.bram.us/2023/09/16/solved-by-css-scroll-driven-animations-detect-if-an-element-can-scroll-or-not/). 
```
@containerscroll-state(scrollable:top){}
@containerscroll-state(scrollable:right){}
@containerscroll-state(scrollable:bottom){}
@containerscroll-state(scrollable:left){}

```

[Full syntax list](https://drafts.csswg.org/css-conditional-5/#scrollable)
#### Indicate scroll with shadows
There's a famous [CSS trick by Lea Verou](https://lea.verou.me/blog/2012/04/background-attachment-local/) that uses `background-attachment: local` to achieve an effect similar to this, as well as a way to do it with [scroll driven animation](https://kizu.dev/scroll-driven-animations/#proper-scrolling-shadows). Each technique has tradeoffs, it's on us to explore when and where each of these techniques is best suited.
The following example uses a single sticky element that spans the scrollport. A gradient at the top and a gradient at the bottom have their opacity animated with `@property` when their contextual scroll state query applies: `@container scroll-state(scrollable: top)`. 
Also notice, it's the first container that is both a `size` and `scroll-state` container.
<https://codepen.io/web-dot-dev/pen/OPLZWBj> ```
.scroll-container{
container-type:scroll-statesize;
overflow:auto;
&::after{
content:" ";
background:var(--_shadow-top),var(--_shadow-bottom);
transition:
--_scroll-shadow-color-1-opacity.5sease,
--_scroll-shadow-color-2-opacity.5sease;
@containerscroll-state(scrollable:top){
--_scroll-shadow-color-1-opacity:var(--_shadow-color-opacity,25%);
}
@containerscroll-state(scrollable:bottom){
--_scroll-shadow-color-2-opacity:var(--_shadow-color-opacity,25%);
}
}
}

```

#### Arrow prompt
Sometimes showing an arrow can aid users in discovering that an area is scrollable. These tend to point in the direction that scrolling can occur, and disappear once they're not needed anymore. You can do that with the following code.
<https://codepen.io/web-dot-dev/pen/OPLZWBj> ```
@containerscroll-state((scrollable:top)or(not(scrollable:bottom))){
translate:0calc(100%+10px);
}
@containerscroll-state((scrollable:top)and(not(scrollable:bottom))){
translate:0calc(100%+10px);
rotate:.5turn;
}

```

#### Return to top
Another popular scroll state interaction is the "scroll to top" convenience button. The following code causes the scroll to top button to disappear when there's nowhere to scroll up. 
This solution is a little bit inverted, but it lets you to reduce the amount of CSS. The natural resting place of the button is in view, so you need to tell it to hide when there's nowhere to scroll up anymore.
<https://codepen.io/web-dot-dev/pen/OPLZWBj> ```
@containernotscroll-state(scrollable:top){
translate:0calc(100%+10px);
}

```

## Continued study
If you're looking for more, here's a few resources that range from specification details to other great articles covering this topic:
  * What else should we be able to container query? <https://github.com/w3c/csswg-drafts/issues/5989>
  * scroll-state() explainer - <https://drafts.csswg.org/css-conditional-5/scroll_state_explainer.md>
  * scroll-state() CSS specification - <https://www.w3.org/TR/css-conditional-5/#scroll-state-container>
  * Layout [snapshotting](https://github.com/w3c/csswg-drafts/pull/11056) in HTML event loop
  * A podcast episode on state queries - <https://nerdy.dev/the-css-podcast-on-state-queries>
  * More articles 
    * <https://utilitybend.com/blog/is-the-sticky-thing-stuck-is-the-snappy-item-snapped-a-look-at-state-queries-in-css/>
    * <https://ishadeed.com/article/css-state-queries/>
    * <https://csscade.com/can-you-detect-overflow-with-css/>
    * <https://css-tip.com/overflow-detection/> - detecting with scroll driven animation in a way that more than just children can know (with the tradeoff of trickery)


Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-01-15 UTC.

