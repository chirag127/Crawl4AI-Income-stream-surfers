---
url: https://developer.chrome.com/blog/firefox-support-in-puppeteer-with-webdriver-bidi?hl=en
title: https://developer.chrome.com/blog/firefox-support-in-puppeteer-with-webdriver-bidi?hl=en
date: 2025-05-11T16:56:02.805214
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/firefox-support-in-puppeteer-with-webdriver-bidi?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/firefox-support-in-puppeteer-with-webdriver-bidi?hl=es-419)




  * On this page
  * [Firefox, CDP, and Puppeteer](https://developer.chrome.com/blog/firefox-support-in-puppeteer-with-webdriver-bidi?hl=en#firefox_cdp_and_puppeteer)
  * [Teamwork makes the dream work](https://developer.chrome.com/blog/firefox-support-in-puppeteer-with-webdriver-bidi?hl=en#teamwork_makes_the_dream_work)
  * [CDP support in the future](https://developer.chrome.com/blog/firefox-support-in-puppeteer-with-webdriver-bidi?hl=en#cdp_support_in_the_future)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  WebDriver BiDi production-ready in Firefox, Chrome and Puppeteer 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Firefox, CDP, and Puppeteer](https://developer.chrome.com/blog/firefox-support-in-puppeteer-with-webdriver-bidi?hl=en#firefox_cdp_and_puppeteer)
  * [Teamwork makes the dream work](https://developer.chrome.com/blog/firefox-support-in-puppeteer-with-webdriver-bidi?hl=en#teamwork_makes_the_dream_work)
  * [CDP support in the future](https://developer.chrome.com/blog/firefox-support-in-puppeteer-with-webdriver-bidi?hl=en#cdp_support_in_the_future)


Matthias Rohmer 
[ GitHub ](https://github.com/matthiasrohmer) [ LinkedIn ](https://www.linkedin.com/in/matthias-rohmer-b09191b0) [ Bluesky ](https://bsky.app/profile/matthiasrohmer.bsky.social)
Just last week, together with BrowserStack, we announced WebDriver BiDi becoming [production-ready in BrowserStack](https://developer.chrome.com/blog/webdriver-bidi-support-in-browserstack). This week the summer of [WebDriver BiDi](https://developer.chrome.com/blog/webdriver-bidi) continues with Firefox 129 and Puppeteer 23 each getting production-ready support for WebDriver BiDi!
Mozilla has been a strong collaborator on WebDriver BiDi for over four years now, initially helping to shape the new standard and then gradually implementing it in Firefox, neatly documenting their progress with the [Firefox WebDriver Newsletter](https://fxdx.dev/category/remote-protocols/webdriver-bidi/).
With WebDriver BiDi now production-ready in Firefox, Puppeteer, from version 23, offers stable support for Firefox through WebDriver BiDi. This lets you automate Firefox with the same concise API as Chrome. Puppeteer's support for Chrome DevTools Protocol (CDP) remains unchanged.
## Firefox, CDP, and Puppeteer
Puppeteer is a reliable tool for developers to automate Chromium-based browsers using the Chrome DevTools Protocol, also known as CDP. In 2019 Puppeteer got experimental support for Firefox.
To make this work, Mozilla implemented and maintained a subset of CDP in Firefox. This solution let Firefox be automated with the Puppeteer API, but it had caveats:
  * As the name suggests, the CDP is used by Chrome's DevTools and needs to change with DevTools requirements.
  * The CDP is not standardized in a shared, public specification and maintaining it in Firefox required steady communication and effort.
  * Since Firefox only implemented a subset of CDP, Puppeteer could never guarantee its full API to work with Firefox, creating confusion for users.


While we're glad to have maintained this support together with Mozilla for the last few years, we always knew it wasn't a permanent solution. Building on this partnership, and [including other major browser and tooling vendors](https://www.w3.org/groups/wg/browser-tools-testing/), together we created WebDriver BiDi.
## Teamwork makes the dream work
The Firefox team has been eagerly working to implement WebDriver BiDi in Firefox. At the same time the Puppeteer team has been expanding WebDriver BiDi support across the Puppeteer API. The goal that both teams worked towards was to make every API required for production automation use cases available using WebDriver BiDi in Puppeteer, ensuring support in both Chrome and Firefox.
Shared team dashboard showing the number of passing tests over the last few months. 
This lets Puppeteer users select either Firefox or Chrome for their automations, by specifying the `browser` configuration key when launching a Puppeteer instance.
```
importpuppeteerfrom'puppeteer';
constfirefoxBrowser=awaitpuppeteer.launch({
browser:'firefox',// WebDriver BiDi is used by default in Firefox.
});
constpage=awaitfirefoxBrowser.newPage();
...
awaitfirefoxBrowser.close();
constchromeBrowser=awaitpuppeteer.launch({
browser:'chrome',
protocol:'webDriverBiDi',// CDP would be used by default for Chrome.
});
constpage=awaitchromeBrowser.newPage();
...
awaitchromeBrowser.close();

```

To learn more about what's new in Firefox 129 and Mozilla's work on WebDriver BiDi see the related [Mozilla Hacks blog post](https://hacks.mozilla.org/2024/08/puppeteer-support-for-firefox/).
## CDP support in the future
The preceding code snippet shows that to automate Chrome using WebDriver BiDi with Puppeteer you need to explicitly set `protocol` to `webDriverBiDi`. This is because for Chrome, Puppeteer will keep defaulting to CDP—to not break existing automations, but also to keep supporting automations specialized to Chrome's features.
CDP support in Firefox is deprecated from Firefox 129 and [scheduled to be removed at the end of 2024](https://fxdx.dev/deprecating-cdp-support-in-firefox-embracing-the-future-with-webdriver-bidi/). If you have existing automations that rely on CDP support in Firefox we strongly recommend migrating to WebDriver BiDi. If that's not possible, reach out to dev-webdriver@mozilla.org with your use case.
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-08-07 UTC.

