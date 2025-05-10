---
url: https://docs.expo.dev/deploy/web
title: https://docs.expo.dev/deploy/web
date: 2025-04-30T17:11:46.547889
depth: 1
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Publish your web app
Learn how to deploy your web app using EAS Hosting.
> EAS Hosting is in preview and subject to changes.
If you are building a universal app, you can quickly deploy your web app using [EAS Hosting](https://docs.expo.dev/eas/hosting/introduction). It is a service for deploying web apps built with Expo Router and React.
## Prerequisites
Before you begin, in your project's app.json file, ensure that the [`expo.web.output`](https://docs.expo.dev/versions/latest/config/app#output) property is either `static` or `server`.
## Export your web project
To deploy your web app, you need to create a static build of your web project. Export your web project into a dist directory by running the following command:
Terminal
Copy
`- ``npx expo export --platform web`
> Remember to re-run this command every time before deploying when you make changes to your web app.
## Initial deployment
To publish your web app, run the following [EAS CLI](https://docs.expo.dev/develop/tools#eas-cli) command:
Terminal
Copy
`- ``eas deploy`
After running this command for the first time, you'll be prompted to select a preview subdomain for your project. This subdomain is a prefix used to create a preview URL and is used for production deployments. For example, in `https://test-app--1234.expo.app`, `test-app` is the preview subdomain.
Once your deployment is complete, the EAS CLI will output a preview URL to access your deployed app.
## Production deployment
To create a production deployment, run the following [EAS CLI](https://docs.expo.dev/develop/tools#eas-cli) command:
Terminal
Copy
`- ``eas deploy --prod`
Once your deployment is complete, the EAS CLI will output a production URL to access your deployed app.
## Learn more
You can learn more about setting up [deployment aliases](https://docs.expo.dev/eas/hosting/deployments-and-aliases), using a [custom domain](https://docs.expo.dev/eas/hosting/custom-domain), or [deploying an API Route](https://docs.expo.dev/router/reference/api-routes#deployment).

