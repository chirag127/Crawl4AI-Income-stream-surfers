---
url: https://docs.expo.dev/eas/hosting/custom-domain
title: https://docs.expo.dev/eas/hosting/custom-domain
date: 2025-04-30T17:13:38.641136
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Custom domain
Set up a custom domain for your production deployment.
By default, your production deployment on EAS Hosting will look like this: `my-app.expo.app` , where `my-app` is your chosen preview subdomain name. If you own a domain, you may assign it as a custom domain to the production deployment.
Each project can have exactly one custom domain, which is assigned to the production deployment.
> Note: Setting up a custom domain is a premium feature and isn't available on the free plan. Learn more about different plans and benefits at [EAS pricing](https://expo.dev/pricing).
## Prerequisites
An EAS Hosting project with a production deployment
The custom domain will always load the production deployment. Therefore, to add a custom domain to your project, you will need a deployment that's been promoted to production first.
A domain name
You will need to own a domain name you want to use.
## Assigning a custom domain
  1. In your project's dashboard, navigate to [Hosting settings](https://expo.dev/accounts/%5BaccountName%5D/projects/%5BprojectName%5D/hosting/settings).
  2. If you do not have a production deployment, you'll be prompted to assign one first.
  3. Under Custom domain, enter the custom domain you'd like to set up. Both apex domains and subdomains are supported. If you own `example.com`, you can select:
     * `example.com`: apex domain
     * `anything.example.com`: a subdomain
  4. Next, you'll be prompted to fill out some DNS records with your DNS provider:
     * Verification: to prove you own the domain
     * SSL: to set up SSL certificates
     * CNAME (subdomains) or A record (apex domains): to point the domain at your production deployment
  5. Press the refresh button until all checks pass. Depending on your DNS provider, this step usually only takes a couple of minutes.


> If you require for the domain name switchover to be zero downtime, it's important to fill out these records one by one in the order they are presented in the table. That is, add the TXT record for verification, press the refresh button until the UI says verification is successful, then proceed to the next one. If downtime isn't important or relevant, you may add all three DNS records at once.
After assigning a custom domain to your app, the custom domain will route to your production deployment.

