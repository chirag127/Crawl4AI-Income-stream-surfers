---
url: https://developer.chrome.com/blog/keyboard-lock-pointer-lock-permission?hl=en
title: https://developer.chrome.com/blog/keyboard-lock-pointer-lock-permission?hl=en
date: 2025-05-11T16:56:32.445569
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/keyboard-lock-pointer-lock-permission?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/keyboard-lock-pointer-lock-permission?hl=es-419)

Sign in


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  The Keyboard Lock and the Pointer Lock APIs require permission from Chrome 131 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Thomas Steiner 
[ GitHub ](https://github.com/tomayac) [ Glitch ](https://glitch.com/@tomayac) [ LinkedIn ](https://www.linkedin.com/in/thomassteinerlinkedin) [ Mastodon ](https://toot.cafe/@tomayac) [ Bluesky ](https://bsky.app/profile/tomayac.com) [ Homepage ](https://blog.tomayac.com/)
The [Keyboard Lock API](https://developer.mozilla.org/docs/Web/API/Keyboard/lock) lets developers provide an immersive, full screen experience for a variety of use cases, including interactive websites, games, and remote desktop or application streaming. It does so by enabling websites to use all available keys allowed by the host operating system.
The [Pointer Lock API](https://developer.mozilla.org/docs/Web/API/Pointer_Lock_API) lets a desktop application hide the pointer icon and interpret mouse motion for something else, like looking around in a 3D world.
From Chrome 131, using either of these two APIs requires permission. You can _check_ for permission as shown in the following snippets:
```
const{state}=awaitnavigator.permissions.query({name:'pointer-lock'});
if(state==='granted'){
// The Pointer Lock API can be used.
}

```
```
const{state}=awaitnavigator.permissions.query({name:'keyboard-lock'});
if(state==='granted'){
// The Keyboard Lock API can be used.
}

```

There's no explicit need to _ask_ for permission. If permission wasn't granted before, the browser will show a permission prompt upon the first request to lock the pointer or the keyboard.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-09-10 UTC.

