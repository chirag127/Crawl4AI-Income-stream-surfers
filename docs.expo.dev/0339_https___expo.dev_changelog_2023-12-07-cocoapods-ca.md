---
url: https://expo.dev/changelog/2023-12-07-cocoapods-cache
title: https://expo.dev/changelog/2023-12-07-cocoapods-cache
date: 2025-04-30T17:18:58.342050
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [Keep your cache close — It’s Faster!](https://expo.dev/changelog/2023-12-07-cocoapods-cache)
Dec 7, 2023 by
Stanisław Chmiela
At Expo we care about speed. Speed of iteration, speed of development, speed of the app, and also the speed of your app's builds. For example, here are a few of the mechanisms we use to speed up your builds on EAS Build:
we use best available infrastructure for the job (like [Apple Silicon](https://expo.dev/changelog/2023/01-31-q4-summary#m1-workers-on-eas-build)),
VMs come with useful tools preinstalled so you don't need to wait for them to install,
we maintain proxy cache servers for Node.js, NPM and [CocoaPods](https://docs.expo.dev/more/glossary-of-terms/#cocoapods) for faster and more reliable downloads
…but we’re always searching for ways to get faster…
## [How to speed up CocoaPods ](https://expo.dev/changelog/2023-12-07-cocoapods-cache#how-to-speed-up-cocoapods)
The CocoaPods cache server is good, but what if we could serve Pods from the local filesystem rather than the network?
In the first half of November we added “warm” CocoaPods cache to every Mac VM image. It includes popular remote Pods that your app may need.
The cache is created by building several different reference Expo apps on a single worker and uploading the resulting `~/Library/Caches/CocoaPods` to the cloud. When building VM templates we include that directory in the resulting image, so your builds run faster and don't rely on the network.
## [Results ](https://expo.dev/changelog/2023-12-07-cocoapods-cache#results)
In total the cache comes close to 5 GB and saves, on average, a minute from your iOS build time. For a blank new app this means “Install Pods” took 1:37 before and now it takes a whopping 12 seconds.
“Install Pods” Phase Times Comparison. Shorter is better. Values vary based on the project.
Another way you could speed up your builds is custom caching. By configuring [`cache`](https://docs.expo.dev/eas/json/#cache) [property in](https://docs.expo.dev/eas/json/#cache) [**eas.json**](https://docs.expo.dev/eas/json/#cache), you can tell EAS which directories you would like to be automatically saved and restored. Read more at [“Custom Caching”](https://docs.expo.dev/build-reference/caching/#custom-caching).

