---
url: https://developer.chrome.com/blog/how-boxysvg-uses-the-local-font-access-api?hl=en
title: https://developer.chrome.com/blog/how-boxysvg-uses-the-local-font-access-api?hl=en
date: 2025-05-11T16:56:14.350283
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/how-boxysvg-uses-the-local-font-access-api?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/how-boxysvg-uses-the-local-font-access-api?hl=es-419)

Sign in


  * On this page
  * [Local Font Access API in Boxy SVG](https://developer.chrome.com/blog/how-boxysvg-uses-the-local-font-access-api?hl=en#local_font_access_api_in_boxy_svg)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  How vector image editing app Boxy SVG uses the Local Font Access API to let users pick their favorite local fonts 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Local Font Access API in Boxy SVG](https://developer.chrome.com/blog/how-boxysvg-uses-the-local-font-access-api?hl=en#local_font_access_api_in_boxy_svg)


The Local Font Access API provides a mechanism to access the user's locally installed font data, including higher-level details such as names, styles, and families, as well as the raw bytes of the underlying font files. Learn how the SVG editing app Boxy SVG makes use of this API.
Thomas Steiner 
[ GitHub ](https://github.com/tomayac) [ Glitch ](https://glitch.com/@tomayac) [ LinkedIn ](https://www.linkedin.com/in/thomassteinerlinkedin) [ Mastodon ](https://toot.cafe/@tomayac) [ Bluesky ](https://bsky.app/profile/tomayac.com) [ Homepage ](https://blog.tomayac.com/)
Jarek Foksa 
[ GitHub ](https://github.com/jarek-foksa) [ Homepage ](http://foksa.name/)
## Introduction
(This article is also available in form of a video.)
[Boxy SVG](https://boxy-svg.com/) is a vector graphics editor. Its main use case is editing drawings in the SVG file format, for creating illustrations, logos, icons, and other elements of graphic design. It's developed by Polish developer [Jarosław Foksa](https://foksa.name/) and was initially released on March 15, 2013. Jarosław runs a [Boxy SVG blog](https://boxy-svg.com/blog/) in which he announces new features he adds to the app. The developer is a strong supporter of [Chromium's Project Fugu](https://developer.chrome.com/capabilities) and even has a [Fugu tag](https://boxy-svg.com/ideas?tag=Fugu) on the app's ideas tracker.
## Local Font Access API in Boxy SVG
One feature addition Jarosław [blogged about](https://boxy-svg.com/blog/15/enabling-local-system-fonts-support) was the [Local Font Access API](https://developer.mozilla.org/docs/Web/API/Local_Font_Access_API). The Local Font Access API lets users access their locally installed fonts, including higher-level details such as names, styles, and families, as well as the raw bytes of the underlying font files. In the following screenshot you can see how I have granted the app access to the locally installed fonts on my MacBook and chosen the Marker Felt font for my text.
The underlying code is quite straightforward. When the user opens the font family picker for the first time, the application first checks if the web browser supports the Local Font Access API.
It also checks for the old experimental version of the API and uses it if present. As of 2023, you can safely ignore the old API as it was available only for a short time via experimental Chrome flags, but some Chromium-derivatives may still use it.
```
letisLocalFontsApiEnabled=(
// Local Font Access API, Chrome >= 102
window.queryLocalFonts!==undefined||
// Experimental Local Font Access API, Chrome < 102
navigator.fonts?.query!==undefined
);

```

If the Local Font Access API is not available, the font family picker will turn gray. A placeholder text will be displayed to the user instead of the fonts list:
```
if(isLocalFontsApiEnabled===false){
showPlaceholder("no-local-fonts-api");
return;
}

```

Otherwise, the Local Font Access API is used to retrieve the list of all fonts from the operating system. Notice the `try…catch` block which is needed in order to handle permission errors properly.
```
letlocalFonts;
if(isLocalFontsApiEnabled===true){
try{
// Local Font Access API, Chrome >= 102
if(window.queryLocalFonts){
localFonts=awaitwindow.queryLocalFonts();
}
// Experimental Local Font Access API, Chrome < 102
elseif(navigator.fonts?.query){
localFonts=awaitnavigator.fonts.query({
persistentAccess:true,
});
}
}catch(error){
showError(error.message,error.name);
}
}

```

Once the list of local fonts is retrieved, a simplified and normalized `fontsIndex` is created from it:
```
letfontsIndex=[];
for(letlocalFontoflocalFonts){
letface="400";
// Determine the face name
{
letsubfamily=localFont.style.toLowerCase();
subfamily=subfamily.replaceAll(" ","");
subfamily=subfamily.replaceAll("-","");
subfamily=subfamily.replaceAll("_","");
if(subfamily.includes("thin")){
face="100";
}elseif(subfamily.includes("extralight")){
face="200";
}elseif(subfamily.includes("light")){
face="300";
}elseif(subfamily.includes("medium")){
face="500";
}elseif(subfamily.includes("semibold")){
face="600";
}elseif(subfamily.includes("extrabold")){
face="800";
}elseif(subfamily.includes("ultrabold")){
face="900";
}elseif(subfamily.includes("bold")){
face="700";
}
if(subfamily.includes("italic")){
face+="i";
}
}
letdescriptor=fontsIndex.find((descriptor)=>{
returndescriptor.family===localFont.family);
});
if(descriptor){
if(descriptor.faces.includes(face)===false){
descriptor.faces.push(face);
}
}else{
letdescriptor={
family:localFont.family,
faces:[face],
};
fontsIndex.push(descriptor);
}
}
for(letdescriptoroffontsIndex){
descriptor.faces.sort();
}

```

The normalized fonts index is then stored in the IndexedDB database so that it can be easily queried, shared between app instances, and preserved between sessions. Boxy SVG uses [Dexie.js](https://dexie.org/) to manage the database:
```
letdatabase=newDexie("LocalFontsManager");
database.version(1).stores({cache:"family"}).
awaitdatabase.cache.clear();
awaitdatabase.cache.bulkPut(fontsIndex);

```

Once the database is populated, the font picker widget can query it and display the results on the screen:
It's worth mentioning that Boxy SVG renders the list in a custom element named `<bx-fontfamilypicker>` and styles each font list item so that it's displayed in the particular font family. To isolate from the rest of the page, Boxy SVG uses the [Shadow DOM](https://developer.mozilla.org/docs/Web/Web_Components/Using_shadow_DOM) in this and other custom elements.
## Conclusions
[The local fonts feature](https://boxy-svg.com/ideas/80/system-fonts-list-in-typography-panel) has been really popular, with users enjoying access to their local fonts for their designs and creations. When the API shape changed and the [feature broke](https://boxy-svg.com/bugs/237/cant-access-local-fonts-with-chrome-102) briefly, users noted immediately. Jarosław was quick to change the code to the defensive pattern you can see in the snippet above that works with the up-to-date Chrome and also other Chromium derivatives that may not have switched to the latest version. Take Boxy SVG for a spin and be sure to check out your locally installed fonts. You might discover some long forgotten classics like [Zapf Dingbats](https://en.wikipedia.org/wiki/Zapf_Dingbats) or [Webdings](https://en.wikipedia.org/wiki/Webdings).
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2023-06-01 UTC.

