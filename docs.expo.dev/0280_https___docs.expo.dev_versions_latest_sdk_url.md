---
url: https://docs.expo.dev/versions/latest/sdk/url
title: https://docs.expo.dev/versions/latest/sdk/url
date: 2025-04-30T17:17:50.720857
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# URL
Standard URL API available on all Expo-supported platforms.
Android
iOS
tvOS
Web
The standard URL API is available on all Expo-supported platforms.
## Installation
This API is part of the `expo` package. On native platforms, built-in `URL` and `URLSearchParams` implementations replace the shims in `react-native`. Refer to the [browser and server runtime support](https://caniuse.com/url) for web and Node.js.
## Usage
```
const url = new URL('https://expo.dev');
const params = new URLSearchParams();

```

## Conformance
Expo's built-in URL support attempts to be fully [spec compliant](https://developer.mozilla.org/en-US/docs/Web/API/URL).
The only missing exception is that native platforms do not currently support [non-ASCII characters](https://unicode.org/reports/tr46/) in the hostname.
Consider the following example:
```
console.log(new URL('http://🥓').toString());

```

This outputs the following:
  * Web, Node.js: `http://xn--pr9h/`
  * Android, iOS: `http://🥓/`



