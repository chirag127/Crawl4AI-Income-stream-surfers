---
url: https://developer.chrome.com/blog/new-in-chrome-136?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-136?hl=en
date: 2025-05-11T16:57:34.064290
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-136?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-chrome-136?hl=es-419)




  * On this page
  * [Highlights from this release](https://developer.chrome.com/blog/new-in-chrome-136?hl=en#highlights_from_this_release)
  * [RegExp.escape is now Baseline Newly available](https://developer.chrome.com/blog/new-in-chrome-136?hl=en#escape)
  * [:visited link history is now partitioned](https://developer.chrome.com/blog/new-in-chrome-136?hl=en#visited)
  * [Upgrade credentials to passkeys](https://developer.chrome.com/blog/new-in-chrome-136?hl=en#passkey-upgrade)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  New in Chrome 136 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Highlights from this release](https://developer.chrome.com/blog/new-in-chrome-136?hl=en#highlights_from_this_release)
  * [RegExp.escape is now Baseline Newly available](https://developer.chrome.com/blog/new-in-chrome-136?hl=en#escape)
  * [:visited link history is now partitioned](https://developer.chrome.com/blog/new-in-chrome-136?hl=en#visited)
  * [Upgrade credentials to passkeys](https://developer.chrome.com/blog/new-in-chrome-136?hl=en#passkey-upgrade)


Rachel Andrew 
[ GitHub ](https://github.com/rachelandrew) [ LinkedIn ](https://www.linkedin.com/in/rachelandrew) [ Mastodon ](https://front-end.social/@rachelandrew) [ Bluesky ](https://bsky.app/profile/rachelandrew.bsky.social) [ Homepage ](https://rachelandrew.co.uk)
Published: April 29, 2025 
Chrome 136 is rolling out now, and this post shares some of the key features from the release. Read the full [Chrome 136 release notes](https://developer.chrome.com/release-notes/136).
## Highlights from this release
  * Use the static [RegExp.escape](https://developer.chrome.com/blog/new-in-chrome-136?hl=en#escape) method for strings used inside a regular expression.
  * [`:visited` link history is now partitioned](https://developer.chrome.com/blog/new-in-chrome-136?hl=en#visited)
  * You can now [upgrade existing password credentials](https://developer.chrome.com/blog/new-in-chrome-136?hl=en#passkey-upgrade) to a passkey.
  * And plenty [more](https://developer.chrome.com/blog/new-in-chrome-136?hl=en#more).


## `RegExp.escape` is now Baseline Newly available
The [`RegExp.escape`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/RegExp/escape) static method has landed across all browsers within a few months, and becomes Baseline Newly available as it lands in Chrome 136.
This method escapes any potential regular expression syntax characters in a string, returning a new string that can be safely used as a literal pattern for the `RegExp()` constructor.
## `:visited` link history is now partitioned
To eliminate user browsing history leaks, anchor elements are styled as `:visited` only if they have been clicked from this top-level site and frame origin before.
By only styling links that have been clicked on this site and frame before, the many side-channel attacks that have been developed to obtain `:visited` links styling information are now obsolete. They no longer provide sites with new information about users.
Learn more about these [improvements to the privacy of `:visited` links](https://developer.chrome.com/blog/visited-links).
## Upgrade credentials to passkeys
WebAuthn Conditional Create requests let a website (known as a Relying Party or RP) create a passkey without prominent modal mediation, if the user has previously consented to credential creation.
The main use case is commonly referred to as "passkey upgrades". That is, if the browser or credential manager already stores an existing password credential for the same relying party and user, conditional create lets the website automatically create a matching passkey.
## And more!
Of course there's plenty more.
  * The `dynamic-range-limit` property enables a page to limit the maximum brightness of HDR content.
  * You can now add a tag field to speculation rules. This optional field can be used to track the source of speculation rules.
  * FecCM can now show multiple identity providers in the same dialog, by having all providers in the same `get()` call.


## Further reading
This covers only some key highlights. Check the following links for additional changes in Chrome 136.
  * [Release notes for Chrome 136](https://developer.chrome.com/release-notes/136).
  * [What's new in Chrome DevTools (136)](https://developer.chrome.com/blog/new-in-devtools-136).
  * [ChromeStatus.com updates for Chrome 136](https://chromestatus.com/features#milestone%3D136).
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule).


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video. Or follow us on X or LinkedIn for new articles and blog posts.
As soon as Chrome 137 is released, we'll be right here to tell you what's new in Chrome!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-04-29 UTC.

