---
url: https://expo.dev/changelog/2024-01-23-router-3
title: https://expo.dev/changelog/2024-01-23-router-3
date: 2025-04-30T17:19:00.792955
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [Expo Router v3: API Routes, bundle splitting, speed improvements, and more](https://expo.dev/changelog/2024-01-23-router-3)
Jan 23, 2024 by
Evan Bacon
Welcome to Expo Router v3, our most powerful release yet! Today we're introducing beta support for the newest Expo platform: Servers. With this, Expo Router is now the first **universal, full-stack React framework**!
  * [**API Routes (beta)**](https://expo.dev/changelog/2024/01-23-router-3#introducing-api-routes): Build universal server endpoints for your app and website.
  * [**Bundle splitting (web)**](https://expo.dev/changelog/2024/01-23-router-3#route-based-bundle-splitting): Route-based bundle splitting on web for faster page loads.
  * [**Speed improvements**](https://expo.dev/changelog/2024/01-23-router-3#faster-builds-and-smaller-bundles): 2x faster static web builds, 30% smaller base JS bundle, added `.mjs` support.
  * [**Testing library**](https://expo.dev/changelog/2024/01-23-router-3#expo-router-testing-library): You can now test and reproduce complex navigation flows with Jest.
  * [**Web**](https://expo.dev/changelog/2024/01-23-router-3#new-link-props) [**`<Link />`**](https://expo.dev/changelog/2024/01-23-router-3#new-link-props)[**props**](https://expo.dev/changelog/2024/01-23-router-3#new-link-props): Configure and style `<Link />` components with the new `target`, `push`, and `className` props.


Get started with Expo Router v3 today in one line:
Terminal
Copy
`npx create-expo-app@latest -t tabs@50`
If you're new here, Expo Router uses a file-based approach to app development which enables you to build more powerful apps than ever before, with less boilerplate code. The key features so far have been [autocomplete and type safety](https://docs.expo.dev/router/reference/typed-routes/) for navigation, [SEO and accessibility for web](https://docs.expo.dev/router/reference/static-rendering/), automatic [universal linking](https://docs.expo.dev/guides/deep-linking/), [lazy bundling](https://docs.expo.dev/router/reference/async-routes/), and more!
## [Introducing API routes ](https://expo.dev/changelog/2024-01-23-router-3#introducing-api-routes)
**Note: API Routes are still in beta during SDK 50.**
Based on our [API Routes RFC](https://blog.expo.dev/rfc-api-routes-cce5a3b9f25d) — API Routes are a zero-config system for creating server endpoints with a unified build process. This is the first step toward making Expo Router a full-stack React framework.
Adding a `+api.js` extension to a route will ensure it's only rendered on the server. API routes are hosted from the same dev server as the website and app in development and must be deployed to a dynamic hosting service in production.
Code
Copy
```

import{ExpoRequest,ExpoResponse}from'expo-router/server';
exportfunctionGET(){
returnExpoResponse.json({ hello:'world'});
exportfunctionPOST(request:ExpoRequest){
const{ prompt }=await request.json();
// Do something with the prompt
returnExpoResponse.json({
/* ... */
});

```

You can export any of the following functions `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, and `OPTIONS` from an API route. The function executes when the corresponding HTTP method is matched. Unsupported methods will automatically return `405: Method not allowed`.
Learn more and get started today in [API Routes](https://docs.expo.dev/router/reference/api-routes/). Additionally, you can download an [example app](https://github.com/expo/examples/tree/master/with-openai) that uses OpenAI to generate text from a GPT-3 model with:
Terminal
Copy
`npx create-expo-app@latest -e with-openai`
The new server architecture will be used to render universal **React Server Components** in an upcoming release.
### [Relative Fetch requests ](https://expo.dev/changelog/2024-01-23-router-3#relative-fetch-requests)
To better support API Routes, we've added the ability to perform relative fetch requests on native by setting the production server URL in the **app.json** :
Code
Copy
```

"plugins":[
"expo-router",
"origin":"https://my-app.dev/"

```

This will enable making relative requests with the `fetch` API, in both development and production environments:
Code
Copy
```

asyncfunctionfetchHello(){
// Requests from `http://localhost:8081/hello` in development and `https://my-app.dev/hello` in production.
const response =awaitfetch('/hello');
const data =await response.json();
// Alerts "Hello world"
alert('Hello '+ data.hello);

```

In order to use this in production, the server must be hosted publicly. [Learn more about hosting production servers](https://docs.expo.dev/router/reference/api-routes/#deployment).
### [Supporting 404s with +not-found ](https://expo.dev/changelog/2024-01-23-router-3#supporting-404s-with-not-found)
API Routes are a special type of route that is only matched after standard routes have been matched. If you were previously using a top-level catch-all like `app/[...missing].js` to handle 404s and missing routes, then no API Route would ever be matched.
To account for API Routes, we've added an official convention to match all 404 / Not Found routes. By creating a `+not-found.js` route you can match all remaining requests _after_ API routes have been processed. This is supported on all native platforms, and web in `server`-mode. When this route is matched, a 404 status code will also be returned on web. [Learn more about](https://docs.expo.dev/router/reference/not-found/) [`+not-found`](https://docs.expo.dev/router/reference/not-found/) [routes](https://docs.expo.dev/router/reference/not-found/).
## [Route-based bundle splitting ](https://expo.dev/changelog/2024-01-23-router-3#route-based-bundle-splitting)
Expo CLI now supports bundle splitting on async imports (e.g. `await import("./route")`) when bundling for the web platform. We've extended this behavior with Expo Router to automatically split on routes in the app directory.
Expo Router also eagerly loads chunks to prevent network waterfalls on initial requests. [Learn more in "Async Routes"](https://docs.expo.dev/router/reference/async-routes).
We built this entire feature to be completely universal, but due to the complex nature of native caching we've opted for web-only support in Expo Router v3. Support for splitting bundles on native platforms will be included with **React Server Component** support in the future.
## [Configurable app directory ](https://expo.dev/changelog/2024-01-23-router-3#configurable-app-directory)
You can now change the `/app` directory to be any directory in your project. This is useful for testing and white-labeling projects with multiple sub-apps. [Learn more about the root directory](https://docs.expo.dev/router/reference/src-directory/#custom-directory).
Code
Copy
```

"plugins":[["expo-router",{"root":"./routes"}]]

```

Avoid changing the root directory as this complicates the build process and may cause unexpected development issues. Opt to use the `app` and `src/app` directories instead for a consistent and tested experience. [Learn more about the](https://docs.expo.dev/router/reference/src-directory/) [`src/app`](https://docs.expo.dev/router/reference/src-directory/) [directory](https://docs.expo.dev/router/reference/src-directory/).
## [Static font optimization ](https://expo.dev/changelog/2024-01-23-router-3#static-font-optimization)
Fonts loaded with `expo-font` are now automatically extracted and preloaded on web when using `static` or `server` output. This enables fonts to start loading before the JavaScript has finished, leading to better initial styles. This system also enables you to statically render your app even if there's a top-level render guard. [Learn more](https://docs.expo.dev/router/appearance/#fonts).
Code
Copy
```

import{ useFonts }from'expo-font';
exportdefaultfunctionRootLayout(){
// `loaded` will be `true` in static websites as the font was eagerly loaded with the HTML before this JS was executed.
const[loaded]=useFonts({
  inter:require('@/fonts/inter.ttf'),
});
if(!loaded){
// This will no longer be called on static web, meaning the entire boundary will be statically rendered to searchable HTML.
returnnull;
return<Stack/>;

```

## [New push and navigate behaviors ](https://expo.dev/changelog/2024-01-23-router-3#new-push-and-navigate-behaviors)
To fix issues with pushing screens in complex routing scenarios, we've changed the `router.push()` API to always push new routes, whereas the previous version would pop occasionally. You can use the new `router.navigate()` API to obtain this previous behavior. [Learn more about the imperative routing API](https://docs.expo.dev/router/navigating-pages/#imperative-navigation).
## [Expo Router testing library ](https://expo.dev/changelog/2024-01-23-router-3#expo-router-testing-library)
To provide robust test coverage for Expo Router, we created a set of [Jest utilities](https://jestjs.io/) that could quickly emulate entire navigation structures. This testing library is now available for public consumption. [Learn more in "Testing Expo Router"](https://docs.expo.dev/router/reference/testing/).
Code
Copy
```

import{ renderRouter, screen }from'expo-router/testing-library';
it('my-test',async()=>{
constMockComponent= jest.fn(()=><View/>);
renderRouter(
   index:MockComponent,
'folder/a':MockComponent,
'(group)/b':MockComponent,
},
   initialUrl:'/folder/a',
);
expect(screen).toHavePathname('/folder/a');
});

```

We use this internally to prevent regressions against the majority of reported issues. We recommend using this system to create minimal reproducible test cases before reporting issues with Expo Router.
## [New Link props ](https://expo.dev/changelog/2024-01-23-router-3#new-link-props)
The `Link` component now supports `target`, `rel`, and `download` props on web. `Link` also now has `className` support which works as-is on web and can be used with tools like [Nativewind](https://www.nativewind.dev/) to add [Tailwind](https://tailwindcss.com/) support on all platforms.
Code
Copy
```

<Link target="_blank" className="text-blue-300" href="/home"/>

```

`Link` components currently navigate to the nearest route matching the `href` prop, you can now force them to always push a new route by passing the new `push` prop.
Code
Copy
```

// Navigate to the closest route
<Link href="/"/>
// Push "/" as a new route
<Link push href="/"/>

```

## [Faster builds and smaller bundles ](https://expo.dev/changelog/2024-01-23-router-3#faster-builds-and-smaller-bundles)
`npx expo export -p web` is over 2x faster for static websites. An average v2 project exported in ~23s, v3 exports in ~11s. These savings scale proportional to the project size.
The base JS bundle size for production websites is now **30% smaller** (from 1.48mb to 1.05mb). The initial bundle size is further decreased by enabling the new [bundle splitting functionality](https://expo.dev/changelog/2024/01-23-router-3#route-based-bundle-splitting) on web.
**The** `URL` **and** `URLSearchParams` **standards are built-in**. It was previously necessary to polyfill the web standard `URL` API in order to use many cross-platform libraries available on npm, where developers tend to assume that the `URL` API is available. We believe that `URL` is an important enough primitive that it deserves to be built in to the Expo core runtime, and so we now ship our own implementation in the `expo` package. By doing this, we were able to remove all the various duplicate helper libraries that were used to parse URLs, this further reduced the base bundle size. [Learn more about the URL API](https://docs.expo.dev/versions/latest/sdk/url/).
We'll continue to reduce the bundle size by reworking parts of React Navigation and improving tree shaking in Expo CLI.
## [Stability and support ](https://expo.dev/changelog/2024-01-23-router-3#stability-and-support)
In Expo Router v3, we've moved the source code and issue tracking to the [**expo/expo**](https://github.com/expo/expo) monorepo. During the migration, we fixed and addressed the majority of issues and bugs regarding Expo Router and added lots more documentation and tests.
Configuration requirements like the Babel plugin have been folded into `babel-preset-expo` and Expo CLI, this also enables many Metro web features like `expo-constants` features for non-router users. Additional Expo Router functionality has been integrated across the SDK with packages like Splash Screen, Linking, and Font. We've also removed the need for any custom Yarn resolutions and upstreamed a number of bug fixes to Metro and React Native.
Overall, **Expo Router is now more powerful, reliable, and seamless than ever before**.
## [Other Highlights ](https://expo.dev/changelog/2024-01-23-router-3#other-highlights)
  * **Server-hosted dynamic routes on web.** The new `server` output mode supports server navigation to dynamic routes on web. Previously, you could only perform client-side navigation to routes like `app/[id].tsx` but the server API is capable of redirecting requests to any route in your project automatically. This is not supported with standard `static` output.
  * **Universal Fast Refresh.** We've fixed universal Fast Refresh upstream so you no longer need resolutions on `react-refresh` (be sure to remove them if you have any). The same Fast Refresh implementation now works across all platforms universally and is far more reliable!
  * **Experimental base URL support.** Expo Router now supports deploying to subdomains with `experiments.baseUrl`——this applies to all platforms so you may want to configure it with an environment variable in `app.config.js`. With the addition of this feature, you can now deploy static Expo Router websites to [GitHub Pages](https://docs.expo.dev/distribution/publishing-websites/#github-pages). We plan to stabilize this API in SDK 51.
  * **Improved Tailwind/PostCSS on web.** PostCSS with Expo's Metro web will no longer be blocked on caching. This means you can use full [Tailwind](https://tailwindcss.com/) + PostCSS on web and integrate with fantastic UI packages like [Shadcn UI](https://ui.shadcn.com/) (web-only). Metro CSS is now enabled by default! Here's an example of using [Expo Router with Nativewind v4](https://github.com/expo/examples/tree/master/with-router-tailwind).
  * **Support for system links.** You can now link to popular external URLs like `mailto:` and `sms:` which don't follow the standard `://` convention of other URLs.
  * **Added mjs and cjs support.** All modules are converted to commonjs in the bundler because ESM is not supported on native, but you can now import `.mjs` modules as expected without modifying the `metro.config.js`.
  * **Custom Metro resolvers and transforms.** Users can now extend the Metro resolver and modify the transformer using the Babel caller, enabling better control over the bundling process. [Learn more in the new Expo Metro docs](https://docs.expo.dev/versions/v50.0.0/config/metro/#extending-the-babel-transformer).
  * **Improved Typed Routes.** Typed routes ensure better stability over time by automatically generating TypeScript types for your project. You can now generate types in CI with `npx expo customize tsconfig.json`. Learn more about [Typed Routes in Expo Router](https://docs.expo.dev/router/reference/typed-routes/).
  * **Improved monorepo support.** Projects no longer need `expo-yarn-workspaces` to enable monorepo support in their app. The majority of standard monorepo functionality is built-in to Expo CLI and Expo Metro Config.
  * **Better source maps.** Source map exports in production web are now supported, we've renamed the `npx expo export` flag `--dump-sourcemap` to `--source-maps`——Hermes source maps now work more reliably.
  * **Improved error messages and code removal.** Expo CLI now provides full stack traces for component-based errors, tree shakes all unused platform-specific code, and transforms faster when bundling for Hermes.
  * `@expo/webpack-config` **is deprecated in favor of Expo CLI's Metro web.** This means that Webpack support will continue to work in SDK 50, but it will not be actively developed, and it will be removed in a future release. Read the ["Webpack support in Expo CLI is now deprecated" blog](https://blog.expo.dev/webpack-support-in-expo-cli-is-now-deprecated-e9831d7eb631) for the full story, and [learn about migrating away from Webpack to Metro](https://docs.expo.dev/router/migrate/from-expo-webpack/).
  * **CSS is enabled by default with Metro web**. CSS is not supported on Android and iOS, but on web you can use all CSS features by importing CSS files. [Learn more](https://docs.expo.dev/versions/latest/config/metro/#css).
  * `tsconfigPaths` **is now enabled in** `@expo/metro-config` **by default:** this means that all you need to do to add path aliases is configure the `paths` property in your **tsconfig.json**. For example, `"@/*": ["src/*"]` will allow you to write code like `import Button from '@/components/Button';` anywhere in your codebase and have it resolve to the correct location within `src`. They're also now supported in `jest-expo`. [Learn more](https://docs.expo.dev/guides/typescript/#path-aliases).

## [Notable breaking changes ](https://expo.dev/changelog/2024-01-23-router-3#notable-breaking-changes)
  * **`expo-router/babel`****has been removed.** Delete this plugin from your `babel.config.js` file, and be sure to **clear the Metro cache before restarting your dev server** ——this means running `npx expo start --clear`.
  * **`router.push`****default behavior changed.** `router.push` is now `router.navigate` and the new `router.push` will always push routes. This is technically a bug fix, but it may cause unexpected changes in complex navigation behavior.
  * **`react-native-gesture-handler`****is no longer added automatically.** You can now choose to optionally add gesture handler if you wish to use the `<Drawer />` navigator. We recommend avoiding this dependency on web platforms as it will increase bundle size substantially and mostly be unused on web. [Learn more about the Drawer navigator](https://docs.expo.dev/router/advanced/drawer/).
  * **`src`****directory changed to** **`build`.** We now ship transpiled JavaScript to production in the `expo-router/build/*` directory. This is a breaking change if you were imported internals from Expo Router in your project.

## [Known issues ](https://expo.dev/changelog/2024-01-23-router-3#known-issues)
  * API Routes will remain in beta throughout v3. See the list of [known limitations](https://docs.expo.dev/router/reference/api-routes/#known-limitations) for more info.
  * [Snack](https://snack.expo.dev/) does not support Expo Router or API routes.
  * Found an issue? [Report a regression](https://github.com/expo/expo/issues/new?assignees=&amp;labels=needs+review&amp;template=bug_report.yml).

## [➡️ Upgrading your app ](https://expo.dev/changelog/2024-01-23-router-3#️-upgrading-your-app)
Here's how to upgrade your app to Expo Router v3 from v2:
  * **Upgrade your app to SDK 50** : [follow the instructions in the SDK 50 release notes](https://expo.dev/changelog/2024/01-18-sdk-50#%E2%9E%A1%EF%B8%8F-upgrading-your-app).
  * **Update the** **`babel.config.js`**:
    * Remove the `expo-router/babel` plugin in favor of `babel-preset-expo` preset.


Code
Copy
```

module.exports = function (api) {
 api.cache(true);
 return {
  presets: ['babel-preset-expo'],
-  plugins: ['expo-router/babel']
 };
};

```

  * Be sure to **clear the Metro cache before restarting your dev server** :


Terminal
Copy
`npx expo start --clear`
  * Possibly the largest behavior change in any version of Expo Router——`router.push` is now `router.navigate` and the new `router.push` will always push routes. This is technically a bug fix, but it may cause unexpected changes in complex navigation behavior.
  * `react-native-gesture-handler` is no longer added automatically and must be injected if you wish to use the `<Drawer />` navigator. We recommend avoiding this dependency on web platforms as it will increase bundle size substantially and mostly be unused on web. Learn more about the [Drawer navigator](https://docs.expo.dev/router/advanced/drawer/).
  * Enable [Async Routes](https://docs.expo.dev/router/reference/async-routes/) to use the new **bundle splitting** functionality on web. Async Routes may have issues on Android with Reanimated, you can disable the feature per-platform if needed.
  * If you have a top-level catch-all route like `[...missing].js`, ensure you rename this to `+not-found.js` if you plan to use API Routes. Otherwise, you'll only see the "not found" route when you ping an API endpoint.
  * If you have custom splash screen handling, change the import of `SplashScreen` in `expo-router` to `expo-splash-screen`.
  * If you were using the `hrefAttrs` prop on the `Link` component for adding additional web props, migrate to top-level props by the same name, e.g. `hrefAttrs={{ target: '_blank' }}` should now be `target="_blank"`——this applies to `target`, `rel`, `download`——all of which are web-only and automatically shimmed on native.
  * If you're using the `react-native-web` style escape hatch (`style={{ $$css: true, _: "myclass" }}`) to set `className` on `Link` components for web, migrate to the top-level `className` prop, e.g. `<Link className="myclass" />`
  * **Questions?** We'll be hosting an SDK 50 launch live-stream on January 31st, [join us on YouTube](https://www.youtube.com/watch?v=cKFSVUo3AnI).

## [Compatibility ](https://expo.dev/changelog/2024-01-23-router-3#compatibility)
Ensure you use libraries that are versioned to work with Expo SDK 50:
  * `expo@^50.0.0`
  * `expo-router@^3.0.0`
  * `react@18.2.0`
  * `react-native@~0.73.2`
  * `react-native-web@~0.19.6`
  * `@react-navigation/native@^6.0.2`


You can validate versions automatically with Expo CLI:
Terminal
Copy
`npx expo install --check`
## [Thanks to everyone who contributed to the release! ](https://expo.dev/changelog/2024-01-23-router-3#thanks-to-everyone-who-contributed-to-the-release)
Along with everyone who's adopted this exciting new technology, we'd like to thank the following people for their contributions to Expo Router v3: [@sync](https://github.com/sync) [@kudo](https://github.com/kudo) [@muneebahmedayub](https://github.com/muneebahmedayub) [@gabrieldonadel](https://github.com/gabrieldonadel) [@tsapeta](https://github.com/tsapeta) [@quinlanj](https://github.com/quinlanj) [@douglowder](https://github.com/douglowder) [@marklawlor](https://github.com/marklawlor) [@kitten](https://github.com/kitten) [@byCedric](https://github.com/byCedric) [@EvanBacon](https://github.com/EvanBacon)

