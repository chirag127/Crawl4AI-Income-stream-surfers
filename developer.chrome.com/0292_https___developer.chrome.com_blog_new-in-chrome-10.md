---
url: https://developer.chrome.com/blog/new-in-chrome-103?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-103?hl=en
date: 2025-05-11T16:57:01.022178
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-103?hl=en#main-content)


  * On this page
  * [HTTP 103 status code 103 - early hints](https://developer.chrome.com/blog/new-in-chrome-103?hl=en#http103)
  * [Local Font Access API](https://developer.chrome.com/blog/new-in-chrome-103?hl=en#local-fonts)
  * [Easier Timeouts with AbortSignal.timeout()](https://developer.chrome.com/blog/new-in-chrome-103?hl=en#abort-timeout)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  New in Chrome 103 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP 103 status code 103 - early hints](https://developer.chrome.com/blog/new-in-chrome-103?hl=en#http103)
  * [Local Font Access API](https://developer.chrome.com/blog/new-in-chrome-103?hl=en#local-fonts)
  * [Easier Timeouts with AbortSignal.timeout()](https://developer.chrome.com/blog/new-in-chrome-103?hl=en#abort-timeout)


Pete LePage 
[ GitHub ](https://github.com/petele) [ Glitch ](https://glitch.com/@petele) [ Mastodon ](https://techhub.social/@petele) [ Homepage ](https://petelepage.com/)
Here's what you need to know:
  * There's a new [HTTP 103 status code](https://developer.chrome.com/blog/new-in-chrome-103?hl=en#http103) that helps the browser decide what content to preload before the page has even started to arrive.
  * The [Local Font Access API](https://developer.chrome.com/blog/new-in-chrome-103?hl=en#local-fonts) gives web applications the ability to enumerate and use fonts installed on the user's computer.
  * [`AbortSignal.timeout()`](https://developer.chrome.com/blog/new-in-chrome-103?hl=en#abort-timeout) is an easier way to implement timeouts on asynchronous APIs.
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-103?hl=en#more).


I'm [Pete LePage](https://petelepage.com). Let's dive in and see what's new for developers in Chrome 103.
## HTTP 103 status code 103 - early hints
One way you can improve page performance is to use resource hints. They give the browser "hints" about what stuff it might need later. For example, preloading files, or connecting to a different server.
```
<link as="font" crossorigin="anonymous"
   href="..." rel="preload">
<link as="font" crossorigin="anonymous"
   href="..." rel="preload">
<link href="cdn.example.com"
   rel="preconnect">

```

But the browser can't act on those hints until the server sends at least part of the page.
Imagine the browser requests a page, but the server requires a few hundred milliseconds to generate it. Until the browser starts to receive the page, it just sits there and waits. But, if the server knows the page will always need a certain set of subresources, for example, a CSS file, some JavaScript, and a few images, it can immediately respond with the new HTTP 103 Early Hints status code, and ask the browser to preload those subresources.
Then, once the server has generated the page, it can send it with the normal HTTP 200 response. As the page comes in, the browser has already started loading the required resources.
Since this is a new HTTP status code, using it requires updates to your server.
Get started with HTTP 103 Early hints:
  * [Explainer for Early Hints](https://github.com/bashi/early-hints-explainer/blob/main/explainer.md)
  * [Apache 2 Early Hints configuration](https://httpd.apache.org/docs/2.4/howto/http2.html#earlyhints)
  * [Using Early Hints on Cloudflare](https://developers.cloudflare.com/cache/about/early-hints/)
  * [Fastly Beyond Server Push: The 103 Early Hints Status Code](https://www.fastly.com/blog/beyond-server-push-experimenting-with-the-103-early-hints-status-code)


## Local Font Access API
Fonts on the web have always been a challenge, and especially so for apps that let users create their own graphics and designs. Until now, web apps could only really use web fonts. There was no way to get a list of fonts the user had installed on their computer. And, there was no way to access the full font table data, critical if you need to implement your own custom text stack.
The new Local Font Access API gives web applications the ability to enumerate the local fonts on the user's device, and provides access to the font table data.
To get a list of fonts installed on the device, you'll first need to request permission.
```
// Ask for permission to use the API
try{
conststatus=awaitnavigator.permissions.request({
name:'local-fonts',
});
if(status.state!=='granted'){
thrownewError('No Permission.');
}
}catch(err){
if(err.name!=='TypeError'){
throwerr;
}
}

```

Then, call `window.queryLocalFonts()`. It returns an array of all the fonts installed on the users device.
```
constopts={};
constpickedFonts=awaitself.queryLocalFonts();
for(constfontDataofpickedFonts){
console.log(fontData.postscriptName);
console.log(fontData.fullName);
console.log(fontData.family);
console.log(fontData.style);
}

```

If you're only interested in a subset of fonts, you can filter them by adding a `postscriptNames` parameter.
```
constopts={
postscriptNames:[
'Verdana',
'Verdana-Bold',
'Verdana-Italic',
],
};
constpickedFonts=awaitself.queryLocalFonts(opts);

```

Check out Tom's article [Use advanced typography with local fonts](https://developer.chrome.com/docs/capabilities/web-apis/local-fonts) on web.dev for complete details.
## Easier Timeouts with AbortSignal.timeout()
In JavaScript, `AbortController` and `AbortSignal` are used to cancel an asynchronous call.
For example, when making a `fetch()` request, you can create an `AbortSignal`, and pass it to `fetch()`. If you want to cancel the `fetch()` before it returns, call `abort()` on the instance of the `AbortSignal`. Up until now, if you wanted it to abort after a specific amount of time, you'd need to wrap it in a `setTimeout()`.
```
constcontroller=newAbortController();
constsignal=controller.signal;
constresp=fetch(url,{signal});
setTimeout(()=>{
// abort the fetch after 6 seconds
controller.abort();
},6000);

```

Thankfully, that just got easier with a new `timeout()` static method on `AbortSignal`. It returns an `AbortSignal` object that is automatically aborted after the given number of milliseconds. What used to be a handful of lines of code, is now just one.
```
constsignal=AbortSignal.timeout(6000);
constresp=fetch(url,{signal});

```

[`AbortSignal.timeout()`](https://developer.mozilla.org/docs/Web/API/AbortSignal) is supported in Chrome 103, and is already in Firefox, and Safari.
## And more!
Of course there's plenty more.
  * The `avif` image file format is now sharable by Web Share
  * Chromium now matches Firefox by firing `popstate` immediately after URL changes. The order of events is now: `popstate` then `hashchange` on both platforms.
  * And `Element.isVisible()` tells you whether an element is visible or not.


## Further reading
This covers only some of the key highlights. Check the links below for additional changes in Chrome 103.
  * [What's new in Chrome DevTools (103)](https://developer.chrome.com/blog/new-in-devtools-103)
  * [Chrome 103 deprecations and removals](https://developer.chrome.com/blog/deps-rems-103)
  * [ChromeStatus.com updates for Chrome 103](https://www.chromestatus.com/features#milestone%3D103)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/102.0.5005.113..103.0.5060.60)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
I'm Pete LePage, and as soon as Chrome 104 is released, I'll be right here to tell you what's new in Chrome!
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2022-06-21 UTC.

