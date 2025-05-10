---
url: https://docs.expo.dev/versions/latest/sdk/webbrowser
title: https://docs.expo.dev/versions/latest/sdk/webbrowser
date: 2025-04-30T17:17:50.659167
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo WebBrowser
A library that provides access to the system's web browser and supports handling redirects.
Android
iOS
Web
Bundled version:
~14.0.2
`expo-web-browser` provides access to the system's web browser and supports handling redirects. On Android, it uses `ChromeCustomTabs` and on iOS, it uses `SFSafariViewController` or `ASWebAuthenticationSession`, depending on the method you call. As of iOS 11, `SFSafariViewController` no longer shares cookies with Safari, so if you are using `WebBrowser` for authentication you will want to use `WebBrowser.openAuthSessionAsync`, and if you just want to open a webpage (such as your app privacy policy), then use `WebBrowser.openBrowserAsync`.
## Installation
Terminal
Copy
`- ``npx expo install expo-web-browser`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Usage
Basic WebBrowser usage
```
import { useState } from 'react';
import { Button, Text, View, StyleSheet } from 'react-native';
import * as WebBrowser from 'expo-web-browser';
%%placeholder-start%%%%placeholder-end%%import Constants from 'expo-constants';
export default function App() {
 const [result, setResult] = useState(null);
 const _handlePressButtonAsync = async () => {
  let result = await WebBrowser.openBrowserAsync('https://expo.dev');
  setResult(result);
 };
 return (
  <View style={styles.container}><Button title="Open WebBrowser" onPress={_handlePressButtonAsync} /><Text>{result && JSON.stringify(result)}</Text></View>
 );
}
const styles = StyleSheet.create({
 container: {
  flex: 1,
  alignItems: 'center',
  justifyContent: 'center',
  paddingTop: Constants.statusBarHeight,
  backgroundColor: '#ecf0f1',
 },
});

Show More

```

