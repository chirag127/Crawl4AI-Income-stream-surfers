---
url: https://expo.dev/changelog/eas-build-workflows-m4-pro
title: https://expo.dev/changelog/eas-build-workflows-m4-pro
date: 2025-04-30T17:19:25.279329
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [EAS Build & Workflows: introducing M4 Pro](https://expo.dev/changelog/eas-build-workflows-m4-pro)
Mar 25, 2025 by
James Ide
EAS is introducing M4 Pro-powered workers for iOS build jobs and other CI/CD workflow jobs that run on macOS. They are enabled by default and build times are over 1.85x faster on average.
We're continuously improving EAS and most recently, we've boosted the performance of iOS build jobs and all other CI/CD jobs that run on macOS by introducing workers powered by M4 Pro.
## [Performance ](https://expo.dev/changelog/eas-build-workflows-m4-pro#performance)
Each job differs but to give a general sense of the performance improvement you can expect, the average build job runs about 1.85x faster — a 45-50% reduction in build time — with the new workers. This is due to more CPU cores, more memory, and the newer chip architecture.
#### [Real-world average build times over one day ](https://expo.dev/changelog/eas-build-workflows-m4-pro#real-world-average-build-times-over-one-day)
The new M4 Pro-based workers finish builds in about half the time as the old workers (lower is better)
## [How to use them ](https://expo.dev/changelog/eas-build-workflows-m4-pro#how-to-use-them)
M4 Pro-based workers are enabled by default. You do not need to do anything to use them. Customers running paid build jobs will receive priority to run their jobs run on a new, faster worker. We have provisioned enough capacity to cover EAS's customers. Thank you for your support.
Developers on the Free plan also may be assigned M4 Pro-based workers but do not receive priority access. We will make M4 Pro-based workers the default for the Free plan over the next couple of weeks.
## [Pricing ](https://expo.dev/changelog/eas-build-workflows-m4-pro#pricing)
There is no change in pricing for these upgraded workers. Developers will enjoy faster iteration speed without needing to spend more or think about pricing changes.
## [Let us know ](https://expo.dev/changelog/eas-build-workflows-m4-pro#let-us-know)
Let us know on [X](https://x.com/expo) and [Bluesky](https://bsky.app/profile/did:plc:xinso5nzzhsfncnr5rtsoqba) how your EAS build times have improved compared to a few weeks ago. You can also [contact us](https://expo.dev/contact) through our website if you encounter compatibility problems with the new workers. So far, we have observed only performance improvements and think this change will give you even more iteration speed as app developers.

