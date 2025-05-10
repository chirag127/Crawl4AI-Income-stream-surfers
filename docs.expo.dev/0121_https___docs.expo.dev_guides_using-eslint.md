---
url: https://docs.expo.dev/guides/using-eslint
title: https://docs.expo.dev/guides/using-eslint
date: 2025-04-30T17:14:04.169519
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Using ESLint and Prettier
A guide on configuring ESLint and Prettier to format Expo apps.
[ESLint](https://eslint.org/) is a JavaScript linter that helps you find and fix errors in your code. It's a great tool to help you write better code and catch mistakes before they make it to production. In conjunction, you can use [Prettier](https://prettier.io/docs/en/), a code formatter that ensures all the code files follow a consistent styling.
This guide provides steps to set up and configure ESLint and Prettier.
## ESLint
### Setup
To set up ESLint in your Expo project, you can use the Expo CLI to install the necessary dependencies. Running this command also creates a eslint.config.js file at the root of your project which extends configuration from [`eslint-config-expo`](https://github.com/expo/expo/tree/main/packages/eslint-config-expo).
Terminal
Copy
`# Install and configure ESLint`
`- ``npx expo lint`
> From SDK 53 onwards, the created ESLint config file will use the [Flat config](https://eslint.org/blog/2022/08/new-config-system-part-2/) format. However, legacy config will also be supported.
Setup instructions for SDK 50 and below
1
Install ESLint, and [`eslint-config-expo`](https://github.com/expo/expo/tree/main/packages/eslint-config-expo) in your project.
macOS/Linux
Windows
Terminal
Copy
`- ``npx expo install eslint@8 eslint-config-expo --dev`
Terminal
Copy
`- ``npx expo install eslint@8 eslint-config-expo "--" --dev`
2
Create an ESLint configuration file called .eslintrc.js at the root of your project. The configuration in .eslintrc.js extends [`eslint-config-expo`](https://github.com/expo/expo/tree/main/packages/eslint-config-expo).
.eslintrc.js
Copy
```
module.exports = {
 extends: 'expo',
};

```

3
Add a `script` to your package.json to run ESLint.
package.json
Copy
```
{
 "scripts": {
  "lint": "expo lint"
 }
}

```

You can replace the `.` with specific directories or files to lint. For example, if you use Expo Router, you can use the `eslint app` command to lint only your routes inside the app directory.
### Usage
> Recommended: If you're using VS Code, install the [ESLint extension](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) to lint your code as you type.
You can lint your code manually from the command line with the `npx expo lint` script:
For SDK 51 and above
For SDK 50 and below
Terminal
Copy
`# After ESLint has been configured, run the command again to lint your code.`
`- ``npx expo lint`
Running the above command will run the `lint` script from package.json.
Terminal
`# Example output for npx expo lint command``/app/components/HelloWave.tsx`` 22:6 warning React Hook useEffect has a missing dependency: "rotateAnimation".``    Either include it or remove the dependency array react-hooks/exhaustive-deps``✖ 1 problem (0 errors, 1 warning)`
Terminal
Copy
`- ``npm run lint`
### Environment configuration
ESLint is generally configured for a single environment. However, the source code is written in JavaScript in an Expo app that runs in multiple different environments. For example, the app.config.js, metro.config.js, babel.config.js, and app/+html.tsx files are run in a Node.js environment. It means they have access to the global `__dirname` variable and can use Node.js modules such as `path`. Standard Expo project files like app/index.js can be run in Hermes, Node.js, or the web browser.
You can add the `eslint-env` comment directive to the top of a file to tell ESLint which environment the file is running in. For example, to tell ESLint that a file is run in Node.js, add the following comment to the top of the file:
metro.config.js
Copy
```
/* eslint-env node */
const { getDefaultConfig } = require('expo/metro-config');
/** @type {import('expo/metro-config').MetroConfig} */
const config = getDefaultConfig(
 __dirname
);
module.exports = config;

```

## Prettier
### Installation
To install Prettier in your project:
macOS/Linux
Windows
Terminal
Copy
`- ``npx expo install prettier eslint-config-prettier eslint-plugin-prettier --dev`
Terminal
Copy
`- ``npx expo install prettier eslint-config-prettier eslint-plugin-prettier "--" --dev`
### Setup
Flat config
Legacy config
To integrate Prettier with ESLint, update your eslint.config.js:
eslint.config.js
Copy
```
const { defineConfig } = require('eslint/config');
const expoConfig = require('eslint-config-expo/flat');
const eslintPluginPrettierRecommended = require('eslint-plugin-prettier/recommended');
module.exports = defineConfig([
 expoConfig,
 eslintPluginPrettierRecommended,
 {
  ignores: ['dist/*'],
 },
]);

```

To integrate Prettier with ESlint, update your .eslintrc.js:
.eslintrc.js
Copy
```
module.exports = {
 extends: ['expo', 'prettier'],
 plugins: ['prettier'],
 rules: {
  'prettier/prettier': 'error',
 },
};

```

> Note: In the above configuration, you can use `"prettier/prettier": "warn"` if you prefer these formatting issues as warnings instead of errors.
Now, when you run `npx expo lint`, anything that is not aligned with Prettier formatting will be caught as an error.
To customize Prettier settings, create a .prettierrc file at the root of your project and add your configuration.
[Custom Prettier configurationLearn more about customizing Prettier configuration.](https://github.com/expo/expo/tree/main/packages/eslint-config-universe#customizing-prettier)
## Troubleshooting
### ESLint is not updating in VS Code
If you're using VS Code, install the [ESLint extension](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) to lint your code as you type. You can try restarting the ESLint server by running the command `ESLint: Restart ESLint Server` from the [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette).
### ESLint is slow
ESLint can be slow to run on large projects. The easiest way to speed up the process is to lint fewer files. Add a .eslintignore file to your project root to ignore certain files and directories such as:
.eslintignore
Copy
```
/.expo
node_modules

```

## Migration to Flat config
> Note: Flat config is supported in Expo SDK 53 and above.
Upgrade ESLint and `eslint-config-expo`:
macOS/Linux
Windows
Terminal
Copy
`- ``npx expo install eslint eslint-config-expo --dev`
Terminal
Copy
`- ``npx expo install eslint eslint-config-expo "--" --dev`
If you haven't customized your ESLint config at all, delete your .eslintrc.js and generate the new config with:
Terminal
Copy
`- ``npx expo lint`
Alternatively, migrate your config based on the [ESLint's migration guide](https://eslint.org/docs/latest/use/configure/migration-guide). `npx expo lint` supports both legacy and flat config, so the new config will automatically be picked up by the CLI.

