---
url: https://developer.chrome.com/blog/extension-news-july-2024?hl=en
title: https://developer.chrome.com/blog/extension-news-july-2024?hl=en
date: 2025-05-11T16:55:48.328701
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/extension-news-july-2024?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/extension-news-july-2024?hl=es-419)

Sign in


  * On this page
  * [Manifest V2 phase out begins](https://developer.chrome.com/blog/extension-news-july-2024?hl=en#manifest_v2_phase_out_begins)
  * [Declarative Net Request fast-track: Expedited review for extensions with safe rule updates](https://developer.chrome.com/blog/extension-news-july-2024?hl=en#declarative_net_request_fast-track_expedited_review_for_extensions_with_safe_rule_updates)
  * [New action.openPopup API](https://developer.chrome.com/blog/extension-news-july-2024?hl=en#new_actionopenpopup_api)
  * [Updates to side panel UI](https://developer.chrome.com/blog/extension-news-july-2024?hl=en#updates_to_side_panel_ui)
  * [Origin trials in extensions](https://developer.chrome.com/blog/extension-news-july-2024?hl=en#origin_trials_in_extensions)
  * [Extensions which interact with YouTube need to migrate to Trusted Types](https://developer.chrome.com/blog/extension-news-july-2024?hl=en#extensions_which_interact_with_youtube_need_to_migrate_to_trusted_types)
  * [Documentation updates](https://developer.chrome.com/blog/extension-news-july-2024?hl=en#documentation_updates)
  * [Upcoming features](https://developer.chrome.com/blog/extension-news-july-2024?hl=en#upcoming_features)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  What's happening in Chrome Extensions? 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Manifest V2 phase out begins](https://developer.chrome.com/blog/extension-news-july-2024?hl=en#manifest_v2_phase_out_begins)
  * [Declarative Net Request fast-track: Expedited review for extensions with safe rule updates](https://developer.chrome.com/blog/extension-news-july-2024?hl=en#declarative_net_request_fast-track_expedited_review_for_extensions_with_safe_rule_updates)
  * [New action.openPopup API](https://developer.chrome.com/blog/extension-news-july-2024?hl=en#new_actionopenpopup_api)
  * [Updates to side panel UI](https://developer.chrome.com/blog/extension-news-july-2024?hl=en#updates_to_side_panel_ui)
  * [Origin trials in extensions](https://developer.chrome.com/blog/extension-news-july-2024?hl=en#origin_trials_in_extensions)
  * [Extensions which interact with YouTube need to migrate to Trusted Types](https://developer.chrome.com/blog/extension-news-july-2024?hl=en#extensions_which_interact_with_youtube_need_to_migrate_to_trusted_types)
  * [Documentation updates](https://developer.chrome.com/blog/extension-news-july-2024?hl=en#documentation_updates)
  * [Upcoming features](https://developer.chrome.com/blog/extension-news-july-2024?hl=en#upcoming_features)


Milica Mihajlija 
[ GitHub ](https://github.com/mihajlija) [ Homepage ](https://mihajlija.github.io/)
The first half of the year is over and a lot has happened in the Chrome Extensions platform and the Web Store. We've rolled out several significant updates and new features that we're excited to share with you. In this blog post we give you a summary of what happened in Chrome Extensions in the past three months.
## Manifest V2 phase out begins
As planned, on June 3rd, we started warning users that Manifest Version 2 extensions will soon go away. This warning has continued to roll out across Chrome channels. Following this, we will begin disabling Manifest V2 extensions. Users will still be able to re-enable these extensions if they choose.
## Google I/O
Another Google I/O is behind us and we have covered all the exciting extensions updates! There's a preview of a new menu that will give users more control and with the newly introduced version rollback feature developers can quickly re-deploy the previously published version of an extension without the need to wait for review. Plus, we recapped the Chrome Web Store refresh which highlights the best extensions. Head over to YouTube to [check out the full video](https://www.youtube.com/watch?v=hvxOW21na48) and read [our blog post](https://developer.chrome.com/blog/extensions-io-24) for some of the highlights.
## Declarative Net Request fast-track: Expedited review for extensions with safe rule updates
Chrome extensions using the Declarative Net Request API (DNR) can bypass review for updates that only modify safe static rules within the rule_resources manifest key. The re-deployed extension changes will go live within minutes, as long as the extension hasn't been flagged for policy violations and other eligibility criteria are met.
Developers must opt in to this expedited review process through the Chrome Web Store Developer Dashboard or Publish API. Learn more about eligibility and how to opt-in in the [Chrome Web Store documentation](https://developer.chrome.com/docs/webstore/skip-review).
## New action.openPopup API
Beginning in Chrome 127, the [action.openPopup](https://developer.chrome.com/docs/extensions/reference/api/action#method-openPopup) API is now available to all extensions. This change was highly requested by developers, including those who starred the issue in our bug tracker. The API was previously only available to extensions installed by a policy, but after discussions in the WebExtensions Community Group, we're excited to be finally launching the API to everyone. This makes Chrome and other Chromium browsers consistent with Firefox and Safari where this API is already available.
## Updates to side panel UI
[Chrome has updated the side panel UI](https://groups.google.com/a/chromium.org/g/chromium-extensions/c/5PQyHPYQuXY/m/ZbsHqqTlAgAJ) with an added pin icon to easily re-open side panels linked to an extension's action icon and removed the global side panel icon as each panel should provide its own unique experience.
If your extension uses a side panel, you may need to change how you onboard users and ensure you provide an explicit way for the panel to be opened.
## Origin trials in extensions
Starting in Chrome 126, you can opt into origin trials and deprecation trials across all extension surfaces. Check out the documentation on how to add a [trial_token](https://developer.chrome.com/docs/extensions/reference/manifest/trial_tokens) to your [manifest.json file](https://developer.chrome.com/docs/extensions/reference/manifest) to use a trial feature inside of a background script, popup, or offscreen document.
## Extensions which interact with YouTube need to migrate to Trusted Types
The YouTube team is improving the client-side security of YouTube with [Trusted Types](https://web.dev/articles/trusted-types), which requires third-party browser extensions to use [typed objects instead of strings](https://web.dev/trusted-types/#fix-the-violations) when assigning values to DOM APIs. Starting on July 25, 2024, browser extensions that don't comply with Trusted Types security requirements may stop working after enforcement so developers need to ensure their extensions are compatible with the new YouTube security standards. If your extension modifies HTML, and a user could use it on youtube.com, read the [instructions for how to check if your extensions are compatible](https://developer.chrome.com/blog/trusted-types-on-youtube#developers) and will operate properly after the feature enforcement.
## Documentation updates
We recently updated our Chrome Web Store API documentation to include information about [deployPercentage](https://developer.chrome.com/docs/webstore/api#parameters-publish), which lets you assign a percentage of a partial rollout deployment.
We've also added a new [content filtering ](https://developer.chrome.com/docs/extensions/develop/concepts/content-filtering)guide. You can learn more about network filtering with the Declarative Net Request API, find details about the limitations on the number of rules that can be included in an extension, learn how users can define their own filtering rules, and more.
## Upcoming features
We're working on a new API proposal for supporting multiple user script worlds in extensions, allowing user script managers to better isolate individual user scripts when multiple may be injected on a given site. To learn more, check out the [WECG Multiple user script worlds proposal](https://github.com/w3c/webextensions/pull/560).
Another exciting feature proposal we're working on is enabling developers to enhance extension icon visibility in dark mode by supplying a set of dark mode icons. For more details, check out the [Dark mode extension icon support WECG proposal](https://github.com/w3c/webextensions/pull/585).
## 🗃️ New videos
Patrick from the Chrome Extensions team explains the concept of Remotely Hosted Code (RHC) in Chrome extensions. Learn why RHC is no longer allowed, how to detect it, and what to do if your extension needs to be updated in [What is a Remote Hosted Code?](https://www.youtube.com/watch?v=aYxzHUX_elo&ab_channel=ChromeforDevelopers).
Patrick and Oliver also met with the Chrome Web Store review team in person to unpack the intricacies of the review process. They asked all the questions and feedback you shared, check it out in [Behind the Chrome Web Store: Asking Trust & Safety your questions](https://www.youtube.com/watch?v=BHIZUT_m7AM).
Thanks again for being part of the extensions community! ❤️
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-07-10 UTC.

