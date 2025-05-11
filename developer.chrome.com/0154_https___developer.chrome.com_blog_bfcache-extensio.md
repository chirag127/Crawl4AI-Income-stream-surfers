---
url: https://developer.chrome.com/blog/bfcache-extension-messaging-changes
title: https://developer.chrome.com/blog/bfcache-extension-messaging-changes
date: 2025-05-11T16:54:03.756232
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/bfcache-extension-messaging-changes#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/bfcache-extension-messaging-changes?hl=es-419)

Sign in


  * On this page
  * [Extension message port](https://developer.chrome.com/blog/bfcache-extension-messaging-changes#extension_message_port)
  * [Back/forward cache](https://developer.chrome.com/blog/bfcache-extension-messaging-changes#backforward_cache)
  * [Extension message ports' impact on BFCache](https://developer.chrome.com/blog/bfcache-extension-messaging-changes#extension_message_ports_impact_on_bfcache)
  * [New behavior: closing the message channel when the page is stored in BFCache](https://developer.chrome.com/blog/bfcache-extension-messaging-changes#new_behavior_closing_the_message_channel_when_the_page_is_stored_in_bfcache)
  * [Am I impacted?](https://developer.chrome.com/blog/bfcache-extension-messaging-changes#am_i_impacted)
    * [Testing the new behavior](https://developer.chrome.com/blog/bfcache-extension-messaging-changes#testing_the_new_behavior)
    * [Identify simple issues using the old behavior](https://developer.chrome.com/blog/bfcache-extension-messaging-changes#identify_simple_issues_using_the_old_behavior)
  * [Release timeline](https://developer.chrome.com/blog/bfcache-extension-messaging-changes#release_timeline)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  Changes to BFCache behavior with extension message ports 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Extension message port](https://developer.chrome.com/blog/bfcache-extension-messaging-changes#extension_message_port)
  * [Back/forward cache](https://developer.chrome.com/blog/bfcache-extension-messaging-changes#backforward_cache)
  * [Extension message ports' impact on BFCache](https://developer.chrome.com/blog/bfcache-extension-messaging-changes#extension_message_ports_impact_on_bfcache)
  * [New behavior: closing the message channel when the page is stored in BFCache](https://developer.chrome.com/blog/bfcache-extension-messaging-changes#new_behavior_closing_the_message_channel_when_the_page_is_stored_in_bfcache)
  * [Am I impacted?](https://developer.chrome.com/blog/bfcache-extension-messaging-changes#am_i_impacted)
    * [Testing the new behavior](https://developer.chrome.com/blog/bfcache-extension-messaging-changes#testing_the_new_behavior)
    * [Identify simple issues using the old behavior](https://developer.chrome.com/blog/bfcache-extension-messaging-changes#identify_simple_issues_using_the_old_behavior)
  * [Release timeline](https://developer.chrome.com/blog/bfcache-extension-messaging-changes#release_timeline)


Mingyu Lei 
[ GitHub ](https://github.com/lozy219)
Back/forward cache (or BFCache) is a browser optimization that enables instant back and forward navigation. We are making changes to Chrome BFCache which potentially impact extensions using message ports. If you own a Chrome extension that uses messaging to communicate between content scripts and your extension, read on to learn about how to test and adapt your extension.
## Extension message port
Extensions communicate with the content script or other extensions through message passing. Messages can be sent using one-time requests by calling `runtime.sendMessage()` and `tabs.sendMessage()`, or using a reusable message port. As long as the port is active, both the content script and the extension background script can reuse the port to post messages to each other.
For more information, see [Message passing](https://developer.chrome.com/docs/extensions/develop/concepts/messaging).
## Back/forward cache
When navigating away from a page that is [eligible for BFCache](https://web.dev/articles/bfcache#optimize_your_pages_for_bfcache), the browser allows the page with all of its state to remain in memory but in the non-[fully-active](https://html.spec.whatwg.org/#fully-active-documents) state. If the user performs a history navigation (either back or forward) to the cached page, the browser will try to restore the page from BFCache. This makes the navigation faster and improves the user's browsing experience.
While the page is in BFCache, it's in a frozen state where no JavaScript execution is allowed. This means that it cannot process messages it receives.
For more information, see [Back/forward cache](https://web.dev/articles/bfcache).
## Extension message ports' impact on BFCache
In short, extension sending messages to a page in BFCache may cause the cache eviction and affect performance.
When a page with an open extension message port is stored in BFCache, the port stays open. Once the page is restored from BFCache, the old reference of the message port can still be used by the extension service workers to post messages to the content script.
However, if the extension attempts to post a message through that message port while the page is still in BFCache, the message is sent but not fully delivered because the handler is frozen. It is challenging for the extension to reason about and address this situation, as both queuing and dropping the message have their own problems.
To avoid getting into the problems related to lost messages, in Chrome's current implementation, it evicts the host page from BFCache and discards the message. If the user goes back to the page, it will be loaded fresh, allowing the extension to set up a new connection.
On the other hand, this implementation constrains the scenarios where BFCache applies, limiting the performance gains, especially for extensions with broadcast or heartbeat mechanisms that regularly send messages to all connections. Moreover, as the eviction is triggered when the extension sends a message to the content script, web developers have no means to prevent their pages from being evicted.
To improve the overall performance, we plan to introduce a new message port behavior.
## New behavior: closing the message channel when the page is stored in BFCache
Starting in Chrome 123, when a page with an open extension message port is stored in BFCache, the underlying message channel is proactively closed from the content script side. As a result, all message ports will be closed, and the extension will receive an `onDisconnect` event.
Since the channel is closed, no messages will be sent to the page while it is in BFCache. Therefore, the page won't be evicted due to the extension.
Even after the page is restored from BFCache, the closed message channel won't be reopened. The recommended practice for extension authors is to listen to the [page lifecycle events](https://developer.chrome.com/docs/web-platform/page-lifecycle-api), and set up a new connection when the page is restored from BFCache, as shown in the following example.
```
// content script
letport;
window.addEventListener('pageshow',(event)=>{
if(event.persisted){
// The page is restored from BFCache, set up a new connection.
port=chrome.runtime.connect();
}
});

```

Read more about the [WECG conversation](https://github.com/w3c/webextensions/blob/main/_minutes/2023-11-23-wecg.md#:%7E:text=Issue%20474%3A-,Behavior%20of%20extension%20message%20ports%20and%20bfcache,-%5Btomislav%5D%20I%20investigated) from different browsers' representatives (under issue 474).
## Am I impacted?
The new behavior will be available behind a flag in Chrome 123 so that you can test your code. See the [timeline](https://developer.chrome.com/blog/bfcache-extension-messaging-changes#release_timeline) for more information. Use the steps that follow to test your extension. Note that it only provides a simple test, and we encourage you to run Chrome with the feature enabled for a period of time as it can be hard to predict what features in the extension may cause issues.
### Testing the new behavior
To force-enable the experiment in Chrome 123:
  1. Launch Chrome with the following flag, which forces the **new** behavior:
```
--enable-features=DisconnectExtensionMessagePortWhenPageEntersBFCache

```

  2. Go to a page, and interact with your extension if necessary, so that a content script will open a port to your extension.
  3. Navigate away and back. The page should be restored now, but the message channel between the content script and the service worker should be disconnected.
  4. Test if the extension still works as usual, if not, you should manually reconnect as demonstrated in the previous section.


### Identify simple issues using the old behavior
Prior to this change, Chrome would show a warning if you attempted to send a message to a port associated with a page in the bfcache. This can be useful to identify some but not all issues that involve messages from the background to the page.
  1. Make sure the Chrome version is at least 123. Ideally, use Chrome Canary, which has an additional warning to make testing easier.
  2. Launch Chrome with the following flag, which forces the **old** behavior:
```
--disable-features=DisconnectExtensionMessagePortWhenPageEntersBFCache

```

  3. Go to a page that is eligible for BFCache without the extension running (for example, some simple site like <https://example.com/>). Follow [the BFCache tutorial](https://developer.chrome.com/docs/devtools/application/back-forward-cache) to ensure that it is restored from BFCache.
  4. Install and enable the extension, and test the BFCache eligibility again. You may manually navigate away, wait for some time that is long enough for your extension to post a message to the BFCached page, and navigate back.
  5. If the page had to be loaded fresh instead of from BFCache due to an eviction, and [the issue preventing restoring](https://developer.chrome.com/docs/devtools/application/back-forward-cache#resolve-issues) is "ExtensionSentMessageToCachedFrame", then the extension might be impacted by this change.
In Chrome Canary 124.0.6315.0 and newer, you will also see the following warning in the page:
Warning shown when a page is not restored from BFCache.


Once it's confirmed that the extension is posting messages to the BFCache page, you can follow the steps in the previous section to force enabling the experiment and observe if any logic breaks.
## Release timeline
We plan to gradually ramp up the new behavior starting in Chrome 123. Here is the detailed plan:
Date | Planned milestone  
---|---  
February 15 | Start the experiment for the new behavior in Chrome 123 Canary and Dev.  
March 7 | Start the experiment for the new behavior in Chrome 123 Beta.  
March 18 | Release the new behavior to 4 percent of users in Chrome 123 Stable.  
March 25 | Release the new behavior to 50 percent of users in Chrome 123 Stable.  
April 2 | The experiment ends, making the new behavior as default.  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-02-22 UTC.

