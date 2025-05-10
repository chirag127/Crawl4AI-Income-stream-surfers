---
url: https://reactnative.dev/docs/0.71/environment-setup
title: https://reactnative.dev/docs/0.71/environment-setup
date: 2025-05-10T21:28:54.586884
depth: 1
---

[Skip to main content](https://reactnative.dev/docs/0.71/environment-setup#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
This is documentation for React Native **0.71** , which is no longer in active development.
For up-to-date documentation, see the (0.79).
Version: 0.71
This page will help you install and build your first React Native app.
**If you are new to mobile development** , the easiest way to get started is with Expo Go. Expo is a set of tools and services built around React Native and, while it has many [features](https://docs.expo.dev), the most relevant feature for us right now is that it can get you writing a React Native app within minutes. You will only need a recent version of Node.js and a phone or emulator. If you'd like to try out React Native directly in your web browser before installing any tools, you can try out [Snack](https://snack.expo.dev/).
**If you are already familiar with mobile development** , you may want to use React Native CLI. It requires Xcode or Android Studio to get started. If you already have one of these tools installed, you should be able to get up and running within a few minutes. If they are not installed, you should expect to spend about an hour installing and configuring them.
  * Expo Go Quickstart
  * React Native CLI Quickstart


Run the following command to create a new React Native project called "AwesomeProject":
  * npm
  * Yarn


shell
```
npx create-expo-app AwesomeProjectcd AwesomeProjectnpx expo start
```

shell
```
yarn create expo-app AwesomeProjectcd AwesomeProjectyarn expo start
```

This will start a development server for you.
## Running your React Native application
Install the [Expo Go](https://expo.dev/client) app on your iOS or Android phone and connect to the same wireless network as your computer. On Android, use the Expo Go app to scan the QR code from your terminal to open your project. On iOS, use the built-in QR code scanner of the default iOS Camera app.
### Modifying your app
Now that you have successfully run the app, let's modify it. Open `App.js` in your text editor of choice and edit some lines. The application should reload automatically once you save your changes.
### That's it!
Congratulations! You've successfully run and modified your first React Native app.
## Now what?
Expo also has [docs](https://docs.expo.dev) you can reference if you have questions specific to the tool. You can also ask for help on the [Expo Discord](https://chat.expo.dev).
If you have a problem with Expo, before creating a new issue, please see if there's an existing issue about it in the [Expo issues](https://github.com/expo/expo/issues).
If you're curious to learn more about React Native, check out the [Introduction to React Native](https://reactnative.dev/docs/0.71/getting-started).
### Running your app on a simulator or virtual device
Expo Go allows you to run your React Native app on a physical device without installing iOS and Android native SDKs. If you want to run your app on the iOS Simulator or an Android Virtual Device, please refer to the instructions for "React Native CLI Quickstart" to learn how to install Xcode or set up your Android development environment.
Once you've set these up, you can launch your app on an Android Virtual Device by running `npm run android`, or on the iOS Simulator by running `npm run ios` (macOS only).
### Caveats
The Expo Go app is a great tool to get started — it exists to help developers quickly get projects off the ground, to experiment with ideas (such as on [Snack](https://snack.expo.dev/)) and share their work with minimal friction. Expo Go makes this possible by including a feature-rich native runtime made up of every module in the [Expo SDK](https://docs.expo.dev/versions/latest/), so all you need to do to use a module is install the package with `npx expo install` and reload your app.
The tradeoff is that the Expo Go app does not allow you to add custom native code — you can only use native modules built into the Expo SDK. There are many great libraries available outside of the Expo SDK, and you may even want to build your own native library. You can leverage these libraries with [development builds](https://docs.expo.dev/develop/development-builds/introduction/), or by using ["prebuild"](https://docs.expo.dev/workflow/prebuild/) to generate the native projects, or both. [Learn more about adding native code to projects created with `create-expo-app`](https://docs.expo.dev/workflow/customizing/).
`create-expo-app` configures your project to use the most recent React Native version that is supported by the Expo SDK. The Expo Go app usually gains support for a given React Native version with new SDK versions (released quarterly). You can check [this document](https://docs.expo.dev/versions/latest/#each-expo-sdk-version-depends-on-a) to find out what versions are supported.
If you're integrating React Native into an existing project, [you can use the Expo SDK](https://docs.expo.dev/bare/installing-expo-modules/) and [development builds](https://docs.expo.dev/develop/development-builds/introduction/), but you will need to set up a native development environment. Select "React Native CLI Quickstart" above for instructions on configuring a native build environment for React Native.
Follow these instructions if you need to build native code in your project. For example, if you are integrating React Native into an existing application, or if you ran "prebuild" from Expo to generate your project's native code, you'll need this section.
The instructions are a bit different depending on your development operating system, and whether you want to start developing for iOS or Android. If you want to develop for both Android and iOS, that's fine - you can pick one to start with, since the setup is a bit different.
#### Development OS[​](https://reactnative.dev/docs/0.71/environment-setup#development-os "Direct link to Development OS")
  * macOS
  * Windows
  * Linux


#### Target OS[​](https://reactnative.dev/docs/0.71/environment-setup#target-os "Direct link to Target OS")
  * Android
  * iOS


## Installing dependencies[​](https://reactnative.dev/docs/0.71/environment-setup#installing-dependencies "Direct link to Installing dependencies")
You will need Node, Watchman, the React Native command line interface, a JDK, and Android Studio.
While you can use any editor of your choice to develop your app, you will need to install Android Studio in order to set up the necessary tooling to build your React Native app for Android.
### Node & Watchman
We recommend installing Node and Watchman using [Homebrew](http://brew.sh/). Run the following commands in a Terminal after installing Homebrew:
shell
```
brew installnodebrew install watchman
```

If you have already installed Node on your system, make sure it is Node 14 or newer.
[Watchman](https://facebook.github.io/watchman) is a tool by Facebook for watching changes in the filesystem. It is highly recommended you install it for better performance.
### Java Development Kit
We recommend installing the OpenJDK distribution called Azul **Zulu** using [Homebrew](http://brew.sh/). Run the following commands in a Terminal after installing Homebrew:
shell
```
brew install--cask zulu@11# Get path to where cask was installed to double-click installerbrew info --cask zulu@11
```

After you install the JDK, update your `JAVA_HOME` environment variable. If you used above steps, JDK will likely be at `/Library/Java/JavaVirtualMachines/zulu-11.jdk/Contents/Home`
The Zulu OpenJDK distribution offers JDKs for **both Intel and M1 Macs**. This will make sure your builds are faster on M1 Macs compared to using an Intel-based JDK.
If you have already installed JDK on your system, we recommend JDK 11. You may encounter problems using higher JDK versions.
### Android development environment
Setting up your development environment can be somewhat tedious if you're new to Android development. If you're already familiar with Android development, there are a few things you may need to configure. In either case, please make sure to carefully follow the next few steps.
#### 1. Install Android Studio
[Download and install Android Studio](https://developer.android.com/studio/index.html). While on Android Studio installation wizard, make sure the boxes next to all of the following items are checked:
  * `Android SDK`
  * `Android SDK Platform`
  * `Android Virtual Device`


Then, click "Next" to install all of these components.
> If the checkboxes are grayed out, you will have a chance to install these components later on.
Once setup has finalized and you're presented with the Welcome screen, proceed to the next step.
#### 2. Install the Android SDK
Android Studio installs the latest Android SDK by default. Building a React Native app with native code, however, requires the `Android 13 (Tiramisu)` SDK in particular. Additional Android SDKs can be installed through the SDK Manager in Android Studio.
To do that, open Android Studio, click on "More Actions" button and select "SDK Manager".
> The SDK Manager can also be found within the Android Studio "Settings" dialog, under **Languages & Frameworks** → **Android SDK**.
Select the "SDK Platforms" tab from within the SDK Manager, then check the box next to "Show Package Details" in the bottom right corner. Look for and expand the `Android 13 (Tiramisu)` entry, then make sure the following items are checked:
  * `Android SDK Platform 33`
  * `Intel x86 Atom_64 System Image` or `Google APIs Intel x86 Atom System Image` or (for Apple M1 Silicon) `Google APIs ARM 64 v8a System Image`


Next, select the "SDK Tools" tab and check the box next to "Show Package Details" here as well. Look for and expand the "Android SDK Build-Tools" entry, then make sure that `33.0.0` is selected.
Finally, click "Apply" to download and install the Android SDK and related build tools.
#### 3. Configure the ANDROID_HOME environment variable
The React Native tools require some environment variables to be set up in order to build apps with native code.
Add the following lines to your `~/.zprofile` or `~/.zshrc` (if you are using `bash`, then `~/.bash_profile` or `~/.bashrc`) config file:
shell
```
exportANDROID_HOME=$HOME/Library/Android/sdkexportPATH=$PATH:$ANDROID_HOME/emulatorexportPATH=$PATH:$ANDROID_HOME/platform-tools
```

Run `source ~/.zprofile` (or `source ~/.bash_profile` for `bash`) to load the config into your current shell. Verify that ANDROID_HOME has been set by running `echo $ANDROID_HOME` and the appropriate directories have been added to your path by running `echo $PATH`.
> Please make sure you use the correct Android SDK path. You can find the actual location of the SDK in the Android Studio "Settings" dialog, under **Languages & Frameworks** → **Android SDK**.
### React Native Command Line Interface
React Native has a built-in command line interface. Rather than install and manage a specific version of the CLI globally, we recommend you access the current version at runtime using `npx`, which ships with Node.js. With `npx react-native <command>`, the current stable version of the CLI will be downloaded and executed at the time the command is run.
## Creating a new application
> If you previously installed a global `react-native-cli` package, please remove it as it may cause unexpected issues:
> shell
> ```
npm uninstall -g react-native-cli @react-native-community/cli
```

React Native has a built-in command line interface, which you can use to generate a new project. You can access it without installing anything globally using `npx`, which ships with Node.js. Let's create a new React Native project called "AwesomeProject":
shell
```
npx react-native@latest init AwesomeProject
```

This is not necessary if you are integrating React Native into an existing application, or if you've installed [Expo](https://docs.expo.dev/bare/installing-expo-modules/) in your project, or if you're adding Android support to an existing React Native project (see [Integration with Existing Apps](https://reactnative.dev/docs/0.71/integration-with-existing-apps)). You can also use a third-party CLI to init your React Native app, such as [Ignite CLI](https://github.com/infinitered/ignite).
### [Optional] Using a specific version or template
If you want to start a new project with a specific React Native version, you can use the `--version` argument:
shell
```
npx react-native@X.XX.X init AwesomeProject --version X.XX.X
```

You can also start a project with a custom React Native template with the `--template` argument.
## Preparing the Android device
You will need an Android device to run your React Native Android app. This can be either a physical Android device, or more commonly, you can use an Android Virtual Device which allows you to emulate an Android device on your computer.
Either way, you will need to prepare the device to run Android apps for development.
### Using a physical device
If you have a physical Android device, you can use it for development in place of an AVD by plugging it in to your computer using a USB cable and following the instructions [here](https://reactnative.dev/docs/0.71/running-on-device).
### Using a virtual device
If you use Android Studio to open `./AwesomeProject/android`, you can see the list of available Android Virtual Devices (AVDs) by opening the "AVD Manager" from within Android Studio. Look for an icon that looks like this:
If you have recently installed Android Studio, you will likely need to [create a new AVD](https://developer.android.com/studio/run/managing-avds.html). Select "Create Virtual Device...", then pick any Phone from the list and click "Next", then select the **Tiramisu** API Level 33 image.
Click "Next" then "Finish" to create your AVD. At this point you should be able to click on the green triangle button next to your AVD to launch it, then proceed to the next step.
## Running your React Native application
### Step 1: Start Metro
First, you will need to start Metro, the JavaScript bundler that ships with React Native. Metro "takes in an entry file and various options, and returns a single JavaScript file that includes all your code and its dependencies."—[Metro Docs](https://metrobundler.dev/docs/concepts)
To start Metro, run `npx react-native start` inside your React Native project folder:
shell
```
npx react-native start
```

`react-native start` starts Metro Bundler.
> If you use the Yarn package manager, you can use `yarn` instead of `npx` when running React Native commands inside an existing project.
> If you're familiar with web development, Metro is a lot like webpack—for React Native apps. Unlike Kotlin or Java, JavaScript isn't compiled—and neither is React Native. Bundling isn't the same as compiling, but it can help improve startup performance and translate some platform-specific JavaScript into more widely supported JavaScript.
### Step 2: Start your application
Let Metro Bundler run in its own terminal. Open a new terminal inside your React Native project folder. Run the following:
shell
```
npx react-native run-android
```

If everything is set up correctly, you should see your new app running in your Android emulator shortly.
`npx react-native run-android` is one way to run your app - you can also run it directly from within Android Studio.
> If you can't get this to work, see the [Troubleshooting](https://reactnative.dev/docs/0.71/troubleshooting) page.
### Modifying your app
Now that you have successfully run the app, let's modify it.
  * Open `App.tsx` in your text editor of choice and edit some lines.
  * Press the `R` key twice or select `Reload` from the Developer Menu (`⌘M`) to see your changes!


### That's it!
Congratulations! You've successfully run and modified your first React Native app.
## Now what?
  * If you want to add this new React Native code to an existing application, check out the [Integration guide](https://reactnative.dev/docs/0.71/integration-with-existing-apps).


If you're curious to learn more about React Native, check out the [Introduction to React Native](https://reactnative.dev/docs/0.71/getting-started).
## Installing dependencies[​](https://reactnative.dev/docs/0.71/environment-setup#installing-dependencies "Direct link to Installing dependencies")
You will need Node, Watchman, the React Native command line interface, a Ruby version manager, Xcode and CocoaPods.
While you can use any editor of your choice to develop your app, you will need to install Xcode in order to set up the necessary tooling to build your React Native app for iOS.
### Node & Watchman[​](https://reactnative.dev/docs/0.71/environment-setup#node--watchman "Direct link to Node & Watchman")
We recommend installing Node and Watchman using [Homebrew](http://brew.sh/). Run the following commands in a Terminal after installing Homebrew:
shell
```
brew installnodebrew install watchman
```

If you have already installed Node on your system, make sure it is Node 14 or newer.
[Watchman](https://facebook.github.io/watchman) is a tool by Facebook for watching changes in the filesystem. It is highly recommended you install it for better performance.
### Ruby[​](https://reactnative.dev/docs/0.71/environment-setup#ruby "Direct link to Ruby")
[Ruby](https://www.ruby-lang.org/en/) is a general-purpose programming language. React Native uses in some scripts related to the iOS dependency management. As every programming language, there are different versions of Ruby that have been developed during the years.
React Native uses a `.ruby-version` file to make sure that your version of Ruby is aligned with what is needed. Currently, macOS 13.2 is shipped with Ruby 2.6.10, which is **not** what is required by this version of React Native (2.7.6). Our suggestion is to install a Ruby version manager and to install the proper version of Ruby in your system.
Some common Ruby version manager are:
  * [asdf-vm](https://github.com/asdf-vm) with the [asdf-ruby](https://github.com/asdf-vm/asdf-ruby) plugin


To check what is your current version of Ruby, you can run this command:
```
ruby --version
```

React Native uses [this version](https://github.com/facebook/react-native/blob/v0.71.3/.ruby-version) of Ruby. You can also find which version your specific project needs in the `.ruby-version` file at root of your RN project.
### Ruby's Bundler[​](https://reactnative.dev/docs/0.71/environment-setup#rubys-bundler "Direct link to Ruby's Bundler")
Ruby uses the concept of **gems** to handle its own dependencies. You can think of a gem as a package in NPM, a formula in Homebrew or a single pod in CocoaPods.
Ruby's [Bundler](https://bundler.io/) is a Ruby gem that helps managing the Ruby dependencies of your project. We need Ruby to install CocoaPods and using Bundler will make sure that all the dependencies are aligned and that the project works properly.
If you want to learn more about why we need this tool, you can read [this article](https://bundler.io/guides/rationale.html#bundlers-purpose-and-rationale).
### Xcode[​](https://reactnative.dev/docs/0.71/environment-setup#xcode "Direct link to Xcode")
Please use the **latest version** of Xcode.
The easiest way to install Xcode is via the [Mac App Store](https://itunes.apple.com/us/app/xcode/id497799835?mt=12). Installing Xcode will also install the iOS Simulator and all the necessary tools to build your iOS app.
#### Command Line Tools[​](https://reactnative.dev/docs/0.71/environment-setup#command-line-tools "Direct link to Command Line Tools")
You will also need to install the Xcode Command Line Tools. Open Xcode, then choose "Preferences..." from the Xcode menu. Go to the Locations panel and install the tools by selecting the most recent version in the Command Line Tools dropdown.
#### Installing an iOS Simulator in Xcode[​](https://reactnative.dev/docs/0.71/environment-setup#installing-an-ios-simulator-in-xcode "Direct link to Installing an iOS Simulator in Xcode")
To install a simulator, open **Xcode > Preferences...** and select the **Components** tab. Select a simulator with the corresponding version of iOS you wish to use.
If you are using Xcode version 14.0 or greater to install a simulator, open **Xcode > Settings > Platforms** tab, then click "+" icon and select **iOS…** option.
#### CocoaPods[​](https://reactnative.dev/docs/0.71/environment-setup#cocoapods "Direct link to CocoaPods")
[CocoaPods](https://cocoapods.org/) is one of the dependency management system available for iOS. It is built with Ruby and you can install it using the version of Ruby you configured with in the previous steps.
For more information, please visit [CocoaPods Getting Started guide](https://guides.cocoapods.org/using/getting-started.html).
### React Native Command Line Interface[​](https://reactnative.dev/docs/0.71/environment-setup#react-native-command-line-interface "Direct link to React Native Command Line Interface")
React Native has a built-in command line interface. Rather than install and manage a specific version of the CLI globally, we recommend you access the current version at runtime using `npx`, which ships with Node.js. With `npx react-native <command>`, the current stable version of the CLI will be downloaded and executed at the time the command is run.
## Creating a new application[​](https://reactnative.dev/docs/0.71/environment-setup#creating-a-new-application "Direct link to Creating a new application")
> If you previously installed a global `react-native-cli` package, please remove it as it may cause unexpected issues:
> shell
> ```
npm uninstall -g react-native-cli @react-native-community/cli
```

You can use React Native's built-in command line interface to generate a new project. Let's create a new React Native project called "AwesomeProject":
shell
```
npx react-native@latest init AwesomeProject
```

This is not necessary if you are integrating React Native into an existing application, or if you've installed [Expo](https://docs.expo.dev/bare/installing-expo-modules/) in your project, or if you're adding iOS support to an existing React Native project (see [Integration with Existing Apps](https://reactnative.dev/docs/0.71/integration-with-existing-apps)). You can also use a third-party CLI to init your React Native app, such as [Ignite CLI](https://github.com/infinitered/ignite).
info
If you are having trouble with iOS, try to reinstall the dependencies by running:
  1. `cd ios` to navigate to the
  2. `bundle install` to install Bundler 
    1. If needed: install a [Ruby Version Manager](https://reactnative.dev/docs/0.71/environment-setup#ruby) and update the Ruby version
  3. `bundle exec pod install` to install the iOS dependencies.


### [Optional] Using a specific version or template[​](https://reactnative.dev/docs/0.71/environment-setup#optional-using-a-specific-version-or-template "Direct link to \[Optional\] Using a specific version or template")
If you want to start a new project with a specific React Native version, you can use the `--version` argument:
shell
```
npx react-native@X.XX.X init AwesomeProject --version X.XX.X
```

You can also start a project with a custom React Native template with the `--template` argument.
> **Note** If the above command is failing, you may have old version of `react-native` or `react-native-cli` installed globally on your pc. Try uninstalling the cli and run the cli using `npx`.
### [Optional] Configuring your environment[​](https://reactnative.dev/docs/0.71/environment-setup#optional-configuring-your-environment "Direct link to \[Optional\] Configuring your environment")
Starting from React Native version 0.69, it is possible to configure the Xcode environment using the `.xcode.env` file provided by the template.
The `.xcode.env` file contains an environment variable to export the path to the `node` executable in the `NODE_BINARY` variable. This is the **suggested approach** to decouple the build infrastructure from the system version of `node`. You should customize this variable with your own path or your own `node` version manager, if it differs from the default.
On top of this, it's possible to add any other environment variable and to source the `.xcode.env` file in your build script phases. If you need to run script that requires some specific environment, this is the **suggested approach** : it allows to decouple the build phases from a specific environment.
## Running your React Native application[​](https://reactnative.dev/docs/0.71/environment-setup#running-your-react-native-application "Direct link to Running your React Native application")
### Step 1: Start Metro[​](https://reactnative.dev/docs/0.71/environment-setup#step-1-start-metro "Direct link to Step 1: Start Metro")
First, you will need to start Metro, the JavaScript bundler that ships with React Native. Metro "takes in an entry file and various options, and returns a single JavaScript file that includes all your code and its dependencies."—[Metro Docs](https://metrobundler.dev/docs/concepts)
To start Metro, run `npx react-native start` inside your React Native project folder:
shell
```
npx react-native start
```

`react-native start` starts Metro Bundler.
> If you use the Yarn package manager, you can use `yarn` instead of `npx` when running React Native commands inside an existing project.
> If you're familiar with web development, Metro is a lot like webpack—for React Native apps. Unlike Swift or Objective-C, JavaScript isn't compiled—and neither is React Native. Bundling isn't the same as compiling, but it can help improve startup performance and translate some platform-specific JavaScript into more widely supported JavaScript.
### Step 2: Start your application[​](https://reactnative.dev/docs/0.71/environment-setup#step-2-start-your-application "Direct link to Step 2: Start your application")
Let Metro Bundler run in its own terminal. Open a new terminal inside your React Native project folder. Run the following:
shell
```
npx react-native run-ios
```

You should see your new app running in the iOS Simulator shortly.
`npx react-native run-ios` is one way to run your app. You can also run it directly from within Xcode.
> If you can't get this to work, see the [Troubleshooting](https://reactnative.dev/docs/0.71/troubleshooting) page.
### Running on a device[​](https://reactnative.dev/docs/0.71/environment-setup#running-on-a-device "Direct link to Running on a device")
The above command will automatically run your app on the iOS Simulator by default. If you want to run the app on an actual physical iOS device, please follow the instructions [here](https://reactnative.dev/docs/0.71/running-on-device).
### Modifying your app[​](https://reactnative.dev/docs/0.71/environment-setup#modifying-your-app "Direct link to Modifying your app")
Now that you have successfully run the app, let's modify it.
  * Open `App.tsx` in your text editor of choice and edit some lines.
  * Hit `⌘R` in your iOS Simulator to reload the app and see your changes!


### That's it![​](https://reactnative.dev/docs/0.71/environment-setup#thats-it "Direct link to That's it!")
Congratulations! You've successfully run and modified your first React Native app.
## Now what?[​](https://reactnative.dev/docs/0.71/environment-setup#now-what "Direct link to Now what?")
  * If you want to add this new React Native code to an existing application, check out the [Integration guide](https://reactnative.dev/docs/0.71/integration-with-existing-apps).


If you're curious to learn more about React Native, check out the [Introduction to React Native](https://reactnative.dev/docs/0.71/getting-started).
#### Target OS[​](https://reactnative.dev/docs/0.71/environment-setup#target-os-1 "Direct link to Target OS")
  * Android
  * iOS


## Installing dependencies
You will need Node, the React Native command line interface, a JDK, and Android Studio.
While you can use any editor of your choice to develop your app, you will need to install Android Studio in order to set up the necessary tooling to build your React Native app for Android.
### Node, JDK
We recommend installing Node via [Chocolatey](https://chocolatey.org), a popular package manager for Windows.
It is recommended to use an LTS version of Node. If you want to be able to switch between different versions, you might want to install Node via [nvm-windows](https://github.com/coreybutler/nvm-windows), a Node version manager for Windows.
React Native also requires [Java SE Development Kit (JDK)](https://openjdk.java.net/projects/jdk/11/), which can be installed using Chocolatey as well.
Open an Administrator Command Prompt (right click Command Prompt and select "Run as Administrator"), then run the following command:
powershell
```
choco install -y nodejs-lts microsoft-openjdk11
```

If you have already installed Node on your system, make sure it is Node 14 or newer. If you already have a JDK on your system, we recommend JDK11. You may encounter problems using higher JDK versions.
> You can find additional installation options on [Node's Downloads page](https://nodejs.org/en/download/).
> If you're using the latest version of Java Development Kit, you'll need to change the Gradle version of your project so it can recognize the JDK. You can do that by going to `{project root folder}\android\gradle\wrapper\gradle-wrapper.properties` and changing the `distributionUrl` value to upgrade the Gradle version. You can check out [here the latest releases of Gradle](https://gradle.org/releases/).
### Android development environment
Setting up your development environment can be somewhat tedious if you're new to Android development. If you're already familiar with Android development, there are a few things you may need to configure. In either case, please make sure to carefully follow the next few steps.
#### 1. Install Android Studio
[Download and install Android Studio](https://developer.android.com/studio/index.html). While on Android Studio installation wizard, make sure the boxes next to all of the following items are checked:
  * `Android SDK`
  * `Android SDK Platform`
  * `Android Virtual Device`
  * If you are not already using Hyper-V: `Performance (Intel ® HAXM)` ([See here for AMD or Hyper-V](https://android-developers.googleblog.com/2018/07/android-emulator-amd-processor-hyper-v.html))


Then, click "Next" to install all of these components.
> If the checkboxes are grayed out, you will have a chance to install these components later on.
Once setup has finalized and you're presented with the Welcome screen, proceed to the next step.
#### 2. Install the Android SDK
Android Studio installs the latest Android SDK by default. Building a React Native app with native code, however, requires the `Android 13 (Tiramisu)` SDK in particular. Additional Android SDKs can be installed through the SDK Manager in Android Studio.
To do that, open Android Studio, click on "More Actions" button and select "SDK Manager".
> The SDK Manager can also be found within the Android Studio "Settings" dialog, under **Languages & Frameworks** → **Android SDK**.
Select the "SDK Platforms" tab from within the SDK Manager, then check the box next to "Show Package Details" in the bottom right corner. Look for and expand the `Android 13 (Tiramisu)` entry, then make sure the following items are checked:
  * `Android SDK Platform 33`
  * `Intel x86 Atom_64 System Image` or `Google APIs Intel x86 Atom System Image`


Next, select the "SDK Tools" tab and check the box next to "Show Package Details" here as well. Look for and expand the `Android SDK Build-Tools` entry, then make sure that `33.0.0` is selected.
Finally, click "Apply" to download and install the Android SDK and related build tools.
#### 3. Configure the ANDROID_HOME environment variable
The React Native tools require some environment variables to be set up in order to build apps with native code.
  1. Open the **Windows Control Panel.**
  2. Click on **User Accounts,** then click **User Accounts** again
  3. Click on **Change my environment variables**
  4. Click on **New...** to create a new `ANDROID_HOME` user variable that points to the path to your Android SDK:


The SDK is installed, by default, at the following location:
powershell
```
%LOCALAPPDATA%\Android\Sdk
```

You can find the actual location of the SDK in the Android Studio "Settings" dialog, under **Languages & Frameworks** → **Android SDK**.
Open a new Command Prompt window to ensure the new environment variable is loaded before proceeding to the next step.
  1. Open powershell
  2. Copy and paste **Get-ChildItem -Path Env:\** into powershell
  3. Verify `ANDROID_HOME` has been added


#### 4. Add platform-tools to Path
  1. Open the **Windows Control Panel.**
  2. Click on **User Accounts,** then click **User Accounts** again
  3. Click on **Change my environment variables**
  4. Select the **Path** variable.
  5. Click **Edit.**
  6. Click **New** and add the path to platform-tools to the list.


The default location for this folder is:
powershell
```
%LOCALAPPDATA%\Android\Sdk\platform-tools
```

### React Native Command Line Interface
React Native has a built-in command line interface. Rather than install and manage a specific version of the CLI globally, we recommend you access the current version at runtime using `npx`, which ships with Node.js. With `npx react-native <command>`, the current stable version of the CLI will be downloaded and executed at the time the command is run.
## Creating a new application
> If you previously installed a global `react-native-cli` package, please remove it as it may cause unexpected issues:
> shell
> ```
npm uninstall -g react-native-cli @react-native-community/cli
```

React Native has a built-in command line interface, which you can use to generate a new project. You can access it without installing anything globally using `npx`, which ships with Node.js. Let's create a new React Native project called "AwesomeProject":
shell
```
npx react-native@latest init AwesomeProject
```

This is not necessary if you are integrating React Native into an existing application, or if you've installed [Expo](https://docs.expo.dev/bare/installing-expo-modules/) in your project, or if you're adding Android support to an existing React Native project (see [Integration with Existing Apps](https://reactnative.dev/docs/0.71/integration-with-existing-apps)). You can also use a third-party CLI to init your React Native app, such as [Ignite CLI](https://github.com/infinitered/ignite).
### [Optional] Using a specific version or template
If you want to start a new project with a specific React Native version, you can use the `--version` argument:
shell
```
npx react-native@X.XX.X init AwesomeProject --version X.XX.X
```

You can also start a project with a custom React Native template with the `--template` argument.
## Preparing the Android device
You will need an Android device to run your React Native Android app. This can be either a physical Android device, or more commonly, you can use an Android Virtual Device which allows you to emulate an Android device on your computer.
Either way, you will need to prepare the device to run Android apps for development.
### Using a physical device
If you have a physical Android device, you can use it for development in place of an AVD by plugging it in to your computer using a USB cable and following the instructions [here](https://reactnative.dev/docs/0.71/running-on-device).
### Using a virtual device
If you use Android Studio to open `./AwesomeProject/android`, you can see the list of available Android Virtual Devices (AVDs) by opening the "AVD Manager" from within Android Studio. Look for an icon that looks like this:
If you have recently installed Android Studio, you will likely need to [create a new AVD](https://developer.android.com/studio/run/managing-avds.html). Select "Create Virtual Device...", then pick any Phone from the list and click "Next", then select the **Tiramisu** API Level 33 image.
> If you don't have HAXM installed, click on "Install HAXM" or follow [these instructions](https://github.com/intel/haxm/wiki/Installation-Instructions-on-Windows) to set it up, then go back to the AVD Manager.
Click "Next" then "Finish" to create your AVD. At this point you should be able to click on the green triangle button next to your AVD to launch it, then proceed to the next step.
## Running your React Native application
### Step 1: Start Metro
First, you will need to start Metro, the JavaScript bundler that ships with React Native. Metro "takes in an entry file and various options, and returns a single JavaScript file that includes all your code and its dependencies."—[Metro Docs](https://metrobundler.dev/docs/concepts)
To start Metro, run `npx react-native start` inside your React Native project folder:
shell
```
npx react-native start
```

`react-native start` starts Metro Bundler.
> If you use the Yarn package manager, you can use `yarn` instead of `npx` when running React Native commands inside an existing project.
> If you're familiar with web development, Metro is a lot like webpack—for React Native apps. Unlike Kotlin or Java, JavaScript isn't compiled—and neither is React Native. Bundling isn't the same as compiling, but it can help improve startup performance and translate some platform-specific JavaScript into more widely supported JavaScript.
### Step 2: Start your application
Let Metro Bundler run in its own terminal. Open a new terminal inside your React Native project folder. Run the following:
shell
```
npx react-native run-android
```

If everything is set up correctly, you should see your new app running in your Android emulator shortly.
`npx react-native run-android` is one way to run your app - you can also run it directly from within Android Studio.
> If you can't get this to work, see the [Troubleshooting](https://reactnative.dev/docs/0.71/troubleshooting) page.
### Modifying your app
Now that you have successfully run the app, let's modify it.
  * Open `App.tsx` in your text editor of choice and edit some lines.
  * Press the `R` key twice or select `Reload` from the Developer Menu (`Ctrl + M`) to see your changes!


### That's it!
Congratulations! You've successfully run and modified your first React Native app.
## Now what?
  * If you want to add this new React Native code to an existing application, check out the [Integration guide](https://reactnative.dev/docs/0.71/integration-with-existing-apps).


If you're curious to learn more about React Native, check out the [Introduction to React Native](https://reactnative.dev/docs/0.71/getting-started).
## Unsupported[​](https://reactnative.dev/docs/0.71/environment-setup#unsupported "Direct link to Unsupported")
> A Mac is required to build projects with native code for iOS. You can follow the **Expo Go Quickstart** to learn how to build your app using Expo instead.
#### Target OS[​](https://reactnative.dev/docs/0.71/environment-setup#target-os-2 "Direct link to Target OS")
  * Android
  * iOS


## Installing dependencies[​](https://reactnative.dev/docs/0.71/environment-setup#installing-dependencies "Direct link to Installing dependencies")
You will need Node, the React Native command line interface, a JDK, and Android Studio.
While you can use any editor of your choice to develop your app, you will need to install Android Studio in order to set up the necessary tooling to build your React Native app for Android.
### Node
Follow the [installation instructions for your Linux distribution](https://nodejs.org/en/download/package-manager/) to install Node 14 or newer.
### Java Development Kit
React Native currently recommends version 11 of the Java SE Development Kit (JDK). You may encounter problems using higher JDK versions. You may download and install [OpenJDK](http://openjdk.java.net) from [AdoptOpenJDK](https://adoptopenjdk.net/) or your system packager.
### Android development environment
Setting up your development environment can be somewhat tedious if you're new to Android development. If you're already familiar with Android development, there are a few things you may need to configure. In either case, please make sure to carefully follow the next few steps.
#### 1. Install Android Studio
[Download and install Android Studio](https://developer.android.com/studio/index.html). While on Android Studio installation wizard, make sure the boxes next to all of the following items are checked:
  * `Android SDK`
  * `Android SDK Platform`
  * `Android Virtual Device`


Then, click "Next" to install all of these components.
> If the checkboxes are grayed out, you will have a chance to install these components later on.
Once setup has finalized and you're presented with the Welcome screen, proceed to the next step.
#### 2. Install the Android SDK
Android Studio installs the latest Android SDK by default. Building a React Native app with native code, however, requires the `Android 13 (Tiramisu)` SDK in particular. Additional Android SDKs can be installed through the SDK Manager in Android Studio.
To do that, open Android Studio, click on "Configure" button and select "SDK Manager".
> The SDK Manager can also be found within the Android Studio "Settings" dialog, under **Languages & Frameworks** → **Android SDK**.
Select the "SDK Platforms" tab from within the SDK Manager, then check the box next to "Show Package Details" in the bottom right corner. Look for and expand the `Android 13 (Tiramisu)` entry, then make sure the following items are checked:
  * `Android SDK Platform 33`
  * `Intel x86 Atom_64 System Image` or `Google APIs Intel x86 Atom System Image`


Next, select the "SDK Tools" tab and check the box next to "Show Package Details" here as well. Look for and expand the "Android SDK Build-Tools" entry, then make sure that `33.0.0` is selected.
Finally, click "Apply" to download and install the Android SDK and related build tools.
#### 3. Configure the ANDROID_HOME environment variable
The React Native tools require some environment variables to be set up in order to build apps with native code.
Add the following lines to your `$HOME/.bash_profile` or `$HOME/.bashrc` (if you are using `zsh` then `~/.zprofile` or `~/.zshrc`) config file:
shell
```
exportANDROID_HOME=$HOME/Android/SdkexportPATH=$PATH:$ANDROID_HOME/emulatorexportPATH=$PATH:$ANDROID_HOME/platform-tools
```

> `.bash_profile` is specific to `bash`. If you're using another shell, you will need to edit the appropriate shell-specific config file.
Type `source $HOME/.bash_profile` for `bash` or `source $HOME/.zprofile` to load the config into your current shell. Verify that ANDROID_HOME has been set by running `echo $ANDROID_HOME` and the appropriate directories have been added to your path by running `echo $PATH`.
> Please make sure you use the correct Android SDK path. You can find the actual location of the SDK in the Android Studio "Settings" dialog, under **Languages & Frameworks** → **Android SDK**.
### Watchman
Follow the [Watchman installation guide](https://facebook.github.io/watchman/docs/install#buildinstall) to compile and install Watchman from source.
> [Watchman](https://facebook.github.io/watchman/docs/install) is a tool by Facebook for watching changes in the filesystem. It is highly recommended you install it for better performance and increased compatibility in certain edge cases (translation: you may be able to get by without installing this, but your mileage may vary; installing this now may save you from a headache later).
### React Native Command Line Interface
React Native has a built-in command line interface. Rather than install and manage a specific version of the CLI globally, we recommend you access the current version at runtime using `npx`, which ships with Node.js. With `npx react-native <command>`, the current stable version of the CLI will be downloaded and executed at the time the command is run.
## Creating a new application
> If you previously installed a global `react-native-cli` package, please remove it as it may cause unexpected issues:
> shell
> ```
npm uninstall -g react-native-cli @react-native-community/cli
```

React Native has a built-in command line interface, which you can use to generate a new project. You can access it without installing anything globally using `npx`, which ships with Node.js. Let's create a new React Native project called "AwesomeProject":
shell
```
npx react-native@latest init AwesomeProject
```

This is not necessary if you are integrating React Native into an existing application, or if you've installed [Expo](https://docs.expo.dev/bare/installing-expo-modules/) in your project, or if you're adding Android support to an existing React Native project (see [Integration with Existing Apps](https://reactnative.dev/docs/0.71/integration-with-existing-apps)). You can also use a third-party CLI to init your React Native app, such as [Ignite CLI](https://github.com/infinitered/ignite).
### [Optional] Using a specific version or template
If you want to start a new project with a specific React Native version, you can use the `--version` argument:
shell
```
npx react-native@X.XX.X init AwesomeProject --version X.XX.X
```

You can also start a project with a custom React Native template with the `--template` argument.
## Preparing the Android device
You will need an Android device to run your React Native Android app. This can be either a physical Android device, or more commonly, you can use an Android Virtual Device which allows you to emulate an Android device on your computer.
Either way, you will need to prepare the device to run Android apps for development.
### Using a physical device
If you have a physical Android device, you can use it for development in place of an AVD by plugging it in to your computer using a USB cable and following the instructions [here](https://reactnative.dev/docs/0.71/running-on-device).
### Using a virtual device
If you use Android Studio to open `./AwesomeProject/android`, you can see the list of available Android Virtual Devices (AVDs) by opening the "AVD Manager" from within Android Studio. Look for an icon that looks like this:
If you have recently installed Android Studio, you will likely need to [create a new AVD](https://developer.android.com/studio/run/managing-avds.html). Select "Create Virtual Device...", then pick any Phone from the list and click "Next", then select the **Tiramisu** API Level 33 image.
> We recommend configuring [VM acceleration](https://developer.android.com/studio/run/emulator-acceleration.html#vm-linux) on your system to improve performance. Once you've followed those instructions, go back to the AVD Manager.
Click "Next" then "Finish" to create your AVD. At this point you should be able to click on the green triangle button next to your AVD to launch it, then proceed to the next step.
## Running your React Native application
### Step 1: Start Metro
First, you will need to start Metro, the JavaScript bundler that ships with React Native. Metro "takes in an entry file and various options, and returns a single JavaScript file that includes all your code and its dependencies."—[Metro Docs](https://metrobundler.dev/docs/concepts)
To start Metro, run `npx react-native start` inside your React Native project folder:
shell
```
npx react-native start
```

`react-native start` starts Metro Bundler.
> If you use the Yarn package manager, you can use `yarn` instead of `npx` when running React Native commands inside an existing project.
> If you're familiar with web development, Metro is a lot like webpack—for React Native apps. Unlike Kotlin or Java, JavaScript isn't compiled—and neither is React Native. Bundling isn't the same as compiling, but it can help improve startup performance and translate some platform-specific JavaScript into more widely supported JavaScript.
### Step 2: Start your application
Let Metro Bundler run in its own terminal. Open a new terminal inside your React Native project folder. Run the following:
shell
```
npx react-native run-android
```

If everything is set up correctly, you should see your new app running in your Android emulator shortly.
`npx react-native run-android` is one way to run your app - you can also run it directly from within Android Studio.
> If you can't get this to work, see the [Troubleshooting](https://reactnative.dev/docs/0.71/troubleshooting) page.
### Modifying your app
Now that you have successfully run the app, let's modify it.
  * Open `App.tsx` in your text editor of choice and edit some lines.
  * Press the `R` key twice or select `Reload` from the Developer Menu (`Ctrl + M`) to see your changes!


### That's it!
Congratulations! You've successfully run and modified your first React Native app.
## Now what?
  * If you want to add this new React Native code to an existing application, check out the [Integration guide](https://reactnative.dev/docs/0.71/integration-with-existing-apps).


If you're curious to learn more about React Native, check out the [Introduction to React Native](https://reactnative.dev/docs/0.71/getting-started).
## Unsupported[​](https://reactnative.dev/docs/0.71/environment-setup#unsupported-1 "Direct link to Unsupported")
> A Mac is required to build projects with native code for iOS. You can follow the **Expo Go Quickstart** to learn how to build your app using Expo instead.
Is this page useful?

