---
url: https://developer.chrome.com/blog/better-text-rendering-in-chromium-based-browsers-on-windows?hl=en
title: https://developer.chrome.com/blog/better-text-rendering-in-chromium-based-browsers-on-windows?hl=en
date: 2025-05-11T16:54:03.718660
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/better-text-rendering-in-chromium-based-browsers-on-windows?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/better-text-rendering-in-chromium-based-browsers-on-windows?hl=es-419)

Sign in
Chrome is back at Google I/O on May 20-21! [Explore the agenda now](https://io.google/2025/explore/?utm_source=devsite&utm_medium=embedded_marketing&utm_campaign=dcc&utm_content=)
  * [ Chrome for Developers ](https://developer.chrome.com/)


#  Better text rendering in Chromium-based browsers on Windows 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Kurt Catti-Schmidt 
Patrick Brosset 
[ Homepage ](https://patrickbrosset.com/)
Published: February 12, 2025 
The job of a web rendering engine is vast, and much of this work, such as styling, media, or layout, is driven by standards. These standards ensure that independent engines can be interoperable, which has allowed the web to flourish. But some finer details, such as how text is rendered at the pixel level, are often left to interpretation by the standards bodies, and typically end up relying on the operating systems that browsers run on.
In 2020, Microsoft Edge had a rare opportunity—a complete replacement of its underlying rendering engine. [Edge transitioned to Chromium](https://github.com/MicrosoftEdge/MSEdge/blob/master/README.md), away from a Windows-only platform where it used Windows APIs directly, and became a true cross-platform web renderer. Before the switch to Chromium, Edge relied entirely on a Windows API called [DirectWrite](https://learn.microsoft.com/windows/win32/directwrite/direct-write-portal) for text rendering. However, Chromium relies on [Skia](https://skia.org/), a powerful and flexible cross-platform graphics engine, which abstracts many of the operating system-specific code from its API.
During Edge's transition to Chromium, the Edge team had the opportunity to gather feedback from its users about the Chromium rendering engine. One piece of feedback was significant—many Edge users shared that text appeared "washed out" and that it didn't look consistent with text in other parts of Windows.
The team took this feedback seriously and did some investigation. While Skia uses DirectWrite on Windows for certain functionality such as font lookup, the final text rasterization is actually handled directly by Skia. And one major factor in the "washed out" feedback from users is the internal contrast and gamma settings for text rendering.
Two main differences in text contrast and gamma values were uncovered between Edge's Chromium-based engine and its prior engine. First, Skia does not pick up text contrast and gamma values from the [Windows ClearType Tuner](https://learn.microsoft.com/en-us/typography/cleartype/). Secondly, it uses different default values for text contrast and gamma than those used by Edge's DirectWrite-based text stack.
The Edge team added support for respecting the ClearType Tuner values in Chromium directly, last year. This gave Chromium-based browser users the ability to control text contrast and gamma settings on Windows. While this was a significant step in the right direction, most users tend to not adjust their system-wide text contrast and gamma settings. So the next phase in this journey was to seriously consider adjusting the default text contrast and gamma settings for both web and browser UI text content.
Changing what text looks like on the web is a large undertaking. The web has always been text heavy, and a high-quality text engine is necessary. It was evident that the text contrast value needed to increase, but data was needed to determine how much to adjust it.
The Edge team began experimenting with various text contrast values back in 2021. After a lot of user research, members of both Edge and Chromium determined that a contrast value of 1.0 closely matched the text rendering of pre-Chromium Edge and looked consistent compared to other native Windows applications.
On the Edge team, we believed our research and experiments could be beneficial to the overall Chromium community on Windows, so we shared our findings with the Chrome team at Google, who confirmed them with their own experiments. We then proceeded to enable the new contrast value by default for Windows builds, starting with Chrome 132.
Today, all users of Chromium-based browsers on Windows can benefit from these past years of shared research, experimentation, and implementation.
Special thanks to Ian Prest, Daniel Libby, and Alison Maher at Microsoft, as well as Dominik Röttsches, David Yeung, Ben Wagner, and Brian Osman at Google for their contributions to this project!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-02-12 UTC.

