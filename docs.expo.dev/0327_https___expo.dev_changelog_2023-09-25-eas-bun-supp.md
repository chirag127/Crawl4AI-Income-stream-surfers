---
url: https://expo.dev/changelog/2023-09-25-eas-bun-support
title: https://expo.dev/changelog/2023-09-25-eas-bun-support
date: 2025-04-30T17:18:38.434761
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [Support for Bun in EAS and Expo CLI](https://expo.dev/changelog/2023-09-25-eas-bun-support)
Sep 25, 2023 by
Kadi Kraman
We have added support for [Bun](https://bun.sh/) on Expo CLI and EAS! This means you can use Bun to create your Expo app, install packages, run scripts and build your app on EAS.
## [Using Bun locally ](https://expo.dev/changelog/2023-09-25-eas-bun-support#using-bun-locally)
The first step (if you haven't yet) is to [install](https://bun.sh/docs/installation) Bun on your local machine. After installation, you should have access to `bun` in your terminal.
To create a new Expo app:
Terminal
Copy
`bun create expo my-app`
Run a **package.json** script:
Terminal
Copy
`bun run ios`
Install a package:
Terminal
Copy
`bun expo install expo-av`
You can also use Bun to install packages, but output a readable **yarn.lock** as well as the **bun.lockb** :
Terminal
Copy
`bun install --yarn`
## [Using Bun for EAS builds ](https://expo.dev/changelog/2023-09-25-eas-bun-support#using-bun-for-eas-builds)
EAS will decide which packager to use based the lockfile in your codebase. So if you want EAS to use Bun, run `bun install` in your codebase and ensure it creates a **bun.lockb** - the Bun lockfile. As long as this lockfile is in your codebase, Bun will be used as the package manager for your builds.
## [Customizing your Bun version on EAS ](https://expo.dev/changelog/2023-09-25-eas-bun-support#customizing-your-bun-version-on-eas)
EAS will use `bun@1.0.2` by default. If you want or need to use a particular version of Bun, you can configure the exact version in each build in your **eas.json**.
eas.json
Copy
```

"build":{
"test":{
"bun":"1.0.0"
// other settings...
// other build profiles...

```


