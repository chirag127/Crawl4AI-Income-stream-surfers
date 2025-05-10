---
url: https://expo.dev/changelog/2023-12-20-2023-year-in-review
title: https://expo.dev/changelog/2023-12-20-2023-year-in-review
date: 2025-04-30T17:19:00.770486
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [Expo 2023: The year in review](https://expo.dev/changelog/2023-12-20-2023-year-in-review)
Dec 20, 2023 by
Jon Samp
2023 began with some audacious goals. We made a long list of new features and capabilities to build. Our goal, in general terms, was to make Expo a more helpful part of developer workflows.
In our all-hands last Thursday our [CEO, Charlie Cheever](https://x.com/ccheever?s=20), pulled up that original list and ran through the startling number of new features and capabilities we shipped. There were a few misses for sure. But not many. Our progress in 2023 is something we’re all proud of. And as a result of our work it’s now easier than ever to create and maintain a universal app with your team.
It’s instinctual to want to keep our momentum and run right through the holidays with our eyes on the horizon. And while we’re excited about what the future holds (starting with [SDK 50 in January](https://expo.dev/changelog/2023/12-12-sdk-50-beta)!), let’s take a moment to appreciate some of the highlights from 2023.
## [2023 Expo Accomplishments ](https://expo.dev/changelog/2023-12-20-2023-year-in-review#2023-expo-accomplishments)
The list of features and capabilities we shipped in 2023 is longer than a list of new AI companies. We won’t bore you with every line item. Let’s just focus on some of the stars:
### [Expo Orbit launched ](https://expo.dev/changelog/2023-12-20-2023-year-in-review#expo-orbit-launched)
In November we launched [Expo Orbit for macOS](https://expo.dev/changelog/2023/11-14-orbit-v1) to make it faster and easier to install and run builds from EAS or elsewhere, and to run Snack projects on simulators and physical devices. It has handy features like opening multiple simulators at once for quicker testing, and even opening Android emulators without audio, which will keep the music you’re listening to pitch perfect.
You can [download it](https://github.com/expo/orbit/releases) or install it with homebrew:
Terminal
Copy
`brew install expo-orbit`
### [Expo Router gets more powerful ](https://expo.dev/changelog/2023-12-20-2023-year-in-review#expo-router-gets-more-powerful)
[Evan Bacon](https://x.com/Baconbrix?s=20) and his team have been busy bringing the best routing concepts from the web to native iOS and Android apps with [Expo Router](https://docs.expo.dev/router/introduction/). Every file in the app directory automatically becomes a route in your mobile navigation, making it easier than ever to build, maintain, and scale your project.
This year we added a lot of new features:
  * tsconfig path support
  * [First-class support for build-time static generation on web](https://docs.expo.dev/router/reference/static-rendering/)
  * A `<Head />` component, which supports SSG on web and a ton of truly native functionality on iOS, like automatic handoff, Siri Context, and Quick Notes.
  * [CSS Support in Metro bundler for web](https://docs.expo.dev/guides/customizing-metro/)
  * [Direct debugging inside of VS Code](https://docs.expo.dev/debugging/tools/#debugging-with-vs-code)
  * [Support for universal server endpoints with API Routes](https://docs.expo.dev/router/reference/api-routes/).


The [Expo Router V3 Beta](https://blog.expo.dev/expo-router-v3-beta-is-now-available-eab52baf1e3e) opened recently, so check that out if you haven’t already.
### [EAS Build gets faster and easier to use ](https://expo.dev/changelog/2023-12-20-2023-year-in-review#eas-build-gets-faster-and-easier-to-use)
EAS Build is our hosted service for building app binaries for your Expo and React Native projects. In 2023 we made large strides on EAS Build’s feature set with several new performance and workflow improvements.
Here are some of the features we released this year:
  * We implemented [GitHub build triggers](https://docs.expo.dev/build/building-from-github/), which allows you to automatically build when you update your codebase on GitHub. For example, now you can push to main, and we can kick off a production build for you.
  * We improved build speed by 40% - 60% on average by making Apple Silicon default for our build workers.
  * [You can now download and view simulator builds](https://docs.expo.dev/build-reference/simulators/) from your team with the new `eas build:run` command.
  * When you add a new person to your team, we can now re-sign a development build with their credentials instead of kicking off an entirely new build. This takes about 90 seconds.
  * We now support customizing the build job process with a .yml file. This allows you to run unit tests or other processes during your build jobs.
  * Build logs are improved. We now suggest possible fixes to certain, often esoteric, errors inline in the build logs.

### [EAS Update matures ](https://expo.dev/changelog/2023-12-20-2023-year-in-review#eas-update-matures)
[EAS Update is our hosted service](https://docs.expo.dev/eas-update/introduction/) for shipping OTA bug fixes in between app store submissions. In 2023 we delivered literal millions of updates, learned a from our users, and shipped some key improvements:
  * We released [EAS Update rollouts](https://docs.expo.dev/eas-update/rollouts/), which allow you to ship a new update to a small percentage of users.
  * We also improved the expo-updates with a new JS API. It utilizes hooks to allow you to see the state of updates running and downloaded. With it, it’s also easier to trigger fetching and downloading an update at a specific time.
  * Better website support, which now shows all channels, branches, updates, and a new deployments dashboard which links shows the relationships between builds and compatible updates.

### [Appjs Conf 2023 ](https://expo.dev/changelog/2023-12-20-2023-year-in-review#appjs-conf-2023)
For both technical and human reasons this conference was a highlight of the year. It felt great to spend a few days surrounded by hundreds of the best React developers in the world.
At the conference we announced many new features and updates that help teams iterate faster and with more confidence. Here’s a nice excerpt from the keynote that Charlie and our CTO James Ide delivered on the big stage (You can watch all the talks from that conference [here](https://docs.expo.dev/additional-resources/#talks).):
Charlie Cheever at Appjs Conf
[Appjs Conf 2024](https://appjs.co/) begins accepting CFPs next month and you can still grab early bird ticket prices. We’d love to see you in Poland!
## [But wait, there’s more… ](https://expo.dev/changelog/2023-12-20-2023-year-in-review#but-wait-theres-more)
The engineering team at Expo builds and ships product with a combination of speed and quality that sometimes feels impossible. It’s part of the culture of the company. It’s a byproduct of the example our leaders and core members established back in the early Expo days.
It’s hard to pick a handful of highlights and exclude so much of the good work we shipped this year. So let’s take a look at just a few more meaningful 2023 accomplishments:
  * We shipped SDKs [48](https://blog.expo.dev/expo-sdk-48-ccb8302e231), [49](https://blog.expo.dev/expo-sdk-49-c6d398cdf740), and [50 (beta release)](https://expo.dev/changelog/2023/12-12-sdk-50-beta).
  * We shipped [Expo Modules API](https://docs.expo.dev/modules/overview/), which standardizes writing native modules.
  * You can now publish a preview of your app with EAS Update and a GitHub Action. We love scanning QR codes to see the preview of a PR.
  * We released a [VS Code theme](https://marketplace.visualstudio.com/items?itemName=expo.vscode-expo-theme).
  * Our website can do a lot more. We now have [improved dashboards](https://expo.dev/changelog/2023/12-13-eas-update-ui), tables, insights, search, notifications, and more.
  * [We now support SSO](https://docs.expo.dev/accounts/sso/).
  * We shipped a new [On Demand plan](https://expo.dev/pricing), which allows you to pay as you go.
  * You can see all the latest changes on [our changelog](https://expo.dev/changelog).

## [What to expect in 2024 ](https://expo.dev/changelog/2023-12-20-2023-year-in-review#what-to-expect-in-2024)
Thank you to all of the React, React Native, and Expo developers who helped us this year by testing and providing feedback on all the changes we made. Over 250 different developers made contributions in 2023. Your feedback and input meaningfully guide our product direction.
Our goal in 2023 was to improve our open source platform to allow any developer to create genuine native apps. Alongside it, we wanted to make major improvements to [our cloud services, EAS](https://expo.dev/eas), to help developers deliver their code to millions of users. We delivered on those goals.
Next year, we can’t wait to go even further. We’re thinking hard about how teams work together and test their changes before sending them to users. We’re also thinking about how developers can make premier universal experiences that include Android, iOS, and the web.
2024 is going to be a big year for speeding up iterations and making it easier for developers to understand how their apps are doing, react to issues, and consistently deliver the best user experience possible.
We look forward to your feedback and your support. And, as always, we can’t wait to see what you build.

