---
url: https://docs.expo.dev/bare/overview
title: https://docs.expo.dev/bare/overview
date: 2025-04-30T17:12:45.557687
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Overview of using Expo with existing React Native apps
Learn how to use Expo tools and services with existing React Native apps.
If you have a React Native app that doesn't use any Expo tools, you might be wondering what Expo can provide for you, why you might want to use Expo tools and services, and how to get started.
All tools and services provided by Expo work great in any React Native app.
You can use [EAS](https://docs.expo.dev/eas) to get quickly set up with a professional CI/CD workflow for building, reviewing, deploying, and updating your apps. [Expo CLI](https://docs.expo.dev/more/expo-cli) provides the best command-line experience for working with React Native. The [Expo SDK](https://docs.expo.dev/versions/latest) is an extended standard library for React Native. It gives developers high-quality, well-maintained native libraries that use consistent API conventions to make them easier to learn and use.
If you've ever written a native module for React Native, you'll be surprised how much easier it is to build and maintain modules with the idiomatic Swift and Kotlin DSL provided by the [Expo Modules API](https://docs.expo.dev/modules/overview).
There's so much more to explore, and the links below will help you to explore the options available to you.
## Incremental adoption steps
Below are four suggested phases of incremental adoption. These phases generally progress from quick changes to improve developer experience, to more significant workflow and codebase optimizations.
Only the first phase — prerequisites — is required by other phases. After following its instructions, you can skip to the tools and services that are most relevant to your goals in adopting Expo.
### Prerequisites
These first steps are required to later adopt Expo tools and services:
[Install Expo modulesTo unlock Expo capabilities, you need to install the `expo` package in your existing React Native project. This guide provides both automated and manual installation steps.](https://docs.expo.dev/bare/installing-expo-modules) [Use Expo CLIMigration to Expo CLI is a drop-in replacement for `@react-native-community/cli`. It provides full compatibility with all Expo tools and services. This guide explains the benefits and provides compilation commands to start your development server after installing`expo` package.](https://docs.expo.dev/bare/using-expo-cli)
### Quick wins
The following helps improving development experience and requires configuration:
[Use Expo SDKUse one of the many libraries provided by the Expo SDK, an extensive set of libraries that provide access to native APIs.](https://docs.expo.dev/versions) [Install expo-dev-client`expo-dev-client` provides access to Expo Go-style app launcher interface into your debug app variants. Learn how to install and configure it in your existing React Native project.](https://docs.expo.dev/bare/install-dev-builds-in-bare) [Write native modulesUse the Expo Modules API to write native modules using Swift and Kotlin.](https://docs.expo.dev/modules/overview) [Native project upgrade helperView file-by-file diffs of all the changes you need to make to your native projects to upgrade them to the next Expo SDK and React Native version.](https://docs.expo.dev/bare/upgrade)
### New workflows
Once your app has `expo` package installed, you can submit your app to app stores with a single command or update configure `expo-updates` library to manage remote updates to you app's code:
[App distributionBuild and submit your app to app stores with a single command.](https://docs.expo.dev/distribution/introduction) [Install expo-updatesLearn how to install and configure `expo-updates` to manage remote updates and enable PR previews.](https://docs.expo.dev/bare/installing-updates)
### New mindsets
The following helps with your project's long term maintainability, native code maintenance, and easier upgrades:
[Adopt PrebuildLearn how to simplify maintaining your native projects by generating them on demand from configuration.](https://docs.expo.dev/guides/adopting-prebuild) [Expo RouterExpo Router is a file-based routing library that offers advantages such as organized navigation hierarchy, automatic deep linking support, and more.](https://docs.expo.dev/router/introduction)
## Common questions
How long will it take to adopt Expo in my existing React Native project?
Adopting Expo doesn't have to be done in one step. You can start with the _quick wins_ and then move on to more complex parts. You can also pick and choose which features you want to adopt based on what is most helpful for your project.
What will I gain from using Expo in my React Native app?
Adopting Expo tools in your existing React Native app can help you develop faster with the [Expo SDK](https://docs.expo.dev/versions/latest), streamline native code maintenance and upgrades with [CNG](https://docs.expo.dev/workflow/continuous-native-generation), deploy faster with [EAS Update](https://docs.expo.dev/eas-update/introduction), and more.
Who uses Expo?
Expo is used by top companies worldwide that serve millions of end users. For more information, see our [Expo showcase](https://expo.dev/customers).
What impact will adopting Expo have on my app's size?
The `expo` package has a small footprint since it only includes a minimal set of modules required in every app with autolinking infrastructure and other Expo SDK libraries that are built-in. For more information on how to determine the actual size of your app, see [Understanding app size](https://docs.expo.dev/distribution/app-size).
Why did React Native recommend using Expo?
Most React Native developers solve common problems when building an app, such as implementing navigation, accessing Native APIs, upgrading to new versions, and more. This requires using a specific set of tools and libraries to build and maintain your app — which means you are creating your own framework.
Expo solves these problems by providing a set of primitives and helping you (the developer) to focus on building your app. It also offers tools to iterate faster in development. For more information, see [Why React Native recommends using a framework](https://reactnative.dev/blog/2024/06/25/use-a-framework-to-build-react-native-apps).
Do I have to get rid of my native projects to use Expo?
By default, Expo projects created with `create-expo-app` use [Continuous Native Generation (CNG)](https://docs.expo.dev/workflow/continuous-native-generation) and do not contain android and ios native directories. If you incrementally adopt Expo in your existing React Native app, you don't have to remove these directories. You can use `npx expo run:[android|ios]` as an alternative to commands offered by `@react-native-community/cli` to compile your app locally and keep the configuration of your native projects.
I use CodePush. Can I continue using it with Expo?
CodePush will be retired in March 2025 and is incompatible with React Native's New Architecture, so, in the long run, we recommend switching to EAS Update to manage remote updates to your app's code. However, you can start using Expo tools in your CodePush enabled app today, including the Expo SDK, Expo CLI, EAS Build, and more.
Do I have to build with EAS?
[Expo Application Services (EAS)](https://docs.expo.dev/eas) are deeply integrated cloud services for Expo and React Native apps that provide tools to build, test, and deploy your app.
Although we recommend using EAS for a smooth collaboration with your teammates and fast distribution, you can compile your app locally, on your CI, or any other way you prefer.
Can I install third-party native libraries in my code?
Yes, you can install and use third-party libraries that require native projects (android and ios) configuration or provides a [config plugin](https://docs.expo.dev/config-plugins/introduction) with [development builds](https://docs.expo.dev/workflow/overview#development-builds). See [Using Third-Party libraries](https://docs.expo.dev/workflow/using-libraries#third-party-libraries) for more information.
I use React Navigation. Do I have to use Expo Router?
You can continue using any navigation library in your project. However, we recommend using Expo Router for all the benefits [described here](https://docs.expo.dev/router/introduction).

