---
url: https://reactnative.dev/docs/using-a-scrollview
title: https://reactnative.dev/docs/using-a-scrollview
date: 2025-05-10T21:42:46.839513
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/using-a-scrollview#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
The [ScrollView](https://reactnative.dev/docs/scrollview) is a generic scrolling container that can contain multiple components and views. The scrollable items can be heterogeneous, and you can scroll both vertically and horizontally (by setting the `horizontal` property).
This example creates a vertical `ScrollView` with both images and text mixed together.
ScrollViews can be configured to allow paging through views using swiping gestures by using the `pagingEnabled` props. Swiping horizontally between views can also be implemented on Android using the [ViewPager](https://github.com/react-native-community/react-native-viewpager) component.
On iOS a ScrollView with a single item can be used to allow the user to zoom content. Set up the `maximumZoomScale` and `minimumZoomScale` props and your user will be able to use pinch and expand gestures to zoom in and out.
The ScrollView works best to present a small number of things of a limited size. All the elements and views of a `ScrollView` are rendered, even if they are not currently shown on the screen. If you have a long list of items which cannot fit on the screen, you should use a `FlatList` instead. So let's [learn about list views](https://reactnative.dev/docs/using-a-listview) next.
Is this page useful?

