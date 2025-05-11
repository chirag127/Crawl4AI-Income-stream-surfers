---
url: https://developer.chrome.com/docs/webstore/prepare
title: https://developer.chrome.com/docs/webstore/prepare
date: 2025-05-11T16:52:41.881646
depth: 1
---

[ Skip to main content ](https://developer.chrome.com/docs/webstore/prepare#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/webstore/prepare?hl=es-419)




  * On this page
  * [Test your extension in production](https://developer.chrome.com/docs/webstore/prepare#test)
  * [Review your manifest](https://developer.chrome.com/docs/webstore/prepare#manifest)
  * [Zip your extension files](https://developer.chrome.com/docs/webstore/prepare#zip)
  * [Additional store listing content](https://developer.chrome.com/docs/webstore/prepare#listing)




Was this helpful?
#  Prepare your extension 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Test your extension in production](https://developer.chrome.com/docs/webstore/prepare#test)
  * [Review your manifest](https://developer.chrome.com/docs/webstore/prepare#manifest)
  * [Zip your extension files](https://developer.chrome.com/docs/webstore/prepare#zip)
  * [Additional store listing content](https://developer.chrome.com/docs/webstore/prepare#listing)


After [registering](https://developer.chrome.com/docs/webstore/register) and [setting up](https://developer.chrome.com/docs/webstore/set-up-account) your developer account, you can submit your extension to the Chrome Web Store. But before you do so, there are a few ways to prepare your extension and other content before submitting your item.
## Test your extension in production
[Load your extension locally](https://developer.chrome.com/docs/extensions/mv3/getstarted/development-basics#load-unpacked) and make sure all your features work as intended before uploading your extension to the Chrome Web Store. 
## Review your manifest
After uploading your item, you won't be able to edit the metadata of your manifest in the developer dashboard. This means, that if you notice a typo, you will have to edit the manifest, increase the version number, and zip the files all over again.
Make sure you check and include the following fields:  

`"name"`
    This [name](https://developer.chrome.com/docs/extensions/mv3/manifest/name) appears in the Chrome Web Store and the Chrome browser. 

`"version"`
    The [version](https://developer.chrome.com/docs/extensions/mv3/manifest/version) number of this extension release. 

`"icons"`
    An array specifying the [icons](https://developer.chrome.com/docs/extensions/mv3/manifest/icons) of your extension. 

`"description"`
    A string of no more than 132 characters that [describes](https://developer.chrome.com/docs/extensions/mv3/manifest/description) your extension.
Set the initial [version number](https://developer.chrome.com/docs/extensions/mv3/manifest/version) in the manifest to a low value, such as 0.0.0.1. That way, you have room to increase the version number when you [upload new versions](https://developer.chrome.com/docs/webstore/publish#upload-your-item) of your item. Each new version that you upload to the Chrome Web Store must have a larger version number than the previous version.
## Zip your extension files
To upload your extension, you need to submit a ZIP file that contains all extension files. Make sure you place the manifest file in the **root directory** , not in a folder.
## Additional store listing content
Besides the metadata in your manifest, you will also need to provide content, images, and URLs that will help your users understand what value your extension offers. See [Creating a great listing page](https://developer.chrome.com/docs/webstore/best_listing) for details on creating a high-quality listing page that clearly communicates what your item will offer, using the item description, images, and other listing metadata. 
## Next steps
  * [Publish your extension](https://developer.chrome.com/docs/webstore/publish).


Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2023-10-16 UTC.

