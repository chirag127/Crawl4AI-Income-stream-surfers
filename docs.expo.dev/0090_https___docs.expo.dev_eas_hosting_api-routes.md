---
url: https://docs.expo.dev/eas/hosting/api-routes
title: https://docs.expo.dev/eas/hosting/api-routes
date: 2025-04-30T17:13:38.628761
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# API Routes
Learn how to inspect requests from API routes on the EAS Hosting dashboard.
> This page is for EAS Hosting specific details about API routes. For general documentation about the topic, see the [API routes](https://docs.expo.dev/router/reference/api-routes) documentation under Expo Router.
Crashes, logs, and requests that occur in API routes can be inspected on the EAS Hosting dashboard.
### Crashes
A crash is any uncaught error that is thrown while a request was handled, which prevented a response from being returned, for example, `throw new Error("An error!")`. Crashes may be viewed on the [Hosting crashes](https://expo.dev/accounts/%5BaccountName%5D/projects/%5BprojectName%5D/hosting/crashes) page.
Crashes are grouped. If similar crashes are detected, you will see just one line item for them. The crash details will show the stack trace and metadata for the first and last known occurrence of the crash.
### Logs
All logs from API routes and server functions (`console.log`, `console.info`, `console.error`, and so on) are recorded on the deployment level logs page. Go to [Hosting deployments](https://expo.dev/accounts/%5BaccountName%5D/projects/%5BprojectName%5D/hosting/deployments) > _select a deployment_ > Logs.
### Requests
Requests can be viewed on the project level at [Hosting requests](https://expo.dev/accounts/%5BaccountName%5D/projects/%5BprojectName%5D/hosting/requests) and deployment level [Hosting Deployments](https://expo.dev/accounts/%5BaccountName%5D/projects/%5BprojectName%5D/hosting/deployments) > _select a deployment_ > Requests.
This will show a list of requests against your service, with metadata (status, browser, region, duration, and more) per request. These include all requests to the service, including requests to API routes.
### Looking up a request by ID
All response headers include a `Cf-Ray` header that looks like `8ffb63895cf6779b-LHR`. The first part of this is the request ID and you may look up the request on the EAS dashboard via this ID using the filters in [Hosting Requests](https://expo.dev/accounts/%5BaccountName%5D/projects/%5BprojectName%5D/hosting/requests).
This request ID is also displayed on any service-level error pages.
### Sampling
If a deployment receives a high amount of traffic, data that EAS Hosting records will be [downsampled](https://developers.cloudflare.com/analytics/graphql-api/sampling/). This means as your deployments receive more requests, fewer data points will be recorded, and you may not see individual requests, logs, and crashes be listed one by one. However, statistical counts, such as number of requests or crashes, will be estimated to still reflect all requests proportionally.

