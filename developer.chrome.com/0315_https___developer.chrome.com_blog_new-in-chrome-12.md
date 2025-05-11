---
url: https://developer.chrome.com/blog/new-in-chrome-127?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-127?hl=en
date: 2025-05-11T16:57:27.075251
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-127?hl=en#main-content)
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


#  New in Chrome 127 
Stay organized with collections  Save and categorize content based on your preferences. 
Adriana Jara 
[ GitHub ](https://github.com/tropicadri) [ LinkedIn ](https://www.linkedin.com/in/adrianajara) [ Mastodon ](https://hachyderm.io/@tropicadri)
Here's what you need to know:
  * [`font-size-adjust`](https://developer.chrome.com/blog/new-in-chrome-127?hl=en#font-size-adjust) helps you improve fallback fonts legibility.
  * User activations now get [propagated](https://developer.chrome.com/blog/new-in-chrome-127?hl=en#dpip-user-activation-propagation) between picture-in-picture documents and their opener.
  * [Scroll containers](https://developer.chrome.com/blog/new-in-chrome-127?hl=en#keyboard-focusable-scroll-containers) are now keyboard focusable by default.
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-127?hl=en#more).


I'm Adriana Jara. Let's dive in and see what's new for developers in Chrome 127.
## CSS `font-size-adjust`
Your site's legibility can decrease when the first-choice font-family is unavailable and its fallback font has a significantly different aspect value.
The following image shows the difference between the Verdana and Times fonts even though the text is the same size.
If your site were to fall back to the Times font it becomes a lot harder to read.
The [`font-size-adjust`](https://developer.mozilla.org/docs/Web/CSS/font-size-adjust) CSS property helps you adjust the font size of fallback fonts to keep the aspect value (height of lowercase letters divided by font size) consistent, ensuring that the text appears similar, regardless of the font used.
In the following image using font-size-adjust maintains the legibility between the Verdana and Times fonts.
```
font-size-adjust:0.545;

```

With the launch of `font-size-adjust` in Chrome this feature becomes Baseline newly available read the details in [CSS font-size-adjust is now in Baseline](https://web.dev/blog/font-size-adjust).
## Document picture-in-picture: propagate user activation
The Document Picture-in-Picture API now propagates user activations between the document picture-in-picture window and its opener.
Visit [the user gesture activation propagation demo](https://steimelchrome.github.io/document-pip/user-gesture.html) and see the changes to the page's background color when a user activation is detected. The user gesture is propagated in both contexts changing the background for both windows.
This makes user activations in a document picture-in-picture window usable inside its opener window and the other way round. This change makes using [user-activation-gated APIs](https://developer.mozilla.org/docs/Web/Security/User_activation) more ergonomic, since often event handlers in the document picture-in-picture window are actually run in the opener's context, so the opener's context needs access to the user gesture.
Visit [Picture-in-Picture for any element, not just `<video>`](https://developer.chrome.com/docs/web-platform/document-picture-in-picture) for more details.
## Keyboard focusable scroll containers.
Scroll containers becoming keyboard focusable is important to make scrollers and content within scrollers more accessible to all users.
From now on scrollers will be programmatically-focusable by default. Before this change, a scroller element could only be tab focused if the tabindex was explicitly set to 0 or higher.
Note that this behavior only happens if the scroller has no focusable children. For example, if the scroller already contains a button, then the tab focus will skip the scroller and focus on the button directly.
Accessibility best practices recommend that all features must be available using a keyboard. Keyboard focusable scrollers by default makes it easier for the user to use sequential focus navigation to access the scrollers.
Note that this change is being enabled for users very slowly over time, so we can monitor for issues caused by the change. Therefore, some users may not see this feature enabled until version 130 or even later.
See more details in [Keyboard focusable scrollers](https://developer.chrome.com/blog/keyboard-focusable-scrollers)
## And more!
Of course there's plenty more.
  * Concurrent same-document view transitions in a main frame and same-origin iframe are now available.
  * Alt text generated from [CSS content](https://developer.mozilla.org/docs/Web/CSS/content) now supports multiple arguments.
  * The [DevTools](https://developer.chrome.com/blog/new-in-devtools-127) Performance panel now captures WebSocket message events and shows them in the performance trace.


[Read the full release notes](https://developer.chrome.com/release-notes/127).
## Further reading
This covers only some key highlights. Check the following links for additional changes in Chrome 127.
  * [What's new in Chrome DevTools (127)](https://developer.chrome.com/blog/new-in-devtools-127)
  * [ChromeStatus.com updates for Chrome 127](https://chromestatus.com/features#milestone%3D127)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/126.0.6478.136..127.0.6533.58)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
Yo soy Adriana Jara, and as soon as Chrome 127 is released, I'll be right here to tell you what's new in Chrome!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-07-23 UTC.

