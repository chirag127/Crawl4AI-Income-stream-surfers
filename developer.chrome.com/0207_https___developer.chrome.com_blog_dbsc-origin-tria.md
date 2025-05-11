---
url: https://developer.chrome.com/blog/dbsc-origin-trial?hl=en
title: https://developer.chrome.com/blog/dbsc-origin-trial?hl=en
date: 2025-05-11T16:55:10.240533
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/dbsc-origin-trial?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/dbsc-origin-trial?hl=es-419)




  * On this page
  * [How it works](https://developer.chrome.com/blog/dbsc-origin-trial?hl=en#how_it_works)
    * [Example implementation](https://developer.chrome.com/blog/dbsc-origin-trial?hl=en#example_implementation)
  * [Privacy and security considerations](https://developer.chrome.com/blog/dbsc-origin-trial?hl=en#privacy_and_security_considerations)
  * [Try it out](https://developer.chrome.com/blog/dbsc-origin-trial?hl=en#try_it_out)
    * [For local testing](https://developer.chrome.com/blog/dbsc-origin-trial?hl=en#for_local_testing)
    * [For public testing](https://developer.chrome.com/blog/dbsc-origin-trial?hl=en#for_public_testing)
  * [Get involved and shape the future of web security](https://developer.chrome.com/blog/dbsc-origin-trial?hl=en#get_involved_and_shape_the_future_of_web_security)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  Origin trial: Device Bound Session Credentials in Chrome 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [How it works](https://developer.chrome.com/blog/dbsc-origin-trial?hl=en#how_it_works)
    * [Example implementation](https://developer.chrome.com/blog/dbsc-origin-trial?hl=en#example_implementation)
  * [Privacy and security considerations](https://developer.chrome.com/blog/dbsc-origin-trial?hl=en#privacy_and_security_considerations)
  * [Try it out](https://developer.chrome.com/blog/dbsc-origin-trial?hl=en#try_it_out)
    * [For local testing](https://developer.chrome.com/blog/dbsc-origin-trial?hl=en#for_local_testing)
    * [For public testing](https://developer.chrome.com/blog/dbsc-origin-trial?hl=en#for_public_testing)
  * [Get involved and shape the future of web security](https://developer.chrome.com/blog/dbsc-origin-trial?hl=en#get_involved_and_shape_the_future_of_web_security)


José Luis Zapata 
[ GitHub ](https://github.com/zapata131) [ LinkedIn ](https://www.linkedin.com/in/zapata131) [ Bluesky ](https://bsky.app/profile/zapata131.bsky.social) [ Homepage ](https://www.zapata131.com)
Device Bound Session Credentials (DBSC) is a new web capability designed to protect user sessions from cookie theft and session hijacking. This feature is now available for testing as an Origin Trial in Chrome 135.
## Background
Cookies play a crucial role in modern web authentication, allowing users to stay logged in across browsing sessions. However, attackers increasingly exploit stolen authentication cookies to hijack sessions, bypassing multi-factor authentication and other login security mechanisms.
Malware operators often exfiltrate session cookies from compromised devices, enabling unauthorized access to user accounts. Since cookies are bearer tokens, they grant access without requiring proof of possession—making them a lucrative target for attackers.
Device Bound Session Credentials (DBSC) aims to disrupt cookie theft by creating an authenticated session that is bound to a device. This approach mitigates the chance that exfiltrated cookies can access accounts from another device.
## How it works
DBSC introduces a new API that allows servers to create an authenticated session that is bound to a device. When a session is initiated, the browser generates a public-private key pair, storing the private key securely using hardware-backed storage such as a Trusted Platform Module (TPM) when available.
The browser then issues a regular session cookie. During the session lifetime, the browser periodically proves possession of the private key and refreshes the session cookie. The cookie's lifetime can be set short enough so that stealing the cookie won't be a benefit for attackers.
### Key components
  * **Session registration** :
    * When a user logs in, the server requests a device-bound session using the `Sec-Session-Registration` HTTP header.
    * The browser generates a new key pair, storing the private key securely.
    * A short-lived authentication cookie is also established and bound to this key pair.
    * The server associates the session with the corresponding public key, ensuring the session can only be used on the original device.
  * **Session refresh and proof-of-possession** :
    * When the short-lived cookie expires, Chrome triggers a session refresh.
    * The browser sends a request to a server-defined refresh endpoint (provided during session registration), and, if the server provides one, a signed challenge using the `Sec-Session-Challenge` header.
    * The server verifies the proof of possession by validating the response signed with the session's private key.
    * If valid, the server issues a new short-lived cookie, allowing the session to continue.


One benefit of this approach is that Chrome defers requests that would otherwise be missing the refreshed short-lived cookie. This behavior keeps session-bound cookies consistently available throughout the session and allows developers to rely on them more confidently than with approaches where cookies might expire or disappear without automatic renewal.
### Example implementation
A server can request a device-bound session like this:
```
HTTP/1.1 200 OK
Sec-Session-Registration: (ES256);path="/refresh";challenge="12345"

```

When the session is active, the server can verify it with a challenge-response exchange:
```
HTTP/1.1 401 Unauthorized
Sec-Session-Challenge: "verify-session"

```

The browser responds with:
```
POST /refresh
Sec-Session-Response: "signed-proof"

```

## Benefits
  * **Mitigates cookie theft** : Even if session cookies are stolen, they cannot be used from another device.
  * **Enhances security without major UX changes** : Works transparently in the background without requiring additional user interaction.
  * **Reduces reliance on long-lived session cookies** : Short-lived cookies are automatically refreshed as long as the session remains valid on the original device.
  * **Supports standard cryptographic mechanisms** : Leverages TPM-backed secure storage when available, providing strong protection against exfiltration.


## Privacy and security considerations
DBSC is designed to enhance security while preserving user privacy:
  * **No additional tracking vectors** : Each session is associated with a unique key pair, preventing cross-session tracking.
  * **No long-term device fingerprinting** : Servers cannot correlate different sessions on the same device unless explicitly allowed by the user.
  * **Clearable by users** : Sessions and keys are deleted when the user clears site data.
  * **Aligned with cookie policies** : DBSC follows the same site-based scoping as cookies, ensuring it does not introduce cross-origin data leaks.


## Try it out
The Device Bound Session Credentials Origin Trial is available from Chrome 135.
### For local testing
To test DBSC locally:
  * Go to `chrome://flags#device-bound-session-credentials` and enable the feature.


### For public testing
To test DBSC with the origin trial in a public environment:
  1. Visit the [Chrome Origin Trials page](https://developer.chrome.com/origintrials#/view_trial/3911939226324697089) and sign up.
  2. Add the provided token to your site's HTTP headers:
```
Origin-Trial: <your-trial-token>

```



## Resources
  * [Device Bound Session Credentials specification](https://w3c.github.io/webappsec-dbsc/)
  * [GitHub repository for DBSC](https://github.com/w3c/webappsec)
  * [Device Bound Session Credentials (DBSC) integration guide](https://developer.chrome.com/docs/web-platform/device-bound-session-credentials)


## Get involved and shape the future of web security
Join us in making web authentication more secure! We encourage web developers to test DBSC, integrate it into their applications, and share feedback. You can engage with us on[ GitHub](https://github.com/w3c/webappsec/issues) or participate in discussions with the Web Application Security Working Group.
By implementing DBSC, we can collectively reduce session hijacking risks and enhance authentication security for users. Get started today and help define the future of web security!
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-04-22 UTC.

