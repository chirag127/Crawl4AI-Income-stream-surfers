---
url: https://developer.chrome.com/blog/new-in-chrome-105?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-105?hl=en
date: 2025-05-11T16:57:01.025887
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-105?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-chrome-105?hl=es-419)




  * On this page
  * [Container queries and the :has() CSS property](https://developer.chrome.com/blog/new-in-chrome-105?hl=en#container-queries)
    * [CSS :has() pseudo-class](https://developer.chrome.com/blog/new-in-chrome-105?hl=en#css_has_pseudo-class)
  * [Deprecating Web SQL for non-secure contexts](https://developer.chrome.com/blog/new-in-chrome-105?hl=en#web-sql-deprecation)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  New in Chrome 105 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Container queries and the :has() CSS property](https://developer.chrome.com/blog/new-in-chrome-105?hl=en#container-queries)
    * [CSS :has() pseudo-class](https://developer.chrome.com/blog/new-in-chrome-105?hl=en#css_has_pseudo-class)
  * [Deprecating Web SQL for non-secure contexts](https://developer.chrome.com/blog/new-in-chrome-105?hl=en#web-sql-deprecation)


Pete LePage 
[ GitHub ](https://github.com/petele) [ Glitch ](https://glitch.com/@petele) [ Mastodon ](https://techhub.social/@petele) [ Homepage ](https://petelepage.com/)
Here's what you need to know:
  * [Container queries and :has()](https://developer.chrome.com/blog/new-in-chrome-105?hl=en#container-queries) are a match made in responsive heaven.
  * The new [Sanitizer API](https://developer.chrome.com/blog/new-in-chrome-105?hl=en#sanitizer-api) provides a robust processor for arbitrary strings to help reduce cross site scripting vulnerabilities.
  * We’re taking another step towards [deprecating Web SQL](https://developer.chrome.com/blog/new-in-chrome-105?hl=en#web-sql-deprecation).
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-105?hl=en#more).


I'm [Pete LePage](https://petelepage.com). Let's dive in and see what's new for developers in Chrome 105.
## Container queries and the `:has()` CSS property
Container queries, one of the most highly requested features are landing in Chrome 105. They enable developers to query a parent selector for its size and styling information, making it possible for a child element to own its responsive styling logic, no matter where it lives on a page.
They’re similar to a @media query, except they evaluate against the size of a container instead of the size of the viewport.
To use container queries, you need to set containment on a parent element. For example, you might have a card with an image and some text.
To create a container query, set `container-type` on the card container. Setting `container-type` to `inline-size` queries the `inline-direction` size of the parent.
```
.card-container{
container-type:inline-size;
}

```

Now, we can use that container to apply styles to any of its children using `@container`.
```
.card{
display:grid;
grid-template-columns:1fr1fr;
}
@container(max-width:400px){
.card{
grid-template-columns:1fr;
}
}

```

In this case, when the _container_ is less than 400px, it switches to a single column layout.
### CSS `:has()` pseudo-class
We can take this a step further with the CSS `:has()` pseudo-class. It allows you to check if a parent element contains children with specific parameters.
For example, `p:has(span)` indicates a paragraph selector with a span inside of it. You can use this to style the parent paragraph itself, or anything within it. Or, you can use `figure:has(figcaption)` to style a figure element that contains a caption.
```
p:has(span){
/* magic styles */
}
figure:has(figcaption){
/* this figure has a figcaption */
}

```

Check out Una’s article [@container and :has(): two powerful new responsive APIs](https://developer.chrome.com/blog/has-with-cq-m105) for a more detailed explanation and some fun demos.
## Sanitizer API
Most web apps frequently deal with untrusted strings, but safely rendering that content can be tricky. Without sufficient care, it's easy to accidentally create opportunities for cross-site scripting vulnerabilities.
There are libraries like [DomPurify](https://github.com/cure53/DOMPurify) that help, but add a small maintenance burden. The HTML Sanitizer API helps to reduce the number of cross-site scripting vulnerabilities by building sanitization into the platform.
To use it, create a new instance of Sanitizer. Then, call `setHTML()` on the element you want to insert the sanitized content into.
```
constmySanitizer=newSanitizer();
constuser_input=`<img src="" onerror=alert(0)>`;
elem.setHTML(user_input,{sanitizer:mySanitizer});

```

The Sanitizer API is designed to be safe by default and customizable, allowing you to specify different config options, for example dropping certain elements, or allowing others.
```
constconfig={
allowElements:[],
blockElements:[],
dropElements:[],
allowAttributes:{},
dropAttributes:{},
allowCustomElements:true,
allowComments:true
};
// sanitized result is customized by configuration
constmySanitizer=newSanitizer(config);

```

Check out [Safe DOM manipulation with the Sanitizer API](https://web.dev/sanitizer/) for more details.
## Deprecating Web SQL for non-secure contexts
Some time ago, we announced our plans to deprecate Web SQL. Starting in Chrome 105, Web SQL will be deprecated in _non-secure_ contexts.
If you’re using Web SQL in non-secure contexts, you should migrate to IndexDB, or another local storage container as soon as possible.
## And more!
Of course there's plenty more.
  * You can now update the name of an installed PWA on both desktop and mobile by updating the web app manifest.
  * The multi-screen window placement API gets accurate screen name labels.
  * The window controls overlay API is now available. It lets PWAs provide a more app-like feel by swapping the existing full-width title bar for a small overlay. This allows you to place custom content in the title bar area.


## Further reading
This covers only some of the key highlights. Check the links below for additional changes in Chrome 105.
  * [What's new in Chrome DevTools (105)](https://developer.chrome.com/blog/new-in-devtools-105)
  * [Chrome 105 deprecations and removals](https://developer.chrome.com/blog/deps-rems-105)
  * [ChromeStatus.com updates for Chrome 105](https://www.chromestatus.com/features#milestone%3D105)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/104.0.5112.84..105.0.5195.74)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
I'm Pete LePage, and as soon as Chrome 106 is released, we'll be right here to tell you what's new in Chrome!
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2022-08-30 UTC.

