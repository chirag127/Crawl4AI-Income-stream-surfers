---
url: https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts
title: https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts
date: 2025-05-11T16:51:49.667250
depth: 1
---

[ Skip to main content ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=es-419)




  * On this page
  * [Understand content script capabilities](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#capabilities)
  * [Work in isolated worlds](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#isolated_world)
  * [Inject scripts](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#functionality)
    * [Inject with static declarations](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#static-declarative)
    * [Inject with dynamic declarations](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#dynamic-declarative)
    * [Inject programmatically](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#programmatic)
    * [Exclude matches and globs](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#matchAndGlob)
    * [Specify frames](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#frames)
    * [Inject in to related frames](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#injecting-in-related-frames)
  * [Communication with the embedding page](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#host-page-communication)
  * [Access extension files](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#files)




Was this helpful?
#  Content scripts 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Understand content script capabilities](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#capabilities)
  * [Work in isolated worlds](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#isolated_world)
  * [Inject scripts](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#functionality)
    * [Inject with static declarations](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#static-declarative)
    * [Inject with dynamic declarations](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#dynamic-declarative)
    * [Inject programmatically](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#programmatic)
    * [Exclude matches and globs](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#matchAndGlob)
    * [Specify frames](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#frames)
    * [Inject in to related frames](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#injecting-in-related-frames)
  * [Communication with the embedding page](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#host-page-communication)
  * [Access extension files](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#files)


Content scripts are files that run in the context of web pages. Using the standard [Document Object Model](https://developer.mozilla.org/docs/Web/API/Document_Object_Model) (DOM), they are able to read details of the web pages the browser visits, make changes to them, and pass information to their parent extension.
## Understand content script capabilities
Content scripts can access the following extension APIs directly:
  * [`runtime.getManifest()`](https://developer.chrome.com/docs/extensions/reference/api/runtime#method-getManifest)
  * [`runtime.sendMessage()`](https://developer.chrome.com/docs/extensions/reference/api/runtime#method-sendMessage)


Content scripts are unable to access other APIs directly. But they can access them indirectly by [exchanging messages](https://developer.chrome.com/docs/extensions/develop/concepts/messaging) with other parts of your extension.
You can also access other files in your extension from a content script, using APIs like `fetch()`. To do this, you need to declare them as [web-accessible resources](https://developer.chrome.com/docs/extensions/reference/manifest/web-accessible-resources). Note that this also exposes the resources to any first-party or third-party scripts running on the same site.
## Work in isolated worlds
Content scripts live in an isolated world, allowing a content script to make changes to its JavaScript environment without conflicting with the page or other extensions' content scripts.
An extension may run in a web page with code similar to the following example.
webPage.html
```
<html>
 <button id="mybutton">click me</button>
 <script>
  var greeting = "hello, ";
  var button = document.getElementById("mybutton");
  button.person_name = "Bob";
  button.addEventListener(
    "click", () => alert(greeting + button.person_name + "."), false);
 </script>
</html>

```

That extension could inject the following content script using one of the techniques outlined in the [Inject scripts](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#functionality) section.
content-script.js
```
vargreeting="hola, ";
varbutton=document.getElementById("mybutton");
button.person_name="Roberto";
button.addEventListener(
"click",()=>alert(greeting+button.person_name+"."),false);

```

With this change, both alerts appear in sequence when the button is clicked.
## Inject scripts
Content scripts can be [declared statically](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#static-declarative), [declared dynamically](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#dynamic-declarative), or [programmatically injected](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#programmatic).
### Inject with static declarations
Use static content script declarations in manifest.json for scripts that should be automatically run on a well known set of pages.
Statically declared scripts are registered in the manifest under the `"content_scripts"` key. They can include JavaScript files, CSS files, or both. All auto-run content scripts must specify [match patterns](https://developer.chrome.com/docs/extensions/develop/concepts/match-patterns).
manifest.json
```
{
 "name": "My extension",
 ...
 "content_scripts": [
  {
   "matches": ["https://*.nytimes.com/*"],
   "css": ["my-styles.css"],
   "js": ["content-script.js"]
  }
 ],
 ...
}

```

Name | Type | Description  
---|---|---  
`matches` | array of strings | _Required._ Specifies which pages this content script will be injected into. See [Match Patterns](https://developer.chrome.com/docs/extensions/develop/concepts/match-patterns) for details on the syntax of these strings and [Match patterns and globs](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#matchAndGlob) for information on how to exclude URLs.  
`css` | array of strings | _Optional._ The list of CSS files to be injected into matching pages. These are injected in the order they appear in this array, before any DOM is constructed or displayed for the page.  
`js` |  array of strings | _Optional._ The list of JavaScript files to be injected into matching pages. Files are injected in the order they appear in this array. Each string in this list must contain a relative path to a resource in the extension's root directory. Leading slashes (`/`) are automatically trimmed.  
`run_at` | _Optional._ Specifies when the script should be injected into the page. Defaults to `document_idle`.  
`match_about_blank` | boolean | _Optional._ Whether the script should inject into an `about:blank` frame where the parent or opener frame matches one of the patterns declared in `matches`. Defaults to false.  
`match_origin_as_fallback` | boolean |  _Optional._ Whether the script should inject in frames that were created by a matching origin, but whose URL or origin may not directly match the pattern. These include frames with different schemes, such as `about:`, `data:`, `blob:`, and `filesystem:`. See also [Injecting in related frames](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#injecting-in-related-frames).   
`world` |  _Optional._ The JavaScript world for a script to execute within. Defaults to `ISOLATED`. See also [Work in isolated worlds](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#isolated_world).   
### Inject with dynamic declarations
Dynamic content scripts are useful when the match patterns for content scripts are not well known or when content scripts shouldn't always be injected on known hosts.
Introduced in Chrome 96, dynamic declarations are similar to [static declarations](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts#static-declarative), but the content script object is registered with Chrome using methods in the [`chrome.scripting` namespace](https://developer.chrome.com/docs/extensions/reference/api/scripting) rather than in [manifest.json](https://developer.chrome.com/docs/extensions/reference/manifest). The Scripting API also allows extension developers to:
  * [Register](https://developer.chrome.com/docs/extensions/reference/api/scripting#method-registerContentScripts) content scripts.
  * [Get a list of](https://developer.chrome.com/docs/extensions/reference/api/scripting#method-getRegisteredContentScripts) registered content scripts.
  * [Update](https://developer.chrome.com/docs/extensions/reference/api/scripting#method-updateContentScripts) the list of registered content scripts.
  * [Remove](https://developer.chrome.com/docs/extensions/reference/api/scripting#method-unregisterContentScripts) registered content scripts.


Like static declarations, dynamic declarations can include JavaScript files, CSS files, or both.
service-worker.js
```
chrome.scripting
.registerContentScripts([{
id:"session-script",
js:["content.js"],
persistAcrossSessions:false,
matches:["*://example.com/*"],
runAt:"document_start",
}])
.then(()=>console.log("registration complete"))
.catch((err)=>console.warn("unexpected error",err))

```

service-worker.js
```
chrome.scripting
.updateContentScripts([{
id:"session-script",
excludeMatches:["*://admin.example.com/*"],
}])
.then(()=>console.log("registration updated"));

```

service-worker.js
```
chrome.scripting
.getRegisteredContentScripts()
.then(scripts=>console.log("registered content scripts",scripts));

```

service-worker.js
```
chrome.scripting
.unregisterContentScripts({ids:["session-script"]})
.then(()=>console.log("un-registration complete"));

```

### Inject programmatically
Use programmatic injection for content scripts that need to run in response to events or on specific occasions.
To inject a content script programmatically, your extension needs [host permissions](https://developer.chrome.com/docs/extensions/reference/permissions) for the page it's trying to inject scripts into. Host permissions can either be granted by requesting them as part of your extension's manifest or temporarily using [`"activeTab"`](https://developer.chrome.com/docs/extensions/develop/concepts/activeTab).
The following is a different versions of an activeTab-based extension.
manifest.json:
```
{
 "name": "My extension",
 ...
 "permissions": [
  "activeTab",
  "scripting"
 ],
 "background": {
  "service_worker": "background.js"
 },
 "action": {
  "default_title": "Action Button"
 }
}

```

Content scripts can be injected as files.
content-script.js
```

document.body.style.backgroundColor="orange";

```

service-worker.js:
```
chrome.action.onClicked.addListener((tab)=>{
chrome.scripting.executeScript({
target:{tabId:tab.id},
files:["content-script.js"]
});
});

```

Or, a function body can be injected and executed as a content script.
service-worker.js:
```
functioninjectedFunction(){
document.body.style.backgroundColor="orange";
}
chrome.action.onClicked.addListener((tab)=>{
chrome.scripting.executeScript({
target:{tabId:tab.id},
func:injectedFunction,
});
});

```

Be aware that the injected function is a copy of the function referenced in the `chrome.scripting.executeScript()` call, not the original function itself. As a result, the function's body must be self contained; references to variables outside of the function will cause the content script to throw a [`ReferenceError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError).
When injecting as a function, you can also pass arguments to the function.
service-worker.js
```
functioninjectedFunction(color){
document.body.style.backgroundColor=color;
}
chrome.action.onClicked.addListener((tab)=>{
chrome.scripting.executeScript({
target:{tabId:tab.id},
func:injectedFunction,
args:["orange"],
});
});

```

### Exclude matches and globs
To customize specified page matching, include the following fields in a declarative registration.
Name | Type | Description  
---|---|---  
`exclude_matches` | array of strings | _Optional._ Excludes pages that this content script would otherwise be injected into. See [Match Patterns](https://developer.chrome.com/docs/extensions/develop/concepts/match-patterns) for details of the syntax of these strings.  
`include_globs` | array of strings | _Optional._ Applied after `matches` to include only those URLs that also match this glob. This is intended to emulate the [`@include`](https://wiki.greasespot.net/Metadata_Block#.40include) Greasemonkey keyword.  
`exclude_globs` | array of string | _Optional._ Applied after `matches` to exclude URLs that match this glob. Intended to emulate the [`@exclude`](https://wiki.greasespot.net/Metadata_Block#.40exclude) Greasemonkey keyword.  
The content script will be injected into a page if both of the following are true:
  * Its URL matches any `matches` pattern and any `include_globs` pattern.
  * The URL doesn't also match an `exclude_matches` or `exclude_globs` pattern. Because the `matches` property is required, `exclude_matches`, `include_globs`, and `exclude_globs` can only be used to limit which pages will be affected.


The following extension injects the content script into `https://www.nytimes.com/health` but not into `https://www.nytimes.com/business` .
manifest.json
```
{
 "name": "My extension",
 ...
 "content_scripts": [
  {
   "matches": ["https://*.nytimes.com/*"],
   "exclude_matches": ["*://*/*business*"],
   "js": ["contentScript.js"]
  }
 ],
 ...
}

```

service-worker.js
```
chrome.scripting.registerContentScripts([{
id:"test",
matches:["https://*.nytimes.com/*"],
excludeMatches:["*://*/*business*"],
js:["contentScript.js"],
}]);

```

Glob properties follow a different, more flexible syntax than [match patterns](https://developer.chrome.com/docs/extensions/develop/concepts/match-patterns). Acceptable glob strings are URLs that may contain "wildcard" asterisks and question marks. The asterisk (`*`) matches any string of any length, including the empty string, while the question mark (`?`) matches any single character.
For example, the glob `https://???.example.com/foo/\*` matches any of the following:
  * `https://www.example.com/foo/bar`
  * `https://the.example.com/foo/`


However, it does _not_ match the following:
  * `https://my.example.com/foo/bar`
  * `https://example.com/foo/`
  * `https://www.example.com/foo`


This extension injects the content script into `https://www.nytimes.com/arts/index.html` and `https://www.nytimes.com/jobs/index.htm*`, but not into `https://www.nytimes.com/sports/index.html`:
manifest.json
```
{
 "name": "My extension",
 ...
 "content_scripts": [
  {
   "matches": ["https://*.nytimes.com/*"],
   "include_globs": ["*nytimes.com/???s/*"],
   "js": ["contentScript.js"]
  }
 ],
 ...
}

```

This extension injects the content script into `https://history.nytimes.com` and `https://.nytimes.com/history`, but not into `https://science.nytimes.com` or `https://www.nytimes.com/science`:
manifest.json
```
{
 "name": "My extension",
 ...
 "content_scripts": [
  {
   "matches": ["https://*.nytimes.com/*"],
   "exclude_globs": ["*science*"],
   "js": ["contentScript.js"]
  }
 ],
 ...
}

```

One, all, or some of these can be included to achieve the correct scope.
manifest.json
```
{
 "name": "My extension",
 ...
 "content_scripts": [
  {
   "matches": ["https://*.nytimes.com/*"],
   "exclude_matches": ["*://*/*business*"],
   "include_globs": ["*nytimes.com/???s/*"],
   "exclude_globs": ["*science*"],
   "js": ["contentScript.js"]
  }
 ],
 ...
}

```

### Run time
The `run_at` field controls when JavaScript files are injected into the web page. The preferred and default value is `"document_idle"`. See the [RunAt](https://developer.chrome.com/docs/extensions/reference/api/extensionTypes#type-RunAt) type for other possible values.
manifest.json
```
{
 "name": "My extension",
 ...
 "content_scripts": [
  {
   "matches": ["https://*.nytimes.com/*"],
   "run_at": "document_idle",
   "js": ["contentScript.js"]
  }
 ],
 ...
}

```

service-worker.js
```
chrome.scripting.registerContentScripts([{
id:"test",
matches:["https://*.nytimes.com/*"],
runAt:"document_idle",
js:["contentScript.js"],
}]);

```

Name | Type | Description  
---|---|---  
`document_idle` | string | _Preferred._ Use `"document_idle"` whenever possible.The browser chooses a time to inject scripts between `"document_end"` and immediately after the [`window.onload`](https://developer.mozilla.org/docs/Web/API/Window/load_event) event fires. The exact moment of injection depends on how complex the document is and how long it is taking to load, and is optimized for page load speed.Content scripts running at `"document_idle"` don't need to listen for the `window.onload` event, they are guaranteed to run after the DOM is complete. If a script definitely needs to run after `window.onload`, the extension can check if `onload` has already fired by using the [`document.readyState`](https://developer.mozilla.org/docs/Web/API/Document/readyState) property.  
`document_start` | string | Scripts are injected after any files from `css`, but before any other DOM is constructed or any other script is run.  
`document_end` | string | Scripts are injected immediately after the DOM is complete, but before subresources like images and frames have loaded.  
### Specify frames
For declarative content scripts specified in the manifest, the [`"all_frames"`](https://developer.chrome.com/docs/extensions/reference/manifest/content-scripts#frames) field allows the extension to specify if JavaScript and CSS files should be injected into all frames matching the specified URL requirements or only into the topmost frame in a tab:
manifest.json
```
{
 "name": "My extension",
 ...
 "content_scripts": [
  {
   "matches": ["https://*.nytimes.com/*"],
   "all_frames": true,
   "js": ["contentScript.js"]
  }
 ],
 ...
}

```

When programmatically registering content scripts using [`chrome.scripting.registerContentScripts(...)`](https://developer.chrome.com/docs/extensions/reference/api/scripting#type-RegisteredContentScript), the [`allFrames`](https://developer.chrome.com/docs/extensions/reference/api/scripting#properties_4) parameter can be used to specify if the content script should be injected into all frames matching the specified URL requirements or only into the topmost frame in a tab. This can only be used with tabId, and cannot be used if frameIds or documentIds are specified:
service-worker.js
```
chrome.scripting.registerContentScripts([{
id:"test",
matches:["https://*.nytimes.com/*"],
allFrames:true,
js:["contentScript.js"],
}]);

```

### Inject in to related frames
Extensions may want to run scripts in frames that are related to a matching frame, but don't themselves match. A common scenario when this is the case is for frames with URLs that were created by a matching frame, but whose URLs don't themselves match the script's specified patterns.
This is the case when an extension wants to inject in frames with URLs that have `about:`, `data:`, `blob:`, and `filesystem:` schemes. In these cases, the URL won't match the content script's pattern (and, in the case of `about:` and `data:`, don't even include the parent URL or origin in the URL at all, as in `about:blank` or `data:text/html,<html>Hello, World!</html>`). However, these frames can still be associated with the creating frame.
To inject into these frames, extensions can specify the `"match_origin_as_fallback"` property on a content script specification in the manifest.
manifest.json
```
{
"name":"My extension",
...
"content_scripts":[
{
"matches":["https://*.google.com/*"],
"match_origin_as_fallback":true,
"js":["contentScript.js"]
}
],
...
}

```

When specified and set to `true`, Chrome will look at the origin of the initiator of the frame to determine whether the frame matches, rather than at the URL of the frame itself. Note that this might also be different than the target frame's _origin_ (e.g., `data:` URLs have a null origin).
The initiator of the frame is the frame that created or navigated the target frame. While this is commonly the direct parent or opener, it may not be (as in the case of a frame navigating an iframe within an iframe).
Because this compares the _origin_ of the initiator frame, the initiator frame could be on at any path from that origin. To make this implication clear, Chrome requires any content scripts specified with `"match_origin_as_fallback"` set to `true` to also specify a path of `*`.
When both `"match_origin_as_fallback"` and `"match_about_blank"` are specified, `"match_origin_as_fallback"` takes priority.
## Communication with the embedding page
Although the execution environments of content scripts and the pages that host them are isolated from each other, they share access to the page's DOM. If the page wishes to communicate with the content script, or with the extension through the content script, it must do so through the shared DOM.
An example can be accomplished using [`window.postMessage()`](https://developer.mozilla.org/docs/Web/API/Window/postMessage):
content-script.js
```
varport=chrome.runtime.connect();
window.addEventListener("message",(event)=>{
// We only accept messages from ourselves
if(event.source!==window){
return;
}
if(event.data.type && (event.data.type==="FROM_PAGE")){
console.log("Content script received: "+event.data.text);
port.postMessage(event.data.text);
}
},false);

```

example.js
```
document.getElementById("theButton").addEventListener("click",()=>{
window.postMessage(
{type:"FROM_PAGE",text:"Hello from the webpage!"},"*");
},false);

```

The non-extension page, example.html, posts messages to itself. This message is intercepted and inspected by the content script and then posted to the extension process. In this way, the page establishes a line of communication to the extension process. The reverse is possible through similar means.
## Access extension files
To access an extension file from a content script, you can call [`chrome.runtime.getURL()`](https://developer.chrome.com/docs/extensions/reference/api/runtime#method-getURL) to get the _absolute URL_ of your extension asset as shown in the following example (`content.js`):
content-script.js
```
letimage=chrome.runtime.getURL("images/my_image.png")

```

To use fonts or images in a CSS file, you can use [`@@extension_id`](https://developer.chrome.com/docs/extensions/reference/api/i18n#overview-predefined) to construct a URL as shown in the following example (`content.css`):
content.css
```
body{
background-image:url('chrome-extension://__MSG_@@extension_id__/background.png');
}
@font-face{
font-family:'Stint Ultra Expanded';
font-style:normal;
font-weight:400;
src:url('chrome-extension://__MSG_@@extension_id__/fonts/Stint Ultra Expanded.woff')format('woff');
}

```

All assets must be declared as [web accessible resources](https://developer.chrome.com/docs/extensions/reference/manifest/web-accessible-resources) in the `manifest.json` file:
manifest.json
```
{
...
"web_accessible_resources":[
{
"resources":["images/*.png"],
"matches":["https://example.com/*"]
},
{
"resources":["fonts/*.woff"],
"matches":["https://example.com/*"]
}
],
...
}

```

## Stay secure
While isolated worlds provide a layer of protection, using content scripts can create vulnerabilities in an extension and the web page. If the content script receives content from a separate website, such as by calling `fetch()`, be careful to filter content against [cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting) attacks before injecting it. Only communicate over HTTPS in order to avoid ["man-in-the-middle"](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) attacks.
Be sure to filter for malicious web pages. For example, the following patterns are dangerous, and disallowed in Manifest V3:
Don't
content-script.js
```
constdata=document.getElementById("json-data");
// WARNING! Might be evaluating an evil script!
constparsed=eval("("+data+")");
```

Don't
content-script.js
```
constelmt_id=...
// WARNING! elmt_id might be '); ... evil script ... //'!
window.setTimeout("animate("+elmt_id+")",200);
```

Instead, prefer safer APIs that don't run scripts:
Do
content-script.js
```
constdata=document.getElementById("json-data")
// JSON.parse does not evaluate the attacker's scripts.
constparsed=JSON.parse(data);
```

Do
content-script.js
```
constelmt_id=...
// The closure form of setTimeout does not evaluate scripts.
window.setTimeout(()=>animate(elmt_id),200);
```

Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2012-09-17 UTC.

