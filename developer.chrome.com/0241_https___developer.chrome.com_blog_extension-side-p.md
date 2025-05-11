---
url: https://developer.chrome.com/blog/extension-side-panel-launch?hl=en
title: https://developer.chrome.com/blog/extension-side-panel-launch?hl=en
date: 2025-05-11T16:55:55.958043
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/extension-side-panel-launch?hl=en#main-content)
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


#  Design a superior user experience with the new Side Panel API 
Stay organized with collections  Save and categorize content based on your preferences. 
Oliver Dunk 
[ GitHub ](https://github.com/oliverdunk) [ Bluesky ](https://bsky.app/profile/oliverdunk.com) [ Homepage ](https://oliverdunk.com)
Amy Steam 
[ GitHub ](https://github.com/amysteam) [ LinkedIn ](https://www.linkedin.com/in/amysteam)
A year ago, in May 2022, we added the side panel to Chrome. This is a new companion surface that allows users to use tools alongside the content they are browsing. Today, we're excited to announce that your extension can start showing content in the side panel, beginning in Chrome 114.
A dictionary extension that shows the definition of a selected word. See the [code](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/functional-samples/sample.sidepanel-dictionary) in the chrome-extensions-samples repository. 
## Better for users, easier for developers
We've already seen many developers implement sidebar-like experiences into their extension, which is why we're thrilled to make it a platform standard. With the new [Side Panel API](https://developer.chrome.com/docs/extensions/reference/api/sidePanel), you can now offer a persistent UI that opens alongside a page that the user is visiting. Users will benefit from consistent positioning and layout between extensions. In addition, the ability to show UI without requesting host permissions is a significant privacy win for users, with the added benefit of reducing the number of warnings that show for your extension at install time.
The [Side Panel API](https://developer.chrome.com/docs/extensions/reference/api/sidePanel) eliminates the headaches associated with injecting content into an untrusted page. It also significantly reduces the requirement for maintaining compatibility across different sites and sifting through bug reports about accidental disruptions caused by your extension.
## A companion to users across the web
When building a new side panel experience as part of your extension, you need to keep one thing in mind: how are you assisting users to complete tasks across the web? Here are a few questions you should consider: 

How does my side panel help the user?
    The [single-purpose](https://developer.chrome.com/docs/extensions/mv3/quality_guidelines#single-purpose) policy also applies to your side panel. Make sure that your side panel provides functionality that directly relates to the rest of your extension and what the user is trying to achieve. 

Does my side panel only appear when it's relevant?
    The [Side Panel API](https://developer.chrome.com/docs/extensions/reference/sidePanel/#by-site) lets you choose which sites your users will see the side panel on. This way you can avoid showing it when it isn't relevant to the user or it isn't related to the content the user is browsing. 

Is the design consistent with the rest of my extension?
    Your side panel should have a visually appealing design that matches the logo, colors, icons, and fonts of your extension and store listing. This provides users a consistent, recognizable experience wherever they are using your extension. 

How do users discover my side panel?
    Let new users know how to use your side panel by providing sufficient documentation or training within the extension. This will help you retain users and avoid bad reviews in your store listing. Remember, you can start to teach users before they install the extension by including a [YouTube video](https://developer.chrome.com/docs/webstore/cws-dashboard-listing#graphic-assets) that shows how your extension works in your store listing!
We've also updated our [Program Policies](https://developer.chrome.com/docs/webstore/program-policies), with updates to our [Best Practices](https://developer.chrome.com/docs/webstore/program-policies/best-practices) and [Quality Guidelines](https://developer.chrome.com/docs/webstore/program-policies/quality-guidelines) sections to reflect some of these considerations. These changes highlight that your side panel should act as a helpful companion to users' browsing experiences by providing complementary functionality. They also make it clear that your side panel shouldn't have unnecessary distractions.
## An overview of the API
For your extension to appear in the side panel, request the `"sidePanel"` permission in your [manifest](https://developer.chrome.com/docs/extensions/mv3/manifest), and add the `"side_panel"` key with a `"default_path"` pointing to a page within your extension:
manifest.json:
```
{
...
"side_panel":{
"default_path":"sidepanel.html"
},
"permissions":[
"sidePanel"
]
...
}

```

On a side panel page, you can load scripts and call extension APIs as you would on any other extension page. The icon for your side panel will be taken from your [extension's icon](https://developer.chrome.com/docs/extensions/mv3/manifest/icons) - don't forget to set that for an extra bit of polish.
## Extra capabilities
You can link the side panel to your action icon, so it can be easily opened at any time:
service-worker.js:
```
awaitchrome.sidePanel.setPanelBehavior({openPanelOnActionClick:true});

```

If you'd only like your side panel to show up on specific pages, you can control that, and prevent it from appearing elsewhere where it is not relevant to the user:
service-worker.js:
```
chrome.tabs.onUpdated.addListener((tabId,info,tab)=>{
if(!tab.url)return;
consturl=newURL(tab.url);
if(url.origin==='https://example.com'){
chrome.sidePanel.setOptions({tabId,path:'sidepanel.html',enabled:true});
}else{
chrome.sidePanel.setOptions({tabId,enabled:false});
}
});

```

## Learn more
We've published the [Side Panel API](https://developer.chrome.com/docs/extensions/reference/api/sidePanel) documentation which you can start reading today. We've also added [samples](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/functional-samples/) to the chrome-extensions-samples repository, which is a great place to see how the API can be used in practice.
As mentioned, our policy pages and best practices have also been revised to share more about how to build a side panel that provides the best experience for your users.
You can keep up with Chrome extension news by visiting our [What's new page](https://developer.chrome.com/docs/extensions/whatsnew), and if you have questions or need help with the Side Panel API, you can visit the [Chromium extensions](https://groups.google.com/a/chromium.org/g/chromium-extensions) Google Group.
_Photo by[Vardan Papikyan](https://unsplash.com/@timberfoster?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/photos/lSegRSDBMLw?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)_
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2023-05-30 UTC.

