---
url: https://docs.expo.dev/versions/latest/sdk/checkbox
title: https://docs.expo.dev/versions/latest/sdk/checkbox
date: 2025-04-30T17:15:48.266354
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo Checkbox
A universal React component that provides basic checkbox functionality.
Android
iOS
Web
Bundled version:
~4.0.1
`expo-checkbox` provides a basic `boolean` input element for all platforms.
## Installation
Terminal
Copy
`- ``npx expo install expo-checkbox`
## Usage
Basic Checkbox usage
```
import Checkbox from 'expo-checkbox';
import { useState } from 'react';
import { StyleSheet, Text, View } from 'react-native';
export default function App() {
 const [isChecked, setChecked] = useState(false);
 return (
  <View style={styles.container}><View style={styles.section}><Checkbox style={styles.checkbox} value={isChecked} onValueChange={setChecked} /><Text style={styles.paragraph}>Normal checkbox</Text></View><View style={styles.section}><Checkbox
     style={styles.checkbox}
     value={isChecked}
     onValueChange={setChecked}
     color={isChecked ? '#4630EB' : undefined}
    /><Text style={styles.paragraph}>Custom colored checkbox</Text></View><View style={styles.section}><Checkbox style={styles.checkbox} disabled value={isChecked} onValueChange={setChecked} /><Text style={styles.paragraph}>Disabled checkbox</Text></View></View>
 );
}
const styles = StyleSheet.create({
 container: {
  flex: 1,
  marginHorizontal: 16,
  marginVertical: 32,
 },
 section: {
  flexDirection: 'row',
  alignItems: 'center',
 },
 paragraph: {
  fontSize: 15,
 },
 checkbox: {
  margin: 8,
 },
});

Show More

```

## API
```
import Checkbox from 'expo-checkbox';

```

## Component
### `Checkbox`
Android
iOS
Web
Type: `React.Element[](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<CheckboxProps[](https://docs.expo.dev/versions/latest/sdk/checkbox/#checkboxprops)>`
CheckboxProps
### `color`
Android
iOS
Web
Optional • Type: 
The tint or color of the checkbox. This overrides the disabled opaque style.
### `disabled`
Android
iOS
Web
Optional • Type: `boolean`
If the checkbox is disabled, it becomes opaque and uncheckable.
### `onChange`
Android
iOS
Web
Optional • Type: `(event: NativeSyntheticEvent<> | SyntheticEvent[](https://react.dev/reference/react-dom/components/common#react-event-object)<>) => void`
Callback that is invoked when the user presses the checkbox.
`event: NativeSyntheticEvent<> | SyntheticEvent[](https://react.dev/reference/react-dom/components/common#react-event-object)<>`
A native event containing the checkbox change.
### `onValueChange`
Android
iOS
Web
Optional • Type: `(value: boolean) => void`
Callback that is invoked when the user presses the checkbox.
`value: boolean`
A boolean indicating the new checked state of the checkbox.
### `value`
Android
iOS
Web
Optional • Type: `boolean` • Default: `false`
Value indicating if the checkbox should be rendered as checked or not.
#### Inherited Props
  * 

## Types
### `CheckboxEvent`
Android
iOS
Web
Property| Type| Description  
---|---|---  
target| `any`| On native platforms, a `NodeHandle` for the element on which the event has occurred. On web, a DOM node on which the event has occurred.  
value| `boolean`| A boolean representing checkbox current value.

