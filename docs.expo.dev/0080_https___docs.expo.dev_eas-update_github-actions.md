---
url: https://docs.expo.dev/eas-update/github-actions
title: https://docs.expo.dev/eas-update/github-actions
date: 2025-04-30T17:13:13.164622
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Github Action for PR previews
Learn how to use GitHub Actions to automate publishing updates with EAS Update.
A GitHub Action is a cloud function that runs every time an event on GitHub occurs. You can configure GitHub Actions to automate building and publishing updates when you or members of your team merge to a branch, like "production". This makes the process of deploying consistent and fast, leaving you more time to develop your app.
This guide will walk you through how to set up GitHub Actions to publish previews on pull requests.
## Publish previews on pull requests
Another common use case is to create a new update for every pull request. This allows you to test the changes in the pull request on a device before merging the code, and without having to start the project locally. Below are the steps to publish an update every time a pull request is opened:
1
Create a file path named .github/workflows/preview.yml at the root of your project.
2
Inside preview.yml, copy and paste the following snippet:
preview.yml
Copy
```
name: preview
on: pull_request
jobs:
 update:
  name: EAS Update
  runs-on: ubuntu-latest
  permissions:
   contents: read
   pull-requests: write
  steps:
   - name: Check for EXPO_TOKEN
    run: |
     if [ -z "${{ secrets.EXPO_TOKEN }}" ]; then
      echo "You must provide an EXPO_TOKEN secret linked to this project's Expo account in this repo's secrets. Learn more: https://docs.expo.dev/eas-update/github-actions"
      exit 1
     fi
   - name: Checkout repository
    uses: actions/checkout@v4
   - name: Setup Node
    uses: actions/setup-node@v4
    with:
     node-version: 18.x
     cache: yarn
   - name: Setup EAS
    uses: expo/expo-github-action@v8
    with:
     eas-version: latest
     token: ${{ secrets.EXPO_TOKEN }}
   - name: Install dependencies
    run: yarn install
   - name: Create preview
    uses: expo/expo-github-action/preview@v8
    with:
     command: eas update --auto

Show More

```

In the above script:
  * You are using the workflow event `on` to run every time a pull request is opened or updated.
  * In the `update` job, the Node.js version, Expo's GitHub Action and the dependencies are set up using GitHub Action's built-in cache.
  * The `eas update --auto` is run by the [preview subaction](https://github.com/expo/expo-github-action/tree/main/preview#readme). It adds a comment to the pull request with basic information about the update and a QR code to scan the update.


> Don't forget to add the `permissions` section to the job. This enables the job to add comments to the pull request.
3
You can skip this step if you have already set up `EXPO_TOKEN` in the previous section. Only one valid `EXPO_TOKEN` is required to authenticate GitHub Actions with your Expo account.
If you haven't, you need to give the script above permission to run by providing an `EXPO_TOKEN` environment variable.
  * Navigate to <https://expo.dev/settings/access-tokens>.
  * Click Create token to create a new personal access token.
  * Copy the token generated.
  * Navigate to <https://github.com/your-username/your-repo-name/settings/secrets/actions> by replacing "your-username" and "your-repo-name" with your project's info.
  * Under Repository secrets, click New repository secret.
  * Create a secret with the name EXPO_TOKEN, and paste the copied access token in as the value.


Your GitHub Action should be set up now. Whenever a developer creates a pull request, this action will build an update and publish it, making it available to all reviewers with builds that have access to the EAS branch.
> Some repositories or organizations might need to explicitly enable GitHub Workflows and allow third-party Actions.
## Using Bun instead of Yarn
To use [Bun](https://docs.expo.dev/guides/using-bun) as the package manager instead of Yarn, follow the steps below for both publishing updates on push and previews on pull requests:
1
Replace the `Setup Node` step in update.yml or preview.yml with the following snippet:
update.yml/preview.yml
Copy
```
- name: Setup Bun
 uses: oven-sh/setup-bun@v1
 with:
  bun-version: latest

```

2
To install dependencies using Bun, replace the Install dependencies step with the following snippet:
update.yml/preview.yml
Copy
```
- name: Install dependencies
 run: bun install

```


