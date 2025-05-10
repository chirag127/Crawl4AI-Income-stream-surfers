---
url: https://docs.expo.dev/tutorial/eas/multiple-app-variants
title: https://docs.expo.dev/tutorial/eas/multiple-app-variants
date: 2025-04-30T17:15:11.813310
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Configure multiple app variants
Learn how to configure dynamic app config to install multiple app variants on a single device.
In this chapter, we'll configure our project to run multiple build types (development, preview, production) on a single device simultaneously. This setup will allow us to test various stages of our app development without the need to uninstall and reinstall different versions.
[Watch: How to configure multiple app variants](https://www.youtube.com/watch?v=UtJJCAfrjIg)
Each variant requires a unique Android Application ID and iOS Bundle Identifier to enable simultaneous installations on one device. Here's how the IDs are set up in our app.json file:
app.json
Copy
```
{
 "ios": {
  "bundleIdentifier": "com.yourname.stickersmash"
  %%placeholder-start%%... %%placeholder-end%%
 },
 "android": {
  "package": "com.yourname.stickersmash"
  %%placeholder-start%%... %%placeholder-end%%
 }
}

```

1
## Add app.config.js for dynamic configuration
app.json contains app-related configuration in a JSON file. It's static and isn't ideal if we want to use [dynamic values for certain properties](https://docs.expo.dev/workflow/configuration#dynamic-configuration). We're going to add different Android Application IDs and iOS Bundle Identifiers for all build profiles based on [environment variables](https://docs.expo.dev/workflow/configuration#switching-configuration-based-on-the-environment).
  * In the root of your project, create a new file called app.config.js.
  * In app.config.js, export a default function that takes `config` as its argument. We'll then destructure the `config` to copy all existing properties from app.json.


app.config.js
Copy
```
export default ({ config }) => ({
 ...config,
});

```

2
## Update dynamic values based on environment
To identify the build type, let's add two environment variables called `IS_DEV` and`IS_PREVIEW` for `development` and `preview` build profiles in app.config.js:
app.config.js
Copy
```
const IS_DEV = process.env.APP_VARIANT === 'development';
const IS_PREVIEW = process.env.APP_VARIANT === 'preview';

```

Then, add two functions that dynamically change the app name, Android Application ID and iOS Bundle Identifier:
app.config.js
Copy
```
const getUniqueIdentifier = () => {
 if (IS_DEV) {
  return 'com.yourname.stickersmash.dev';
 }
 if (IS_PREVIEW) {
  return 'com.yourname.stickersmash.preview';
 }
 return 'com.yourname.stickersmash';
};
const getAppName = () => {
 if (IS_DEV) {
  return 'StickerSmash (Dev)';
 }
 if (IS_PREVIEW) {
  return 'StickerSmash (Preview)';
 }
 return 'StickerSmash: Emoji Stickers';
};

Show More

```

We'll use `getAppName()` to assign dynamic `name` values for the app and `getUniqueIdentifier()` to differentiate `android.package` and `ios.bundleIdentifier` for development and preview builds:
app.config.js
Copy
```
export default ({ config }) => ({
 ...config,
 name: getAppName(),
 ios: {
  ...config.ios,
  bundleIdentifier: getUniqueIdentifier(),
 },
 android: {
  ...config.android,
  package: getUniqueIdentifier(),
 },
};

```

3
## Configure eas.json
In eas.json, add the `APP_VARIANT` environment variable:
eas.json
Copy
```
{
 "build": {
  "development": {
   "developmentClient": true,
   "distribution": "internal",
   "env": {
    "APP_VARIANT": "development"
   }
  },
  "preview": {
   "distribution": "internal",
   "env": {
    "APP_VARIANT": "preview"
   }
  }
  %%placeholder-start%%... %%placeholder-end%%
 }
}

```

Running `eas build --profile development` will now set `APP_VARIANT` to `development`.
> Note: Since we changed the Android Application ID and iOS Bundle Identifier, the EAS CLI will prompt us to generate a new Keystore for Android and a new provisioning profile for iOS. To learn more about what these steps include, see the previous chapter for more information.
Since our `ios-simulator` build profile extends `development`, this configuration is automatically applied for iOS Simulators.
4
## Run development server
> After builds are complete, follow the same procedure from previous chapters to install them on a device or emulator/simulator.
Since we're identifying our development build with the `APP_VARIANT` environment variable, we need to pass it to the command when starting the development server. To do this, add a `dev` script in the [`"scripts"`](https://docs.npmjs.com/cli/v10/using-npm/scripts) field of our project's package.json:
package.json
Copy
```
{
 "scripts": {
  "dev": "APP_VARIANT=development npx expo start"
 }
}

```

Run the `npm run dev` command to start the development server:
Terminal
Copy
`- ``npm run dev`
This script will evaluate app.config.js locally and load the environment variable for the `development` profile.
Now, our development build will run on both Android and iOS, displaying the modified app name from app.config.js. For example, the below development build is running on an iOS Simulator. See that the app name is StickerSmash (Dev):
You can now continue using app.json for static values and use app.config.js for dynamic values.
## Summary
Chapter 5: Configure multiple app variants
We successfully created app.config.js just for our dynamic configuration while leaving static configuration in **app.json** unchanged, added environment variables in eas.json to configure specific build profile, and learned how to start the development server with a custom package.json script.
Mark this chapter as read
In the next chapter, learn about what are internal distribution builds, why we need them, and how to create them.
[Next: Create and share internal distribution build](https://docs.expo.dev/tutorial/eas/internal-distribution-builds)

