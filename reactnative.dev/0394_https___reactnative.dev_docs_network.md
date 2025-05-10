---
url: https://reactnative.dev/docs/network
title: https://reactnative.dev/docs/network
date: 2025-05-10T21:41:01.612679
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/network#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
Many mobile apps need to load resources from a remote URL. You may want to make a POST request to a REST API, or you may need to fetch a chunk of static content from another server.
## Using Fetch[​](https://reactnative.dev/docs/network#using-fetch "Direct link to Using Fetch")
React Native provides the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) for your networking needs. Fetch will seem familiar if you have used `XMLHttpRequest` or other networking APIs before. You may refer to MDN's guide on [Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) for additional information.
### Making requests[​](https://reactnative.dev/docs/network#making-requests "Direct link to Making requests")
In order to fetch content from an arbitrary URL, you can pass the URL to fetch:
tsx
```
fetch('https://mywebsite.com/mydata.json');
```

Fetch also takes an optional second argument that allows you to customize the HTTP request. You may want to specify additional headers, or make a POST request:
tsx
```
fetch('https://mywebsite.com/endpoint/',{ method:'POST', headers:{Accept:'application/json','Content-Type':'application/json', body:JSON.stringify({  firstParam:'yourValue',  secondParam:'yourOtherValue',}),});
```

Take a look at the [Fetch Request docs](https://developer.mozilla.org/en-US/docs/Web/API/Request) for a full list of properties.
### Handling the response[​](https://reactnative.dev/docs/network#handling-the-response "Direct link to Handling the response")
The above examples show how you can make a request. In many cases, you will want to do something with the response.
Networking is an inherently asynchronous operation. Fetch method will return a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that makes it straightforward to write code that works in an asynchronous manner:
tsx
```
constgetMoviesFromApi=()=>{returnfetch('https://reactnative.dev/movies.json').then(response => response.json()).then(json =>{return json.movies;.catch(error =>{console.error(error);});
```

You can also use the `async` / `await` syntax in a React Native app:
tsx
```
constgetMoviesFromApiAsync=async()=>{try{const response =awaitfetch('https://reactnative.dev/movies.json',const json =await response.json();return json.movies;}catch(error){console.error(error);
```

Don't forget to catch any errors that may be thrown by `fetch`, otherwise they will be dropped silently.
  * TypeScript
  * JavaScript


> By default, iOS 9.0 or later enforce App Transport Security (ATS). ATS requires any HTTP connection to use HTTPS. If you need to fetch from a cleartext URL (one that begins with `http`) you will first need to [add an ATS exception](https://reactnative.dev/docs/integration-with-existing-apps#test-your-integration). If you know ahead of time what domains you will need access to, it is more secure to add exceptions only for those domains; if the domains are not known until runtime you can [disable ATS completely](https://reactnative.dev/docs/publishing-to-app-store#1-enable-app-transport-security). Note however that from January 2017, [Apple's App Store review will require reasonable justification for disabling ATS](https://forums.developer.apple.com/thread/48979). See [Apple's documentation](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW33) for more information.
> On Android, as of API Level 28, clear text traffic is also blocked by default. This behaviour can be overridden by setting [`android:usesCleartextTraffic`](https://developer.android.com/guide/topics/manifest/application-element#usesCleartextTraffic) in the app manifest file.
## Using Other Networking Libraries[​](https://reactnative.dev/docs/network#using-other-networking-libraries "Direct link to Using Other Networking Libraries")
The [XMLHttpRequest API](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) is built into React Native. This means that you can use third party libraries such as [frisbee](https://github.com/niftylettuce/frisbee) or [axios](https://github.com/axios/axios) that depend on it, or you can use the XMLHttpRequest API directly if you prefer.
tsx
```
const request =newXMLHttpRequest();request.onreadystatechange= e =>{if(request.readyState!==4){return;if(request.status===200){console.log('success', request.responseText);}else{console.warn('error');request.open('GET','https://mywebsite.com/endpoint/');request.send();
```

> The security model for XMLHttpRequest is different than on web as there is no concept of [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) in native apps.
## WebSocket Support[​](https://reactnative.dev/docs/network#websocket-support "Direct link to WebSocket Support")
React Native also supports [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket), a protocol which provides full-duplex communication channels over a single TCP connection.
tsx
```
const ws =newWebSocket('ws://host.com/path');ws.onopen=()=>{// connection opened ws.send('something');// send a messagews.onmessage= e =>{// a message was receivedconsole.log(e.data);ws.onerror= e =>{// an error occurredconsole.log(e.message);ws.onclose= e =>{// connection closedconsole.log(e.code, e.reason);
```

## Known Issues with `fetch` and cookie based authentication[​](https://reactnative.dev/docs/network#known-issues-with-fetch-and-cookie-based-authentication "Direct link to known-issues-with-fetch-and-cookie-based-authentication")
The following options are currently not working with `fetch`
  * `redirect:manual`
  * `credentials:omit`


  * Having same name headers on Android will result in only the latest one being present. A temporary solution can be found here: <https://github.com/facebook/react-native/issues/18837#issuecomment-398779994>.
  * Cookie based authentication is currently unstable. You can view some of the issues raised here: <https://github.com/facebook/react-native/issues/23185>
  * As a minimum on iOS, when redirected through a `302`, if a `Set-Cookie` header is present, the cookie is not set properly. Since the redirect cannot be handled manually this might cause a scenario where infinite requests occur if the redirect is the result of an expired session.


## Configuring NSURLSession on iOS[​](https://reactnative.dev/docs/network#configuring-nsurlsession-on-ios "Direct link to Configuring NSURLSession on iOS")
For some applications it may be appropriate to provide a custom `NSURLSessionConfiguration` for the underlying `NSURLSession` that is used for network requests in a React Native application running on iOS. For instance, one may need to set a custom user agent string for all network requests coming from the app or supply `NSURLSession` with an ephemeral `NSURLSessionConfiguration`. The function `RCTSetCustomNSURLSessionConfigurationProvider` allows for such customization. Remember to add the following import to the file in which `RCTSetCustomNSURLSessionConfigurationProvider` will be called:
objectivec
```
#import<React/RCTHTTPRequestHandler.h>
```

`RCTSetCustomNSURLSessionConfigurationProvider` should be called early in the application life cycle such that it is readily available when needed by React, for instance:
objectivec
```
-(void)application:(__unused UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {// set RCTSetCustomNSURLSessionConfigurationProviderRCTSetCustomNSURLSessionConfigurationProvider(^NSURLSessionConfiguration *{   NSURLSessionConfiguration *configuration =[NSURLSessionConfiguration defaultSessionConfiguration];// configure the sessionreturn configuration;});// set up React _bridge =[[RCTBridge alloc] initWithDelegate:self launchOptions:launchOptions];
```

Is this page useful?
  * [Using Fetch](https://reactnative.dev/docs/network#using-fetch)
    * [Making requests](https://reactnative.dev/docs/network#making-requests)
    * [Handling the response](https://reactnative.dev/docs/network#handling-the-response)
  * [Using Other Networking Libraries](https://reactnative.dev/docs/network#using-other-networking-libraries)
  * [WebSocket Support](https://reactnative.dev/docs/network#websocket-support)
  * [Known Issues with `fetch` and cookie based authentication](https://reactnative.dev/docs/network#known-issues-with-fetch-and-cookie-based-authentication)
  * [Configuring NSURLSession on iOS](https://reactnative.dev/docs/network#configuring-nsurlsession-on-ios)



