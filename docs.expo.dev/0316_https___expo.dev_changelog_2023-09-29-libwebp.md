---
url: https://expo.dev/changelog/2023-09-29-libwebp
title: https://expo.dev/changelog/2023-09-29-libwebp
date: 2025-04-30T17:18:38.394694
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [Fix for CVE-2023-4863 in expo-image@1.3.4](https://expo.dev/changelog/2023-09-29-libwebp)
Sep 29, 2023 by
Brent Vatne
`expo-image@1.3.4` for SDK 49 has been released with a fix for [CVE-2023-4863](https://nvd.nist.gov/vuln/detail/CVE-2023-4863) — a vulnerability in [`libwebp`](https://chromium.googlesource.com/webm/libwebp) that impacted Chrome and many other applications that used the library for WebP decoding. This vulnerability was fixed in `libwebp@1.3.2`, which was released on September 13, 2023.
The following explains how to apply the fix on each Expo-supported platform, along with context on what changed.
## [Android ](https://expo.dev/changelog/2023-09-29-libwebp#android)
**Update expo-image** : run `npx expo install expo-image` on SDK 49, verify that `expo-image@1.3.4` or greater is installed, and deploy a new native build. If you are still using SDK 48, ensure that you are using `expo-image@1.0.2` or greater.
### [How to know if a build is affected ](https://expo.dev/changelog/2023-09-29-libwebp#how-to-know-if-a-build-is-affected)
Any build that used `expo-image@1.3.3` or earlier (and therefore `libweb@1.3.1` or earlier) is affected.
### [Explanation ](https://expo.dev/changelog/2023-09-29-libwebp#explanation)
In `expo-image@1.3.4`, we removed [GlideWebpDecoder](https://github.com/zjupure/GlideWebpDecoder), which (at the time of writing) depends on an outdated `libwebp` version. This dependency was responsible for animated WebP decoding in `expo-image`. We now use [APNG4Android](https://github.com/penfeizhou/APNG4Android) instead, which was already included for supporting other animated image formats. If you notice any regressions in animated WebP support in your application, [file a bug report on expo/expo](https://github.com/expo/expo/issues/new?assignees=&amp;labels=needs+validation&amp;projects=&amp;template=bug_report.yml).
## [iOS ](https://expo.dev/changelog/2023-09-29-libwebp#ios)
**Ensure that you are using libwebp** **`1.3.2`****or greater** :
**If you use** [**CNG**](https://docs.expo.dev/workflow/continuous-native-generation/), the new version of `libwebp` will be installed automatically when you generate your iOS project with `npx expo prebuild --clean` (or on EAS Build).
**If you manage your own iOS project** , you can verify in **ios/Podfile.lock** that you are using `libwebp@1.3.2`, and run `pod update libwebp` in your **ios** directory if not.
### [How to know if a build is affected ](https://expo.dev/changelog/2023-09-29-libwebp#how-to-know-if-a-build-is-affected)
**If you use EAS Build** , look in your "Install pods" logs for your build on EAS Build, and find the `libwebp` line. If you see `Installing libwebp (1.3.1)` (or any other earlier version), then it is affected.
Alternatively, on the commit where you created your last build, check the **Podfile.lock** in your **ios** directory for `libwebp`. If you are using `1.3.1` or earlier, then it is affected.
### [Explanation ](https://expo.dev/changelog/2023-09-29-libwebp#explanation)
`libwebp@1.3.2`, [released on September 13, 2023](https://github.com/webmproject/libwebp/releases/tag/v1.3.2), matches the version constraint specified by `SDWebImageWebPCoder` (`~> 1.0`), so any new installs in the last ~2 weeks will have automatically picked this up.
## [Web ](https://expo.dev/changelog/2023-09-29-libwebp#web)
No changes are required on your part, `libwebp` is part of Chrome.
## [Other platforms ](https://expo.dev/changelog/2023-09-29-libwebp#other-platforms)
If you support platforms beyond those listed above, be sure to check with the related frameworks that you use to see if they are affected.

