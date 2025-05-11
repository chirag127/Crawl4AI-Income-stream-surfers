---
url: https://developer.chrome.com/docs/extensions/reference/api/action
title: https://developer.chrome.com/docs/extensions/reference/api/action
date: 2025-05-11T16:52:37.953024
depth: 1
---

[ Skip to main content ](https://developer.chrome.com/docs/extensions/reference/api/action#main-content)
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




#  chrome.action 
Stay organized with collections  Save and categorize content based on your preferences. 
## Description
Use the `chrome.action` API to control the extension's icon in the Google Chrome toolbar.
The action icons are displayed in the browser toolbar next to the [omnibox](https://en.wiktionary.org/wiki/omnibox). After installation, these appear in the extensions menu (the puzzle piece icon). Users can pin your extension icon to the toolbar. 
## Availability
Chrome 88+ MV3+ 
## Manifest
The following keys must be declared [in the manifest](https://developer.chrome.com/docs/extensions/mv3/manifest) to use this API.
`"action"`
To use the `chrome.action` API, specify a `"manifest_version"` of `3` and include the `"action"` key in your [manifest file](https://developer.chrome.com/docs/extensions/reference/manifest).
```
{
"name":"Action Extension",
...
"action":{
"default_icon":{// optional
"16":"images/icon16.png",// optional
"24":"images/icon24.png",// optional
"32":"images/icon32.png"// optional
},
"default_title":"Click Me",// optional, shown in tooltip
"default_popup":"popup.html"// optional
},
...
}

```

The `"action"` key (along with its children) is optional. When it isn't included, your extension is still shown in the toolbar to provide access to the extension's menu. For this reason, we recommend that you always include at least the `"action"` and `"default_icon"` keys.
## Concepts and usage
### Parts of the UI
#### Icon
The icon is the main image on the toolbar for your extension, and is set by the `"default_icon"` key in your manifest's `"action"` key. Icons must be 16 device-independent pixels (DIPs) wide and tall.
The `"default_icon"` key is a dictionary of sizes to image paths. Chrome uses these icons to choose which image scale to use. If an exact match is not found, Chrome selects the closest available and scales it to fit the image, which might affect image quality.
Because devices with less-common scale factors like 1.5x or 1.2x are becoming more common, we encourage you to provide multiple sizes for your icons. This also futureproofs your extension against potential icon display size changes. However, if only providing a single size, the `"default_icon"` key can also be set to a string with the path to a single icon instead of a dictionary.
You can also call `action.setIcon()` to set your extension's icon programmatically by specifying a different image path or providing a dynamically-generated icon using the [HTML canvas element](https://developer.mozilla.org/docs/Web/API/HTMLCanvasElement), or, if setting from an extension service worker, the [offscreen canvas](https://developer.mozilla.org/docs/Web/API/OffscreenCanvas) API.
```
constcanvas=newOffscreenCanvas(16,16);
constcontext=canvas.getContext('2d');
context.clearRect(0,0,16,16);
context.fillStyle='#00FF00';// Green
context.fillRect(0,0,16,16);
constimageData=context.getImageData(0,0,16,16);
chrome.action.setIcon({imageData:imageData},()=>{/* ... */});

```

For packed extensions (installed from a .crx file), images can be in most formats that the Blink rendering engine can display, including PNG, JPEG, BMP, ICO, and others. SVG isn't supported. Unpacked extensions must use PNG images.
#### Tooltip (title)
The tooltip, or title, appears when the user holds their mouse pointer over the extension's icon in the toolbar. It's also included in the accessible text spoken by screen readers when the button gets focus.
The default tooltip is set using the `"default_title"` field of the `"action"` key in `manifest.json`. You can also set it programmatically by calling `action.setTitle()`.
#### Badge
Actions can optionally display a "badge" — a bit of text layered over the icon. This lets you update the action to display a small amount of information about the state of the extension, such as a counter. The badge has a text component and a background color. Because space is limited, we recommend that badge text use four or fewer characters.
To create a badge, set it programmatically by calling `action.setBadgeBackgroundColor()` and `action.setBadgeText()`. There isn't a default badge setting in the manifest. Badge color values can be either an array of four integers between 0 and 255 that make up the RGBA color of the badge or a string with a [CSS color](https://developer.mozilla.org/docs/Web/CSS/color) value.
```
chrome.action.setBadgeBackgroundColor(
{color:[0,255,0,0]},// Green
()=>{/* ... */},
);
chrome.action.setBadgeBackgroundColor(
{color:'#00FF00'},// Also green
()=>{/* ... */},
);
chrome.action.setBadgeBackgroundColor(
{color:'green'},// Also, also green
()=>{/* ... */},
);

```

#### Popup
An action's popup is shown when the user clicks on the extension's action button in the toolbar. The popup can contain any HTML contents you like, and will be automatically sized to fit its contents. The popup's size must be between 25x25 and 800x600 pixels.
The popup is initially set by the `"default_popup"` property in the `"action"` key in the `manifest.json` file. If present, this property should point to a relative path within the extension directory. It can also be updated dynamically to point to a different relative path using the `action.setPopup()` method.
## Use cases
### Per-tab state
Extension actions can have different states for each tab. To set a value for an individual tab, use the `tabId` property in the `action` API's setting methods. For example, to set the badge text for a specific tab, do something like the following:
```
functiongetTabId(){/* ... */}
functiongetTabBadge(){/* ... */}
chrome.action.setBadgeText(
{
text:getTabBadge(tabId),
tabId:getTabId(),
},
()=>{...}
);

```

If the `tabId` property is left out, the setting is treated as a global setting. Tab-specific settings take priority over global settings.
### Enabled state
By default, toolbar actions are enabled (clickable) on every tab. You can change this default by setting the `default_state` property in the `action` key of the manifest. If `default_state` is set to `"disabled"`, the action is disabled by default and must be enabled programmatically to be clickable. If `default_state` is set to `"enabled"` (the default), the action is enabled and clickable by default.
You can control the state programmatically using the `action.enable()` and `action.disable()` methods. This only affects whether the popup (if any) or `action.onClicked` event is sent to your extension; it doesn't affect the action's presence in the toolbar.
## Examples
The following examples show some common ways that actions are used in extensions. To try this API, install the [Action API example](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/api-samples/action) from the [chrome-extension-samples](https://github.com/GoogleChrome/chrome-extensions-samples) repository.
### Show a popup
It's common for an extension to display a popup when the user clicks the extension's action. To implement this in your own extension, declare the popup in your `manifest.json` and specify the content that Chrome should display in the popup.
```
// manifest.json
{
"name":"Action popup demo",
"version":"1.0",
"manifest_version":3,
"action":{
"default_title":"Click to view a popup",
"default_popup":"popup.html"
}
}

```
```
<!-- popup.html -->
<!DOCTYPE html>
<html>
<head>
 <style>
  html {
   min-height: 5em;
   min-width: 10em;
   background: salmon;
  }
 </style>
</head>
<body>
 <p>Hello, world!</p>
</body>
</html>

```

### Inject a content script on click
A common pattern for extensions is to expose their primary feature using the extension's action. The following example demonstrates this pattern. When the user clicks the action, the extension injects a content script into the current page. The content script then displays an alert to verify that everything worked as expected.
```
// manifest.json
{
"name":"Action script injection demo",
"version":"1.0",
"manifest_version":3,
"action":{
"default_title":"Click to show an alert"
},
"permissions":["activeTab","scripting"],
"background":{
"service_worker":"background.js"
}
}

```
```
// background.js
chrome.action.onClicked.addListener((tab)=>{
chrome.scripting.executeScript({
target:{tabId:tab.id},
files:['content.js']
});
});

```
```
// content.js
alert('Hello, world!');

```

### Emulate actions with declarativeContent
This example shows how an extension's background logic can (a) disable an action by default and (b) use [declarativeContent](https://developer.chrome.com/docs/extensions/reference/api/declarativeContent) to enable the action on specific sites.
```
// service-worker.js
// Wrap in an onInstalled callback to avoid unnecessary work
// every time the service worker is run
chrome.runtime.onInstalled.addListener(()=>{
// Page actions are disabled by default and enabled on select tabs
chrome.action.disable();
// Clear all rules to ensure only our expected rules are set
chrome.declarativeContent.onPageChanged.removeRules(undefined,()=>{
// Declare a rule to enable the action on example.com pages
letexampleRule={
conditions:[
newchrome.declarativeContent.PageStateMatcher({
pageUrl:{hostSuffix:'.example.com'},
})
],
actions:[newchrome.declarativeContent.ShowAction()],
};
// Finally, apply our new array of rules
letrules=[exampleRule];
chrome.declarativeContent.onPageChanged.addRules(rules);
});
});

```

## Types
### OpenPopupOptions
Chrome 99+ 
#### Properties
  * windowId
number optional
The ID of the window to open the action popup in. Defaults to the currently-active window if unspecified.


### TabDetails
#### Properties
  * tabId
number optional
The ID of the tab to query state for. If no tab is specified, the non-tab-specific state is returned.


### UserSettings
Chrome 91+ 
The collection of user-specified settings relating to an extension's action.
#### Properties
  * isOnToolbar
boolean
Whether the extension's action icon is visible on browser windows' top-level toolbar (i.e., whether the extension has been 'pinned' by the user).


### UserSettingsChange
Chrome 130+ 
#### Properties
  * isOnToolbar
boolean optional
Whether the extension's action icon is visible on browser windows' top-level toolbar (i.e., whether the extension has been 'pinned' by the user).


## Methods
### disable()
Promise 
```
chrome.action.disable(  tabId?: number,  callback?: function,)
```

Disables the action for a tab.
#### Parameters
  * tabId
number optional
The ID of the tab for which you want to modify the action.
  * callback
function optional
The `callback` parameter looks like: 
```
() => void
```



#### Returns
  * Promise<void>
Promises are supported in Manifest V3 and later, but callbacks are provided for backward compatibility. You cannot use both on the same function call. The promise resolves with the same type that is passed to the callback. 


### enable()
Promise 
```
chrome.action.enable(  tabId?: number,  callback?: function,)
```

Enables the action for a tab. By default, actions are enabled.
#### Parameters
  * tabId
number optional
The ID of the tab for which you want to modify the action.
  * callback
function optional
The `callback` parameter looks like: 
```
() => void
```



#### Returns
  * Promise<void>
Promises are supported in Manifest V3 and later, but callbacks are provided for backward compatibility. You cannot use both on the same function call. The promise resolves with the same type that is passed to the callback. 


### getBadgeBackgroundColor()
Promise 
```
chrome.action.getBadgeBackgroundColor(  details: [TabDetails](https://developer.chrome.com/docs/extensions/reference/api/action#type-TabDetails),  callback?: function,)
```

Gets the background color of the action.
#### Parameters
  * details
[TabDetails](https://developer.chrome.com/docs/extensions/reference/api/action#type-TabDetails)
  * callback
function optional
The `callback` parameter looks like: 
```
(result: [ColorArray](https://developer.chrome.com/docs/extensions/reference/browserAction/#type-ColorArray)) => void
```

    * result
[ColorArray](https://developer.chrome.com/docs/extensions/reference/browserAction/#type-ColorArray)


#### Returns
  * Promise<[browserAction.ColorArray](https://developer.chrome.com/docs/extensions/reference/browserAction/#type-ColorArray)>
Promises are supported in Manifest V3 and later, but callbacks are provided for backward compatibility. You cannot use both on the same function call. The promise resolves with the same type that is passed to the callback. 


### getBadgeText()
Promise 
```
chrome.action.getBadgeText(  details: [TabDetails](https://developer.chrome.com/docs/extensions/reference/api/action#type-TabDetails),  callback?: function,)
```

Gets the badge text of the action. If no tab is specified, the non-tab-specific badge text is returned. If [displayActionCountAsBadgeText](https://developer.chrome.com/docs/extensions/reference/declarativeNetRequest/#setExtensionActionOptions) is enabled, a placeholder text will be returned unless the [declarativeNetRequestFeedback](https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions#declarativeNetRequestFeedback) permission is present or tab-specific badge text was provided.
#### Parameters
  * details
[TabDetails](https://developer.chrome.com/docs/extensions/reference/api/action#type-TabDetails)
  * callback
function optional
The `callback` parameter looks like: 
```
(result: string) => void
```

    * result
string


#### Returns
  * Promise<string>
Promises are supported in Manifest V3 and later, but callbacks are provided for backward compatibility. You cannot use both on the same function call. The promise resolves with the same type that is passed to the callback. 


### getBadgeTextColor()
Promise Chrome 110+ 
```
chrome.action.getBadgeTextColor(  details: [TabDetails](https://developer.chrome.com/docs/extensions/reference/api/action#type-TabDetails),  callback?: function,)
```

Gets the text color of the action.
#### Parameters
  * details
[TabDetails](https://developer.chrome.com/docs/extensions/reference/api/action#type-TabDetails)
  * callback
function optional
The `callback` parameter looks like: 
```
(result: [ColorArray](https://developer.chrome.com/docs/extensions/reference/browserAction/#type-ColorArray)) => void
```

    * result
[ColorArray](https://developer.chrome.com/docs/extensions/reference/browserAction/#type-ColorArray)


#### Returns
  * Promise<[browserAction.ColorArray](https://developer.chrome.com/docs/extensions/reference/browserAction/#type-ColorArray)>
Promises are supported in Manifest V3 and later, but callbacks are provided for backward compatibility. You cannot use both on the same function call. The promise resolves with the same type that is passed to the callback. 


### getPopup()
Promise 
```
chrome.action.getPopup(  details: [TabDetails](https://developer.chrome.com/docs/extensions/reference/api/action#type-TabDetails),  callback?: function,)
```

Gets the html document set as the popup for this action.
#### Parameters
  * details
[TabDetails](https://developer.chrome.com/docs/extensions/reference/api/action#type-TabDetails)
  * callback
function optional
The `callback` parameter looks like: 
```
(result: string) => void
```

    * result
string


#### Returns
  * Promise<string>
Promises are supported in Manifest V3 and later, but callbacks are provided for backward compatibility. You cannot use both on the same function call. The promise resolves with the same type that is passed to the callback. 


### getTitle()
Promise 
```
chrome.action.getTitle(  details: [TabDetails](https://developer.chrome.com/docs/extensions/reference/api/action#type-TabDetails),  callback?: function,)
```

Gets the title of the action.
#### Parameters
  * details
[TabDetails](https://developer.chrome.com/docs/extensions/reference/api/action#type-TabDetails)
  * callback
function optional
The `callback` parameter looks like: 
```
(result: string) => void
```

    * result
string


#### Returns
  * Promise<string>
Promises are supported in Manifest V3 and later, but callbacks are provided for backward compatibility. You cannot use both on the same function call. The promise resolves with the same type that is passed to the callback. 


### getUserSettings()
Promise Chrome 91+ 
```
chrome.action.getUserSettings(  callback?: function,)
```

Returns the user-specified settings relating to an extension's action.
#### Parameters
  * callback
function optional
The `callback` parameter looks like: 
```
(userSettings: [UserSettings](https://developer.chrome.com/docs/extensions/reference/api/action#type-UserSettings)) => void
```

    * userSettings
[UserSettings](https://developer.chrome.com/docs/extensions/reference/api/action#type-UserSettings)


#### Returns
  * Promise<[UserSettings](https://developer.chrome.com/docs/extensions/reference/api/action#type-UserSettings)>
Promises are supported in Manifest V3 and later, but callbacks are provided for backward compatibility. You cannot use both on the same function call. The promise resolves with the same type that is passed to the callback. 


### isEnabled()
Promise Chrome 110+ 
```
chrome.action.isEnabled(  tabId?: number,  callback?: function,)
```

Indicates whether the extension action is enabled for a tab (or globally if no `tabId` is provided). Actions enabled using only [`declarativeContent`](https://developer.chrome.com/docs/extensions/reference/declarativeContent/) always return false.
#### Parameters
  * tabId
number optional
The ID of the tab for which you want check enabled status.
  * callback
function optional
The `callback` parameter looks like: 
```
(isEnabled: boolean) => void
```

    * isEnabled
boolean
True if the extension action is enabled.


#### Returns
  * Promise<boolean>
Promises are supported in Manifest V3 and later, but callbacks are provided for backward compatibility. You cannot use both on the same function call. The promise resolves with the same type that is passed to the callback. 


### openPopup()
Promise Chrome 127+ 
```
chrome.action.openPopup(  options?: [OpenPopupOptions](https://developer.chrome.com/docs/extensions/reference/api/action#type-OpenPopupOptions),  callback?: function,)
```

Opens the extension's popup. Between Chrome 118 and Chrome 126, this is only available to policy installed extensions.
#### Parameters
  * options
[OpenPopupOptions](https://developer.chrome.com/docs/extensions/reference/api/action#type-OpenPopupOptions) optional
Specifies options for opening the popup.
  * callback
function optional
The `callback` parameter looks like: 
```
() => void
```



#### Returns
  * Promise<void>
Promises are supported in Manifest V3 and later, but callbacks are provided for backward compatibility. You cannot use both on the same function call. The promise resolves with the same type that is passed to the callback. 


### setBadgeBackgroundColor()
Promise 
```
chrome.action.setBadgeBackgroundColor(  details: object,  callback?: function,)
```

Sets the background color for the badge.
#### Parameters
  * details
object
    * color
string | [ColorArray](https://developer.chrome.com/docs/extensions/reference/browserAction/#type-ColorArray)
An array of four integers in the range [0,255] that make up the RGBA color of the badge. For example, opaque red is `[255, 0, 0, 255]`. Can also be a string with a CSS value, with opaque red being `#FF0000` or `#F00`.
    * tabId
number optional
Limits the change to when a particular tab is selected. Automatically resets when the tab is closed.
  * callback
function optional
The `callback` parameter looks like: 
```
() => void
```



#### Returns
  * Promise<void>
Promises are supported in Manifest V3 and later, but callbacks are provided for backward compatibility. You cannot use both on the same function call. The promise resolves with the same type that is passed to the callback. 


### setBadgeText()
Promise 
```
chrome.action.setBadgeText(  details: object,  callback?: function,)
```

Sets the badge text for the action. The badge is displayed on top of the icon.
#### Parameters
  * details
object
    * tabId
number optional
Limits the change to when a particular tab is selected. Automatically resets when the tab is closed.
    * text
string optional
Any number of characters can be passed, but only about four can fit in the space. If an empty string (`''`) is passed, the badge text is cleared. If `tabId` is specified and `text` is null, the text for the specified tab is cleared and defaults to the global badge text.
  * callback
function optional
The `callback` parameter looks like: 
```
() => void
```



#### Returns
  * Promise<void>
Promises are supported in Manifest V3 and later, but callbacks are provided for backward compatibility. You cannot use both on the same function call. The promise resolves with the same type that is passed to the callback. 


### setBadgeTextColor()
Promise Chrome 110+ 
```
chrome.action.setBadgeTextColor(  details: object,  callback?: function,)
```

Sets the text color for the badge.
#### Parameters
  * details
object
    * color
string | [ColorArray](https://developer.chrome.com/docs/extensions/reference/browserAction/#type-ColorArray)
An array of four integers in the range [0,255] that make up the RGBA color of the badge. For example, opaque red is `[255, 0, 0, 255]`. Can also be a string with a CSS value, with opaque red being `#FF0000` or `#F00`. Not setting this value will cause a color to be automatically chosen that will contrast with the badge's background color so the text will be visible. Colors with alpha values equivalent to 0 will not be set and will return an error.
    * tabId
number optional
Limits the change to when a particular tab is selected. Automatically resets when the tab is closed.
  * callback
function optional
The `callback` parameter looks like: 
```
() => void
```



#### Returns
  * Promise<void>
Promises are supported in Manifest V3 and later, but callbacks are provided for backward compatibility. You cannot use both on the same function call. The promise resolves with the same type that is passed to the callback. 


### setIcon()
Promise 
```
chrome.action.setIcon(  details: object,  callback?: function,)
```

Sets the icon for the action. The icon can be specified either as the path to an image file or as the pixel data from a canvas element, or as dictionary of either one of those. Either the **path** or the **imageData** property must be specified.
#### Parameters
  * details
object
    * imageData
ImageData | object optional
Either an ImageData object or a dictionary {size -> ImageData} representing icon to be set. If the icon is specified as a dictionary, the actual image to be used is chosen depending on screen's pixel density. If the number of image pixels that fit into one screen space unit equals `scale`, then image with size `scale` * n will be selected, where n is the size of the icon in the UI. At least one image must be specified. Note that 'details.imageData = foo' is equivalent to 'details.imageData = {'16': foo}'
    * path
string | object optional
Either a relative image path or a dictionary {size -> relative image path} pointing to icon to be set. If the icon is specified as a dictionary, the actual image to be used is chosen depending on screen's pixel density. If the number of image pixels that fit into one screen space unit equals `scale`, then image with size `scale` * n will be selected, where n is the size of the icon in the UI. At least one image must be specified. Note that 'details.path = foo' is equivalent to 'details.path = {'16': foo}'
    * tabId
number optional
Limits the change to when a particular tab is selected. Automatically resets when the tab is closed.
  * callback
function optional
The `callback` parameter looks like: 
```
() => void
```



#### Returns
  * Promise<void>
Chrome 96+ 
Promises are supported in Manifest V3 and later, but callbacks are provided for backward compatibility. You cannot use both on the same function call. The promise resolves with the same type that is passed to the callback. 


### setPopup()
Promise 
```
chrome.action.setPopup(  details: object,  callback?: function,)
```

Sets the HTML document to be opened as a popup when the user clicks on the action's icon.
#### Parameters
  * details
object
    * popup
string
The relative path to the HTML file to show in a popup. If set to the empty string (`''`), no popup is shown.
    * tabId
number optional
Limits the change to when a particular tab is selected. Automatically resets when the tab is closed.
  * callback
function optional
The `callback` parameter looks like: 
```
() => void
```



#### Returns
  * Promise<void>
Promises are supported in Manifest V3 and later, but callbacks are provided for backward compatibility. You cannot use both on the same function call. The promise resolves with the same type that is passed to the callback. 


### setTitle()
Promise 
```
chrome.action.setTitle(  details: object,  callback?: function,)
```

Sets the title of the action. This shows up in the tooltip.
#### Parameters
  * details
object
    * tabId
number optional
Limits the change to when a particular tab is selected. Automatically resets when the tab is closed.
    * title
string
The string the action should display when moused over.
  * callback
function optional
The `callback` parameter looks like: 
```
() => void
```



#### Returns
  * Promise<void>
Promises are supported in Manifest V3 and later, but callbacks are provided for backward compatibility. You cannot use both on the same function call. The promise resolves with the same type that is passed to the callback. 


## Events
### onClicked
```
chrome.action.onClicked.addListener(  callback: function,)
```

Fired when an action icon is clicked. This event will not fire if the action has a popup.
#### Parameters
  * callback
function
The `callback` parameter looks like: 
```
(tab: [tabs.Tab](https://developer.chrome.com/docs/extensions/reference/tabs/#type-Tab)) => void
```

    * tab
[tabs.Tab](https://developer.chrome.com/docs/extensions/reference/tabs/#type-Tab)


### onUserSettingsChanged
Chrome 130+ 
```
chrome.action.onUserSettingsChanged.addListener(  callback: function,)
```

Fired when user-specified settings relating to an extension's action change.
#### Parameters
  * callback
function
The `callback` parameter looks like: 
```
(change: [UserSettingsChange](https://developer.chrome.com/docs/extensions/reference/api/action#type-UserSettingsChange)) => void
```

    * change
[UserSettingsChange](https://developer.chrome.com/docs/extensions/reference/api/action#type-UserSettingsChange)


Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-12-12 UTC.

