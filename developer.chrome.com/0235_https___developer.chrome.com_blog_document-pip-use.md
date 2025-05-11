---
url: https://developer.chrome.com/blog/document-pip-use-case?hl=en
title: https://developer.chrome.com/blog/document-pip-use-case?hl=en
date: 2025-05-11T16:55:43.076935
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/document-pip-use-case?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/document-pip-use-case?hl=es-419)




  * On this page
  * [Browser support and progressive enhancement](https://developer.chrome.com/blog/document-pip-use-case?hl=en#browser_support_and_progressive_enhancement)
  * [Improving the learner's user experience with the Document PiP API](https://developer.chrome.com/blog/document-pip-use-case?hl=en#improving_the_learners_user_experience_with_the_document_pip_api)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  Unlock exciting use cases with the Document Picture-in-Picture API 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Browser support and progressive enhancement](https://developer.chrome.com/blog/document-pip-use-case?hl=en#browser_support_and_progressive_enhancement)
  * [Improving the learner's user experience with the Document PiP API](https://developer.chrome.com/blog/document-pip-use-case?hl=en#improving_the_learners_user_experience_with_the_document_pip_api)


Jad Joubran 
[ GitHub ](https://github.com/jadjoubran) [ Homepage ](https://jadjoubran.io/)
Published: March 4, 2025 
The [Document Picture-in-Picture API](https://developer.mozilla.org/docs/Web/API/Document_Picture-in-Picture_API) (Document PiP API) lets web applications open a floating, always-on-top window (a picture-in-picture window) that can display any arbitrary HTML content.
This API builds on top of the [Picture-in-Picture API for `<video>`](https://developer.mozilla.org/docs/Web/API/Picture-in-Picture_API), which lets you continue consuming video in a PiP window.
As the Document PiP API can display any arbitrary HTML content, you can use it to unlock exciting new use cases.
## Browser support and progressive enhancement
Browser Support
  * 116 
  * 116 


[Source](https://developer.mozilla.org/docs/Web/API/DocumentPictureInPicture)
At the time of writing, the Document Picture-in-Picture API has limited availability.
However, this shouldn't stop you from using it with [progressive enhancement](https://developer.mozilla.org/docs/Glossary/Progressive_Enhancement) or [graceful degradation](https://developer.mozilla.org/docs/Glossary/Graceful_degradation).
When planning your use case, make sure to treat it as a progressive enhancement rather than a standard feature. In this article, you'll see an example of graceful degradation.
## Improving the learner's user experience with the Document PiP API
[LearnHTMLCSS.online](https://learnhtmlcss.online/) is an interactive learning platform that teaches semantic and accessible HTML and CSS. It offers an interactive text editor and browser preview window.
The following screencast shows the layout of the app; the screen is divided into two columns. The first column contains the code editor. The second column contains a tabbed layout. By default, the user can see the instructions of the challenge, and they can click the **Browser** tab to view a live preview.
As a student, you might sometimes want to maximise the browser preview window. This is a perfect opportunity to add support for the Document Picture-in-Picture API.
To implement this, start by checking for browser support:
```
constisPipSupported="documentPictureInPicture"inwindow;

```

You can now use this variable to wrap any `documentPictureInPicture` calls, or to early return from a function that relies on Document PiP. The following code checks for support of Document PiP, then opens a Document PiP window.
```
asyncfunctioninitDocumentPip(){
if(!isPipSupported){
returnfalse;
}
constpipWindow=awaitdocumentPictureInPicture.requestWindow({
width:window.innerWidth,
height:window.innerHeight,
});
}

```

Depending on your use case, you can specify any width and height for the window. You can try to match a particular element, the current document, or even provide fixed values.
So far, you have an empty document. You now need to populate it with content.
```
// htmlCode is the HTML code of the challenge
pipWindow.document.documentElement.innerHTML=htmlCode;

```

For challenges with CSS code, you will also need to sync the CSS.
That's it! You now have a maximize button that opens in a separate PiP window.In addition to maximizing the browser preview tab, you can also move it to a separate screen if you have an external monitor, or even rearrange the main web app and the browser preview tab in a column layout.
## Fallback
Remember that this API has limited availability. On browsers and devices where this API is not supported, you'll need to provide a fallback (graceful degradation) behavior.
Instead of making the maximize button pull the whole browser preview tab out, we can make it take up all the remaining space of the current web app.
</video
Try this behavior in different browsers: <https://learnhtmlcss.online/app.html?id=2096>
Don't forget to pay attention to small details in the tooltips. When `isPipSupported` is `true`, the maximize/minimize button's tooltip toggles between _Enter Picture-in-Picture_ and _Exit Picture-in-Picture_. On the other hand, when `isPipSupported` is `false`, the fallback behavior is described with _Maximize_ and _Minimize_.
As you can see, the Document Picture-in-Picture API can unlock exciting new use cases for your Web App when combined with progressive enhancement or graceful degradation.
Don't let limited browser support limit you, and don't forget to have a decent fallback use case.
Check out the [documentation for Document PiP](https://developer.chrome.com/docs/web-platform/document-picture-in-picture) to explore various examples and use cases of this API.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-03-04 UTC.

