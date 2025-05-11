---
url: https://developer.chrome.com/blog/new-in-chrome-123?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-123?hl=en
date: 2025-05-11T16:57:21.675196
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-123?hl=en#main-content)
Sign in


  * On this page
  * [light-dark() CSS function.](https://developer.chrome.com/blog/new-in-chrome-123?hl=en#light-dark)
  * [Long Animation Frames API.](https://developer.chrome.com/blog/new-in-chrome-123?hl=en#long-animation-frames)
  * [Service worker Static Routing API.](https://developer.chrome.com/blog/new-in-chrome-123?hl=en#sw-static-routing-api)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  New in Chrome 123 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [light-dark() CSS function.](https://developer.chrome.com/blog/new-in-chrome-123?hl=en#light-dark)
  * [Long Animation Frames API.](https://developer.chrome.com/blog/new-in-chrome-123?hl=en#long-animation-frames)
  * [Service worker Static Routing API.](https://developer.chrome.com/blog/new-in-chrome-123?hl=en#sw-static-routing-api)


Adriana Jara 
[ GitHub ](https://github.com/tropicadri) [ LinkedIn ](https://www.linkedin.com/in/adrianajara) [ Mastodon ](https://hachyderm.io/@tropicadri)
Here's what you need to know:
  * Adapt your color-scheme with the new [`light-dark()` function](https://developer.chrome.com/blog/new-in-chrome-123?hl=en#light-dark).
  * Diagnose responsiveness on your site with the [Long Animation Frames API](https://developer.chrome.com/blog/new-in-chrome-123?hl=en#long-animation-frames).
  * Avoid service worker start-up performance penalties with the [Service Worker Static Routing API](https://developer.chrome.com/blog/new-in-chrome-123?hl=en#sw-static-routing-api).
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-123?hl=en#more).


I'm Adriana Jara. Let's dive in and see what's new for developers in Chrome 123.
## `light-dark()` CSS function.
The `light-dark()` function in CSS lets you [create colors that adapt to a user's preference for light or dark mode](https://web.dev/articles/light-dark). Use the `light-dark()` function to specify two different color values within a single CSS property.
The browser will automatically choose the appropriate color based on the element's computed `color-scheme` value. For example, with the following CSS:
```
html{
color-scheme:lightdark;
}
.target{
background-color:light-dark(lime,green);
}

```

  * If the user selected a light theme, the element will have a lime background.
  * If the user selected a dark theme, the element will have a green background.


## Long Animation Frames API.
The [Long Animation Frames API](https://w3c.github.io/long-animation-frames/) is available to help you find the causes for main-thread congestion which is often the cause for bad INP ([Interaction to Next Paint](https://web.dev/articles/inp))—a Core Web Vital that measures a website's responsiveness.
The new API is an enhanced version of the Long Tasks API, which provides a better understanding of slow user interface updates. The [Long Animation Frames API](https://developer.chrome.com/docs/web-platform/long-animation-frames) lets you measure blocking work. It measures the tasks together with the following rendering update and adds information such as long running scripts, rendering time, and time spent in forced layout and style, known as [layout thrashing](https://web.dev/articles/avoid-large-complex-layouts-and-layout-thrashing).
Collecting and analyzing this information lets you identify and troubleshoot performance bottlenecks. You can capture long frames with the following code.
```
constobserver=newPerformanceObserver((list)=>{
console.log(list.getEntries());
});
observer.observe({type:'long-animation-frame',buffered:true});

```

## Service worker Static Routing API.
Using service workers you can make websites work offline and create caching strategies that can provide a performance boost.
However, there can be a performance cost when a page is loaded for the first time in a while and the controlling service worker isn't running in that moment. Since all fetches need to happen through the service worker, the browser has to wait for the service worker to start up and run to know what content to load.
With the [Service Worker Static Routing API](https://developer.chrome.com/blog/service-worker-static-routing), at install time, you can declare paths to always be served from the network. When a controlled URL is later loaded, the browser can start fetching resources from those paths before the service worker has finished starting. This removes the service worker from the URLs that you know don't need a service worker.
```
addEventListener('install',(event)=>{
event.addRoutes({
condition:{
urlPattern:"/articles/*",
runningStatus:"running"
},
source:"fetch-event"
});
});

```

## And more!
Of course there's plenty more.
  * You can offer customized pages based on where the user navigated from with the `NavigationActivation` interface.
  * Chrome now has support for [Zstandard](https://www.rfc-editor.org/info/rfc8478) (`zstd`). This `Content-Encoding` helps load pages faster and use less bandwidth, and spend less time, CPU, and power on compression on servers, resulting in reduced server costs.
  * The [`notRestoredReasons` API](https://developer.chrome.com/docs/web-platform/bfcache-notrestoredreasons) for bfcache is rolling out from Chrome 123. This allows site-owners to collect reasons in the field as to why the [bfcache](https://web.dev/articles/bfcache) was unable to be used. Site owners can use this to improve usage of the bfcache which allows faster history navigations.
  * The [`picture-in-picture`](https://developer.mozilla.org/docs/Web/API/Document_Picture-in-Picture_API/Using#target_styles_when_in_picture-in-picture_mode) value for `display-mode` lets you write specific CSS rules that only apply when the web app is shown in picture-in-picture mode. For example:

```
@mediaalland(display-mode:picture-in-picture){
body{
margin:0;
}
h1{
font-size:0.8em;
}
}

```

## Further reading
This covers only some key highlights. Check the following links for additional changes in Chrome 123.
  * [What's new in Chrome DevTools (123)](https://developer.chrome.com/blog/new-in-devtools-123)
  * [Chrome 123 deprecations and removals](https://developer.chrome.com/blog/deps-rems-123)
  * [ChromeStatus.com updates for Chrome 123](https://chromestatus.com/features#milestone%3D123)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/122.0.6261.135..123.0.6312.53)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
Yo soy Adriana Jara, and as soon as Chrome 124 is released, I'll be right here to tell you what's new in Chrome!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-03-19 UTC.

