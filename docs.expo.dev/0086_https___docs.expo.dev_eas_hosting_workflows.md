---
url: https://docs.expo.dev/eas/hosting/workflows
title: https://docs.expo.dev/eas/hosting/workflows
date: 2025-04-30T17:13:38.613943
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Deploy with Workflows
Learn how to automate React Native CI/CD for web deployments with EAS Hosting and Workflows.
EAS Workflows is a great way to automate the React Native CI/CD pipeline for web deployment of your project to EAS Hosting with pull request (PR) previews and production deployments.
## Setup workflows
To use [EAS workflows](https://docs.expo.dev/eas/workflows/get-started) to automatically deploy your project, follow the instructions in [Get started with EAS workflows](https://docs.expo.dev/eas/workflows/get-started) and add the [GitHub integration](https://docs.expo.dev/eas/workflows/get-started#configure-your-project) for your project.
## Create a deployment workflow
Add the following file to .eas/workflows/deploy.yml. This will use the production environment variables, export the web bundle, deploy your project and promote it to production whenever you push to the `main` branch.
.eas/workflows/deploy.yml
Copy
```
name: Deploy
on:
 push:
  branches: ['main']
jobs:
 deploy:
  type: deploy
  name: Deploy
  environment: production
  params:
   prod: true

```

Now, whenever a commit is pushed to `main` or a PR is merged, the workflow will run to deploy your website.
You can also test this workflow by triggering it manually:
Terminal
Copy
`- ``eas workflow:run .eas/workflows/deploy.yml`

