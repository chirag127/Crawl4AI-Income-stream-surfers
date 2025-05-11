---
url: https://developer.chrome.com/blog/delaying-shipping-of-css-functions?hl=en
title: https://developer.chrome.com/blog/delaying-shipping-of-css-functions?hl=en
date: 2025-05-11T16:55:10.325007
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/delaying-shipping-of-css-functions?hl=en#main-content)


  * On this page
  * [Call to experiment](https://developer.chrome.com/blog/delaying-shipping-of-css-functions?hl=en#call_to_experiment)
  * [Want to know more about @function?](https://developer.chrome.com/blog/delaying-shipping-of-css-functions?hl=en#want_to_know_more_about_function)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  Delaying the shipping of CSS @function from Chrome 136 to 139 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Call to experiment](https://developer.chrome.com/blog/delaying-shipping-of-css-functions?hl=en#call_to_experiment)
  * [Want to know more about @function?](https://developer.chrome.com/blog/delaying-shipping-of-css-functions?hl=en#want_to_know_more_about_function)


Adam Argyle 
[ GitHub ](https://github.com/argyleink) [ Glitch ](https://glitch.com/@argyleink) [ Homepage ](https://nerdy.dev)
Published: March 06, 2025 
On February 25th Chrome published an [Intent To Ship for `@function`](https://groups.google.com/a/chromium.org/g/blink-dev/c/bvi4D7eD7wI/m/djYVLu6OAwAJ) and received feedback requesting a longer experimentation phase. While the overall experimentation phase wasn't short, there have been some recent impactful spec changes, and these deserved some more experimentation time. 
We're also hopeful and excited that this extended experimentation phase may yield more community experimentation.
## Call to experiment
Now is the time to grab a copy of [Canary](https://www.google.com/chrome/canary/), enable [experimental web platform features](https://developer.chrome.com/docs/web-platform/chrome-flags), start testing CSS `@function`, and [report any bugs](https://issues.chromium.org/issues/new?component=1456329&template=0) you find. We now have time to experiment longer, we should take advantage of this.
To help get you started, here's a few explorations:
  * [Pontus Horn - button variants](https://codepen.io/pantz/pen/wBvJjGV)
  * [Nils Riedemann - font scales](https://codepen.io/nocksock/pen/YPzWpWY)
  * [Bramus - a light dark function for more than color](https://codepen.io/bramus/pen/wBvKVpR)


The following CSS demonstrates a terse yet useful example:
```
@function--light-dark(--light,--dark){
result:var(--light);
@media(prefers-color-scheme:dark){
result:var(--dark);
}
}

```

[CSS Mixins 1 Specification](https://drafts.csswg.org/css-mixins-1/#defining-custom-functions)
## Want to know more about `@function`?
[Bramus has a great set of demos](https://www.bram.us/2025/02/18/css-at-function-and-css-if/) and [CSS Tricks also didn't delay to jump on the excitement](https://css-tricks.com/functions-in-css/).
> Arguments?! Return values?! That's worth spitting my coffee out for! I had to learn more about them, and luckily, the spec is clearly written.
- [Juan Diego Rodriguez](https://css-tricks.com/author/monknow/) on [CSS Tricks](https://css-tricks.com/functions-in-css/)
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-03-06 UTC.

