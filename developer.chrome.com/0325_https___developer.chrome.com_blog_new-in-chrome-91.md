---
url: https://developer.chrome.com/blog/new-in-chrome-91?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-91?hl=en
date: 2025-05-11T16:57:34.983273
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-91?hl=en#main-content)
Sign in


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  New in Chrome 91 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Pete LePage 
[ GitHub ](https://github.com/petele) [ Glitch ](https://glitch.com/@petele) [ Mastodon ](https://techhub.social/@petele) [ Homepage ](https://petelepage.com/)
Here's what you need to know:
  * Web apps that interact with files, can now [suggest file names and directories](https://developer.chrome.com/blog/new-in-chrome-91?hl=en#filenames) when using the File System Access API.
  * You can [read files from the clipboard](https://developer.chrome.com/blog/new-in-chrome-91?hl=en#clipboard).
  * If your [site has more than one domain](https://developer.chrome.com/credentials), and they share the same account management backend, you can tell Chrome they're the same, allowing the password manager to suggest the right credentials.
  * All the videos from I/O are available on [Chrome Developers YouTube channel](https://developer.chrome.com/io-playlist)!
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-91?hl=en#more).


I'm [Pete LePage](https://petelepage.com/), working, and shooting from home, let's dive in and see what's new for developers in Chrome 91!
## Suggested names for File System Access API
One of my favorite APIs to come out of the Fugu project this year is the File System Access APIs. Once the user has granted permission, apps can interact with files on the users local device, in the same way other installed apps do, allowing you to create a more natural user experience.
Starting in Chrome 91, you can now suggest the name and location of a file or directory to interact with. To do so, pass a `suggestedName` property as part of the `showSaveFilePicker` options.
```
constfileHandle=awaitself.showSaveFilePicker({
suggestedName:'Untitled Text.txt',
types:[{
description:'Text documents',
accept:{
'text/plain':['.txt'],
},
}],
});

```

The same goes for the default starting directory. For example, a text editor probably wants to start the file save or file open dialog in the `documents` folder. Whereas an image editor probably wants to start in the `pictures` folder. You can suggest a default start directory by passing a `startIn` property.
```
constfileHandle=awaitself.showOpenFilePicker({
startIn:'documents'
});

```

Check out Tom's [File System Access](https://web.dev/file-system-access/) post for complete details.
## Reading files from the clipboard
There's one other cool new API for interacting with files that lands in Chrome 91. On desktop, web apps can now read files from the clipboard. (Reading files from the clipboard has been available in Safari since 2018.)
Of course, you don't get unrestricted access to the clipboard, so you'll need to set-up a `paste` event listener. Then, in the event handler, you can access the content of each file on the clipboard.
```
window.addEventListener('paste',onPaste);
asyncfunctiononPaste(e){
constfile=e.clipboardData.files[0];
constcontents=awaitfile.text();
...
}

```

## Share credentials on affiliated sites
If your site has multiple domains, and they share the same account management backend, you can now associate your sites with one another, allowing users to save credentials once, and have the Chrome password manager suggest them to any of your affiliated sites.
This is ideal when your site is served from different top level domains, like `google.com`, and `google.ca`. Or maybe you've got multiple domains names.
To associate your websites, you'll need to create an `assetlinks.json` file that defines the relationship between the domains. In the example below, I'm telling the browser that both the `.com` and `.co.uk` domains are related and can share the credentials.
```
[{
"relation":["delegate_permission/common.get_login_creds"],
"target":{
"namespace":"web",
"site":"https://www.example.com"
}
},
{
"relation":["delegate_permission/common.get_login_creds"],
"target":{
"namespace":"web",
"site":"https://www.example.co.uk"
}
}]

```

Then, host the `assetlinks.json` file in the `.well-known` folder for each domain.
This functionality will start to roll out gradually in Chrome 91, and may not be available on day one, so check out [Enable Chrome to share login credentials across affiliated sites](https://developer.chrome.com/blog/site-affiliation/) for the latest details.
## And more!
Of course there's plenty more.
All the [videos from I/O 2021](https://www.youtube.com/playlist?list=PLNYkxOF6rcIAK3hg7C9WVBaGgWZeQCD12) are online now, there's some great content there, so check it out!
[Web Transport](https://web.dev/webtransport/)-previously called Quic Transport has undergone a number of changes and is starting a new origin trial.
Web Assembly SIMD has finished its origin trial and is available to all users.
The refreshed form elements have finally landed on Android, improving the user experience.
And the `<link>` element's `media` attribute will be honored for `link rel="icon"`, meaning you can define different icons based on media queries. For example a different icons for dark and light modes.
```
<link
 rel="icon"
 media="(prefers-color-scheme: dark)"
 href="/icons/dark.png">
<link
 rel="icon"
 media="(prefers-color-scheme: light)"
 href="/icons/light.png">

```

## Further reading
This covers only some of the key highlights. Check the links below for additional changes in Chrome 91.
  * [What's new in Chrome DevTools (91)](https://developer.chrome.com/blog/new-in-devtools-91)
  * [Chrome 91 deprecations & removals](https://developer.chrome.com/blog/deps-rems-91)
  * [ChromeStatus.com updates for Chrome 91](https://www.chromestatus.com/features#milestone%3D91)
  * [What's new in JavaScript in Chrome 91](https://v8.dev/blog/v8-release-91)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/90.0.4430.71..91.0.4472.78)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
I'm Pete LePage, and as soon as Chrome 92 is released, I'll be right here to tell you what's new in Chrome!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2021-05-26 UTC.

