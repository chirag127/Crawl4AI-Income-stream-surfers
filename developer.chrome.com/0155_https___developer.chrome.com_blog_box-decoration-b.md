---
url: https://developer.chrome.com/blog/box-decoration-break?hl=en
title: https://developer.chrome.com/blog/box-decoration-break?hl=en
date: 2025-05-11T16:54:03.758797
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/box-decoration-break?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/box-decoration-break?hl=es-419)




  * On this page
  * [Inline fragmentation](https://developer.chrome.com/blog/box-decoration-break?hl=en#inline_fragmentation)
  * [Block fragmentation](https://developer.chrome.com/blog/box-decoration-break?hl=en#block_fragmentation)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  The box-decoration-break property in Chrome 130 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Inline fragmentation](https://developer.chrome.com/blog/box-decoration-break?hl=en#inline_fragmentation)
  * [Block fragmentation](https://developer.chrome.com/blog/box-decoration-break?hl=en#block_fragmentation)


Rachel Andrew 
[ GitHub ](https://github.com/rachelandrew) [ LinkedIn ](https://www.linkedin.com/in/rachelandrew) [ Mastodon ](https://front-end.social/@rachelandrew) [ Bluesky ](https://bsky.app/profile/rachelandrew.bsky.social) [ Homepage ](https://rachelandrew.co.uk)
Published: October 11, 2024 
In Chrome 130 the [`box-decoration-break`](https://developer.mozilla.org/docs/Web/CSS/box-decoration-break) CSS property with a value of `clone` is available, with support for inline and block fragmentation. This post explains why and how to use it.
## Inline fragmentation
Inline fragmentation is what happens when an inline element, for example a string of text, breaks over multiple lines. Inline elements have a box, which you typically don't need to think about, unless you try to add a background or border to the element. In the following example a background with a `border-radius` is added to a span. The border only curves at the beginning and end of the string.
```
span{
background-color:#002856;
color:#fff;
border-radius:0.5em;
border:2pxsolidblack;
}

```

The initial value of `box-decoration-break` is `slice`, which gives this sliced effect on the boxes. The newly supported `box-decoration-break: clone` however, means that each line begins and ends with the rounded border.
```
span{
background-color:#002856;
color:#fff;
border-radius:0.5em;
border:2pxsolidblack;
box-decoration-break:clone;
}

```

## Block fragmentation
Block fragmentation happens if you break content into columns with multiple-column layout, or when you print and the content breaks into pages.
In the following example, content is broken into columns, and each paragraph has a border. With the initial value of `slice` the boxes are sliced at the bottom and top of columns.
```
.columns{
column-count:5;
}
.columnsp{
border:5pxsolid#34c9eb;
padding:0.5em;
}

```

With `box-decoration-break: clone`, when a box is fragmented, each fragment is wrapped with the border.
```
.columns{
column-count:5;
}
.columnsp{
border:5pxsolid#34c9eb;
padding:0.5em;
box-decoration-break:clone;
}

```

The same thing happens if you have borders on boxes that are fragmented when printing the page. If a box is split over two pages, the border on the box will complete on the first page then open a new box on the second page.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-10-11 UTC.

