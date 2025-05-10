---
url: https://expo.dev/changelog/xcode-16-3-patches
title: https://expo.dev/changelog/xcode-16-3-patches
date: 2025-04-30T17:19:25.157245
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [SDK 52 patches for Xcode 16.3](https://expo.dev/changelog/xcode-16-3-patches)
Apr 2, 2025 by
Christian Falch
We have released patches for four modules to address a breaking change in Xcode 16.3, which was released March 31st. The breaking change is the removal of a specific base template type in C++ in LLVM 19 (the Xcode compiler) and introduces errors when building Expo apps. You may encounter an error like this ([GitHub issue](https://github.com/expo/expo/issues/35807)):
Xcode 16.3 build error
Copy
```

 298 |  static_assert(is_standard_layout<value_type>::value, "Character type of basic_string_view must be standard-layout");
 299 |  static_assert(is_trivial<value_type>::value, "Character type of basic_string_view must be trivial");
> 300 |  static_assert(is_same<_CharT,typenametraits_type::char_type>::value,
   |                     ^ implicit instantiation of undefined template 'std::char_traits<unsignedchar>'
 301 |         "traits_type::char_type must be the same type as CharT");
 302 | 
 303 |  // [string.view.cons], construct/copy

```

We have published a fix to the affected packages with the following versions:
  * `expo-device@7.0.3`
  * `expo-gl@15.0.5`
  * `expo-dev-client@5.0.18`
  * `expo-dev-menu@6.0.23` (installed by `expo-dev-client`)
  * `expo-dev-launcher@5.0.33` (installed by `expo-dev-client`)


Run the following command to upgrade these packages:
Terminal
Copy
`- ``npx expo install --fix`
In addition, React Native versions older than 0.77 have the same issues. This was fixed in `react-native@0.77.0` with an upgrade to the native dependency, Folly. You will need to use React Native 0.77 or newer if you are using Xcode 16.3. A fix for React Native 0.76 is in progress: [facebook/react-native#50431](https://github.com/facebook/react-native/pull/50431).
If you need to use Xcode 16.3 on your project today, you can [learn more about using React Native 0.77 in SDK 52](https://expo.dev/changelog/2025-01-21-react-native-0.77).

