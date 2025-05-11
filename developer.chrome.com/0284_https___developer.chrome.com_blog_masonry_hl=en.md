---
url: https://developer.chrome.com/blog/masonry?hl=en
title: https://developer.chrome.com/blog/masonry?hl=en
date: 2025-05-11T16:56:47.790416
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/masonry?hl=en#main-content)
Sign in


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  An alternative proposal for CSS masonry 
Stay organized with collections  Save and categorize content based on your preferences. 
Rachel Andrew 
[ GitHub ](https://github.com/rachelandrew) [ LinkedIn ](https://www.linkedin.com/in/rachelandrew) [ Mastodon ](https://front-end.social/@rachelandrew) [ Bluesky ](https://bsky.app/profile/rachelandrew.bsky.social) [ Homepage ](https://rachelandrew.co.uk)
The Chrome team is keen to see an implementation of masonry type layouts on the web. However, we feel that implementing it as part of the CSS Grid specification as proposed in the [recent WebKit post](https://webkit.org/blog/15269/help-us-invent-masonry-layouts-for-css-grid-level-3) would be a mistake. We also feel that the WebKit post argued against a version of masonry that no one was proposing.
Therefore, this post aims to explain why we at Chrome have concerns about implementing masonry as part of the CSS Grid Layout specification, and clarify exactly what the alternate proposal enables. In short:
  * The Chrome team is very keen to unblock masonry, we know it's something developers want.
  * Adding masonry to the grid specification is problematic for reasons other than whether you think masonry is a grid or not.
  * Defining masonry outside of the grid specification does not prevent multiple track sizes for masonry, or the use of properties such as alignment or gaps, or any other features used in grid layout.


## Should masonry be part of grid?
The Chrome team believes that masonry should be a [separate layout method](https://github.com/w3c/csswg-drafts/issues/9041#issuecomment-2075210820), defined using `display: masonry` (or another keyword should a better name be decided upon). Later in this post, you can see some examples of what that could look like in code.
There are two related reasons why we feel that masonry is better defined outside of grid layout—the potential of layout performance issues, and the fact that both masonry and grid have features that make sense in one layout method but not the other.
### Performance
Grid and masonry are opposite in terms of how the browser deals with sizing and placement. When a grid is laid out, all items are placed before layout and the browser knows exactly what is in each track. This enables the complex intrinsic sizing that's so useful in grid. With masonry, the items are placed as they are laid out, and the browser doesn't know how many are in each track. This isn't a problem with all intrinsic sized tracks or all fixed sized tracks but is if you mix fixed and intrinsic tracks. To get round the problem, the browser needs to do a pre-layout step of laying out every item in every possible way to get measurements, with a large grid this would contribute to layout performance issues.
Therefore, if you had a masonry layout with a track definition of `grid-template-columns: 200px auto 200px`—a very common thing to do in grid—you start to run into problems. [These problems become exponential once you add subgrids](https://github.com/w3c/csswg-drafts/issues/10053).
There is an argument that most people won't run into this, however we already know that people [do have very large grids](https://issues.chromium.org/issues/40225429). We don't want to ship something that has limits to how it can be used, when there is an alternative approach.
### What do we do about the things that don't make sense in each layout method?
When flexbox and grid became part of CSS, developers often felt that they behaved in an inconsistent way. The inconsistency they were experiencing was because of long-held assumptions about how layout worked, based on block layout. Over time, developers have started to get an understanding of formatting contexts. When we switch into a grid or flex formatting context some things behave differently. For example, you know that when you are in flexbox, not all of the alignment methods are available, because flexbox is one-dimensional.
Bundling masonry into grid breaks this clear link between formatting context and availability of things like alignment properties, which are defined in the Box Alignment specification per formatting context.
If we decide to deal with the performance issue outlined previously by making mixed intrinsic and fixed track definitions illegal in masonry, then you will have to remember that a very common pattern for grid layouts doesn't work for masonry.
There are also patterns that would make sense in masonry, for example `grid-template-columns: repeat(auto-fill, max-content)`, because you don't have cross constraints, but need to remain invalid in grid. The following is a list of properties that [we expect to behave differently](https://github.com/w3c/csswg-drafts/issues/9041#issuecomment-2075501616) or have different valid values.
  * `grid-template-areas`: In masonry you can only specify the initial row in the non-masonry direction.
  * `grid-template`: The shorthand would need to account for all differences. 
  * Track sizing values for `grid-template-columns` and `grid-template-rows` due to differences in legal values.
  * `grid-auto-flow` doesn't apply to masonry and `masonry-auto-flow` doesn't apply to grid. Merging them would create problems of things that are invalid due to the layout method you are in.
  * Grid has four placement properties (`grid-column-start` and so on), masonry only has two.
  * Grid can use all six of the `justify-*` and `align-*` properties, but Masonry uses only a subset like flexbox.


There will also be a requirement to specify what happens in all of the new error cases caused by developers using a value that isn't valid in grid-with-masonry or grid-without-masonry. For example, it's valid to use `grid-template-columns: masonry` or `grid-template-rows: masonry` but not both at once. What happens if you do use both at once? These details have to be specified so that all browsers do the same thing.
This all becomes complicated from a specification point of view, now and in the future. We will need to ensure that everything takes into account masonry, and whether it does or does not work in masonry. It's also confusing from the point of view of developers. Why should you need to keep in your head that despite using `display: grid` some things don't work on account of using masonry?
## An alternative proposal
As already mentioned, the Chrome team would like to define masonry outside of the grid specification. This does not mean that it would be limited to a very simple layout method with identical column sizes. All of the demos in the WebKit post would still be possible.
### Classic masonry layout
When most people think of masonry, they think of a layout with multiple, equal sized columns. This would be defined using the following CSS, which needs a line less code than the equivalent [grid bundled version](https://webkit.org/blog/15269/help-us-invent-masonry-layouts-for-css-grid-level-3/#creating-a-classic-masonry-waterfall-layout).
```
.masonry{
display:masonry;
masonry-template-tracks:repeat(auto-fill,minmax(14rem,1fr));
gap:1rem;
}

```

### Use grid type track sizing for different column widths
Other than the previously mentioned issue with mixed intrinsic and fixed track sizing, you could use all of the track sizing that you love from grid. Such as [the example from the WebKit blog post](https://webkit.org/blog/15269/help-us-invent-masonry-layouts-for-css-grid-level-3/#leveraging-grid%e2%80%99s-full-power-to-define-columns), a pattern of repeating narrow and wider columns.
```
.masonry{
display:masonry;
masonry-template-tracks:repeat(auto-fill,minmax(8rem,1fr)minmax(16rem,2fr))minmax(8rem,1fr);
gap:1rem;
}

```

### Additional track sizing for masonry
There are additional track sizing options that we don't allow in grid because of the fact that grid is a two-dimensional layout method. These would be useful in masonry but it would be confusing if they then didn't work in grid.
Auto-filling `max-content` sized tracks.
```
.masonry{
display:masonry;
masonry-template-tracks:repeat(auto-fill,max-content);
gap:1rem;
}

```

Auto-filling `auto` sized tracks, which will create tracks of the same size, auto-sized to accommodate the largest one.
```
.masonry{
display:masonry;
masonry-template-tracks:repeat(auto-fill,auto);
gap:1rem;
}

```

### Allow content to span columns, and place items on the masonry layout
There's no reason not to have content spanning columns in a separate masonry specification. This might use a `masonry-track` property, being a shorthand for `masonry-track-start` and `masonry-track-end` as you only have one dimension to span things when in a masonry layout.
```
.masonry{
display:masonry;
masonry-template-tracks:repeat(auto-fill,auto);
}
.span-2{
masonry-track:span2;/* spans two columns */
}
.placed{
masonry-track:2/5;/* covers tracks 2, 3, and 4 */
}

```

### Sub-masonry or subgrid adopting masonry tracks
This could be supported with a separate masonry specification, again with the proviso that mixed intrinsic and fixed sized tracks are disallowed. Exactly what that looks like will need to be defined. We see no reason that this wouldn't work.
## Conclusion
We would love to get to a point of a specification that can be shipped interoperably. However, we want to do that in a way that works well now and in the future, and that can be relied upon by developers. The only way to deal with the performance issues outlined, would be to make the second issue—that of having parts of grid illegal in masonry—worse. We don't think that's a good solution, especially when it's possible to have all the grid features you want while keeping the things that are different clearly separated.
If you have any feedback, join the discussion in [Issue 9041](https://github.com/w3c/csswg-drafts/issues/9041).
_Thanks to Bramus, Tab Atkins-Bittner, Una Kravets, Ian Kilpatrick, and Chris Harrelson for review of this post and the discussions that informed it._
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-04-30 UTC.

