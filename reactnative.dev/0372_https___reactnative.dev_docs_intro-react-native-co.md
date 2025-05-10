---
url: https://reactnative.dev/docs/intro-react-native-components
title: https://reactnative.dev/docs/intro-react-native-components
date: 2025-05-10T21:40:25.798913
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/intro-react-native-components#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
React Native is an open source framework for building Android and iOS applications using [React](https://reactjs.org/) and the app platform’s native capabilities. With React Native, you use JavaScript to access your platform’s APIs as well as to describe the appearance and behavior of your UI using React components: bundles of reusable, nestable code. You can learn more about React in the next section. But first, let’s cover how components work in React Native.
## Views and mobile development[​](https://reactnative.dev/docs/intro-react-native-components#views-and-mobile-development "Direct link to Views and mobile development")
In Android and iOS development, a **view** is the basic building block of UI: a small rectangular element on the screen which can be used to display text, images, or respond to user input. Even the smallest visual elements of an app, like a line of text or a button, are kinds of views. Some kinds of views can contain other views. It’s views all the way down!
Just a sampling of the many views used in Android and iOS apps.
## Native Components[​](https://reactnative.dev/docs/intro-react-native-components#native-components "Direct link to Native Components")
In Android development, you write views in Kotlin or Java; in iOS development, you use Swift or Objective-C. With React Native, you can invoke these views with JavaScript using React components. At runtime, React Native creates the corresponding Android and iOS views for those components. Because React Native components are backed by the same views as Android and iOS, React Native apps look, feel, and perform like any other apps. We call these platform-backed components **Native Components.**
React Native comes with a set of essential, ready-to-use Native Components you can use to start building your app today. These are React Native's **Core Components**.
caution
This documentation references a legacy set of API and needs to be updated to reflect the New Architecture
React Native also lets you build your own Native Components for [Android](https://reactnative.dev/docs/legacy/native-components-android) and [iOS](https://reactnative.dev/docs/legacy/native-components-ios) to suit your app’s unique needs. We also have a thriving ecosystem of these **community-contributed components.** Check out [Native Directory](https://reactnative.directory) to find what the community has been creating.
## Core Components[​](https://reactnative.dev/docs/intro-react-native-components#core-components "Direct link to Core Components")
React Native has many Core Components for everything from controls to activity indicators. You can find them all [documented in the API section](https://reactnative.dev/docs/components-and-apis). You will mostly work with the following Core Components:
React Native UI Component| Android View| iOS View| Web Analog| Description  
---|---|---|---|---  
`<View>`| `<ViewGroup>`| `<UIView>`| A non-scrolling `<div>`| A container that supports layout with flexbox, style, some touch handling, and accessibility controls  
`<Text>`| `<TextView>`| `<UITextView>`| `<p>`| Displays, styles, and nests strings of text and even handles touch events  
`<Image>`| `<ImageView>`| `<UIImageView>`| `<img>`| Displays different types of images  
`<ScrollView>`| `<ScrollView>`| `<UIScrollView>`| `<div>`| A generic scrolling container that can contain multiple components and views  
`<TextInput>`| `<EditText>`| `<UITextField>`| `<input type="text">`| Allows the user to enter text  
In the next section, you will start combining these Core Components to learn about how React works. Have a play with them here now!
Because React Native uses the same API structure as React components, you’ll need to understand React component APIs to get started. The [next section](https://reactnative.dev/docs/intro-react) makes for a quick introduction or refresher on the topic. However, if you’re already familiar with React, feel free to [skip ahead](https://reactnative.dev/docs/handling-text-input).
Is this page useful?
  * [Views and mobile development](https://reactnative.dev/docs/intro-react-native-components#views-and-mobile-development)
  * [Native Components](https://reactnative.dev/docs/intro-react-native-components#native-components)
  * [Core Components](https://reactnative.dev/docs/intro-react-native-components#core-components)



