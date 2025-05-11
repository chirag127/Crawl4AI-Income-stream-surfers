---
url: https://developer.chrome.com/blog/css-text-box-trim?hl=en
title: https://developer.chrome.com/blog/css-text-box-trim?hl=en
date: 2025-05-11T16:54:40.988371
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/css-text-box-trim?hl=en#main-content)
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Nederlands
  * Português – Brasil
  * Tiếng Việt
  * Русский
  * العربيّة
  * ภาษาไทย
  * 中文 – 简体
  * 中文 – 繁體

Sign in


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  CSS text-box-trim 
Stay organized with collections  Save and categorize content based on your preferences. 
Take back space from above and below your text content; achieve optical balance.
Adam Argyle 
[ GitHub ](https://github.com/argyleink) [ Bluesky ](https://bsky.app/profile/nerdy.dev)
Published: Jan 14, 2025 
From Chrome 133, `text-box` lets developers and designers tailor the space above and below text. 
Browser Support
  * 133 
  * 133 
  * 18.2 


[Source](https://developer.mozilla.org/docs/Web/CSS/text-box)
**Longhand:**
```
text-box-trim:trim-start|trim-end|trim-both|none;
text-box-edge:cap|ex|text|leading+alphabetic|text;

```

**Shorthand:**
```
text-box:trim-bothcapalphabetic;

```

This property lets you control the space above and below text, for example `<h1>`, `<button>` and `<p>`. Every font produces a different amount of this block directional space which contributes to the element's size. This chaotic space contribution is not easily measured, and has been impossible to control until now.
The font knows, now CSS knows!
<https://codepen.io/web-dot-dev/pen/xbKjRxL>
The space above and below a font is due to how the web lays out text, called "half-leading". This is expertly covered in a post by [Matthias Ott](https://matthiasott.com/) called [The Thing With Leading In CSS](https://matthiasott.com/notes/the-thing-with-leading-in-css). Essentially, when typesetting was done by hand, pieces of metal lead were used to separate lines of text. The web, inspired by leading, divides that piece of lead in half and distributes a piece above and a piece below the content.
This history is meaningful because, `text-box` gives us names for each half: over and under. Plus, the ability to trim it off.
There is prior art to `text-box` also, you may recall the exciting post from Ethan Wang called [Leading-Trim: The Future Of Digital Typesetting](https://medium.com/microsoft-design/leading-trim-the-future-of-digital-typesetting-d082d84b202), where `leading-trim` (the name `text-box` previously had) was first introduced.
Your entry point into text trimming might be from [Figma and its "vertical trim" controls](https://help.figma.com/hc/en-us/articles/360039956634-Explore-text-properties#h_01H96FW9Z3W7J7Z2HEN8V17BZT) for designers. [This X post demonstrates where this vertical trim option is](https://x.com/figma/status/1640750882613493760) and how it's helpful for buttons.
Regardless of how you got here, this small sounding typography control can make a big difference.
## Feature and syntax overview
Here, in my opinion, are the two most common one-liners you'll need when working with `text-box`:
```
h1{
/* trim both sides to the capital letters */
text-box:trim-bothcapalphabetic;
/* trim both sides to the lowercase letter x */
text-box:trim-bothexalphabetic;
}

```

Trimming both to `cap alphabetic` will be the most common use of this feature. The following demos use this many times. However, the previous example also shows `ex alphabetic` because it is useful for optical balance in its own unique ways.
### Explorer playground
The following demo lets you [explore the syntax](https://codepen.io/web-dot-dev/pen/RNbyooE) and see results using dropdown menus. You can change fonts, change over and under trim values, and follow along with the color coded visuals and labels.
**Things to try:**
  1. Visually inspecting how `text-box-trim` works across single line and multi-line text variants.
  2. Hovering over a variant, seeing the trim values used to achieve that effect.
  3. Changing the font.
  4. Trimming only one side of a text box.
  5. Review the syntax as you play.

<https://codepen.io/web-dot-dev/pen/RNbyooE>
## What can I build with it or what problems does it solve?
There are some much simpler centering and alignment solutions that emerge from this trim capability. You can even get closer to proper leading, where something like `gap` can be used between contents.
<https://codepen.io/web-dot-dev/pen/RNbyoKE>
### Easier centering
For smaller, more inline and content intrinsic components, `padding: 10px` is a reasonable style to specify for an element for equal spacing on all sides. However, the result can confuse people, as it often has extra space on the top and bottom. 
To work around this, developers often explicitly putting less padding on the top and bottom (block) to offset the effects of half leading.
```
button{
padding-block:5px;
padding-inline:10px;
}

```

At this point we're left to try value combinations until things are optically centered. This might look good on one screen and operating system, but not on another.
`text-box` allows us to trim the half leading space from the text, making equal padding values like `10px` useful:
```
button{
text-box:trim-bothcapalphabetic;
padding:10px;
}

```
<https://codepen.io/web-dot-dev/pen/NPKMbgq>
Here are a few `<button>` elements that show how trimming the space with `text-box` makes `padding: 10px` look equal on all sides in a practical interactive element. Notice how the alternative font can produce some wildly different half leading space.
<https://codepen.io/web-dot-dev/pen/mybLOMg>
Here are `<span>` elements, often used to show categories or badges. Another moment where equal sided padding should be the best solution, but until `text-box` we've had to work around it.
<https://codepen.io/web-dot-dev/pen/mybLOMg>
### Easier Alignment
The extra, uncontrollable, half leading space above (`over`) and below (`under`) a text box also makes alignment difficult. The following examples show when half leading can make alignment difficult and how trimming the block sides of a text box can create better alignments.
Here an image is placed next to text. The image will grow to the height that the text needs, but without `text-box`, the image is always a little bit taller. With `text-box`, the image can perfectly align with the text content.
<https://codepen.io/web-dot-dev/pen/yyBjVpg>
Notice the whitespace is above the first formatted line of text and below the last formatted line of text in scenarios with line wrapping.
In the following example, notice how the feature [logically adapts](https://web.dev/learn/css/logical-properties) to a change in [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/writing-mode). Try changing the text, watch how the layout continues to stay aligned.
<https://codepen.io/web-dot-dev/pen/dPbeOJQ>
## Continue study
Want to know more? The following list of links offer various amounts of additional information and use cases.
  * <https://codepen.io/collection/zxQBaL> - a Codepen collection of all the above demo's
  * <https://github.com/jantimon/text-box-trim-examples> - Great research and demos by Jan Nicklas
  * <https://css-tricks.com/two-css-properties-for-trimming-text-box-whitespace/>
  * <https://drafts.csswg.org/css-inline-3/#text-edges>
  * Not to be confused with `size-adjust` or `ascent-override` https://web.dev/articles/css-size-adjust 
  * <https://www.smashingmagazine.com/2012/12/css-baseline-the-good-the-bad-and-the-ugly/>
  * <https://css-tricks.com/two-css-properties-for-trimming-text-box-whitespace/>
  * applied to many HTML elements <https://codepen.io/nileshprajapati/pen/RweKdmw>
  * Safari's blog post <https://webkit.org/blog/16301/webkit-features-in-safari-18-2/>
  * <https://piccalil.li/blog/why-im-excited-about-text-box-trim-as-a-designer/>


Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-01-14 UTC.

