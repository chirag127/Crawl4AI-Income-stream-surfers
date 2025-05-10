---
url: https://docs.expo.dev/more/create-expo
title: https://docs.expo.dev/more/create-expo
date: 2025-04-30T17:14:13.317607
depth: 2
---

Search
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# create-expo-app
A command-line tool to create a new Expo and React Native project.
`create-expo-app` is a command-line tool to create and set up a new Expo and React Native project. This tool simplifies the initialization process by providing various templates to get started quickly without the need for manual configuration.
## Create a new project
To create a new project, run the following command:
npm
Yarn
pnpm
Bun
Terminal
Copy
`- ``npx create-expo-app@latest`
Terminal
Copy
`- ``yarn create expo-app`
Terminal
Copy
`- ``pnpm create expo-app`
Terminal
Copy
`- ``bun create expo`
Running the above command will prompt you to enter the app name of your project. This app name is also used in the app config's [`name`](https://docs.expo.dev/versions/latest/config/app#name) property.
Terminal
Copy
`What is your app named? my-app`
## Options
Uses the following options to customize the command behavior.
### `--yes`
Uses the default options to create a new project.
### `--no-install`
Skips installing npm dependencies or CocoaPods.
### `--template`
Running `create-expo-app` with a [Node Package Manager](https://docs.expo.dev/more/create-expo#node-package-managers-support) initializes and sets up a new Expo project using the default template.
You can use the `--template` option to select one of the following templates or pass it as an argument to the option. For example, `--template default`.
Template| Description  
---|---  
Default template. Designed to build multi-screen apps. Includes recommended tools such as Expo CLI, Expo Router library and TypeScript configuration enabled. Suitable for most apps.  
Installs minimum required npm dependencies without configuring navigation.  
A Blank template with TypeScript enabled.  
Installs and configures file-based routing with Expo Router and TypeScript enabled.  
A Blank template with native directories (android and ios) generated. Runs [`npx expo prebuild`](https://docs.expo.dev/workflow/prebuild) during the setup.  
### `--example`
Use this option to initialize a project using an example from [expo/examples](https://github.com/expo/examples).
For example, running `npx create-expo-app --example with-router` will set up a project with Expo Router library.
### `--version`
Prints the version number and exits.
### `--help`
Prints the list of available options and exits.
## Node Package Managers support
Creating a new project with `create-expo-app` also handles setting up additional configuration needed for a specific Node Package Manager.
If you are migrating from one package manager to another, you've to manually carry out the additional configuration in your project. If you are using [EAS](https://docs.expo.dev/eas), you also have to configure your project for any additional required steps manually.
All the additional steps for each package manager are listed below.
### npm
#### Local installation
npm is installed as part of Node.js installation. See [Node.js documentation](https://nodejs.org/en/download/package-manager) for installation instructions.
#### EAS installation
Supported by default if the project directory contains package-lock.json.
### Yarn 1 (Classic)
#### Local installation
Yarn 1 (Classic) is usually installed as a global dependency of npm. See [Yarn 1 documentation](https://classic.yarnpkg.com/en/docs/getting-started) for installation instructions.
#### EAS installation
Supported by default if the project directory contains yarn.lock.
### Yarn 2+ (Modern)
#### Local installation
See [Yarn documentation](https://yarnpkg.com/getting-started/install) for installation instructions.
Yarn 2+ handles package management differently than Yarn 1. One of the core changes in Yarn 2+ is the [Plug'n'Play (PnP)](https://yarnpkg.com/features/pnp) node linking model that does not work with React Native.
By default, a project created with `create-expo-app` and Yarn 2+ uses [`nodeLinker`](https://yarnpkg.com/features/linkers#nodelinker-node-modules) with its value set to `node-modules` to install dependencies.
.yarnrc.yml
Copy
```
nodeLinker: node-modules

```

#### EAS installation
Yarn Modern on EAS requires adding [`eas-build-pre-install` hook](https://docs.expo.dev/build-reference/npm-hooks). In your project's package.json, add the following configuration:
package.json
Copy
```
{
 "scripts": {
  "eas-build-pre-install": "corepack enable && yarn set version 4"
 }
}

```

### pnpm
#### Local installation
Requires installing Node.js. See [pnpm documentation](https://pnpm.io/installation) for installation instructions.
By default, a project created with `create-expo-app` and pnpm uses [`node-linker`](https://pnpm.io/npmrc#node-linker) with its value set to `hoisted` to install dependencies.
.npmrc
Copy
```
node-linker=hoisted

```

#### EAS installation
Supported by default if the project directory contains pnpm-lock.yaml.
### Bun
See [Bun](https://docs.expo.dev/guides/using-bun) guide for details on creating a new Expo project with `bun`, migration from another package manager, and usage with EAS.

