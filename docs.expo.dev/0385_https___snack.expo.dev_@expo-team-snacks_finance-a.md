---
url: https://snack.expo.dev/@expo-team-snacks/finance-app
title: https://snack.expo.dev/@expo-team-snacks/finance-app
date: 2025-04-30T17:19:40.891607
depth: 2
---

# 
Finance app 
No description
Edit details
[Log in](https://expo.dev/login?redirect_uri=https%3A%2F%2Fsnack.expo.dev%2F%40expo-team-snacks%2Ffinance-app%3FhideQueryParams%3Dtrue) to save your changes as you work
[Expo Docs](https://docs.expo.dev/versions/v52.0.0/)SavedRun on deviceDownload as zipShow embed code
#### Open files
  * ×
App.js


#### Project
assets
components
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
26
27
import { View, StyleSheet } from'react-native';
importConstantsfrom'expo-constants';
importCardfrom'./components/Card';
importBalancefrom'./components/Balance';
importTransactionsfrom'./components/Transactions';
exportdefaultfunctionApp() {
return (
View style={styles.container}>
View style={styles.staticSection}>
Card />
Balance />
</View>
Transactions />
</View>
);
const styles = StyleSheet.create({
container: {
flex: 1,
gap: 16,
paddingTop: 16 + Constants.statusBarHeight,
backgroundColor: '#ecf0f1',
overflowX: 'hidden',
},
Enter to Rename, Shift+Enter to Preview
My DeviceAndroidiOSWeb
package.json (3:5) 'expo-constants@~17.0.3' is not the recommended version for SDK 52.0.0. Update to ~17.0.8
Prettier
Editor
Expov48.0.0v49.0.0v50.0.0v51.0.0v52.0.0
Devices1
Preview
Device connected!

