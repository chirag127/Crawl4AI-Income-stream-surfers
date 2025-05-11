---
url: https://developer.chrome.com/blog/new-in-chrome-93?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-93?hl=en
date: 2025-05-11T16:57:43.097802
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-93?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-chrome-93?hl=es-419)




  * On this page
  * [CSS Module Scripts](https://developer.chrome.com/blog/new-in-chrome-93?hl=en#css-modules)
  * [Multi-Screen Window Placement API](https://developer.chrome.com/blog/new-in-chrome-93?hl=en#window-placement)
  * [Shortened release cycle](https://developer.chrome.com/blog/new-in-chrome-93?hl=en#shortened_release_cycle)
  * [New PWA features](https://developer.chrome.com/blog/new-in-chrome-93?hl=en#new-pwa)
    * [URL handlers for PWAs](https://developer.chrome.com/blog/new-in-chrome-93?hl=en#url-handlers)
    * [Window controls overlay](https://developer.chrome.com/blog/new-in-chrome-93?hl=en#window-controls-overlay)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  New in Chrome 93 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [CSS Module Scripts](https://developer.chrome.com/blog/new-in-chrome-93?hl=en#css-modules)
  * [Multi-Screen Window Placement API](https://developer.chrome.com/blog/new-in-chrome-93?hl=en#window-placement)
  * [Shortened release cycle](https://developer.chrome.com/blog/new-in-chrome-93?hl=en#shortened_release_cycle)
  * [New PWA features](https://developer.chrome.com/blog/new-in-chrome-93?hl=en#new-pwa)
    * [URL handlers for PWAs](https://developer.chrome.com/blog/new-in-chrome-93?hl=en#url-handlers)
    * [Window controls overlay](https://developer.chrome.com/blog/new-in-chrome-93?hl=en#window-controls-overlay)


Pete LePage 
[ GitHub ](https://github.com/petele) [ Glitch ](https://glitch.com/@petele) [ Mastodon ](https://techhub.social/@petele) [ Homepage ](https://petelepage.com/)
Here's what you need to know:
  * You can now load CSS style sheets with [`import` statements](https://developer.chrome.com/blog/new-in-chrome-93?hl=en#css-modules), just like JavaScript modules.
  * Installed PWAs can register as [URL handlers](https://developer.chrome.com/blog/new-in-chrome-93?hl=en#url-handlers), making it possible for users to jump straight into your PWA.
  * The [Multi-Screen Window Placement API](https://developer.chrome.com/blog/new-in-chrome-93?hl=en#window-placement) has been updated based on your feedback, and starts a second origin trial.
  * The [PWA Summit](https://developer.chrome.com/blog/new-in-chrome-93?hl=en#pwa_summit) is coming up October 6-7.
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-93?hl=en#more).


I'm [Pete LePage](https://petelepage.com), working, and shooting from home, let's dive in and see what's new for developers in Chrome 93.
## CSS Module Scripts
You can now load CSS style sheets with `import` statements, just like JavaScript modules. The style sheets can then be applied to the document or shadow roots in the same manner as constructable stylesheets.
The new CSS Module Scripts feature is great for custom elements. And unlike other ways of applying CSS from JavaScript, there is no need to create elements, or mess with JavaScript strings of CSS text.
To use it, import the style sheet with `assert {type: 'css'}`, then apply it to the `document` or `shadowRoot` by calling `adoptedStyleSheets`.
```
importsheetfrom'./styles.css'assert{type:'css'};
document.adoptedStyleSheets=[sheet];
shadowRoot.adoptedStyleSheets=[sheet];

```

But beware, if you leave off the `assert` - the file will be treated as JavaScript, and won't work!
Check out [Using CSS Module Scripts to import stylesheets](https://web.dev/css-module-scripts/) on web.dev for complete details.
## Multi-Screen Window Placement API
For some apps, opening new windows and putting them in specific places or specific displays is an important feature. For example, when using Slides to present, I want the slides to appear full screen on the primary display, and my speaker notes to appear on the other display.
The Multi-Screen Window Placement API makes it possible to enumerate the displays connected to the users machine, and place windows on specific screens. This is its second origin trial, and we've made a number of changes based on your feedback.
You can quickly check if there's more than one screen connected to the device:
```
constisExtended=window.screen.isExtended;
// returns true/false

```

But, the key functionality is in `window.getScreens()`, which provides all the details about the attached displays.
```
constscreens=awaitwindow.getScreens();
// returns
// {
//  currentScreen: {...}
//  oncurrentscreenchange: null
//  onscreenschange: null
//  screens: [{...}, {...}]
// }

```

For example, you can determine the primary screen, then use `requestFullscreen()` to display an element on that screen.
```
try{
constscreens=awaitwindow.getScreens();
constprimary=screens.filter((screen)=>screen.primary)[0];
awaitelem.requestFullscreen({screen:primary});
}catch(err){
console.error(err);
}

```

And it provides a way to listen for changes, for example if a new display is plugged in, or removed.
```
constscreens=awaitwindow.getScreens();
letnumScreens=screens.screens.length;
screens.addEventListener('screenschange',(event)=>{
if(screens.screens.length!==numScreens){
console.log('Screen count changed');
numScreens=screens.screens.length;
}
});

```

Check out Tom's article [Managing several displays with the Multi-Screen Window Placement API](https://web.dev/multi-screen-window-placement/) on web.dev for a deeper dive.
## Shortened release cycle
In March, we announced our plans to [shorten the release cycle](https://developer.chrome.com/blog/faster-release-cycle/) and ship a new version of Chrome every four weeks.
That time has arrived, and we'll ship Chrome 94 on September 21st. You can find planned release dates for each version on the [Chrome Calendar](https://chromiumdash.appspot.com/schedule).
## New PWA features
If you're building a Progressive Web App, there are two new origin trials worth checking out.
### URL handlers for PWAs
If you have a PWA installed, and you click on a link to that PWA, you probably want it to open in the PWA, **not** a browser tab.
By specifying [`url_handlers`](https://web.dev/pwa-url-handler/) in your [web app manifest](https://web.dev/add-manifest/), and adding a `web-app-origin-association` file to your `.well-known/` directory, you can tell the browser that if a user clicks a link to your PWA, it should open within the installed PWA.
Example `url_handlers` in the `manifest.json` file:
```
{
...
"url_handlers":[
{"origin":"https://music.example.com"}
]
}

```

Example `web-app-origin-association` file:
```
{
"web_apps":[
{
"manifest":"https://music.example.com/manifest.json",
"details":{
"paths":["/*"],
"exclude_paths":["/internal/*"]
}
}
]
}

```

And with a little extra verification, you can even have your PWA handle links from other origins you own.
All the details about the origin trial are in [PWAs as URL Handlers](https://web.dev/pwa-url-handler/) on web.dev.
### Window controls overlay
Window controls overlay extends the client area to cover the entire window, including the title bar, and the window control buttons, like the close, maximize, and minimize buttons.
You can use this feature to make your installed PWA look more like other installed apps.
For more information about the origin trial, check out [Customize the window controls overlay of your PWA's title bar](https://web.dev/window-controls-overlay/).
## PWA Summit
The [PWA Summit](https://pwasummit.org/) is coming up in October. It's a a free, online conference focused on helping everyone succeed with Progressive Web Apps. The PWA Summit is a collaboration between folks from a handful of different companies involved in the creation of PWA technologies: Google, Intel, Microsoft, and Samsung.
There are a ton of great talks and content. You can learn more and register at [PWASummit.org](https://pwasummit.org/).
## And more!
Of course there's plenty more.
  * Flexbox and flexbox items have added support for the alignment keywords: `start`, `end`, `self-start`, `self-end`, `left`, and `right`.
  * The async clipboard API now supports SVG files.
  * And, the `media` attribute will be honored when setting `meta` `theme-color`, so you can specify different theme colors for light and dark modes.

```
<meta name="theme-color"
   media="(prefers-color-scheme: light)"
   content="white">
<meta name="theme-color"
   media="(prefers-color-scheme: dark)"
   content="black">

```

## Further reading
This covers only some of the key highlights. Check the links below for additional changes in Chrome 93.
  * [What's new in Chrome DevTools (93)](https://developer.chrome.com/blog/new-in-devtools-93)
  * [Chrome 93 deprecations & removals](https://developer.chrome.com/blog/deps-rems-93)
  * [ChromeStatus.com updates for Chrome 93](https://www.chromestatus.com/features#milestone%3D93)
  * [What's new in JavaScript in Chrome 93](https://v8.dev/blog/v8-release-93)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/92.0.4515.105..93.0.4577.69)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
I'm Pete LePage, and as soon as Chrome 94 is released, I'll be right here to tell you what's new in Chrome!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2021-08-31 UTC.

