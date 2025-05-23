---
url: https://docs.expo.dev/versions/latest/sdk/router
title: https://docs.expo.dev/versions/latest/sdk/router
date: 2025-04-30T17:17:16.045676
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo Router
A file-based routing library for React Native and web applications.
Android
iOS
tvOS
Web
Bundled version:
~4.0.20
`expo-router` is a routing library for React Native and web apps. It enables navigation management using a file-based routing system and provides native navigation components and is built on top of [React Navigation](https://reactnavigation.org/).
## Installation
To use Expo Router in your project, you need to install. Follow the instructions from the [Install Expo Router](https://docs.expo.dev/router/installation) guide.
## Configuration in app config
If you are using the [default](https://docs.expo.dev/more/create-expo#--template) template to create a new project, `expo-router` [config plugin](https://docs.expo.dev/config-plugins/introduction) is automatically configured in the app config automatically.
### Example app.json with config plugin
app.json
Copy
```
{
 "expo": {
  "plugins": ["expo-router"]
 }
}

```

## Usage
Find more information and guides about using `expo-router` in [Expo Router](https://docs.expo.dev/router/introduction) section.
## API
```
import { Stack, Tabs, Link } from 'expo-router';

```

## Components
### `ErrorBoundary`
Android
iOS
tvOS
Web
Type: `React.Element[](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<ErrorBoundaryProps[](https://docs.expo.dev/versions/latest/sdk/router/#errorboundaryprops)>`
Props passed to a page's `ErrorBoundary` export.
ErrorBoundaryProps
### `error`
Android
iOS
tvOS
Web
Type: 
The error that was thrown.
### `retry`
Android
iOS
tvOS
Web
Type: `() => Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
A function that will re-render the route component by clearing the `error` state.
### `Link`
Android
iOS
tvOS
Web
Type: `React.Element[](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<PropsWithChildren<>>`
Component that renders a link using [`href`](https://docs.expo.dev/versions/latest/sdk/router/#href) to another route. By default, it accepts children and wraps them in a `<Text>` component.
Uses an anchor tag (`<a>`) on web and performs a client-side navigation to preserve the state of the website and navigate faster. The web-only attributes such as `target`, `rel`, and `download` are supported and passed to the anchor tag on web. See [`WebAnchorProps`](https://docs.expo.dev/versions/latest/sdk/router/#webanchorprops) for more details.
> Note: Client-side navigation works with both single-page apps, and [static-rendering](https://docs.expo.dev/router/reference/static-rendering).
Example
```
import { Link } from 'expo-router';
import { View } from 'react-native';
export default function Route() {
 return (
 <View><Link href="/about">About</Link></View>
 );
}

```

LinkProps
### `asChild`
Android
iOS
tvOS
Web
Optional • Type: `boolean`
Used to customize the `Link` component. It will forward all props to the first child of the `Link`. Note that the child component must accept `onPress` or `onClick` props. The `href` and `role` are also passed to the child.
Example
```
import { Link } from 'expo-router';
import { Pressable, Text } from 'react-native';
export default function Route() {
 return (
 <View><Link href="/home" asChild><Pressable><Text>Home</Text></Pressable></Link></View>
 );
}

```

### `className`
Android
iOS
tvOS
Web
Optional • Type: `string`
On native, this can be used with CSS interop tools like Nativewind. On web, this sets the HTML `class` directly.
### `dismissTo`
Android
iOS
tvOS
Web
Optional • Type: `boolean`
While in a stack, this will dismiss screens until the provided href is reached. If the href is not found, it will instead replace the current screen with the provided href.
Example
```
import { Link } from 'expo-router';
import { View } from 'react-native';
export default function Route() {
 return (
 <View><Link dismissTo href="/feed">Close modal</Link></View>
 );
}

```

### `href`
Android
iOS
tvOS
Web
Literal type: `union`
The path of the route to navigate to. It can either be:
  * string: A full path like `/profile/settings` or a relative path like `../settings`.
  * object: An object with a `pathname` and optional `params`. The `pathname` can be a full path like `/profile/settings` or a relative path like `../settings`. The params can be an object of key-value pairs.


Example
Dynamic
Copy
```
import { Link } from 'expo-router';
import { View } from 'react-native';
export default function Route() {
 return (
 <View><Link href="/about">About</Link><Link
  href={{
   pathname: '/user/[id]',
   params: { id: 'bacon' }
  }}>
   View user
  </Link></View>
 );
}

```

Acceptable values are: `string` | 
### `onPress`
Android
iOS
tvOS
Web
Optional • Type: `(e: MouseEvent[](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent)<> | GestureResponderEvent) => void`
This function is called on press. Text intrinsically supports press handling with a default highlight state (which can be disabled with suppressHighlighting).
### `push`
Android
iOS
tvOS
Web
Optional • Type: `boolean`
Always pushes a new route, and never pops or replaces to existing route. You can push the current route multiple times or with new parameters.
Example
```
import { Link } from 'expo-router';
import { View } from 'react-native';
export default function Route() {
 return (
 <View><Link push href="/feed">Login</Link></View>
 );
}

```

### `relativeToDirectory`
Android
iOS
tvOS
Web
Optional • Type: `boolean`
Relative URL references are either relative to the directory or the document. By default, relative paths are relative to the document.
> See: [Resolving relative references in Mozilla's documentation](https://developer.mozilla.org/en-US/docs/Web/API/URL_API/Resolving_relative_references).
### `replace`
Android
iOS
tvOS
Web
Optional • Type: `boolean`
Removes the current route from the history and replace it with the specified URL. This is useful for [redirects](https://docs.expo.dev/router/reference/redirects).
Example
```
import { Link } from 'expo-router';
import { View } from 'react-native';
export default function Route() {
 return (
 <View><Link replace href="/feed">Login</Link></View>
 );
}

```

### `withAnchor`
Android
iOS
tvOS
Web
Optional • Type: `boolean`
Replaces the initial screen with the current route.
#### Inherited Props
  * `Omit[](https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys)<'href'>`
  * `WebAnchorProps[](https://docs.expo.dev/versions/latest/sdk/router/#webanchorprops)`


### `Redirect`
Android
iOS
tvOS
Web
Type: `React.Element[](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<RedirectProps[](https://docs.expo.dev/versions/latest/sdk/router/#redirectprops)>`
Redirects to the `href` as soon as the component is mounted.
Example
```
import { View, Text } from 'react-native';
import { Redirect } from 'expo-router';
export default function Page() {
 const { user } = useAuth();
 if (!user) {
  return <Redirect href="/login" />;
 }
 return (
  <View><Text>Welcome Back!</Text></View>
 );
}

```

RedirectProps
### `href`
Android
iOS
tvOS
Web
Type: 
The path of the route to navigate to. It can either be:
  * string: A full path like `/profile/settings` or a relative path like `../settings`.
  * object: An object with a `pathname` and optional `params`. The `pathname` can be a full path like `/profile/settings` or a relative path like `../settings`. The params can be an object of key-value pairs.


Example
Dynamic
Copy
```
import { Redirect } from 'expo-router';
export default function RedirectToAbout() {
 return (
  <Redirect href="/about">About</Link>
 );
}

```

### `relativeToDirectory`
Android
iOS
tvOS
Web
Optional • Type: `boolean`
Relative URL references are either relative to the directory or the document. By default, relative paths are relative to the document.
> See: [Resolving relative references in Mozilla's documentation](https://developer.mozilla.org/en-US/docs/Web/API/URL_API/Resolving_relative_references).
### `withAnchor`
Android
iOS
tvOS
Web
Optional • Type: `boolean`
Replaces the initial screen with the current route.
### `Slot`
Android
iOS
tvOS
Web
Type: `React.Element[](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<Omit[](https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys)<NavigatorProps[](https://docs.expo.dev/versions/latest/sdk/router/#navigatorprops)<any>, 'children'>>`
Renders the currently selected content.
There are actually two different implementations of `<Slot/>`:
  * Used inside a `_layout` as the `Navigator`
  * Used inside a `Navigator` as the content


Since a custom `Navigator` will set the `NavigatorContext.contextKey` to the current `_layout`, you can use this to determine if you are inside a custom navigator or not.
## Hooks
### `useFocusEffect(effect, do_not_pass_a_second_prop)`
Android
iOS
tvOS
Web
Parameter| Type| Description  
---|---|---  
effect| `EffectCallback[](https://docs.expo.dev/versions/latest/sdk/router/#effectcallback)`| Memoized callback containing the effect, should optionally return a cleanup function.  
do_not_pass_a_second_prop(optional)| `undefined`  
Hook to run an effect whenever a route is focused. Similar to [`React.useEffect`](https://react.dev/reference/react/useEffect).
This can be used to perform side-effects such as fetching data or subscribing to events. The passed callback should be wrapped in [`React.useCallback`](https://react.dev/reference/react/useCallback) to avoid running the effect too often.
Returns:
`void`
Example
```
import { useFocusEffect } from 'expo-router';
import { useCallback } from 'react';
export default function Route() {
 useFocusEffect(
  // Callback should be wrapped in `React.useCallback` to avoid running the effect too often.
  useCallback(() => {
   // Invoked whenever the route is focused.
   console.log('Hello, I'm focused!');
   // Return function is invoked whenever the route gets out of focus.
   return () => {
    console.log('This route is now unfocused.');
   };
  }, []);
  );
 return </>;
}

Show More

```

### `useGlobalSearchParams()`
Android
iOS
tvOS
Web
Returns URL parameters for globally selected route, including dynamic path segments. This function updates even when the route is not focused. Useful for analytics or other background operations that don't draw to the screen.
Route URL example: `acme://profile/baconbrix?extra=info`.
When querying search params in a stack, opt-towards using [`useLocalSearchParams`](https://docs.expo.dev/versions/latest/sdk/router/#uselocalsearchparams) because it will only update when the route is focused.
> Note: For usage information, see [Local versus global search parameters](https://docs.expo.dev/router/reference/url-parameters#local-versus-global-url-parameters).
Returns:
`RouteParams<TRoute> & TParams`
Example
app/profile/[user].tsx
Copy
```
import { Text } from 'react-native';
import { useGlobalSearchParams } from 'expo-router';
export default function Route() {
 // user=baconbrix & extra=info
 const { user, extra } = useGlobalSearchParams();
 return <Text>User: {user}</Text>;
}

```

### `useLocalSearchParams()`
Android
iOS
tvOS
Web
Returns the URL parameters for the contextually focused route. Useful for stacks where you may push a new screen that changes the query parameters. For dynamic routes, both the route parameters and the search parameters are returned.
Route URL example: `acme://profile/baconbrix?extra=info`.
To observe updates even when the invoking route is not focused, use [`useGlobalSearchParams`](https://docs.expo.dev/versions/latest/sdk/router/#useglobalsearchparams).
> Note: For usage information, see [Local versus global search parameters](https://docs.expo.dev/router/reference/url-parameters#local-versus-global-url-parameters).
Returns:
`RouteParams<TRoute> & TParams`
Example
app/profile/[user].tsx
Copy
```
import { Text } from 'react-native';
import { useLocalSearchParams } from 'expo-router';
export default function Route() {
 // user=baconbrix & extra=info
 const { user, extra } = useLocalSearchParams();
 return <Text>User: {user}</Text>;
}

```

### `useNavigation(parent)`
Android
iOS
tvOS
Web
Parameter| Type| Description  
---|---|---  
parent(optional)| `string | `| Provide an absolute path such as `/(root)` to the parent route or a relative path like `../../` to the parent route.  
Returns the underlying React Navigation [`navigation` object](https://reactnavigation.org/docs/navigation-object) to imperatively access layout-specific functionality like `navigation.openDrawer()` in a [Drawer](https://docs.expo.dev/router/advanced/drawer) layout.
Returns:
`T`
The navigation object for the current route.
> See: React Navigation documentation on [navigation dependent functions](https://reactnavigation.org/docs/navigation-object/#navigator-dependent-functions) for more information.
Example
app/index.tsx
Copy
```
import { useNavigation } from 'expo-router';
export default function Route() {
 // Access the current navigation object for the current route.
 const navigation = useNavigation();
 return (
  <View><Text onPress={() => {
    // Open the drawer view.
    navigation.openDrawer();
   }}>
    Open Drawer
   </Text></View>
 );
}

```

When using nested layouts, you can access higher-order layouts by passing a secondary argument denoting the layout route. For example, `/menu/_layout.tsx` is nested inside `/app/orders/`, you can use `useNavigation('/orders/menu/')`.
Example
app/orders/menu/index.tsx
Copy
```
import { useNavigation } from 'expo-router';
export default function MenuRoute() {
 const rootLayout = useNavigation('/');
 const ordersLayout = useNavigation('/orders');
 // Same as the default results of `useNavigation()` when invoked in this route.
 const parentLayout = useNavigation('/orders/menu');
}

```

If you attempt to access a layout that doesn't exist, an error such as `Could not find parent navigation with route "/non-existent"` is thrown.
### `useNavigationContainerRef()`
Android
iOS
tvOS
Web
Returns:
`NavigationContainerRefWithCurrent<>`
The root `<NavigationContainer />` ref for the app. The `ref.current` may be `null` if the `<NavigationContainer />` hasn't mounted yet.
### `usePathname()`
Android
iOS
tvOS
Web
Returns the currently selected route location without search parameters. For example, `/acme?foo=bar` returns `/acme`. Segments will be normalized. For example, `/[id]?id=normal` becomes `/normal`.
Returns:
`string`
Example
app/profile/[user].tsx
Copy
```
import { Text } from 'react-native';
import { usePathname } from 'expo-router';
export default function Route() {
 // pathname = "/profile/baconbrix"
 const pathname = usePathname();
 return <Text>User: {user}</Text>;
}

```

> Deprecated Use [`useNavigationContainerRef`](https://docs.expo.dev/versions/latest/sdk/router/#usenavigationcontainerref) instead, which returns a React `ref`.
### `useRootNavigation()`
Android
iOS
tvOS
Web
Returns:
`null | NavigationContainerRef[](https://reactnavigation.org/docs/navigating-without-navigation-prop)<>`
### `useRootNavigationState()`
Android
iOS
tvOS
Web
Returns the [navigation state](https://reactnavigation.org/docs/navigation-state/) of the navigator which contains the current screen.
Returns:
`any`
Example
```
import { useRootNavigationState } from 'expo-router';
export default function Route() {
 const { routes } = useRootNavigationState();
 return <Text>{routes[0].name}</Text>;
}

```

### `useRouter()`
Android
iOS
tvOS
Web
Returns the [Router](https://docs.expo.dev/versions/latest/sdk/router/#router) object for imperative navigation.
Returns:
Example
```
import { useRouter } from 'expo-router';
import { Text } from 'react-native';
export default function Route() {
 const router = useRouter();
 return (
 <Text onPress={() => router.push('/home')}>Go Home</Text>
 );
}

```

### `useSegments()`
Android
iOS
tvOS
Web
Returns a list of selected file segments for the currently selected route. Segments are not normalized, so they will be the same as the file path. For example, `/[id]?id=normal` becomes `["[id]"]`.
Returns:
`RouteSegments<TSegments>`
Example
app/profile/[user].tsx
Copy
```
import { Text } from 'react-native';
import { useSegments } from 'expo-router';
export default function Route() {
 // segments = ["profile", "[user]"]
 const segments = useSegments();
 return <Text>Hello</Text>;
}

```

`useSegments` can be typed using an abstract. Consider the following file structure:
```
- app
 - [user]
  - index.tsx
  - followers.tsx
 - settings.tsx

```

This can be strictly typed using the following abstract with `useSegments` hook:
```
const [first, second] = useSegments<['settings'] | ['[user]'] | ['[user]', 'followers']>()

```

## Methods
### `withLayoutContext(Nav, processor)`
Android
iOS
tvOS
Web
Parameter| Type  
---|---  
Nav  
processor(optional)| `(options: ScreenProps[][](https://docs.expo.dev/versions/latest/sdk/router/#screenprops)) => ScreenProps[][](https://docs.expo.dev/versions/latest/sdk/router/#screenprops)`  
Returns a navigator that automatically injects matched routes and renders nothing when there are no children. Return type with `children` prop optional.
Returns:
`Component[](https://react.dev/reference/react/Component)<PropsWithoutRef<PickPartial[](https://docs.expo.dev/versions/latest/sdk/router/#pickpartial)<ComponentProps<T>, 'children'>>> & {  Screen: (props: ScreenProps[](https://docs.expo.dev/versions/latest/sdk/router/#screenprops)<TOptions, TState, TEventMap>) => null }`
## Types
### `EffectCallback()`
Android
iOS
tvOS
Web
Memoized callback containing the effect, should optionally return a cleanup function.
Returns:
`undefined | void | () => void`
### `ExternalPathString`
Android
iOS
tvOS
Web
Literal Type: `union`
Acceptable values are: `{string}:{string}` | `//{string}`
### `Href<T>`
Android
iOS
tvOS
Web
The main routing type for Expo Router. It includes all available routes with strongly typed parameters. It can either be:
  * string: A full path like `/profile/settings` or a relative path like `../settings`.
  * object: An object with a `pathname` and optional `params`. The `pathname` can be a full path like `/profile/settings` or a relative path like `../settings`. The params can be an object of key-value pairs.


An Href can either be a string or an object.
Generic: `T`
Type: `T ? T[href] : string | `
### `HrefObject`
Android
iOS
tvOS
Web
Property| Type| Description  
---|---|---  
params(optional)| `UnknownInputParams`| Optional parameters for the route.  
pathname| `string`| The path of the route.  
### `NativeIntent`
Android
iOS
tvOS
Web
Created by using a special file called `+native-intent.tsx` at the top-level of your project's app directory. It exports `redirectSystemPath` or `legacy_subscribe` functions, both methods designed to handle URL/path processing.
Useful for re-writing URLs to correctly target a route when unique/referred URLs are incoming from third-party providers or stale URLs from previous versions.
> See: For more information on how to use `NativeIntent`, see [Customizing links](https://docs.expo.dev/router/advanced/native-intent).
Property| Type| Description  
---|---|---  
legacy_subscribe(optional)| `(listener: (url: string) => void) => undefined | void | () => void`| 
> Experimentally available in SDK 52.
Useful as an alternative API when a third-party provider doesn't support Expo Router but has support for React Navigation via `Linking.subscribe()` for existing projects. Using this API is not recommended for newer projects or integrations since it is incompatible with Server Side Routing and [Static Rendering](https://docs.expo.dev/router/reference/static-rendering), and can become challenging to manage while offline or in a low network environment.  
redirectSystemPath(optional)| `(event: {  initial: boolean,   path: string }) => Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<string> | string`| A special method used to process URLs in native apps. When invoked, it receives an `options` object with the following properties:
  * path: represents the URL or path undergoing processing.
  * initial: a boolean indicating whether the path is the app's initial URL.

It's return value should either be a `string` or a `Promise<string>`. Note that throwing errors within this method may result in app crashes. It's recommended to wrap your code inside a `try/catch` block and utilize `.catch()` when appropriate.
> See: For usage information, see [Redirecting system paths](https://docs.expo.dev/router/advanced/native-intent#redirectsystempath).  
### `PickPartial`
Android
iOS
tvOS
Web
Literal Type: `union`
The list of input keys will become optional, everything else will remain the same.
Acceptable values are: `Omit[](https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys)<T, K>` | `Partial[](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)<Pick[](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)<T, K>>`
### `RelativePathString`
Android
iOS
tvOS
Web
Literal Type: `union`
Acceptable values are: `./{string}` | `../{string}` | `'..'`
### `ResultState`
Android
iOS
tvOS
Web
Type: `PartialState<>` extended by:
Property| Type| Description  
---|---|---  
state(optional)|   
### `Route`
Android
iOS
tvOS
Web
Type: `Exclude[](https://www.typescriptlang.org/docs/handbook/utility-types.html#excludeuniontype-excludedmembers)<Extract[pathname], RelativePathString[](https://docs.expo.dev/versions/latest/sdk/router/#relativepathstring) | ExternalPathString[](https://docs.expo.dev/versions/latest/sdk/router/#externalpathstring)>`
### `Router`
Android
iOS
tvOS
Web
Returns `router` object for imperative navigation API.
Example
```
import { router } from 'expo-router';
import { Text } from 'react-native';
export default function Route() {
 return (
 <Text onPress={() => router.push('/home')}>Go Home</Text>
 );
}

```

Property| Type| Description  
---|---|---  
back| `() => void`| Goes back in the navigation history.  
canDismiss| `() => boolean`| Checks if it is possible to dismiss the current screen. Returns `true` if the router is within the stack with more than one screen in stack's history.  
canGoBack| `() => boolean`| Navigates to a route in the navigator's history if it supports invoking the `back` function.  
dismiss| `(count: number) => void`| Navigates to the a stack lower than the current screen using the provided count if possible, otherwise 1. If the current screen is the only route, it will dismiss the entire stack.  
dismissAll| `() => void`| Returns to the first screen in the closest stack. This is similar to [`popToTop`](https://reactnavigation.org/docs/stack-actions/#poptotop) stack action.  
dismissTo| `(href: Href[](https://docs.expo.dev/versions/latest/sdk/router/#href), options: NavigationOptions[](https://reactnavigation.org/docs/screen-options/)) => void`| Dismisses screens until the provided href is reached. If the href is not found, it will instead replace the current screen with the provided `href`.  
navigate| `(href: Href[](https://docs.expo.dev/versions/latest/sdk/router/#href), options: NavigationOptions[](https://reactnavigation.org/docs/screen-options/)) => void`| Navigates to the provided [`href`](https://docs.expo.dev/versions/latest/sdk/router/#href).  
push| `(href: Href[](https://docs.expo.dev/versions/latest/sdk/router/#href), options: NavigationOptions[](https://reactnavigation.org/docs/screen-options/)) => void`| Navigates to the provided [`href`](https://docs.expo.dev/versions/latest/sdk/router/#href) using a push operation if possible.  
replace| `(href: Href[](https://docs.expo.dev/versions/latest/sdk/router/#href), options: NavigationOptions[](https://reactnavigation.org/docs/screen-options/)) => void`| Navigates to route without appending to the history. Can be used with [`useFocusEffect`](https://docs.expo.dev/versions/latest/sdk/router/#usefocuseffecteffect-do_not_pass_a_second_prop) to redirect imperatively to a new screen.
> See: [Using `useRouter()` hook](https://docs.expo.dev/router/reference/redirects) to redirect.  
setParams| `(params: Partial[](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)<RouteInputParams<T>>) => void`| Updates the current route's query params.  
### `ScreenProps`
Android
iOS
tvOS
Web
Property| Type| Description  
---|---|---  
getId(optional)| `({ params }: {  params: Record<string, any> }) => string | undefined`  
initialParams(optional)| `Record<string, any>`  
listeners(optional)| `ScreenListeners<TState, TEventMap> | (prop: {  navigation: any,   route: RouteProp[](https://reactnavigation.org/docs/glossary-of-terms/#route-object)<ParamListBase, string> }) => ScreenListeners<TState, TEventMap>`  
name(optional)| `string`| Name is required when used inside a Layout component.  
options(optional)| `TOptions | (prop: {  navigation: any,   route: RouteProp[](https://reactnavigation.org/docs/glossary-of-terms/#route-object)<ParamListBase, string> }) => TOptions`  
redirect(optional)| `boolean`| Redirect to the nearest sibling route. If all children are `redirect={true}`, the layout will render `null` as there are no children to render.  
### `SearchOrHash`
Android
iOS
tvOS
Web
Literal Type: `union`
Acceptable values are: `?{string}` | `#{string}`
### `WebAnchorProps`
Web
Property| Type| Description  
---|---|---  
download(optional)| `string`| Specifies that the [`href`](https://docs.expo.dev/versions/latest/sdk/router/#href) should be downloaded when the user clicks on the link, instead of navigating to it. It is typically used for links that point to files that the user should download, such as PDFs, images, documents, and more. The value of the `download` property, which represents the filename for the downloaded file. This property is passed to the underlying anchor (`<a>`) tag.Example```
<Link href="/image.jpg" download="my-image.jpg">Download image</Link>

```
  
rel(optional)| `string`| Specifies the relationship between the [`href`](https://docs.expo.dev/versions/latest/sdk/router/#href) and the current route. Common values:
  * nofollow: Indicates to search engines that they should not follow the `href`. This is often used for user-generated content or links that should not influence search engine rankings.
  * noopener: Suggests that the `href` should not have access to the opening window's `window.opener` object, which is a security measure to prevent potentially harmful behavior in cases of links that open new tabs or windows.
  * noreferrer: Requests that the browser does not send the `Referer` HTTP header when navigating to the `href`. This can enhance user privacy.

The `rel` property is primarily used for informational and instructive purposes, helping browsers and web crawlers make better decisions about how to handle and interpret the links on a web page. It is important to use appropriate `rel` values to ensure that links behave as intended and adhere to best practices for web development and SEO (Search Engine Optimization). This property is passed to the underlying anchor (`<a>`) tag.Example```
<Link href="https://expo.dev" rel="nofollow">Go to Expo</Link>

```
  
target(optional)| `'_self' | '_blank' | '_parent' | '_top' | string & object`| Specifies where to open the [`href`](https://docs.expo.dev/versions/latest/sdk/router/#href).
  * _self: the current tab.
  * _blank: opens in a new tab or window.
  * _parent: opens in the parent browsing context. If no parent, defaults to _self.
  * _top: opens in the highest browsing context ancestor. If no ancestors, defaults to _self.

This property is passed to the underlying anchor (`<a>`) tag.Default:`'_self'`Example```
<Link href="https://expo.dev" target="_blank">Go to Expo in new tab</Link>

```


