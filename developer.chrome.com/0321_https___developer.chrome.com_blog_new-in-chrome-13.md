---
url: https://developer.chrome.com/blog/new-in-chrome-133?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-133?hl=en
date: 2025-05-11T16:57:33.468980
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-133?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-chrome-133?hl=es-419)

Sign in


  * On this page
  * [CSS advanced attr() function](https://developer.chrome.com/blog/new-in-chrome-133?hl=en#attr)
  * [CSS scroll state container queries](https://developer.chrome.com/blog/new-in-chrome-133?hl=en#scroll-state)
  * [CSS text-box, text-box-trim, and text-box-edge](https://developer.chrome.com/blog/new-in-chrome-133?hl=en#text-box)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  New in Chrome 133 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [CSS advanced attr() function](https://developer.chrome.com/blog/new-in-chrome-133?hl=en#attr)
  * [CSS scroll state container queries](https://developer.chrome.com/blog/new-in-chrome-133?hl=en#scroll-state)
  * [CSS text-box, text-box-trim, and text-box-edge](https://developer.chrome.com/blog/new-in-chrome-133?hl=en#text-box)


Rachel Andrew 
[ GitHub ](https://github.com/rachelandrew) [ LinkedIn ](https://www.linkedin.com/in/rachelandrew) [ Mastodon ](https://front-end.social/@rachelandrew) [ Bluesky ](https://bsky.app/profile/rachelandrew.bsky.social) [ Homepage ](https://rachelandrew.co.uk)
Here's what you need to know:
  * [CSS advanced `attr()` function](https://developer.chrome.com/blog/new-in-chrome-133?hl=en#attr) allows types besides `<string>` and use in all CSS properties.
  * [CSS scroll state container queries](https://developer.chrome.com/blog/new-in-chrome-133?hl=en#scroll-state) let you use container queries to style descendants of containers based on their scroll state.
  * [CSS `text-box`, `text-box-trim`, and `text-box-edge`](https://developer.chrome.com/blog/new-in-chrome-133?hl=en#text-box) make finer control of vertical alignment of text possible
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-133?hl=en#more).


## CSS advanced `attr()` function
This feature adds to the existing `attr()` function, features specified in CSS Level 5. This allows types besides `<string>` and use in all CSS properties (in addition to the existing support for the pseudo-element content).
In the following example the value of the `color` property for `div` uses the value from the `data-color` attribute. This attribute value is parsed into a `<color>` using `attr()` and `type()`. The fallback value is set to `red`.
```
<div data-foo="blue">test</div>

```
```
div{
color:attr(data-footype(<color>),red);
}

```

Learn more in [CSS `attr()` gets an upgrade](https://developer.chrome.com/blog/advanced-attr).
## CSS scroll state container queries
Use container queries to style descendants of containers based on their scroll state.
The query container is either a scroll container, or an element affected by the scroll position of a scroll container. The following states can be queried:
  * `stuck`: A sticky positioned container is stuck to one of the edges of the scroll box.
  * `snapped`: A scroll snap aligned container is currently snapped horizontally or vertically.
  * `scrollable`: Whether a scroll container can be scrolled in a queried direction.


A new container-type: `scroll-state` lets containers be queried. For example:
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

Learn more and see some demos in [CSS scroll state queries](https://developer.chrome.com/blog/css-scroll-state-queries).
## CSS `text-box`, `text-box-trim`, and `text-box-edge`
The `text-box-trim` property specifies the sides to trim, above or below, and the `text-box-edge` property specifies how the edge should be trimmed.
These properties let you control vertical spacing precisely by using the font metrics.
```
h1{
/* trim both sides to the capital letters */
text-box:trim-bothcapalphabetic;
/* trim both sides to the lowercase letter x */
text-box:trim-bothexalphabetic;
}

```

Find out how to use these new properties in [CSS `text-box-trim`](https://developer.chrome.com/blog/css-text-box-trim).
## And more!
Of course there's plenty more.
  * `Animation.overallProgress`gives you a convenient and consistent representation of how far along an animation has advanced across its iterations and regardless of the nature of its timeline.
  * `Node.prototype.moveBefore` lets you move elements around a DOM tree, without resetting the element's state.
  * The `FileSystemObserver` interface notifies websites of changes to the file system.
  * The `PublicKeyCredential` `getClientCapabilities()` method lets you determine which WebAuthn features are supported by the user's client.


See the full [Chrome 133 release notes](https://developer.chrome.com/release-notes/133) for details of these and many other features that are New in Chrome!
## Further reading
This covers only some key highlights. Check the following links for additional changes in Chrome 133.
  * [Release notes for Chrome 133](https://developer.chrome.com/release-notes/133).
  * [What's new in Chrome DevTools (133)](https://developer.chrome.com/blog/new-in-devtools-133).
  * [ChromeStatus.com updates for Chrome 133](https://chromestatus.com/features#milestone%3D133).
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule).


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
As soon as Chrome 133 is released, we'll be right here to tell you what's new in Chrome!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-02-04 UTC.

