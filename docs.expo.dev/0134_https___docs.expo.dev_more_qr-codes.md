---
url: https://docs.expo.dev/more/qr-codes
title: https://docs.expo.dev/more/qr-codes
date: 2025-04-30T17:14:23.276385
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# qr.expo.dev
Reference for the QR code generator at qr.expo.dev.
qr.expo.dev is a cloud function that generates Expo-branded QR codes. This function creates QR codes for [EAS Update](https://docs.expo.dev/eas-update/introduction), which are used to preview updates in [development builds](https://docs.expo.dev/develop/development-builds/introduction) and Expo Go.
For example, if you and your team have a development build, and you'd like to load the latest update on a specific build's channel, you could go to the following endpoint to generate a QR code:
```
https://qr.expo.dev/eas-update?projectId=your-project-id&runtimeVersion=your-runtime-version&channel=your-channel

```

Which would produce the following QR code SVG:
This QR code represents the following URL:
```
exp+your-slug://expo-development-client/?url=https://u.expo.dev/your-project-id?runtime-version=your-runtime-version&channel-name=your-channel

```

This URL will deep link into a development build and instruct it to fetch the latest update on the specified channel.
> If sharing the URL is more convenient, you can request the URL directly by adding `format=url` to the query parameters.
## General
The following parameters apply to the `/eas-update` endpoint.
### Base query parameters
The following base query parameters can be included with any request to `/eas-update`.
Param| Required| Default| Description  
---|---|---|---  
`slug`| No| exp| Use [`slug`](https://docs.expo.dev/versions/latest/config/app#slug) from [app config](https://docs.expo.dev/workflow/configuration) to target a development build. Otherwise use "exp" to target Expo Go.  
`appScheme` (deprecated)| No| exp| Replaced by `slug`. Use `slug` instead.  
`host`| No| u.expo.dev| The hostname of the server that handles update requests.  
`format`| No| svg| Endpoints respond with SVGs by default. To receive a plain text URL, use `url`.  
### Update by device traits
Preview and production builds make requests to the EAS Update service with `runtimeVersion` and `channel` properties. You can emulate this behavior with the following query parameters:
Param| Required| Description  
---|---|---  
`projectId`| Yes| The ID of the project  
`runtimeVersion`| Yes| The [runtime version](https://docs.expo.dev/eas-update/runtime-versions) of the build  
`channel`| Yes| The channel name of the build  
#### Example
```
https://qr.expo.dev/eas-update?projectId=your-project-id&runtimeVersion=your-runtime-version&channel=your-channel

```

### Update by ID
You can create a QR code for a specific update given its platform-specific ID.
Param| Required| Description  
---|---|---  
`updateId`| Yes| The ID of the update  
#### Example
```
https://qr.expo.dev/eas-update?updateId=your-update-id

```

### Update by group ID
You can create a QR code for an update group given the update's group ID.
Param| Required| Description  
---|---|---  
`projectId`| Yes| The ID of the project  
`groupId`| Yes| The ID of the update group  
#### Example
```
https://qr.expo.dev/eas-update?projectId=your-project-id&groupId=your-update-id

```

### Update by branch ID
You can create a QR code with a branch's ID, which will return the latest update available on that branch.
Param| Required| Description  
---|---|---  
`projectId`| Yes| The ID of the project  
`branchId`| Yes| The ID of the branch  
#### Example
```
https://qr.expo.dev/eas-update?projectId=your-project-id&branchId=your-branch-id

```

### Update by channel ID
You can create a QR code with a channel's ID, which will return the latest update available on the branch or branches that are mapped to that channel.
Param| Required| Description  
---|---|---  
`projectId`| Yes| The ID of the project  
`channelId`| Yes| The ID of the channel  
#### Example
```
https://qr.expo.dev/eas-update?projectId=your-project-id&channelId=your-channel-id

```


