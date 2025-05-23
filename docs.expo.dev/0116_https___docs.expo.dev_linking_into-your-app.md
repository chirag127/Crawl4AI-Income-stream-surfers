---
url: https://docs.expo.dev/linking/into-your-app
title: https://docs.expo.dev/linking/into-your-app
date: 2025-04-30T17:14:04.150844
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Linking into your app
Learn how to handle an incoming URL in your React Native and Expo app by creating a deep link.
This guide provides steps to configure standard deep links in your project by adding a custom scheme.
> For most apps, you probably want to set up [Android App/iOS Universal Links](https://docs.expo.dev/linking/overview#universal-linking) instead of the deep links described in this guide or set up both.
## Add a custom scheme in app config
To provide a link to your app, add a custom string to the [`scheme`](https://docs.expo.dev/versions/latest/config/app#scheme) property in the [app config](https://docs.expo.dev/workflow/configuration):
app.json
Copy
```
{
 "expo": {
  "scheme": "myapp"
 }
}

```

After adding a custom scheme to your app, you need to [create a new development build](https://docs.expo.dev/develop/development-builds/create-a-build). Once the app is installed on a device, you can open links within your app using `myapp://`.
If the custom scheme is not defined, the app will use `android.package` and `ios.bundleIdentifier` as the default schemes in both development and production builds. This is because [Expo Prebuild](https://docs.expo.dev/workflow/prebuild) automatically adds these properties as custom schemes for Android and iOS.
## Test the deep link
You can test a link that opens your app using [`npx uri-scheme`](https://github.com/expo/expo/tree/main/packages/uri-scheme#readme), which is a command-line utility for interacting and testing URI schemes.
For example, if your app has a `/details` screen that you want to open when a user taps on a link (either through another app or a web browser), you can test this behavior by running the following command:
Terminal
`# If you have `android.package` or `ios.bundleIdentifier` defined in your app.json`
`- ``npx uri-scheme open com.example.app://somepath/details --android`
`# If you have a `scheme` defined in your app.json`
`- ``npx uri-scheme open myapp://somepath/details --ios`
Running the above command:
  * Opens your app's `/details` screen
  * The `android` or `ios` options specify that the link should be opened on Android or iOS
  * Alternatively, you can try opening the link by clicking a link like `<a href="scheme://">Click me</a>` in the device's web browser. Note that entering the link in the address bar may not work as expected, and you can use [universal linking](https://docs.expo.dev/linking/overview#universal-linking) to implement that ability.

Test a link using Expo Go
By default, [Expo Go](https://expo.dev/go) uses the `exp://` scheme. If you link to `exp://` without specifying a URL address afterward, it will open the app to the home screen. In development, your app's complete URL looks like `exp://127.0.0.1:8081`.
To open the `/details` screen while testing on Expo Go, you can use `npx uri-scheme`:
Terminal
Copy
`- ``npx uri-scheme open exp://127.0.0.1:8081/--/somepath/into/app?hello=world --ios`
In Expo Go, `/--/` is added to the URL when a path is specified. This indicates to Expo Go that the substring after it corresponds to the deep link path and is not part of the path to the app itself.
By default, `exp://` is replaced with `http://` when opening a URL in Expo Go. You can also use `exps://` to open `https://` URLs. However, `exps://` does not currently support loading sites with insecure TLS certificates.
## Handle URLs
> If you are using [Expo Router](https://docs.expo.dev/linking/overview#use-expo-router-to-handle-deep-linking), you can ignore this section.
You can observe links that launch your app using the [`Linking.useURL()`](https://docs.expo.dev/versions/latest/sdk/linking#useurl) hook from [`expo-linking`](https://docs.expo.dev/versions/latest/sdk/linking).
index.tsx
Copy
```
import * as Linking from 'expo-linking';
export default function Home() {
 const url = Linking.useURL();
 return <Text>URL: {url}</Text>;
}

```

The `Linking.useURL()` hook works behind the scenes by following these imperative methods:
  * The link that launched the app is initially returned using [`Linking.getInitialURL()`](https://docs.expo.dev/versions/latest/sdk/linking#linkinggetinitialurl)
  * Any new links triggered while the app is already open are observed with [`Linking.addEventListener('url', callback)`](https://docs.expo.dev/versions/latest/sdk/linking#linkingaddeventlistenertype-handler)


## Parse URLs
You can use the [`Linking.parse()`](https://docs.expo.dev/versions/latest/sdk/linking#linkingparseurl) method to parse the path, hostname, and query parameters from a URL. This method extracts deep linking information and considers nonstandard implementations.
index.tsx
Copy
```
import * as Linking from 'expo-linking';
export default function Home() {
 const url = Linking.useURL();
 if (url) {
  const { hostname, path, queryParams } = Linking.parse(url);
  console.log(
   `Linked to app with hostname: ${hostname}, path: ${path} and data: ${JSON.stringify(
    queryParams
   )}`
  );
 }
 return (
  %%placeholder-start%%Your React component here. %%placeholder-end%%
 )
}

```

## Limitations
If a user does not have your app installed, deep links to your app will not work. Attribution services like [Branch](https://www.branch.io/deep-linking/) offer solutions for conditionally linking to your app or web page.
Android App/iOS Universal Links is another solution you can use to handle such cases. This type of linking allows your app to open when a user clicks follows an HTTP(S) link pointing to your web domain. If the user doesn't have your app installed, the link takes them to your website. For more details, see [universal linking](https://docs.expo.dev/linking/overview#universal-linking).

