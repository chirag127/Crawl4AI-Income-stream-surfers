---
url: https://developer.chrome.com/blog/new-in-chrome-112?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-112?hl=en
date: 2025-05-11T16:57:06.090254
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-112?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-chrome-112?hl=es-419)

Sign in


  * On this page
  * [CSS support for nesting.](https://developer.chrome.com/blog/new-in-chrome-112?hl=en#nesting-rules)
  * [Algorithm update for <dialog> initial focus.](https://developer.chrome.com/blog/new-in-chrome-112?hl=en#dialog)
  * [Skipping service worker no-op fetch handlers.](https://developer.chrome.com/blog/new-in-chrome-112?hl=en#no-op-sw)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  New in Chrome 112 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [CSS support for nesting.](https://developer.chrome.com/blog/new-in-chrome-112?hl=en#nesting-rules)
  * [Algorithm update for <dialog> initial focus.](https://developer.chrome.com/blog/new-in-chrome-112?hl=en#dialog)
  * [Skipping service worker no-op fetch handlers.](https://developer.chrome.com/blog/new-in-chrome-112?hl=en#no-op-sw)


Adriana Jara 
[ GitHub ](https://github.com/tropicadri) [ LinkedIn ](https://www.linkedin.com/in/adrianajara) [ Mastodon ](https://hachyderm.io/@tropicadri)
Here's what you need to know:
  * CSS now supports [nesting rules](https://developer.chrome.com/blog/new-in-chrome-112?hl=en#nesting-rules).
  * The algorithm to set the initial focus on [`<dialog>` elements was updated](https://developer.chrome.com/blog/new-in-chrome-112?hl=en#dialog).
  * No-op `fetch()` handlers on [service workers are skipped](https://developer.chrome.com/blog/new-in-chrome-112?hl=en#no-op-sw) from now on to make navigations faster.
  * And there’s plenty [more](https://developer.chrome.com/blog/new-in-chrome-112?hl=en#more).


I’m Adriana Jara. Let’s dive in and see what’s new for developers in Chrome 112.
## CSS support for nesting.
One of our favorite CSS preprocessor features is now built into the language: nesting style rules.
Before nesting, every selector needed to be explicitly declared, separately from one another. This leads to repetition, stylesheet bulk, and a scattered authoring experience.
Before
```
.nesting{
color:hotpink;
}
.nesting>.is{
color:rebeccapurple;
}
.nesting>.is>.awesome{
color:deeppink;
}
```

After [nesting](https://www.w3.org/TR/css-nesting-1/), selectors can be continued and related style rules to it can be grouped within.
After
```
.nesting{
color:hotpink;
>.is{
color:rebeccapurple;
>.awesome{
color:deeppink;
}
}
}
```

Nesting helps developers by reducing the need to repeat selectors while also co-locating style rules for related elements. It can also help styles match the HTML they target.
If the `.nesting` component in the example was removed from the project, you could delete the entire group instead of searching files for related selector instances.
Nesting can help with:
  * Organization.
  * Reducing file size.
  * Refactoring.


Checkout [this article](https://developer.chrome.com/articles/css-nesting) for tips to make the most of CSS nesting and you can find the support for nesting in devtools [here](https://developer.chrome.com/blog/new-in-devtools-112#nesting).
## Algorithm update for `<dialog>` initial focus.
The HTML `<dialog>` element is the standardized way to represent a dialog box or other interactive component, such as a dismissible alert or a subwindow, that needs to be displayed on top of all other content in a web page.
This HTML element is the recommended way to create such content because its features were built to provide better and consistent usability and accessibility.
One of those features is handling which element gets focused when the dialog is opened, in this version the algorithm that selects that element was updated.
From now on:
The dialog focusing steps look at keyboard focusable elements instead of any focusable element The `<dialog>` element itself gets focus if it has the autofocus attribute set
The `<dialog>` element itself gets focus as a fallback instead of focus being "reset" to the `<body>` element.
Read the [documentation](https://developer.mozilla.org/docs/Web/HTML/Element/dialog) for more details on the `<dialog>` element.
## Skipping service worker no-op fetch handlers.
From Chrome 112 the service worker start and the listener dispatch from the navigation critical path will be omitted, if a user agent identifies that all the service worker's fetch listeners are no-ops.
This feature makes the navigation of those pages faster.
Having the fetch handler was one of the PWA requirements for a web app to be installable. We suspect that might be the reason some sites have essentially an empty fetch handler. However, to start a service worker and execute a no-op listener only brings overhead, without bringing any of the benefits that could be implemented with the right service worker like caching or offline capabilities. So Chrome now skips them to improve navigation.
As part of this change, Chrome will show console warnings if all the service worker’s fetch listeners are no-ops, and encourage developers to remove those fetch listeners.
## And more!
Of course there’s plenty more.
  * The setter for `document.domain` is now deprecated.
  * There is an [origin trial](https://developer.chrome.com/origintrials#/view_trial/1390486384950640641) for the `X-Requested-With header` deprecation in WebView
  * The recorder in devtools can now record with [pierce selectors](https://developer.chrome.com/blog/new-in-devtools-112#pierce-selectors).


## Further reading
This covers only some key highlights. Check the links below for additional changes in Chrome 112.
  * [What's new in Chrome DevTools (112)](https://developer.chrome.com/blog/new-in-devtools-112)
  * [Chrome 112 deprecations and removals](https://developer.chrome.com/blog/deps-rems-112)
  * [ChromeStatus.com updates for Chrome 112](https://www.chromestatus.com/features#milestone%3D112)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/111.0.5563.53..112.0.5615.54)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
I’m Adriana Jara, and as soon as Chrome 113 is released, I'll be right here to tell you what's new in Chrome!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2023-04-04 UTC.

