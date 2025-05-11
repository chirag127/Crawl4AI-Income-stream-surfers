---
url: https://developer.chrome.com/blog/chrome-116-beta-whats-new-for-extensions?hl=en
title: https://developer.chrome.com/blog/chrome-116-beta-whats-new-for-extensions?hl=en
date: 2025-05-11T16:54:12.847539
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/chrome-116-beta-whats-new-for-extensions?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/chrome-116-beta-whats-new-for-extensions?hl=es-419)

Sign in


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  What's new in Chrome 116 for Extensions 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Chrome 116 is now available in beta and includes many exciting updates for Chrome Extension developers. Let’s take a quick look at what’s new.
Sebastian Benz 
[ GitHub ](https://github.com/sebastianbenz) [ Mastodon ](https://mastodon.cloud/@sebabenz) [ Bluesky ](https://bsky.app/profile/sebabenz.bsky.social)
## Programmatically open a Sidepanel
Sidepanel has been one of the most requested features in Chrome extensions and has been available in Chrome since version 114. After launching the Side Panel API, one of the first pieces of feedback that we’ve received was that developers wanted a way to programmatically open a side panel. And here it is: [`chrome.sidePanel.open`](https://developer.chrome.com/docs/extensions/reference/sidePanel#method-open) is now in beta. You can use it to open the extension side panel programmatically in response to a user interaction, such as a context menu click:
```
chrome.contextMenus.onClicked.addListener((info,tab)=>{
if(info.menuItemId==='openSidePanel'){
// This will open the panel in all the pages on the current window.
chrome.sidePanel.open({windowId:tab.windowId});
}
});

```

## WebSocket support in Service Workers
WebSocket support is critical for many extensions planning to move to Manifest V3. Chrome 116 further improves WebSocket support in service workers as all WebSocket activity will reset the [30s service worker idle timer](https://developer.chrome.com/docs/extensions/mv3/service_workers/service-worker-lifecycle). This means that as long as your WebSocket is active, the service worker will stay alive. 
You can use this to implement a keepalive mechanism ensuring your service worker stays active while you’re waiting for messages from your server - even if it takes more than 30s until the next message arrives:
```
functionkeepAlive(){
constkeepAliveIntervalId=setInterval(
()=>{
if(webSocket){
webSocket.send('keepalive');
}else{
clearInterval(keepAliveIntervalId);
}
},
// It's important to pick an interval that's shorter than 30s, to
// avoid that the service worker becomes inactive.
20*1000
);
}

```

Check out our new WebSocket [guide](https://developer.chrome.com/docs/extensions/mv3/tut_websockets) and [sample](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/functional-samples/tutorial.websockets) for more details.
## Strong keepalive for Service Workers
Speaking of service worker lifecycle, another important update has landed: strong keepalive for APIs requiring user interaction. APIs that require a user interaction will have "strong" keepalives for extension service workers (i.e., allow the worker to take longer than 5 minutes on this task):
  * [`permissions.request()`](https://developer.chrome.com/docs/extensions/reference/permissions#method-request)
  * [`desktopCapture.chooseDesktopMedia()`](https://developer.chrome.com/docs/extensions/reference/desktopCapture#method-chooseDesktopMedia)
  * [`identity.launchWebAuthFlow()`](https://developer.chrome.com/docs/extensions/reference/identity#method-launchWebAuthFlow)
  * [`management.uninstall()`](https://developer.chrome.com/docs/extensions/reference/management#method-uninstall)


## Recording audio and video in the background
Another gap between Manifest V2 and Manifest V3 has been closed: you can record audio and video in the background using `tabCapture` and offscreen documents. Use the [`chrome.tabCapture`](https://developer.chrome.com/docs/extensions/reference/tabCapture) API in a service worker to obtain a stream ID following a user gesture. This can then be passed to an [offscreen document](https://developer.chrome.com/docs/extensions/reference/offscreen) to start recording.
Check out our updated [`tabCapture` guide](https://developer.chrome.com/docs/extensions/mv3/screen_capture) to learn how it works or, for a working example, see the [Tab Capture - Recorder](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/functional-samples/sample.tabcapture-recorder) sample.
## New API: runtime.getContexts()
The new [`runtime.getContexts()` API](https://developer.chrome.com/docs/extensions/reference/runtime#method-getContexts) lets you fetch information about active contexts associated with your extensions. For example, you can use it to check if there is an active offscreen document:
```
constexistingContexts=awaitchrome.runtime.getContexts({});
constoffscreenDocument=existingContexts.find(
(c)=>c.contextType==='OFFSCREEN_DOCUMENT'
);

```

## New offscreen reason: GEOLOCATION
`geolocation` has been added as another [valid reason for using an offscreen document](https://developer.chrome.com/docs/extensions/reference/offscreen#type-Reason). Check out our guide [using geolocation](https://developer.chrome.com/docs/extensions/mv3/geolocation) to learn more about how to obtain the geographical location of the extension using the Offscreen API.
## chrome.action.setBadgeText()
[`action.setBadgeText`](https://developer.chrome.com/docs/extensions/reference/action#method-setBadgeText) has been updated to address an inconsistency between Manifest V2 and Manifest V3. Passing an empty string or `null` to `action.setBadgeText` will clear the badge text for the specified tab and default to the global badge text instead.
```
action.setBadgeText({tabId:tabId,text:''});

```

## Summary: another step towards Manifest V3
With improved Service Worker lifetime support and the updated TabCapture API we’ve continued to make progress on our goal to close the feature gap between Manifest V2 and V3. Checkout our [known issues page](https://developer.chrome.com/docs/extensions/migrating/known-issues) for the current status. 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2023-07-20 UTC.

