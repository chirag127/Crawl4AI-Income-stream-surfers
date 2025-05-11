---
url: https://developer.chrome.com/blog/new-in-chrome-video-q1-2025?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-video-q1-2025?hl=en
date: 2025-05-11T16:57:43.092295
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-video-q1-2025?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-chrome-video-q1-2025?hl=es-419)

Sign in


  * On this page
  * [State preserving way to move a DOM element](https://developer.chrome.com/blog/new-in-chrome-video-q1-2025?hl=en#movebefore)
  * [File system access API](https://developer.chrome.com/blog/new-in-chrome-video-q1-2025?hl=en#fileaccess)
  * [Light dismiss comes to the <dialog> element](https://developer.chrome.com/blog/new-in-chrome-video-q1-2025?hl=en#lightdismiss)
  * [Updates in Baseline](https://developer.chrome.com/blog/new-in-chrome-video-q1-2025?hl=en#baseline)
    * [Baseline Newly available](https://developer.chrome.com/blog/new-in-chrome-video-q1-2025?hl=en#baseline_newly_available)
    * [Baseline Widely available](https://developer.chrome.com/blog/new-in-chrome-video-q1-2025?hl=en#baseline_widely_available)
    * [Interop project is back for 2025](https://developer.chrome.com/blog/new-in-chrome-video-q1-2025?hl=en#interop_project_is_back_for_2025)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  New in Chrome Q1 2025: CSS text-box, file system access for Android, Baseline updates and more! 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [State preserving way to move a DOM element](https://developer.chrome.com/blog/new-in-chrome-video-q1-2025?hl=en#movebefore)
  * [File system access API](https://developer.chrome.com/blog/new-in-chrome-video-q1-2025?hl=en#fileaccess)
  * [Light dismiss comes to the <dialog> element](https://developer.chrome.com/blog/new-in-chrome-video-q1-2025?hl=en#lightdismiss)
  * [Updates in Baseline](https://developer.chrome.com/blog/new-in-chrome-video-q1-2025?hl=en#baseline)
    * [Baseline Newly available](https://developer.chrome.com/blog/new-in-chrome-video-q1-2025?hl=en#baseline_newly_available)
    * [Baseline Widely available](https://developer.chrome.com/blog/new-in-chrome-video-q1-2025?hl=en#baseline_widely_available)
    * [Interop project is back for 2025](https://developer.chrome.com/blog/new-in-chrome-video-q1-2025?hl=en#interop_project_is_back_for_2025)


Mariko Kosaka 
It's been a while! The New In Chrome video is back with information about:
  * [CSS text-box](https://developer.chrome.com/blog/new-in-chrome-video-q1-2025?hl=en#csstext), which lets you control vertical spacing precisely by using the font metrics.
  * The [file system access API](https://developer.chrome.com/blog/new-in-chrome-video-q1-2025?hl=en#fileaccess) that's now supported on Android and web view.
  * A [State preserving way to move a DOM element](https://developer.chrome.com/blog/new-in-chrome-video-q1-2025?hl=en#movebefore) with `moveBefore`.
  * [Light dismiss](https://developer.chrome.com/blog/new-in-chrome-video-q1-2025?hl=en#lightdismiss) comes to the `<dialog>` element.
  * And there's many updates in [Baseline and more](https://developer.chrome.com/blog/new-in-chrome-video-q1-2025?hl=en#baseline)!


I'm Mariko. Let's dive in and see what's new in Chrome for the past three releases.
## CSS text-box
The CSS `text-box` property lets you control vertical spacing precisely by using the font metrics.
Every font produces a different amount of space above, and below the characters, which determines the size of the element.
It has been impossible to control the size of these spaces until now.
The new `text-box-trim` property specifies the sides to trim, above or below, and `text-box-edge` property specifies how it should be trimmed. For example, trim at cap height, which is the top of uppercase characters.
You can also write this using the shorthand `text-box` property.
Find out more about how to use these new properties in the [CSS `text-box-trim`](https://developer.chrome.com/blog/css-text-box-trim) article.
## State preserving way to move a DOM element
Added in Chrome 133, a DOM primitive `Node.prototype.moveBefore` lets you move elements around a DOM tree, without resetting the element's state.
When you remove, then re-insert an element to move a DOM element, it will reset the state of that element. Using this new primitive, the state of a node is preserved.
So iframes remain loaded, active elements remain in focus, things like popovers and dialogs remain open, and CSS transitions or animations carry on.
## File system access API
The File System Access API has been available on Chrome Desktop for some time now. This API lets web apps interact with files on the user's local file system. From Chrome 132, the API is available on Android and in WebViews as well.
To read a file, call `showOpenFilePicker()`. This method shows a file picker, then returns a file handle that you can use to read the file.
```

letfileHandle;
btn.addEventListener('click',async()=>{
[fileHandle]=awaitwindow.showOpenFilePicker();
// Do something with the file handle.
});

```

To save a file to disk, you can use the same file handle you got earlier, or call `showSaveFilePicker()` to get a new file handle.
```
asyncfunctiongetNewFileHandle(){
constoptions={
// Add options
};
consthandle=awaitwindow.showSaveFilePicker(options);
returnhandle;
}

```

## Light dismiss comes to the `<dialog>` element
If you've used the Popover API to make a popover, you know that one of the nice features of Popover API is the light dismiss behavior. Users can click the background and the popover element is closed without specifically hitting the close button.
This light dismiss capability is now supported in the `<dialog>` element as well!
When you set `closedby` attribute to `any`, the dialog can be dismissed by clicking outside of the dialog or pressing escape keys.
```

<dialog closedby="any">...</dialog>

```

This is the same behavior as when a popover is set to auto.
## Updates in Baseline
And, here's news about Baseline
### Baseline Newly available
First, Baseline Newly available, these are features that shipped in all four major browsers recently.
#### `scrollbar-gutter` and `scrollbar-width`
With the [scrollbar-gutter CSS property](https://developer.mozilla.org/docs/Web/CSS/scrollbar-gutter) you can reserve a space for the scrollbar to avoid unwanted layout changes when the scrollbar appears or disappears. With [scrollbar-width](https://developer.mozilla.org/docs/Web/CSS/scrollbar-width) you can create a narrower scrollbar, or even to hide the scrollbar completely without affecting scrollability.
#### `ruby-align`
With the [ruby-align CSS property](https://developer.mozilla.org/docs/Web/CSS/ruby-align) you can specify alignment of ruby base text and ruby annotation text.
#### `Promise.try`
[Promise.try](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise/try) is a convenience method to make error handling for synchronous requests. Using this, you can eliminate callback functions when you try to request with Promise.resolve.
#### Wasm Garbage Collection and tail call optimizations
WebAssembly now supports Garbage Collection and tail call optimizations.
### Baseline Widely available
#### Array `findLast()` and `findLastIndex()`
Array [findLast()](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array/findLast) and [findLastIndex()](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array/findLastIndex) are very convenient methods to get items from the end of an array. This feature has been supported by all major browsers for 30 months, which means it is now Baseline widely available.
#### Individual transform properties
[Individual transform properties](https://web.dev/articles/css-individual-transform-properties) which give you finer grained control over CSS transforms are now Baseline Widely available as well .
#### More about Baseline
If you want to know more about Baseline and the difference between Newly and Widely available, check out [the short video](https://www.youtube.com/shorts/3ja-dfmlDnI) I made.
You can also find more about the baseline status of a feature at the [Web Platform Status dashboard](https://webstatus.dev/) !
### Interop project is back for 2025
And lastly, the Interop project is returning for 2025 with a list of focus areas including view transitions, CSS anchor positioning, and the Navigation API. Be sure to check out [the project announcement](https://web.dev/blog/interop-2025)!
## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
I'm Mariko Kosaka, and I will be back in three months to tell you more about What’s new in Chrome!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-03-11 UTC.

