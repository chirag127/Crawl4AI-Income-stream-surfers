---
url: https://docs.expo.dev/review/share-previews-with-your-team
title: https://docs.expo.dev/review/share-previews-with-your-team
date: 2025-04-30T17:12:05.565824
depth: 1
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Share previews with your team
Share previews of your app with your team by publishing updates on branches.
Once you've made changes on a branch, you can share them with your team by publishing an update. This allows you to get feedback on your changes during review.
The following steps will outline a basic flow for publishing a preview of your changes, and then sharing it with your team. For a more comprehensive resource, see the [Preview updates](https://docs.expo.dev/eas-update/preview) guide.
## Publish a preview of your changes
You can publish a preview of your current changes by running the following [EAS CLI](https://docs.expo.dev/develop/tools#eas-cli) command:
Terminal
Copy
`- ``eas update --auto`
This command will publish an update under the current branch name.
## Share with your team
Once the preview is published, you'll see output like this in the terminal window:
Terminal
`✔ Published!``...``EAS Dashboard   https://expo.dev/accounts/your-account/projects/your-project/updates/708b05d8-9bcf-4212-a052-ce40583b04fd`
Share the EAS dashboard link with a reviewer. After opening the link, they can click on the Preview button. They will see a QR code that they can scan to open the preview on their device.
## Learn more
[Preview updatesLearn how to preview updates in development, preview, and production builds.](https://docs.expo.dev/eas-update/preview)

