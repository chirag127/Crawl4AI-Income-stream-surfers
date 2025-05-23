---
url: https://developer.chrome.com/blog/new-in-chrome-116?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-116?hl=en
date: 2025-05-11T16:57:13.172464
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-116?hl=en#main-content)


  * On this page
  * [Document Picture-in-Picture API.](https://developer.chrome.com/blog/new-in-chrome-116?hl=en#document-picture-in-picture)
  * [DevTools missing stylesheets debugging improvements.](https://developer.chrome.com/blog/new-in-chrome-116?hl=en#missing-stylesheets-debug)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  New in Chrome 116 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Document Picture-in-Picture API.](https://developer.chrome.com/blog/new-in-chrome-116?hl=en#document-picture-in-picture)
  * [DevTools missing stylesheets debugging improvements.](https://developer.chrome.com/blog/new-in-chrome-116?hl=en#missing-stylesheets-debug)


Adriana Jara 
[ GitHub ](https://github.com/tropicadri) [ LinkedIn ](https://www.linkedin.com/in/adrianajara) [ Mastodon ](https://hachyderm.io/@tropicadri)
Here's what you need to know:
  * Use the [Document Picture in Picture API](https://developer.chrome.com/blog/new-in-chrome-116?hl=en#document-picture-in-picture) to increase user productivity.
  * It is now easier to [debug missing stylesheets](https://developer.chrome.com/blog/new-in-chrome-116?hl=en#missing-stylesheets-debug) in DevTools
  * And there’s plenty [more](https://developer.chrome.com/blog/new-in-chrome-116?hl=en#more).


I’m Adriana Jara. Let’s dive in and see what’s new for developers in Chrome 116.
## Document Picture-in-Picture API.
The Document Picture-in-Picture API makes it possible to open an always-on-top window that can be populated with arbitrary HTML content.
A Picture-in-Picture window created with the Document Picture-in-Picture API ([demo](https://document-picture-in-picture-api.glitch.me/)).
The Picture-in-Picture window in the Document Picture-in-Picture API is similar to a blank same-origin window opened using `window.open()`, with some differences:
  * The Picture-in-Picture window floats on top of other windows.
  * The Picture-in-Picture window never outlives the opening window.
  * The Picture-in-Picture window cannot be navigated.
  * The Picture-in-Picture window position cannot be set by the website.


The following HTML sets up a custom video player and a button element to open the video player in a Picture-in-Picture window.
```
<div id="playerContainer">
 <div id="player">
  <video id="video"></video>
 </div>
</div>
<button id="pipButton">Open Picture-in-Picture window</button>

```

The following JavaScript calls `documentPictureInPicture.requestWindow()` when the user clicks the button to open a blank Picture-in-Picture window. The returned promise resolves with a Picture-in-Picture window JavaScript object. The video player is moved to that window using `append()`.
```
pipButton.addEventListener('click',async()=>{
constplayer=document.querySelector("#player");
// Open a Picture-in-Picture window.
constpipWindow=awaitdocumentPictureInPicture.requestWindow();
// Move the player to the Picture-in-Picture window.
pipWindow.document.body.append(player);
});

```

Check out [Picture-in-picture for any element](https://developer.chrome.com/docs/web-platform/document-picture-in-picture) for more details and examples.
## DevTools missing stylesheets debugging improvements.
DevTools got a number of improvements to identify and debug issues with missing stylesheets.
First: the **Sources > Page** tree now shows only the successfully deployed and loaded stylesheets to minimize confusion.
Also the **Sources > Editor** now underlines and shows inline error tooltips next to failed, `@import`,`url()`, and `href` statements.
  * The **Console** , in addition to links to failed requests, now provides links to the exact line that references a stylesheet that failed to load.


The **Network panel** consistently populates the **Initiator** column with links to the exact line that references a stylesheet that failed to load.
The **Issues panel** lists all stylesheets loading issues, including broken URLs, failed requests, and misplaced `@import` statements.
Check out [what’s new in DevTools](https://developer.chrome.com/blog/new-in-devtools-116) for all the details and more information on DevTools in Chrome 116.
## And more!
Of course there’s plenty more.
  * [Motion path](https://developer.mozilla.org/docs/Web/CSS/CSS_motion_path) allows authors to position any graphical object and animate it along a path specified by the developer.
  * The `display` and `content-visibility` properties are now supported in keyframe animations, which allows exit animations to be added purely in CSS.
  * The fetch API can now be used with [Bring Your Own Buffer readers](https://developer.mozilla.org/docs/Web/API/ReadableStreamBYOBReader), reducing garbage collection overhead and copies, and improving responsiveness for users.


## Further reading
This covers only some key highlights. Check the links below for additional changes in Chrome 116.
  * [What's new in Chrome DevTools (116)](https://developer.chrome.com/blog/new-in-devtools-116)
  * [Chrome 116 deprecations and removals](https://developer.chrome.com/blog/deps-rems-116)
  * [ChromeStatus.com updates for Chrome 116](https://chromestatus.com/features#milestone%3D116)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/115.0.5790.181..116.0.5845.87)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
Yo soy Adriana Jara, and as soon as Chrome 117 is released, I'll be right here to tell you what's new in Chrome!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2023-08-15 UTC.

