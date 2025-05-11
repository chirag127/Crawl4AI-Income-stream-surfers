---
url: https://developer.chrome.com/blog/longer-esw-lifetimes?hl=en
title: https://developer.chrome.com/blog/longer-esw-lifetimes?hl=en
date: 2025-05-11T16:56:43.192629
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/longer-esw-lifetimes?hl=en#main-content)
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


#  Longer extension service worker lifetimes 
Stay organized with collections  Save and categorize content based on your preferences. 
Extension service workers can now stay alive as long as they're receiving events. This increases the reliability of extension services workers, but has a pitfall you should avoid.
Joe Medley 
[ GitHub ](https://github.com/jpmedley)
Starting in Chrome 110 (in beta as of February 7, 2023), extension service workers stay alive as long as they're receiving events. This corrects a timing problem in the previous implementation of extension service workers. It was possible for timeouts to occur when new events were in the event queue and for the timeouts to truncate asynchronous work. This improvement removes the hard five-minute maximum lifetime for extension service workers. 
This article describes how these behaviors have changed.
## Background
Extension service workers mostly behave like web service workers, but in addition to [service worker events](https://developer.mozilla.org/docs/Web/API/ServiceWorkerGlobalScope#events), extension service workers can also listen to extension events. While normal service worker events extend the service worker's lifetime, before the release of 110 only a few extension platform events kept an extension service worker alive.
Normally, Chromium terminates a service worker after one of the following conditions is met:
  * The service worker has not received an event for over thirty seconds and there are no outstanding long running tasks in progress. If a service worker received an event during that time, the idle timer was removed.
  * A long running task has taken over five minutes to complete and no events have been received in the past thirty seconds.


New service worker events received before the idle timer or long running task timer expire would reset the timers and extend the service worker's lifetime.
Unfortunately, this behavior did not apply to extension events. Extension events could wake an extension service worker, and keep it alive until the event completes, but it could not extend the thirty second idle timer. This effectively meant that extension service workers could be terminated any time after the last extension event completed, even if the browser had just dispatched a new event to the extension.
## What's changed
As of Chrome 110, all events reset the idle timer and the idle timeout will not occur if there are pending events. In other words, assuming there are no unexpected interruptions, extension service workers will now typically stay alive as long as they are actively processing events. In addition, calls to extension specific Chrome APIs, such as `chrome.storage.local.get()`, will reset the idle timeout. Specifically:
  * The service worker terminates after 30 seconds of inactivity. (Receiving an event or calling an extension API resets this timer).
  * The service worker terminates if a single request, such as an event or API call, takes longer than 5 minutes to process.


Some APIs like native messaging provide a strong keep-alive which cancel both of these timers.
We are still working to ensure that extension service workers are terminated when possible, without shutting down long-running work. Resource-concious extension service workers should always yield when possible. Additionally, extensions should prepare for unexpected termination by persisting state. This guards against unpredictable events like the browser being forcefully closed by the user.
Photo by [Paula Guerreiro](https://unsplash.com/@pguerreiro?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/photos/W2atfIRHDIk?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2023-01-27 UTC.

