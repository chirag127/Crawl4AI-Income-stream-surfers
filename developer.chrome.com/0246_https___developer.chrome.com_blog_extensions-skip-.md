---
url: https://developer.chrome.com/blog/extensions-skip-review-eligible-changes?hl=en
title: https://developer.chrome.com/blog/extensions-skip-review-eligible-changes?hl=en
date: 2025-05-11T16:56:01.635382
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/extensions-skip-review-eligible-changes?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/extensions-skip-review-eligible-changes?hl=es-419)

Sign in


  * On this page
  * [Why are we making this change?](https://developer.chrome.com/blog/extensions-skip-review-eligible-changes?hl=en#why_are_we_making_this_change)
  * [How can I qualify?](https://developer.chrome.com/blog/extensions-skip-review-eligible-changes?hl=en#how_can_i_qualify)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  Skip review for eligible changes to extensions 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Why are we making this change?](https://developer.chrome.com/blog/extensions-skip-review-eligible-changes?hl=en#why_are_we_making_this_change)
  * [How can I qualify?](https://developer.chrome.com/blog/extensions-skip-review-eligible-changes?hl=en#how_can_i_qualify)


Josh Hews 
We are excited to announce a new feature that will allow developers to skip the review process for eligible changes to Manifest V3 extensions using the [Declarative Net Request API](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest).
## Why are we making this change?
In Manifest V3, developers of content filtering extensions make heavy use of the Declarative Net Request API. These extensions rely on filter lists which can change often and need to be kept up to date for users. We already support dynamic rules and we are adding this option to make sure developers can continue to offer the same set of capabilities in MV3.
Before MV3, making a change like this would have been hard because we couldn't statically determine what an extension was capable of. Moving towards a more declarative API opened up this possibility to us.
## How can I qualify?
You will now be able to publish updates to [safe static rules](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest#safe_rules) in your extensions without needing to go through review. Once submitted these changes will go live in a few minutes. Refer to the [skip review for eligible changes documentation](https://developer.chrome.com/docs/webstore/skip-review) for more details on eligibility.
When submitting your change for review in the Developer Dashboard you will have an option to request to skip review before confirming.
"Submit for review" dialog in the Developer Dashboard
Once you submit for review we will verify your item qualifies. If we detect ineligible changes we will let you know and confirm if you want to proceed with a standard review.
Warning for non-eligible submissions
In addition to the Developer Dashboard, you will also be able to request skipping review when publishing with the API. Refer to [Chrome Web Store API documentation](https://developer.chrome.com/docs/webstore/api#publish) for details on how.
This feature is live now, and the Chrome Web Store team is looking forward to continuing to improve the publishing experience for developers.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-05-30 UTC.

