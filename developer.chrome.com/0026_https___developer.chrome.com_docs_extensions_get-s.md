---
url: https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab
title: https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab
date: 2025-05-11T16:51:54.708375
depth: 1
---

[ Skip to main content ](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab?hl=es-419)




  * On this page
  * [Before you start](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#prereq)
  * [Build the extension](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#build)
    * [Step 1: Add the extension data and icons](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#step-1)
    * [Step 2: Initialize the extension](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#step-2)
    * [Step 3: Enable the extension action](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#step-3)
    * [Step 4: Track the state of the current tab](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#step-4)
    * [Step 5: Add or remove the style sheet](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#step-5)
    * [Optional: Assign a keyboard shortcut](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#step-6)
  * [Test that it works](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#try-out)
    * [Load your extension locally](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#locally)
    * [Test the extension on a documentation page](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#open-sites)
  * [🎯 Potential enhancements](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#challenge)
  * [Keep building.](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#continue)
  * [Continue exploring](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#continue_exploring)




Was this helpful?
#  Inject scripts into the active tab 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you start](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#prereq)
  * [Build the extension](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#build)
    * [Step 1: Add the extension data and icons](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#step-1)
    * [Step 2: Initialize the extension](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#step-2)
    * [Step 3: Enable the extension action](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#step-3)
    * [Step 4: Track the state of the current tab](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#step-4)
    * [Step 5: Add or remove the style sheet](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#step-5)
    * [Optional: Assign a keyboard shortcut](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#step-6)
  * [Test that it works](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#try-out)
    * [Load your extension locally](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#locally)
    * [Test the extension on a documentation page](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#open-sites)
  * [🎯 Potential enhancements](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#challenge)
  * [Keep building.](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#continue)
  * [Continue exploring](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#continue_exploring)


Simplify the styling of the current page by clicking the extension toolbar icon.
## Overview
This tutorial builds an extension that simplifies the styling of the Chrome extension and Chrome Web Store documentation pages so that they are easier to read.
In this guide, we're going to explain how to do the following:
  * Use the extension service worker as the event coordinator.
  * Preserve user privacy through the `"activeTab"` permission.
  * Run code when the user clicks the extension toolbar icon.
  * Insert and remove a style sheet using the [Scripting](https://developer.chrome.com/docs/extensions/reference/api/scripting) API.
  * Use a keyboard shortcut to execute code.


## Before you start
This guide assumes that you have basic web development experience. We recommend checking out [Hello World](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world) for an introduction to the extension development workflow.
## Build the extension
To start, create a new directory called `focus-mode` that will hold the extension's files. If you prefer, you can download the complete source code from [GitHub](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/functional-samples/tutorial.focus-mode).
### Step 1: Add the extension data and icons
Create a file called `manifest.json` and include the following code.
```
{
"manifest_version":3,
"name":"Focus Mode",
"description":"Enable focus mode on Chrome's official Extensions and Chrome Web Store documentation.",
"version":"1.0",
"icons":{
"16":"images/icon-16.png",
"32":"images/icon-32.png",
"48":"images/icon-48.png",
"128":"images/icon-128.png"
}
}

```

To learn more about these manifest keys, check out the "Run scripts on every tab" tutorial that explains the extension's [metadata](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-on-every-tab#step-1) and [icons](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-on-every-tab#step-2) in more detail.
Create an `images` folder then [download the icons](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/functional-samples/tutorial.focus-mode/images) into it.
### Step 2: Initialize the extension
Extensions can monitor browser events in the background using the [extension's service worker](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers). Service workers are special JavaScript environments that handle events and terminate when they're not needed.
Start by registering the service worker in the `manifest.json` file:
```
{
...
"background":{
"service_worker":"background.js"
},
...
}

```

Create a file called `background.js` and add the following code:
```
chrome.runtime.onInstalled.addListener(()=>{
chrome.action.setBadgeText({
text:"OFF",
});
});

```

The first event our service worker will listen for is [`runtime.onInstalled()`](https://developer.chrome.com/docs/extensions/reference/api/runtime#event-onInstalled). This method allows the extension to set an initial state or complete some tasks on installation. Extensions can use the [Storage API](https://developer.chrome.com/docs/extensions/reference/api/storage) and [IndexedDB](https://developer.mozilla.org/docs/Web/API/IndexedDB_API) to store the application state. In this case, though, since we're only handling two states, we will use the _action's badge_ text itself to track whether the extension is 'ON' or 'OFF'.
### Step 3: Enable the extension action
The _extension action_ controls the extension's toolbar icon. So whenever the user clicks the extension icon, it will either run some code (like in this example) or display a popup. Add the following code to declare the extension action in the `manifest.json` file:
```
{
...
"action":{
"default_icon":{
"16":"images/icon-16.png",
"32":"images/icon-32.png",
"48":"images/icon-48.png",
"128":"images/icon-128.png"
}
},
...
}

```

#### Use the activeTab permission to protect user privacy
The [`activeTab`](https://developer.chrome.com/docs/extensions/develop/concepts/activeTab) permission grants the extension _temporary_ ability to execute code on the active tab. It also allows access to [sensitive properties](https://developer.chrome.com/docs/extensions/develop/concepts/activeTab#what-activeTab-allows) of the current tab.
This permission is enabled when the user **_invokes_** the extension. In this case, the user invokes the extension by clicking on the extension action.
💡 **What other user interactions enable the activeTab permission in my own extension?**
  * Pressing a keyboard shortcut combination.
  * Selecting a context menu item.
  * Accepting a suggestion from the omnibox.
  * Opening an extension popup.


The `"activeTab"` permission allows users to _purposefully_ choose to run the extension on the focused tab; this way, it protects the user's privacy. Another benefit is that it does not trigger a [permission warning](https://developer.chrome.com/docs/extensions/develop/concepts/permission-warnings#permissions_with_warnings).
To use the `"activeTab"` permission, add it to the manifest's permission array:
```
{
...
"permissions":["activeTab"],
...
}

```

### Step 4: Track the state of the current tab
After the user clicks the extension action, the extension will check if the URL matches a documentation page. Next, it will check the state of the current tab and set the next state. Add the following code to `background.js`:
```
constextensions='https://developer.chrome.com/docs/extensions';
constwebstore='https://developer.chrome.com/docs/webstore';
chrome.action.onClicked.addListener(async(tab)=>{
if(tab.url.startsWith(extensions)||tab.url.startsWith(webstore)){
// Retrieve the action badge to check if the extension is 'ON' or 'OFF'
constprevState=awaitchrome.action.getBadgeText({tabId:tab.id});
// Next state will always be the opposite
constnextState=prevState==='ON'?'OFF':'ON';
// Set the action badge to the next state
awaitchrome.action.setBadgeText({
tabId:tab.id,
text:nextState,
});
}
});

```

### Step 5: Add or remove the style sheet
Now it's time to change the layout of the page. Create a file named `focus-mode.css` and include the following code:
```
*{
display:none!important;
}
html,
body,
*:has(article),
article,
article*{
display:revert!important;
}
[role='navigation']{
display:none!important;
}
article{
margin:auto;
max-width:700px;
}

```

Insert or remove the style sheet using the [Scripting](https://developer.chrome.com/docs/extensions/reference/api/scripting) API. Start by declaring the `"scripting"` permission in the manifest:
```
{
...
"permissions":["activeTab","scripting"],
...
}

```

Finally, in `background.js` add the following code to change the layout of the page:
```
...
if(nextState==="ON"){
// Insert the CSS file when the user turns the extension on
awaitchrome.scripting.insertCSS({
files:["focus-mode.css"],
target:{tabId:tab.id},
});
}elseif(nextState==="OFF"){
// Remove the CSS file when the user turns the extension off
awaitchrome.scripting.removeCSS({
files:["focus-mode.css"],
target:{tabId:tab.id},
});
}
}
});

```

💡 **Can I use the Scripting API to inject code instead of a style sheet?**
Yes. You can use [`scripting.executeScript()`](https://developer.chrome.com/docs/extensions/reference/api/scripting#injected-code) to inject JavaScript.
### _Optional: Assign a keyboard shortcut_
Just for fun, add a shortcut to make it easier to enable or disable focus mode. Add the `"commands"` key to the manifest.
```
{
...
"commands":{
"_execute_action":{
"suggested_key":{
"default":"Ctrl+B",
"mac":"Command+B"
}
}
}
}

```

The `"_execute_action"` key runs the same code as the `action.onClicked()` event, so no additional code is needed.
## Test that it works
Verify that the file structure of your project looks like the following:
### Load your extension locally
To load an unpacked extension in developer mode, follow the steps in [Hello World](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world#load-unpacked).
### Test the extension on a documentation page
First, open any of the following pages:
  * [Welcome to the Chrome Extension documentation](https://developer.chrome.com/docs/extensions)
  * [Publish in the Chrome Web Store](https://developer.chrome.com/docs/webstore/publish)


Then, click the extension action. If you set up a [keyboard shortcut](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#step-6), you can test it by pressing `Ctrl + B` or `Cmd + B`.
It should go from this:
Focus Mode extension off 
To this:
Focus Mode extension on 
## 🎯 Potential enhancements
Based on what you've learned today, try to accomplish any of the following:
  * Improve the CSS style sheet.
  * Assign a different keyboard shortcut.
  * Change the layout of your favorite blog or documentation site.


## Keep building.
Congratulations on finishing this tutorial 🎉. Continue leveling up your skills by completing other tutorials on this series:
Extension | What you will learn  
---|---  
To insert an element on a specific set of pages automatically.  
To create a popup that manages browser tabs.  
## Continue exploring
We hope you enjoyed building this Chrome extension and are excited to continue your extension development learning journey. We recommend the following learning paths:
  * The [developer's guide](https://developer.chrome.com/docs/extensions/develop) has dozens of additional links to pieces of documentation relevant to advanced extension creation.
  * Extensions have access to powerful APIs beyond what's available on the open web. The [Chrome APIs documentation](https://developer.chrome.com/docs/extensions/reference/api) walks through each API.


Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2022-10-04 UTC.

