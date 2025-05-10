---
url: https://docs.expo.dev/versions/latest/sdk/build-properties
title: https://docs.expo.dev/versions/latest/sdk/build-properties
date: 2025-04-30T17:15:47.467135
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo BuildProperties
A config plugin that allows customizing native build properties during prebuild.
Android
iOS
tvOS
Bundled version:
~0.13.2
`expo-build-properties` is a [config plugin](https://docs.expo.dev/config-plugins/introduction) configuring the native build properties of your android/gradle.properties and ios/Podfile.properties.json directories during [Prebuild](https://docs.expo.dev/workflow/prebuild).
> This config plugin configures how [Prebuild command](https://docs.expo.dev/workflow/prebuild) generates the native android and ios directories and therefore cannot be used with projects that don't run `npx expo prebuild` (bare projects).
## Installation
Terminal
Copy
`- ``npx expo install expo-build-properties`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Usage
### Example app.json with config plugin
app.json
app.config.js
app.json
Copy
```
{
 "expo": {
  "plugins": [
   [
    "expo-build-properties",
    {
     "android": {
      "compileSdkVersion": 35,
      "targetSdkVersion": 35,
      "buildToolsVersion": "35.0.0"
     },
     "ios": {
      "deploymentTarget": "15.1"
     }
    }
   ]
  ]
 }
}

```

app.config.js
Copy
```
export default {
 expo: {
  plugins: [
   [
    'expo-build-properties',
    {
     android: {
      compileSdkVersion: 35,
      targetSdkVersion: 35,
      buildToolsVersion: '35.0.0',
     },
     ios: {
      deploymentTarget: '15.1',
     },
    },
   ],
  ],
 },
};

```

### All configurable properties
[`PluginConfigType`](https://docs.expo.dev/versions/latest/sdk/build-properties#pluginconfigtype) interface represents currently available configuration properties.
## API
## Methods
### `BuildProperties.withBuildProperties(config, props)`
Android
iOS
tvOS
Parameter| Type| Description  
---|---|---  
config| | Expo config for application.  
props| `PluginConfigType[](https://docs.expo.dev/versions/latest/sdk/build-properties/#pluginconfigtype)`| Configuration for the build properties plugin.  
Config plugin allowing customizing native Android and iOS build properties for managed apps.
Returns:
## Interfaces
### `AndroidMavenRepository`
Android
Property| Type| Description  
---|---|---  
authentication(optional)| `'basic' | 'digest' | 'header'`| The authentication scheme to use when accessing the Maven repository.  
credentials(optional)| `AndroidMavenRepositoryCredentials[](https://docs.expo.dev/versions/latest/sdk/build-properties/#androidmavenrepositorycredentials)`| The credentials to use when accessing the Maven repository. May be of type PasswordCredentials, HttpHeaderCredentials, or AWSCredentials.
> See: The authentication schemes section of [Gradle documentation](https://docs.gradle.org/current/userguide/declaring_repositories.html#sec:authentication_schemes) for more information.  
url| `string`| The URL of the Maven repository.  
### `AndroidMavenRepositoryAWSCredentials`
Android
Property| Type| Description  
---|---|---  
accessKey| `string`  
secretKey| `string`  
sessionToken(optional)| `string`  
### `AndroidMavenRepositoryHttpHeaderCredentials`
Android
Property| Type| Description  
---|---|---  
name| `string`  
value| `string`  
### `AndroidMavenRepositoryPasswordCredentials`
Android
Property| Type| Description  
---|---|---  
password| `string`  
username| `string`  
### `ExtraIosPodDependency`
iOS
Interface representing extra CocoaPods dependency.
> See: [Podfile syntax reference](https://guides.cocoapods.org/syntax/podfile.html#pod)
Property| Type| Description  
---|---|---  
branch(optional)| `string`| The git branch to fetch. See the `git` property for more information.  
commit(optional)| `string`| The git commit to fetch. See the `git` property for more information.  
configurations(optional)| `string[]`| Build configurations for which the pod should be installed.Example`['Debug', 'Release'] `  
git(optional)| `string`| Use the bleeding edge version of a Pod.Example```
{
 "name": "AFNetworking",
 "git": "https://github.com/gowalla/AFNetworking.git",
 "tag": "0.7.0"
}

```
This acts like to add this pod dependency statement: ```
pod 'AFNetworking', :git => 'https://github.com/gowalla/AFNetworking.git', :tag => '0.7.0'

```
  
modular_headers(optional)| `boolean`| Whether this pod should use modular headers.  
name| `string`| Name of the pod.  
path(optional)| `string`| Custom local filesystem path to add the dependency.Example`~/Documents/AFNetworking `  
podspec(optional)| `string`| Custom podspec path.Example`https://example.com/JSONKit.podspec`  
source(optional)| `string`| Custom source to search for this dependency.Example`https://github.com/CocoaPods/Specs.git `  
tag(optional)| `string`| The git tag to fetch. See the `git` property for more information.  
testspecs(optional)| `string[]`| Test specs can be optionally included via the :testspecs option. By default, none of a Pod's test specs are included.Example`['UnitTests', 'SomeOtherTests'] `  
version(optional)| `string`| Version of the pod. CocoaPods supports various [versioning options](https://guides.cocoapods.org/using/the-podfile.html#pod).Example`~> 0.1.2 `  
### `PluginConfigType`
Android
iOS
tvOS
Interface representing base build properties configuration.
Property| Type| Description  
---|---|---  
android(optional)| `PluginConfigTypeAndroid[](https://docs.expo.dev/versions/latest/sdk/build-properties/#pluginconfigtypeandroid)`| Only for: AndroidInterface representing available configuration for Android native build properties.  
ios(optional)| `PluginConfigTypeIos[](https://docs.expo.dev/versions/latest/sdk/build-properties/#pluginconfigtypeios)`| Only for: iOSInterface representing available configuration for iOS native build properties.  
### `PluginConfigTypeAndroid`
Android
Interface representing available configuration for Android native build properties.
Property| Type| Description  
---|---|---  
buildToolsVersion(optional)| `string`| Override the default `buildToolsVersion` version number in build.gradle.  
compileSdkVersion(optional)| `number`| Override the default `compileSdkVersion` version number in build.gradle.  
enablePngCrunchInReleaseBuilds(optional)| `boolean`| Enable [`crunchPngs`](https://developer.android.com/topic/performance/reduce-apk-size#crunch) in release builds to optimize PNG files. This property is enabled by default, but "might inflate PNG files that are already compressed", so you may want to disable it if you do your own PNG optimization.Default:`true`  
enableProguardInReleaseBuilds(optional)| `boolean`| Enable [Proguard or R8](https://developer.android.com/studio/build/shrink-code) in release builds to obfuscate Java code and reduce app size.  
enableShrinkResourcesInReleaseBuilds(optional)| `boolean`| Enable [`shrinkResources`](https://developer.android.com/studio/build/shrink-code#shrink-resources) in release builds to remove unused resources from the app. This property should be used in combination with `enableProguardInReleaseBuilds`.  
extraMavenRepos(optional)| `(string | AndroidMavenRepository[](https://docs.expo.dev/versions/latest/sdk/build-properties/#androidmavenrepository))[]`| Add extra maven repositories to all gradle projects. Takes an array of objects or strings. Strings are passed as the `url` property of the object with no credentials or authentication scheme. This adds the following code to android/build.gradle: ```
allprojects {
 repositories {
 maven {
  url "https://foo.com/maven-releases"
 }
}

```
By using an `AndroidMavenRepository` object, you can specify credentials and an authentication scheme. ```
allprojects {
 repositories {
  maven {
   url "https://foo.com/maven-releases"
   credentials {
    username = "bar"
    password = "baz"
   }
   authentication {
    basic(BasicAuthentication)
   }
  }
 }
}

```

> See: [Gradle documentation](https://docs.gradle.org/current/userguide/declaring_repositories.html#sec:case-for-maven)  
extraProguardRules(optional)| `string`| Append custom [Proguard rules](https://www.guardsquare.com/manual/configuration/usage) to android/app/proguard-rules.pro.  
kotlinVersion(optional)| `string`| Override the Kotlin version used when building the app.  
manifestQueries(optional)| `PluginConfigTypeAndroidQueries[](https://docs.expo.dev/versions/latest/sdk/build-properties/#pluginconfigtypeandroidqueries)`| Specifies the set of other apps that an app intends to interact with. These other apps are specified by package name, by intent signature, or by provider authority.
> See: [Android documentation](https://developer.android.com/guide/topics/manifest/queries-element)  
minSdkVersion(optional)| `number`| Override the default `minSdkVersion` version number in build.gradle.  
networkInspector(optional)| `boolean`| Enable the Network Inspector.Default:`true`  
newArchEnabled(optional)| `boolean`| 
> Deprecated Use app config [`newArchEnabled`](https://docs.expo.dev/versions/latest/config/app/#newarchenabled) instead. Enable React Native new architecture for Android platform.  
packagingOptions(optional)| `PluginConfigTypeAndroidPackagingOptions[](https://docs.expo.dev/versions/latest/sdk/build-properties/#pluginconfigtypeandroidpackagingoptions)`| Interface representing available configuration for Android Gradle plugin [`PackagingOptions`](https://developer.android.com/reference/tools/gradle-api/7.0/com/android/build/api/dsl/PackagingOptions).  
targetSdkVersion(optional)| `number`| Override the default `targetSdkVersion` version number in build.gradle.  
useLegacyPackaging(optional)| `boolean`| Instructs the Android Gradle plugin to compress native libraries in the APK using the legacy packaging system.Default:`false`
> See: [Android documentation](https://developer.android.com/build/releases/past-releases/agp-4-2-0-release-notes#compress-native-libs-dsl)  
usesCleartextTraffic(optional)| `boolean`| Indicates whether the app intends to use cleartext network traffic.Default:`false`
> See: [Android documentation](https://developer.android.com/guide/topics/manifest/application-element#usesCleartextTraffic)  
### `PluginConfigTypeAndroidPackagingOptions`
Android
Interface representing available configuration for Android Gradle plugin [`PackagingOptions`](https://developer.android.com/reference/tools/gradle-api/7.0/com/android/build/api/dsl/PackagingOptions).
Property| Type| Description  
---|---|---  
doNotStrip(optional)| `string[]`| Array of patterns for native libraries that should not be stripped of debug symbols.  
exclude(optional)| `string[]`| Array of patterns for native libraries that should be excluded from being packaged in the APK.  
merge(optional)| `string[]`| Array of patterns for native libraries where all occurrences are concatenated and packaged in the APK.  
pickFirst(optional)| `string[]`| Array of patterns for native libraries where only the first occurrence is packaged in the APK.  
### `PluginConfigTypeAndroidQueries`
Android
Property| Type| Description  
---|---|---  
intent(optional)| `PluginConfigTypeAndroidQueriesIntent[][](https://docs.expo.dev/versions/latest/sdk/build-properties/#pluginconfigtypeandroidqueriesintent)`| Specifies an intent filter signature. Your app can discover other apps that have matching `<intent-filter>` elements. These intents have restrictions compared to typical intent filter signatures.
> See: [Android documentation](https://developer.android.com/training/package-visibility/declaring#intent-filter-signature) for details  
package(optional)| `string[]`| Specifies one or more apps that your app intends to access. These other apps might integrate with your app, or your app might use services that these other apps provide.  
provider(optional)| `string[]`| Specifies one or more content provider authorities. Your app can discover other apps whose content providers use the specified authorities. There are some restrictions on the options that you can include in this `<provider>` element, compared to a typical `<provider>` manifest element. You may only specify the `android:authorities` attribute.  
### `PluginConfigTypeAndroidQueriesData`
Android
Property| Type| Description  
---|---|---  
host(optional)| `string`| Specify a URI authority host that is handled  
mimeType(optional)| `string`| Specify a MIME type that is handled  
scheme(optional)| `string`| Specify a URI scheme that is handled  
### `PluginConfigTypeAndroidQueriesIntent`
Android
Property| Type| Description  
---|---|---  
action(optional)| `string`| A string naming the action to perform. Usually one of the platform-defined values, such as `ACTION_SEND` or `ACTION_VIEW`.  
category(optional)| `string | string[]`| Provides an additional way to characterize the activity handling the intent, usually related to the user gesture or location from which it's started.  
data(optional)| `PluginConfigTypeAndroidQueriesData[](https://docs.expo.dev/versions/latest/sdk/build-properties/#pluginconfigtypeandroidqueriesdata)`| A description of the data associated with the intent.  
### `PluginConfigTypeIos`
iOS
Interface representing available configuration for iOS native build properties.
Property| Type| Description  
---|---|---  
ccacheEnabled(optional)| `boolean`| Enable C++ compiler cache for iOS builds. This speeds up compiling C++ code by caching the results of previous compilations.
> See: [React Native's documentation on local caches](https://reactnative.dev/docs/build-speed#local-caches) and [Ccache documentation](https://ccache.dev/).  
deploymentTarget(optional)| `string`| Override the default iOS "Deployment Target" version in the following projects:
  * in CocoaPods projects,
  * `PBXNativeTarget` with "com.apple.product-type.application" `productType` in the app project.

  
extraPods(optional)| `ExtraIosPodDependency[][](https://docs.expo.dev/versions/latest/sdk/build-properties/#extraiospoddependency)`| Add extra CocoaPods dependencies for all targets. This configuration is responsible for adding the new Pod entries to ios/Podfile.ExampleCreating entry in the configuration like below: ```
[
 {
  name: "Protobuf",
  version: "~> 3.14.0",
 }
]

```
Will produce the following entry in the generated ios/Podfile: ```
pod 'Protobuf', '~> 3.14.0'

```
  
networkInspector(optional)| `boolean`| Enable the Network Inspector.Default:`true`  
newArchEnabled(optional)| `boolean`| 
> Deprecated Use app config [`newArchEnabled`](https://docs.expo.dev/versions/latest/config/app/#newarchenabled) instead. Enable React Native new architecture for iOS platform.  
privacyManifestAggregationEnabled(optional)| `boolean`| Enable aggregation of Privacy Manifests (`PrivacyInfo.xcprivacy`) from CocoaPods resource bundles. If enabled, the manifests will be merged into a single file. If not enabled, developers will need to manually aggregate them.
> See: [Privacy manifests](https://docs.expo.dev/guides/apple-privacy/) guide and [Apple's documentation on Privacy manifest files](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files).  
useFrameworks(optional)| `'static' | 'dynamic'`| Enable [`use_frameworks!`](https://guides.cocoapods.org/syntax/podfile.html#use_frameworks_bang) in `Podfile` to use frameworks instead of static libraries for Pods.  
## Types
### `AndroidMavenRepositoryCredentials`
Android
Literal Type: `union`
Acceptable values are: `AndroidMavenRepositoryPasswordCredentials[](https://docs.expo.dev/versions/latest/sdk/build-properties/#androidmavenrepositorypasswordcredentials)` | `AndroidMavenRepositoryHttpHeaderCredentials[](https://docs.expo.dev/versions/latest/sdk/build-properties/#androidmavenrepositoryhttpheadercredentials)` | `AndroidMavenRepositoryAWSCredentials[](https://docs.expo.dev/versions/latest/sdk/build-properties/#androidmavenrepositoryawscredentials)`

