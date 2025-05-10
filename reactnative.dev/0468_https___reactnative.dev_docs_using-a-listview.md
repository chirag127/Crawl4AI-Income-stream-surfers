---
url: https://reactnative.dev/docs/using-a-listview
title: https://reactnative.dev/docs/using-a-listview
date: 2025-05-10T21:42:47.000690
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/using-a-listview#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
React Native provides a suite of components for presenting lists of data. Generally, you'll want to use either [FlatList](https://reactnative.dev/docs/flatlist) or [SectionList](https://reactnative.dev/docs/sectionlist).
The `FlatList` component displays a scrolling list of changing, but similarly structured, data. `FlatList` works well for long lists of data, where the number of items might change over time. Unlike the more generic [`ScrollView`](https://reactnative.dev/docs/using-a-scrollview), the `FlatList` only renders elements that are currently showing on the screen, not all the elements at once.
The `FlatList` component requires two props: `data` and `renderItem`. `data` is the source of information for the list. `renderItem` takes one item from the source and returns a formatted component to render.
This example creates a basic `FlatList` of hardcoded data. Each item in the `data` props is rendered as a `Text` component. The `FlatListBasics` component then renders the `FlatList` and all `Text` components.
If you want to render a set of data broken into logical sections, maybe with section headers, similar to `UITableView`s on iOS, then a [SectionList](https://reactnative.dev/docs/sectionlist) is the way to go.
One of the most common uses for a list view is displaying data that you fetch from a server. To do that, you will need to [learn about networking in React Native](https://reactnative.dev/docs/network).
Is this page useful?

