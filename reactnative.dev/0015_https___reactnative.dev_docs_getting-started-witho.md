---
url: https://reactnative.dev/docs/getting-started-without-a-framework
title: https://reactnative.dev/docs/getting-started-without-a-framework
date: 2025-05-10T21:31:28.923965
depth: 1
---

[Skip to main content](https://reactnative.dev/docs/getting-started-without-a-framework#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
**Platform support**
Android
iOS
macOS
TV
watchOS
Web
Windows
visionOS
If you have constraints that are not served well by a [Framework](https://reactnative.dev/architecture/glossary#react-native-framework), or you prefer to write your own Framework, you can create a React Native app without using a Framework.
To do so, you'll first need to [set up your environment](https://reactnative.dev/docs/set-up-your-environment). Once you're set up, continue with the steps below to create an application and start developing.
### Step 1: Creating a new application[​](https://reactnative.dev/docs/getting-started-without-a-framework#step-1-creating-a-new-application "Direct link to Step 1: Creating a new application")
> If you previously installed a global `react-native-cli` package, please remove it as it may cause unexpected issues:
> shell
> ```
npm uninstall -g react-native-cli @react-native-community/cli
```

You can use [React Native Community CLI](https://github.com/react-native-community/cli) to generate a new project. Let's create a new React Native project called "AwesomeProject":
shell
```
npx @react-native-community/cli@latest init AwesomeProject
```

This is not necessary if you are integrating React Native into an existing application, or if you've installed [Expo](https://docs.expo.dev/bare/installing-expo-modules/) in your project, or if you're adding Android support to an existing React Native project (see [Integration with Existing Apps](https://reactnative.dev/docs/integration-with-existing-apps)). You can also use a third-party CLI to set up your React Native app, such as [Ignite CLI](https://github.com/infinitered/ignite).
info
If you are having trouble with iOS, try to reinstall the dependencies by running:
  1. `cd ios` to navigate to the `ios` folder.
  2. `bundle install` to install [Bundler](https://bundler.io/)
  3. `bundle exec pod install` to install the iOS dependencies managed by CocoaPods.


#### [Optional] Using a specific version or template[​](https://reactnative.dev/docs/getting-started-without-a-framework#optional-using-a-specific-version-or-template "Direct link to \[Optional\] Using a specific version or template")
If you want to start a new project with a specific React Native version, you can use the `--version` argument:
shell
```
npx @react-native-community/cli@X.XX.X init AwesomeProject --version X.XX.X
```

You can also start a project with a custom React Native template with the `--template` argument, read more [here](https://github.com/react-native-community/cli/blob/main/docs/init.md#initializing-project-with-custom-template).
### Step 2: Start Metro[​](https://reactnative.dev/docs/getting-started-without-a-framework#step-2-start-metro "Direct link to Step 2: Start Metro")
[**Metro**](https://metrobundler.dev/) is the JavaScript build tool for React Native. To start the Metro development server, run the following from your project folder:
  * npm
  * Yarn


shell
```
npm start
```

shell
```
yarn start
```

note
If you're familiar with web development, Metro is similar to bundlers such as Vite and webpack, but is designed end-to-end for React Native. For instance, Metro uses [Babel](https://babel.dev/) to transform syntax such as JSX into executable JavaScript.
### Step 3: Start your application[​](https://reactnative.dev/docs/getting-started-without-a-framework#step-3-start-your-application "Direct link to Step 3: Start your application")
Let Metro Bundler run in its own terminal. Open a new terminal inside your React Native project folder. Run the following:
  * npm
  * Yarn


shell
```
npm run android
```

shell
```
yarn android
```

If everything is set up correctly, you should see your new app running in your Android emulator shortly.
This is one way to run your app - you can also run it directly from within Android Studio.
> If you can't get this to work, see the [Troubleshooting](https://reactnative.dev/docs/troubleshooting) page.
### Step 4: Modifying your app[​](https://reactnative.dev/docs/getting-started-without-a-framework#step-4-modifying-your-app "Direct link to Step 4: Modifying your app")
Now that you have successfully run the app, let's modify it.
  * Open `App.tsx` in your text editor of choice and edit some lines.
  * Press the `R` key twice or select `Reload` from the Dev Menu (`Ctrl` + `M`) to see your changes!


### That's it![​](https://reactnative.dev/docs/getting-started-without-a-framework#thats-it "Direct link to That's it!")
Congratulations! You've successfully run and modified your first barebone React Native app.
### Now what?[​](https://reactnative.dev/docs/getting-started-without-a-framework#now-what "Direct link to Now what?")
  * If you want to add this new React Native code to an existing application, check out the [Integration guide](https://reactnative.dev/docs/integration-with-existing-apps).
  * If you're curious to learn more about React Native, check out the [Introduction to React Native](https://reactnative.dev/docs/getting-started).


Is this page useful?

