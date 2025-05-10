---
url: https://docs.expo.dev/guides/local-app-production
title: https://docs.expo.dev/guides/local-app-production
date: 2025-04-30T17:14:04.143408
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Create a production build locally
Learn how to create a production build for your Expo app locally.
To create your app's production build (also known as release build) locally, you need to follow separate steps on your computer and use the tools required to create any native app. This guide provides the necessary steps for Android and iOS.
## Android
Creating a production build locally for Android requires signing it with an [upload key](https://developer.android.com/studio/publish/app-signing#certificates-keystores) and generating an Android Application Bundle (.aab). Follow the steps below:
### Prerequisites
  * [OpenJDK distribution](https://docs.expo.dev/get-started/set-up-your-environment?mode=development-build&buildEnv=local#install-watchman-and-jdk) installed to access the `keytool` command
  * android directory generated. If you are using [CNG](https://docs.expo.dev/workflow/continuous-native-generation), then run `npx expo prebuild` to generate it.


1
### Create an upload key
Already created a build with EAS Build? Download your credentials and skip to the next step.
If you've already created a build with EAS Build, follow the steps below to download the credentials, which contains the upload key and its password, key alias, and key password:
  1. In your terminal, run `eas credentials -p android` and select the build profile.
  2. Select credentials.json > Download credentials from EAS to credentials.json.
  3. Move the downloaded keystore.jks file to the android/app directory.
  4. Copy the values for the upload keystore password, key alias, and key password from the credentials.json as you will need them in the next step.


Inside your Expo project directory, run the following `keytool` command to create an upload key:
Terminal
Copy
`- ``sudo keytool -genkey -v -keystore my-upload-key.keystore -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000`
After running this command, you will be prompted to enter a password for the keystore. This password will protect the upload key. Remember the password you enter here, as you'll need it in the next step.
This command also generates the keystore file named my-upload-key.keystore in your project directory. Move it to the android/app directory.
> If you commit the android directory to a version control system like Git, don't commit this keystore file. It contains your upload key and should be kept private.
2
### Update gradle variables
Open android/gradle.properties file and add the following gradle variables at the end of the file. Replace the `*****` with the correct keystore and key password that you provided in the previous step.
These variables contain information about your upload key:
android/gradle.properties
Copy
```
# If you've downloaded the credentials from `eas credentials` command, see comments below for each value.
MYAPP_UPLOAD_STORE_FILE=my-upload-key.keystore   # Path to the "keystore.jks" file
MYAPP_UPLOAD_KEY_ALIAS=my-key-alias        # Replace with value of the `keystore.keyAlias` field in the credentials.json file
MYAPP_UPLOAD_STORE_PASSWORD=*****         # Replace with value of the `keystore.password` field in the credentials.json file
MYAPP_UPLOAD_KEY_PASSWORD=*****          # Replace with value of the `keystore.keyPassword` field in the credentials.json file

```

> If you commit the android directory to a version control system like Git, don't commit the above information. Instead, create a ~/.gradle/gradle.properties file on your computer and add the above variables to this file.
3
### Add signing config to build.gradle
Open android/app/build.gradle file and add the following configuration:
android/app/build.gradle
101| 101|  keyAlias 'androiddebugkey'  
---|---|---  
102| 102|  keyPassword 'android'  
103| 103|  }  
104|  release {  
105|  if (project.hasProperty('MYAPP_UPLOAD_STORE_FILE')) {  
106|  storeFile file(MYAPP_UPLOAD_STORE_FILE)  
107|  storePassword MYAPP_UPLOAD_STORE_PASSWORD  
108|  keyAlias MYAPP_UPLOAD_KEY_ALIAS  
109|  keyPassword MYAPP_UPLOAD_KEY_PASSWORD  
110|  }  
111|  }  
104| 112|  }  
105| 113|  buildTypes {  
106| 114|  debug {  
110| 118|  // Caution! In production, you need to generate your own keystore file.  
111| 119|  // see https://reactnative.dev/docs/signed-apk-android.  
112| 120|  signingConfig signingConfigs.debug  
121|  signingConfig signingConfigs.release  
113| 122|  shrinkResources (findProperty('android.enableShrinkResourcesInReleaseBuilds')?.toBoolean() ?: false)  
114| 123|  minifyEnabled enableProguardInReleaseBuilds  
115| 124|  proguardFiles getDefaultProguardFile("proguard-android.txt"), "proguard-rules.pro"  
4
### Generate release Android Application Bundle (aab)
Navigate inside the android directory and create a production build in .aab format by running Gradle's `bundleRelease` command:
Terminal
Copy
`- ``cd android`
`- ``./gradlew app:bundleRelease`
This command will generate app-release.aab inside the android/app/build/outputs/bundle/release directory.
5
### Manual app submission to Google Play Console
Google Play Store requires manual app submission when submitting the .aab file for the first time.
[Manual submission of an Android appFollow the steps from the FYI guide on manually submitting your app to Google Play Store for the first time.](https://expo.fyi/first-android-submission)
## iOS
To create an iOS production build locally for Apple App Store, you need to use Xcode which handles the signing and submission process via App Store Connect.
### Prerequisites
  * Paid Apple Developer membership
  * [Xcode installed](https://docs.expo.dev/get-started/set-up-your-environment?platform=ios&device=physical&mode=development-build&buildEnv=local#set-up-xcode-and-watchman) on your computer
  * ios directory generated. If you are using [CNG](https://docs.expo.dev/workflow/continuous-native-generation), then run `npx expo prebuild` to generate it.


1
### Open iOS workspace in Xcode
Inside your Expo project directory, run the following command to open `your-project.xcworkspace` in Xcode:
Terminal
Copy
`- ``xed ios`
After opening the iOS project in Xcode:
  1. From the sidebar on the left, select your app's workspace.
  2. Go to Signing & Capabilities and select All or Release.
  3. Under Signing > Team, ensure your Apple Developer team is selected. Xcode will generate an automatically managed Provisioning Profile and Signing Certificate.


2
### Configure a release scheme
To configure your app's release scheme:
  1. From the menu bar, open Product > Scheme > Edit Scheme.
  2. Select Run from the sidebar, then set the Build configuration to Release using the dropdown.


3
### Build app for release
To build your app for release, From the menu bar, open Product > Build. This step will build your app binary for release.
4
### App submission using App Store Connect
Once the build is complete, you can distribute your app to TestFlight or submit it to the App Store using App Store Connect:
  1. From the menu bar, open Product > Archive.
  2. Under Archives, click Distribute App from the right sidebar.
  3. Click App Store Connect and follow the prompts shown in the window. This step will create an app store record and upload your app to the App Store.
  4. Now you can go to your App Store Connect account, select your app under Apps, and submit it for testing using TestFlight or prepare it for final release by following the steps in the App Store Connect dashboard.



