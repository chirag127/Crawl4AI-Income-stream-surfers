---
url: https://docs.expo.dev/guides/using-logrocket
title: https://docs.expo.dev/guides/using-logrocket
date: 2025-04-30T17:14:04.164369
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Using LogRocket
A guide on installing and configuring LogRocket for session replays and error monitoring.
[LogRocket](https://logrocket.com) records user sessions and identifies bugs as your users use your app. You can filter sessions by update IDs and also connect to your LogRocket account on the Expo dashboard to get quick access to your app's session data.
## Install and configure LogRocket
You can install the LogRocket SDK with the following command:
Terminal
Copy
`- ``npx expo install @logrocket/react-native expo-build-properties`
Then, in your [app config](https://docs.expo.dev/workflow/configuration), include the LogRocket config plugin:
app.json
Copy
```
{
 "plugins": [
  [
   "expo-build-properties",
   {
    "android": {
     "minSdkVersion": 25
    }
   }
  ],
  "@logrocket/react-native"
 ]
}

```

Finally, initialize LogRocket in your app in a top-level file, like app/_layout.tsx:
app/_layout.tsx
Copy
```
import { useEffect } from 'react';
import * as Updates from 'expo-updates';
import LogRocket from '@logrocket/react-native';
const App = () => {
 useEffect(() => {
  LogRocket.init('<App ID>', {
   updateId: Updates.isEmbeddedLaunch ? null : Updates.updateId,
   expoChannel: Updates.channel,
  });
 }, []);
};

```

In the code above, replace `<App ID>` with your [LogRocket App ID](https://app.logrocket.com/r/settings/setup).
## Connecting LogRocket on the Expo dashboard
You can link your LogRocket account and project to your Expo account and project on Expo's dashboard, so that you can see the last few sessions from your app in the deployments and updates dashboards.
Go to your [account settings](https://expo.dev/accounts/%5Baccount%5D/settings) and click Connect to authenticate with LogRocket:
Then, go to your [project settings](https://expo.dev/accounts/%5Baccount%5D/projects/%5BprojectName%5D/settings) and click Connect to link your LogRocket project with your project on Expo:
Then, you'll start to see View on LogRocket buttons in the Expo dashboard in the Deployments and Updates dashboards, along with the last few sessions from your app.
## Learn more about LogRocket
To learn more about how to use LogRocket with Expo, check out the [LogRocket documentation](https://docs.logrocket.com/reference/react-native-expo-adding-the-sdk).

