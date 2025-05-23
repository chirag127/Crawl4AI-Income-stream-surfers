---
url: https://docs.expo.dev/versions/latest/sdk/fingerprint
title: https://docs.expo.dev/versions/latest/sdk/fingerprint
date: 2025-04-30T17:16:17.704930
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo Fingerprint
A library to generate a fingerprint from a React Native project.
Node
`@expo/fingerprint` provides an API to generate a fingerprint (hash) of your project for use in determining compatibility between the native layer and JavaScript layer of your app. The hash calculation is configurable, but is by default derived from hashing app dependencies, custom native code, native project files, and configuration.
## Installation
`@expo/fingerprint` is included with [`expo`](https://docs.expo.dev/versions/latest/sdk/expo) and [`expo-updates`](https://docs.expo.dev/versions/latest/sdk/updates) by default.
If you wish to use `@expo/fingerprint` as a standalone package, you can install it by running the command:
Terminal
Copy
`- ``npx expo install @expo/fingerprint`
## CLI Usage
Terminal
Copy
`- ``npx @expo/fingerprint --help`
## Configuration
`@expo/fingerprint` provides defaults that should work for most projects, but also provides a few ways to configure the fingerprinting process to better fit your app structure and workflow.
### .fingerprintignore
Placed in your project root, .fingerprintignore is a [.gitignore](https://git-scm.com/docs/gitignore#_pattern_format)-like ignore mechanism used to exclude files from hash calculation. It behaves similarly but instead uses `minimatch` for pattern matching which has some [limitations](https://docs.expo.dev/versions/latest/sdk/fingerprint#options) (see documentation for `ignorePaths` under [Options](https://docs.expo.dev/versions/latest/sdk/fingerprint#options)).
For example, to skip a folder but keep some files:
```
# Ignore the entire /app/ios folder
/app/ios/**/*
# But still keep /app/ios/Podfile and /app/ios/Podfile.lock
!/app/ios/Podfile
!/app/ios/Podfile.lock

```

### fingerprint.config.js
Placed in your project root, fingerprint.config.js allows you to specify custom hash calculation configuration beyond what is configurable in the .fingerprintignore. For supported configurations, see [Config](https://docs.expo.dev/versions/latest/sdk/fingerprint#config) and [`SourceSkips`](https://docs.expo.dev/versions/latest/sdk/fingerprint#sourceskips).
Below is an example fingerprint.config.js configuration, assuming you have `@expo/fingerprint` installed as a direct dependency:
```
/** @type {import('@expo/fingerprint').Config} */
const config = {
 sourceSkips: [
  'ExpoConfigRuntimeVersionIfString',
  'ExpoConfigVersions',
  'PackageJsonAndroidAndIosScriptsIfNotContainRun',
 ],
};
module.exports = config;

```

If you are using `@expo/fingerprint` through `expo` (where `@expo/fingerprint` is installed as a transitive dependency), you can import fingerprint from `expo/fingerprint`:
```
/** @type {import('expo/fingerprint').Config} */

```

## Limitations
Limited support for `@expo/config-plugins` raw functions
When using config plugins with raw functions, it's essential to be aware of certain limitations, particularly in the context of fingerprinting. The library makes a best effort to generate fingerprints for changes made through config plugins; however, raw functions pose specific challenges. Raw functions are not serializable as fingerprints, which means they cannot be directly used for generating unique hashes.
To work around this limitation, the library employs one of the following strategies to create serializable fingerprints for raw functions:
  1. Using `Function.name`: The library utilizes the `Function.name` property if available for named raw functions. This property provides a recognizable name for the function, which can be used as a fingerprint property.
  2. Using `withAnonymous`: For anonymous raw functions without a `Function.name`, the library resorts to using `withAnonymous` as the fingerprint property. This is a generic identifier for anonymous functions.


Here's an example to illustrate a case in which the library will use [`withMyPlugin`, `withAnonymous`] as plugin properties for fingerprint hashing:
app.config.js
Copy
```
const { withInfoPlist } = require('expo/config-plugins');
const withMyPlugin = (config) => {
 return withInfoPlist(config, (config) => {
  config.modResults.NSLocationWhenInUseUsageDescription = 'Allow $(PRODUCT_NAME) to use your location';
  return config;
 });
};
export default ({ config }) => {
 config.plugins ||= [];
 config.plugins.push(withMyPlugin);
 config.plugins.push((config) => config);
 return config;
};

```

It's important to note that due to this design, if you make changes to the implementation of raw config plugins functions, such as altering the Info.plist value within `withMyPlugin`, the fingerprint will still generate the same hash value. To ensure unique fingerprints when modifying config plugins implementations, consider the following options:
  * Avoid Anonymous Functions: Avoid using anonymous raw config plugins functions. Instead, use named functions whenever possible, and ensure that their names remain consistent as long as the implementation changes.
  * Use Local config plugins: Alternatively, you can create local config plugins as separate modules, each with its own export. This approach allows you to specify a different function name when making changes to the config plugins implementations.


Here's an example of using a local config plugin:
./plugins/withMyPlugin.js
Copy
```
const { withInfoPlist } = require('expo/config-plugins');
const withMyPlugin = config => {
 return withInfoPlist(config, config => {
  config.modResults.NSLocationWhenInUseUsageDescription =
   'Allow $(PRODUCT_NAME) to use your location';
  return config;
 });
};
module.exports = withMyPlugin;

```

app.json
Copy
```
{
 "expo": {
  %%placeholder-start%%... %%placeholder-end%%
  "plugins": "./plugins/withMyPlugin"
 }
}

```

By following these guidelines, you can effectively manage changes to config plugins and ensure that fingerprinting remains consistent and reliable.
## API
```
import * as Fingerprint from '@expo/fingerprint';

```

## Constants
### `Fingerprint.DEFAULT_IGNORE_PATHS`
Node
Type: `string[]`
### `Fingerprint.DEFAULT_SOURCE_SKIPS`
Node
Type: `PackageJsonAndroidAndIosScriptsIfNotContainRun[](https://docs.expo.dev/versions/latest/sdk/fingerprint/#packagejsonandroidandiosscriptsifnotcontainrun)`
## Methods
### `Fingerprint.createFingerprintAsync(projectRoot, options)`
Node
Parameter| Type  
---|---  
projectRoot| `string`  
options(optional)| `Options`  
Create a fingerprint for a project.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
Example
```
const fingerprint = await createFingerprintAsync('/app');
console.log(fingerprint);

```

### `Fingerprint.createProjectHashAsync(projectRoot, options)`
Node
Parameter| Type  
---|---  
projectRoot| `string`  
options(optional)| `Options`  
Create a native hash value for a project.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<string>`
Example
```
const hash = await createProjectHashAsync('/app');
console.log(hash);

```

### `Fingerprint.diffFingerprintChangesAsync(fingerprint, projectRoot, options)`
Node
Parameter| Type  
---|---  
fingerprint|   
projectRoot| `string`  
options(optional)| `Options`  
Diff the fingerprint with the fingerprint of the provided project.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<FingerprintDiffItem[][](https://docs.expo.dev/versions/latest/sdk/fingerprint/#fingerprintdiffitem)>`
Example
```
// Create a fingerprint for the project
const fingerprint = await createFingerprintAsync('/app');
// Make some changes to the project
// Calculate the diff
const diff = await diffFingerprintChangesAsync(fingerprint, '/app');
console.log(diff);

```

### `Fingerprint.diffFingerprints(fingerprint1, fingerprint2)`
Node
Parameter| Type  
---|---  
fingerprint1|   
fingerprint2|   
Diff two fingerprints. The implementation assumes that the sources are sorted.
Returns:
`FingerprintDiffItem[][](https://docs.expo.dev/versions/latest/sdk/fingerprint/#fingerprintdiffitem)`
Example
```
// Create a fingerprint for the project
const fingerprint = await createFingerprintAsync('/app');
// Make some changes to the project
// Create a fingerprint again
const fingerprint2 = await createFingerprintAsync('/app');
const diff = await diffFingerprints(fingerprint, fingerprint2);
console.log(diff);

```

## Interfaces
### `DebugInfoContents`
Node
Property| Type| Description  
---|---|---  
hash| `string`  
isTransformed(optional)| `boolean`| Indicates whether the source is transformed by `fileHookTransform`.  
### `DebugInfoDir`
Node
Property| Type| Description  
---|---|---  
children| `(undefined | )[]`  
hash| `string`  
path| `string`  
### `DebugInfoFile`
Node
Property| Type| Description  
---|---|---  
hash| `string`  
isTransformed(optional)| `boolean`| Indicates whether the source is transformed by `fileHookTransform`.  
path| `string`  
### `Fingerprint`
Node
Property| Type| Description  
---|---|---  
hash| `string`| The final hash value of the whole project fingerprint.  
sources| `FingerprintSource[][](https://docs.expo.dev/versions/latest/sdk/fingerprint/#fingerprintsource)`| Sources and their hash values from which the project fingerprint was generated.  
### `HashResultContents`
Node
Property| Type| Description  
---|---|---  
debugInfo(optional)| `DebugInfoContents[](https://docs.expo.dev/versions/latest/sdk/fingerprint/#debuginfocontents)`  
hex| `string`  
id| `string`  
type| `'contents'`  
### `HashResultDir`
Node
Property| Type| Description  
---|---|---  
debugInfo(optional)|   
hex| `string`  
id| `string`  
type| `'dir'`  
### `HashResultFile`
Node
Property| Type| Description  
---|---|---  
debugInfo(optional)| `DebugInfoFile[](https://docs.expo.dev/versions/latest/sdk/fingerprint/#debuginfofile)`  
hex| `string`  
id| `string`  
type| `'file'`  
### `HashSourceContents`
Node
Property| Type| Description  
---|---|---  
contents| `string | `  
id| `string`  
reasons| `string[]`| Reasons of this source coming from.  
type| `'contents'`  
### `HashSourceDir`
Node
Property| Type| Description  
---|---|---  
filePath| `string`  
reasons| `string[]`| Reasons of this source coming from.  
type| `'dir'`  
### `HashSourceFile`
Node
Property| Type| Description  
---|---|---  
filePath| `string`  
reasons| `string[]`| Reasons of this source coming from.  
type| `'file'`  
### `Options`
Node
Property| Type| Description  
---|---|---  
concurrentIoLimit(optional)| `number`| I/O concurrency limit.Default:`The number of CPU cores.`  
debug(optional)| `boolean`| Whether to include verbose debug info in source output. Useful for debugging.  
dirExcludes(optional)| `string[]`| 
> Deprecated Use `ignorePaths` instead.
Exclude specified directories from hashing. The supported pattern is the same as `glob()`. Default is `['android/build', 'android/app/build', 'android/app/.cxx', 'ios/Pods']`.  
enableReactImportsPatcher(optional)| `boolean`| Enable ReactImportsPatcher to transform imports from React of the form `#import "RCTBridge.h"` to `#import <React/RCTBridge.h>`. This is useful when you want to have a stable fingerprint for Expo projects, since expo-modules-autolinking will change the import style on iOS.Default:`true for Expo SDK 51 and lower.`  
extraSources(optional)| `HashSource[][](https://docs.expo.dev/versions/latest/sdk/fingerprint/#hashsource)`| Additional sources for hashing.  
fileHookTransform(optional)| `FileHookTransformFunction[](https://docs.expo.dev/versions/latest/sdk/fingerprint/#filehooktransformfunction)`| A custom hook function to transform file content sources before hashing.  
hashAlgorithm(optional)| `string`| The algorithm to use for `crypto.createHash()`.Default:`'sha1'`  
ignorePaths(optional)| `string[]`| Ignore files and directories from hashing. The supported pattern is the same as `glob()`. Please note that the pattern matching is slightly different from gitignore. Partial matching is unsupported. For example, `build` does not match `android/build`; instead, use `'**' + '/build'`.
> See: [minimatch implementations](https://github.com/isaacs/minimatch#comparisons-to-other-fnmatchglob-implementations) for further reference. Fingerprint comes with implicit default ignorePaths defined in `Options.DEFAULT_IGNORE_PATHS`. If you want to override the default ignorePaths, use `!` prefix in `ignorePaths`.  
platforms(optional)| | Limit native files to those for specified platforms.Default:`['android', 'ios']`  
silent(optional)| `boolean`| Whether running the functions should mute all console output. This is useful when fingerprinting is being done as part of a CLI that outputs a fingerprint and outputting anything else pollutes the results.  
sourceSkips(optional)| | Skips some sources from fingerprint. Value is the result of bitwise-OR'ing desired values of SourceSkips.Default:`DEFAULT_SOURCE_SKIPS`  
useRNCoreAutolinkingFromExpo(optional)| `boolean`| Use the react-native core autolinking sources from `expo-modules-autolinking` rather than `@react-native-community/cli`.Default:`true for Expo SDK 52 and higher.`  
## Types
### `Config`
Node
Supported options for use in fingerprint.config.js
Type: `Pick[](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)<Options, 'concurrentIoLimit' | 'hashAlgorithm' | 'ignorePaths' | 'extraSources' | 'enableReactImportsPatcher' | 'useRNCoreAutolinkingFromExpo' | 'debug' | 'fileHookTransform'>` extended by:
Property| Type| Description  
---|---|---  
sourceSkips(optional)| `SourceSkipsKeys[][](https://docs.expo.dev/versions/latest/sdk/fingerprint/#sourceskipskeys)`  
### `DebugInfo`
Node
Literal Type: `union`
Acceptable values are: `DebugInfoFile[](https://docs.expo.dev/versions/latest/sdk/fingerprint/#debuginfofile)` |  | `DebugInfoContents[](https://docs.expo.dev/versions/latest/sdk/fingerprint/#debuginfocontents)`
### `FileHookTransformFunction(source, chunk, isEndOfFile, encoding)`
Node
Hook function to transform file content sources before hashing.
Parameter| Type  
---|---  
source| `FileHookTransformSource[](https://docs.expo.dev/versions/latest/sdk/fingerprint/#filehooktransformsource)`  
chunk| `string | null`  
isEndOfFile| `boolean`  
encoding| `BufferEncoding[](https://docs.expo.dev/versions/latest/sdk/fingerprint/#bufferencoding)`  
Returns:
`string | null`
### `FileHookTransformSource`
Node
The `source` parameter for `FileHookTransformFunction`.
Type: `object` shaped as below:
Property| Type| Description  
---|---|---  
filePath| `string`  
type| `'file'`  
Or object shaped as below:
Property| Type| Description  
---|---|---  
id| `string`  
type| `'contents'`  
### `FingerprintDiffItem`
Node
Type: `object` shaped as below:
Property| Type| Description  
---|---|---  
addedSource| `FingerprintSource[](https://docs.expo.dev/versions/latest/sdk/fingerprint/#fingerprintsource)`| The added source.  
op| `'added'`| The operation type of the diff item.  
Or object shaped as below:
Property| Type| Description  
---|---|---  
op| `'removed'`| The operation type of the diff item.  
removedSource| `FingerprintSource[](https://docs.expo.dev/versions/latest/sdk/fingerprint/#fingerprintsource)`| The removed source.  
Or object shaped as below:
Property| Type| Description  
---|---|---  
afterSource| `FingerprintSource[](https://docs.expo.dev/versions/latest/sdk/fingerprint/#fingerprintsource)`| The source after.  
beforeSource| `FingerprintSource[](https://docs.expo.dev/versions/latest/sdk/fingerprint/#fingerprintsource)`| The source before.  
op| `'changed'`| The operation type of the diff item.  
### `FingerprintSource`
Node
Type: extended by:
Property| Type| Description  
---|---|---  
debugInfo(optional)| | Debug info from the hashing process. Differs based on source type. Designed to be consumed by humans as opposed to programmatically.  
hash| `string | null`| Hash value of the `source`. If the source is excluded the value will be null.  
### `HashResult`
Node
Literal Type: `union`
Acceptable values are: `HashResultFile[](https://docs.expo.dev/versions/latest/sdk/fingerprint/#hashresultfile)` | `HashResultDir[](https://docs.expo.dev/versions/latest/sdk/fingerprint/#hashresultdir)` | `HashResultContents[](https://docs.expo.dev/versions/latest/sdk/fingerprint/#hashresultcontents)`
### `HashSource`
Node
Literal Type: `union`
Acceptable values are: `HashSourceFile[](https://docs.expo.dev/versions/latest/sdk/fingerprint/#hashsourcefile)` | `HashSourceDir[](https://docs.expo.dev/versions/latest/sdk/fingerprint/#hashsourcedir)` | `HashSourceContents[](https://docs.expo.dev/versions/latest/sdk/fingerprint/#hashsourcecontents)`
### `Platform`
Node
Literal Type: `string`
Acceptable values are: `'android'` | `'ios'`
## Enums
### `SourceSkips`
Node
Bitmask of values that can be used to skip certain parts of the sourcers when generating a fingerprint.
#### `None`
`SourceSkips.None ＝ 0`
Skip nothing
#### `ExpoConfigVersions`
`SourceSkips.ExpoConfigVersions ＝ 1`
Versions in app.json, including Android versionCode and iOS buildNumber
#### `ExpoConfigRuntimeVersionIfString`
`SourceSkips.ExpoConfigRuntimeVersionIfString ＝ 2`
runtimeVersion in app.json if it is a string
#### `ExpoConfigNames`
`SourceSkips.ExpoConfigNames ＝ 4`
App names in app.json, including shortName and description
#### `ExpoConfigAndroidPackage`
`SourceSkips.ExpoConfigAndroidPackage ＝ 8`
Android package name in app.json
#### `ExpoConfigIosBundleIdentifier`
`SourceSkips.ExpoConfigIosBundleIdentifier ＝ 16`
iOS bundle identifier in app.json
#### `ExpoConfigSchemes`
`SourceSkips.ExpoConfigSchemes ＝ 32`
Schemes in app.json
#### `ExpoConfigEASProject`
`SourceSkips.ExpoConfigEASProject ＝ 64`
EAS project information in app.json
#### `ExpoConfigAssets`
`SourceSkips.ExpoConfigAssets ＝ 128`
Assets in app.json, including icons and splash assets
#### `ExpoConfigAll`
`SourceSkips.ExpoConfigAll ＝ 256`
Skip the whole ExpoConfig. Prefer the other ExpoConfig source skips when possible and use this flag with caution. This will potentially ignore some native changes that should be part of most fingerprints. E.g., adding a new config plugin, changing the app icon, or changing the app name.
#### `PackageJsonAndroidAndIosScriptsIfNotContainRun`
`SourceSkips.PackageJsonAndroidAndIosScriptsIfNotContainRun ＝ 512`
package.json scripts if android and ios items do not contain "run". Because prebuild will change the scripts in package.json, this is useful to generate a consistent fingerprint before and after prebuild.
#### `PackageJsonScriptsAll`
`SourceSkips.PackageJsonScriptsAll ＝ 1024`
Skip the whole `scripts` section in the project's package.json.
#### `GitIgnore`
`SourceSkips.GitIgnore ＝ 2048`
Skip .gitignore files.

