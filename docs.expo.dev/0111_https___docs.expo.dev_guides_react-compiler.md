---
url: https://docs.expo.dev/guides/react-compiler
title: https://docs.expo.dev/guides/react-compiler
date: 2025-04-30T17:14:04.127621
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# React Compiler
Learn how to enable and use the React Compiler in Expo apps.
> Warning: React Compiler is experimental. Currently, it is on hold and we'll soon provide more updates on its usage.
The new [React Compiler](https://react.dev/learn/react-compiler) automatically memoizes components and hooks to enable fine-grained reactivity. This can lead to significant performance improvements in your app. The React Compiler is currently experimental and is not enabled by default. You can enable it in your app by following the instructions below.
## Enabling React Compiler
1
[Check how compatible](https://react.dev/learn/react-compiler#checking-compatibility) your project is with the React Compiler.
Terminal
Copy
`- ``npx react-compiler-healthcheck@latest`
This will generally verify if your app is following the [rules of React](https://react.dev/reference/rules).
2
Install `babel-plugin-react-compiler` and the React compiler runtime in your project:
SDK 53 and above
SDK 52 and below
Terminal
Copy
`- ``npx expo install babel-plugin-react-compiler@beta`
Terminal
Copy
`- ``npx expo install babel-plugin-react-compiler@beta react-compiler-runtime@beta`
3
Toggle on the React Compiler experiment in your app config file:
app.json
Copy
```
{
 "experiments": {
  "reactCompiler": true
 }
}

```

### Enabling the linter
> In the future, all of the following steps below will be automated by Expo CLI.
Additionally, you should use the ESLint plugin to continuously enforce the rules of React in your project.
1
Run [`npx expo lint`](https://docs.expo.dev/guides/using-eslint#eslint) to ensure ESLint is setup in your app, then install the ESLint plugin for React Compiler:
Terminal
Copy
`- ``npx expo install eslint-plugin-react-compiler`
2
Update your [ESLint configuration](https://docs.expo.dev/guides/using-eslint) to include the plugin:
.eslintrc.js
Copy
```
// https://docs.expo.dev/guides/using-eslint/
const { defineConfig } = require('eslint/config');
const expoConfig = require('eslint-config-expo/flat');
module.exports = defineConfig([
 expoConfig,
 {
  ignores: ['dist/*'],
  plugins: ['react-compiler'],
  rules: {
   'react-compiler/react-compiler': 'error',
  },
 },
]);

```

## Incremental adoption
You can incrementally adopt the React Compiler in your app using a few strategies:
1
Configure the Babel plugin to only run on specific files or components. To do this:
  1. If your project doesn't have [babel.config.js](https://docs.expo.dev/versions/latest/config/babel), create one by running `npx expo customize babel.config.js`.
  2. Add the following configuration to babel.config.js:


babel.config.js
Copy
```
module.exports = function (api) {
 api.cache(true);
 return {
  presets: [
   [
    'babel-preset-expo',
    {
     'react-compiler': {
      sources: filename => {
       // Match file names to include in the React Compiler.
       return filename.includes('src/path/to/dir');
      },
     },
    },
   ],
  ],
 };
};

Show More

```

Whenever you change your babel.config.js file, you need to restart the Metro bundler to apply the changes:
Terminal
Copy
`- ``npx expo start --clear`
2
Use the `"use no memo"` directive to opt out of the React Compiler for specific components or files.
```
function MyComponent() {
 'use no memo';
 return <Text>Will not be optimized</Text>;
}

```

## Usage
> To better understand how React Compiler works, check out the [React Playground](https://playground.react.dev/).
Improvements are primarily automatic. You can remove instances of `useCallback`, `useMemo`, and `React.memo` in favor of the automatic memoization. Class components will not be optimized. Instead, migrate to function components.
Expo's implementation of the React Compiler will only run on application code (no node modules), and only when bundling for the client (disabled in server rendering).
## Configuration
You can pass additional settings to the React Compiler Babel plugin by using the `react-compiler` object in the Babel configuration:
babel.config.js
Copy
```
module.exports = function (api) {
 api.cache(true);
 return {
  presets: [
   [
    'babel-preset-expo',
    {
     'react-compiler': {
      // Passed directly to the React Compiler Babel plugin.
      compilationMode: 'strict',
      panicThreshold: 'all_errors',
     },
     web: {
      'react-compiler': {
       // Web-only settings...
      },
     },
    },
   ],
  ],
 };
};

Show More

```


