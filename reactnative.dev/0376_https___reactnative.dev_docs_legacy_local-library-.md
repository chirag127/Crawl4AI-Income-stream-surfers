---
url: https://reactnative.dev/docs/legacy/local-library-setup
title: https://reactnative.dev/docs/legacy/local-library-setup
date: 2025-05-10T21:40:25.808614
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/legacy/local-library-setup#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
A local library is a library containing views or modules that's local to your app and not published to a registry. This is different from the traditional setup for view and modules in the sense that a local library is decoupled from your app's native code.
The local library is created outside of the `android/` and `ios/` folders and makes use of autolinking to integrate with your app. The structure with a local library may look like this:
plaintext
```
MyApp├── node_modules├── modules <-- folder for your local libraries│ └── awesome-module <-- your local library├── android├── ios├── src├── index.js└── package.json
```

Since a local library's code exists outside of `android/` and `ios/` folders, it makes it easier to upgrade React Native versions in the future, copy to other projects etc.
To create local library we will use [create-react-native-library](https://callstack.github.io/react-native-builder-bob/create). This tool contains all the necessary templates.
### Getting Started[​](https://reactnative.dev/docs/legacy/local-library-setup#getting-started "Direct link to Getting Started")
Inside your React Native application's root folder, run the following command:
shell
```
npx create-react-native-library@latest awesome-module
```

Where `awesome-module` is the name you would like for the new module. After going through the prompts, you will have a new folder called `modules` in your project's root directory which contains the new module.
### Linking[​](https://reactnative.dev/docs/legacy/local-library-setup#linking "Direct link to Linking")
By default, the generated library is automatically linked to the project using `link:` protocol when using Yarn and `file:` when using npm:
  * npm
  * Yarn


json
```
"dependencies":{"awesome-module":"file:./modules/awesome-module"
```

json
```
"dependencies":{"awesome-module":"link:./modules/awesome-module"
```

This creates a symlink to the library under `node_modules` which makes autolinking work.
### Installing dependencies[​](https://reactnative.dev/docs/legacy/local-library-setup#installing-dependencies "Direct link to Installing dependencies")
To link the module you need to install dependencies:
  * npm
  * Yarn


shell
```
npminstall
```

shell
```
yarninstall
```

### Using module inside your app[​](https://reactnative.dev/docs/legacy/local-library-setup#using-module-inside-your-app "Direct link to Using module inside your app")
To use the module inside your app, you can import it by its name:
js
```
import{multiply}from'awesome-module';
```

Is this page useful?
  * [Getting Started](https://reactnative.dev/docs/legacy/local-library-setup#getting-started)
  * [Installing dependencies](https://reactnative.dev/docs/legacy/local-library-setup#installing-dependencies)
  * [Using module inside your app](https://reactnative.dev/docs/legacy/local-library-setup#using-module-inside-your-app)



