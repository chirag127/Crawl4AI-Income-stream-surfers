---
url: https://docs.expo.dev/versions/latest/config/package-json
title: https://docs.expo.dev/versions/latest/config/package-json
date: 2025-04-30T17:15:18.455191
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# package.json
A reference for Expo-specific properties that can be used in the package.json file.
package.json is a JSON file that contains the metadata for a JavaScript project. This is a reference to Expo-specific properties that can be used in the package.json file.
## `install.exclude`
The following commands perform a version check for the libraries installed in a project and give a warning when a library's version is different from the version recommended by Expo:
  * `npx expo start` and `npx expo-doctor`
  * `npx expo install` (when installing a new version of that library or using `--check` or `--fix` options)


By specifying the library under the `install.exclude` array in the package.json file, you can exclude it from the version checks:
package.json
Copy
```
{
 "expo": {
  "install": {
   "exclude": ["expo-updates", "expo-splash-screen"]
  }
 }
}

```

## `autolinking`
Allows configuring module resolution behavior by using `autolinking` property in package.json.
For complete reference, see [Autolinking configuration](https://docs.expo.dev/modules/autolinking#configuration).
## `doctor`
Allows configuring the behavior of the [`npx expo-doctor`](https://docs.expo.dev/develop/tools#expo-doctor) command.
### `reactNativeDirectoryCheck`
By default, Expo Doctor validates your project's packages against the [React Native directory](https://reactnative.directory/). This check throws a warning with a list of packages that are not included in the React Native Directory.
You can customize this check by adding the following configuration in your project's package.json file:
package.json
Copy
```
{
 "expo": {
  "doctor": {
   "reactNativeDirectoryCheck": {
    "enabled": true,
    "exclude": ["/foo/", "bar"],
    "listUnknownPackages": true
   }
  }
 }
}

```

By default, the check is enabled and unknown packages are listed.
### `appConfigFieldsNotSyncedCheck`
Expo Doctor checks if your project includes native project directories such as android or ios. If these directories exist but are not listed in your .gitignore or [.easignore](https://docs.expo.dev/build-reference/easignore) files, Expo Doctor verifies the presence of an app config file. If this file exists, it means your project is configured to use [Prebuild](https://docs.expo.dev/workflow/prebuild).
When the android or ios directories are present, EAS Build does not sync app config properties to the native projects. Expo Doctor throws a warning if these conditions are true.
You can disable or enable this check by adding the following configuration to your project's package.json file:
package.json
Copy
```
{
 "expo": {
  "doctor": {
   "appConfigFieldsNotSyncedCheck": {
    "enabled": false
   }
  }
 }
}

```


