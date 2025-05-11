---
url: https://developer.chrome.com/blog/new-in-chrome-129?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-129?hl=en
date: 2025-05-11T16:57:28.577886
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-129?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-chrome-129?hl=es-419)




  * On this page
  * [Break up long tasks with scheduler.yield()](https://developer.chrome.com/blog/new-in-chrome-129?hl=en#yield)
  * [Animations with intrinsic sizes](https://developer.chrome.com/blog/new-in-chrome-129?hl=en#animate)
  * [Changes to CSS anchor positioning](https://developer.chrome.com/blog/new-in-chrome-129?hl=en#anchor-positioning)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  New in Chrome 129 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Break up long tasks with scheduler.yield()](https://developer.chrome.com/blog/new-in-chrome-129?hl=en#yield)
  * [Animations with intrinsic sizes](https://developer.chrome.com/blog/new-in-chrome-129?hl=en#animate)
  * [Changes to CSS anchor positioning](https://developer.chrome.com/blog/new-in-chrome-129?hl=en#anchor-positioning)


Pete LePage 
[ GitHub ](https://github.com/petele) [ Glitch ](https://glitch.com/@petele) [ Mastodon ](https://techhub.social/@petele) [ Homepage ](https://petelepage.com/)
Here's what you need to know:
  * You can [yield](https://developer.chrome.com/blog/new-in-chrome-129?hl=en#yield) in long tasks to improve performance.
  * Animate elements with [intrinsic sizes](https://developer.chrome.com/blog/new-in-chrome-129?hl=en#animate).
  * There are some changes to [anchor positioning](https://developer.chrome.com/blog/new-in-chrome-129?hl=en#anchor-positioning) syntax.
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-129?hl=en#more).


I'm Pete LePage. Let's dive in and see what's new for developers in Chrome 129.
## Break up long tasks with `scheduler.yield()`
Long tasks delay the browser's ability to respond to user input, creating a perception that a site is slow, and impacting critical performance metrics like INP. With `scheduler.yield()`, you can break up long tasks into smaller chunks, improving responsiveness by explicitly yielding back to the main thread.
It lets you tell the browser:
> "HEY! The work I'm about to do could take a while, if you need to paint a frame, respond to user input, or have other important tasks, it's OK, I can wait"
Add the following line into your JavaScript code frequently to give the browser breathing space, and avoid [INP](https://web.dev/articles/inp) issues.
```
awaitscheduler.yield();

```

Importantly, it allows continuation of your code to be prioritized so you don't lose out by yielding. We recommend liberal use of `scheduler.yield()` in functions between any larger chunks of work.
See [Optimize long tasks](https://web.dev/articles/optimize-long-tasks#scheduler-dot-yield) for more details.
## Animations with intrinsic sizes
CSS animations are pretty sweet, but they typically require explicit sizes, you _couldn't_ use the intrinsic sizing keywords like `auto`, `min-content`, or `fit-content`.
The CSS property `interpolate-size` opens up a new set of animations that weren't possible when using _intrinsic_ sizing keywords.
Without `interpolate-size`, the buttons in the following video have no transition.
After adding `interpolate-size: allow-keywords`, the buttons in the video get a beautiful transition animation effect.
Specifying `interpolate-size: allow-keywords` on the `root` element sets the new behavior for the entire page. We suggest doing this whenever compatibility isn't an issue.
```
:root{
interpolate-size:allow-keywords;
}
.item{
height:auto;
@starting-style{
height:0;
}
}

```

For finer control, the CSS `calc-size()` function, similar to `calc()`, also supports operations on exactly one of the supported intrinsic sizing keywords. When performing layout calculations, the `size` keyword evaluates to the original size of `calc-size-basis`.
```
nava{
width:80px;
overflow-x:clip;
transition:width0.35sease;
&:hover{
width:calc-size(auto,size);
}
}

```

Check out [Animate to height: auto; (and other intrinsic sizing keywords) in CSS](https://developer.chrome.com/docs/css-ui/animate-to-height-auto) for complete details.
## Changes to CSS anchor positioning
CSS anchor positioning landed in Chrome 125, but after some additional discussion within the CSS working group, there are a few changes to the spec and implementation. If you're already using CSS anchor position, you'll need to update your code as soon as possible.
First, `inset-area` has been renamed to `position-area`. This was preferred because the phrasing `position-` helps you remember that this property is applied to the positioned element, not the anchor element.
Second, `position-try-options` is renamed to `position-try-fallbacks`. This helps you remember that these are just fallbacks to the primary position, which is determined by the base styles.
Finally, the `inset-area()` functional syntax is being removed from `position-try`. Therefore use `position-try-fallbacks: top` instead of `position-try-fallbacks: inset-area(top)`.
## And more!
Of course there's plenty more.
There's a new `Intl` method for formatting durations, with support for multiple locales.
```
constl="fr-FR";
constd={hours:1,minutes:46,seconds:40};
constopts={style:"long"};
newIntl.DurationFormat(l,opts).format(d);
// "1 heure, 46 minutes et 40 secondes"

```

Web GPU canvas can now use the full range of the display for HDR images.
And there are a few deprecations and removals that may impact some developers.
[Read the full release notes](https://developer.chrome.com/release-notes/129).
## Further reading
This covers only some key highlights. Check the following links for additional changes in Chrome 129.
  * [What's new in Chrome DevTools (129)](https://developer.chrome.com/blog/new-in-devtools-129)
  * [ChromeStatus.com updates for Chrome 129](https://chromestatus.com/features#milestone%3D129)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/128.0.6613.62..129.0.6668.62)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
Filling in for Adriana, I'm Pete LePage, and as soon as Chrome 130 is released, we'll be right here to tell you what's new in Chrome!
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-09-17 UTC.

