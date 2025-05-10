---
url: https://expo.dev/privacy-explained
title: https://expo.dev/privacy-explained
date: 2025-04-30T17:19:28.718689
depth: 2
---

# [Privacy of the Expo Platform and Expo Services Explained](https://expo.dev/privacy-explained#privacy-of-the-expo-platform-and-expo-services-explained)
Last updated February 25th, 2025
An explanation of GDPR, CCPA, and other privacy policies at Expo.
To try and remove some of the fog that surrounds privacy policies, and help you contextualize intimidating walls of legal text, we've provided a brief explanation of what data we collect, and why. For a more detailed explanation, see our [privacy policy](https://expo.dev/privacy).
In general, there are two ways Expo handles data. In technical terms, Expo is sometimes a _data controller_ and sometimes a _data processor_. When a developer uses Expo as a tool and service, we are a controller of their data since we're directly providing services to them. After the developer uses Expo's services to create an app and distributes it to their users (end-users), we become a data processor because we process end-user data on behalf of the developer. Below is an explanation of how we treat data in both cases and the implications of both.
## [Expo and developer data](https://expo.dev/privacy-explained#expo-and-developer-data)
When you create an account on Expo or use our tools and services, we collect data including your name, email, and, if you enable [paid services](https://expo.dev/pricing), your billing information. In addition, we also collect tracking information about how you use Expo CLI, our documentation site (<https://docs.expo.dev>), and our website ([https://expo.dev](https://expo.dev/)). This data helps us make decisions about our products and services, in addition to allowing us to deliver satisfactory user experiences.
In all scenarios regarding our users' data, Expo is GDPR-, CCPA-, and Data Privacy Framework-compliant.
## [Expo and end-user data](https://expo.dev/privacy-explained#expo-and-end-user-data)
When developers create apps with Expo, their users (end-users) ultimately use their apps and websites. When end-users use apps built by Expo, we collect very little end-user data. The data we may collect includes the end-user's push token, which we use for push notifications, but this is only collected if you specifically opt in to push notifications and collect the user's `ExpoPushToken`.
An example situation is when an app uses the EAS Update feature, the end-user's app will often request new app updates over HTTPS when the app is opened on the end-user's device. If there is a new update available, we will push the new update to that end-user. These requests do not contain identifying information such as unique device identifiers. The request contains non-identifying information needed to correctly process the update request, including the end-user's operating system, the developer's project ID, and a random token used to determine if an installation of the app has requested an update.
Another example is when a developer uses Expo to send push notifications. We do store end-user push tokens to make it possible to send notifications, however the most sensitive part of sending notifications is the notification's content itself. We process that data to send it to end-users; however, it is never stored and we only handle that data as long as it takes to send the notification.
There are some cases where we may disclose user data to others. These include situations when we have consent or when we send data to a service that processes data for us (you can see a list of services we use [here](https://expo.dev/privacy/subprocessors)).
In all scenarios regarding end-user data, Expo is GDPR-, CCPA-, and Data Privacy Framework-compliant.
## [Apps made with Expo](https://expo.dev/privacy-explained#apps-made-with-expo)
While Expo ensures the proper handling and processing of developer data and end-user data, we cannot guarantee that the developers who build apps with Expo follow data privacy practices themselves. For example, a developer could build an app that collects an end-user's information and shares it publicly in some way. In this case, Expo would not have access to this information, only the developer who created the app would. While it's ultimately up to each individual end-user to evaluate what data they share and what apps or services they trust, we recommend they start by looking for similar policies in their app developer's privacy policy.
## [How will I be notified of changes?](https://expo.dev/privacy-explained#how-will-i-be-notified-of-changes)
As our privacy policies change, we will either email you or put a prominent banner on our website to notify you of any changes.
## [More on privacy](https://expo.dev/privacy-explained#more-on-privacy)
For more information please see our privacy policy at [https://expo.dev/privacy](https://expo.dev/privacy). If you have questions about how we collect and use data, please send us a message via our [contact form](https://expo.dev/contact).

