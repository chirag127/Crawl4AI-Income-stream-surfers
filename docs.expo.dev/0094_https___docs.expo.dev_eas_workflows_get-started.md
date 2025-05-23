---
url: https://docs.expo.dev/eas/workflows/get-started
title: https://docs.expo.dev/eas/workflows/get-started
date: 2025-04-30T17:13:38.641136
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Get started with EAS Workflows
Learn how to use EAS Workflows to automate your React Native CI/CD development and release processes.
Builds, submissions, updates, and more are all a part of delivering your app to users. EAS Workflows consist of a sequence of jobs, which help you and your team get things done. With workflows, you can build your project, run end-to-end tests, submit that build to the app stores, and then run custom scripts after the submission is complete. Since each job can have prerequisites and conditionals, you can automate your and your team's CI/CD for your React Native project.
## Get started
Learn what EAS Workflows are and how to use them to automate your CI/CD processes with the following video tutorial:
[Watch: Get Started with EAS WorkflowsLearn how to automate some of the most common processes that every app development team must tackle: creating development builds, publishing preview updates, and deploying to production.](https://www.youtube.com/watch?v=OJ2u9tQCpr4)
Share the following slide in your next team meeting to discuss what EAS Workflows are and how they can help your team:
[EAS Workflows CI/CD sync slideLearn the benefits of using EAS Workflows to automate your CI/CD processes.](https://docs.expo.dev/static/images/eas-workflows/eas-worfklows-slide.png) How do workflows compare to other CI services?
EAS Workflows are designed to help you and your team release your app. It comes preconfigured with pre-packaged job types that can build, submit, update, run Maestro tests, and more. All job types run on EAS, so you'll only have to manage one set of YAML files, and all the artifacts from your job runs will appear on [expo.dev](https://expo.dev/).
Other CI services, like CircleCI and GitHub Actions, are more generalized and have the ability to do more than workflows. However, those services also require you to understand more about the implementation of each job. While that is necessary in some cases, workflows help you get common tasks done quickly by pre-packaging the most essential types of jobs for app developers. In addition, workflows are designed to provide you with the fastest possible cloud machine for the task at hand, and we're constantly updating those for you.
EAS Workflows are great for operations related to your Expo apps, while other CI/CD services will provide a better experience for other types of workflows.
## Set up your project
If you haven't already, you'll need to create a project and sync it with EAS:
Create a project and sync it with EAS
You can create a new project with the following command:
Terminal
Copy
`- ``npx create-expo-app@latest`
Once you've created the project, login with your account:
Terminal
Copy
`- ``npx eas-cli@latest login`
Finally, link the project you have locally with EAS:
Terminal
Copy
`- ``npx eas-cli@latest init`
## Configure your project
EAS Workflows require a GitHub repository that's linked to your EAS project to run. You can link a GitHub repo to your EAS project with the following steps:
  * Navigate to your project's [GitHub settings](https://expo.dev/accounts/%5Baccount%5D/projects/%5BprojectName%5D/github).
  * Follow the UI to install the GitHub app.
  * Select the GitHub repository that matches the Expo project and connect it.


## Write a workflow
First, create a directory named .eas/workflows at the root of your project with a YAML file inside of it. For example: .eas/workflows/hello-world.yml.
Now we're ready to write the contents of hello-world.yml. Each workflow consists of three top-level elements:
  * `name`: defines the name of the workflow. For example: "Hello World"
  * `on`: defines when this workflow should be triggered. For example, when pushing a new commit to a GitHub branch.
  * `jobs`: a sequence of jobs which can depend on and pass data between each other. For example: a job that runs a unit test followed by a job that builds your project into an app.


Here's an example of a workflow that prints "Hello, world":
.eas/workflows/hello-world.yml
Copy
```
name: Hello World
on:
 push:
  branches: ['*']
jobs:
 Hello World:
  steps:
   - run: echo "Hello, World"

```

Here's another example that creates and submits an iOS build of a project on every push to every branch. This is similar to running `eas build --platform ios --profile production --auto-submit`:
.eas/workflows/ios-build-and-submit.yml
Copy
```
name: Release iOS app
on:
 push:
  branches: ['*']
jobs:
 build:
  type: build
  params:
   platform: ios
   profile: production
 submit:
  needs: [build]
  type: submit
  params:
   build_id: ${{ needs.build.outputs.build_id }}

```

> Download the [Expo Tools VS Code extension](https://marketplace.visualstudio.com/items?itemName=expo.vscode-expo-tools) to get descriptions and autocompletions for your workflow files.
## Run your workflow
Once you have a workflow file and your project is connected to Expo's GitHub app, you can trigger your workflow by pushing a commit to your GitHub repository. For the workflow to run, you'll need to make sure the trigger (defined with `on`) you defined in your workflow is met.
Alternatively, you can trigger a workflow manually by running the following command:
Terminal
Copy
`- ``npx eas-cli@latest workflow:run .eas/workflows/<your-workflow-file>.yml`
Once you do, you can see your workflow running on your project's [workflows page](https://expo.dev/accounts/%5Baccount%5D/projects/%5BprojectName%5D/workflows).
> Got feedback or feature requests? Send us an email at workflows@expo.dev.

