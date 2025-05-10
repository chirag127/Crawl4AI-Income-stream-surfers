---
url: https://expo.dev/changelog/2023-08-08-rollouts-eas-update
title: https://expo.dev/changelog/2023-08-08-rollouts-eas-update
date: 2025-04-30T17:18:38.428653
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [Rollouts for EAS Update](https://expo.dev/changelog/2023-08-08-rollouts-eas-update)
Aug 8, 2023 by
Quin Jung
EAS Update allows you to ship critical bug fixes and improvements to your end-users between app store releases. By default, published updates go to 100% of users running a compatible build. While this can get changes to your end users quickly, it also can be risky.
For developers who want more control, we're releasing percentage-based rollouts with EAS Update in Developer Preview.
You can get started by publishing an update to a new EAS Update branch you'd like to roll out. You can do this with `eas update --branch [branch-name]`.
Then, you can start a rollout with `npx eas-cli@latest channel:rollout`. Once your rollout has begun, you can rerun this command to increase, decrease, or end the rollout.
Learn more in our EAS Update [docs](https://docs.expo.dev/eas-update/rollouts/).
### [Usage ](https://expo.dev/changelog/2023-08-08-rollouts-eas-update#usage)
Terminal
Copy
`npx eas-cli@latest channel:rollout`
Since this feature is currently in Developer Preview, it is not advised to use it in production workflows yet and website support will be coming soon. We'd love to hear your feedback on it, so email rollouts@expo.dev if you have any thoughts or questions.

