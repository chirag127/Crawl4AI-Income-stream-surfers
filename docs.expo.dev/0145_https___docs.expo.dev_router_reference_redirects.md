---
url: https://docs.expo.dev/router/reference/redirects
title: https://docs.expo.dev/router/reference/redirects
date: 2025-04-30T17:14:28.182397
depth: 2
---

Search
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Redirects
Learn how to redirect URLs in Expo Router.
You can redirect a request to a different URL based on some in-app criteria. Expo Router supports a number of different redirection patterns.
## Using `Redirect` component
You can immediately redirect from a particular screen by using the `Redirect` component:
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

## Using `useRouter` hook
You can also redirect imperatively with the `useRouter` hook:
```
import { Text } from 'react-native';
import { useRouter, useFocusEffect } from 'expo-router';
function MyScreen() {
 const router = useRouter();
 useFocusEffect(() => {
  // Call the replace method to redirect to a new route without adding to the history.
  // We do this in a useFocusEffect to ensure the redirect happens every time the screen
  // is focused.
  router.replace('/profile/settings');
 });
 return <Text>My Screen</Text>;
}

```


