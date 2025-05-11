---
url: https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager
title: https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager
date: 2025-05-11T16:51:54.735737
depth: 1
---

[ Skip to main content ](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager?hl=es-419)




  * On this page
  * [Before you start](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager#prereq)
  * [Build the extension](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager#build)
    * [Step 1: Add the extension data and icons](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager#step-1)
    * [Step 2: Create and style the popup](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager#step-2)
    * [Step 3: Manage the tabs](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager#step-3)
  * [Test that it works](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager#try-out)
    * [Load your extension locally](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager#locally)
    * [Open a few documentation pages](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager#open-sites)
  * [🎯 Potential enhancements](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager#challenge)
  * [Keep building!](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager#continue)
  * [Continue exploring](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager#continue_exploring)




Was this helpful?
#  Manage tabs 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you start](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager#prereq)
  * [Build the extension](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager#build)
    * [Step 1: Add the extension data and icons](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager#step-1)
    * [Step 2: Create and style the popup](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager#step-2)
    * [Step 3: Manage the tabs](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager#step-3)
  * [Test that it works](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager#try-out)
    * [Load your extension locally](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager#locally)
    * [Open a few documentation pages](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager#open-sites)
  * [🎯 Potential enhancements](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager#challenge)
  * [Keep building!](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager#continue)
  * [Continue exploring](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager#continue_exploring)


Build your first tabs manager.
## Overview
This tutorial builds a tabs manager to organize your Chrome extension and Chrome Web store documentation tabs.
Tabs Manager extension 
In this guide, we're going to explain how to do the following:
  * Create an extension popup using the [Action](https://developer.chrome.com/docs/extensions/reference/api/action) API.
  * Query for specific tabs using the [Tabs](https://developer.chrome.com/docs/extensions/reference/api/tabs) API.
  * Preserve user privacy through narrow host permissions.
  * Change the focus of the tab.
  * Move tabs to the same window and group them.
  * Rename tab groups using the [TabGroups](https://developer.chrome.com/docs/extensions/reference/api/tabGroups) API.


## Before you start
This guide assumes that you have basic web development experience. We recommend checking out [Hello World](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world) for an introduction to the extension development workflow.
## Build the extension
To start, create a new directory called `tabs-manager` to hold the extension's files. If you prefer, you can download the complete source code on [GitHub](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/functional-samples/tutorial.tabs-manager).
### Step 1: Add the extension data and icons
Create a file called `manifest.json` and add the following code:
```
{
"manifest_version":3,
"name":"Tab Manager for Chrome Dev Docs",
"version":"1.0",
"icons":{
"16":"images/icon-16.png",
"32":"images/icon-32.png",
"48":"images/icon-48.png",
"128":"images/icon-128.png"
}
}

```

To learn more about these manifest keys, check out the Reading time tutorial that explains the extension's [metadata](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-on-every-tab#step-1) and [icons](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-on-every-tab#step-2) in more detail.
Create an `images` folder then [download the icons](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/functional-samples/tutorial.tabs-manager/images) into it.
### Step 2: Create and style the popup
The [Action](https://developer.chrome.com/docs/extensions/reference/api/action) API controls the extension action (toolbar icon). When the user clicks on the extension action, it will either run some code or open a popup, like in this case. Start by declaring the popup in the `manifest.json`:
```
{
"action":{
"default_popup":"popup.html"
}
}

```

A popup is similar to a web page with one exception: it can't run inline JavaScript. Create a `popup.html` file and add the following code:
```
<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" href="./popup.css" />
 </head>
 <body>
  <template id="li_template">
   <li>
    <a>
     <h3 class="title">Tab Title</h3>
     <p class="pathname">Tab Pathname</p>
    </a>
   </li>
  </template>
  <h1>Google Dev Docs</h1>
  <button>Group Tabs</button>
  <ul></ul>
  <script src="./popup.js" type="module"></script>
 </body>
</html>

```

Next, you'll style the popup. Create a `popup.css` file and add the following code:
```
body{
width:20rem;
}
ul{
list-style-type:none;
padding-inline-start:0;
margin:1rem0;
}
li{
padding:0.25rem;
}
li:nth-child(odd){
background:#80808030;
}
li:nth-child(even){
background:#ffffff;
}
h3,
p{
margin:0;
}

```

### Step 3: Manage the tabs
The [Tabs API](https://developer.chrome.com/docs/extensions/reference/api/tabs) allows an extension to create, query, modify, and rearrange tabs in the browser.
#### Request permission
Many methods in the Tabs API can be used without requesting any permission. However, we need access to the `title` and the `URL` of the tabs; these sensitive properties require permission. We could request `"tabs"` permission, but this would give access to the sensitive properties of **all** tabs. Since we are only managing tabs of a specific site, we will request narrow host permissions.
Narrow [host permissions](https://developer.chrome.com/docs/extensions/develop/concepts/match-patterns) allow us to protect user privacy by granting elevated permission to **specific sites**. This will grant access to the `title`, and `URL` properties, as well as additional capabilities. Add the highlighted code to the `manifest.json` file:
```
{
 "host_permissions": [
  "https://developer.chrome.com/*"
 ]
}

```

💡 **What are the main differences between the tabs permission and host permissions?**
Both the `"tabs"` permission and host permissions have drawbacks.
The `"tabs"` permission grants an extension the ability to read sensitive data on all tabs. Over time, this information could be used to collect a user's browsing history. As such, if you request this permission Chrome will display the following warning message at install time:
Host permissions allow an extension to read and query a matching tab's sensitive properties, plus inject scripts on these tabs. Users will see the following warning message at install time:
These warning can be alarming for users. For a better onboarding experience, we recommend implementing [optional permissions](https://developer.chrome.com/docs/extensions/reference/api/permissions).
#### Query the tabs
You can retrieve the tabs from specific URLs using the `tabs.query()` method. Create a `popup.js` file and add the following code:
```
consttabs=awaitchrome.tabs.query({
url:[
"https://developer.chrome.com/docs/webstore/*",
"https://developer.chrome.com/docs/extensions/*",
]
});

```

💡 **Can I use Chrome APIs directly in the popup?**
A popup and other extension pages can call any [Chrome API](https://developer.chrome.com/docs/extensions/reference) because they are served from the chrome schema. For example `chrome-extension://EXTENSION_ID/popup.html`.
#### Focus on a tab
First, the extension will sort tab names (the titles of the contained HTML pages) alphabetically. Then, when a list item is clicked, it will focus on that tab using `tabs.update()` and bring the window to the front using `windows.update()`. Add the following code to the `popup.js` file:
```
...
constcollator=newIntl.Collator();
tabs.sort((a,b)=>collator.compare(a.title,b.title));
consttemplate=document.getElementById("li_template");
constelements=newSet();
for(consttaboftabs){
constelement=template.content.firstElementChild.cloneNode(true);
consttitle=tab.title.split("-")[0].trim();
constpathname=newURL(tab.url).pathname.slice("/docs".length);
element.querySelector(".title").textContent=title;
element.querySelector(".pathname").textContent=pathname;
element.querySelector("a").addEventListener("click",async()=>{
// need to focus window as well as the active tab
awaitchrome.tabs.update(tab.id,{active:true});
awaitchrome.windows.update(tab.windowId,{focused:true});
});
elements.add(element);
}
document.querySelector("ul").append(...elements);
...

```

💡 **Interesting JavaScript used in this code**
  * The [Collator](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Intl/Collator) used to sort the tabs array by the user's preferred language.
  * The [template tag](https://web.dev/webcomponents-template/) used to define an HTML element that can be cloned instead of using `document.createElement()` to create each item.
  * The [URL constructor](https://developer.mozilla.org/docs/Web/API/URL/URL) used to create and parse URLs.
  * The [Spread syntax](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Operators/Spread_syntax) used to convert the Set of elements into arguments in the `append()` call.


#### Group the tabs
The [TabGroups](https://developer.chrome.com/docs/extensions/reference/api/tabGroups) API allows the extension to name the group and choose a background color. Add the `"tabGroups"` permission to the manifest by adding the highlighted code:
```
{
 "permissions": [
  "tabGroups"
 ]
}

```

In `popup.js`, add the following code to create a button that will group all the tabs using [`tabs.group()`](https://developer.chrome.com/docs/extensions/reference/api/tabGroups) and move them into the current window.
```
constbutton=document.querySelector("button");
button.addEventListener("click",async()=>{
consttabIds=tabs.map(({id})=>id);
if(tabIds.length){
constgroup=awaitchrome.tabs.group({tabIds});
awaitchrome.tabGroups.update(group,{title:"DOCS"});
}
});

```

## Test that it works
Verify that the file structure of your project matches the following directory tree:
### Load your extension locally
To load an unpacked extension in developer mode, follow the steps in [Hello World](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world#load-unpacked).
### Open a few documentation pages
Open the following docs in different windows:
  * [Design the user interface](https://developer.chrome.com/docs/extensions/develop/ui)
  * [Discovery on the Chrome Web Store](https://developer.chrome.com/docs/webstore/discovery)
  * [Extension development overview](https://developer.chrome.com/docs/extensions/develop)
  * [Manifest file format](https://developer.chrome.com/docs/extensions/reference/manifest)
  * [Publish in the Chrome Web Store](https://developer.chrome.com/docs/webstore/publish)


Click the popup. It should look like this:
Tabs Manager extension popup 
Click the "Group tabs" button. It should look like this:
Grouped tabs using the Tabs Manager extension 
## 🎯 Potential enhancements
Based on what you've learned today, try to implement any of the following:
  * Customize the popup style sheet.
  * Change the color and title of the tab group.
  * Manage the tabs of another documentation site.
  * Add support for ungrouping the grouped tabs.


## Keep building!
Congratulations on finishing this tutorial 🎉. Continue developing your skills by completing other tutorials on this series:
Extension | What you will learn  
---|---  
To insert an element on every page automatically.  
To run code on the current page after clicking on the extension action.  
## Continue exploring
We hope you enjoyed building this Chrome extension and are excited to continue your Chrome development learning journey. We recommend the following learning path:
  * The [developer's guide](https://developer.chrome.com/docs/extensions/develop) has dozens of additional links to pieces of documentation relevant to advanced extension creation.
  * Extensions have access to powerful APIs beyond what's available on the open web. The [Chrome APIs documentation](https://developer.chrome.com/docs/extensions/reference) walks through each API.


Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2022-10-04 UTC.

