---
url: https://expo.dev/changelog/2023-08-10-custom-builds
title: https://expo.dev/changelog/2023-08-10-custom-builds
date: 2025-04-30T17:18:38.399691
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [Preview: fully customizable builds on EAS Build](https://expo.dev/changelog/2023-08-10-custom-builds)
Aug 10, 2023 by
Szymon Dziedzic
It’s extremely satisfying when you `eas build` on a new project and it Just Works — at Expo, we know what we need to do to build Android and iOS React Native apps, and we handle all of that automatically for you. In many cases, this is all a project ever needs; but, not always.
We’ve come across a number of cases where developers have asked to replace single steps in their build process with their own implementations (such as for [installing dependencies for Rush or Nx monorepos](https://expo.canny.io/feature-requests/p/eas-custom-install-command)) or even replace the majority of the build process in order to build for another platform (such as Electron app or one of the many TV platforms). We’ve also heard from developers that want to use EAS Build to run their test suite, so that they could consolidate their CI into a single service.
To enable all of these use cases and more, **today we are releasing a preview of our new fully customizable build process**. You can use it by creating a `yml` file in `.eas/build` and pointing to that file from the `config` field on your build profile. For example, you can configure a build profile to run tests with the following:
eas.json
Copy
```

"build":{
"test":{
"config":"test.yml",
"withoutCredentials":true
// other build profiles...

```

.eas/build/test.yml
Copy
```

build:
name: Run tests
steps:
- eas/checkout
- eas/install_node_modules
-run:
name: Unit tests
command:|
     echo "Running tests..."
     npm test

```

When you run `eas build -p android --profile test`, you'll see the following:
## [Reusing existing build steps ](https://expo.dev/changelog/2023-08-10-custom-builds#reusing-existing-build-steps)
If you needed to rewrite the entire build process from scratch as soon as you wanted to replace a single step, this wouldn’t be particularly useful. Each step in the standard build process can be used in your custom build definition. In the above **test.yml** example, we are using `eas/checkout` to check out the repository and `eas/install_node_modules` to re-use the same logic for installing Node modules (select the correct package manager, handle monorepos appropriately, etc).
For example, the following steps will create a development build for Android:
Code
Copy
```

build:
name: Development build - Android
steps:
- eas/checkout
- eas/use_npm_token
- eas/install_node_modules
- eas/prebuild
- eas/run_gradle
- eas/find_and_upload_build_artifacts

```

And the equivalent for iOS:
Code
Copy
```

build:
name: Development build - iOS
steps:
- eas/checkout
- eas/use_npm_token
- eas/install_node_modules
- eas/prebuild
-run:
name: Install pods
working_directory: ./ios
command: pod install
- eas/generate_gymfile_from_template
- eas/run_fastlane
- eas/find_and_upload_build_artifacts

```

Example configurations for store-ready builds are available in the [eas-custom-builds-example](https://github.com/expo/eas-custom-builds-example/) repository: [Android](https://github.com/expo/eas-custom-builds-example/blob/main/.eas/build/production-build-android.yml), [iOS](https://github.com/expo/eas-custom-builds-example/blob/main/.eas/build/production-build-ios.yml).
You can learn more about the provided reusable steps and others in the [“Built-in EAS functions” documentation](https://docs.expo.dev/custom-builds/schema/#built-in-eas-functions). You can also fork these steps in your own JavaScript / TypeScript functions, or write your own build steps from scratch.
## [Writing build steps in JavaScript / TypeScript ](https://expo.dev/changelog/2023-08-10-custom-builds#writing-build-steps-in-javascript--typescript)
If you’d like to fork a default build step, or if you just want to use JavaScript or TypeScript instead of Bash because the logic for a step is complex, you can run `npx create-eas-build-function@latest .eas/build/my-new-function` to create a new function (we suggest creating the function in the `.eas/build` directory, next to your YAML configuration — but you can put the functions anywhere in your repository).
After you’ve defined your function, you can refer to it from your build configuration YAML file. Refer to the **README.md** in the generated directory for more information about how to use it. Your configuration will look something like this:
eas.json
Copy
```

"build":{
"test":{
"config":"test.yml",
"withoutCredentials":true
// other build profiles...

```

.eas/build/test.yml
Copy
```

build:
 name: Run tests
 steps:
  - eas/checkout
  - eas/install_node_modules
  - run:
    name: Unit tests
    command: npm run test
  - my-new-function
functions:
 my-new-function:
  name: my-new-function
  path: ./my-new-function

```

.eas/build/my-new-function/src/index.ts
Copy
```

import { BuildStepContext } from '@expo/steps';
async function myFunction(ctx: BuildStepContext): Promise<void> {
 ctx.logger.info('Hello from my TypeScript function!');
export default myFunction;

```

[Learn more about creating EAS Build functions with TypeScript](http://docs.expo.dev/custom-builds/functions/).
## [Current limitations ](https://expo.dev/changelog/2023-08-10-custom-builds#current-limitations)
  * **These features are currently in preview and are likely to change** : APIs may change as we continue to iterate on them and on the the system as a whole. We expect custom builds to reach General Availability (GA) by late 2023 / early 2024.
  * **EAS Build pricing model is not yet adapted to new use cases enabled by custom builds** : while in preview, builds with custom configurations will be priced [the same as standard builds](https://expo.dev/pricing). As the feature approaches GA, we will roll out pricing that is more appropriate to the usage patterns. We understand that for many folks this uncertainty may be a blocker for beginning to invest in adopting custom builds, and we will do our best to communicate the pricing model as soon as possible.
  * **Artifacts can only be uploaded once during a build job** : it is currently only possible to upload files once for each artifact type (application archive, generic build artifacts). So if you want to upload multiple artifacts, you will need to do that after all of the artifacts are ready, rather than as part of the steps where those artifacts are prepared. [Example of uploading artifacts](https://github.com/expo/eas-custom-builds-example/blob/main/.eas/build/upload.yml).
  * **Reusable step for caching dependencies and outputs is not ready yet** : we don’t yet expose a re-usable step for caching files that would speed up subsequent build runs.
  * **Classic Update is not supported** : the `eas/configure-eas-update-if-installed` step only supports EAS Update. [Example of configuring EAS Update](https://github.com/expo/eas-custom-builds-example/blob/d5556653daf68a230e349df5e5ef65f21a5c0753/.eas/build/eas-update-build-ios.yml#L27).
  * **Build jobs nominally tied to target platforms** : custom builds are still identified as either Android or iOS builds — this may not be true for many use cases, such as if you are running unit tests for multiple platforms or building for a different platform. For now, perform an “Android” build if you would like to use a Linux worker, and “iOS” builds if you’d like to use a macOS worker.
  * **GitHub integration not ready yet** : custom build jobs can’t yet be triggered from the [EAS GitHub integration](https://expo.dev/changelog/2023/07-19-github-linking).

## [Try it out and give us feedback! ](https://expo.dev/changelog/2023-08-10-custom-builds#try-it-out-and-give-us-feedback)
This new feature helps bring EAS Build more in alignment with the spirit of how we think about building apps at Expo — our tools and services give you great defaults out of the box, and when you need to, you can opt-out of any those default choices and customize any part of your experience without having to face a sudden complexity cliff. Keep what works for you, change what doesn’t.
Some ideas for areas we’d like feedback on:
  * There are small differences between the default build process and the equivalent composed of assembling the required steps ([Android example](https://github.com/expo/eas-custom-builds-example/blob/main/.eas/build/production-build-android.yml), [iOS example](https://github.com/expo/eas-custom-builds-example/blob/main/.eas/build/production-build-ios.yml)). Some are intentional, such as not supporting classic update configuration, and others might not be. Please report any discrepancies that you encounter that impact your project.
  * Try out the [reusable](https://docs.expo.dev/custom-builds/schema/#built-in-eas-functions) [`eas/`](https://docs.expo.dev/custom-builds/schema/#built-in-eas-functions) [functions](https://docs.expo.dev/custom-builds/schema/#built-in-eas-functions). Are they the right level of abstraction? Should they accept additional inputs for further customization, or provide additional outputs for use in subsequent steps?
  * Every team has their own unique culture and preferences around tools and workflows, let us know if we’re missing something or could improve the APIs to better fit your use cases.


Feel free to send us feedback on [Discord](https://chat.expo.dev/), [@expo](https://twitter.com/expo), [Threads](https://www.threads.net/@expo.dev), or [Bluesky](https://bsky.app/profile/expo.dev).
_A special mention goes out to_  _[Dominik Sokal](https://github.com/dsokal), who built out the foundation of custom builds._

