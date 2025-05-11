---
url: https://developer.chrome.com/blog/css-shape?hl=en
title: https://developer.chrome.com/blog/css-shape?hl=en
date: 2025-05-11T16:54:40.982843
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/css-shape?hl=en#main-content)


  * On this page
  * [Create a flag shape](https://developer.chrome.com/blog/css-shape?hl=en#create_a_flag_shape)
    * [Create the flag with clip-path: path()](https://developer.chrome.com/blog/css-shape?hl=en#create_the_flag_with_clip-path_path)
    * [Create the flag with shape()](https://developer.chrome.com/blog/css-shape?hl=en#create_the_flag_with_shape)
    * [Make it responsive](https://developer.chrome.com/blog/css-shape?hl=en#make_it_responsive)
    * [Add custom properties and animations](https://developer.chrome.com/blog/css-shape?hl=en#add_custom_properties_and_animations)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  Use shape() for responsive clipping 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Create a flag shape](https://developer.chrome.com/blog/css-shape?hl=en#create_a_flag_shape)
    * [Create the flag with clip-path: path()](https://developer.chrome.com/blog/css-shape?hl=en#create_the_flag_with_clip-path_path)
    * [Create the flag with shape()](https://developer.chrome.com/blog/css-shape?hl=en#create_the_flag_with_shape)
    * [Make it responsive](https://developer.chrome.com/blog/css-shape?hl=en#make_it_responsive)
    * [Add custom properties and animations](https://developer.chrome.com/blog/css-shape?hl=en#add_custom_properties_and_animations)


Noam Rosenthal 
[ GitHub ](https://github.com/noamr) [ Mastodon ](https://indieweb.social/@nomster)
Published: April 8, 2025 
The `clip-path` property lets you change the shape of an element by clipping to a circle, polygon, or even an SVG path. However, before Chrome 135 and Safari 18.4, you had to choose between responsive polygons, and more complex shapes that are not responsive using SVG paths. With the new `shape()` function, a `clip-path` can clip the element to a non-polygon shape which is also responsive.
Browser Support
  * 135 
  * 135 
  * 18.4 


[Source](https://developer.mozilla.org/docs/Web/CSS/basic-shape/shape)
## Create a flag shape
As an example, compare creating a flag shape with `clip-path: path()` and `clip-path: shape()`.
A flag shape is not exactly a polygon, as its top and bottom borders are cubic Bézier curves rather than straight lines or rounded corners.
### Create the flag with `clip-path: path()`
A shape like this flag can be represented using an SVG path:
```
.flag{
clip-path:path(
"M 0 20 \
   C 25 0 75 40 100 20 \
   V 80 \
   C 75 100 25 60 0 80 \
   z");
}

```

To break this down, an SVG path is a series of path commands:
  1. Move to 0, 20.
  2. Curve to 100, 20, using control points (25,0 and 75, 40).
  3. Vertical line to 80.
  4. Curve to 0, 80, using control points (75,100 and 25,50).
  5. Close the path (line to 0,20).


This draws a flag shape, but all the units are in pixels. SVG can scale those pixels to a view-box, but in a way that would always look like a geometric scale of the whole shape.
For example, if you wanted the whole rectangle to scale, but maintain the height and width of the curves 20px, SVG wouldn't be up to the task.
### Create the flag with `shape()`
Compare the same result using `shape()`. The shape function accepts a series of commands, similar to the SVG path commands. However, these commands accept CSS lengths and percentages, in any CSS unit.
The following CSS converts the flag a `shape()` with percentage units:
```
.flag{
clip-path:shape(from0%20%,
curveto100%20%with25%0%/75%40%,
vlineto80%,
curveto0%80%with75%100%/25%60%,
close
);
}

```

### Make it responsive
With the full range of CSS lengths available, you can pick which ones to use for each coordinate.
For example, to make the entire size of the flag scale by the element's size, but keep the height of the curve constant, you can do the following:
```
.flag{
clip-path:shape(from0%20px,
curveto100%20pxwith25%0%/75%40px,
vlinetocalc(100%-20px),
curveto0%calc(100%-20px)
with75%100%/25%calc(100%-40px),
close
);
}

```

### Add custom properties and animations
With the shape now defined in CSS, you can also use custom properties, to make it easy to manipulate the height:
```
.flag{
--wave-height:40px;
clip-path:shape(
from0pxvar(--wave-height),
curveto100%var(--wave-height)
with25%0px/75%calc(var(--wave-height)*2),
vlinetocalc(100%-var(--wave-height)),
curveto0calc(100%-var(--wave-height))
with75%100%/25%calc(100%-var(--wave-height)*2),
close
)
}

```

You can even animate the CSS property using the `@property` descriptor, and clamp it so that it doesn't overreach:
```
@property--animated-wave-height{
syntax:"<length>";
inherits:false;
initial-value:40px;
}
@keyframescurve{
from{--animated-wave-height:0px;}
to{--animated-wave-height:180px;}
}
.flag{
width:600px;
height:400px;
background:green;
animation:curve1sinfinitealternate;
--wave-height:calc(min(var(--animated-wave-height,40px),40%));
clip-path:shape(
from0pxvar(--wave-height),
curveto100%var(--wave-height)
with25%0px/75%calc(var(--wave-height)*2),
vlinetocalc(100%-var(--wave-height)),
curveto0calc(100%-var(--wave-height))
with75%100%/25%calc(100%-var(--wave-height)*2),
close
)
}

```

## Try the demo
In Chrome 135 or Safari 18.4, you can see the animating flag shape created using `clip-path: shape()` in [this CodePen demo](https://codepen.io/web-dot-dev/pen/YPzgNrL).
## Summary
`clip-path: shape()` lets you clip your element using arbitrary and responsive shapes, previously only possible using techniques like conic gradients or JavaScript-constructed SVG.
Check [the specification](https://drafts.csswg.org/css-shapes-2/#shape-function) for the full syntax.
At the moment, it only works for `clip-path`. In the future, we envision using this kind of shape for [setting the shape of the element's border](https://drafts.csswg.org/css-borders-4/#border-shape-func), which would unlock even more non-rectangular ways of expression.
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-04-08 UTC.

