---
url: https://expo.dev/changelog/2023-11-29-automatic-github-builds
title: https://expo.dev/changelog/2023-11-29-automatic-github-builds
date: 2025-04-30T17:18:39.068440
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [Speed up your development workflow with Automatic GitHub builds](https://expo.dev/changelog/2023-11-29-automatic-github-builds)
Nov 29, 2023 by
Juwan Wheatley
When you want to build a preview version of your app to test out some changes, it can be tedious to manually go through the process of running EAS CLI to build your app after pushing or pulling down the latest changes from your repository. You have to find the right branch or tag to pull down, install EAS CLI, log in, choose the right build profile, and run the build command locally.
With Automatic GitHub builds, we eliminate all of those manual steps. By setting up build triggers, your project is automatically built whenever you push updates to GitHub, ensuring that your latest builds are up to date with your codebase.
## [How to set up build triggers ](https://expo.dev/changelog/2023-11-29-automatic-github-builds#how-to-set-up-build-triggers)
The steps are simple. Just link a repository on expo.dev, add a build trigger, and push to your repository. If you've run a build on EAS before, this will be a smooth process. (If you haven't run a build you can learn how to [create your first build here](https://docs.expo.dev/build/setup/).)
You can customize build triggers for branches, pull requests, and Git tags. For example, running an iOS production build when `main` gets pushed or creating an Android development build when any pull request with a source branch matching `feature/*` gets updated.
We decided to develop and ship Automatic Github builds because we want developers focused on business logic and shipping beautiful applications, not developing and maintaining a complex CI/CD system.
This feature is now in preview for EAS subscribers, with general availability slated for 2024. There are many more improvements to come!
Learn more about how to get set up with our [GitHub builds guide](https://docs.expo.dev/build/building-from-github/#build-automatically-when-code-is-pushed-to-repository).

