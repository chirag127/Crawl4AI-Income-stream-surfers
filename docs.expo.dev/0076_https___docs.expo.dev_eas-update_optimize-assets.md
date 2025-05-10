---
url: https://docs.expo.dev/eas-update/optimize-assets
title: https://docs.expo.dev/eas-update/optimize-assets
date: 2025-04-30T17:13:13.153606
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Optimize assets for EAS Update
Learn how EAS Update downloads assets and how to optimize them for download size.
> For SDK 50 and above, the new [asset selection feature](https://docs.expo.dev/eas-update/asset-selection) can greatly reduce the total number and size of downloaded assets.
When an app finds a new update, it downloads a manifest and then downloads any new or updated assets so that it can run the update. The process is as follows:
Many users running Android and iOS apps are using mobile connections that are not as consistent or fast as when they are using Wi-Fi, so it's important that the assets shipped as a part of an update are as small as possible.
## Code assets
When publishing an update, EAS CLI runs Expo CLI to bundle the project into an update. The update will appear in our project's dist directory.
In dist/bundles, we can see the size of the index.android.js and index.ios.js files that will be part of the Android and iOS updates, respectively. Note that these are uncompressed file sizes; EAS Update uses Brotli and gzip compression, which can significantly reduce download sizes. Nevertheless, these files will be downloaded to a user's device when getting the new update if the device has not downloaded them before. Making these file sizes as small as possible helps end-users download updates quickly.
## Image assets
App users will have to download any new images or other assets when they detect a new update if those assets are not already a part of their build. You can view all the assets uploaded to EAS servers in dist/assets. The assets there are hashed with their extensions removed, so it is difficult to know what assets are there. To see a pretty-printed list of assets, we can run:
Terminal
Copy
`- ``npx expo export`
### Optimizing image assets
To manually optimize image assets in your project, you can use the `npx expo-optimize` command. It uses [sharp](https://sharp.pixelplumbing.com/) library to compress images.
Terminal
Copy
`- ``npx expo-optimize`
After running the command, all image assets are compressed except the ones that are already optimized. You can adjust the compression quality by including the `--quality [number]` option with the command. For example, to compress to 90%, run:
Terminal
Copy
`- ``npx expo-optimize --quality 90`
### Other manual optimization methods
To optimize images and videos manually, see [Assets](https://docs.expo.dev/develop/user-interface/assets#manual-optimization-methods) for more information.
## Ensuring assets are included in updates
When you publish an update, EAS will upload your assets to the CDN so that they may be fetched when users run your app. However, for assets to be uploaded to the CDN, they must be explicitly required somewhere in your application's code. Conditionally requiring assets will result in the bundler being unable to detect them, and they will not be uploaded when you publish your project.
## Further considerations
It's important to note that a user's app will only download new or updated assets. It will not re-download unchanged assets that already exist inside the app.
One way to make sure that updates stay as slim as possible is to build and submit the app frequently to the app stores so that users can download a new app binary that includes more up-to-date assets. Generally, it's a good practice to build and submit an app when adding large or multiple assets, and it's good to use updates to fix small bugs and make minor changes between app store releases.

