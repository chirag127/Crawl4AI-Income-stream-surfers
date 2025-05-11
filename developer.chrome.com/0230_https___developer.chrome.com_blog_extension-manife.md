---
url: https://developer.chrome.com/blog/extension-manifest-converter?hl=en
title: https://developer.chrome.com/blog/extension-manifest-converter?hl=en
date: 2025-05-11T16:55:43.052655
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/extension-manifest-converter?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/extension-manifest-converter?hl=es-419)




  * [ Chrome for Developers ](https://developer.chrome.com/)


#  Extension Manifest Converter 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Easily convert an entire directory, extension zip file, or manifest.json file.
Solomon Kinard 
[ GitHub ](https://github.com/solomonkinard) [ Glitch ](https://glitch.com/@solomonkinard) [ Homepage ](https://kinard.com)
Simeon Vincent 
[ GitHub ](https://github.com/dotproto) [ Glitch ](https://glitch.com/@dotproto)
Hi everyone. My name is Solomon and I'm a software engineer on Chrome's extensions team.
As we continue to build out the latest version of [Chrome's extensions platform](https://developer.chrome.com/docs/extensions/mv3/intro/mv3-overview/), I found myself needing to convert Manifest V2 extensions to Manifest V3 for testing purposes. To make this process a little easier I created a tool called [Extension Manifest Converter](https://github.com/GoogleChromeLabs/extension-manifest-converter) (EMC).
EMC is a Python 3 command line tool that automates several parts of converting an extension between manifest formats. Users can quickly convert an extension directory, zip file, or manifest.json file with a single command.
```
python3emc.py<extension_path>

```

This tool focuses on automating the mechanical parts of converting an extension. For example, it will replace `chrome.browserAction` with `chrome.action` in JavaScript, but it cannot handle abstract tasks like updating background logic to fully adopt service workers. See the project's [README](https://github.com/GoogleChromeLabs/extension-manifest-converter#readme) for more details.
We've found this tool useful on our team and wanted to open source it in the hope that you might too. Keep in mind, though, that as a personal side project we cannot offer support or maintain it indefinitely.
If you encounter any issues with the project, please [open an issue](https://github.com/GoogleChromeLabs/extension-manifest-converter/issues) on the [project's repo](https://github.com/GoogleChromeLabs/extension-manifest-converter).
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2021-04-28 UTC.

