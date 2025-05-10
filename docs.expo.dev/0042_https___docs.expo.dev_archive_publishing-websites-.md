---
url: https://docs.expo.dev/archive/publishing-websites-webpack
title: https://docs.expo.dev/archive/publishing-websites-webpack
date: 2025-04-30T17:12:40.068172
depth: 2
---

[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Publish websites with Webpack
Different ways to publish the Expo web app with third-party services with webpack.
> Deprecated: In SDK 50 and above, publishing with `webpack` is deprecated in favor of `metro`. Learn more in [migrating from Webpack to Expo Router](https://docs.expo.dev/router/migrate/from-expo-webpack).
A web app created using Expo can be served locally for testing out the production behavior. Once the testing phase checks out, you can choose from a variety of third-party services to host it.
Bundler| Expo Router| API Routes| Description  
---|---|---|---  
`webpack`| Outputs a Single Page Application (SPA) with a single index.html in the output directory.  
## Create a web build
Creating a web build of the project is the first step to publishing a web app. Whether you want to serve it locally or host it on a third-party service, you have to export all JavaScript and assets of a project. This is known as a static bundle. It can be exported by running the following command:
Run the webpack export command to compile the project for web:
Terminal
Copy
`- ``npx expo export:web`
The resulting project files are in the web-build directory. Any files inside the web directory are also copied to the web-build directory.
If you make changes to your project, rebuild it for production. Do not edit the web-build directory directly.
## Serve locally
Use [Serve CLI](https://www.npmjs.com/package/serve) to quickly test locally how your website will be hosted in production. Run the following command to serve the static bundle:
Run the following command to serve the single-page application:
Terminal
Copy
`- ``npx serve web-build --single`
Open [`http://localhost:5000`](http://localhost:5000) to see your project in action. This method is HTTP only, so permissions, camera, location, and many other things won't work.
## Server a sub-directory
If you want to serve your site in a sub-directory, add its path to your package.json as shown below:
package.json
Copy
```
{
 "homepage": "/path/to/sub-directory"
}

```

## Hosting on third-party services
### Netlify
[Netlify](https://www.netlify.com/) is a mostly-unopinionated platform for deploying web apps. This has the highest compatibility with Expo web apps as it makes few assumptions about the framework.
#### Manual deployment with the Netlify CDN
1
Install the Netlify CLI by running the following command:
Terminal
Copy
`- ``npm install -g netlify-cli`
2
Configure redirects for single-page applications.
If your app implements any navigation, you'll need to configure Netlify to redirect requests to the single web-build/index.html file. This can be done in Netlify by creating a ./public/_redirects file and redirecting all requests to /index.html.
Navigate inside the web-build directory and run the following command to create _redirects file with following rule:
web/_redirects
Copy
```
/*  /index.html  200

```

If you modify this file, you must rebuild your project with `npx expo export:web` to have it safely copied into the web-build directory.
3
Deploy the web build directory by running the following command:
Terminal
Copy
`- ``netlify deploy --dir web-build`
You will see a URL that you can use to view your project online.
#### Continuous delivery
Netlify can also build and deploy when you push to git or open a new pull request:
  * [Start a new Netlify project](https://app.netlify.com/signup).
  * Pick your Git hosting service and select your repository.
  * Click Build your site.


### Vercel
[Vercel](https://vercel.com/) has a single-command deployment flow.
1
Install the [Vercel CLI](https://vercel.com/docs/cli).
Terminal
Copy
`- ``npm install -g vercel@latest`
2
Configure redirects for single-page applications. Create a vercel.json file at the root of your app and add the following:
vercel.json
Copy
```
{
 "buildCommand": "expo export:web",
 "outputDirectory": "web-build",
 "devCommand": "expo",
 "cleanUrls": true,
 "framework": null,
 "rewrites": [
  {
   "source": "/:path*",
   "destination": "/"
  }
 ]
}

```

3
Deploy the website.
Terminal
Copy
`- ``vercel`
You will now see a URL that you can use to view your project online. Paste that URL into your browser when the build is complete, and see your deployed app.
### AWS Amplify Console
The [AWS Amplify Console](https://console.amplify.aws) provides a Git-based workflow for continuously deploying and hosting full-stack serverless web apps. Amplify deploys your PWA from a repository instead of your computer, so you must use a GitHub repository. Before starting, [create a new repo on GitHub](https://github.com/new).
1
Add the [amplify-explicit.yml](https://github.com/expo/amplify-demo/blob/master/amplify-explicit.yml) file to the root of your repository. Ensure you have removed the generated dist directory from the .gitignore file and committed those changes.
2
Push your local Expo project to a GitHub repository. If you have not pushed to GitHub yet, follow [GitHub's guide to add an existing project to GitHub](https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github).
3
Login to the [Amplify Console](https://console.aws.amazon.com/amplify/home) and select an existing app or create a new app. Grant Amplify permission to read from your GitHub account or the organization that owns your repo.
4
Add your repo, select the branch, and select Connecting a monorepo? to enter the path to your app's dist directory and choose Next.
The Amplify Console will detect the amplify.yml file in your project. Select Allow AWS Amplify to automatically deploy all files hosted in your project root directory and choose Next.
5
Review your settings and choose Save and deploy. Your app will now be deployed to a `https://branchname.xxxxxx.amplifyapp.com` URL. You can now visit your web app, deploy another branch, or add a unified backend environment across your Expo mobile and web apps.
Follow the steps in the Learn how to get the most out of Amplify Hosting drop-down to Add a custom domain with a free SSL certificate and more information.
### GitHub Pages
[GitHub Pages](https://pages.github.com/) allows you to publish a website directly from a GitHub repository.
1
Start by initializing a new git repository in your project. If this is already done, skip this step.
If not then you'll want to run the following command in your project's root directory:
Terminal
Copy
`- ``git init`
2
Add the GitHub repository as a `remote` in your local git repository.
Terminal
Copy
`- ``git remote add origin https://github.com/username/expo-gh-pages.git`
Running the above command makes git know to which repository you want to push your source code. It also makes the `gh-pages` package (installed in the next step) know where you want to deploy your app.
3
Install the `gh-pages` package as a `dev-dependency` in your project:
Terminal
Copy
`- ``yarn add -D gh-pages`
4
Configure your project's package.json for web hosting. Start by adding a `homepage` property. Set its value to the string `http://{username on GitHub}.github.io/{repo-name}`.
For example, if a GitHub username is called `dev` and the GitHub repository is `expo-gh-pages`, the following will be the value of the `homepage` property:
package.json
Copy
```
{
 "homepage": "http://dev.github.io/expo-gh-pages"
}

```

In the same file, modify the `scripts` property by adding `predeploy` and `deploy` properties. Each has its own value as shown:
package.json
Copy
```
"scripts": {
 %%placeholder-start%%... %%placeholder-end%%
 "deploy": "gh-pages -d web-build",
 "predeploy": "expo export:web"
}

```

5
To generate a production build of your app, and deploy it to GitHub Pages, run the following command:
Terminal
Copy
`- ``yarn deploy`
Your web app is now available at the URL you set as `homepage` in your package.json.
> When you publish code to your repository, for example: `gh-pages`, it will create and push the code to a branch in your repo. This branch will have your build code, however, not your development source code.
### Firebase hosting
[Firebase Hosting](https://console.firebase.google.com/) is production-grade web content hosting for web projects.
1
Create a firebase project with the [Firebase Console](https://console.firebase.google.com) and install the Firebase CLI by following these [instructions](https://firebase.google.com/docs/hosting).
2
Using the CLI, login to your Firebase account by running the command:
Terminal
Copy
`- ``firebase login`
3
Then, initialize your firebase project to host by running the command:
Terminal
Copy
`- ``firebase init`
The settings will depend on how you built your Expo website:
When asked about the public path, make sure to specify the web-build directory. Also, when prompted Configure as a single-page app (rewrite all urls to /index.html), select Yes.
4
In the existing `scripts` property of package.json, add `predeploy` and `deploy` properties. Each has the following values:
package.json
Copy
```
"scripts": {
 %%placeholder-start%%... %%placeholder-end%%
 "predeploy": "expo export:web",
 "deploy-hosting": "npm run predeploy && firebase deploy --only hosting",
}

```

5
To deploy, run the following command:
Terminal
Copy
`- ``npm run deploy-hosting`
Open the URL from the console output to check your deployment, for example: `https://project-name.firebaseapp.com`.
In case you want to change the header for hosting add the following config for `hosting` section in firebase.json:
firebase.json
Copy
```
 "hosting": [
  {
   %%placeholder-start%%... %%placeholder-end%%
   "headers": [
    {
     "source": "/**",
     "headers": [
      {
       "key": "Cache-Control",
       "value": "no-cache, no-store, must-revalidate"
      }
     ]
    },
    {
     "source": "**/*.@(jpg|jpeg|gif|png|svg|webp|js|css|eot|otf|ttf|ttc|woff|woff2|font.css)",
     "headers": [
      {
       "key": "Cache-Control",
       "value": "max-age=604800"
      }
     ]
    }
   ],
  }
 ]

Show More

```


