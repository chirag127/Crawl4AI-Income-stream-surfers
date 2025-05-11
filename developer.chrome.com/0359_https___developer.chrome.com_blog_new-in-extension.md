---
url: https://developer.chrome.com/blog/new-in-extensions-1?hl=en
title: https://developer.chrome.com/blog/new-in-extensions-1?hl=en
date: 2025-05-11T17:54:04.203201
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-extensions-1?hl=en#main-content)


  * On this page


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  Web Accessible Resources for Manifest V3 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


Solomon Kinard 
[ GitHub ](https://github.com/solomonkinard) [ Glitch ](https://glitch.com/@solomonkinard) [ Homepage ](https://kinard.com)
Simeon Vincent 
[ GitHub ](https://github.com/dotproto) [ Glitch ](https://glitch.com/@dotproto)
New and improved Web Accessible Resources for Manifest V3!
New and improved Web Accessible Resources for Manifest V3!
## Summary
Web Accessible Resources for Manifest V3 is here! Now `manifest.json` supports permission definitions. Developers can restrict resources based on the requesting site origin or extension id.
## Examples
Wildcard site:
```
{
"web_accessible_resources":[
{
"resources":["a.png"],
"matches":["*://*/*"]
}
],
...
}

```

Site specific:
```
{
"web_accessible_resources":[
{
"resources":["a.png"],
"matches":["https://example.com/*"]
}
],
...
}

```

Extension specific:
```
{
"web_accessible_resources":[
{
"resources":["a.png"],
"extension_ids":["abcdefghijlkmnopabcdefghijlkmnop"]
}
],
...
}

```

Extension and site specific:
```
{
"web_accessible_resources":[
{
"resources":["a.png"],
"matches":["https://example.com/*"],
"extension_ids":["abcdefghijlkmnopabcdefghijlkmnop"]
}
],
...
}

```

## Links


## Launched
m89
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2021-04-20 UTC.

