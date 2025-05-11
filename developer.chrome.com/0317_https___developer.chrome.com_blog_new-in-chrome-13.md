---
url: https://developer.chrome.com/blog/new-in-chrome-130?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-130?hl=en
date: 2025-05-11T16:57:28.571373
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-130?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-chrome-130?hl=es-419)




  * On this page
  * [Document Picture-in-Picture](https://developer.chrome.com/blog/new-in-chrome-130?hl=en#dpip)
  * [CSS nested declarations](https://developer.chrome.com/blog/new-in-chrome-130?hl=en#cssnest)
  * [box-decoration-break](https://developer.chrome.com/blog/new-in-chrome-130?hl=en#bdb)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  New in Chrome 130 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Document Picture-in-Picture](https://developer.chrome.com/blog/new-in-chrome-130?hl=en#dpip)
  * [CSS nested declarations](https://developer.chrome.com/blog/new-in-chrome-130?hl=en#cssnest)
  * [box-decoration-break](https://developer.chrome.com/blog/new-in-chrome-130?hl=en#bdb)


Pete LePage 
[ GitHub ](https://github.com/petele) [ Glitch ](https://glitch.com/@petele) [ Mastodon ](https://techhub.social/@petele) [ Homepage ](https://petelepage.com/)
Here's what you need to know:
  * [Document picture in picture](https://developer.chrome.com/blog/new-in-chrome-130?hl=en#dpip) gives you more control over picture-in-picture windows.
  * [CSS Nested declarations](https://developer.chrome.com/blog/new-in-chrome-130?hl=en#cssnest) fix some tricky edge cases.
  * You can specify the behavior of [decorations on elements](https://developer.chrome.com/blog/new-in-chrome-130?hl=en#bdb) that split across multiple lines.
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-130?hl=en#more).


I'm Pete LePage. Let's dive in and see what's new for developers in Chrome 130.
## Document Picture-in-Picture
The picture-in-picture API is great when you want to pop a video out of a browser tab so you can keep an eye on the video while interacting with other sites or applications. But it only does video.
The document picture-in-picture API eliminates that restriction, allowing you to create a picture-in-picture window where you have control over the content. It's great for things like custom video players, video conferencing, and productivity apps. I love what Spotify has done with it in their web player. I get a window with the artwork for the current song, play controls, and can easily add the song to my favorites.
To use it, request a new document picture-in-picture window. The returned `promise` resolves with a Picture-in-Picture window JavaScript object. Then, use that to add your content to the window.
```
asyncfunctionopenDPiP(){
constplayer=document.querySelector("#player");
constpipWindow=awaitdocumentPictureInPicture
.requestWindow();
pipWindow.document.body.append(player);
}
pipButton.addEventListener('click',openDPiP);

```

With the new `preferInitialWindowPlacement` property, you can tell Chrome to always open the picture-in-picture window in its default position and size, instead of reusing the position or size of the previous window.
```
// Open a Picture-in-Picture window in its default position / size.
constpipWindow=awaitdocumentPictureInPicture.requestWindow({
preferInitialWindowPlacement:true,
});

```

Check out François' post [Picture-in-Picture for any Element](https://developer.chrome.com/docs/web-platform/document-picture-in-picture) for lots more details!
## CSS nested declarations
[CSS nesting](https://developer.mozilla.org/docs/Web/CSS/CSS_nesting/Using_CSS_nesting) allows for shorter selectors, easier reading, and more modularity by nesting rules inside others. CSS Nesting is [Baseline Newly available](https://webstatus.dev/features/nesting?q=nesting), and it's been available for almost a year.
There were a few edge cases that didn't work as expected. For example, with the following CSS block, you would expect the background color to be green, since it comes last, but it's red!
```
.foo{
width:fit-content;
@mediascreen{
background-color:red;
}
background-color:green;
}

```

To fix edge cases like this, the CSS working group introduced the nested declarations rule, which is implemented in Chrome 130. Now, that same CSS block results in a green background, as expected. If you were interleaving bare declarations with nested rules, you should double check your code.
Check out Bramus' article [CSS nesting improves with `CSSNestedDeclarations`](https://web.dev/blog/css-nesting-cssnesteddeclarations) for a more in-depth explanation.
## `box-decoration-break`
The `box-decoration-break` CSS property lets you specify how an element's fragments should be rendered when broken across multiple lines, columns, or pages.
For example, this element looks great when everything is on one line.
When the content gets split across multiple lines, decorations like background, box shadow, border, and so on are sliced, creating a rather drastic look.
By adding `box-decoration-break: clone`, each fragment is rendered independently, creating a much nicer look.
While it's not quite Baseline, it's available in Chrome and Firefox, and is vendor prefixed in Safari.
```
.bdb-clone{
-webkit-box-decoration-break:clone;
box-decoration-break:clone;
}

```

Check out the [`box-decoration-break` docs on MDN](https://developer.mozilla.org//docs/Web/CSS/box-decoration-break) and Rachel's post [The box-decoration-break property in Chrome 130](https://developer.chrome.com/blog/box-decoration-break) for more details.
## And more!
Of course there's plenty more.
  * After a few false starts, [keyboard focusable scroll containers](https://developer.chrome.com/blog/keyboard-focusable-scrollers) are finally landing.
  * WebGPU gets dual source blending.
  * And web serial gets a connected attribute.


## Further reading
This covers only some key highlights. Check the following links for additional changes in Chrome 130.
  * [Release notes for Chrome 130](https://developer.chrome.com/release-notes/130).
  * [What's new in Chrome DevTools (130)](https://developer.chrome.com/blog/new-in-devtools-130)
  * [ChromeStatus.com updates for Chrome 130](https://chromestatus.com/features#milestone%3D130)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/129.0.6668.62..130.0.6723.53)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
I'm Pete LePage, and as soon as Chrome 131 is released, we'll be right here to tell you what's new in Chrome!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-10-15 UTC.

