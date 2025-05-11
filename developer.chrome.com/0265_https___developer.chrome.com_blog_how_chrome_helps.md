---
url: https://developer.chrome.com/blog/how_chrome_helps_users_install_the_apps_they_value?hl=en
title: https://developer.chrome.com/blog/how_chrome_helps_users_install_the_apps_they_value?hl=en
date: 2025-05-11T16:56:25.893537
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/how_chrome_helps_users_install_the_apps_they_value?hl=en#main-content)
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


#  How Chrome helps users install the apps they value 
Stay organized with collections  Save and categorize content based on your preferences. 
Thomas Steiner 
[ GitHub ](https://github.com/tomayac) [ Glitch ](https://glitch.com/@tomayac) [ LinkedIn ](https://www.linkedin.com/in/thomassteinerlinkedin) [ Mastodon ](https://toot.cafe/@tomayac) [ Bluesky ](https://bsky.app/profile/tomayac.com) [ Homepage ](https://blog.tomayac.com/)
Dibyajyoti Pal 
[ LinkedIn ](https://www.linkedin.com/in/dpal1996)
Vincent Scheib 
[ LinkedIn ](https://www.linkedin.com/in/vincentscheib)
Dan Murphy 
[ LinkedIn ](https://www.linkedin.com/in/daniel-murphy-09961314)
Chrome's internal user research shows that many people value installing web apps. There are many benefits such as:
  * Having a chat app launch from the operating system taskbar or dock.
  * Playing music from a dedicated top level window that's visible when switching apps.
  * Decluttering the browser UX for an immersive video call.
  * Opening a web app directly from an associated file the operating system file explorer.


There are multiple ways Chrome and web developers can help, including a new machine learning promotion feature. This post gives an overview of the ways users can install your app.
## "Crafted" apps meeting the installability criteria
Apps that meet Chrome's [installability criteria](https://web.dev/articles/install-criteria) automatically show an install icon in the address bar of the Chrome desktop browser (highlighted in the following screenshot). A user can click to install the app.
An alternative way to install is going using the **More** > **Save and Share** > **Install $appName**.
On mobile, users can install the app using the displayed install prompt, or using **More** > **Add to Home screen** > **Install app**.
These installs are called "crafted" as the developer has opted into this UX by fulfilling the installability criteria.
### Customized install experience
Developers can take it one step further and offer a [customized install experience](https://web.dev/articles/customize-install). This is the approach apps like [Squoosh](https://squoosh.app/) and [SVGcode](https://svgco.de/) have taken. See the highlighted **Install** buttons in the following examples. By [providing screenshots](https://web.dev/patterns/web-apps/richer-install-ui), developers can create an even richer install experience.
## "Manual" installation of any app
Research at Google has shown that users also want to install _any_ web experiences, even if they don't meet the install criteria or offer a customized install flow. An example is [Wordle](https://www.nytimes.com/games/wordle/index.html). At the time of writing, its web app manifest is missing the `icons` member and the `start_url`.
```
{
"name":"Wordle",
"short_name":"Wordle",
"theme_color":"#FFFFFF",
"background_color":"#FFFFFF",
"display":"minimal-ui"
}

```

For such cases, Chrome offers a manual way to [install a page as a "manual" app](https://support.google.com/chrome/answer/9658361?sjid=5259992915796232748-EU), highlighted in the following screenshot for desktop. At the top right of the browser window, select **More** > **Save and share** > **Install Page as App**. In the install prompt, you can change the app name to your liking.
On mobile, tap **More** > **Add to home screen** > **Install app**.
While this works, it's not necessarily discoverable in practice. This is why the Chrome team has invested in an approach driven by **machine learning (ML)**.
## Install prompt based on machine learning
On Android, the team uses [Chrome segmentation](https://chromium.googlesource.com/chromium/src/+/refs/heads/main/components/segmentation_platform/README.md) to predict whether a user will want to install a given page based on a collection of signals, including site health characteristics (for example, the existence of a valid manifest) and user site visitation data (for example, the total count of site visits in the past 14 days). This data is collected and used to train an ML model to trigger an install dialog if there's a high probability that the user will install it. If the site meets the install criteria, then this shows the normal installation dialog, while other pages will get the manual installation dialog.
Initial results show that users are receptive to ML-triggered install prompts, and the team plans on using the experiences gained so far to further fine-tune the model to help users install the apps they want.
## Create a shortcut on desktop and mobile
From Chrome 128, **More** > **Save and Share** > **Create Shortcut** creates a bookmark on the user's desktop or homescreen. This launches a specific page in a new tab, matching Android's behavior, where you create a shortcut using **More** > **Add to Home screen** > **Create shortcut**.
The previous behavior of this menu item on desktop has now moved to the **Install Page as App** option, which creates a "manual" app as described before.
## Conclusions
Users love coming back to their apps. Sometimes in a browser tab, sometimes as a standalone experience. Chrome helps users get there by:
  * Allowing developers to craft rich installation experiences.
  * Enabling users to install apps, even if their developers didn't have installability planned.
  * Letting users create shortcuts to pages they want to revisit.
  * Proactively suggesting apps to install based on machine learning with high confidence installation is what the user wants.


And now back to Wordle, erm, work…
Wordle 1,110 3/6
⬛⬛⬛🟨⬛
⬛🟨⬛🟨🟩
🟩🟩🟩🟩🟩
## Acknowledgements
This document was reviewed by Finnur Breki Thorarinsson, Ella Ge, and [Rachel Andrew](https://rachelandrew.co.uk/).
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-07-23 UTC.

