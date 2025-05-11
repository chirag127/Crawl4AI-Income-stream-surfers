---
url: https://developer.chrome.com/blog/ebay-digital-asset-links-case-study?hl=en
title: https://developer.chrome.com/blog/ebay-digital-asset-links-case-study?hl=en
date: 2025-05-11T16:55:43.072258
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/ebay-digital-asset-links-case-study?hl=en#main-content)
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


#  How eBay improved login success rates by 10% with seamless credential sharing 
Stay organized with collections  Save and categorize content based on your preferences. 
Raphael Tsow 
[ LinkedIn ](https://www.linkedin.com/in/rstow)
Mahendar Madhavan 
[ GitHub ](https://github.com/madmahen) [ LinkedIn ](https://www.linkedin.com/in/mahendarmadhavan)
Yu Tsuno 
[ LinkedIn ](https://www.linkedin.com/in/yu-tsuno-a6182116b)
Simplifying user login processes is an ongoing challenge for developers, especially when users access services across multiple platforms. Failed sign-ins not only lead to frustrated users, but also increase support costs.
eBay faced this exact problem. With millions of users signing in across multiple domains and apps (such as ebay.com, ebay.co.uk, and their mobile app), they needed a seamless and secure login process in place. Websites and apps don't always recognize that saved credentials belong to the same user account. A common frustration occurs when you update your password on the web, but can't sign in on the app because it's still using the old password. This happens when the app and website aren't linked to share account credentials, leading to sign-in failures.
To tackle this, eBay implemented [Digital Asset Links](https://developers.google.com/digital-asset-links/v1/getting-started) to enable seamless credential sharing across their platforms. By securely linking their websites and Android apps, eBay ensured that Google Password Manager could reliably recognize their credentials across platforms.
## What is seamless credential sharing?
Seamless credential sharing, enabled by the Digital Asset Links protocol, allows websites and Android apps to securely share login information. This protocol lets apps and websites publicly declare their associations through verifiable digital signatures, enabling features like credential sharing and deep linking.
By supporting seamless credential sharing, Google Password Manager can seamlessly autofill login information across associated websites and apps, ensuring stored credentials are readily available and reducing user friction.
## How eBay solved the problem
The process starts with eBay hosting a configuration file called `assetlinks.json` on its domains. This file defined the credential-sharing relationship between eBay's web and app platforms. By updating their Android app to reference these configurations and [following the seamless credential-sharing setup guide](https://developers.google.com/identity/credential-sharing/set-up), eBay enabled secure, verifiable links between platforms.
With this implementation:
  * Sign-in success rates increased by 10% for users whose passwords were prefilled.
  * Sign-in error rates decreased by 5%.


In addition to seamlessly connecting your experience across eBay's website and apps, this change also improves security by ensuring only verified connections between eBay's domains and apps, reducing the risk of phishing and login information misuse.
## What's next for eBay?
Following the success of seamless credential sharing, eBay is further improving the login experience by implementing [passkeys](https://developer.chrome.com/docs/identity/passkeys) and exploring new approaches to credential recovery. They have already implemented passkeys across their platforms, improving security and the login experience.
eBay is also experimenting with the [Restore Credentials](https://developer.android.com/identity/sign-in/restore-credentials) feature in Android, which enables users to seamlessly access their accounts on new devices. In addition, eBay is planning to use [Related Origin Requests](https://web.dev/articles/webauthn-related-origin-requests) to allow users to reuse passkeys across multiple domains. This dedication to cutting-edge technologies reinforces eBay's commitment to providing a secure and user-friendly experience.
## Why this matters for you
By reducing friction and frustration during the login journey, you can significantly improve user experience, particularly for users accessing your services across multiple domains and Android apps, by implementing seamless credential sharing, and potentially increase user engagement.
This solution isn't limited to ecommerce; no matter what industry that requires authentication can benefit from deploying seamless credential sharing.
Ready to improve your user sign-in experience? Start by checking out the [guide for implementing Digital Asset Links](https://developers.google.com/identity/credential-sharing/set-up). Small changes to your login flow can bring big results for your users.
## Learn more
  * [Digital Asset Links setup guide](https://developers.google.com/identity/credential-sharing/set-up)
  * [Digital Asset Links Asset Owners Guide](https://developers.google.com/digital-asset-links)
  * [Passwordless login with passkeys](https://developers.google.com/identity/passkeys/)
  * [Related Origin Requests](https://developer.chrome.com/blog/passkeys-updates-chrome-129#related-origin-requests)


Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-03-06 UTC.

