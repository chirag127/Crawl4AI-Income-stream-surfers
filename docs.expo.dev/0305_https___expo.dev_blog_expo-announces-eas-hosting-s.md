---
url: https://expo.dev/blog/expo-announces-eas-hosting-service
title: https://expo.dev/blog/expo-announces-eas-hosting-service
date: 2025-04-30T17:18:15.264177
depth: 2
---

[All Posts](https://expo.dev/blog)
Share this post
# React Native Hosting with EAS: Deploy your server-driven Expo apps to the cloud
Product, Development•January 14, 2025•10 minute read
Phil Pluckthun
Engineering
Introducing EAS Hosting: the first ever end-to-end deployment solution for universal app development. 
From weather apps, and commerce websites, to AI-powered chat apps, most modern applications today need reliable servers. That's why **today we're introducing EAS Hosting** for instantly deploying and scaling universal API routes, React websites, and more!
## [The challenge of universal app deployment ](https://expo.dev/blog/expo-announces-eas-hosting-service#the-challenge-of-universal-app-deployment)
Many massive companies such as Netflix, Meta, and Apple use server-driven UI in their native apps. But building a server-driven application is extremely challenging and simply out of reach for most developers. Our goal with Expo Router has been to solve this problem and enable anyone to build and scale world-class server-driven apps for Android, iOS, and web using the same codebase.
To this end, we've introduced [API Routes that can be used to create server endpoints](https://docs.expo.dev/router/reference/api-routes/) for your app, [secure environment variables](https://docs.expo.dev/guides/environment-variables/), and static generation for web pages, all building toward [universal React Server Components](https://docs.expo.dev/guides/server-components/). While all these features work great on a local dev server, deployment has become more challenging.
There are many full-stack problems to consider when building a modern application. We've historically recommended deploying Expo websites and universal API routes to traditional hosting services that are focused only on websites. But hosting services for websites traditionally don’t integrate with the problems native apps face.
  * New versions of your servers may need to be deployed while new versions of your native app are being published to app stores.
  * Different versions of your native app may need to have their requests routed to different versions of your server.
  * Observability of servers for critical metrics, such as feature adoption by platform become more important for Expo native apps.


With [EAS Hosting](https://docs.expo.dev/eas/hosting/introduction/), in conjunction with EAS Workflows, we’re providing an end-to-end deployment solution that **just works across all platforms** , and stays working as you scale.
[Evan Bacon 🥓](https://twitter.com/Baconbrix/status/1879187492072800486)
[@Baconbrix](https://twitter.com/Baconbrix/status/1879187492072800486)
☁️ EAS Hosting is here! In addition to our fantastic native deployment, you can now push: ◆ Websites ◆ API Routes ◆ Environment variables Will be adding native support via [@expo](https://twitter.com/expo)'s React Server Components soon 🚀 Run `eas deploy` today! 
[590](https://twitter.com/intent/like?tweet_id=1879187492072800486)[Reply](https://twitter.com/intent/tweet?in_reply_to=1879187492072800486)Copy link
## [How to get started with EAS Hosting ](https://expo.dev/blog/expo-announces-eas-hosting-service#how-to-get-started-with-eas-hosting)
First, ensure you’re using the latest version of EAS CLI:
Terminal
Copy
`npm i -g eas-cli`
Then simply bundle your app with Expo CLI, then deploy your website and server code worldwide with a single EAS command and get a preview URL immediately.
Terminal
Copy
`npx expo export -p web ``eas deploy`
That's it! Your website and API routes are now live with a beautiful `*.expo.app` URL that you can share with anyone. (For an example Expo web deployment, visit: <https://bacon.expo.app>)
Add [environment variables](https://docs.expo.dev/eas/hosting/environment-variables/) to your `.env` file and these will securely reside on the server-side for use in API routes and React Server Functions, keeping them out of your client code.
By [visiting the EAS dashboard](https://expo.dev/accounts/%5Baccount%5D/projects/%5Bproject%5D/hosting), you can monitor your deployments and see helpful telemetry. Server errors are automatically aggregated and can be linked to for triaging!
Here's a comprehensive video demonstration of EAS Hosting that covers deployment, assigning aliases, using API routes, looking up request logs, managing environment variables, and automating deployments with Workflows:
EAS Hosting tutorial video## [The time for React Native Hosting is now ](https://expo.dev/blog/expo-announces-eas-hosting-service#the-time-for-react-native-hosting-is-now)
Today, EAS Workflows, EAS Build, EAS Submit, and EAS Update provide you with the tools you need to get a **native** Expo app built, tested, and delivered to your users’ devices via app stores.
As Expo’s feature set is expanding to include more capabilities which target servers or the web (such as API Routes, Expo for Web, and React Server Components) we can’t ignore the need for a new EAS service that allows you to get your apps to production, even if they make use of our newer server-side features.
As mentioned above, EAS Hosting provides you with a new service to deploy API routes for your Expo native apps and Expo web apps. This is the first of many steps toward building a platform that can support our future ambitions for server-side code and Web support for Expo.
> 🚧 Initially, we’re launching EAS Hosting as a Public Preview while we’re monitoring your feedback and usage patterns. We are confident in it scaling as it should, but some parts of EAS Hosting are still subject to changes as we’re iterating.
EAS Hosting expands our set of services to services to:
  * Deploying API routes, server functions, and server components to the cloud.
  * Building servers that can handle Expo’s future feature-specific requirements for advanced server-side features while also providing best of class debugging and metrics.


As a platform, EAS Hosting allows us to polish the development experience and capabilities of a hosting service that will support React Server Components natively, and will integrate well with Expo apps that make API calls to it.
You can already write server-side code in the same Expo codebase you’re already working in. With EAS Hosting, you’ll be able to deploy this logic alongside your app during your EAS build process and instantly gain access to logging and metrics for this server-side code.
## [What features will EAS Hosting support on day one? ](https://expo.dev/blog/expo-announces-eas-hosting-service#what-features-will-eas-hosting-support-on-day-one)
[Deploying an exported Expo web app](https://docs.expo.dev/eas/hosting/get-started/), either in `server` or `static` mode, is done with one command: `eas deploy`.
When setting up your project for EAS Hosting for the first time, you’ll pick a preview name and each deployment you create will subsequently get its own [Preview URL](https://docs.expo.dev/eas/hosting/deployments-and-aliases/). Afterwards, your deployment will immediately be available under a preview URL, such as `my-app--id.expo.app`
With a [paid plan](https://expo.dev/pricing#host), there are no limits to how many deployments you can create, and all deployments will remain accessible. This feature will be an important cornerstone in the future, when tying worker deployments to native apps, as it’ll allow you to deploy many versions of your API and tie them to your native apps’ released versions.
EAS Hosting [records runtime crashes, requests, and logs](https://docs.expo.dev/eas/hosting/api-routes/) and makes them available to you via the dashboard. From day one, you’ll have one of the best visibility and debugging experiences EAS has ever had.
Uncaught JavaScript runtime exceptions will be recorded and categorized by their error messages, and you’ll be able to view them per request or across your entire Hosting project.
With requests being recorded, we’re also offering a metrics view, which gives you a quick overview of how many requests your deployments are handling, where they’re coming from, and how long your deployment is taking to process them.
All four views of the data EAS Hosting tracks are available at launch — Crashes, Logs, Requests, and Metrics — and we’re actively working on expanding these views based on your feedback, and are working on specialized views for React Server Components.
## [EAS Hosting — under the hood and in the future ](https://expo.dev/blog/expo-announces-eas-hosting-service#eas-hosting-under-the-hood-and-in-the-future)
We’ve partnered with Cloudflare to build EAS Hosting on [Cloudflare’s Workers platform](https://workers.cloudflare.com/). This allows you to deploy your APIs to a serverless platform with exceptional performance, reliability, and without worrying about scale.
Under the hood, Cloudflare Workers use the [V8 JavaScript engine](https://www.cloudflare.com/en-gb/learning/serverless/glossary/what-is-chrome-v8/), which also powers Chromium and Node.js. Rather than running on individual virtual machines, applications deployed using EAS Hosting deploy to Workers using small V8 isolates, small scopes in the V8 engine, which spin up rapidly and limit their resources safely.
Cloudflare Workers were the natural choice for us to build on as they’re part of [WinterTC (”](https://wintercg.org/)[Technical Committee on Web-interoperable Server Runtimes](https://wintercg.org/)[”)](https://wintercg.org/). Code you write for EAS Hosting uses [Web-standard APIs](https://docs.expo.dev/eas/hosting/reference/worker-runtime/), such as `fetch` , `Request`, and `Response`, and will be compatible with most other JavaScript runtimes and hosting services.
While this means that some Node.js libraries won’t be compatible (at least, right now), some Node.js compatibility modules are available and will work as expected.
In the future, we’re looking to emulate this environment locally with a CLI command, so you can code confidently and know that your server will work when deployed to EAS Hosting.
We believe that the global edge-network that Cloudflare provides is a unique and natural platform to build future React Server Components-powered applications on and that it’ll give you more confidence when building Expo apps with new React framework features.
## [What’s next for EAS Hosting? ](https://expo.dev/blog/expo-announces-eas-hosting-service#whats-next-for-eas-hosting)
We’re thrilled to ship this preview of EAS Hosting today. This is the first ever end-to-end deployment solution for universal app development and we’re eager for everyone to test it and share their feedback.
As excited as we are about Hosting, we’re even more excited about what this unlocks for developers moving forward. Here’s what you can expect:
  * As we’re building out our support for [React Server Components](https://docs.expo.dev/guides/server-components/), EAS Hosting gives us a platform to grow alongside and be the easiest hosting service for your Expo applications, powered by React’s server-side capabilities.
  * We’re actively exploring adding more complex and non-standard features to worker deployments, that tie in more deeply with Cloudflare Worker’s ecosystem and the features offered by Cloudflare.
  * Going forward, we’ll improve Expo CLI’s emulation of our hosting platform, so you can write code and be confident it’s working identically and as intended when you’re testing it locally.


Thanks for reading the post and please give EAS Hosting a try. You can find its pricing on our [pricing page](https://expo.dev/pricing) — there is a free tier. Feel free to ask questions in our [Discord’s #eas-hosting channel](https://chat.expo.dev/) and report issues on the [expo/eas-cli repo](https://github.com/expo/eas-cli).
Developer trust is our top priority at Expo, we appreciate your patience as we sharpen this EAS Hosting preview into a solution for all apps built with Expo over the course of 2025!
EAS Hosting
Expo Router
Universal apps
API Routes
React Server Components
EAS
#### Table of Contents
[The challenge of universal app deployment](https://expo.dev/blog/expo-announces-eas-hosting-service#the-challenge-of-universal-app-deployment)[How to get started with EAS Hosting](https://expo.dev/blog/expo-announces-eas-hosting-service#how-to-get-started-with-eas-hosting)[The time for React Native Hosting is now](https://expo.dev/blog/expo-announces-eas-hosting-service#the-time-for-react-native-hosting-is-now)[What features will EAS Hosting support on day one?](https://expo.dev/blog/expo-announces-eas-hosting-service#what-features-will-eas-hosting-support-on-day-one)[EAS Hosting — under the hood and in the future](https://expo.dev/blog/expo-announces-eas-hosting-service#eas-hosting-under-the-hood-and-in-the-future)[What’s next for EAS Hosting?](https://expo.dev/blog/expo-announces-eas-hosting-service#whats-next-for-eas-hosting)
#### Related Blog Posts
[Beta: Universal React Server Components in Expo Router](https://expo.dev/blog/universal-react-server-components-developer-preview)[Convert your website into a native app with Expo DOM Components](https://expo.dev/blog/the-magic-of-expo-dom-components)[Why Expo is a great fit for new and existing React Native apps](https://expo.dev/blog/why-expo-is-a-great-fit-for-new-and-existing-react-native-apps)
Share this post
### Sign up for the Expo Newsletter
Sign up to receive a summary of new features, capabilities, content, and news about Expo and the React Native community.
### Create amazing apps, in record time
[Learn More](https://expo.dev/eas)

