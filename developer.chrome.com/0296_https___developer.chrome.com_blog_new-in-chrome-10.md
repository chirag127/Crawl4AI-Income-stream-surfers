---
url: https://developer.chrome.com/blog/new-in-chrome-104?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-104?hl=en
date: 2025-05-11T16:57:01.057640
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-104?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-chrome-104?hl=es-419)




  * On this page
  * [Specify a crop area with region capture](https://developer.chrome.com/blog/new-in-chrome-104?hl=en#region-capture)
  * [Easier media queries with level 4 syntax and evaluation](https://developer.chrome.com/blog/new-in-chrome-104?hl=en#mq-math)
  * [Shared Element Transitions start new origin trial](https://developer.chrome.com/blog/new-in-chrome-104?hl=en#shared-element-transitions)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  New in Chrome 104 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Specify a crop area with region capture](https://developer.chrome.com/blog/new-in-chrome-104?hl=en#region-capture)
  * [Easier media queries with level 4 syntax and evaluation](https://developer.chrome.com/blog/new-in-chrome-104?hl=en#mq-math)
  * [Shared Element Transitions start new origin trial](https://developer.chrome.com/blog/new-in-chrome-104?hl=en#shared-element-transitions)


Pete LePage 
[ GitHub ](https://github.com/petele) [ Glitch ](https://glitch.com/@petele) [ Mastodon ](https://techhub.social/@petele) [ Homepage ](https://petelepage.com/)
Here's what you need to know:
  * You can now specify a crop area using [region capture](https://developer.chrome.com/blog/new-in-chrome-104?hl=en#region-capture) when using `getDisplayMedia()` to capture the current tab.
  * Media query syntax can be written using [mathematical comparison operators](https://developer.chrome.com/blog/new-in-chrome-104?hl=en#mq-math).
  * [Shared Element Transitions](https://developer.chrome.com/blog/new-in-chrome-104?hl=en#shared-element-transitions) starts an origin trial.
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-104?hl=en#more).


I'm [Pete LePage](https://petelepage.com). Let's dive in and see what's new for developers in Chrome 104.
## Specify a crop area with region capture
`getDisplayMedia()` makes it possible to create a video stream from the current tab. But, there are times when you don’t want the entire tab, only a small portion of it. Until now, the only way to do that was to manually crop each video frame.
With Region Capture, a web app can define the specific area of the screen it wants to share. For example, Google Slides could allow you to stay in the standard editing view, and share the current slide.
The main content area is in blue and the cross-origin iframe is in red. 
To use it, select the element to share, then create a new `CropTarget` based on that element. Next, start screen sharing by calling `getDisplayMedia()`. That prompts the user for permission to share their screen. Then, call `track.cropTo()` and pass the `cropTarget` created earlier.
```
constelem=document.querySelector("#main");
constcropTarget=awaitCropTarget.fromElement(elem);
conststream=awaitnavigator.mediaDevices
.getDisplayMedia({preferCurrentTab:true});
const[track]=stream.getVideoTracks();
awaittrack.cropTo(cropTarget);

```

Check out [Better tab sharing with Region Capture](https://developer.chrome.com/docs/web-platform/region-capture) for more details.
## Easier media queries with level 4 syntax and evaluation
Media Queries are critical to responsive design, allowing you to define specific styles for different viewport sizes. But, unless you use them every single day, the syntax can be a little confusing.
Chrome 104 adds support for [Media Queries - Level 4 - Syntax and Evaluation](https://www.w3.org/TR/mediaqueries-4/#mq-range-context), allowing you to write media queries using ordinary mathematical comparison operators.
So instead of something like this to indicate a viewport between 400 and 600 pixels:
```
@media(min-width:400px)and(max-width:600px){
/* Styles for viewports between 400px and 600px. */
}

```

It can be written like this:
```
@media(400px<=width<=600px){
/* Styles for viewports between 400px and 600px. */
}

```

In addition to making media queries less verbose, the new syntax can be more accurate. The `min-` and `max-` queries are inclusive, for example: `min-width: 400px` tests for a width of 400px or greater. The new syntax allows you to be more explicit about what you mean.
```
@media(width400px){
/* Styles for viewports less than 400px. */
}
@media(400px<=width<=600px){
/* Styles for viewports between 400px and 600px. */
}
@media(601px<=width<=1000px){
/* Styles for viewports between 601px and 1000px. */
}

```

It's already supported in Firefox, and there’s a [PostCSS plugin](https://github.com/postcss/postcss-media-minmax) that will re-write the new syntax to the old syntax, ensuring browser compatibility!
Check out Rachel’s article [New syntax for range media queries in Chrome 104](https://developer.chrome.com/blog/media-query-range-syntax) for more details.
## Shared Element Transitions start new origin trial
Platform specific apps typically have smooth transitions between different views, they look beautiful, they keep the user in context, and they help the experience feel more performant. Whereas on the web, a full navigation can be harsh, and sometimes means a momentary blank screen. For a single page app, it can be better, but transitions are still hard.
Shared Element Transitions, starting a new [origin trial](https://developer.chrome.com/origintrials#/view_trial/1762033354208706561) in Chrome 104, allows you to provide smooth transitions, regardless of whether the transitions are cross-document (for example in a multi-page app), or intra-document (for example in a single page app).
Here’s a rough example of how transitions work for a single page app. In the navigate function, get the new page content, then check to see if transitions are supported, if not, update the page without a transition. If they are, create a `transition()` and call `start()` on it, letting the API know when the DOM change is complete.
```
asyncfunctionspaNavigate(path){
// Get new page content.
constdata=awaitfetchPage(path);
// Check if transitions are supported, if not, use classic method.
if(!document.createDocumentTransition){
awaitupdateDOM(data);
return;
}
// Create transition
consttransition=document.createDocumentTransition();
// Start transition, let API know when DOM change is complete.
transition.start(()=>updateDOM(data));
}

```

Under the hood, Shared Element Transitions uses CSS Animations, so you can change from a fade in effect, to slide in, or whatever you want.
I’ve just scratched the surface, so check out Jake’s video [Bringing Page Transitions to the Web](https://www.youtube.com/watch?v=JCJUPJ_zDQ4), or dive into the [explainer](https://github.com/WICG/shared-element-transitions/blob/main/explainer.md).
## And more!
Of course there's plenty more.
  * When cookies are set with an explicit `Expires` or `Max-Age` attribute, the value will now be capped to no more than 400 days.
  * There are enhancements to the multi-screen window placement API.
  * And the `overflow-clip-margin` CSS property specifies how far an element's content is allowed to paint before being clipped.


## Further reading
This covers only some of the key highlights. Check the links below for additional changes in Chrome 104.
  * [What's new in Chrome DevTools (104)](https://developer.chrome.com/blog/new-in-devtools-104)
  * [Chrome 104 deprecations and removals](https://developer.chrome.com/blog/deps-rems-104)
  * [ChromeStatus.com updates for Chrome 104](https://www.chromestatus.com/features#milestone%3D104)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/103.0.5060.60..104.0.5112.84)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
I'm Pete LePage, and as soon as Chrome 105 is released, I'll be right here to tell you what's new in Chrome!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2022-08-02 UTC.

