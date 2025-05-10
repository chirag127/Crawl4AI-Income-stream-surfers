---
url: https://reactnative.dev/docs/navigation
title: https://reactnative.dev/docs/navigation
date: 2025-05-10T21:41:01.650896
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/navigation#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
Mobile apps are rarely made up of a single screen. Managing the presentation of, and transition between, multiple screens is typically handled by what is known as a navigator.
This guide covers the various navigation components available in React Native. If you are getting started with navigation, you will probably want to use [React Navigation](https://reactnative.dev/docs/navigation#react-navigation). React Navigation provides a straightforward navigation solution, with the ability to present common stack navigation and tabbed navigation patterns on both Android and iOS.
If you're integrating React Native into an app that already manages navigation natively, or looking for an alternative to React Navigation, the following library provides native navigation on both platforms: [react-native-navigation](https://github.com/wix/react-native-navigation).
## React Navigation[​](https://reactnative.dev/docs/navigation#react-navigation "Direct link to React Navigation")
The community solution to navigation is a standalone library that allows developers to set up the screens of an app with a few lines of code.
### Installation and setup[​](https://reactnative.dev/docs/navigation#installation-and-setup "Direct link to Installation and setup")
First, you need to install them in your project:
shell
```
npminstall @react-navigation/native @react-navigation/native-stack
```

Next, install the required peer dependencies. You need to run different commands depending on whether your project is an Expo managed project or a bare React Native project.
  * If you have an Expo managed project, install the dependencies with `expo`:
shell
```
npx expo install react-native-screens react-native-safe-area-context
```

  * If you have a bare React Native project, install the dependencies with `npm`:
shell
```
npminstall react-native-screens react-native-safe-area-context
```

For iOS with bare React Native project, make sure you have [CocoaPods](https://cocoapods.org/) installed. Then install the pods to complete the installation:
shell
```
cd iospod installcd..
```



note
You might get warnings related to peer dependencies after installation. They are usually caused by incorrect version ranges specified in some packages. You can safely ignore most warnings as long as your app builds.
Now, you need to wrap the whole app in `NavigationContainer`. Usually you'd do this in your entry file, such as `index.js` or `App.js`:
tsx
```
import*asReactfrom'react';import{NavigationContainer}from'@react-navigation/native';constApp=()=>{return(<NavigationContainer>{/* Rest of your app code */}</NavigationContainer>exportdefaultApp;
```

Now you are ready to build and run your app on the device/simulator.
### Usage[​](https://reactnative.dev/docs/navigation#usage "Direct link to Usage")
Now you can create an app with a home screen and a profile screen:
tsx
```
import*asReactfrom'react';import{NavigationContainer}from'@react-navigation/native';import{createNativeStackNavigator}from'@react-navigation/native-stack';constStack=createNativeStackNavigator();constMyStack=()=>{return(<NavigationContainer><Stack.Navigator><Stack.Screenname="Home"component={HomeScreen}options={{title:'Welcome'}}/><Stack.Screenname="Profile"component={ProfileScreen}/></Stack.Navigator></NavigationContainer>
```

In this example, there are 2 screens (`Home` and `Profile`) defined using the `Stack.Screen` component. Similarly, you can define as many screens as you like.
You can set options such as the screen title for each screen in the `options` prop of `Stack.Screen`.
Each screen takes a `component` prop that is a React component. Those components receive a prop called `navigation` which has various methods to link to other screens. For example, you can use `navigation.navigate` to go to the `Profile` screen:
tsx
```
constHomeScreen=({navigation})=>{return(<Buttontitle="Go to Jane's profile"onPress={()=>    navigation.navigate('Profile',{name:'Jane'})/>constProfileScreen=({navigation, route})=>{return<Text>This is {route.params.name}'s profile</Text>;
```

This `native-stack` navigator uses the native APIs: `UINavigationController` on iOS and `Fragment` on Android so that navigation built with `createNativeStackNavigator` will behave the same and have the same performance characteristics as apps built natively on top of those APIs.
React Navigation also has packages for different kind of navigators such as tabs and drawer. You can use them to implement various patterns in your app.
For a complete intro to React Navigation, follow the [React Navigation Getting Started Guide](https://reactnavigation.org/docs/getting-started).
Is this page useful?
  * [React Navigation](https://reactnative.dev/docs/navigation#react-navigation)
    * [Installation and setup](https://reactnative.dev/docs/navigation#installation-and-setup)



