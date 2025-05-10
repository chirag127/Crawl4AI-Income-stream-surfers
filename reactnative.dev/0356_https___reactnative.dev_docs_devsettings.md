---
url: https://reactnative.dev/docs/devsettings
title: https://reactnative.dev/docs/devsettings
date: 2025-05-10T21:39:59.434619
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/devsettings#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
The `DevSettings` module exposes methods for customizing settings for developers in development.
# Reference
## Methods[​](https://reactnative.dev/docs/devsettings#methods "Direct link to Methods")
### `addMenuItem()`[​](https://reactnative.dev/docs/devsettings#addmenuitem "Direct link to addmenuitem")
tsx
```
staticaddMenuItem(title:string,handler:()=>any);
```

Add a custom menu item to the Dev Menu.
**Parameters:**
Name| Type  
---|---  
title Required| string  
handler Required| function  
**Example:**
tsx
```
DevSettings.addMenuItem('Show Secret Dev Screen',()=>{Alert.alert('Showing secret dev screen!');});
```

### `reload()`[​](https://reactnative.dev/docs/devsettings#reload "Direct link to reload")
tsx
```
staticreload(reason?:string):void;
```

Reload the application. Can be invoked directly or on user interaction.
**Example:**
tsx
```
<Buttontitle="Reload"onPress={()=>DevSettings.reload()}/>
```

Is this page useful?
  * [Methods](https://reactnative.dev/docs/devsettings#methods)



