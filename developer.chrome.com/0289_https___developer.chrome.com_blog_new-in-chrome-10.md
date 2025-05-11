---
url: https://developer.chrome.com/blog/new-in-chrome-102?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-102?hl=en
date: 2025-05-11T16:56:56.925149
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-102?hl=en#main-content)
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


#  New in Chrome 102 
Stay organized with collections  Save and categorize content based on your preferences. 
Pete LePage 
[ GitHub ](https://github.com/petele) [ Glitch ](https://glitch.com/@petele) [ Mastodon ](https://techhub.social/@petele) [ Homepage ](https://petelepage.com/)
Here's what you need to know:
  * Installed PWAs can register as [file handlers](https://developer.chrome.com/blog/new-in-chrome-102?hl=en#file-handlers), making it easy for users to open files directly from disk.
  * The [`inert`](https://developer.chrome.com/blog/new-in-chrome-102?hl=en#inert) attribute allows you to mark parts of the DOM as inert.
  * The [Navigation API](https://developer.chrome.com/blog/new-in-chrome-102?hl=en#navigation-api) makes it easier for single page apps to handle navigation and updates to the URL
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-102?hl=en#more).


I'm [Pete LePage](https://petelepage.com). Let's dive in and see what's new for developers in Chrome 102.
## File Handling API
The File Handling API allows installed PWAs to register with the OS as a file handler. Once registered, a user can click on a file to open it with the installed PWA. This is perfect for PWAs that interact with files, for example, image editors, IDEs, text editors, and so on.
To add file handling functionality to your PWA, you'll need to update your web app manifest, adding a `file_handlers` array with details about the types of files your PWA can handle. You'll need to specify the URL to open, the mime types, an icon for the file type, and the launch type. The launch type defines whether multiple files should be opened in a single client, or in multiple clients.
```
"file_handlers":[
{
"action":"/open-csv",
"accept":{"text/csv":[".csv"]},
"icons":[
{
"src":"csv-icon.png",
"sizes":"256x256",
"type":"image/png"
}
],
"launch_type":"single-client"
}
]

```

Then, to access those files when the PWA is launched, you need to specify a consumer for the `launchQueue` object. Launches are queued until they are handled by the consumer.
```
// Access from Window.launchQueue.
launchQueue.setConsumer((launchParams)=>{
if(!launchParams.files.length){
// Nothing to do when the queue is empty.
return;
}
for(constfileHandleoflaunchParams.files){
// Handle the file.
openFile(fileHandle);
}
});

```

Check out [Let installed web applications be file handlers](https://developer.chrome.com/docs/capabilities/web-apis/file-handling) for all the details.
## The `inert` property
The `inert` property is a global HTML attribute that tells the browser to ignore user input events for an element, including focus events, and events from assistive technologies.
This can be useful when building UIs. For example, with a modal dialog, you want to "trap" the focus inside the modal when it's visible. Or, for a drawer that is not always visible to the user, adding `inert` ensures that while the drawer is offscreen, a keyboard user cannot accidentally interact with it.
```
<div>
 <label for="button1">Button 1</label>
 <button id="button1">I am not inert</button>
</div>
<div inert>
 <label for="button2">Button 2</label>
 <button id="button2">I am inert</button>
</div>

```

Here, `inert` has been declared on the second `<div>` element, so all content contained within, including the `<button>` and `<label>`, cannot receive focus or be clicked.
`inert` is supported in Chrome 102, and is coming to both Firefox and Safari.
Check out [Introducing inert](https://developer.chrome.com/articles/inert) for more details.
## Navigation API
Many web apps depend on the ability to update the URL without a page navigation. Today, we use the [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API/Working_with_the_History_API), but it's clunky and doesn't always work as expected. Rather than trying to patch the History API's rough edges, the Navigation API completely overhauls this space.
To use the Navigation API, add a `navigate` listener on the global `navigation` object.
```
navigation.addEventListener('navigate',(navigateEvent)=>{
switch(navigateEvent.destination.url){
case'https://example.com/':
navigateEvent.transitionWhile(loadIndexPage());
break;
case'https://example.com/cats':
navigateEvent.transitionWhile(loadCatsPage());
break;
}
});

```

The event is fundamentally centralized and it will fire for all types of navigations, whether the user performed an action, such as clicking a link, submitting a form, or going back and forward, even when navigation is triggered programmatically. In most cases, it lets your code override the browser's default behavior for that action.
Check out the [Modern client-side routing: the Navigation API](https://developer.chrome.com/docs/web-platform/navigation-api) for complete details and a demo you can try out.
## And more!
Of course there's plenty more.
  * The new Sanitizer API aims to build a robust processor for arbitrary strings to be safely inserted into a page.
  * The `hidden=until-found` attribute makes it possible for the browser to search text in hidden regions, and reveal that section if a match is found.


## Further reading
This covers only some of the key highlights. Check the links below for additional changes in Chrome 102.
  * [What's new in Chrome DevTools (102)](https://developer.chrome.com/blog/new-in-devtools-102)
  * [Chrome 102 deprecations and removals](https://developer.chrome.com/blog/deps-rems-102)
  * [ChromeStatus.com updates for Chrome 102](https://www.chromestatus.com/features#milestone%3D102)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/101.0.4951.49..102.0.5005.113)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
I'm Pete LePage, and as soon as Chrome 103 is released, I'll be right here to tell you what's new in Chrome!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2022-06-09 UTC.

