---
url: https://snack.expo.dev/@expo-team-snacks/social-app
title: https://snack.expo.dev/@expo-team-snacks/social-app
date: 2025-04-30T17:19:41.233670
depth: 2
---

# 
Social app 
No description
Edit details
[Log in](https://expo.dev/login?redirect_uri=https%3A%2F%2Fsnack.expo.dev%2F%40expo-team-snacks%2Fsocial-app%3FhideQueryParams%3Dtrue) to save your changes as you work
[Expo Docs](https://docs.expo.dev/versions/v52.0.0/)SavedRun on deviceDownload as zipShow embed code
#### Open files
  * ×
App.js


#### Project
assets
components
data
screens
App.js
package.json
README.md
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
import { NavigationContainer, DefaultTheme } from
'@react-navigation/native';
import { createStackNavigator } from
'@react-navigation/stack';
importHomefrom'./screens/Home';
importProfilefrom'./screens/Profile';
constStack = createStackNavigator();
exportdefaultfunctionApp() {
return (
NavigationContainer
theme={{
...DefaultTheme,
colors: {
...DefaultTheme.colors,
background: '#fff',
card: '#f1f3f5',
border: 'transparent',
},
}}>
Stack.Navigator
initialRouteName="Home"
screenOptions={{
headerBackTitleVisible: false,
}}>
Enter to Rename, Shift+Enter to Preview
My DeviceAndroidiOSWeb
package.json (4:5) '@shopify/flash-list@1.7.1' is not the recommended version for SDK 52.0.0. Update to 1.7.3
Prettier
Editor
Expov48.0.0v49.0.0v50.0.0v51.0.0v52.0.0
Devices0
Preview

