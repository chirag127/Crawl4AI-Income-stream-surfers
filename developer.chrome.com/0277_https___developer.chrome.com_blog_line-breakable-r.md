---
url: https://developer.chrome.com/blog/line-breakable-ruby?hl=en
title: https://developer.chrome.com/blog/line-breakable-ruby?hl=en
date: 2025-05-11T16:56:43.177885
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/line-breakable-ruby?hl=en#main-content)
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


#  Line-breakable <ruby> and CSS ruby-align property 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Mariko Kosaka 
The HTML [`<ruby>`](https://developer.mozilla.org/docs/Web/HTML/Element/ruby) element is a powerful tool for enhancing text presentation, especially for East Asian languages. This element lets you display phonetic annotations or other supplemental information above or beside base text. From Chrome 128, ruby annotation will be line-breakable, and you can style ruby text with `ruby-align` CSS property.
A `<ruby>` element consists of two main parts, _ruby base_ which is the main text and _ruby text_ which is the annotation text, marked up with the [`<rt>`](https://developer.mozilla.org/docs/Web/HTML/Element/rt) element. Ruby text can be displayed over or under the ruby base, as shown in the following examples.
```
<ruby>
 絵文字
 <rt>emoji</rt>
</ruby>

```
English pronunciation as an annotation over Japanese base text. ```

<ruby style="ruby-position: under;">
 강남대로
 <rt>江南大路</rt>
</ruby>

```
Chinese annotation added below Korean hangul.
### Why is it called ruby?
When books were typeset using movable types, the sizes of these movable types were defined in point-size names such as Perl, and Diamond. Ruby was used in the British system to refer to 5.5 point size. Japanese printers used a size similar to Ruby (5.5 point) for annotation text and so started to refer to the annotation text itself as Ruby (or Rubi phonetically) in prints. When the annotation text was included in HTML, the element was defined as `<ruby>`. Pica (`pc`) is another historical point-size name used in CSS as a font size unit.
## Line-breakable ruby
Previously if a ruby-base or a ruby-text was longer than a whole line, they were wrapped individually creating layout challenges. To overcome this, web developers often mark up a piece of text using multiple ruby tags. With line-breakable ruby, you can skip creating such markup.
In the following example, pinyin (romanization of Chinese) is added as one set of ruby annotations on classical Chinese poetry. Current rendering results wrap within the ruby annotation text area.
Rendering result before Chrome 128 with long ruby annotation text.
Rendering from Chrome 128 with line-breakable ruby places wrapped ruby annotation text over wrapped base text achieving ideal text rendering.
Rendering result from Chrome 128 with long ruby annotation text.
In another example from Japanese literature, the line break happens before the long ruby element, creating a blank space in the first line. 
Rendering result before Chrome 128 with long ruby text.
With line-breakable ruby, line break is placed in the middle of long ruby element achieving ideal layout.
Rendering result from Chrome 128 with long ruby text.
This feature won't break short ruby text that has less than or equal to four base characters and less than or equal to eight annotation characters.
When a `<ruby>` element is nested inside of another `<ruby>` element, the inner `<ruby>` element won't line break.
Since this changes the behavior of current web pages using long ruby text, if you need to disable this line-break behavior, applying `white-space:nowrap` disables line-breaking inside the target element as usual.
## The `ruby-align` CSS property
Browser Support
  * 128 
  * 128 
  * 38 
  * 18.2 


[Source](https://developer.mozilla.org/docs/Web/CSS/ruby-align)
The new CSS property [`ruby-align`](https://developer.mozilla.org/docs/Web/CSS/ruby-align) is also available from Chrome 128. The property accepts one of the keyword values`space-around`, `space-between`, `start`, and `center`, and controls the alignment of ruby base text and ruby annotation text.
Image showing use-case for ruby-align property.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-07-26 UTC.