### Handling deep links from the WebBrowser
With Expo Router
Without Expo Router
If your project uses Expo Router, deep links are handled automatically.
If you use the `WebBrowser` window for authentication or another use case where you want to pass information back into your app through a deep link, add a handler with `Linking.addEventListener` before opening the browser. When the listener fires, you should call [`dismissBrowser`](https://docs.expo.dev/versions/latest/sdk/webbrowser#webbrowserdismissbrowser). It will not automatically be dismissed when a deep link is handled. Aside from that, redirects from `WebBrowser` work the same as other deep links. Read more about it in [Linking](https://docs.expo.dev/linking/into-your-app#handle-urls).
## API
```
import * as WebBrowser from 'expo-web-browser';

```

## Methods
### `WebBrowser.coolDownAsync(browserPackage)`
Android
Parameter| Type| Description  
---|---|---  
browserPackage(optional)| `string`| Package of browser to be cooled. If not set, preferred browser will be used.  
This methods removes all bindings to services created by [`warmUpAsync`](https://docs.expo.dev/versions/latest/sdk/webbrowser/#webbrowserwarmupasyncbrowserpackage) or [`mayInitWithUrlAsync`](https://docs.expo.dev/versions/latest/sdk/webbrowser/#webbrowsermayinitwithurlasyncurl-browserpackage). You should call this method once you don't need them to avoid potential memory leaks. However, those binding would be cleared once your application is destroyed, which might be sufficient in most cases.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<WebBrowserCoolDownResult[](https://docs.expo.dev/versions/latest/sdk/webbrowser/#webbrowsercooldownresult)>`
The promise which fulfils with ` WebBrowserCoolDownResult` when cooling is performed, or an empty object when there was no connection to be dismissed.
### `WebBrowser.dismissAuthSession()`
iOS
Web
Dismisses the current authentication session. On web, it will close the popup window associated with auth process.
Returns:
`void`
The `void` on the successful attempt or throws an error if dismiss functionality is not available.
### `WebBrowser.dismissBrowser()`
iOS
Dismisses the presented web browser.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<{  type: WebBrowserResultType.DISMISS }>`
The promise that resolves with `{ type: 'dismiss' }` on the successful attempt or throws an error if dismiss functionality is not available.
### `WebBrowser.getCustomTabsSupportingBrowsersAsync()`
Android
Returns a list of applications package names supporting Custom Tabs, Custom Tabs service, user chosen and preferred one. This may not be fully reliable, since it uses `PackageManager.getResolvingActivities` under the hood. (For example, some browsers might not be present in browserPackages list once another browser is set to default.)
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<WebBrowserCustomTabsResults[](https://docs.expo.dev/versions/latest/sdk/webbrowser/#webbrowsercustomtabsresults)>`
The promise which fulfils with [`WebBrowserCustomTabsResults`](https://docs.expo.dev/versions/latest/sdk/webbrowser/#webbrowsercustomtabsresults) object.
### `WebBrowser.maybeCompleteAuthSession(options)`
Web
Parameter| Type  
---|---  
options(optional)| `WebBrowserCompleteAuthSessionOptions[](https://docs.expo.dev/versions/latest/sdk/webbrowser/#webbrowsercompleteauthsessionoptions)`  
Possibly completes an authentication session on web in a window popup. The method should be invoked on the page that the window redirects to.
Returns:
`WebBrowserCompleteAuthSessionResult[](https://docs.expo.dev/versions/latest/sdk/webbrowser/#webbrowsercompleteauthsessionresult)`
Returns an object with message about why the redirect failed or succeeded:
If `type` is set to `failed`, the reason depends on the message:
  * `Not supported on this platform`: If the platform doesn't support this method (Android, iOS).
  * `Cannot use expo-web-browser in a non-browser environment`: If the code was executed in an SSR or node environment.
  * `No auth session is currently in progress`: (the cached state wasn't found in local storage). This can happen if the window redirects to an origin (website) that is different to the initial website origin. If this happens in development, it may be because the auth started on localhost and finished on your computer port (Ex: `128.0.0.*`). This is controlled by the `redirectUrl` and `returnUrl`.
  * `Current URL "<URL>" and original redirect URL "<URL>" do not match`: This can occur when the redirect URL doesn't match what was initial defined as the `returnUrl`. You can skip this test in development by passing `{ skipRedirectCheck: true }` to the function.


If `type` is set to `success`, the parent window will attempt to close the child window immediately.
If the error `ERR_WEB_BROWSER_REDIRECT` was thrown, it may mean that the parent window was reloaded before the auth was completed. In this case you'll need to close the child window manually.
### `WebBrowser.mayInitWithUrlAsync(url, browserPackage)`
Android
Parameter| Type| Description  
---|---|---  
url| `string`| The url of page that is likely to be loaded first when opening browser.  
browserPackage(optional)| `string`| Package of browser to be informed. If not set, preferred browser will be used.  
This method initiates (if needed) [CustomTabsSession](https://developer.android.com/reference/android/support/customtabs/CustomTabsSession.html#maylaunchurl) and calls its `mayLaunchUrl` method for browser specified by the package.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<WebBrowserMayInitWithUrlResult[](https://docs.expo.dev/versions/latest/sdk/webbrowser/#webbrowsermayinitwithurlresult)>`
A promise which fulfils with `WebBrowserMayInitWithUrlResult` object.
### `WebBrowser.openAuthSessionAsync(url, redirectUrl, options)`
Android
iOS
Web
Parameter| Type| Description  
---|---|---  
url| `string`| The url to open in the web browser. This should be a login page.  
redirectUrl(optional)| `null | string`| _Optional_ - The url to deep link back into your app. On web, this defaults to the output of [`Linking.createURL("")`](https://docs.expo.dev/versions/latest/sdk/linking#linkingcreateurlpath-namedparameters).  
options(optional)| `AuthSessionOpenOptions[](https://docs.expo.dev/versions/latest/sdk/webbrowser/#authsessionopenoptions)`| _Optional_ - An object extending the [`WebBrowserOpenOptions`](https://docs.expo.dev/versions/latest/sdk/webbrowser/#webbrowseropenoptions). If there is no native AuthSession implementation available (which is the case on Android) these params will be used in the browser polyfill. If there is a native AuthSession implementation, these params will be ignored.Default:`{}`  
#### On Android:
This will be done using a "custom Chrome tabs" browser, [AppState](https://reactnative.dev/docs/appstate), and [Linking](https://docs.expo.dev/versions/latest/sdk/linking) APIs.
#### On iOS:
Opens the url with Safari in a modal using `ASWebAuthenticationSession`. The user will be asked whether to allow the app to authenticate using the given url. To handle redirection back to the mobile application, the redirect URI set in the authentication server has to use the protocol provided as the scheme in app.json [`expo.scheme`](https://docs.expo.dev/versions/latest/config/app#scheme). For example, `demo://` not `https://` protocol. Using `Linking.addEventListener` is not needed and can have side effects.
#### On web:
> This API can only be used in a secure environment (localhost/https). to test this. Otherwise, an error with code [`ERR_WEB_BROWSER_CRYPTO`](https://docs.expo.dev/versions/latest/sdk/webbrowser/#err_web_browser_crypto) will be thrown. This will use the browser's [`window.open()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/open) API.
  * _Desktop_ : This will create a new web popup window in the browser that can be closed later using `WebBrowser.maybeCompleteAuthSession()`.
  * _Mobile_ : This will open a new tab in the browser which can be closed using `WebBrowser.maybeCompleteAuthSession()`.


How this works on web:
  * A crypto state will be created for verifying the redirect. 
    * This means you need to run with `npx expo start --https`
  * The state will be added to the window's `localstorage`. This ensures that auth cannot complete unless it's done from a page running with the same origin as it was started. Ex: if `openAuthSessionAsync` is invoked on `https://localhost:19006`, then `maybeCompleteAuthSession` must be invoked on a page hosted from the origin `https://localhost:19006`. Using a different website, or even a different host like `https://128.0.0.*:19006` for example will not work.
  * A timer will be started to check for every 1000 milliseconds (1 second) to detect if the window has been closed by the user. If this happens then a promise will resolve with `{ type: 'dismiss' }`.


> On mobile web, Chrome and Safari will block any call to [`window.open()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/open) which takes too long to fire after a user interaction. This method must be invoked immediately after a user interaction. If the event is blocked, an error with code [`ERR_WEB_BROWSER_BLOCKED`](https://docs.expo.dev/versions/latest/sdk/webbrowser/#err_web_browser_blocked) will be thrown.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<WebBrowserAuthSessionResult[](https://docs.expo.dev/versions/latest/sdk/webbrowser/#webbrowserauthsessionresult)>`
  * If the user does not permit the application to authenticate with the given url, the Promise fulfills with `{ type: 'cancel' }` object.
  * If the user closed the web browser, the Promise fulfills with `{ type: 'cancel' }` object.
  * If the browser is closed using [`dismissBrowser`](https://docs.expo.dev/versions/latest/sdk/webbrowser/#webbrowserdismissbrowser), the Promise fulfills with `{ type: 'dismiss' }` object.


### `WebBrowser.openBrowserAsync(url, browserParams)`
Android
iOS
Web
Parameter| Type| Description  
---|---|---  
url| `string`| The url to open in the web browser.  
browserParams(optional)| `WebBrowserOpenOptions[](https://docs.expo.dev/versions/latest/sdk/webbrowser#webbrowseropenoptions)`| A dictionary of key-value pairs.Default:`{}`  
Opens the url with Safari in a modal on iOS using [`SFSafariViewController`](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller), and Chrome in a new [custom tab](https://developer.chrome.com/multidevice/android/customtabs) on Android. On iOS, the modal Safari will not share cookies with the system Safari. If you need this, use [`openAuthSessionAsync`](https://docs.expo.dev/versions/latest/sdk/webbrowser/#webbrowseropenauthsessionasyncurl-redirecturl-options).
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
The promise behaves differently based on the platform. On Android promise resolves with `{ type: 'opened' }` if we were able to open browser. On iOS:
  * If the user closed the web browser, the Promise resolves with `{ type: 'cancel' }`.
  * If the browser is closed using [`dismissBrowser`](https://docs.expo.dev/versions/latest/sdk/webbrowser/#webbrowserdismissbrowser), the Promise resolves with `{ type: 'dismiss' }`.


### `WebBrowser.warmUpAsync(browserPackage)`
Android
Parameter| Type| Description  
---|---|---  
browserPackage(optional)| `string`| Package of browser to be warmed up. If not set, preferred browser will be warmed.  
This method calls `warmUp` method on [CustomTabsClient](https://developer.android.com/reference/android/support/customtabs/CustomTabsClient.html#warmup\(long\)) for specified package.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<WebBrowserWarmUpResult[](https://docs.expo.dev/versions/latest/sdk/webbrowser/#webbrowserwarmupresult)>`
A promise which fulfils with `WebBrowserWarmUpResult` object.
## Types
### `AuthSessionOpenOptions`
Android
iOS
Web
If there is no native AuthSession implementation available (which is the case on Android) the params inherited from [`WebBrowserOpenOptions`](https://docs.expo.dev/versions/latest/sdk/webbrowser/#webbrowseropenoptions) will be used in the browser polyfill. Otherwise, the browser parameters will be ignored.
Type: `WebBrowserOpenOptions[](https://docs.expo.dev/versions/latest/sdk/webbrowser#webbrowseropenoptions)` extended by:
Property| Type| Description  
---|---|---  
preferEphemeralSession(optional)| `boolean`| Only for: iOSDetermines whether the session should ask the browser for a private authentication session. Set this to `true` to request that the browser doesn’t share cookies or other browsing data between the authentication session and the user’s normal browser session. Whether the request is honored depends on the user’s default web browser.Default:`false`  
### `WebBrowserAuthSessionResult`
Android
iOS
Web
Literal Type: `union`
Acceptable values are: `WebBrowserRedirectResult[](https://docs.expo.dev/versions/latest/sdk/webbrowser/#webbrowserredirectresult)` | `WebBrowserResult[](https://docs.expo.dev/versions/latest/sdk/webbrowser/#webbrowserresult)`
### `WebBrowserCompleteAuthSessionOptions`
Android
iOS
Web
Property| Type| Description  
---|---|---  
skipRedirectCheck(optional)| `boolean`| Attempt to close the window without checking to see if the auth redirect matches the cached redirect URL.  
### `WebBrowserCompleteAuthSessionResult`
Android
iOS
Web
Property| Type| Description  
---|---|---  
message| `string`| Additional description or reasoning of the result.  
type| `'success' | 'failed'`| Type of the result.  
### `WebBrowserCoolDownResult`
Android
iOS
Web
Type: `ServiceActionResult`
### `WebBrowserCustomTabsResults`
Android
iOS
Web
Property| Type| Description  
---|---|---  
browserPackages| `string[]`| All packages recognized by `PackageManager` as capable of handling Custom Tabs. Empty array means there is no supporting browsers on device.  
defaultBrowserPackage(optional)| `string`| Default package chosen by user, `null` if there is no such packages. Also `null` usually means, that user will be prompted to choose from available packages.  
preferredBrowserPackage(optional)| `string`| Package preferred by `CustomTabsClient` to be used to handle Custom Tabs. It favors browser chosen by user as default, as long as it is present on both `browserPackages` and `servicePackages` lists. Only such browsers are considered as fully supporting Custom Tabs. It might be `null` when there is no such browser installed or when default browser is not in `servicePackages` list.  
servicePackages| `string[]`| All packages recognized by `PackageManager` as capable of handling Custom Tabs Service. This service is used by [`warmUpAsync`](https://docs.expo.dev/versions/latest/sdk/webbrowser/#webbrowserwarmupasyncbrowserpackage), [`mayInitWithUrlAsync`](https://docs.expo.dev/versions/latest/sdk/webbrowser/#webbrowsermayinitwithurlasyncurl-browserpackage) and [`coolDownAsync`](https://docs.expo.dev/versions/latest/sdk/webbrowser/#webbrowsercooldownasyncbrowserpackage).  
### `WebBrowserMayInitWithUrlResult`
Android
iOS
Web
Type: `ServiceActionResult`
### `WebBrowserOpenOptions`
Android
iOS
Web
Property| Type| Description  
---|---|---  
browserPackage(optional)| `string`| Only for: AndroidPackage name of a browser to be used to handle Custom Tabs. List of available packages is to be queried by [`getCustomTabsSupportingBrowsers`](https://docs.expo.dev/versions/latest/sdk/webbrowser/#webbrowsergetcustomtabssupportingbrowsersasync) method.  
controlsColor(optional)| `string`| Only for: iOSTint color for controls in SKSafariViewController. Supports React Native [color formats](https://reactnative.dev/docs/colors).  
createTask(optional)| `boolean`| Only for: AndroidA boolean determining whether the browser should open in a new task or in the same task as your app.Default:`true`  
dismissButtonStyle(optional)| `'done' | 'close' | 'cancel'`| Only for: iOSThe style of the dismiss button. Should be one of: `done`, `close`, or `cancel`.  
enableBarCollapsing(optional)| `boolean`| A boolean determining whether the toolbar should be hiding when a user scrolls the website.  
enableDefaultShareMenuItem(optional)| `boolean`| Only for: AndroidA boolean determining whether a default share item should be added to the menu.  
presentationStyle(optional)| `WebBrowserPresentationStyle[](https://docs.expo.dev/versions/latest/sdk/webbrowser/#webbrowserpresentationstyle)`| Only for: iOSThe [presentation style](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621355-modalpresentationstyle) of the browser window.Default:`WebBrowser.WebBrowserPresentationStyle.OverFullScreen`  
readerMode(optional)| `boolean`| Only for: iOSA boolean determining whether Safari should enter Reader mode, if it is available.  
secondaryToolbarColor(optional)| `string`| Only for: AndroidColor of the secondary toolbar. Supports React Native [color formats](https://reactnative.dev/docs/colors).  
showInRecents(optional)| `boolean`| Only for: AndroidA boolean determining whether browsed website should be shown as separate entry in Android recents/multitasking view. Requires `createTask` to be `true` (default).Default:`false`  
showTitle(optional)| `boolean`| Only for: AndroidA boolean determining whether the browser should show the title of website on the toolbar.  
toolbarColor(optional)| `string`| Color of the toolbar. Supports React Native [color formats](https://reactnative.dev/docs/colors).  
windowFeatures(optional)| `string | WebBrowserWindowFeatures[](https://docs.expo.dev/versions/latest/sdk/webbrowser#webbrowserwindowfeatures)`| Only for: WebFeatures to use with `window.open()`.  
windowName(optional)| `string`| Only for: WebName to assign to the popup window.  
### `WebBrowserRedirectResult`
Android
iOS
Web
Property| Type| Description  
---|---|---  
type| `'success'`| Type of the result.  
url| `string`  
### `WebBrowserResult`
Android
iOS
Web
Property| Type| Description  
---|---|---  
type| `WebBrowserResultType[](https://docs.expo.dev/versions/latest/sdk/webbrowser/#webbrowserresulttype)`| Type of the result.  
### `WebBrowserWarmUpResult`
Android
iOS
Web
Type: `ServiceActionResult`
### `WebBrowserWindowFeatures`
Android
iOS
Web
Type: `Record<string, number | boolean | string>`
## Enums
### `WebBrowserPresentationStyle`
iOS
A browser presentation style. Its values are directly mapped to the [`UIModalPresentationStyle`](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621355-modalpresentationstyle).
#### `AUTOMATIC`
iOS
`WebBrowserPresentationStyle.AUTOMATIC ＝ "automatic"`
The default presentation style chosen by the system. On older iOS versions, falls back to `WebBrowserPresentationStyle.FullScreen`.
#### `CURRENT_CONTEXT`
`WebBrowserPresentationStyle.CURRENT_CONTEXT ＝ "currentContext"`
A presentation style where the browser is displayed over the app's content.
#### `FORM_SHEET`
`WebBrowserPresentationStyle.FORM_SHEET ＝ "formSheet"`
A presentation style that displays the browser centered in the screen.
#### `FULL_SCREEN`
`WebBrowserPresentationStyle.FULL_SCREEN ＝ "fullScreen"`
A presentation style in which the presented browser covers the screen.
#### `OVER_CURRENT_CONTEXT`
`WebBrowserPresentationStyle.OVER_CURRENT_CONTEXT ＝ "overCurrentContext"`
A presentation style where the browser is displayed over the app's content.
#### `OVER_FULL_SCREEN`
`WebBrowserPresentationStyle.OVER_FULL_SCREEN ＝ "overFullScreen"`
A presentation style in which the browser view covers the screen.
#### `PAGE_SHEET`
`WebBrowserPresentationStyle.PAGE_SHEET ＝ "pageSheet"`
A presentation style that partially covers the underlying content.
#### `POPOVER`
`WebBrowserPresentationStyle.POPOVER ＝ "popover"`
A presentation style where the browser is displayed in a popover view.
### `WebBrowserResultType`
Android
iOS
Web
#### `CANCEL`
iOS
`WebBrowserResultType.CANCEL ＝ "cancel"`
#### `DISMISS`
iOS
`WebBrowserResultType.DISMISS ＝ "dismiss"`
#### `LOCKED`
`WebBrowserResultType.LOCKED ＝ "locked"`
#### `OPENED`
Android
`WebBrowserResultType.OPENED ＝ "opened"`
## Error codes
### `ERR_WEB_BROWSER_REDIRECT`
Web only: The window cannot complete the redirect request because the invoking window doesn't have a reference to its parent. This can happen if the parent window was reloaded.
### `ERR_WEB_BROWSER_BLOCKED`
Web only: The popup window was blocked by the browser or failed to open. This can happen in mobile browsers when the `window.open()` method was invoked too long after a user input was fired.
Mobile browsers do this to prevent malicious websites from opening many unwanted popups on mobile.
You're method can still run in an async function but there cannot be any long running tasks before it. You can use hooks to disable user-inputs until any other processes have finished loading.
### `ERR_WEB_BROWSER_CRYPTO`
Web only: The current environment doesn't support crypto. Ensure you are running from a secure origin (localhost/https).

