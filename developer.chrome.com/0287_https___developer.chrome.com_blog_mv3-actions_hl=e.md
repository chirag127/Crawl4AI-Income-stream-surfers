---
url: https://developer.chrome.com/blog/mv3-actions?hl=en
title: https://developer.chrome.com/blog/mv3-actions?hl=en
date: 2025-05-11T16:56:48.304217
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/mv3-actions?hl=en#main-content)


  * On this page
  * [A short history of extension actions](https://developer.chrome.com/blog/mv3-actions?hl=en#a_short_history_of_extension_actions)
  * [Manifest V3 changes](https://developer.chrome.com/blog/mv3-actions?hl=en#manifest_v3_changes)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  Extension actions in Manifest V3 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [A short history of extension actions](https://developer.chrome.com/blog/mv3-actions?hl=en#a_short_history_of_extension_actions)
  * [Manifest V3 changes](https://developer.chrome.com/blog/mv3-actions?hl=en#manifest_v3_changes)


Simeon Vincent 
[ GitHub ](https://github.com/dotproto) [ Glitch ](https://glitch.com/@dotproto)
Since the launch of Chrome extensions, the platform has allowed developers to expose extension functionality directly in the top level Chrome UI using _actions_. An action is an icon button that can open a popup or trigger some functionality in the extension. Historically, Chrome supported two types of actions, browser actions and page actions; Manifest V3 changed this by consolidating their functionality in a new [chrome.action](https://developer.chrome.com/docs/extensions/reference/action/) API.
## A short history of extension actions
While `chrome.action` itself is new in Manifest V3, the basic functionality it provides dates back to when extensions first [landed in stable](https://chrome.googleblog.com/2010/01/over-1500-new-features-for-google.html) in January, 2010. The first stable release of Chrome's extensions platform supported two different kinds of actions: [browser actions](https://developer.chrome.com/docs/extensions/reference/browserAction) and [page actions](https://developer.chrome.com/docs/extensions/reference/pageAction/).
Browser actions allowed extension developers to display an icon "in the main Google Chrome toolbar, to the right of the address bar" ([source](https://web.archive.org/web/20091119105342/http://code.google.com/chrome/extensions/browserAction.html)) and provided users an easy way to trigger extension functionality on any page. Page actions, on the other hand, were intended to "represent actions that can be taken on the current page, but that aren't applicable to all pages" ([source](https://web.archive.org/web/20091125234041/http://code.google.com/chrome/extensions/pageAction.html)).
In other words, browser actions gave extension developers a persistent UI surface in the browser while page actions appeared only when the extension could do something useful on the current page.
Both types of actions were optional, so an extension developer could opt to provide either no actions, a page action, or a browser action (specifying multiple actions isn't allowed).
Roughly six years later, Chrome 49 introduced a new UI paradigm for extensions. In order to help users understand what extensions they had, Chrome began displaying all active extensions to the right of the omnibox. Users could "overflow" extensions into the Chrome menu if they wanted.
In order to display an icon for each extension, this update also ushered in two important changes to how extensions behaved in Chrome's UI. First, all extensions began displaying icons in the toolbar. If the extension didn't have an icon, Chrome would autogenerate one for it. Second, page actions moved into the toolbar alongside browser actions and were given an affordance to differentiate between their "show" and "hide" states.
This change allowed page action extensions to continue working as expected, but it also diminished the role of page actions over time. One of the effects of the UI redesign was that page actions were effectively subsumed by browser actions. Since all extensions appeared in the toolbar, users came to expect that clicking an extension's toolbar icon would invoke the extension, and browser actions became an increasingly important interaction for Chrome extensions.
## Manifest V3 changes
The Chrome UI and extensions continued to evolve in the years following the 2016 extension UI redesign, but browser actions and page actions remained largely unchanged. That is, at least until we started planning how to modernize the extensions platform with Manifest V3.
It was clear to the extensions team that browser actions and page actions were increasingly a distinction without meaning. Worse, their subtle behavior differences made it hard for developers to determine which one to use. We realized that we could address these issues by combining the browser action and page action into a single "action."
Enter the Action API; `chrome.action` is most directly analogous to `chrome.browserAction`, but it has a few notable differences.
First, `chrome.action` introduces a new method named [`getUserSettings()`](https://developer.chrome.com/docs/extensions/reference/action/#method-getUserSettings). This method gives extension developers a way to check if the user has pinned their extension's action to the toolbar.
```
letuserSettings=awaitchrome.action.getUserSettings();
console.log(`Is the action pinned? ${userSettings.isOnToolbar?'Yes':'No'}.`);

```

"getUserSettings" may seem like a bit of an unusual name for this functionality compared to, say, "isPinned", but the history of actions in Chrome shows that the browser UI changes faster than extension APIs do. As such, our goal with this API is to expose action-related user preferences on generic interfaces in order to minimize future API churn. It also lets other browser vendors expose browser-specific UI concepts in the [UserSettings](https://developer.chrome.com/docs/extensions/reference/action/#type-UserSettings) object returned by this method.
Second, the icon and enabled/disabled state of an extension's action can be controlled using the Declarative Content API. This is important because it lets extensions react to the user's browsing behavior without accessing the content or even the URLs of the pages they visit. For example, let's see how an extension can enable its action when the user visits pages on example.com.
```
// Manifest V3
chrome.runtime.onInstalled.addListener(()=>{
chrome.declarativeContent.onPageChanged.removeRules(undefined,()=>{
chrome.declarativeContent.onPageChanged.addRules([
{
conditions:[
newchrome.declarativeContent.PageStateMatcher({
pageUrl:{hostSuffix:'.example.com'},
})
],
actions:[newchrome.declarativeContent.ShowAction()]
}
]);
});
});

```

The above code is almost identical to what an extension would do with a page action. The only difference is that in Manifest V3 we used `declarativeContent.ShowAction` instead of `declarativeContent.ShowPageAction` in Manifest V2.
Finally, content blockers can use the declarativeNetRequest API's [`setExtensionActionOptions`](https://developer.chrome.com/docs/extensions/reference/declarativeNetRequest/#method-setExtensionActionOptions)) method to display the number of requests blocked by the extension for a given tab. This capability is important because it allows content blockers to keep end users informed without exposing potentially sensitive browsing metadata to the extension.
## Wrap up
Modernizing the Chrome extensions platform was one of our major motivations for Manifest V3. In many cases that meant switching to new technologies, but it also meant simplifying our API surface; that's what our goal was here.
I hope this post helped shed some light on this particular corner of the Manifest V3 platform. To learn more about how the Chrome team is approaching the future of browser extensions, check out the [Platform vision](https://developer.chrome.com/docs/extensions/mv3/intro/platform-vision) and [Overview of Manifest V3](https://developer.chrome.com/docs/extensions/mv3/intro/mv3-overview) pages in our developer documentation. You can also discuss Chrome extensions with other developers on the [chromium-extensions](https://groups.google.com/a/chromium.org/forum/#!forum/chromium-extensions) Google Group.
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2021-06-23 UTC.

