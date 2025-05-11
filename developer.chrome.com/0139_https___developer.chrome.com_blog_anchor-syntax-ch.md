---
url: https://developer.chrome.com/blog/anchor-syntax-changes?hl=en
title: https://developer.chrome.com/blog/anchor-syntax-changes?hl=en
date: 2025-05-11T16:53:48.703086
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/anchor-syntax-changes?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/anchor-syntax-changes?hl=es-419)




  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  Anchor positioning syntax changes 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Una Kravets 
[ Mastodon ](https://front-end.social/@una) [ Homepage ](https://una.im)
Mason Freed 
[ GitHub ](https://github.com/mfreed7)
[CSS anchor positioning](https://developer.chrome.com/blog/anchor-positioning-api) was released in Chrome **125**. This first publicly-available version of the API triggered additional discussions about the syntax . As a result of that discussion, there have been some slight changes since the feature launch. If you've already tried out CSS anchor positioning, this post explains the changes you need to make to your code, or content about anchor positioning.
There are two primary property renames that you should be aware of:
  1. `inset-area` is renamed to `position-area`. This rename was preferred by the CSS Working Group because the phrasing `position-` helps you remember that this property is applied to the positioned element, not the anchor element. This change will start in Chrome **129** , and `inset-area` is supported until Chrome **131** to give you time to update any demos or articles you have.
  2. `position-try-options` is renamed to `position-try-fallbacks`. This rename helps you remember that these are just fallbacks to the primary position, which is determined by the base styles. This change shipped with Chrome **128** , and `position-try-options` no longer works as of version **128**. We'd recommend you use the shorthand (changing it to `position-try`), which works from Chrome **125** , and has not changed.


There is also one additional behavioral change:
  * The `inset-area()`functional syntax is being removed from `position-try`. Therefore use `position-try-fallbacks: top` instead of `position-try-fallbacks: inset-area(top)`. This change will also begin in Chrome **129**.


Learn more about using anchor positioning here:
  * [Introduction post](https://developer.chrome.com/blog/anchor-positioning-api)


Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-09-04 UTC.

