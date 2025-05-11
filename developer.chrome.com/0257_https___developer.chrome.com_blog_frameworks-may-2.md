---
url: https://developer.chrome.com/blog/frameworks-may-2024
title: https://developer.chrome.com/blog/frameworks-may-2024
date: 2025-05-11T16:56:14.412211
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/frameworks-may-2024#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/frameworks-may-2024?hl=es-419)




  * On this page
  * [Framework Trends and Convergence](https://developer.chrome.com/blog/frameworks-may-2024#framework_trends_and_convergence)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  What's new in JavaScript Frameworks (May 2024) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Framework Trends and Convergence](https://developer.chrome.com/blog/frameworks-may-2024#framework_trends_and_convergence)


Katie Hempenius 
Addy Osmani 
[ GitHub ](https://github.com/addyosmani) [ Bluesky ](https://bsky.app/profile/addyosmani.bsky.social)
It can be difficult to keep up with everything that is going with JavaScript frameworks. This document provides brief highlights of recent happenings in the JavaScript frameworks ecosystem over the past year or so. For a longer discussion of some of these topics, check out the corresponding [Navigating the JavaScript Frameworks Ecosystem](https://youtu.be/) talk from this year's Google I/O event.
## Framework Trends and Convergence
As shown in the chart, JavaScript frameworks are converging on a number similar features and architectures. These include component-based architecture, file-based routing, and modern SSR support. This convergence demonstrates the maturity and evolution of the ecosystem as frameworks learn from each other and adopt best practices.
At the same time, a number of recent trends (such as server components and different approaches to fine-grained reactivity) continue to set individual frameworks apart. To help understand these trends better, we dive into them one framework at a time.
### Angular
Angular's recent releases have contained a variety of significant changes including signals, deferrable views, NgOptimziedImage, non-destructive hydration, and partial hydration. Some highlights include:
  * [Signals](https://angular.io/guide/signals): Signals are an approach used by multiple frameworks (including now Angular) for tracking state in an application. Angular Signals can improve runtime performance—including [Interaction to Next Paint (INP)](https://web.dev/articles/inp)—by reducing the number of computations that must occur during change detection.
  * [Deferrable views](https://angular.io/guide/defer): Deferrable views make it possible to defer the loading of specific components, directives, and pipes. For example, you can defer loading a dependency until the content enters the viewport or until the main thread is idle.
  * [NgOptimizedImage](https://angular.io/guide/image-directive): NgOptimizedImage is an image component for Angular that automates the adoption of image loading best practices.
  * [Non-destructive hydration](https://blog.angular.io/whats-next-for-server-side-rendering-in-angular-2a6f27662b67#:%7E:text=Full%20Application%20Hydration%20Support): Non-destructive hydration fixes the [flicker](https://github.com/angular/angular/issues/23427) that would occur when the DOM of server-side rendered Angular apps was rebuilt client-side.
  * Partial hydration: The Angular team will soon be releasing the developer preview of partial hydration. With partial hydration, by default, the browser doesn't load any of the page's JavaScript when the page is rendered. Instead, specific parts of the page are hydrated as the user interacts with the page.


### Astro
Astro, a modern static site builder, has been making waves with its innovative approach to web development. With a focus on performance and developer experience, Astro has [released](https://astro.build/blog/) several exciting features and updates:
  * [Astro Islands](https://docs.astro.build/en/concepts/islands/): Astro Islands allow developers to build interactive UI components that are isolated from the rest of the page. This enables efficient updates and optimal performance.
  * [Hybrid rendering](https://astro.build/blog/hybrid-rendering/): Astro now supports hybrid rendering, combining the benefits of static site generation and server-side rendering for enhanced flexibility.
  * [Image](https://astro.build/blog/images/) and [Picture](https://astro.build/blog/astro-330/) components: Astro has introduced new Image and Picture components that simplify the handling of images and provide automatic optimization.
  * [View Transitions support](https://docs.astro.build/en/guides/view-transitions/): Astro offers built-in support for the [View Transitions API](https://developer.mozilla.org/docs/Web/API/View_Transitions_API), enabling smooth and seamless page transitions.
  * [Astro Dev Toolbar](https://astro.build/blog/astro-4/): The Astro Dev Toolbar provides a powerful set of tools for debugging and optimizing Astro applications.


### React
Last year, the [release](http://introduction) of React Server Components introduced a new approach to React components. Since then the React team has been working on a variety of new features including the React Compiler and Server Actions features, as well as:.
  * [Server Components](https://react.dev/reference/rsc/server-components): React server components are components that fetch data and are rendered on the server before being streamed to the client. This moves rendering work to the server and reduces the amount of code that needs to be shipped to the client.
  * [React Compiler](https://react.dev/blog/2024/02/15/react-labs-what-we-have-been-working-on-february-2024#react-compiler): React Compiler is a [compiler](https://www.youtube.com/watch?v=kjOacmVsLSE) that can automatically [memoize](https://react.dev/reference/react/useMemo) components. This improves performance by reducing unnecessary re-renders. The React team has said that developers will be able to adopt the React Compiler without making any code changes.
  * [Server Actions](https://react.dev/blog/2024/02/15/react-labs-what-we-have-been-working-on-february-2024#actions): Server Actions enable client-to-server communication. With Server Actions, you can define server-side functions that can be invoked directly from your React components, eliminating the need for manual API calls and complex state management. This can be particularly useful for things like data mutations and form submissions.
  * [Asset Loading](https://react.dev/blog/2024/02/15/react-labs-what-we-have-been-working-on-february-2024#:%7E:text=React%20Helmet.-,Asset%20Loading,-%3A%20we%20integrated%20Suspense): React has been working on declarative APIs for preloading and loading assets like scripts, styles, fonts, and images.
  * [Offscreen Rendering](https://react.dev/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023#offscreen-rendering): React has also been working on Offscreen Rendering. Offscreen Rendering is "an upcoming capability in React for rendering screens in the background without additional performance overhead. You can think of it as a version of [the content-visibility CSS property](https://web.dev/articles/content-visibility) that works not only for DOM elements but React components, too."


### Remix
Remix, a full-stack web framework, has been gaining traction in the developer community. With its focus on web fundamentals and enhanced developer experience, Remix has introduced several notable updates:
  * [Remix 2.0 release](https://remix.run/blog/remix-v2): Remix 2.0, released in September 2023, brought significant improvements and new features to the framework.
  * [Stable support for Vite](https://remix.run/blog/remix-vite-stable): Remix now offers stable support for Vite, a fast and lightweight build tool, providing faster development builds and improved performance.
  * [SPA mode](https://remix.run/docs/en/main/future/spa-mode): Remix introduced SPA mode, which allows building purely static sites without requiring a JavaScript server in production. This enables developers to use Remix's powerful features like file-based routing, automatic code splitting, and more, while maintaining the simplicity of static site deployment.


### Next.js
The release of [Next.js 13.4](http://Next.js) in May 2023 was particularly noteworthy as it ushered in stable support for React Server Components, streaming, and Suspense. Since then, Next.js continues to build out support for new React APIs (for example, [Server Actions](https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations)) and iterate on the developer experience through initiatives like [Turbopack](https://turbo.build/pack). Other highlights include:
  * [App Router](https://nextjs.org/docs/app): App Router, which became stable in Next.js 13.4, is a new way of structuring and managing routing in Next.js applications. App Router is a prerequisite to using new Next.js features like shared layouts and nested routing, as well as new React APIs like React Server Components, Suspense, and Server Actions in your Next.js app.
  * [Turbopack](https://turbo.build/pack): currently experimental) approach to page rendering that is built on top of [React's Suspense API](https://react.dev/reference/react/Suspense). Partial prerendering renders a page using a static loading shell. However, the shell leaves "holes" for the dynamic content within the page, and this content is loaded asynchronously. This provides the performance benefits of a cacheable, static page while still being able to incorporate dynamic data into page content.


### Vue
Vue's most recent release, [Vue 3.4](https://blog.vuejs.org/posts/vue-3-4), included a variety of performance improvements. Vue is also currently working on [Vue Vapor](https://github.com/vuejs/core-vapor), which is also performance-oriented. Here are a few highlights of what's going on in this space:
  * [Vue 3.4 released](https://blog.vuejs.org/posts/vue-3-4): Features include "a completely rewritten parser that is twice as fast, faster SFC compilation, and a [refactored](https://github.com/vuejs/core/pull/5912) reactivity system that [improves](https://twitter.com/johnsoncodehk/status/1740627870295437812) [re-compute](https://twitter.com/johnsoncodehk/status/1695383715906744449) efficiency."
  * [Vue Vapor Mode](https://blog.vuejs.org/posts/2022-year-in-review): Vue is working on Vapor Mode, an opt-in, performance-oriented compilation strategy that works with [Vue Single File Components](https://vuejs.org/guide/scaling-up/sfc.html). Vapor Mode [generates](https://vapor-repl.netlify.app/) code that is more performant than the code currently produced by the Vue Compiler. Additionally, using Vapor Mode with all components eliminates the need for the Vue Virtual DOM (which reduces bundle size).
  * [Vue 2 reaches EOL](https://blog.vuejs.org/posts/vue-2-eol): Vue 2's end-of-life (EOL) was December 31st, 2023. However, Vue 2 is still fairly widely used: ~50% of Vue npm package downloads are for Vue 2.


### Nuxt
Nuxt is [nearing the release of Nuxt 4](https://nuxt.com/blog/looking-forward-2024#what-about-nuxt-4). In addition to Nuxt's frequent framework releases over the past year, the Nuxt modules ecosystem has grown to almost 220 modules. Some recent developments in this space include:
  * [Nuxt 3.x releases](https://nuxt.com/blog*): Nuxt usually ships new minor releases monthly. Some highlights from these releases include [support for Vite 5](https://nuxt.com/blog/v3-9#%EF%B8%8F-vite-5), [server-only and client-only pages](https://nuxt.com/blog/v3-11#%EF%B8%8F-server-and-client-only-pages), [client-side Node.js support](https://nuxt.com/blog/v3-10#client-side-nodejs-support), and [native web streams](https://nuxt.com/blog/v3-7#%EF%B8%8F-native-web-streams-and-response). * [Nuxt Modules](https://nuxt.com/modules): Highlights from the Nuxt Modules ecosystem include the release of the new [nuxt/fonts](https://github.com/nuxt/fonts) module, and the 1.0 releases of [nuxt/image](https://nuxt.com/modules/image) and [Nuxt DevTools](https://nuxt.com/blog/introducing-nuxt-devtools). Upcoming module releases will include nuxt/scripts, nuxt/hints, nuxt/a11y, and nuxt/auth.
  * [Server Components](https://roe.dev/blog/nuxt-server-components) ([islands components](https://nuxt.com/docs/guide/directory-structure/components#standalone-server-components)): Nuxt continues to build out their support for server components (which is currently experimental). In Nuxt, these server-rendered components can be used within static sites - enabling adoption of an [Islands Architecture](https://www.patterns.dev/vanilla/islands-architecture/).


### Solid
[Solid](https://www.solidjs.com/) has been working towards the [stable 1.0 release](https://github.com/solidjs/solid-start/releases) of their meta-framework [SolidStart](https://start.solidjs.com/getting-started/what-is-solidstart). SolidStart boasts fine-grained reactivity, isomorphic routing, and support for a variety of rendering modes. Highlights include:
  * Fine-grained reactivity: Solid's reactivity system allows for precise updates and optimal performance, enabling efficient rendering and state management.
  * Isomorphic routing: SolidStart provides a unified approach to routing, allowing developers to define routes that work seamlessly on both the client and the server.
  * Flexible rendering modes: SolidStart supports various rendering modes, including server-side rendering, static site generation, and client-side rendering, giving developers the flexibility to choose the best approach for their application.


### Svelte
In the past year, the Svelte team has been focused on the upcoming release of Svelte 5, which will be significant. Other highlights include:
  * [Svelte 5 is coming](https://svelte.dev/blog/whats-new-in-svelte-may-2024): In addition to including a "[rewrite](https://svelte.dev/blog/svelte-4#svelte-5-the-next-generation-of-svelte) of the Svelte compiler and runtime", Svelte 5 also introduces the concept of [Runes](https://svelte.dev/blog/runes).
  * [Runes announced](https://svelte.dev/blog/runes): Runes are an upcoming feature in Svelte 5. "Runes unlock universal, fine-grained reactivity... With runes, reactivity extends beyond the boundaries of your .svelte files... Svelte 5's reactivity is powered by signals - however, [unlike other frameworks], in Svelte 5, signals are an under-the-hood implementation detail rather than something you interact with directly."
  * [SvelteKit 2 released](https://svelte.dev/blog/sveltekit-2): [SvelteKit](https://kit.svelte.dev/) is the meta-framework for Svelte. Features in this release include [shallow routing](https://kit.svelte.dev/) and support for Vite 5.


## Chrome Aurora
[Chrome Aurora](https://developer.chrome.com/docs/aurora) is a team at Google that collaborates with various open-source web frameworks to improve the user experience—particularly performance—across the web. Here are some of the initiatives that we've contributed to over the past year:
  * Images ([next/image](https://nextjs.org/docs/app/building-your-application/optimizing/images), [NgOptimizedImage](https://angular.io/guide/image-directive), and [nuxt/image](https://image.nuxt.com/?utm_source=nuxt_website&utm_medium=modules))
  * Font utilities ([next/font](https://nextjs.org/docs/app/building-your-application/optimizing/fonts), [nuxt/fonts](https://nuxt.com/modules/fonts), and [unjs/fontaine (Vite plugin)](https://github.com/unjs/fontaine)
  * Script loading ([next/script](https://nextjs.org/docs/app/building-your-application/optimizing/scripts) and nuxt/scripts)
  * Third-party script loading ([next/third-parties](https://nextjs.org/docs/app/building-your-application/optimizing/third-party-libraries), nuxt/third-parties, and Angular's [YouTube](https://github.com/angular/components/blob/main/src/youtube-player/README.md) and [Google Maps components](https://github.com/angular/components/tree/main/src/google-maps#readme))
  * Rendering: ([Angular SSR / hydration](https://angular.io/api/core/afterRender))


## Conclusion
The JavaScript framework ecosystem continues to evolve at a rapid pace, with each framework bringing its own set of innovations and improvements. Whether you're interested in the latest features of established frameworks like Angular, React, and Vue, or exploring newer options like Astro, Remix, and Solid, there's no shortage of exciting developments to keep up with.
As developers, staying informed about these advancements helps us make informed decisions when choosing a framework for our projects. By understanding the strengths and unique features of each framework, we can select the one that aligns best with our project requirements and development preferences.
We hope this overview has provided you with a glimpse into the current state of JavaScript frameworks. To dive deeper into the topics covered in this blog post, be sure to check out the accompanying talk from Google I/O. Happy coding!
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-05-16 UTC.

