---
url: https://docs.expo.dev/workflow/development-mode
title: https://docs.expo.dev/workflow/development-mode
date: 2025-04-30T17:17:56.179379
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Development and production modes
Learn how to run a project in development mode or production mode.
Your project will always run in either development or production mode. By default, running your project locally with `npx expo start` runs it in development mode, whereas a published project (with `eas update`), or any standalone app, will run in production mode.
Development mode includes useful warnings and gives you access to tools that make development and debugging easier. Production mode [minifies your code](https://docs.expo.dev/guides/customizing-metro#minification) and better represents the performance your app will have on end users' devices. Let's look at each of these modes in more detail and learn how you can switch between them.
## Development mode
React Native includes some very useful tools for development: remote JavaScript debugging in Chrome, live reload, hot reloading, and an element inspector similar to the beloved inspector you use in Chrome. If you want to see how to use those tools, see [Debugging](https://docs.expo.dev/debugging/runtime-issues).
Development mode also performs validations while your app is running to give you warnings. For example, if you're using a deprecated property or if you forgot to pass a required property into a component. The video below shows the Element Inspector and Performance Monitor in action on both Android Emulator and iOS Simulator:
> This comes at a cost. Your app runs slower in development mode. You can switch it on and off with the Expo CLI, see [Production mode](https://docs.expo.dev/workflow/development-mode#production-mode). When you switch it, close and re-open your app for the change to take effect. Any time you are testing your app's performance, make sure to disable development mode.
### View the developer menu
The menu gives access to a host of features that make development and debugging much easier. For more information on how to open it on Android and iOS, see [Developer menu](https://docs.expo.dev/debugging/tools#developer-menu).
## Production mode
Production mode is most useful for two things:
  * Testing your app's performance, as Development slows your app down considerably.
  * Catching bugs that only show up in production.


The easiest way to simulate how your project will run on end users' devices is with the command:
Terminal
Copy
`- ``npx expo start --no-dev --minify`
It runs the JavaScript of your app in production mode (which tells the Metro bundler to set the `__DEV__` environment variable to `false`, among a few other things). The `--minify` flag minifies your app. This flag also eliminates unnecessary data such as comments, formatting, and unused code. If you are getting an error or crash in your standalone app, running your project with this command can save you a lot of time in finding the root cause.
To completely compile your app for production see [Compiling Android](https://docs.expo.dev/more/expo-cli#compiling-android) and [Compiling iOS](https://docs.expo.dev/more/expo-cli#compiling-ios).

