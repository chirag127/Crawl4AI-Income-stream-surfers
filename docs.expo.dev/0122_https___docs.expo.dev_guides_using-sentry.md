---
url: https://docs.expo.dev/guides/using-sentry
title: https://docs.expo.dev/guides/using-sentry
date: 2025-04-30T17:14:04.174611
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Using Sentry
A guide on installing and configuring Sentry for crash reporting.
[Sentry](http://getsentry.com/) is a crash reporting platform that provides you with real-time insight into production deployments with info to reproduce and fix crashes.
It notifies you of exceptions or errors that your users run into while using your app and organizes them for you on a web dashboard. Reported exceptions include stacktraces, device info, version, and other relevant context automatically. You can also provide additional context that is specific to your application such as the current route and user id.
#### Platform compatibility
Android Device| Android Emulator| iOS Device| iOS Simulator| Web  
---|---|---|---|---  
## Install and configure Sentry
> `sentry-expo` has been merged into `@sentry/react-native` and is now deprecated. We recommend upgrading to SDK 50 to use `@sentry/react-native` for the best experience. If you're already using `sentry-expo`, [learn how to migrate](https://expo.fyi/sentry-expo-migration).
1
### Sign up for a Sentry account and create a project
Before proceeding with installing Sentry, you'll need to make sure you have created a Sentry account and project:
1.1
[Sign up for Sentry](https://sentry.io/signup/) (the free tier supports up to 5,000 events per month), and create a project in your Dashboard. Take note of your organization slug, project name, and DSN as you'll need them later:
  * organization slug is available in your Organization settings tab
  * project name is available in your project's Settings > Projects tab (find it in the list)
  * DSN is available in your project's Settings > Projects > Project name > Under SDK Setup section > Client Keys (DSN) tab.


1.2
Go to the [Developer Settings > Auth Tokens](https://sentry.io/settings/auth-tokens/) page and create a new [Organization Auth Token](https://docs.sentry.io/account/auth-tokens/#organization-auth-tokens). The token is automatically scoped for Source Map Upload and Release Creation. Save it.
Once you have each of these: organization slug, project name, DSN, and auth token, you're all set to proceed.
2
### Install @sentry/react-native
Run the following command in your project directory to install the official React Native library from the Sentry team:
Terminal
Copy
`- ``npx expo install @sentry/react-native`
3
### App configuration
Configuring `@sentry/react-native` can be done through the config plugin. Add the plugin to your project's [app config](https://docs.expo.dev/workflow/configuration) file:
app.json
Copy
```
{
 "expo": {
  "plugins": [
   [
    "@sentry/react-native/expo",
    {
     "organization": "sentry org slug, or use the `SENTRY_ORG` environment variable",
     "project": "sentry project name, or use the `SENTRY_PROJECT` environment variable",
     // If you are using a self-hosted instance, update the value of the url property
     // to point towards your self-hosted instance. For example, https://self-hosted.example.com/.
     "url": "https://sentry.io/"
    }
   ]
  ]
 }
}

```

Next, in an environment where you want to create releases and upload sourcemaps to Sentry, you will need to set the `SENTRY_AUTH_TOKEN` environment variable to your [Sentry auth token](https://docs.sentry.io/product/cli/configuration/). If you are using EAS Build, you can set the environment variable by [creating a secret named SENTRY_AUTH_TOKEN](https://docs.expo.dev/eas/using-environment-variables).
> The Sentry auth token should be stored securely. Do not commit it to a public repository, and treat it as you would any other sensitive API key.
Are you using this library in an existing React Native app?
If you do not use [Continuous Native Generation (CNG)](https://docs.expo.dev/workflow/continuous-native-generation), then you should use the [`@sentry/wizard`](https://docs.sentry.io/platforms/react-native/#install).
4
### Update Metro configuration
Sentry hooks into Metro to inject a "debug ID" into your source maps. This debug ID is used to associate source maps with releases. To enable this, you need to add the following to your metro.config.js (if you don't have the file yet, create it in the root of your project):
metro.config.js
Copy
```
// This replaces `const { getDefaultConfig } = require('expo/metro-config');`
const { getSentryExpoConfig } = require('@sentry/react-native/metro');
// This replaces `const config = getDefaultConfig(__dirname);`
const config = getSentryExpoConfig(__dirname);
module.exports = config;

```

5
### Initialize Sentry
Using Expo Router
Not using Expo Router
If your app uses [Expo Router](https://docs.expo.dev/router/introduction), then you can configure Sentry automatically to capture the current route and pass it along with your error reports. To set this up, configure Sentry in the [Root Layout route](https://docs.expo.dev/router/basics/layout#root-layout) and add the navigation integration.
app/_layout.tsx
Copy
```
import { Slot, useNavigationContainerRef } from 'expo-router';
import { useEffect } from 'react';
import * as Sentry from '@sentry/react-native';
import { isRunningInExpoGo } from 'expo';
// Construct a new integration instance. This is needed to communicate between the integration and React
const navigationIntegration = Sentry.reactNavigationIntegration({
 enableTimeToInitialDisplay: !isRunningInExpoGo(),
});
Sentry.init({
 dsn: 'YOUR DSN HERE',
 debug: true, // If `true`, Sentry will try to print out useful debugging information if something goes wrong with sending the event. Set it to `false` in production
 tracesSampleRate: 1.0, // Set tracesSampleRate to 1.0 to capture 100% of transactions for tracing. Adjusting this value in production.
 integrations: [
  // Pass integration
  navigationIntegration,
 ],
 enableNativeFramesTracking: !isRunningInExpoGo(), // Tracks slow and frozen frames in the application
});
function RootLayout() {
 // Capture the NavigationContainer ref and register it with the integration.
 const ref = useNavigationContainerRef();
 useEffect(() => {
  if (ref?.current) {
   navigationIntegration.registerNavigationContainer(ref);
  }
 }, [ref]);
 return <Slot />;
}
// Wrap the Root Layout route component with `Sentry.wrap` to capture gesture info and profiling data.
export default Sentry.wrap(RootLayout);

Show More

```

Add the following to your app's main file such as App.js:
```
import * as Sentry from '@sentry/react-native';
Sentry.init({
 dsn: 'YOUR DSN HERE',
 debug: true, // If `true`, Sentry will try to print out useful debugging information if something goes wrong with sending the event. Set it to `false` in production
});

```

Now wrap the root component of your app with Sentry. This may be App.js or index.js depending on your project.
```
import * as Sentry from '@sentry/react-native';
// Your App component here
export default Sentry.wrap(App);

```

6
### Verify the configuration
Create a new release build of your app and verify that it uploads source maps correctly. You may want to add a button in your app to test that it is working and sourcemaps are wired up as expected, for example:
```
import { Button } from 'react-native';
// Inside some component
<Button title="Press me" onPress={() => { throw new Error('Hello, again, Sentry!'); }}/>

```

## Usage with EAS Build
Ensure that `SENTRY_AUTH_TOKEN` is set in your build environment, and Sentry will automatically upload source maps for you. If you use environment variables rather than properties in your app config, ensure that those are set as well.
Using the above instructions, no additional work is needed to integrate Sentry into your project when using EAS Build.
## Usage with EAS Update
After running `eas update`, upload the source maps to Sentry:
Terminal
Copy
`# Pass in the "dist" directory generated by `eas update` to the upload script`
`- ``npx sentry-expo-upload-sourcemaps dist`
That's it! Errors for your updates will now be properly symbolicated in Sentry.
Do you want to publish an update and the sourcemaps in one command?
You can chain the commands together with `&&` to publish an update and upload the sourcemaps in one step:
Terminal
Copy
`- ``eas update --branch <branch> && npx sentry-expo-upload-sourcemaps dist`
Do you want to append additional update-related metadata to error reports?
Configuring Sentry to tag your scope with information about your update allows you to see errors happening on certain updates in the Sentry dashboard.
Add the following snippet in the global scope as early as possible in your application's lifecycle.
```
import * as Sentry from '@sentry/react-native';
import * as Updates from 'expo-updates';
const manifest = Updates.manifest;
const metadata = 'metadata' in manifest ? manifest.metadata : undefined;
const extra = 'extra' in manifest ? manifest.extra : undefined;
const updateGroup = metadata && 'updateGroup' in metadata ? metadata.updateGroup : undefined;
Sentry.init({
 // dsn, release, dist, etc...
});
const scope = Sentry.getGlobalScope();
scope.setTag('expo-update-id', Updates.updateId);
scope.setTag('expo-is-embedded-update', Updates.isEmbeddedLaunch);
if (typeof updateGroup === 'string') {
 scope.setTag('expo-update-group-id', updateGroup);
 const owner = extra?.expoClient?.owner ?? '[account]';
 const slug = extra?.expoClient?.slug ?? '[project]';
 scope.setTag(
  'expo-update-debug-url',
  `https://expo.dev/accounts/${owner}/projects/${slug}/updates/${updateGroup}`
 );
} else if (Updates.isEmbeddedLaunch) {
 // This will be `true` if the update is the one embedded in the build, and not one downloaded from the updates server.
 scope.setTag('expo-update-debug-url', 'not applicable for embedded updates');
}

Show More

```

Once configured, information about the associated update will show up in an error's tag section:
## Learn more about Sentry
Sentry does more than just catch fatal errors, learn more about how to use Sentry from their [JavaScript usage](https://docs.sentry.io/platforms/javascript/) documentation.

