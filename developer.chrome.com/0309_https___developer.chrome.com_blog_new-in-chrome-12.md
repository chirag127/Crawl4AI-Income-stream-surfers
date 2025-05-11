---
url: https://developer.chrome.com/blog/new-in-chrome-121?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-121?hl=en
date: 2025-05-11T16:57:18.007887
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-121?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-chrome-121?hl=es-419)




  * On this page
  * [Speculation Rules API updates](https://developer.chrome.com/blog/new-in-chrome-121?hl=en#speculation-rules-api)
  * [Element Capture API origin trial](https://developer.chrome.com/blog/new-in-chrome-121?hl=en#capture-element-api)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  New in Chrome 121 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Speculation Rules API updates](https://developer.chrome.com/blog/new-in-chrome-121?hl=en#speculation-rules-api)
  * [Element Capture API origin trial](https://developer.chrome.com/blog/new-in-chrome-121?hl=en#capture-element-api)


Adriana Jara 
[ GitHub ](https://github.com/tropicadri) [ LinkedIn ](https://www.linkedin.com/in/adrianajara) [ Mastodon ](https://hachyderm.io/@tropicadri)
Here's what you need to know:
  * Add a unique touch to your text with `font-palette` animation and other [CSS updates](https://developer.chrome.com/blog/new-in-chrome-121?hl=en#css-updates).
  * There are improvements to the [Speculation Rules API](https://developer.chrome.com/blog/new-in-chrome-121?hl=en#speculation-rules-api).
  * You can try the [Element Capture API](https://developer.chrome.com/blog/new-in-chrome-121?hl=en#capture-element-api) in an origin trial.
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-121?hl=en#more).


I'm Adriana Jara. Let's dive in and see what's new for developers in Chrome 121.
## CSS updates.
Let's start with CSS updates:
The properties [`scrollbar-color`](https://developer.mozilla.org/docs/Web/CSS/scrollbar-color) and [`scrollbar-width`](https://developer.mozilla.org/docs/Web/CSS/scrollbar-width) are now available. With them you can customize scrollbars and change—as you probably guessed—[their color and width](https://developer.chrome.com/docs/css-ui/scrollbar-styling).
The [`font-palette`](https://developer.mozilla.org/docs/Web/CSS/font-palette) property lets you select a specific palette to render a [color font](https://developer.chrome.com/blog/colrv1-fonts). This property now supports animation, so switching between palettes becomes a smooth transition between the two selected palettes.
The pseudo-elements [`::spelling-error`](https://developer.mozilla.org/docs/Web/CSS/::spelling-error) and [`::grammar-error`](https://developer.mozilla.org/docs/Web/CSS/::grammar-error) let you customize colors for the spelling and grammar errors, highlight misspelled words with background colors or other decorations, and implement custom spell checking with a more integrated appearance.
CSS masking for SVG is improved, this is a follow-up on to the improved CSS mask support in Chrome 120, adding new mask support to SVG (multiple masks, as well as `mask-mode`, `mask-composite`, `mask-position`, and `mask-repeat`). In addition, remote SVG masks (for example, mask: `url(masks.svg#star)`) are now supported.
_Correction: A previous version of this article mentioned adding support for`supports()` conditions to `@import`, which was not the case. The change is included in Chrome 122._
## Speculation Rules API updates
Sites can use the [Speculation Rules API](https://developer.mozilla.org/docs/Web/API/Speculation_Rules_API), to programmatically tell Chrome which pages to prerender, creating a better user experience by reducing page navigation time.
Now the API includes support for [document rules](https://wicg.github.io/nav-speculation/speculation-rules.html#document-rule-predicate): they are an extension to the speculation rules syntax that lets the browser obtain the list of URLs for speculative loading from elements in a page. Document rules may include criteria for which of these links can be used. This, coupled with a new ["eagerness"](https://wicg.github.io/nav-speculation/speculation-rules.html#valid-eagerness-strings) field lets you automatically prefetch or prerender links on pages immediately, on hover or on mouse down.
Here is a document rules example:
```
{
"prerender":[
{"where":{"and":[
{"href_matches":"/*"},
{"not":{"href_matches":"/logout"}},
{"not":{"selector_matches":".no-prerender"}}
]}}
]
}

```

A separate change allows specifying speculation rules using the Speculation-Rules HTTP response header. The header is an alternative to using inline `<script>` elements. The value of this header must be a URL pointing to a text resource with `"application/speculationrules+json"` MIME type. The resource's rules will be added to the document's rule set.
Also, the [`No-Vary-Search`](https://github.com/WICG/nav-speculation/blob/main/no-vary-search.md#-preloading-caches) hint enables speculative prefetches to match even if URL query parameters change. The `No-Vary-Search` HTTP response header declares that some or all parts of a URL's query can be ignored for matching purposes. It can declare that the order of query parameter keys shouldn't prevent matches, that specific query parameters shouldn't prevent matches, or that only certain known query parameters should cause mismatches.
Visit [ Improvements to the Speculation Rules API](https://developer.chrome.com/blog/speculation-rules-improvements) for more information on these changes.
## Element Capture API origin trial
The Element Capture API is available in an origin trial. This API lets you capture and record a specific HTML element. It transforms a capture of the entire tab, into a capture of a specific DOM subtree, capturing only direct descendants of the target-element. In other words, it crops and removes both occluding and occluded content.
An example of where the Element Capture API is useful is a video-conferencing app that lets you embed third-party applications in an iframe. In this scenario, you might want to capture that iframe as a video and transmit it to remote participants.
Elad uses a third-party application in a video-conferencing call with François.
Note that you could use [Region Capture](https://developer.chrome.com/web-platform/region-capture) to do that, but in that case if some content, like a drop-down list, draws on top of the content that's selected, that drop-down will be part of the recording.
Elad's drop-down list shows up on top of the content received by François.
The Element Capture API solves this problem, by letting you target the element you want to share.
François does not see the drop-down list from Elad.
Checkout [Capture a video stream from any element](https://developer.chrome.com/docs/web-platform/element-capture) for code samples and [register for the ElementCapture origin trial](https://developer.chrome.com/origintrials#/register_trial/1946117988977475585)
## And more!
Of course there's plenty more.
  * The `resizeBy()` and `resizeTo()` methods, part of the [Document Picture-in-Picture API](https://developer.mozilla.org/docs/Web/API/Document_Picture-in-Picture_API), now require a user gesture.
  * You can programmatically open the option picker of a `<select>` element with the [`showPicker()`](https://developer.mozilla.org/docs/Web/API/HTMLSelectElement/showPicker) method of `HTMLSelectElement`.
  * [`scope_extensions`](https://developer.chrome.com/docs/capabilities/scope-extensions), is in [origin trial](https://developer.chrome.com/origintrials#/view_trial/3889984178141265921), it allows expanding a web app's behaviors to include other origins, if there is agreement between the primary origin of a web app and the associated origins.


## Further reading
This covers only some key highlights. Check the following links for additional changes in Chrome 121.
  * [What's new in Chrome DevTools (121)](https://developer.chrome.com/blog/new-in-devtools-121)
  * [Chrome 121 deprecations and removals](https://developer.chrome.com/blog/deps-rems-121)
  * [ChromeStatus.com updates for Chrome 121](https://chromestatus.com/features#milestone%3D121)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/120.0.6099.268..121.0.6167.106)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
Yo soy Adriana Jara, and as soon as Chrome 122 is released, I'll be right here to tell you what's new in Chrome!
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-01-23 UTC.

