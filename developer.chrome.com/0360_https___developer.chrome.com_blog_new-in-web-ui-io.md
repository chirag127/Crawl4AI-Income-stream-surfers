---
url: https://developer.chrome.com/blog/new-in-web-ui-io-2024?hl=en
title: https://developer.chrome.com/blog/new-in-web-ui-io-2024?hl=en
date: 2025-05-11T17:54:08.218341
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-web-ui-io-2024?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-web-ui-io-2024?hl=es-419)

Sign in


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  The latest in CSS and web UI: I/O 2024 recap 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Una Kravets 
[ Mastodon ](https://front-end.social/@una) [ Homepage ](https://una.im)
The web platform is alive with innovation, with CSS and web UI features at the forefront of this exciting evolution. We're living in a golden era for web UI, with new CSS features landing across browsers at a pace we've never seen before, opening up a world of possibilities for creating beautiful and engaging web experiences. This blog post will dive deep into the current state of CSS, exploring some of the most game-changing new features that are redefining how we build web applications, featured live at Google I/O 2024.
## Novel interactive experiences
A web experience is fundamentally a call and response between you and your users–that's why it's so important to invest in quality user interactions. We've been working on some really big improvements that unlock capabilities we've never had before on the web for navigating _within_ web pages and navigating _between_ them.
### Scroll-driven animations
Browser Support
  * 115 
  * 115 


[Source](https://developer.mozilla.org/docs/Web/CSS/animation-timeline)
Like the name implies, the scroll-driven animations API lets you create dynamic scroll-based animations without relying on scroll observers, or other heavy scripting. 
#### Create scroll-driven animations
Similar to how _time-based_ animations work on the platform, you can now use a scroller's _scroll progress_ to start, pause, and reverse an animation. So as you scroll forward, you'll see that animation progress, and when scrolling backward it'll go the other way around. This lets you create partial or full-page visuals with elements animating into and within the viewport, also known as [scrollytelling](https://codepen.io/argyleink/pen/gOyoBLj/ffd0d5869cb5492a2401e0ac8609bbc7), for dynamic visual impact. 
Scroll-driven animations can be used to highlight important content, guide users through a story, or simply add a dynamic touch to your web pages.
### Scroll-driven animation visual
### Live demo
```
@keyframesappear{
from{
opacity:0;
scale:0.8;
}
to{
opacity:1;
scale:1;
}
}
img{
animation:appearlinear;
animation-timeline:view();
animation-range:entry25%cover50%;
}

```

The preceding code defines a simple animation that appears in the viewport by changing the opacity and scale of an image. The animation is driven by the scroll position. To create this effect, first set up the CSS animation, and then set the `animation-timeline`. In this case, the `view()` function with its default values tracks the image relative to the scrollport (which in this instance is also the viewport).
It's important to keep browser support and user preferences in mind, especially for accessibility needs. Therefore, use the `@supports` rule to check if the browser supports scroll-driven animations, and wrap your scroll-driven animation in a user preference query like `@media (prefers-reduced-motion: no-preference)` to respect users' motion preferences. Having made these checks you know that your styles will work, and that the animation is not problematic for the user.
```
@supports(animation-timeline:view()){
@media(prefers-reduced-motion:no-preference){
/* Apply scroll-driven animations here */
}
}

```

Scroll-driven animations can mean full-page scrollytelling experiences but they can also mean more subtle animations like a header bar minimizing and showing a shadow as you scroll a web app.
### Scroll-driven animation visual
### Live demo
```
@keyframesshrink-name{
from{
font-size:2em;
}
to{
font-size:1.5em;
}
}
@keyframesadd-shadow{
from{
box-shadow:none;
}
to{
box-shadow:04px2px-2pxgray;
}
}
header{
animation:add-shadowlinearboth;
}
h2{
animation:shrink-namelinearboth;
}
header,h2{
animation-timeline:scroll();
animation-range:0150px;
}

```

This demo uses a few different keyframe animations—the header, text, nav bar, and background— then applies the respective scroll-driven animation to each. While they each have a different animation style, they all have the same animation-timeline, the nearest scroller, and the same animation range–from the top of the page to 150 pixels.
#### Performance benefits of scroll-driven animations
This built-in API reduces a code burden you'd need to maintain, whether that's custom script you wrote or the inclusion of an additional third party dependency. It also removes the need to ship various scroll observers, meaning some pretty significant performance benefits. This is because scroll-driven animations work off the main thread when animating properties that can be animated on the compositor like transforms and opacity, whether you're using the new API directly in CSS or using the JavaScript hooks.
[Tokopedia recently used scroll-driven animations](https://developer.chrome.com/blog/css-ui-ecommerce-sda#tokopedia) to make the product navigation bar appear as you scrolled. Using this API has had some serious benefits, both for code management and for performance.
Scroll-driven animations drive this product navigation bar on [Tokopedia](https://tokopedia.com) as you scroll down.
> "We managed to reduce up to 80% of our lines of code compared to using conventional JS scroll events and observed that the average CPU usage reduced from 50% to 2% while scrolling. - Andy Wihalim, Senior Software Engineer, Tokopedia"
#### The future of scroll effects
We know these effects will continue to make the web a more engaging place, and we're already thinking about what might come next. This includes the ability to not just use new animation timelines, but to also use a scroll point to trigger the start of an animation, called scroll-triggered animations.
And there are even more scroll features coming to browsers in the future. The following demo shows a combination of these future features. It uses CSS `scroll-start-target` to set the initial date and time within the pickers, and the JavaScript `scrollsnapchange` event to update the header date, making it trivial to synchronize the data with the snapped event.
See live demo [on Codepen](https://codepen.io/argyleink/pen/LYvzGRW)
You can also build on this to update a picker in real time with the JavaScript `scrollsnapchanging` event.
These particular features are currently only in Canary behind a flag, however they unlock capabilities previously impossible or very difficult to build in the platform and highlight the future of scroll-based interactions possibilities.
To learn more about getting started with scroll-driven animations, our team just launched a new video series you can find on the [Chrome for Developers Youtube channel](https://www.youtube.com/playlist?list=PLNYkxOF6rcICM3ttukz9x5LCNOHfWBVnn). Here, you'll learn the basics of scroll-driven animations from Bramus Van Damme including how the feature works, vocabulary, various ways to create effects, and how to combine effects to build rich experiences. It's a great video series to check out.
### View transitions
We just covered a powerful new feature animating _within_ web pages, but there is also a powerful new feature called view transitions for animating _between_ page views to create a seamless user experience. View transitions introduce a new level of fluidity to the web, letting you create seamless transitions between different views within a single page, or even across different pages.
Browser Support
  * 111 
  * 111 
  * 18 


[Source](https://developer.mozilla.org/docs/Web/CSS/view-transition-name)
Airbnb is one of the companies already experimenting with integrating view transitions into their UI for a smooth and seamless web navigation experience. This includes the listing editor sidebar, right into editing photos and adding amenities, all within a fluid user flow.
A same-document view transition as seen on [Airbnb](https://airbnb.com). The portfolio of [Maxwell Barvian](https://barvian.me/), showcasing view transitions between views.
While these full-page effects are beautiful and seamless, you can also create micro-interactions, such as this example where your list view is getting updated on user interaction. This effect can be achieved effortlessly with view transitions.
The way to quickly enable view transitions in your single-page application is as simple as wrapping an interaction using `document.startViewTransition`, and making sure each element that is transitioning has a `view-transition-name`, inline, or dynamically using JavaScript as you create DOM nodes.
### Demo visual
### Live demo
```
document.querySelectorAll('.delete-btn').forEach(btn=>{
btn.addEventListener('click',()=>{
document.startViewTransition(()=>{
btn.closest('.card').remove();
});
})
});

```
```
/* Styles for the transition animation */
::view-transition-old(.card):only-child{
animation:fade-outease-out0.5s;
}

```

#### View transition classes
View transition names can be used to apply custom animations to your view transition, though this can get cumbersome with many elements transitioning. The first new update to view transitions this year simplifies this problem, and introduces the ability to create [view transition classes](https://developer.chrome.com/docs/web-platform/view-transitions/same-document#view-transition-class) that can be applied to custom animations.
Browser Support
  * 125 
  * 125 
  * 18.2 


#### View transition types
Another big improvement for view transitions is support for [view transition types](https://developer.chrome.com/docs/web-platform/view-transitions/same-document#view-transition-types). View transition types are useful when you want a different kind of visual view transition when animating to and from page views.
Browser Support
  * 125 
  * 125 
  * 18 


For example, you might want a homepage to animate to a blog page in a different way than that blog page animates back to the homepage. Or you might want pages to swap in and out in different ways like in this example, going from left to right and visa versa. Before this was messy to do. You could add classes to the DOM to apply styles, and would then have to remove the classes afterward. View-transition-types enable the browser to clean up old transitions instead of requiring you to do this manually before initiating new ones, doing this work for you.
Recording of the [Pagination demo](https://view-transitions.netlify.app/pagination/spa-types/). Types determine which animation to use. Styles are separated in the style sheet thanks to active transition types.
You can set up types within your `document.startViewTransition` function, which now accepts an object. `update` is the callback function that updates the DOM, and `types` is an array with the types. 
```
document.startViewTransition({
update:myUpdate,
types:['slide','forwards']
})

```

#### Multi-page view transitions
What makes the web powerful is how expansive it is. Many applications are not just a single-page, but a robust tapestry containing multiple pages. And that's why we're so excited to announce that we're shipping [cross-document view transitions](https://developer.chrome.com/docs/web-platform/view-transitions/cross-document) support for multi-page applications in Chromium 126.
Browser Support
  * 126 
  * 126 
  * 18.2 


[Source](https://developer.mozilla.org/docs/Web/CSS/@view-transition)
This new cross-document feature set includes web experiences that live within the same-origin, Like navigating from web.dev to to web.dev/blog, but this does not include navigating cross-origin, such as navigating from web.dev to blog.web.dev or to another domain like google.com.
One of the key differences with same-document view transitions is that you don't need to wrap your transition with `document.startViewTransition()`. Instead, opt-in both of the pages involved in the view transition by using the CSS `@view-transition` at-rule.
```
@view-transition{
navigation:auto;
}

```

For a more custom effect, you can hook in JavaScript using the new `pageswap` or `pagereveal` event listeners, which give you access to the view transition object.
With `pageswap` you can do some last-minute changes on the outgoing page right before the old snapshots get taken, and with `pagereveal` customize the new page before it begins to render after it has been initialized.
```
window.addEventListener('pageswap',async(e)=>{
// ...
});
window.addEventListener('pagereveal',async(e)=>{
// ...
});

```
Showing view transitions in a multi-page app. See [demo link](https://view-transitions.netlify.app/profiles/mpa/).
In the future, we plan to expand on view transitions, including:
  * **Scoped transitions** : Let you limit a transition to a DOM subtree, enabling the rest of the page to continue to be interactive, and supporting multiple view transitions running at the same time.
  * **Gesture-driven view transitions** : Use dragging or swipe gestures to trigger a cross-document view transition for more native-like experiences on the web.
  * **Navigation matching in CSS** : Customize your cross-document view transition directly in your CSS as an alternative to using `pageswap` and `pagereveal` events in JavaScript To learn more about view transitions for multi-page applications, including how to most performantly set them up with pre-rendering, check out the following talk by Bramus Van Damme:


## Engine-enabled UI components: Simplifying complex interactions
Building complex web applications is no easy feat, but CSS and HTML are evolving to make this process much more manageable. New features and enhancements are simplifying the creation of UI components, letting you focus on building great experiences. This is done through a collaborative effort involving several key standards bodies and community groups, including the CSS Working Group, Open UI community Group, and WHATWG (Web Hypertext Application Technology Working Group).
One big developer pain point is a seemingly simple request: the ability to style dropdown menus (the select element). While it seems straightforward on the surface, this is a complex problem, touching so many pieces of the platform; from layout and rendering, to scroll and interaction, to user agent styling and CSS properties, and even changes to HTML itself.
Breaking down the pieces of a select
A dropdown consists of many pieces and includes many states that must be accounted for, such as:
  * Keyboard bindings (to enter/exit the interaction)
  * Click-away to dismiss
  * Active popover management (close other popovers when one opens)
  * Tab focus management
  * Visualizing the selected option value
  * Arrow interaction style
  * State management (open/close)


It's currently difficult to manage all of this state yourself, but the platform doesn't make it easy, either. To fix this, we broke down those pieces and we're shipping a few primitive features that will enable styling dropdowns, but also do so much more.
### The Popover API
First we shipped a global attribute called `popover`, which I'm excited to announce just reached Baseline newly available status a few weeks ago.
Browser Support
  * 114 
  * 114 
  * 125 
  * 17 


[Source](https://developer.mozilla.org/docs/Web/API/HTMLButtonElement/popoverTargetAction)
Popover elements are hidden with `display: none` until opened with an invoker such as a button or with JavaScript. To create a basic popover, set the popover attribute on the element, and link its ID to a button using `popovertarget`. Now, the button is the invoker,
### Demo visual
### Live demo
```
<buttonpopovertarget="my-popover">OpenPopover</button>
<divid="my-popover"popover>
<p>Iamapopoverwithmoreinformation.</p>
</div>

```

With the popover attribute now enabled, the browser handles many key behaviors without any additional scripting including:
  * **Promotion to the top layer.** : A separate layer above the rest of the page, so you don't have to play around with `z-index`.
  * **Light-dismiss functionality.** : Clicking outside of the popover area will close the popover and return focus.
  * **Default tab focus management.** : Opening the popover makes the next tab stop inside the popover.
  * **Built-in keyboard bindings.** : Hitting the `esc` key or double toggling will close the popover and return focus.
  * **Default Component bindings.** : The browser semantically connects a popover to its trigger.

Menu on the [GitHub](https://github.com) homepage.
You might even be using this popover API today without realizing it. GitHub implemented popover on their homepage “new” menu and in their pull request review overview. Theyprogressively enhanced this feature using the [popover polyfill](https://developer.chrome.com/blog/new-in-web-ui-io-2024?hl=en), built by Oddbird with some significant support from GitHub's own Keith Cirkel, to support older browsers.
> “We've managed to deprecate literally 1000s of lines of code by migrating to popover. Popover helps us by eliminating the need for battling magic z-index numbers... having the correct accessibility tree relationship established with declarative button behavior, and focus behaviors built in makes it significantly easier for our Design System to implement patterns the right way.-Keith Cirkel, Software Engineer, GitHub”
#### Animating entry and exit effects
When you have popovers, you'll likely want to add some interaction. There are [four new interaction features](https://developer.chrome.com/blog/entry-exit-animations) that landed in the past year to support animating popovers. These include:
The ability to animate `display` and `content-visibility` on a keyframe timeline.
The `transition-behavior` property with the `allow-discrete` keyword to enable transitions of discrete properties like `display`.
Browser Support
  * 117 
  * 117 
  * 129 
  * 17.4 


[Source](https://developer.mozilla.org/docs/Web/CSS/transition-behavior)
The `@starting-style` rule to animate entry effects from `display: none` and into the [top-layer](https://developer.chrome.com/blog/what-is-the-top-layer).
Browser Support
  * 117 
  * 117 
  * 129 
  * 17.5 


[Source](https://developer.mozilla.org/docs/Web/CSS/@starting-style)
The overlay property to control top-layer behavior during an animation.
Browser Support
  * 117 
  * 117 


[Source](https://developer.mozilla.org/docs/Web/CSS/overlay)
These properties work for any element that you're animating into the top layer, whether it's a popover or a dialog. All together, it looks like this for a dialog with a backdrop:
### Demo visual
### Live demo
```
dialog,::backdrop{
opacity:0;
transition:opacity1s,display1sallow-discrete,overlay1sallow-discrete;
}
[open],[open]::backdrop{
opacity:1;
}
@starting-style{
[open],[open]::backdrop{
opacity:0;
}
}

```

First, set up the `@starting-style`, so that the browser knows what styles to animate this element into the DOM from. This is done for both the dialog and the backdrop. Then, style the open state for both the dialog and the backdrop. For a dialog, this uses the `open` attribute, and for a popover, the `::popover-open` pseudo-element. Finally, animate the `opacity`, `display`, and `overlay` using the `allow-discrete` keyword to enable the animation mode where discrete properties can transition.
### Anchor positioning
Popover was just the start of the story. A very exciting update is that support for [anchor positioning](https://developer.chrome.com/blog/anchor-positioning-api) is now available from Chrome 125.
Browser Support
  * 125 
  * 125 


[Source](https://developer.mozilla.org/docs/Web/CSS/anchor-name)
Using anchor positioning, with just a few lines of code, the browser can handle the logic to tether a positioned element to one or more anchor elements. In the following example, a simple tooltip is anchored to each button, positioned at the bottom center.
### Demo visual
### Live demo
Set up an anchor positioned relationship in CSS by using the `anchor-name` property on the anchoring element (in this case the button), and the `position-anchor` property on the positioned element (in this case, the tooltip). Then, apply absolute or fixed positioning relative to the anchor using the `anchor()` function. The following code positions the top of the tooltip to the bottom of the button.
```
.anchor{
anchor-name:--my-anchor;
}
.positioned{
position:absolute;
position-anchor:--my-anchor;
}

```

Alternatively, use the anchor-name directly in the anchor function,and skip the `position-anchor` property. This can be useful when anchoring to multiple elements.
```
.anchor{
anchor-name:--my-anchor;
}
.positioned{
position:absolute;
top:anchor(--my-anchorbottom);
}

```

Finally, use the new `anchor-center` keyword for the `justify` and `align` properties to center the positioned element to its anchor.
```
.anchor{
anchor-name:--my-anchor;
}
.positioned{
position:absolute;
top:anchor(--my-anchorbottom);
justify-self:anchor-center;
}

```

While it's very convenient to use anchor positioning with popover, popover is definitely not a requirement for using anchor positioning. Anchor positioning can be used with any two (or more) elements to create a visual relationship. In fact, the following demo, inspired by an [article from Roman Komarov](https://kizu.dev/anchor-positioning-experiments/), shows an underline style being anchored to list items as you hover or tab over them.
### Demo visual
### Live demo
This example uses the anchor function to set up the anchor position using the physical properties of `left`, `right`, and `bottom`. When you hover over one of the links, the target anchor changes, and the browser shifts the target to apply the positioning, also animating the color at the same time to create a neat effect.
```
ul::before{
content:"";
position:absolute;
left:anchor(var(--target)left);
right:anchor(var(--target)right);
bottom:anchor(var(--target)bottom);
...
}
li:nth-child(1){--anchor:--item-1}
ul:has(:nth-child(1)a:is(:hover,:focus-visible)){
--target:--item-1;
--color:red;
}

```

#### `inset-area` positioning
In addition to the default directional absolute positioning you've likely used before, there' is a new layout mechanism included that has landed as a part of the anchor positioning API called inset area. Inset area makes it easy to place positioned elements relative to their respective anchors, and works on a 9-cell grid with the anchoring element in the center. For example, `inset-area: top` places the positioned element at the top, and `inset-area: bottom` places the positioned element at the bottom.
A simplified version of the first anchor demo looks like this with `inset-area`:
```
.anchor{
anchor-name:--my-anchor;
}
.positioned{
position:absolute;
position-anchor:--my-anchor;
inset-area:bottom;
}

```

You can combine these positional values with span keywords to start at the center position and either span to the left, span to the right, or span all to take up the full set of columns or rows available. You can also use logical properties as well. To make it easier to visualize and pick up this layout mechanism, check out [this tool](https://anchor-tool.com) in Chrome 125+:
Because these elements are anchored, the positioned element dynamically moves around the page as its anchor moves. So in this case, we have container-query-styled card elements, which resize based on their intrinsic size (something you could not do with media queries), and the anchored menu will shift with the new layout as the card UI changes.
### Demo visual
### Live demo
#### Dynamic anchor positions with `position-try-options`
Menus, and submenu navigation are so much easier to create with a combination of popover and anchor positioning. And, when you hit the edge of a viewport with your anchored element, you can let the browser handle the positioning change for you, too. You can do this in a few ways. The first is to create your own positioning rules. In this case, the submenu is initially positioned at the right of the “storefront” button. But you can create a `@position-try` block for when there is not enough space to the right of the menu, giving it a custom identifier of `--bottom`. Then, you connect this `@position-try` block to the anchor using `position-try-options`.
Now, the browser will switch between these anchored states, trying the right position first and then shifting to the bottom. And this can be done with a nice transition.
### Demo visual
### Live demo
```
#submenu{
position-anchor:--submenu;
top:anchor(top);
left:anchor(right);
margin-left:var(--padding);
position-try-options:--bottom;
transition:top0.25s,left0.25s;
width:max-content;
}
@position-try--bottom{
top:anchor(left);
left:anchor(bottom);
margin-left:var(--padding);
}

```

Along with the explicit positioning logic, there are a few keywords the browser provides if you want some basic interactions like flipping your anchor in the block or inline directions.
```
position-try-options:flip-block,flip-inline;

```

For a simple flipping experience, take advantage of these flip keyword values and skip writing a `position-try` definition altogether. So now you can have a fully functional location-responsive anchor positioned element with just a few lines of CSS.
### Demo visual
### Live demo
```
.tooltip{
inset-area:top;
position-try-options:flip-block;
}

```

Learn more about using [anchor positioning](https://developer.chrome.com/blog/anchor-positioning-api).
#### The future of layered UI
We see tethered experiences everywhere, and the set of features shown in this post is an excellent start to unleashing creativity and better control over anchor positioned elements and layered interfaces. But this is just the start. For example, currently `popover` only works with buttons as the invoking element, or with JavaScript. For something like Wikipedia-style previews, a pattern seen all over the web platform, it needs to be possible to interact with, and also trigger a popover from a link and from the user showing interest without necessarily clicking through, like a hover or tab focus.
As a next step for the popover API, we're working on [`interesttarget`](https://open-ui.org/components/interest-invokers.explainer/) to solve these needs and make it easier to recreate these experiences with the proper accessibility hooks built in. This is a challenging accessibility problem to solve, with a lot of open questions around ideal behaviors, but solving and normalizing this functionality at a platform level should improve these experiences for everyone.
```
<ainteresttarget="my-tooltip">Hover/Focustoshowthetooltip</a>
<spanpopover=hintid="my-toolip">Thisisthetooltip</span>

```

In addition, there's another future-facing general invoker ([`invoketarget`](https://open-ui.org/components/invokers.explainer/)) available to test in Canary thanks to the work of two third party developers, Keith Cirkel and Luke Warlow. `invoketarget` supports the declarative developer experience that `popovertarget` provides popovers, normalized for all interactive elements, including `<dialog>`, `<details>`, `<video>`, `<input type="file">`, and more.
```
<buttoninvoketarget="my-dialog">
OpenDialog
</button>
<dialogid="my-dialog">
Helloworld!
</dialog>

```

We know that there are use cases that aren't covered by this API yet. For example, styling the arrow that connects an anchored element to its anchor, especially as the position of the anchored element changes, and enabling an element to “slide” and stay in the viewport instead of snap to another position set when it reaches its bounding box. So while we're excited to land this powerful API, we're also looking forward to expanding on its capabilities even more in the future.
### Stylable select
Using `popover` and `anchor` together, the team has been making progress on finally enabling a customizable select dropdown. The good news is that there has been a lot of progress. The bad news is that this API is still very much in an experimental state at this time. However, I'm excited to share some live demos and updates on our progress and hopefully get some of your feedback. First, there has been progress on how to opt users into the new, customizable select experience. The current, work-in-progress way to do this is to use an appearance property in CSS, set to `appearance: base-select`. Once appearance is set, you'll be opting-in to a new, customizable select experience.
```
select{
appearance:base-select;
}

```

In addition to `appearance: base-select`, there are a few new HTML updates. These include the ability to wrap your options in a `datalist` for customization and the ability to add arbitrary non-interactive content like images in your options. You'll also have access to a new element, `<selectedoption>`, which will reflect the content of the options into itself, which you can then customize to your own needs. This element is really handy.
### Demo visual
### Live demo
```
<select>
 <button type=popover>
  <selectedoption></selectedoption>
 </button>
 <datalist>
  <option value="" hidden>
   <p>Select a country</p>
  </option>
  <option value="andorra">
   <img src="Flag_of_Andorra.svg" />
   <p>Andorra</p>
  </option>
  <option value="bolivia">
   <img src="Flag_of_Bolivia.svg" />
   <p>Bolivia</p>
  </option>
...
 </datalist>
</select>

```

The following code demonstrates customizing `<selectedoption>` in the Gmail UI, where a visual icon represents the type of reply selected to save space. You can use basic display styles within `selectedoption` to differentiate the option styling from the preview styling. In this case, text, which is shown in the option can be visually hidden in the `selectedoption`.
### Demo visual
### Live demo
```
selectedoption .text {
 display: none;
}

```

One of the biggest advantages in reusing the `<select>` element for this API is backwards compatibility. In this country select, you can see a customized UI with flag images in the options for easier user-parsing of the content. Because non-supported browsers will ignore the lines they do not understand, such as the custom button, datalist, selectedoption, and images within the options, the fallback will be similar to the current default select UI.
Supported browser visual on the left vs. unsupported browser fallback on the right.
With customizable selects, the possibilities are endless. I particularly love this Airbnb-style country selector because there is a clever style for responsive design. You can do this and so much more with the upcoming stylable select, making it a much-needed addition to the web platform.
### Demo visual
### Live demo
### Exclusive accordion
Solving select styling (and all the pieces that come along with it) isn't the only UI component the Chrome team has been focusing on. The first additional component update is the ability to create exclusive accordions, in which only one of the items in the accordion can be opened at a time
Browser Support
  * 120 
  * 120 
  * 130 
  * 17.2 


The way to enable this is to apply the same name value for multiple details elements, hence creating a connected group of details, much like a group of radio buttons
Exclusive accordion demo ```
<details name="learn-css" open>
 <summary>Welcome to Learn CSS!</summary>
</details>
<details name="learn-css">
 <summary>Box Model</summary>
 <p>...</p>
</details>
<details name="learn-css">
 <summary>Selectors</summary>
 <p>...</p>
</details>

```

### `:user-valid` and `:user-invalid`
Another UI component improvement are the `:user-valid` and `:user-invalid` pseudo-classes. Stable in all browsers recently, the `:user-valid` and `:user-invalid` pseudo-classes behave similarly to the `:valid` and `:invalid` pseudo-classes, but match a form control only after a user has significantly interacted with the input. This means significantly less code is needed to determine if a form value has been interacted with, or has become “dirty”, which can be very useful for providing user feedback, and reduces a lot of scripting that would be necessary to do this in the past.
Browser Support
  * 119 
  * 119 
  * 88 
  * 16.5 


[Source](https://developer.mozilla.org/docs/Web/CSS/:user-valid)
### Demo Screencast
### Live Demo
```
input:user-valid,
select:user-valid,
textarea:user-valid{
--state-color:green;
--bg:linear-gradient(...);
}
input:user-invalid,
select:user-invalid,
textarea:user-invalid{
--state-color:red;
--bg:linear-gradient(...);
}

```

Learn more about using [user-* form validation pseudo-elements](https://web.dev/articles/user-valid-and-user-invalid-pseudo-classes).
### `field-sizing: content`
Another handy component update that has landed recently is `field-sizing: content`, which can be applied to form controls like inputs and textareas. This enables the size of the input to grow (or shrink) depending on its contents. `field-sizing: content` can be particularly handy for textareas, as you no longer are resolved to fixed sizes where you may need to scroll up to see what you wrote in the earlier parts of your prompt in a too-small input box.
Browser Support
  * 123 
  * 123 


[Source](https://developer.mozilla.org/docs/Web/CSS/field-sizing)
### Demo Screencast
### Live Demo
```
textarea,select,input{
field-sizing:content;
}

```

Learn more about [field sizing](https://developer.chrome.com/docs/css-ui/css-field-sizing).
### `<hr>` in `<select>`
The ability to enable the `<hr>`, or horizontal rule element in selects is another small but useful component feature. While this doesn't have much semantic use, it does help you nicely separate content within a select list, especially content that you might not necessarily want to group with an optgroup, like a placeholder value.
### Select Screenshot
### Select Live Demo
```
<select name="majors" id="major-select">
 <option value="">Select a major</option>
 <hr>
 <optgroup label="School of Fine Arts">
  <option value="arthist">
Art History
 </option>
 <option value="finearts">
  Fine Arts
 </option>
...
</select>

```

Learn more about using [using hr in select](https://developer.chrome.com/blog/hr-in-select)
## Quality-of-life improvements
We're constantly iterating, and it's not just for interactions and components. There are many other quality of life updates that have landed in the past year.
### Nesting with lookahead
Native CSS nesting landed in all browsers last year, and has since improved to support lookahead, which means the `&` before element names is no longer a requirement. This makes nesting feel so much more ergonomic and similar to what I have been used to in the past.
Browser Support
  * 120 
  * 120 
  * 117 
  * 17.2 


[Source](https://developer.mozilla.org/docs/Web/CSS/Nesting_selector)
One of my favorite things about CSS nesting is that it enables you to visually block components, and within those components include states and modifiers, such as container queries and media queries. Previously, I was in the habit of grouping all of these queries at the bottom of the file for specificity purposes. Now, you can write them in a way that makes sense, right next to the rest of your code
```
.card{
/* card base styles */
h2{
/* child element style */
}
&.highlight{
/* modifier style */
}
&:hover,&:focus{
/* state styles */
}
@container(width>=300px){
/* container query styles */
}
}

```

### Align-content for block layout
Another really nice change is the ability to use centering mechanisms like `align-content` in block layout. This means you can now do things like vertical centering within a div without needing to apply flex or grid layout, and without side effects like preventing margin-collapse, that you may not want from those layout algorithms.
Browser Support
  * 123 
  * 123 
  * 125 
  * 17.4 


### Screenshot
### Live Demo
```
div{
align-content:center;
}

```

### Text-wrap: balance and pretty
Speaking of layout, text layout got a nice improvement with the addition of `text-wrap: balance` and `pretty`. `text-wrap: balance` is used for a more uniform block of text, while `text-wrap: pretty` focuses on reducing singletons on the last line in the text.
### Demo Screencast
### Live Demo
In the following demo you can compare by dragging the slider, the effects of `balance` and `pretty` on a heading and a paragraph. Try translating the demo into another language!
```
h1{
text-wrap:balance;
}

```

Learn more about [text-wrap: balance](https://developer.chrome.com/blog/css-text-wrap-balance).
### International typography updates
[Typographic layout updates for CJK text features](https://developer.chrome.com/blog/css-i18n-features) got a lot of nice updates in the past year, like the `word-break: auto-phrase` feature that wraps the line at the natural phrase boundary.
Browser Support
  * 119 
  * 119 


Comparison of `word-break: normal` and `word-break: auto-phrase`
And `text-spacing-trim`, which applies kerning between punctuation characters to improve the readability of Chinese, Japanese, and Korean typography for more visually pleasing results.
Browser Support
  * 123 
  * 123 


[Source](https://developer.mozilla.org/docs/Web/CSS/text-spacing-trim)
When punctuation characters appear in a row, the right-half of the CJK period should be removed.
### Relative color syntax
In the world of color theming, we saw a big update with relative color syntax.
In this example, the colors here use Oklch-based theming. As the hue-value adjusts based on the slider, the entire theme changes. This can be achieved with relative color syntax. The background uses the primary color, based on the hue, and adjusts the lightness, chroma, and hue channels to adjust its value. --i is the sibling index in the list for the gradation of values, showing how you can combine stepping with custom properties and relative color syntax to build themes.
### Demo Screencast
### Live Demo
In the following demo you can compare by dragging the slider, the effects of `balance` and `pretty` on a heading and a paragraph. Try translating the demo into another language!
```
:root{
--hue:230;
--primary:oklch(70%.2var(--hue));
}
li{
--_bg:oklch(fromvar(--primary)
calc(l-(var(--i)*.05))
calc(c-(var(--i)*.01))
calc(h-(var(--i)+5)));
}

```

### `light-dark()` function
Along with the `light-dark()` function, theming has become much more dynamic and simplified.
Browser Support
  * 123 
  * 123 
  * 120 
  * 17.5 


[Source](https://developer.mozilla.org/docs/Web/CSS/color_value/light-dark)
The `light-dark()` function is an ergonomic improvement that simplifies color theming options so that you can write theme styles in a more concise way, as demonstrated so nicely in this visual diagram by Adam Argyle. Before, you would need two different blocks of code, (your default theme and a user preference query), to set up theme options. Now, you can write these style options for both light and dark themes in the same line of CSS using the `light-dark()` function.
Visualization of `light-dark()`. See [demo](https://web.dev/articles/light-dark#practical_application) for more.  ```
html{
color-scheme:lightdark;
}
button{
background-color:light-dark(lightblue,darkblue);
}

```

If the user selected a light theme, the button will have a light blue background. If the user selected a dark theme, the button will have a dark blue background.
### `:has()` selector
And I would be remiss to talk about modern UI without mentioning one of the most impactful interop highlights from the past year, which has to be the `:has()` selector, landing across browsers in December of last year. This API is a game-changer for writing logical styles.
Browser Support
  * 105 
  * 105 
  * 121 
  * 15.4 


[Source](https://developer.mozilla.org/docs/Web/CSS/:has)
The `:has()` selector enables you to check if a child element has specific children, or if those children are in a specific state, and essentially can function as a parent selector as well.
Demo of `has()` being used to style comparison blocks on [Tokopedia](https://tokopedia.com/).
`:has()` has already shown to be particularly useful for [many companies](https://developer.chrome.com/blog/css-ui-ecommerce-has), including PolicyBazaar, who use `:has()` to style blocks based on their interior content, such as in the compare section, where the style adjusts if there is a plan to compare in the block, or if its empty.
> “With the :has() selector, we were able to eliminate JavaScript based validation of the user's selection and replace it with a CSS solution which is working seamlessly for us with the same experience as before.–Aman Soni, Tech Lead, PolicyBazaar”
### Container queries
Another key addition to the web that is now newly available and growing in usage is container queries, which enable the ability to query an element parent's intrinsic size to apply styles: a much more fine-toothed comb than media queries, which only query the viewport size.
Browser Support
  * 105 
  * 105 
  * 110 
  * 16 


[Source](https://developer.mozilla.org/docs/Web/CSS/@container)
Angular recently launched a beautiful new documentation site on angular.dev using container queries to style the header blocks based on their available space on the page. So even if the layout changes, and goes from a multicolumn sidebar layout to a single-column layout, the header blocks can self-adjust.
[Angular.dev](https://angular.dev) site showcasing container queries in the header cards.
Without container queries, doing something like this was quite hard to achieve, and damaging for performance, requiring resize observers and element observers. Now, it's trivial to style an element based on its parent size.
### Demo Screencast
### Live Demo
Recreating the Angular header card container query.
### `@property`
And finally very soon, we are excited to see @property land in Baseline. This is a key feature for providing semantic meaning to CSS custom properties (also known as CSS variables), and enables a slew of new interaction features. `@property` also enables contextual meaning, typechecking, defaults, and fallback values in CSS. Opening the doors for even more robust features like range style queries. This is a feature that was never possible before, and now provides so much depth to the language of CSS.
Browser Support
  * 85 
  * 85 
  * 128 
  * 16.4 


[Source](https://developer.mozilla.org/docs/Web/CSS/@property)
### Demo Screencast
### Live Demo
```
@property--card-bg{
syntax:"<color>";
inherits:false;
initial-value:#c0bae8;
}

```

## Conclusion
With all of these new powerful UI capabilities landing across browsers, the possibilities are endless. Novel interactive experiences with scroll-driven animations and view transitions make the web more fluid and interactive in ways we've never seen before. And next level UI components make it easier than ever to build robust, beautifully customized components without ripping out the entire native experience. And finally, quality of life improvements in architecture, layout, typography, and responsive design not only solve the little big things, but also give developers the tools they need to build complex interfaces that work on a variety of devices, form factors, and user needs.
These new features you should be able to remove third-party scripting for performance-heavy features like scrollytelling and tethering elements to each other with anchor positioning, build fluid page transitions, finally style dropdowns, and improve the overall structure of your code natively.
It's never been a better time to be a web developer. There hasn't been so much energy and excitement since the announcement of CSS3. Features we've needed but have only dreamed of actually landing in the past, are finally becoming a reality and a part of the platform. And it's because of your voice that we're able to prioritize and finally bring these capabilities to life. We're working on making it easier to do the hard, tedious stuff natively so you can spend more time building the things that matter–like the core features and design details that set your brand apart.
To learn more about these new features as they land, follow along at developer.chrome.com and web.dev, where our team shares the latest news in web technologies. Try out scroll driven animations, view transitions, anchor positioning, or even the stylable select, and let us know what you think. We're here to listen and we're here to help.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-06-11 UTC.

