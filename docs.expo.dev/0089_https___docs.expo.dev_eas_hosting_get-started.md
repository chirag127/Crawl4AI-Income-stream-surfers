---
url: https://docs.expo.dev/eas/hosting/get-started
title: https://docs.expo.dev/eas/hosting/get-started
date: 2025-04-30T17:13:38.621255
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Deploy your first Expo Router and React app
Learn how to deploy your Expo Router and React apps to EAS Hosting.
EAS Hosting is a react hosting service that allows you to deploy an exported Expo web build to a preview or production URL.
This guide will walk you through the process of creating your first web deployment.
[Watch: Deploy your Expo Router web project](https://www.youtube.com/watch?v=NaKsfWciJLo)
## Why EAS Hosting
Historically, traditional website hosting services were recommended for deploying Expo Router and React apps. However, this approach doesn't address the unique challenges of dealing with native apps. Here are some key limitations:
  * Version synchronization: During the app store publishing process, you may need to deploy new versions of your servers.
  * Request routing complexity: Different versions of your native app may require routing to specific server versions. This can create additional complexity when handling requests.
  * Platform-specific analysis: When running native apps, you need enhanced observability for platform-specific metrics.


The introduction of EAS Hosting aims to address these limitations.
## Prerequisites
An Expo user account
EAS Hosting is available to anyone with an Expo account, regardless of whether you pay for EAS or use the Free plan. You can sign up at [expo.dev/signup](https://expo.dev/signup).
Paid subscribers can create more deployments, have more bandwidth, storage, requests, and may set up a custom domain. Learn more about different plans and benefits at [EAS pricing](https://expo.dev/pricing#host).
An Expo Router web project
If using an existing project, ensure that in your project's app config, the web output ([`expo.web.output`](https://docs.expo.dev/versions/latest/config/app#output)) is set to either `static` or `server` (single page apps are not supported on EAS Hosting).
Don't have a project yet? No problem. It's quick and easy to create a "Hello world" app that you can use with this guide.
Run the following command to create a new project:
Terminal
Copy
`- ``npx create-expo-app@latest my-app`
1
## Install the latest EAS CLI
EAS CLI is the command line app you will use to interact with EAS services from your terminal. To install it, run the command:
Terminal
Copy
`- ``npm install --global eas-cli`
You can also use the above command to check if a new version of EAS CLI is available. We encourage you to always stay up to date with the latest version.
> We recommend using `npm` instead of `yarn` for global package installations. You may alternatively use `npx eas-cli@latest`. Remember to use that instead of `eas` whenever it's called for in the documentation.
2
## Log in to your Expo account
If you are already signed in to an Expo account using Expo CLI, you can skip the steps described in this section. If you are not, run the following command to log in:
Terminal
Copy
`- ``eas login`
You can check whether you are logged in by running `eas whoami`.
3
## Prepare your project
In your app config file set [`expo.web.output`](https://docs.expo.dev/versions/latest/config/app#output) to either `static` or `server`.
  * `static`: Exports your Expo app to a [statically generated web app](https://docs.expo.dev/router/reference/static-rendering)
  * `server`: Supports [server functions](https://docs.expo.dev/guides/server-components#react-server-functions) and [API routes](https://docs.expo.dev/router/reference/api-routes) as well as the static pages for your website


> Don't worry if you're not sure which output mode you need, you can always change this value later and re-deploy.
4
### Export your app
You need to export your web project into a dist directory. To do this, run:
Terminal
Copy
`- ``npx expo export --platform web`
> Remember to re-run this command every time before deploying.
5
### Deploy your app
Now publish your website to EAS Hosting:
Terminal
Copy
`- ``eas deploy`
The first time you run this command, it will:
  1. Prompt you to connect an EAS project if you haven't done so yet
  2. Ask you to choose a preview subdomain name


> A preview subdomain name is a prefix used for the preview URL of your app. For example, if you choose `my-app` as your preview subdomain name, your preview URL would look something like this: `https://my-app--or1170q9ix.expo.app/`, and your production URL would be: `https://my-app.expo.app/`.
Once your deployment is complete, the CLI will output a preview URL for where your deployed app is accessible, as well as a link to the deployment details on the EAS Dashboard.

