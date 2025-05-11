---
url: https://developer.chrome.com/blog/new-extensions-menu-testing?hl=en
title: https://developer.chrome.com/blog/new-extensions-menu-testing?hl=en
date: 2025-05-11T16:56:49.837472
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-extensions-menu-testing?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-extensions-menu-testing?hl=es-419)

Sign in


  * On this page
  * [What's changing?](https://developer.chrome.com/blog/new-extensions-menu-testing?hl=en#whats_changing)
  * [Add a site access request](https://developer.chrome.com/blog/new-extensions-menu-testing?hl=en#add_a_site_access_request)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  Prepare your extension as we begin testing a new extensions menu 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [What's changing?](https://developer.chrome.com/blog/new-extensions-menu-testing?hl=en#whats_changing)
  * [Add a site access request](https://developer.chrome.com/blog/new-extensions-menu-testing?hl=en#add_a_site_access_request)


Oliver Dunk 
[ GitHub ](https://github.com/oliverdunk) [ Bluesky ](https://bsky.app/profile/oliverdunk.com) [ Homepage ](https://oliverdunk.com)
Published: November 19, 2024 
At Google I/O 2024, we shared some early designs for upcoming changes to the extensions menu, which give users more control over the sites extensions can access. We're going to start testing these changes soon, beginning with a small percentage of users in Canary and with the hope to roll them out more widely in the future.
When talking to developers about this change in the past, we often heard concerns about the impact of changing the way extensions are able to request host permissions at install time. The new menu does not impact any default behavior. Extensions will continue to be granted access to all requested hosts at install time. The goal of these changes is to make it easier for users to discover controls that are already available.
This post gives an overview of what to expect and how you can prepare your extensions with a new API to handle cases where access to a page has been withheld by the user.
## What's changing?
To give users more control, we will introduce a new extensions menu. Extensions will continue to be granted access to all requested hosts at install time, but users will now have an easier way to control access per extension.
Work in progress design for the new extensions menu
The new menu (pictured with the current design which may change) more clearly shows which extensions can run on a page, and gives users the ability to change access if chosen. A user can also prevent all extensions from running on a specific site. As mentioned, none of the available settings or defaults are changing–we are focused on making what we already have easier for users to discover.
## Add a site access request
We have designed a new API to complement these changes, with significant input from other browsers and developers in the [WebExtensions Community Group](https://github.com/w3c/webextensions).
If a user has withheld access to a page, extensions can now request access using the new [`permissions.addHostAccessRequest`](https://developer.chrome.com/docs/extensions/reference/api/permissions#method-addHostAccessRequest) API. When an extension does this, the user will see an "Allow" message alongside the extension puzzle piece in the toolbar. Here's one design we are exploring:
A site access request on example.com
When a user clicks "Allow" within the extensions menu, the extension is granted persistent access to the host. The user can withhold it again in the future by accessing the extensions menu or on the chrome://extensions page. Clicking "Allow 1?" within the toolbar provides a faster way to grant immediate access.
Extensions can call `permissions.addHostAccessRequest` with a `tabId` to show a permission request for that tab. You can use feature detection to safely begin using it in your extension today. The API won't do anything for users without the new menu, but adopting it will benefit users with the new menu as it is gradually rolled out.
```
chrome.tabs.onUpdated.addListener(async(tabId,changes)=>{
if(typeofchanges.url!=='string')return;
consturl=newURL(changes.url);
// If we are on the /checkout page of example.com.
if(url.origin==='https://example.com' && url.pathname==='/checkout'){
consthasPermission=awaitchrome.permissions.contains({
origins:['https://example.com/*']
});
// We already have host permissions.
if(hasPermission){
return;
}
// Add a site access request if the API is available.
if(chrome.permissions.addHostAccessRequest){
chrome.permissions.addHostAccessRequest({tabId});
}
}
});

```

In this example, we only add a request if the user is on the `/checkout` page. You can see the [full code](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/functional-samples/cookbook.permissions-addhostaccessrequest) in our chrome-extensions-samples repository.
Extensions should be mindful about when to ask users for access. Users are more likely to ignore noisy requests and Chrome might throttle excessive requests. A user can also choose to turn off the ability for an extension to show requests. As a result, you should only request access in specific situations, when you have high confidence the user will want to engage with your extension.
Requests are bound to a specific tab and are automatically cleared when a user navigates to a different origin. A corresponding [`removeHostAccessRequest`](https://developer.chrome.com/docs/extensions/reference/api/permissions#method-removeHostAccessRequest) method is available to clear a request explicitly (such as if a request is bound to a particular path).
Since this API is linked with the new extensions menu, calls will be ignored if the new menu is not enabled. However, we encourage you to try the API today, and consider adopting it in your extension. You'll provide a great user experience as the new menu changes gradually show for more users.
To learn more about working with optional permissions, check out the permissions [documentation](https://developer.chrome.com/docs/extensions/reference/api/permissions#implement_optional_permissions).
## Try it out
The API is enabled by default in Chrome 133.0.6860.0 and higher (currently in Chrome Canary). To enable the new menu, at chrome://flags, enable the "Extensions Menu Access Control" flag.
As a reminder, this is still work in progress and may continue to evolve and change. We recommend testing in Chrome Canary to see the most up to date experience.
You can leave feedback on the new design in the [chromium-extensions](https://groups.google.com/a/chromium.org/g/chromium-extensions) mailing list which we'll be keeping in mind as we continue work on the new menu.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-11-19 UTC.

