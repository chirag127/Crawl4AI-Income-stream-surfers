---
url: https://docs.expo.dev/versions/latest/sdk/router-ui
title: https://docs.expo.dev/versions/latest/sdk/router-ui
date: 2025-04-30T17:17:22.528276
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo Router UI
An Expo Router submodule that provides headless tab components to create custom tab layouts.
Android
iOS
tvOS
Web
Bundled version:
~4.0.20
`expo-router/ui` is a submodule of `expo-router` library and exports components and hooks to build custom tab layouts, rather than using the default [React Navigation](https://reactnavigation.org/) navigators provided by `expo-router`.
> See the [Expo Router](https://docs.expo.dev/versions/latest/sdk/router) reference for more information about the file-based routing library for native and web app.
## Installation
To use `expo-router/ui` in your project, you need to install `expo-router` in your project. Follow the instructions from the [Install Expo Router](https://docs.expo.dev/router/installation) guide.
## Configuration in app config
If you are using the [default](https://docs.expo.dev/more/create-expo#--template) template to create a new project, `expo-router` [config plugin](https://docs.expo.dev/config-plugins/introduction) is automatically configured in the app config automatically.
### Example app.json with config plugin
app.json
Copy
```
{
 "expo": {
  "plugins": ["expo-router"]
 }
}

```

## Usage
Find more information about using `expo-router/ui` in [Expo Router UI](https://docs.expo.dev/router/advanced/custom-tabs) guide.
## API
```
import { Tabs, TabList, TabTrigger, TabSlot } from 'expo-router/ui';

```

## Components
### `TabList`
Android
iOS
tvOS
Web
Type: `React.Element[](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<TabListProps[](https://docs.expo.dev/versions/latest/sdk/router-ui/#tablistprops)>`
Wrapper component for `TabTriggers`. `TabTriggers` within the `TabList` define the tabs.
Example
```
<Tabs><TabSlot /><TabList><TabTrigger name="home" href="/" /></TabList></Tabs>

```

TabListProps
### `asChild`
Android
iOS
tvOS
Web
Optional • Type: `boolean`
Forward props to child component and removes the extra `<View>`. Useful for custom wrappers.
#### Inherited Props
  * 

### `Tabs`
Android
iOS
tvOS
Web
Type: `React.Element[](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<TabsProps[](https://docs.expo.dev/versions/latest/sdk/router-ui/#tabsprops)>`
Root component for the headless tabs.
> See: [`useTabsWithChildren`](https://docs.expo.dev/versions/latest/sdk/router-ui/#usetabswithchildrenoptions) for a hook version of this component.
Example
```
<Tabs><TabSlot /><TabList><TabTrigger name="home" href="/" /></TabList></Tabs>

```

TabsProps
### `asChild`
Android
iOS
tvOS
Web
Optional • Type: `boolean`
Forward props to child component and removes the extra `<View>`. Useful for custom wrappers.
### `options`
Android
iOS
tvOS
Web
Optional • Type: `UseTabsOptions[](https://docs.expo.dev/versions/latest/sdk/router-ui/#usetabsoptions)`
#### Inherited Props
  * 

### `TabSlot`
Android
iOS
tvOS
Web
Type: `React.Element[](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<TabSlotProps[](https://docs.expo.dev/versions/latest/sdk/router-ui/#tabslotprops)>`
Renders the current tab.
> See: [`useTabSlot`](https://docs.expo.dev/versions/latest/sdk/router-ui/#usetabslot) for a hook version of this component.
Example
```
<Tabs><TabSlot /><TabList><TabTrigger name="home" href="/" /></TabList></Tabs>

```

TabSlotProps
### `detachInactiveScreens`
Android
iOS
tvOS
Web
Optional • Type: `boolean`
Remove inactive screens.
### `renderFn`
Android
iOS
tvOS
Web
Optional • Type: `defaultTabsSlotRender`
Override how the `Screen` component is rendered.
#### Inherited Props
  * `ComponentProps<ScreenContainer>`


### `TabTrigger`
Android
iOS
tvOS
Web
Type: `React.Element[](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<TabTriggerProps[](https://docs.expo.dev/versions/latest/sdk/router-ui/#tabtriggerprops)>`
Creates a trigger to navigate to a tab. When used as child of `TabList`, its functionality slightly changes since the `href` prop is required, and the trigger also defines what routes are present in the `Tabs`.
When used outside of `TabList`, this component no longer requires an `href`.
Example
```
<Tabs><TabSlot /><TabList><TabTrigger name="home" href="/" /></TabList></Tabs>

```

TabTriggerProps
### `asChild`
Android
iOS
tvOS
Web
Optional • Type: `boolean`
Forward props to child component. Useful for custom wrappers.
### `href`
Android
iOS
tvOS
Web
Optional • Type: 
Name of tab. Required when used within a `TabList`.
### `name`
Android
iOS
tvOS
Web
Type: `string`
Name of tab. When used within a `TabList` this sets the name of the tab. Otherwise, this references the name.
### `reset`
Android
iOS
tvOS
Web
Optional • Literal type: `union`
Resets the route when switching to a tab.
Acceptable values are: `SwitchToOptions[reset]` | `'onLongPress'`
#### Inherited Props
  * `PressablePropsWithoutFunctionChildren[](https://docs.expo.dev/versions/latest/sdk/router-ui/#pressablepropswithoutfunctionchildren)`


### `useTabSlot`
Android
iOS
tvOS
Web
Type: `React.Element[](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<TabSlotProps[](https://docs.expo.dev/versions/latest/sdk/router-ui/#tabslotprops)>`
Returns a `ReactElement` of the current tab.
Example
```
function MyTabSlot() {
 const slot = useTabSlot();
 return slot;
}

```

## Constants
### `Tabs.TabContext`
Android
iOS
tvOS
Web
Type: `Context[](https://docs.expo.dev/versions/latest/sdk/router-ui/#context)<ExpoTabsNavigatorScreenOptions[](https://docs.expo.dev/versions/latest/sdk/router-ui/#expotabsnavigatorscreenoptions)>`
## Hooks
### `useTabSlot(namedParameters)`
Android
iOS
tvOS
Web
Parameter| Type  
---|---  
namedParameters(optional)|   
Returns a `ReactElement` of the current tab.
Returns:
Example
```
function MyTabSlot() {
 const slot = useTabSlot();
 return slot;
}

```

### `useTabsWithChildren(options)`
Android
iOS
tvOS
Web
Parameter| Type  
---|---  
options| `UseTabsWithChildrenOptions[](https://docs.expo.dev/versions/latest/sdk/router-ui/#usetabswithchildrenoptions)`  
Hook version of `Tabs`. The returned NavigationContent component should be rendered.
> See: [`Tabs`](https://docs.expo.dev/versions/latest/sdk/router-ui/#tabs) for the component version of this hook.
Example
```
export function MyTabs({ children }) {
 const { NavigationContent } = useTabsWithChildren({ children })
 return <NavigationContent />
}

```

### `useTabsWithTriggers(options)`
Android
iOS
tvOS
Web
Parameter| Type  
---|---  
options| `UseTabsWithTriggersOptions[](https://docs.expo.dev/versions/latest/sdk/router-ui/#usetabswithtriggersoptions)`  
Alternative hook version of `Tabs` that uses explicit triggers instead of `children`.
Returns:
`TabsContextValue[](https://docs.expo.dev/versions/latest/sdk/router-ui/#tabscontextvalue)`
> See: [`Tabs`](https://docs.expo.dev/versions/latest/sdk/router-ui/#tabs) for the component version of this hook.
Example
```
export function MyTabs({ children }) {
 const { NavigationContent } = useTabsWithChildren({ triggers: [] })
 return <NavigationContent />
}

```

### `useTabTrigger(options)`
Android
iOS
tvOS
Web
Parameter| Type  
---|---  
options| `TabTriggerProps[](https://docs.expo.dev/versions/latest/sdk/router-ui/#tabtriggerprops)`  
Utility hook creating custom `TabTrigger`.
Returns:
`UseTabTriggerResult[](https://docs.expo.dev/versions/latest/sdk/router-ui/#usetabtriggerresult)`
## Types
### `ExpoTabsNavigationProp`
Android
iOS
tvOS
Web
Type: `NavigationProp[](https://docs.expo.dev/versions/latest/sdk/router-ui/#navigationprop)<TabNavigationState[](https://reactnavigation.org/docs/custom-navigators/#type-checking-navigators)<ParamListBase>, ExpoTabsScreenOptions[](https://docs.expo.dev/versions/latest/sdk/router-ui/#expotabsscreenoptions), TabNavigationEventMap[](https://docs.expo.dev/versions/latest/sdk/router-ui/#tabnavigationeventmap)>`
### `ExpoTabsNavigatorOptions`
Android
iOS
tvOS
Web
Literal Type: `union`
Acceptable values are: `DefaultNavigatorOptions[](https://reactnavigation.org/docs/custom-navigators/#type-checking-navigators)<ParamListBase, string | undefined, TabNavigationState[](https://reactnavigation.org/docs/custom-navigators/#type-checking-navigators)<ParamListBase>, ExpoTabsScreenOptions[](https://docs.expo.dev/versions/latest/sdk/router-ui/#expotabsscreenoptions), TabNavigationEventMap[](https://docs.expo.dev/versions/latest/sdk/router-ui/#tabnavigationeventmap), ExpoTabsNavigationProp[](https://docs.expo.dev/versions/latest/sdk/router-ui/#expotabsnavigationprop)<ParamListBase>>` | `Omit[](https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys)<'initialRouteName'>` | `ExpoTabsNavigatorScreenOptions[](https://docs.expo.dev/versions/latest/sdk/router-ui/#expotabsnavigatorscreenoptions)`
### `ExpoTabsNavigatorScreenOptions`
Android
iOS
tvOS
Web
Property| Type| Description  
---|---|---  
detachInactiveScreens(optional)| `boolean`  
freezeOnBlur(optional)| `boolean`  
lazy(optional)| `boolean`  
unmountOnBlur(optional)| `boolean`  
### `ExpoTabsResetValue`
Android
iOS
tvOS
Web
Literal Type: `string`
Acceptable values are: `'always'` | `'onFocus'` | `'never'`
### `ExpoTabsScreenOptions`
Android
iOS
tvOS
Web
Type: `Pick[](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)<BottomTabNavigationOptions[](https://docs.expo.dev/versions/latest/sdk/router-ui/#bottomtabnavigationoptions), 'title' | 'lazy' | 'freezeOnBlur'>` extended by:
Property| Type| Description  
---|---|---  
action| `NavigationAction[](https://docs.expo.dev/versions/latest/sdk/router-ui/#navigationaction)`  
params(optional)| `object`  
title| `string`  
### `SwitchToOptions`
Android
iOS
tvOS
Web
Options for `switchTab` function.
Property| Type| Description  
---|---|---  
reset(optional)| `ExpoTabsResetValue[](https://docs.expo.dev/versions/latest/sdk/router-ui/#expotabsresetvalue)`| Navigate and reset the history.  
### `TabNavigationEventMap`
Android
iOS
tvOS
Web
Property| Type| Description  
---|---|---  
tabLongPress| `{  data: undefined }`| Event which fires on long press on the tab in the tab bar.  
tabPress| `{  canPreventDefault: true,   data: undefined }`| Event which fires on tapping on the tab in the tab bar.  
### `TabsContextValue`
Android
iOS
tvOS
Web
Type: `ReturnType[](https://docs.expo.dev/versions/latest/sdk/router-ui/#returntype)<useNavigationBuilder>`
The React Navigation custom navigator.
> See: [`useNavigationBuilder`](https://reactnavigation.org/docs/custom-navigators/#usenavigationbuilder) hook from React Navigation for more information.
### `TabsSlotRenderOptions`
Android
iOS
tvOS
Web
Options provided to the `UseTabSlotOptions`.
Property| Type| Description  
---|---|---  
detachInactiveScreens| `boolean`| Should the screen be unloaded when inactive.  
index| `number`| Index of screen.  
isFocused| `boolean`| Whether the screen is focused.  
loaded| `boolean`| Whether the screen has been loaded.  
### `TabTriggerOptions`
Android
iOS
tvOS
Web
Property| Type| Description  
---|---|---  
href|   
name| `string`  
### `Trigger`
Android
iOS
tvOS
Web
Type: extended by:
Property| Type| Description  
---|---|---  
isFocused| `boolean`  
resolvedHref| `string`  
route| `[number]`  
### `UseTabsOptions`
Android
iOS
tvOS
Web
Options to provide to the Tab Router.
Type: `Omit[](https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys)<DefaultNavigatorOptions[](https://reactnavigation.org/docs/custom-navigators/#type-checking-navigators)<ParamListBase, any, TabNavigationState[](https://reactnavigation.org/docs/custom-navigators/#type-checking-navigators)<any>, ExpoTabsScreenOptions[](https://docs.expo.dev/versions/latest/sdk/router-ui/#expotabsscreenoptions), TabNavigationEventMap[](https://docs.expo.dev/versions/latest/sdk/router-ui/#tabnavigationeventmap), any>, 'children'>` extended by:
Property| Type| Description  
---|---|---  
backBehavior(optional)| `TabRouterOptions[backBehavior]`  
### `UseTabsWithChildrenOptions`
Android
iOS
tvOS
Web
Type: `PropsWithChildren<>`
### `UseTabsWithTriggersOptions`
Android
iOS
tvOS
Web
Type: `UseTabsOptions[](https://docs.expo.dev/versions/latest/sdk/router-ui/#usetabsoptions)` extended by:
Property| Type| Description  
---|---|---  
triggers| `ScreenTrigger[][](https://docs.expo.dev/versions/latest/sdk/router-ui/#screentrigger)`  
### `UseTabTriggerResult`
Android
iOS
tvOS
Web
Property| Type| Description  
---|---|---  
getTrigger| `(name: string) => undefined`  
switchTab| `(name: string, options: SwitchToOptions[](https://docs.expo.dev/versions/latest/sdk/router-ui/#switchtooptions)) => void`  
trigger(optional)|   
triggerProps| 

