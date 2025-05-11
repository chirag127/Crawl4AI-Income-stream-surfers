---
url: https://developer.chrome.com/blog/digital-credentials-cross-device-ot?hl=en
title: https://developer.chrome.com/blog/digital-credentials-cross-device-ot?hl=en
date: 2025-05-11T16:55:36.972451
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/digital-credentials-cross-device-ot?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/digital-credentials-cross-device-ot?hl=es-419)

Sign in


  * On this page
  * [Privacy and security considerations](https://developer.chrome.com/blog/digital-credentials-cross-device-ot?hl=en#privacy_and_security_considerations)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  Origin trial: Cross-device Digital Credentials API now in Chrome desktop 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Privacy and security considerations](https://developer.chrome.com/blog/digital-credentials-cross-device-ot?hl=en#privacy_and_security_considerations)


José Luis Zapata 
[ GitHub ](https://github.com/zapata131) [ LinkedIn ](https://www.linkedin.com/in/zapata131) [ Bluesky ](https://bsky.app/profile/zapata131.bsky.social) [ Homepage ](https://www.zapata131.com)
Published: April 30, 2025 
An exciting update to the Digital Credentials API is here: cross-device support.
Starting from Chrome 136, users can now present verified information stored in their Android device's digital wallet to desktop Chrome. This builds on the [initial release of the Digital Credentials API](https://developer.chrome.com/blog/digital-credentials-api-origin-trial), introduced as an origin trial in Chrome 128 for Android. This feature will first be available on Pixel devices, and other Android vendors are updating their camera apps to support it too.
## Background
More and more, [digital credentials](https://w3c-fedid.github.io/digital-credentials/) (like a mobile driver's license) are stored in mobile wallets like Google Wallet. Presenting them on desktop is possible, but existing methods don't offer strong privacy or security guarantees. Chrome improves this by supporting credential presentation in the browser, enhancing security and privacy, and making it easier for users to present identity information safely and smoothly.
The Digital Credentials (DC) API, allowing Chrome users on Android to present digital credentials from a wallet app on the **same device** , is already in an origin trial. We are now extending this origin trial to support cross-device digital credentials presentation. With the **cross-device capability** , users can now scan a QR code displayed on desktop Chrome to establish a connection to securely present credentials from their Android phone.
This innovation ensures:
  * **Enhanced user convenience:** Users can conveniently present verified information across devices.
  * **Strong security guarantees:** Providing a phishing-resistant cross-device presentation using Bluetooth as a proximity check between the desktop and the mobile device.


## How it works
Sharing verifiable credentials stored in a smartphone's digital wallet with a website using Chrome desktop involves the following steps:
  1. **Credential request initiation** : A website requesting identity verification invokes the DC API. Desktop Chrome displays a QR code asking users to retrieve a credential from an Android device. This QR code contains cryptographic information necessary for secure communication between Chrome desktop and the mobile device.
  2. **User action** : The user scans the QR code using their Android device.
  3. **Device connection** : Desktop Chrome and the Android device establish a secure connection to verify proximity using Bluetooth before proceeding with credential presentation.
  4. **Credential selection** : Android displays the eligible wallet credentials on the device that match the request.
  5. **Wallet consent and authentication:**
     * After the user selects the credential, the request is forwarded to the wallet app holding that credential. The user may be asked by the wallet app to provide sharing consent and authenticate locally (for example, with a PIN or biometrics).
     * The wallet app processes the request and securely sends the encrypted requested information back to desktop Chrome.
  6. **Credential presentation** : The requested information is presented to the [relying party](https://en.wikipedia.org/wiki/Relying_party) website, which sends it to its server for secure decryption and processing (such as verifying the user's age or identity).


## Privacy and security considerations
This cross-device feature incorporates privacy and security practices used in [CTAP 2.2](https://fidoalliance.org/specs/fido-v2.2-rd-20230321/fido-client-to-authenticator-protocol-v2.2-rd-20230321.html#sctn-hybrid):
  * **Proximity of the desktop and the mobile device:** CTAP 2.2 ensures that the phone and desktop are in proximity before credentials are presented, preventing attackers from remotely misusing QR codes to access users' information.
  * **Secure communication:** Communication between desktop Chrome and the Android device is proxied through a secure tunnel server. Wallets typically encrypt the response so only the requesting web server can read it.
  * **User consent:** The user must explicitly act on the credential request by selecting a credential before any data is shared.
  * **Selective disclosure:** Wallet apps only present the specific attributes requested, such as an age range, without exposing unnecessary information. The DC API also supports privacy-enhancing features such as [zero-knowledge proof in Google Wallet](https://blog.google/products/google-pay/google-wallet-age-identity-verifications).


## Try it out
To explore the cross-device Digital Credentials API:
  1. Update to **Chrome 136** on desktop and **Google Play services 24.0** or later on your Android device.
  2. Enable the flag at `chrome://flags#web-identity-digital-credentials`.
  3. Follow the demo:
    1. Navigate to [`https://digital-credentials.dev`](https://digital-credentials.dev) on desktop Chrome.
    2. Press the **Request Credentials** button
    3. Scan the QR code with your Android phone.
    4. Present a demo credential stored in the IC Wallet app (available [through the OpenWallet Foundation](https://digitalcredentials.dev/docs/samples/android-wallet-sample/#install-the-apps)).


This feature is available on Pixel devices, and we are working to enable support for other Android devices in the future.
To get started with experimenting on your own website, [join the Digital Credentials API origin trial](https://developer.chrome.com/blog/digital-credentials-api-origin-trial#participate_in_the_origin_trial).
## Resources
  * [Digital Credentials API origin trial announcement](https://developer.chrome.com/blog/digital-credentials-api-origin-trial)
  * [W3C Digital Credentials GitHub](https://github.com/w3c-fedid/digital-credentials)
  * [W3C Digital Credentials editor's draft](https://w3c-fedid.github.io/digital-credentials/)


## Share feedback
Tried it? Tell us what worked, what didn't, and what you'd fix.
[Give feedback](https://docs.google.com/forms/d/e/1FAIpQLSdIVA5PrtvCoW_RoCGI3iIePdc-hoxb3M0H24dzX79FYshgkg/viewform)
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-04-30 UTC.

