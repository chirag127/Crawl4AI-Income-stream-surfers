---
url: https://developer.chrome.com/docs/chromedriver
title: https://developer.chrome.com/docs/chromedriver
date: 2025-05-11T16:51:26.897935
depth: 1
---

[ Skip to main content ](https://developer.chrome.com/docs/chromedriver#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/chromedriver?hl=es-419)




  * On this page
  * [Latest ChromeDriver binaries](https://developer.chrome.com/docs/chromedriver#latest_chromedriver_binaries)




Was this helpful?
#  What is ChromeDriver? 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Latest ChromeDriver binaries](https://developer.chrome.com/docs/chromedriver#latest_chromedriver_binaries)


ChromeDriver is a standalone server that implements the W3C [WebDriver](https://w3c.github.io/webdriver/) and [WebDriver BiDi](https://w3c.github.io/webdriver-bidi/) standards. WebDriver is an open source tool built for automated testing of web apps across many browsers. Its interface allows for control and introspection of user agents locally or remotely using capabilities.
Capabilities are a language-neutral set of key-value pairs used to define the desired features and behavior of a WebDriver session. Capabilities are typically passed as an argument when creating a WebDriver instance, and can be used to specify browser settings, such as the browser name, version, and page loading strategy.
ChromeDriver extends Webdriver by adding Chromium-specific capabilities. It uses the `ChromeOptions` object to pass capabilities to ChromeDriver from the WebDriver API. Some Chromium-specific capabilities include the ability to install extensions, change window types, and pass command line arguments on startup. 
ChromeDriver is available for Chrome on Android and Chrome on Desktop (Mac, Linux, Windows and ChromeOS).
Review the [current implementation status of the WebDriver standard](https://chromium.googlesource.com/chromium/src/+/master/docs/chromedriver_status.md).
## Latest ChromeDriver binaries
Starting with M115 the latest Chrome and ChromeDriver releases per release channel (Stable, Beta, Dev, Canary) are available at the [Chrome for Testing availability dashboard](https://googlechromelabs.github.io/chrome-for-testing/).
To download the latest ChromeDriver binary, you can use the [JSON endpoints](https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json).
Older releases can be found in [Downloads](https://developer.chrome.com/docs/chromedriver/downloads).
## Documentation
  * [Getting started with ChromeDriver on Desktop](https://developer.chrome.com/docs/chromedriver/get-started) (Windows, Mac, Linux) 
    * [ChromeDriver with Android](https://developer.chrome.com/docs/chromedriver/get-started/android)
    * [ChromeDriver with ChromeOS](https://developer.chrome.com/docs/chromedriver/get-started/chromeos)
  * [ChromeOptions](https://developer.chrome.com/docs/chromedriver/capabilities), the capabilities of ChromeDriver
  * [Mobile emulation](https://developer.chrome.com/docs/chromedriver/mobile-emulation)
  * [Security Considerations](https://developer.chrome.com/docs/chromedriver/security-considerations), with recommendations on keeping ChromeDriver safe
  * [Chrome Extension installation](https://developer.chrome.com/docs/chromedriver/extensions)
  * [Verbose logging](https://developer.chrome.com/docs/chromedriver/logging) and [performance data logging](https://developer.chrome.com/docs/chromedriver/logging/performance-log)


## Troubleshoot
  * [Chrome crashes immediately or doesn't start](https://developer.chrome.com/docs/chromedriver/help/chrome-doesnt-start)
  * [ChromeDriver crashes](https://developer.chrome.com/docs/chromedriver/help/chromedriver-crashes)
  * [Operation Not Supported when using remote debugging](https://developer.chrome.com/docs/chromedriver/help/operation-not-supported-when-using-remote-debugging)


## Get involved
  * The [chromedriver-users mailing list](https://groups.google.com/d/forum/chromedriver-users) for questions, help with troubleshooting, and general discussion.
  * [StackOverflow ChromeDriver posts](http://stackoverflow.com/questions/tagged/selenium-chromedriver)
  * [Guide to our issue tracker and reporting bugs](https://developer.chrome.com/docs/chromedriver/help)
  * [Contribute to ChromeDriver](https://developer.chrome.com/docs/chromedriver/contributing)
  * [Contribute to ChromeDriver BiDi](https://github.com/GoogleChromeLabs/chromium-bidi#contributing)


Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-03-04 UTC.

