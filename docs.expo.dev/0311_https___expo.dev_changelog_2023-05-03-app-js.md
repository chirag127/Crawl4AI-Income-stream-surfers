---
url: https://expo.dev/changelog/2023-05-03-app-js
title: https://expo.dev/changelog/2023-05-03-app-js
date: 2025-04-30T17:18:18.023273
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [App.js 2023](https://expo.dev/changelog/2023-05-03-app-js)
May 3, 2023 by
Jon Samp
Hundreds of React developers gathered to talk about the latest in web and mobile app development at App.js 2023 in Kraków, Poland. We’re thrilled to announce many new features and updates that will help you and your team iterate faster and with more confidence.
## [Continuous Native Generation (CNG) ](https://expo.dev/changelog/2023-05-03-app-js#continuous-native-generation-cng)
We’ve built tools to allow you to generate native code automatically. These features allow you continuously modify native code without manually editing native files.
### [Config plugins ](https://expo.dev/changelog/2023-05-03-app-js#config-plugins)
[Config plugins](https://docs.expo.dev/config-plugins/plugins-and-mods/) allow you to customize native Android and iOS projects when they are generated with `npx expo prebuild`. It is often useful to add properties in native config files, to copy assets to native projects, and for advanced configurations such as adding an app extension target.
### [Autolinking ](https://expo.dev/changelog/2023-05-03-app-js#autolinking)
[Expo Autolinking](https://docs.expo.dev/modules/autolinking/) is a mechanism that automates adding dependencies to manifest files (**build.gradle** on Android, **Podfile** for CocoaPods on iOS, **Package.swift** for SwiftPM on iOS). This automation helps native packages work out of the box without extra configuration.
### [Expo Modules API ](https://expo.dev/changelog/2023-05-03-app-js#expo-modules-api)
[Expo Modules API](https://docs.expo.dev/modules/overview/) allows you to write native code in a way that feels natural with minimal boilerplate that is also consistent on both platforms. It provides a set of APIs and utilities to improve the process of developing native modules for Expo and React Native and expand your app capabilities.
## [Build re-signing ](https://expo.dev/changelog/2023-05-03-app-js#build-re-signing)
The internal distribution flow allows developers to side load apps on their device. This flow is especially powerful with development builds that teams use to develop their apps together.
For the internal distribution flow to work, a build must be signed with everyone’s device credentials. When a new member joins the team or someone gets a new device, it requires uploading the device’s credentials and rebuilding the entire app, which can take time.
To make this flow faster, we now support build re-signing. Instead of rebuilding your entire project, we can re-sign an existing build with new device credentials. In general, this takes about a minute and a half to complete, no matter how large or complex your project is.
You can re-sign a build with `eas build:resign`.
## [Run review builds immediately ](https://expo.dev/changelog/2023-05-03-app-js#run-review-builds-immediately)
Developers create simulator and emulator builds of their projects to verify their code is running as expected. After running `eas build`, developers have to perform manual steps to load it on their computer’s simulator or emulator.
The `eas build` command now supports automating all the steps needed to get a build from EAS onto your simulator or emulator. There are two ways to get a build running fast:
  * At the end of the `eas build` process in your terminal, EAS CLI will prompt you to download and run the build on your computer.
  * You can also run `eas build:run`. This command allows you to choose any compatible build and run it in seconds. What’s more, this command can be run by anyone in your organization, which means once one person creates a build, everyone can run this command to get it running on their own computer quickly, without needing to rebuild.

## [Automated PR previews ](https://expo.dev/changelog/2023-05-03-app-js#automated-pr-previews)
Reviewing PRs takes time. Reviewers need to check out the branch, install the changes, and run the bundler to review the results. With EAS Update, you can now create PR previews automatically that will allow your teammates to scan a QR code and see your feature working on their device while they review your code.
With [expo-github-action](https://github.com/expo/expo-github-action#create-previews-on-prs), when you push a new commit to a branch, EAS Update will create an update on a corresponding EAS Update branch. Then, expo-github-action will comment on your PR with a QR code that deep links to a preview of your feature in Expo Go or in a development build.
[Learn more](https://docs.expo.dev/eas-update/github-actions/#publish-previews-on-pull-requests) with our EAS Update docs.
## [Large build workers ](https://expo.dev/changelog/2023-05-03-app-js#large-build-workers)
In early 2023, we converted our iOS build workers from Intel to Apple silicon workers. On average, this resulted in a 40% decrease in build times. While we are pleased with that result, some developers need even more speed.
Now, we support Apple silicon large workers. In a test of one build, we found that the large worker was 60% faster than an Intel worker and 40% faster than an Apple silicon medium worker (the new default).
To build your project faster, you can enable Apple silicon large workers with the following configuration in your project’s **eas.json** :
Code
Copy
```

"production":{
"resourceClass":"large"

```

[Learn more](https://docs.expo.dev/build-reference/eas-json/#resourceclass) about worker size configurations.
## [Link your GitHub repo with Expo ](https://expo.dev/changelog/2023-05-03-app-js#link-your-github-repo-with-expo)
To make building your project even faster, we now support linking your GitHub repo with your Expo project on expo.dev. This allows you to:
  * Kick off a build from [expo.dev](http://expo.dev/). This allows anyone on your team to kick off a build quickly, without needed to jump into the command line.
  * Kick off a build from a PR using a label. For example, adding a label named `eas-build-android:production` will kick off an Android build on the production build profile using the latest code on the current branch.


You can get started by going to [your project's GitHub settings](https://expo.dev/accounts/%5Baccount%5D/projects/%5Bproject%5D/github) and linking your GitHub account.
## [EAS Update rollouts ](https://expo.dev/changelog/2023-05-03-app-js#eas-update-rollouts)
EAS Update allows you to ship critical bug fixes and improvements to your end-users between app store releases. By default, published updates go to 100% of users running a compatible build. While this can get changes to your end users quickly, it also can be risky.
For developers who want more control, we now support percentage-based rollouts with EAS Update.
You can start a rollout by publishing an update to a new EAS Update branch with `eas update --branch [branch-name]`.
Then, you can start a rollout with `eas channel:rollout`. Once your rollout has started, you can run this command again to increase, decrease, or end the rollout.
[Learn more](https://docs.expo.dev/eas-update/rollouts/) with our EAS Update docs.
## [expo-updates JS API ](https://expo.dev/changelog/2023-05-03-app-js#expo-updates-js-api)
It’s now easier to control when end users check for updates. We built `@expo/use-updates` on top of the expo-updates library to allow you to apply updates at the perfect times.
Our APIs allow you to update your end user’s app after the app foregrounds with a UI affordance. It also allows you to mark certain updates as critical and to download and restart the app immediately. `@expo/use-updates` is incredibly flexible and can meet the needs of your app.
Learn more about `@expo/use-updates`.
## [Expo Router V2 ](https://expo.dev/changelog/2023-05-03-app-js#expo-router-v2)
Expo Router brings the best routing concepts from the web to native iOS and Android apps. Every file in the **app** directory automatically becomes a route in your mobile navigation, making it easier than ever to build, maintain, and scale your project.
### [Auto typed routes ](https://expo.dev/changelog/2023-05-03-app-js#auto-typed-routes)
`Link` components will now be fully typed with TypeScript automatically. Now, when typing in a route, your editor will now autocomplete the route for you.
### [tsconfig path support ](https://expo.dev/changelog/2023-05-03-app-js#tsconfig-path-support)
With Expo SDK 49, we’ll support tsconfig paths. You’ll get editor intellisense and autocomplete when importing with aliases. This feature also supports jump-to-definition, along with all other editor features you’d expect.
### [First-class support for build-time static generation on web ](https://expo.dev/changelog/2023-05-03-app-js#first-class-support-for-build-time-static-generation-on-web)
Now, you can obtain optimal static SEO for your website. Together with universal links, you can achieve universal SEO across your mobile apps and the web.
### [Expo Head ](https://expo.dev/changelog/2023-05-03-app-js#expo-head)
We’ve added a `<Head />` component that’s powered by React Async Helmet on web and has a custom native module on iOS. This enables standard head definitions in web with SSG and a ton of truly native functionality on iOS, like automatic handoff, Siri Context, and Quick Notes.
### [Lazy bundling ](https://expo.dev/changelog/2023-05-03-app-js#lazy-bundling)
We now support async routes, which enable substantially faster startup and incremental upgrades as errors on single pages won't take down all other pages.
### [CSS support in Metro Bundler for web ](https://expo.dev/changelog/2023-05-03-app-js#css-support-in-metro-bundler-for-web)
You can now write standard CSS for your Expo websites, in addition to all of the following tools:
  * SASS/SCSS
  * CSS Modules
  * PostCSS
  * Tailwind
  * Global & External CSS
  * Hot Module Reloading
  * Mocking on native
  * Static Extraction for SSG


All of this is powered by the Rust-based lightningcss.
[Learn more](https://github.com/expo/router) about Expo Router.
## [Direct debugging inside VS Code ](https://expo.dev/changelog/2023-05-03-app-js#direct-debugging-inside-vs-code)
We are excited to announce vscode-expo v1.0.0, which now supports debugging Expo apps directly inside VS Code. This means you can set breakpoints, inspect variables, and step through your code without leaving your editor. You'll be able to:
  * Set breakpoints in your code
  * Inspect variables
  * Execute arbitrary code in the console
  * Inspect network requests made by your project


[Learn more](https://github.com/expo/vscode-expo) about `vscode-expo`.

