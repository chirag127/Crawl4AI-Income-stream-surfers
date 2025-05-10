---
url: https://expo.dev/changelog/2024-11-14-channel-pausing
title: https://expo.dev/changelog/2024-11-14-channel-pausing
date: 2025-04-30T17:19:02.442938
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [Channel pausing for EAS Update](https://expo.dev/changelog/2024-11-14-channel-pausing)
Nov 14, 2024 by
Juwan Wheatley
Channel pausing for [EAS Update](https://docs.expo.dev/eas-update/introduction/) is now available. With channel pausing, you can disable sending updates to specific deployments, which allows you to better control update distribution and prevent runaway EAS Update usage.
Developers can pause and resume updates directly on the channel details page on [expo.dev](https://expo.dev/) or via EAS CLI with the following commands:
Terminal
`eas channel:pause <channel-name>``eas channel:resume <channel-name>`
Check it out and let us know what you think!

