---
url: https://developer.chrome.com/blog/new-in-chrome-118?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-118?hl=en
date: 2025-05-11T16:57:17.088437
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-118?hl=en#main-content)
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


#  New in Chrome 118 
Stay organized with collections  Save and categorize content based on your preferences. 
Adriana Jara 
[ GitHub ](https://github.com/tropicadri) [ LinkedIn ](https://www.linkedin.com/in/adrianajara) [ Mastodon ](https://hachyderm.io/@tropicadri)
Here's what you need to know:
  * Declare specific styles within a component with the [`@scope` css rule](https://developer.chrome.com/blog/new-in-chrome-118?hl=en#css-scope).
  * There's a new media feature: [`prefers-reduced-transparency`](https://developer.chrome.com/blog/new-in-chrome-118?hl=en#new-media-queries).
  * DevTools has improvements in the [**Sources** panel](https://developer.chrome.com/blog/new-in-chrome-118?hl=en#sources-panel-devtools).
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-118?hl=en#more).


I'm Adriana Jara. Let's dive in and see what's new for developers in Chrome 118.
## CSS `@scope` rule.
The `@scope` at-rule allows developers to scope style rules to a given scoping root, and style elements according to the proximity of that scoping root.
With `@scope` you can override styles based on proximity, which is different from the usual CSS styles that are applied relying only on source order and specificity. In the following example, there are two themes.
```
<div class="lightpink-theme">
 <a href="#">I'm lightpink!</a>
 <div class="pink-theme">
  <a href="#">Different pink!</a>
 </div>
</div>

```

without scope, the style applied is the last one declared.
Without @scope
```
.pink-themea{color:hotpink;}
.lightpink-themea{color:lightpink;}
```

With scope you can have nested elements and the style that applies is the one for the nearest ancestor.
With @scope
```
@scope(.pink-theme){
a{
color:hotpink;
}
}
@scope(.lightpink-theme){
a{
color:lightpink;
}
}
```

Scope also saves you from writing long, convoluted class names, and makes it easy to manage larger projects and avoid naming conflicts.
Without @scope
```
<div class="first-container">
 <h1 class="first-container__main-title"> I'm the main title</h1>
</div>
<div class="second-container">
 <h1 class="second-container__main-title"> I'm the main title, but somewhere else</h1>
</div>
```
```
.first-container__main-title{
color:grey;
}
.second-container__main-title{
color:mediumturquoise;
}
```

With @scope
```
<div class="first-container">
 <h1 class="main-title"> I'm the main title</h1>
</div>
<div class="second-container">
 <h1 class="main-title"> I'm the main title, but somewhere else</h1>
</div>
```
```
@scope(.first-container){
.main-title{
color:grey;
}
}
@scope(.second-container){
.main-title{
color:mediumturquoise;
}
}
```

With scope you can also style a component without styling certain things that are nested within. In a way you can have “holes” where the scoped style doesn't apply.
Like in the following example, we could apply style to the text and exclude controls or vice versa.
```
<div class="component">
 <div class="purple">
  <h1>Drink water</h1>
  <p class="purple">hydration is important</p>
 </div>
 <div class="click-here">
  <p>not in scope</p>
  <button>click here</button>
 </div>
 <div class="purple">
  <h1 class="purple">Exercise</h1>
  <p class="purple">move it move it</p>
 </div>
 <div class="link-here">
  <p>Excluded from scope</p>
  <a href="#"> link here </a>
 </div>
</div>

```
```
@scope(.component)to(.click-here,.link-here){
div{
color:purple;
text-align:center;
font-family:sans-serif;
}
}

```

Checkout the article [Limit the reach of your selectors with the CSS @scope at-rule](https://developer.chrome.com/articles/at-scope) for more information.
## `prefers-reduced-transparency` media feature
We use media queries to provide user experiences that adapt to the user's preferences and device conditions. This Chrome version adds a new value that can be used to adapt user experience: `prefers-reduced-transparency`.
A new value you can test with media queries is `prefers-reduced-transparency` which lets developers adapt web content to user-selected preference for reduced transparency in the OS, such as the Reduce transparency setting on macOS. Valid options are `reduce` or `no-preference`.
```
.translucent{
opacity:0.4;
}
@media(prefers-reduced-transparency){
.translucent{
opacity:0.8;
}
}

```

And, you can check how it looks with DevTools:
For more information checkout the [prefers-reduced-transparency](https://developer.mozilla.org/docs/Web/CSS/@media/prefers-reduced-transparency) documentation.
_Correction: A previous version of this article referred to a new[`scripting`](https://developer.mozilla.org/docs/Web/CSS/@media/scripting) media feature being in this release. It will actually be in version 120._
## Sources panel improvements in DevTools
DevTools has the following improvements in the **Sources** panel: the [workspace](https://developer.chrome.com/docs/devtools/workspaces) feature improved consistency, most notably, by renaming the **Sources** > **Filesystem** pane to **Workspace** along with other UI text, the [**Sources** > **Workspace**](https://developer.chrome.com/docs/devtools/workspaces) also lets you sync changes you make in DevTools directly to your source files.
Also, you can now reorder panes on the left side of the **Sources** panel by dragging and dropping, and the **Sources** panel can now pretty-print inline JavaScript within the following script types: [`module`](https://developer.mozilla.org/docs/Web/JavaScript/Guide/Modules), [`importmap`](https://developer.mozilla.org/docs/Web/HTML/Element/script/type/importmap), [`speculationrules`](https://developer.chrome.com/docs/devtools/application/debugging-speculation-rules) and highlight the syntax of `importmap` and `speculationrules` script types, both of which hold JSON.
Checkout [What's New in DevTools](https://developer.chrome.com/blog/new-in-devtools-118) for more on Chrome 118 DevTools updates.
## And more!
Of course there's plenty more.
  * [WebUSB API](https://developer.chrome.com/articles/usb) is now exposed to [Service Workers registered by browser extensions](https://developer.chrome.com/docs/extensions/mv3/service_workers) allowing developers to use the API when responding to extension events.
  * To help developers reduce friction in Payment Request flows, we are removing the user activation requirement in `Payment Request` and `Secure Payment Confirmation`.
  * [Chrome's release cycle is becoming shorter](https://developer.chrome.com/blog/faster-chrome-releases-round2), stable versions will be released every three weeks, starting with Chrome 119 that will be here in three weeks.


## Further reading
This covers only some key highlights. Check the links below for additional changes in Chrome 118.
  * [What's new in Chrome DevTools (118)](https://developer.chrome.com/blog/new-in-devtools-118)
  * [Chrome 118 deprecations and removals](https://developer.chrome.com/blog/deps-rems-118)
  * [ChromeStatus.com updates for Chrome 118](https://chromestatus.com/features#milestone%3D118)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/116.0.5845.171..118.0.5938.57)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
Yo soy Adriana Jara, and as soon as Chrome 119 is released, I'll be right here to tell you what's new in Chrome!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2023-10-10 UTC.

