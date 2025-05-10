---
url: https://docs.expo.dev/deploy/send-over-the-air-updates
title: https://docs.expo.dev/deploy/send-over-the-air-updates
date: 2025-04-30T17:11:42.813989
depth: 1
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Send over-the-air updates
Learn how to send over-the-air updates to push critical bug fixes and improvements to your users.
You can send over-the-air updates containing critical bug fixes and improvements to your users.
## Get started
> If you've published [previews](https://docs.expo.dev/review/share-previews-with-your-team) or created a [build](https://docs.expo.dev/deploy/build-project) before, you may have already set up updates and can skip this section.
To set up updates, run the following [EAS CLI](https://docs.expo.dev/develop/tools#eas-cli) command:
Terminal
Copy
`- ``eas update:configure`
After the command completes, you'll need to make new builds before continuing to the next section.
## Send an update
To send an update, run the following [EAS CLI](https://docs.expo.dev/develop/tools#eas-cli) command:
Terminal
Copy
`- ``eas update --channel production`
This command will create an update and make it available to builds of your app that are configured to receive updates on the `production` channel. This channel is defined in [eas.json](https://docs.expo.dev/eas/json#channel).
You can verify the update works by force closing the app and reopening it two times. The update should be applied on the second launch.
## Learn more
You can learn how to [rollout an update](https://docs.expo.dev/eas-update/rollouts), [optimize assets](https://docs.expo.dev/eas-update/optimize-assets), and more with our [update guides](https://docs.expo.dev/eas-update/introduction).

