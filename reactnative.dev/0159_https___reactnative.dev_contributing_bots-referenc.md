---
url: https://reactnative.dev/contributing/bots-reference
title: https://reactnative.dev/contributing/bots-reference
date: 2025-05-10T21:35:44.829783
depth: 2
---

[Skip to main content](https://reactnative.dev/contributing/bots-reference#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
## pull-bot[​](https://reactnative.dev/contributing/bots-reference#pull-bot "Direct link to pull-bot")
This pull request linter bot performs basic sanity checks whenever a pull request is created. It might leave a comment on a pull request if it is unable to find a test plan or a changelog in the description, or if it notices that the pull request was not opened against the `main` branch. This bot uses [Danger](https://danger.systems), and its configuration can be found in the [`dangerfile.js`](https://github.com/facebook/react-native/blob/main/packages/react-native-bots/dangerfile.js).
## analysis-bot[​](https://reactnative.dev/contributing/bots-reference#analysis-bot "Direct link to analysis-bot")
The code analysis bot collects feedback from tools such as Prettier, eslint, and Flow whenever a commit is added to a pull request. If any of these tools finds issues with the code, the bot will add these as inline review comments on the pull request. Its configuration can be found in the [`analyze_code.sh`](https://github.com/facebook/react-native/blob/main/scripts/circleci/analyze_code.sh) file in core repository.
## label-actions[​](https://reactnative.dev/contributing/bots-reference#label-actions "Direct link to label-actions")
A bot that acts on an issue or pull request based on a label. Configured in [`.github/workflows/on-issue-labeled.yml`](https://github.com/facebook/react-native/blob/main/.github/workflows/on-issue-labeled.yml).
## github-actions[​](https://reactnative.dev/contributing/bots-reference#github-actions "Direct link to github-actions")
A bot that performs actions defined in a GitHub workflow. Workflows are configured in [`.github/workflows`](https://github.com/facebook/react-native/tree/main/.github/workflows).
## facebook-github-bot[​](https://reactnative.dev/contributing/bots-reference#facebook-github-bot "Direct link to facebook-github-bot")
The Facebook GitHub Bot is used across several open source projects at Meta. In the case of React Native, you will most likely encounter it when it pushes a merge commit to `main` after a pull request is successfully imported to Facebook's internal source control. It will also let authors know if they are missing a Contributor License Agreement.
## react-native-bot[​](https://reactnative.dev/contributing/bots-reference#react-native-bot "Direct link to react-native-bot")
The React Native bot is a tool that helps us automate several processes described in this wiki. Configured in [`hramos/react-native-bot`](https://github.com/hramos/react-native-bot).
Is this page useful?
  * [label-actions](https://reactnative.dev/contributing/bots-reference#label-actions)
  * [github-actions](https://reactnative.dev/contributing/bots-reference#github-actions)
  * [facebook-github-bot](https://reactnative.dev/contributing/bots-reference#facebook-github-bot)
  * [react-native-bot](https://reactnative.dev/contributing/bots-reference#react-native-bot)



