---
url: https://developer.chrome.com/blog/missing-from-css?hl=en
title: https://developer.chrome.com/blog/missing-from-css?hl=en
date: 2025-05-11T16:56:47.804635
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/missing-from-css?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/missing-from-css?hl=es-419)




  * On this page
  * [The top ten requests](https://developer.chrome.com/blog/missing-from-css?hl=en#the_top_ten_requests)
    * [Support for styling inputs](https://developer.chrome.com/blog/missing-from-css?hl=en#support_for_styling_inputs)
    * [position: sticky inside overflow:hidden](https://developer.chrome.com/blog/missing-from-css?hl=en#position_sticky_inside_overflowhidden)
    * [Animate to height: auto](https://developer.chrome.com/blog/missing-from-css?hl=en#animate_to_height_auto)
    * [Additional input types](https://developer.chrome.com/blog/missing-from-css?hl=en#additional_input_types)
    * [Real random numbers in CSS](https://developer.chrome.com/blog/missing-from-css?hl=en#real_random_numbers_in_css)
    * [Mixin style classes](https://developer.chrome.com/blog/missing-from-css?hl=en#mixin_style_classes)
    * [Global styles in shadow DOM](https://developer.chrome.com/blog/missing-from-css?hl=en#global_styles_in_shadow_dom)
    * [Dividing mixed units](https://developer.chrome.com/blog/missing-from-css?hl=en#dividing_mixed_units)
  * [Do you agree with the CSS Day top ten?](https://developer.chrome.com/blog/missing-from-css?hl=en#do_you_agree_with_the_css_day_top_ten)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  What's missing from HTML and CSS? 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [The top ten requests](https://developer.chrome.com/blog/missing-from-css?hl=en#the_top_ten_requests)
    * [Support for styling inputs](https://developer.chrome.com/blog/missing-from-css?hl=en#support_for_styling_inputs)
    * [position: sticky inside overflow:hidden](https://developer.chrome.com/blog/missing-from-css?hl=en#position_sticky_inside_overflowhidden)
    * [Animate to height: auto](https://developer.chrome.com/blog/missing-from-css?hl=en#animate_to_height_auto)
    * [Additional input types](https://developer.chrome.com/blog/missing-from-css?hl=en#additional_input_types)
    * [Real random numbers in CSS](https://developer.chrome.com/blog/missing-from-css?hl=en#real_random_numbers_in_css)
    * [Mixin style classes](https://developer.chrome.com/blog/missing-from-css?hl=en#mixin_style_classes)
    * [Global styles in shadow DOM](https://developer.chrome.com/blog/missing-from-css?hl=en#global_styles_in_shadow_dom)
    * [Dividing mixed units](https://developer.chrome.com/blog/missing-from-css?hl=en#dividing_mixed_units)
  * [Do you agree with the CSS Day top ten?](https://developer.chrome.com/blog/missing-from-css?hl=en#do_you_agree_with_the_css_day_top_ten)


Rachel Andrew 
[ GitHub ](https://github.com/rachelandrew) [ LinkedIn ](https://www.linkedin.com/in/rachelandrew) [ Mastodon ](https://front-end.social/@rachelandrew) [ Bluesky ](https://bsky.app/profile/rachelandrew.bsky.social) [ Homepage ](https://rachelandrew.co.uk)
The Chrome team had a big presence at the CSS Day conference this year. We ran the CSS Helpdesk, answering questions from attendees, but also had a whiteboard where we asked people what they thought was still missing from CSS. In this post I'll share the results of asking that question, and also ask you to tell us what you think is missing from HTML and CSS by completing [this short survey](https://forms.gle/PnLGzcB2va1am8qu5). Do you agree with the CSS Day attendees?
The board of ideas at CSS Day.
## The top ten requests
Attendees were asked to write ideas on sticky notes and add them to the board. People could also add their vote to ideas by adding a sticker. The top ten features are as follows.
### Support for styling inputs
This was our top feature request with 21 votes. You really want ways to style these common UI elements in a consistent way.
This is an area that we're well aware of at Chrome, as a top pain point for developers, and there's work underway to create better solutions for developers. For example, [customizable select elements](https://open-ui.org/components/customizableselect/) aim to provide a way to opt into new styling behavior. You could then do things like add images or even more elaborate styling to options. The advantage of this approach is that it would fallback to a regular select menu, allowing this to be a progressive enhancement.
### Visually hidden
With 19 votes at CSS Day, this was the second most popular request. The request is for a way to add content only used by screen readers. This might be an HTML element, where the content is not displayed and only read out by a screen reader.
Typically people achieve this today by creating [a `.visually-hidden` class](https://www.a11yproject.com/posts/how-to-hide-content/) to hide the content but still make it accessible to screen readers.
While this is a popular request, there are people who don't think that this should be implemented. For details read [Visually hidden content is a hack that needs to be resolved, not enshrined](https://www.scottohara.me/blog/2023/03/21/visually-hidden-hack.html) and this discussion on [CSS WG issue 560](https://github.com/w3c/csswg-drafts/issues/560).
### position: sticky inside overflow:hidden
This request received 16 votes. Currently, `position: sticky` only works when all of the parents are `overflow: visible`.
There's [an open issue from 2017 requesting this](https://github.com/w3c/csswg-drafts/issues/865), and while the initial use case of enabling the use of `overflow: hidden` for clearing floats might be less required today, there are many other scenarios detailed in the thread.
### Animate to `height: auto`
At 12 votes, many attendees wanted to animate to `height: auto`. We're happy to be able to say that this is coming to the web platform with [the CSS `interpolate-size` property and `calc-size()` function](https://chromestatus.com/feature/5196713071738880). These will be available from Chrome 129. Look out for a future post with more information about these.
### Additional input types
HTML5 brought you many different [types for the `<input>` element](https://developer.mozilla.org/docs/Web/HTML/Element/input#input_types)—for example `type="email"` for an email address or `type="range"` for a range slider. At CSS Day we got 10 votes for more of these types, for example, double range, or autocomplete with custom datalist.
### Real random numbers in CSS
Another request with 10 votes was for real random numbers in CSS. This has been requested and worked round in the past for a random [animation-duration](https://developer.chrome.com/blog/missing-from-css/%E2%80%8B%E2%80%8Bhttps:/css-tricks.com/random-numbers-css).
### Mixin style classes
CSS has added a number of features previously seen in CSS preprocessors—variables with custom properties, and now CSS Nesting. Reusable mixins however, haven't yet become part of the language, but seven of the CSS Day attendees were keen to see them.
There has been a [CSS Working Group resolution](https://github.com/w3c/csswg-drafts/issues/9350#issuecomment-1939628591) to start working on a specification for this feature, and you can add your thoughts and use cases to the discussion in that issue.
### Global styles in shadow DOM
Another issue that has a large discussion thread of use cases is the request to allow global CSS styles to apply inside a shadow DOM, six people asked for this at CSS Day. This capability would allow global reset styles to also apply in web components, and single CSS files to work across all components of a site. Take a look at [this summary of use cases](https://github.com/WICG/webcomponents/issues/1052#issuecomment-2087900638), and let us know if this is a feature you'd also like to have.
### Dividing mixed units
There was [a proposal for Interop 2024](https://github.com/web-platform-tests/interop/issues/513) requesting the ability to divide by mixed units—for example `calc(100vw / 1px)`. It was deemed too broad for Interop 2024, however many developers, including six people at CSS Day, would like to see this implemented.
### `nth-letter`
CSS has a number of pseudo-elements that act as if you had wrapped a span around some section of content. For example, the [`::first-letter`](https://developer.mozilla.org/docs/Web/CSS/::first-letter) pseudo-element targets the first letter of the first line of the block container it's applied to.
Missing from that list is `::nth-letter`, and you've been asking for `::nth-letter` for [about twenty years](https://adactio.com/journal/14408), so we know this is a long-time ask from web developers. At CSS Day six people voted for this, making it the last of our top ten wanted features.
## Do you agree with the CSS Day top ten?
We would love to hear from a broader audience about these issues, do any of these make your top ten? If not, is there something else you would love to see in CSS and HTML? Let us know by filling out [this short form](https://forms.gle/PnLGzcB2va1am8qu5) and we'll summarize the responses in another post.
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-08-28 UTC.

