---
url: https://developer.chrome.com/blog/eyeos-journey-to-testing-mv3-service%20worker-suspension?hl=en
title: https://developer.chrome.com/blog/eyeos-journey-to-testing-mv3-service%20worker-suspension?hl=en
date: 2025-05-11T16:56:01.655878
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/eyeos-journey-to-testing-mv3-service%20worker-suspension?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/eyeos-journey-to-testing-mv3-service%20worker-suspension?hl=es-419)




  * On this page
  * [What's this about?](https://developer.chrome.com/blog/eyeos-journey-to-testing-mv3-service%20worker-suspension?hl=en#whats_this_about)
  * [What is a service worker?](https://developer.chrome.com/blog/eyeos-journey-to-testing-mv3-service%20worker-suspension?hl=en#what_is_a_service_worker)
    * [When are service workers suspended?](https://developer.chrome.com/blog/eyeos-journey-to-testing-mv3-service%20worker-suspension?hl=en#when_are_service_workers_suspended)
    * [Why is testing this a problem?](https://developer.chrome.com/blog/eyeos-journey-to-testing-mv3-service%20worker-suspension?hl=en#why_is_testing_this_a_problem)
  * [Testing Service Worker Suspension](https://developer.chrome.com/blog/eyeos-journey-to-testing-mv3-service%20worker-suspension?hl=en#testing_service_worker_suspension)
    * [How do we cover the whole functionality? Fuzz Tests](https://developer.chrome.com/blog/eyeos-journey-to-testing-mv3-service%20worker-suspension?hl=en#how_do_we_cover_the_whole_functionality_fuzz_tests)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  Chrome Extensions: eyeo's journey to testing service worker suspension 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [What's this about?](https://developer.chrome.com/blog/eyeos-journey-to-testing-mv3-service%20worker-suspension?hl=en#whats_this_about)
  * [What is a service worker?](https://developer.chrome.com/blog/eyeos-journey-to-testing-mv3-service%20worker-suspension?hl=en#what_is_a_service_worker)
    * [When are service workers suspended?](https://developer.chrome.com/blog/eyeos-journey-to-testing-mv3-service%20worker-suspension?hl=en#when_are_service_workers_suspended)
    * [Why is testing this a problem?](https://developer.chrome.com/blog/eyeos-journey-to-testing-mv3-service%20worker-suspension?hl=en#why_is_testing_this_a_problem)
  * [Testing Service Worker Suspension](https://developer.chrome.com/blog/eyeos-journey-to-testing-mv3-service%20worker-suspension?hl=en#testing_service_worker_suspension)
    * [How do we cover the whole functionality? Fuzz Tests](https://developer.chrome.com/blog/eyeos-journey-to-testing-mv3-service%20worker-suspension?hl=en#how_do_we_cover_the_whole_functionality_fuzz_tests)


Aga Czyżewska 
[ LinkedIn ](https://www.linkedin.com/in/aczyzewska)
Justin Wernick 
[ Mastodon ](https://fosstodon.org/@jworthe) [ Homepage ](https://www.worthe-it.co.za/)
Rowan Deysel 
[ LinkedIn ](https://www.linkedin.com/in/rowan-deysel-17328219)
## What's this about?
The transition from Manifest V2 to Manifest V3 comes with a fundamental change. In Manifest V2, extensions lived in a background page. Background pages managed the communication between extensions and web pages. Manifest V3 uses service workers instead.
In this post, we delve into the problem of testing extension service workers. In particular, we take a look at how to make sure that our product works correctly in case a service worker gets suspended.
## Who are we?
[eyeo](http://www.eyeo.com) is a company dedicated to empowering a balanced and sustainable online value exchange for users, browsers, advertisers, and publishers. We have more than 300 million global ad-filtering users who allow the display of Acceptable Ads, an independently-derived ad standard that determines whether an ad is acceptable and nonintrusive.
Our Extension Engine team provides ad-filtering technology that powers some of the most popular ad-blocking browser extensions on the market, like AdBlock and Adblock Plus with more than 110 million users worldwide. Additionally, we offer this technology as an [open-source library](https://gitlab.com/eyeo/adblockplus/abc/webext-ad-filtering-solution), making it available to other ad-filtering browser extensions.
## What is a service worker?
Extension service workers are a browser extension's central event handler. They run independently in the background. Broadly this is fine. We can do most of the things we need to do on a background page in the new service worker. But there are a few changes in comparison with background pages:
  * Service workers **terminate when not in use**. This requires us to [persist application states](https://developer.chrome.com/docs/extensions/mv3/migrating_to_service_workers#state) instead of relying on global variables. This means that any entry points into our system must be prepared to be called before the system is initialized. 
  * **Event listeners must be attached before waiting for any async callbacks**. Suspended service workers can still receive events that it has subscribed to. If the listener for the event isn't registered in the first turn of the event loop, it won't receive the event if that event woke up the service worker.
  * Idle termination **can interrupt timers** before they complete.


### When are service workers suspended?
For Chrome 119, what we've experienced is that service workers are suspended:
  * After not receiving events or calling extension APIs for 30 seconds.
  * Never if the developer tools are open or you are using a ChromeDriver based testing library ([see feature request](https://bugs.chromium.org/p/chromedriver/issues/detail?id=4686)). 
  * If you click _Stop_ in chrome://serviceworker-internals.


For more recent information refer to [Service Workers Lifecycle](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers/lifecycle).
### Why is testing this a problem?
Ideally, it would have been useful to have official guidance on “how to test service workers in an efficient way” or examples of working tests. During our adventures in testing service workers, we faced a few challenges:
  * We have state in our test extension. When the service worker stops, we lose its state and its registered events. How would we persist data in our testing flow?
  * If service workers can be suspended at any point, we need to test that all features work if they are interrupted.
  * Even if we would introduce a mechanism in our tests that randomly suspends service workers, there's no API in the browser to suspend it easily. [We've asked the W3C team](https://github.com/w3c/webextensions/issues/140) to add this feature, but that is an ongoing conversation. 


## Testing Service Worker Suspension
We've tried several approaches to triggering service worker suspension during tests:
**Approach** | **Issues with the approach**  
---|---  
Wait an arbitrary amount of time (for example 30 seconds)  | This makes testing slow and unreliable, especially when running multiple tests. It does not work when using WebDriver, since WebDriver uses Chrome's DevTools API, and the service worker is not suspended when DevTools is open. Even if we could bypass it, we would still have to check if the service worker was suspended and we don't have a way to do that.   
Run an infinite loop in the service worker  | According to the spec, this can lead to termination depending on how the browser implements this functionality. Chrome does not terminate the service worker in this case so we cannot test the scenario when the service worker gets suspended.   
Having a message in the service worker to check if it's been suspended  | Sending a message wakes up the service worker. This can be used to check if the service worker was asleep, but it breaks results for tests that need to do checks immediately after suspending the service worker.   
Kill the service worker process using chrome.processes.terminate()  | The service worker for the extension shares a process with other parts of the extension, so killing this process using chrome.process.terminate() or Chrome's process manager GUI kills not only the service worker but also any extension pages.   
We ended up with a test that checks how our code responds to the service worker being suspended by having Selenium WebDriver open chrome://serviceworker-internals/ and click the "stop" button for the service worker.
This is the best option so far, but it isn't ideal because our [Mocha tests (which run on an extension page) ](https://gitlab.com/eyeo/adblockplus/abc/webext-ad-filtering-solution/-/blob/master/test/runner.js?ref_type=heads)can't do this themselves, so they need to communicate back to our WebDriver node program. This means that these tests can't run using just the extension; they have to be triggered [using Selenium WebDriver](https://gitlab.com/eyeo/adblockplus/abc/webext-ad-filtering-solution/-/blob/master/test/runner.js?ref_type=heads#L354).
Here is a diagram of how we communicate with the browser API through different flows and how adding the "suspending service workers" mechanism affects it.
Testing flow with service worker suspension.
In a new flow that suspends service workers (blue), we've added Selenium WebDriver to "click" suspend through the UI, which triggers an action in the browser API. 
It's worth mentioning that there was a [Chrome bug](https://bugs.chromium.org/p/chromium/issues/detail?id=1325792) where doing this with Selenium WebDriver caused the service worker to be unable to start again. This was fixed in Chrome 116 and fortunately, there is also a workaround: setting Chrome to open DevTools automatically on every tab makes the service worker start correctly. 
This is the approach we're using when testing even though it isn't ideal since clicking the button may not be a stable API and opening DevTools (for older browsers) seems to have a performance cost.
### How do we cover the whole functionality? Fuzz Tests
Once we had a mechanism for testing suspension, we had to decide how to plug it into our automation test suites. We ran our standard tests in an environment where before each interaction with the background page, the [service worker is suspended](https://gitlab.com/eyeo/adblockplus/abc/webext-ad-filtering-solution/-/blob/master/test/mocha/mocha-runner.js?ref_type=heads#L97) by WebDriver clicking _Stop_ on the chrome://serviceworker-internals/ page.
Image presenting current setup of tests.
We run most and not all of the tests because the suspension mechanism isn't fully stable, and sometimes it causes flakiness. Also, running all test suites in fuzz mode takes a lot of time. So, instead of covering all "similar" cases, we picked the most critical paths for testing in fuzz mode. It's worth mentioning that running functional tests in "fuzz" mode means we had to increase the timeouts of the tests because suspending and restarting service workers takes additional time.
These tests are valuable as a coarse-grained first pass, which highlights many places where the code fails, but may not necessarily uncover all of the subtle ways that service worker suspension might cause things to break.
Internally, we call these kinds of tests "Fuzz tests". Traditionally, fuzz testing is when you throw invalid input at your program and make sure that it responds reasonably, or at least doesn't crash. In our case, the "invalid input" is the service worker being suspended at any time, and the "reasonable behavior" we expect is that our ad-filtering functionality must keep working as before. This isn't really invalid input since this is expected behavior in Manifest V3, but this would have been invalid in Manifest V2 so it feels like reasonable terminology. 
## Summary
Service workers are one of the biggest changes in Manifest V3 (besides declarativeNetRequest rules). Migration to Manifest V3 may require many code changes in browser extensions and new approaches to testing. It also requires developers of extensions with persistent state to prepare their extensions for handling unexpected service worker suspension in a graceful way.
Unfortunately, there is no API for handling suspension in an easy way that fits our use case. Since we wanted to test the robustness of our extension's codebase against suspension mechanisms in an early phase, we had to work around it. Other extension developers that face similar challenges can use this workaround, which, while time-consuming in the development and maintenance phase, is worth it so we can ensure that our extensions can successfully operate in an environment in which service workers are regularly suspended.
Even though there's already [basic support for testing service worker suspension](https://developer.chrome.com/docs/extensions/how-to/test/test-serviceworker-termination-with-puppeteer), better [platform support for testing service workers](https://github.com/w3c/ServiceWorker/issues/1696) from within extensions is something that we really would like to see in the future, as it could greatly reduce our test execution times and maintenance effort.
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-02-27 UTC.

