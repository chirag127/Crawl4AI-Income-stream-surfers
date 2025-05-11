---
url: https://developer.chrome.com/blog/new-in-chrome-115?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-115?hl=en
date: 2025-05-11T16:57:13.220125
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-115?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-chrome-115?hl=es-419)

Sign in


  * On this page
  * [Scroll driven animations](https://developer.chrome.com/blog/new-in-chrome-115?hl=en#scroll-driven-animations)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  New in Chrome 115 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Scroll driven animations](https://developer.chrome.com/blog/new-in-chrome-115?hl=en#scroll-driven-animations)


Adriana Jara 
[ GitHub ](https://github.com/tropicadri) [ LinkedIn ](https://www.linkedin.com/in/adrianajara) [ Mastodon ](https://hachyderm.io/@tropicadri)
Here's what you need to know:
  * Use `ScrollTimeline` and `ViewTimeline` to create [scroll-driven animations](https://developer.chrome.com/blog/new-in-chrome-115?hl=en#scroll-driven-animations) that enhance user experience.
  * [Fenced frames](https://developer.chrome.com/blog/new-in-chrome-115?hl=en#fenced-frames) work along other Privacy Sandbox APIs to embed relevant content while preventing unnecessary context sharing.
  * With the [Topics API](https://developer.chrome.com/blog/new-in-chrome-115?hl=en#topics-api) the browser can share information with third parties about a user's interests while preserving privacy.
  * And there’s plenty [more](https://developer.chrome.com/blog/new-in-chrome-115?hl=en#more).


I’m Adriana Jara. Let’s dive in and see what’s new for developers in Chrome 115.
## Scroll driven animations
Scroll-driven animations are a common UX pattern on the web. A scroll-driven animation is linked to the scroll position of a scroll container. This means that as you scroll up or down, the linked animation goes forward or backward in direct response.
The following examples demonstrate some use cases. For example you can create reading indicators which move as you scroll:
A reading indicator atop a document, driven by scroll.
Scroll-driven animations can also create elements that fade-in as they come into view:
The images on this page fade-in as they come into view.
By default, an animation attached to an element runs on the document timeline. Its origin time starts at 0 when the page loads, and starts ticking forward as clock time progresses. This is the default animation timeline and, until now, was the only animation timeline you had access to.
The [Scroll-driven Animations Specification](https://drafts.csswg.org/scroll-animations-1/) defines two new types of timelines that you can use:
  * **Scroll Progress Timeline** : a timeline that is linked to the scroll position of a scroll container along a particular axis.
  * **View Progress Timeline** : a timeline that is linked to the relative position of a particular element within its scroll container.


Here’s a code sample that uses an anonymous Scroll Progress Timeline to create a reading progress indicator fixed to the top of the viewport.
```
<body>
 <div id="progress"></div>
 …
</body>

```
```
@keyframesgrow-progress{
from{transform:scaleX(0);}
to{transform:scaleX(1);}
}
#progress{
position:fixed;
left:0;top:0;
width:100%;height:1em;
background:red;
transform-origin:050%;
animation:grow-progressautolinear;
animation-timeline:scroll();
}

```

Read [scroll-drive animations](https://developer.chrome.com/articles/scroll-driven-animations) for all the details and more examples.
## Fenced Frames
The [Privacy Sandbox](https://developers.google.com/privacy-sandbox/overview) is an initiative that aims to create technologies that both protect people's privacy online and give developers tools to build thriving digital businesses.
Many of its proposals aim to satisfy cross-site use cases without third-party cookies or other tracking mechanisms. For example:
  * The [Protected Audience API](https://developers.google.com/privacy-sandbox/blog/fledge-api): allows for interest-based ad serving in a privacy-preserving manner.
  * [Shared Storage](https://developers.google.com/privacy-sandbox/relevance/shared-storage): allows access to unpartitioned cross-site data in a secure environment.


In order to preserve privacy some of these APIs require a new way to embed content. The solution is called a fenced frame.
Fenced frames work in combination with other Privacy Sandbox proposals to display documents from different storage partitions within a single page.
A fenced frame is a HTML element for embedded content, similar to an iframe. Unlike iframes, a fenced frame limits communication with its embedding context to allow the frame access to cross-site data without sharing it with the embedding context.
Similarly, any first-party data in the embedding context cannot be shared with the fenced frame.
Feature  | `iframe` | `fencedframe`  
---|---|---  
Embed content | Yes | Yes  
Embedded content can access embedding context DOM | Yes | No  
Embedding context can access embedded content DOM | Yes | No  
Observable attributes, such as `name` | Yes | No  
URLs (`http://example.com`)  | Yes | Yes ([dependent on use case](https://github.com/WICG/fenced-frame/blob/master/explainer/use_cases.md))  
Browser-managed opaque source (`urn:uuid`) | No | Yes  
Access to cross-site data  | No | Yes (dependent on use case)  
For example, let's say `news.example` (the embedding context) embeds an ad from `shoes.example` in a fenced frame. `news.example` cannot exfiltrate data from the `shoes.example` ad, and `shoes.example` cannot learn first-party data from `news.example`.
Check out these articles for documentation about [Fenced Frames](https://developer.chrome.com/docs/privacy-sandbox/fenced-frame), the [Protected Audience API](https://developers.google.com/privacy-sandbox/blog/fledge-api), [Shared Storage](https://developers.google.com/privacy-sandbox/relevance/shared-storage) and more
## Topics API
In the past, third-party cookies and other mechanisms have been used to track user browsing behavior across sites to infer topics of interest. These mechanisms are being phased out as part of the Privacy Sandbox initiative.
The Topics API allows a browser to share information with third parties about a user's interests while preserving privacy.
The Topics API enables interest-based advertising (IBA) without tracking the sites a user visits. The browser observes and records topics that appear to be of interest to the user, based on their browsing activity. This information is recorded on the user's device.
For example, the API might suggest the topic `"Fiber & Textile Arts"` for a user who visits the website `knitting.example`.
Topics are a signal to help ad tech platforms select relevant ads. Unlike third-party cookies, this information is shared without revealing further information about the user themself or the user's browsing activity.
Read [the Privacy Sandbox overview](https://developers.google.com/privacy-sandbox/overview) for all the details on the topics taxonomy and using the Topics API
## And more!
Of course there’s plenty more.
  * The maximum size of a `WebAssembly.Module` on the main thread increased to 8 megabytes
  * The CSS `display` property now accepts multiple keywords as a value, besides the legacy precomposed keywords.
  * There is an [origin trial](https://developer.chrome.com/origintrials#/view_trial/1196831600973709313) for the Compute Pressure API, which offers high-level information about the current state of the device hardware.


## Further reading
This covers only some key highlights. Check the links below for additional changes in Chrome 115.
  * [What's new in Chrome DevTools (115)](https://developer.chrome.com/blog/new-in-devtools-115)
  * [Chrome 115 deprecations and removals](https://developer.chrome.com/blog/deps-rems-115)
  * [ChromeStatus.com updates for Chrome 115](https://chromestatus.com/features#milestone%3D115)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/114.0.5735.237..115.0.5790.93)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
Yo soy Adriana Jara, and as soon as Chrome 116 is released, I'll be right here to tell you what's new in Chrome!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2023-07-13 UTC.

