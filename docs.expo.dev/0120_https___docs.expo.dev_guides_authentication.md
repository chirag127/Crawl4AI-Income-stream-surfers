---
url: https://docs.expo.dev/guides/authentication
title: https://docs.expo.dev/guides/authentication
date: 2025-04-30T17:14:04.167361
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Authentication with OAuth or OpenID providers
Learn how to utilize the expo-auth-session library to implement authentication with OAuth or OpenID providers.
[`expo-auth-session`](https://docs.expo.dev/versions/latest/sdk/auth-session) provides a unified API for implementing OAuth and OpenID Connect providers on Android, iOS, and web. This guide will show you how to use the `AuthSession` API using a few examples.
## Rules for all authentication providers
When using the `AuthSession` API, the following rules apply to all authentication providers:
  * Use `WebBrowser.maybeCompleteAuthSession()` to dismiss the web popup. If you forget to add this then the popup window will not close.
  * Create redirects with `AuthSession.makeRedirectUri()` this does a lot of the heavy lifting involved with universal platform support. Behind the scenes, it uses `expo-linking`.
  * Build requests using `AuthSession.useAuthRequest()`, the hook allows for async setup which means mobile browsers won't block the authentication.
  * Be sure to disable the prompt until `request` is defined.
  * You can only invoke `promptAsync` in user interaction on the web.
  * Expo Go cannot be used for local development and testing of OAuth or OpenID Connect-enabled apps due to the inability to customize your app scheme. You can instead use a [Development Build](https://docs.expo.dev/develop/development-builds/introduction), which enables an Expo Go-like development experience and supports OAuth redirects back to your app after login in a manner that works just like it would in production.


## Obtaining access tokens
Most providers use the [OAuth 2](https://oauth.net/2/) standard for secure authentication and authorization. In the authorization code grant, the identity provider returns a one-time code. This code is then exchanged for the user's access token.
Since [your client application code is not a secure place to store secrets](https://reactnative.dev/docs/security#storing-sensitive-info), it is necessary to exchange the authorization code in a server such as with [API routes](https://docs.expo.dev/router/reference/api-routes) or [React Server Components](https://docs.expo.dev/guides/server-components). This will allow you to securely store and use a client secret to access the provider's token endpoint.
## Examples
The following examples show how to use the `AuthSession` API to authenticate with a few popular providers.
### GitHub
[Create GitHub App](https://github.com/settings/developers)
Website| Provider| PKCE| Auto Discovery  
---|---|---|---  
OAuth 2.0| Supported| Not Available  
  * Provider only allows one redirect URI per app. You'll need an individual app for every method you want to use: 
    * Standalone / development build: `com.your.app://*`
    * Web: `https://yourwebsite.com/*`
  * The `redirectUri` requires two slashes (`://`).
  * `revocationEndpoint` is dynamic and requires your `config.clientId`.


GitHub Auth Example
Copy
```
import { useEffect } from 'react';
import * as WebBrowser from 'expo-web-browser';
import { makeRedirectUri, useAuthRequest } from 'expo-auth-session';
import { Button } from 'react-native';
WebBrowser.maybeCompleteAuthSession();
// Endpoint
const discovery = {
 authorizationEndpoint: 'https://github.com/login/oauth/authorize',
 tokenEndpoint: 'https://github.com/login/oauth/access_token',
 revocationEndpoint: 'https://github.com/settings/connections/applications/<CLIENT_ID>',
};
export default function App() {
 const [request, response, promptAsync] = useAuthRequest(
  {
   clientId: 'CLIENT_ID',
   scopes: ['identity'],
   redirectUri: makeRedirectUri({
    scheme: 'your.app'
   }),
  },
  discovery
 );
 useEffect(() => {
  if (response?.type === 'success') {
   const { code } = response.params;
  }
 }, [response]);
 return (
  <Button
   disabled={!request}
   title="Login"
   onPress={() => {
    promptAsync();
   }}
  />
 );
}

Show More

```

Website| Provider| PKCE| Auto Discovery  
---|---|---|---  
[Sign-up](https://developer.okta.com/signup/) > Applications| OpenID| Supported| Available  
  * You cannot define a custom `redirectUri`, Okta will provide you with one.


Okta Auth Example
Copy
```
import { useEffect } from 'react';
import * as WebBrowser from 'expo-web-browser';
import { makeRedirectUri, useAuthRequest, useAutoDiscovery } from 'expo-auth-session';
import { Button, Platform } from 'react-native';
WebBrowser.maybeCompleteAuthSession();
export default function App() {
 // Endpoint
 const discovery = useAutoDiscovery('https://<OKTA_DOMAIN>.com/oauth2/default');
 // Request
 const [request, response, promptAsync] = useAuthRequest(
  {
   clientId: 'CLIENT_ID',
   scopes: ['openid', 'profile'],
   redirectUri: makeRedirectUri({
    native: 'com.okta.<OKTA_DOMAIN>:/callback',
   }),
  },
  discovery
 );
 useEffect(() => {
  if (response?.type === 'success') {
   const { code } = response.params;
  }
 }, [response]);
 return (
  <Button
   disabled={!request}
   title="Login"
   onPress={() => {
    promptAsync();
   }}
  />
 );
}

Show More

```

## Redirect URI patterns
Here are a few examples of some common redirect URI patterns you may end up using.
### Standalone/development build
> `yourscheme://path`
In some cases there will be anywhere between 1 to 3 slashes (`/`).
  * Environment:
    * Bare workflow 
      * `npx expo prebuild`
    * Standalone builds in the App or Play Store or testing locally 
      * Android: `eas build` or `npx expo run:android`
      * iOS: `eas build` or `npx expo run:ios`
  * Create: Use `AuthSession.makeRedirectUri({ native: '<YOUR_URI>' })` to select native when running in the correct environment.
    * `your.app://redirect` -> `makeRedirectUri({ scheme: 'your.app', path: 'redirect' })`
    * `your.app:///` -> `makeRedirectUri({ scheme: 'your.app', isTripleSlashed: true })`
    * `your.app:/authorize` -> `makeRedirectUri({ native: 'your.app:/authorize' })`
    * `your.app://auth?foo=bar` -> `makeRedirectUri({ scheme: 'your.app', path: 'auth', queryParams: { foo: 'bar' } })`
    * `exp://u.expo.dev/[project-id]?channel-name=[channel-name]&runtime-version=[runtime-version]` -> `makeRedirectUri()`
    * This link can often be created automatically but we recommend you define the `scheme` property at least. The entire URL can be overridden in apps by passing the `native` property. Often this will be used for providers like Google or Okta which require you to use a custom native URI redirect. You can add, list, and open URI schemes using `npx uri-scheme`.
    * If you change the `expo.scheme` after ejecting then you'll need to use the `expo apply` command to apply the changes to your native project, then rebuild them (`yarn ios`, `yarn android`).
  * Usage: `promptAsync({ redirectUri })`


## Improving user experience
The "login flow" is an important thing to get right, in a lot of cases this is where the user will _commit_ to using your app again. A bad experience can cause users to give up on your app before they've really gotten to use it.
Here are a few tips you can use to make authentication quick, easy, and secure for your users:
### Warming the browser
On Android you can optionally warm up the web browser before it's used. This allows the browser app to pre-initialize itself in the background. Doing this can significantly speed up prompting the user for authentication.
```
import { useEffect } from 'react';
import * as WebBrowser from 'expo-web-browser';
function App() {
 useEffect(() => {
  WebBrowser.warmUpAsync();
  return () => {
   WebBrowser.coolDownAsync();
  };
 }, []);
 // Do authentication ...
}

```

### Implicit login
Because there was no secure way to do this to store client secrets in your app bundle, historically, many providers have offered an "Implicit flow" which enables you to request an access token without the client secret. This is no longer recommended due to inherent security risks, including the risk of access token injection. Instead, most providers now support the authorization code with PKCE (Proof Key for Code Exchange) extension to securely exchange an authorization code for an access token within your client app code. Learn more about [transitioning from Implicit flow to authorization code with PKCE](https://oauth.net/2/grant-types/implicit/).
`expo-auth-session` still supports Implicit flow for legacy code purposes. Below is an example implementation of the Implicit flow.
```
import { useEffect } from 'react';
import * as WebBrowser from 'expo-web-browser';
import { makeRedirectUri, useAuthRequest, ResponseType } from 'expo-auth-session';
WebBrowser.maybeCompleteAuthSession();
// Endpoint
const discovery = {
 authorizationEndpoint: 'https://accounts.spotify.com/authorize',
};
function App() {
 const [request, response, promptAsync] = useAuthRequest(
  {
   responseType: ResponseType.Token,
   clientId: 'CLIENT_ID',
   scopes: ['user-read-email', 'playlist-modify-public'],
   redirectUri: makeRedirectUri({
    scheme: 'your.app'
   }),
  },
  discovery
 );
 useEffect(() => {
  if (response && response.type === 'success') {
   const token = response.params.access_token;
  }
 }, [response]);
 return <Button disabled={!request} onPress={() => promptAsync()} title="Login" />;
}

Show More

```

### Storing data
On native platforms such as Android and iOS, you can secure things like access tokens locally using a library called [`expo-secure-store`](https://docs.expo.dev/versions/latest/sdk/securestore) (This is different to `AsyncStorage` which is not secure). It provides native access to encrypted [`SharedPreferences`](https://developer.android.com/training/basics/data-storage/shared-preferences.html) on Android and [keychain services](https://developer.apple.com/documentation/security/keychain_services) on iOS and . There is no web equivalent to this functionality.
You can store your authentication results and rehydrate them later to avoid having to prompt the user to login again.
```
import * as SecureStore from 'expo-secure-store';
const MY_SECURE_AUTH_STATE_KEY = 'MySecureAuthStateKey';
function App() {
 const [, response] = useAuthRequest({});
 useEffect(() => {
  if (response && response.type === 'success') {
   const auth = response.params;
   const storageValue = JSON.stringify(auth);
   if (Platform.OS !== 'web') {
    // Securely store the auth on your device
    SecureStore.setItemAsync(MY_SECURE_AUTH_STATE_KEY, storageValue);
   }
  }
 }, [response]);
 // More login code...
}

Show More

```


