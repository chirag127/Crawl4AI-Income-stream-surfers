---
url: https://docs.expo.dev/versions/latest/sdk/encoding
title: https://docs.expo.dev/versions/latest/sdk/encoding
date: 2025-04-30T17:16:13.097745
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Encoding
Standard TextEncoder and TextDecoder APIs available on all Expo-supported platforms.
Android
iOS
tvOS
Web
The standard URL API is available on all Expo-supported platforms.
## Installation
This API is part of the `expo` package. Refer to the [browser and server runtime support](https://caniuse.com/textencoder) for web and Node.js.
## Usage
`TextEncoder` and `TextDecoder` are available globally without any need to import them.
```
// [104, 101, 108, 108, 111]
const hello = new TextEncoder().encode('hello');
// "hello"
const text = new TextDecoder().decode(hello);

```

## TextEncoder
The `TextEncoder` API is included in the Hermes engine. See the [source code in TextEncoder.cpp inside the Hermes GitHub repository](https://github.com/facebook/hermes/blob/9e2bbf8eda15936ee00aee4f8e024ceaa7cd800d/lib/VM/JSLib/TextEncoder.cpp#L1).
## TextDecoder
The `TextDecoder` API is not [spec-compliant](https://encoding.spec.whatwg.org/#textdecoder) on native platforms. Only the UTF-8 encoding is supported. If you need support for more encodings, use a polyfill like [`text-encoding`](https://www.npmjs.com/package/text-encoding).

