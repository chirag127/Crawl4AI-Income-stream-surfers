---
url: https://developer.chrome.com/blog/new-in-chrome-132?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-132?hl=en
date: 2025-05-11T16:57:33.460954
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-132?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-chrome-132?hl=es-419)

Sign in


  * On this page
  * [Dialog element toggle events](https://developer.chrome.com/blog/new-in-chrome-132?hl=en#dialog-toggle)
  * [Element capture](https://developer.chrome.com/blog/new-in-chrome-132?hl=en#elem-capture)
  * [The File System Access API on Android and WebView](https://developer.chrome.com/blog/new-in-chrome-132?hl=en#fs-access-android-webview)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  New in Chrome 132 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Dialog element toggle events](https://developer.chrome.com/blog/new-in-chrome-132?hl=en#dialog-toggle)
  * [Element capture](https://developer.chrome.com/blog/new-in-chrome-132?hl=en#elem-capture)
  * [The File System Access API on Android and WebView](https://developer.chrome.com/blog/new-in-chrome-132?hl=en#fs-access-android-webview)


Pete LePage 
[ GitHub ](https://github.com/petele) [ Glitch ](https://glitch.com/@petele) [ Mastodon ](https://techhub.social/@petele) [ Homepage ](https://petelepage.com/)
Here's what you need to know:
  * [Dialog element ToggleEvent](https://developer.chrome.com/blog/new-in-chrome-132?hl=en#dialog-toggle) lets you know when a `<dialog>` has opened or closed.
  * [Capture specific elements](https://developer.chrome.com/blog/new-in-chrome-132?hl=en#elem-capture) for video sharing.
  * The File System Access API is now available on [Android and in WebViews](https://developer.chrome.com/blog/new-in-chrome-132?hl=en#fs-access-android-webview)
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-132?hl=en#more).


I'm Pete LePage. Let's dive in and see what's new for developers in Chrome 132.
## Dialog element toggle events
The [`<dialog>` element](https://web.dev/learn/html/dialog) is a useful element for representing any kind of dialog in HTML. It's Baseline Widely available, which means it works across all browsers. Unfortunately, the initial implementation didn't include a direct way to detect when a dialog opens or closes.
Starting in Chrome 132, there's a new `ToggleEvent`. It incorporates the same [`ToggleEvent` that is dispatched by a `popover`](https://developer.mozilla.org/docs/Web/API/ToggleEvent). For `<dialog>` elements, when `showModal` or `show` is called, the `<dialog>` dispatches a `ToggleEvent` with `newState=open`. When a `<dialog>` is closed (using a form, button or `closewatcher`) it dispatches a `ToggleEvent` with `newState=closed`.
```
constdialog=document.getElementById("myDialog");
// Fired just before dialog is shown/hidden
dialog.addEventListener("beforetoggle",(event)=>{
if(event.newState==="open"){
console.log("Dialog is about to be shown");
}else{
console.log("Dialog is about to be hidden");
}
});
// Fired just after dialog is shown/hidden
dialog.addEventListener("toggle",(event)=>{
if(event.newState==="open"){
console.log("Dialog is now visible");
}else{
console.log("Dialog is now hidden");
}
});

```

## Element capture
The web platform allows a web app to capture a video track of the current tab, or [region](https://developer.chrome.com/docs/web-platform/region-capture), and starting in Chrome 132, web apps can [capture an element](https://developer.chrome.com/docs/web-platform/element-capture). This is especially useful when elements are positioned in a way that they may overlap one another.
```
constmyElem=document.getElementById('elementToShare');
// Request screen sharing
conststream=awaitnavigator.mediaDevices
.getDisplayMedia({preferCurrentTab:true});
const[videoTrack]=stream.getVideoTracks();
// Restrict the video stream to myElem and its subtree
constrestrictionTarget=awaitRestrictionTarget.fromElement(myElem);
awaitvideoTrack.restrictTo(restrictionTarget);
// Set the video source to my newly restricted stream
video.srcObject=stream;

```

Check out the [demo](https://element-capture-demo.glitch.me/).
## The File System Access API on Android and WebView
The [File System Access API](https://developer.chrome.com/docs/capabilities/web-apis/file-system-access) has been available on Chrome Desktop for some time now, and allows web apps to interact with files on the users local file system. From Chrome 132, the API is now available on Android and in WebViews.
To read a file call `showOpenFilePicker()`, which shows a file picker, then returns a file handle that you can use to read the file. To save a file to disk, you can either use that file handle that you got earlier, or call `showSaveFilePicker()` to get a new file handle.
```
asyncfunctionsaveFile(fileHandle){
if(!fileHandle){
fileHandle=awaitwindow.showSaveFilePicker();
}
constwritable=awaitfileHandle.createWritable();
awaitwritable.write(contents);
awaitwritable.close();
}

```

## And more!
Of course there's plenty more.
  * Support for [`sideways-rl` and `sideways-lr`](https://developer.mozilla.org/docs/Web/CSS/writing-mode#values) keywords for the `writing-mode` CSS property.
  * Roll out of [keyboard focusable scroll containers](https://developer.chrome.com/blog/keyboard-focusable-scrollers) has resumed.
  * Add a `bytes()` method to the `Request` and `Response` interfaces, which returns a promise that resolves with a Uint8Array.


## Further reading
This covers only some key highlights. Check the following links for additional changes in Chrome 132.
  * [Release notes for Chrome 132](https://developer.chrome.com/release-notes/132).
  * [What's new in Chrome DevTools (132)](https://developer.chrome.com/blog/new-in-devtools-132).
  * [ChromeStatus.com updates for Chrome 132](https://chromestatus.com/features#milestone%3D132).
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule).


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
As soon as Chrome 133 is released, we'll be right here to tell you what's new in Chrome!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-01-14 UTC.

