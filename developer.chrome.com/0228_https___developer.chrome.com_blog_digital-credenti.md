---
url: https://developer.chrome.com/blog/digital-credentials-api-origin-trial?hl=en
title: https://developer.chrome.com/blog/digital-credentials-api-origin-trial?hl=en
date: 2025-05-11T16:55:33.771060
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/digital-credentials-api-origin-trial?hl=en#main-content)
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


#  Introducing the Digital Credentials API origin trial 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Eiji Kitamura 
[ GitHub ](https://github.com/agektmr) [ Glitch ](https://glitch.com/@agektmr) [ Mastodon ](https://infosec.exchange/@agektmr) [ Bluesky ](https://bsky.app/profile/agektmr.com)
Published: September 4, 2024 
An origin trial for the Digital Credentials API is starting from Chrome 128. [Digital Credentials API](https://w3c-fedid.github.io/digital-credentials/) is a new web platform API that allows websites to selectively request verifiable information about the user through digital credentials such as a driver's license or a national identification card stored in a digital wallet.
## Background
Real world digital identity is becoming a reality with many public and private entities starting to issue device-bound digital credentials. For example, mobile driver's licenses and IDs in select US states (such as Arizona, California, Colorado, Georgia, and Maryland) can now be provisioned to digital wallet apps such as Google Wallet on mobile devices. Regulations concerning the acceptance of digital credentials for certain online verifications are also emerging and [eIDAS 2.0](https://en.wikipedia.org/wiki/EIDAS) is one example.
Mobile driver's license in Google Wallet. 
The features of a digital credential depend on its format, though they typically include:
  * **Enhanced security and privacy** : The use of advanced encryption and strong authentication methods helps protect sensitive data and ensures secure access. For example, presenting a credential is usually protected behind a user authentication through the wallet app.
  * **Selective disclosure** : [Relying parties](https://en.wikipedia.org/wiki/Relying_party) (RP) can request select information from the credential, allowing users to limit the data shared to what is needed for the use case. For example, whether a user is over 18 can be shared without revealing the user's date of birth.
  * **Interoperability** : The credential should adhere to international standards, enabling compatibility across different systems and countries, facilitating cross-border acceptance.
  * **Verifiability** : The credential data shared is digitally signed by the issuer; RP can verify this signature to verify the data's authenticity.


Because of digital credentials' verifiable nature, they could enable use cases such as:
  * **Age verification:** Request age to verify a person's age before serving age-restricted content or purchasing age-restricted items.
  * **Identity verification:** Request name and address to verify a person's identity for legal compliance or fraud-prevention.
  * **Driving privileges check:** Verify a person's eligibility to drive (for example, when renting a car).


As websites have begun communicating directly with mobile wallet applications (such as by using custom URL schemes) to request digital credentials for various use cases, browsers see an opportunity to make this interaction more secure, resistant to abuse and easier to use via a purpose-built API.
## Introducing the Digital Credentials API
[The Digital Credentials API](https://w3c-fedid.github.io/digital-credentials/) is a new web platform API that allows RP websites to request the presentation of digital credentials from wallet apps. The API is available in Chrome as an origin trial starting from Chrome 128.
The API is protocol agnostic, allowing the RP to specify a protocol based on their requirements. When an RP makes a request, the browser sends the request to the mobile operating system which searches for a matching credential in installed wallet applications. If any are found, the mobile operating system prompts the user to select one and sends the request to the user-selected wallet. After a local authentication, the wallet returns a response containing the requested credential data.
Diagram of communication between the browser, wallet and relying party. 
Chrome will first support the API in Chrome on Android for requesting credentials from wallet apps on the same device. In the future, we plan on supporting Chrome desktop to request credentials cross-device from another mobile device.
At launch, Google Wallet will integrate with the Digital Credentials API, enabling select businesses and organizations to initiate a request for users to present their ID online, via Chrome on Android, and verify the authenticity of the transmitted data by examining the cryptographic signature. To participate, fill in this [form](https://g.co/io/wallet-id) to express interest in accepting digital IDs from Google Wallet.
The API will also soon be used by Google Accounts to verify certain users' date of birth. Users residing within a supported US state will be able to use their state ID or driver's license provisioned in available wallet apps (including Google Wallet) to seamlessly share just their date of birth with Google without sharing other details of their identity. This empowers users to demonstrate to Google, in a privacy-preserving way, that they meet account-related [age requirements](https://support.google.com/accounts/answer/1350409).
### Try it out
Requirements:
  * Google Play services 23.40 or later
  * Chrome 128 or later
  * Enable the flag at `chrome://flags#web-identity-digital-credentials`


To try the Digital Credentials API follow the instructions:
  1. Install the demo wallet application following the instructions. 
     * Download [the `IC Wallet` app linked in this page](https://digitalcredentials.dev/docs/samples/android-wallet-sample/#install-the-apps) to your Android device. The source code can be found at the OpenWallet Foundation's [Identity Credentials repository](https://github.com/openwallet-foundation-labs/identity-credential/tree/main/wallet).
     * Run a command `adb install -t <path-to-apk>` to install the app.
  2. Launch the **IC Wallet** app and provision a demo mobile driver's license (mDL). 
     * Tap the menu button and select **Add Self Signed Document.**
  3. Navigate to [https://digital-credentials.dev](https://digital-credentials.dev/) with Chrome 128 or later.
  4. Press **Request Credentials (OpenID4VP).**


Check out the demo that's using [https://digital-credentials.dev](https://digital-credentials.dev/), a test website for developers to generate credential requests for different attributes:
Here's how the demo works step by step:
1. The user lands on the relying party's website and is requested to present their verified family name, given name and an age assurance of over 21 years old.  2. The browser confirms if the user intends to share any digital credential with this website. 
3. The operating system displays the information being requested and eligible credentials that can match the request for the user to select and complete the request.  4. The wallet locally authenticates the user with screen unlock. 
5. The requested digital credential is now passed to the relying party's website. 
## How the API works
Digital Credentials API is built upon the foundation of [the Credential Management API](https://developer.mozilla.org/docs/Web/API/Credential_Management_API), but from an independent API surface: `navigator.identity`. By calling `navigator.identity.get()`, the website can request a digital credential stored on a mobile wallet app. .
```
// Gets a CBOR with specific fields out of mobile driver's license as an mdoc
constcontroller=newAbortController();
const{protocol,data}=awaitnavigator.identity.get({
signal:controller.signal,
digital:{
providers:[{
protocol:"openid4vp",
request:{
response_type:"vp_token",
nonce:"n-0S6_WzA2Mj",
client_metadata:{...},
presentation_definition:{...}
}
}],
}
});

```

The basic API surface is similar to `navigator.credentials.get()`, except that it only accepts `"digital"` credential type. Within the digital credential type, add `providers` array that contains [`IdentityRequestProvider`](https://w3c-fedid.github.io/digital-credentials/#the-identityrequestprovider-dictionary) with the following basic parameters:
  * `protocol`: Specify an exchange protocol with a string. At the time of origin trial, the primary protocol being developed is `"openid4vp"`.
  * `request`: Fill in the parameters digital wallet apps accept for the specified protocol. For `"openid4vp"`, parameters are defined in [OpenID for Verifiable Presentation (OID4VP) for the W3C Digital Credentials API](https://openid.github.io/OpenID4VP/openid-4-verifiable-presentations-wg-draft.html#name-openid4vp-profile-for-the-w) specification.


Example payload to the digital credential type using OID4VP:
```
{
protocol:'openid4vp',
request:{
response_type:'vp_token',
nonce:'gf69kepV+m5tGxUIsFtLi6pwg=',
client_metadata:{},
presentation_definition:{
id:'mDL-request-demo',
input_descriptors:[{
id:"org.iso.18013.5.1.mDL",
format:{
mso_mdoc:{
alg:["ES256"]
}
},
constraints:{
limit_disclosure:"required",
fields:[
{
path:["$['org.iso.18013.5.1']['family_name']"],
intent_to_retain:false
},{
path:["$['org.iso.18013.5.1']['given_name']"],
intent_to_retain:false
},{
path:["$['org.iso.18013.5.1']['age_over_21']"],
intent_to_retain:false
}
]
}
}],
}
}
}

```

With this request, wallets that have mDLs on the device will provide verifiable set of credentials that contain:
  * User's family name.
  * User's given name.
  * A boolean value indicating whether the user is over 21 years old or not.


Here's an example response payload:
```
{
data:'{\n "vp_token": "o2d2ZXJzaW9uYz..."\n}'
id:'',
protocol:'openid4vp',
type:'digital'
}

```

In this example, the credential was requested with the `"openid4vp"` protocol and the response contains `"vp_token"` in the `data` property. Please see [OpenID for Verifiable Presentation (OID4VP) for the W3C Digital Credentials API](https://openid.github.io/OpenID4VP/openid-4-verifiable-presentations-wg-draft.html) specification to learn how to parse the response and verify the credential.
Digital Credentials API is supported on Chrome on Android as an [origin trial](https://developer.chrome.com/docs/web-platform/origin-trials). Chrome on desktop and iOS doesn't support it at this time. For other browser engines, active conversations are being facilitated through the [W3C Web Incubator Community Group](https://wicg.io/).
## Participate in the origin trial
For development, you can enable the Digital Credentials API locally by turning on the Chrome flag `chrome://flags#web-identity-digital-credentials` in Chrome 128 or later.
This feature is also available as an origin trial. Origin trials allow you to try new features and give feedback on their usability, practicality, and effectiveness to the web standards community. For more information, see the [Get started with origin trials](https://developer.chrome.com/docs/web-platform/origin-trials). To sign up for this or another origin trial, visit the [registration page](https://developer.chrome.com/origintrials#/trials/active).
  1. [Request a token](https://developer.chrome.com/origintrials#/view_trial/3139571890230657025) for your origin.
  2. Add the token to your pages. There are two ways to do that: 
     * Add an `origin-trial` `<meta>` tag to the head of each page. For example, this may look something like: `<meta http-equiv="origin-trial" content="TOKEN_GOES_HERE">.`
     * If you can configure your server, you can also add the token using an `Origin-Trial` HTTP header. The resulting response header should look something like:`Origin-Trial: TOKEN_GOES_HERE.`


## Share feedback
If you have any feedback about Digital Credentials API, submit it to the dedicated [Chromium issue tracker](https://issues.chromium.org/u/1/issues/new?component=1518527&pli=1&template=0).
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-09-04 UTC.

