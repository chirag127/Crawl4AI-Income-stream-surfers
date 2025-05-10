---
url: https://docs.expo.dev/build/automate-submissions
title: https://docs.expo.dev/build/automate-submissions
date: 2025-04-30T17:12:45.576946
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Automate submissions
Learn how to enable automatic submissions with EAS Build.
Many mobile deployment processes eventually evolve to the point where the app is automatically submitted to the respective store once an appropriate build is completed. This saves developers from having to wait around for the build to complete, avoids a bit of manual work, and eliminates the need to coordinate providing app store credentials to the team.
EAS Build gives you automatic submissions out of the box with the `--auto-submit` flag. This flag tells EAS Build to pass the build along to EAS Submit with the appropriate submission profile upon completion. Refer to the [EAS Submit documentation](https://docs.expo.dev/submit/introduction) for more information on how to set up and configure submissions.
When you run `eas build --auto-submit` you will be provided with a link to a submission details page, where you can track the progress of the submission. You can also find this page at any time on the [submissions dashboard for your project](https://expo.dev/accounts/%5Baccount%5D/projects/%5Bproject%5D/submissions), and it is linked from your build details page.
### Selecting a submission profile
By default, `--auto-submit` will try to use a submission profile with the same name as the selected build profile. If this does not exist, or if you prefer to use a different profile, you can use `--auto-submit-with-profile=<profile-name>` instead.
### Build profile environment variables and submissions
When running `eas build --profile <profile-name> --auto-submit`, the project's app.config.js will be evaluated using any environment variables associated with the build profile `<profile-name>`. For example, suppose we ran `eas build -p ios --profile production --auto-submit` with the following configuration:
eas.json
Copy
```
{
 "build": {
  "production": {
   "env": {
    "APP_ENV": "production"
   }
  },
  "development": {
   "env": {
    "APP_ENV": "development"
   }
  }
 }
}

```

app.config.js
Copy
```
export default () => {
 return {
  name: process.env.APP_ENV === 'production' ? 'My App' : 'My App (DEV)',
  ios: {
   bundleIdentifier: process.env.APP_ENV === 'production' ? 'com.my.app' : 'com.my.app-dev',
  },
  // ... other config here
 };
};

```

The `APP_ENV` variable from the `production` profile will be used when evaluating app.config.js for the submission, and therefore the name will be `My App` and the bundle identifier will be `com.my.app`.

