---
url: https://developer.chrome.com/blog/new-in-chrome-135?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-135?hl=en
date: 2025-05-11T16:57:33.479535
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-135?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-chrome-135?hl=es-419)

Sign in


  * On this page
  * [Highlights from this release](https://developer.chrome.com/blog/new-in-chrome-135?hl=en#highlights_from_this_release)
  * [The command and commandfor attributes](https://developer.chrome.com/blog/new-in-chrome-135?hl=en#command-commandfor)
  * [The CSS shape() function](https://developer.chrome.com/blog/new-in-chrome-135?hl=en#shape)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  New in Chrome 135 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Highlights from this release](https://developer.chrome.com/blog/new-in-chrome-135?hl=en#highlights_from_this_release)
  * [The command and commandfor attributes](https://developer.chrome.com/blog/new-in-chrome-135?hl=en#command-commandfor)
  * [The CSS shape() function](https://developer.chrome.com/blog/new-in-chrome-135?hl=en#shape)


Rachel Andrew 
[ GitHub ](https://github.com/rachelandrew) [ LinkedIn ](https://www.linkedin.com/in/rachelandrew) [ Mastodon ](https://front-end.social/@rachelandrew) [ Bluesky ](https://bsky.app/profile/rachelandrew.bsky.social) [ Homepage ](https://rachelandrew.co.uk)
Published: April 1, 2025 
Chrome 135 is rolling out now, and this post shares some of the key features from the release. Read the full [Chrome 135 release notes](https://developer.chrome.com/release-notes/135), and check out [our quarterly roundup](https://developer.chrome.com/blog/new-in-chrome-video-q1-2025) for everything released so far this year.
## Highlights from this release
There's a whole set of features that [enable CSS carousels](https://developer.chrome.com/blog/new-in-chrome-135?hl=en#carousels). The [`command` and `commandfor`](https://developer.chrome.com/blog/new-in-chrome-135?hl=en#command-commandfor) attributes let you attach behavior to buttons in a declarative way. The[ CSS `shape()` function](https://developer.chrome.com/blog/new-in-chrome-135?hl=en#shape) lets you define a shape for the `clip-path` and `offset-path` properties.
## CSS carousels
There's a large number of CSS features in the release notes, and many of these are different small additions that combine to enable CSS carousels. The key features are the new CSS pseudo-elements—`::scroll-button() and`::scroll-marker()`, which let you turn a scrollable area into a carousel.
To find out how to use these new features, and to get inspiration for your own projects, read [Carousels with CSS](https://developer.chrome.com/blog/carousels-with-css).
## The `command` and `commandfor` attributes
Chrome 135 introduces new capabilities for providing declarative behaviour with the new `command` and `commandfor` attributes, enhancing and replacing the `popovertargetaction` and `popovertarget` attributes. These new attributes can be added to buttons, letting the browser address some core issues around simplicity and accessibility, and provide built-in common functionality.
The following HTML sets up declarative relationships between a button and the menu which lets the browser handle the logic and accessibility for you. There's no need to manage aria-expanded or add any additional JavaScript.
```
<button commandfor="my-menu" command="show-popover">
Open Menu
</button>
<div popover id="my-menu">
 <!-- ... -->
</div>

```

Learn more about these new attributes in [Introducing command and commandfor](https://developer.chrome.com/blog/command-and-commandfor).
## The CSS `shape()` function
The [shape()](https://developer.mozilla.org/docs/Web/CSS/basic-shape/shape) CSS function is used to define a shape for the clip-path and offset-path properties.
The `shape()` function uses a set of commands roughly equivalent to the ones used by [`path()`](https://developer.mozilla.org/docs/Web/CSS/basic-shape/path), but does so with more standard CSS syntax, and allows the full range of CSS functionality, such as additional units and math functions. It's in Firefox Nightly and Safari 18.4 beta, so should be Baseline Newly available soon.
## And more!
Of course there's plenty more.
  * The Web Speech API now includes `MediaStreamTrack` support.
  * The Float16Array is supported and becomes Baseline Newly available.
  * The Observable API is now supported.


## Further reading
This covers only some key highlights. Check the following links for additional changes in Chrome 134.
  * [Release notes for Chrome 135](https://developer.chrome.com/release-notes/135).
  * [What's new in Chrome DevTools (135)](https://developer.chrome.com/blog/new-in-devtools-135).
  * [ChromeStatus.com updates for Chrome 135](https://chromestatus.com/features#milestone%3D135).
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule).


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video. Or follow us on X or LinkedIn for new articles and blog posts.
As soon as Chrome 135 is released, we'll be right here to tell you what's new in Chrome!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-04-01 UTC.

