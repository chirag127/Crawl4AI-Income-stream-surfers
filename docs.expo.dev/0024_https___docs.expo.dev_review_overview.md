---
url: https://docs.expo.dev/review/overview
title: https://docs.expo.dev/review/overview
date: 2025-04-30T17:12:04.471482
depth: 1
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Overview of distributing apps for review
Learn about how to distribute your app for review using app stores, internal distribution, and EAS Update.
This page outlines three approaches to sharing a preview version of your app with your team for QA and review: app store testing tracks, internal distribution, and development builds with EAS Update.
Can I use Expo Go for reviewing releases?
Even though Expo Go is an open-source sandbox that can be good for previewing isolated prototypes on Android and iOS, it is not intended for production apps. It should be avoided during the preview process of your app.
## App store testing tracks
When distributing apps through app store testing tracks, you can only use release builds. You cannot use this method to distribute development builds. An alternative approach is to use ["Internal distribution"](https://docs.expo.dev/review/overview#internal-distribution-with-eas-build), which works with both release and development builds.
Android: Google Play Beta
Before a complete public release, [Google Play beta](https://support.google.com/googleplay/android-developer/answer/9845334?visit_id=638740965629093187-3840249980&rd=1) is another option to distribute your app to testers. You can set up either an internal, closed, or open test track and control who has access to the app.
Each test track has its own requirements. For the internal track, you can only invite up to 100 testers. Both closed and open tracks support larger groups of testers. In closed tracks, you need to invite testers, while in open tracks, anyone can join your program.
To use Google Play beta, you need to upload your app as an AAB (Android App Bundle) to the Google Play Console, set up a test track, and invite users via email or a shareable link. Testers can install the app through the Play Store, and you can collect feedback and crash reports directly from the Google Play Console.
iOS: TestFlight
TestFlight is another option to distribute your app to iOS devices. TestFlight also requires a paid Apple Developer account. TestFlight's internal testing option allows you to create test groups that include up to 100 members of your Apple Developer account team, who then download the app through the TestFlight app. Some teams prefer TestFlight because it doesn't require a new build to add new testers, and apps stay updated automatically.
TestFlight also includes an external testing option that allows you to share your app with up to 10,000 users via an email or a public link.
Both internal and external test distribution in TestFlight require you to [upload your app](https://docs.expo.dev/submit/ios) to App Store Connect and wait for the automated review before you can share a build. However, external test builds will need to go through a more formal App Store review (which is distinct from the review that your app must undergo before production release) before being distributed.
[EAS SubmitLearn how to upload your app to app store testing and release tracks.](https://docs.expo.dev/submit/introduction)
## Internal distribution with EAS Build
[Internal distribution](https://docs.expo.dev/build/internal-distribution) is a feature provided by EAS that allows developers to create builds and easily share them with a URL. The URL can be opened on a device to install the app. The app is provided as an installable APK for Android or an ad hoc provisioned app for iOS.
As soon as an internal distribution build is created, it is available for download and installation — no need to fill out any forms or wait for approval/processing. You can use internal distribution to share both release and development builds.
[How to set up an internal distribution buildLearn how EAS Build provides shareable URLs for your builds with your team for internal distribution.](https://docs.expo.dev/build/internal-distribution)
## Development builds and EAS Update
You can use [development builds](https://docs.expo.dev/develop/development-builds/introduction) to load previews of your app during the review stage by publishing an update with [EAS Update](https://docs.expo.dev/eas-update/introduction). After sharing a development build through internal distribution and installing it, you can launch any update that you published with EAS Update, as long as it is compatible with the installed build. Learn more about [Runtime versions and updates](https://docs.expo.dev/eas-update/runtime-versions).
You can use the Expo dashboard to launch updates and share a link to a specific update. You can explore and launch updates directly from a development build. You can configure GitHub actions to automatically publish updates on PRs and commits.
This approach is uniquely powerful because it allows you to respond to feedback as quickly as you can run `eas update`. It can take seconds to share a new version of your app with your team, and you can do so without needing to rebuild the app or upload it to a store test track.
[Get started with EAS UpdateLearn how to get started using `expo-updates` library and use EAS Update in your project.](https://docs.expo.dev/eas-update/getting-started) [Use GitHub ActionsLearn how to use GitHub Actions to automate the process of publishing updates with EAS Update. It also makes deploying updates consistent and fast, leaving you more time to develop your app.](https://docs.expo.dev/eas-update/github-actions) [Use `expo-dev-client` with EAS UpdateLearn how to use `expo-dev-client` in your project to launch different app versions and preview a published update inside a development build.](https://docs.expo.dev/eas-update/expo-dev-client)

