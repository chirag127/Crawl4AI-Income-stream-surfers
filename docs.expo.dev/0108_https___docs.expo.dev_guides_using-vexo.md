---
url: https://docs.expo.dev/guides/using-vexo
title: https://docs.expo.dev/guides/using-vexo
date: 2025-04-30T17:14:01.071914
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Using Vexo
A guide on installing and configuring Vexo for real-time user analytics.
[Vexo](https://www.vexo.co/) provides real-time user analytics for your Expo application, helping you understand how users interact with your app, identify friction points, and improve engagement.
With a two-line integration, Vexo starts collecting data automatically, giving you actionable insights to optimize your app's user experience. If needed, you can also create custom events.
## Features
  1. Complete Dashboard
     * Active Users
     * Session Time
     * Downloads
     * OS Distribution
     * Version Adoption
     * Geographic Insights
     * Popular Screens
  2. Session Replays
     * Watch real user sessions to understand their interactions.
  3. Heatmaps
     * Identify the most engaged areas of your app.
  4. Funnels
     * Analyze user flows and optimize conversion rates.
  5. Custom Events and Dashboard Personalization
     * Track specific user actions by creating custom events.
     * Customize your dashboard to visualize key metrics.


## Getting started
  1. Create an account: Sign up for a [Vexo account](https://www.vexo.co/).
  2. Create a new app: You'll be prompted to create a new app. Give it a name (you can change it later), and once you submit it, you'll receive an API key.
  3. Install the Vexo package: Run the following command in your project:
npm
yarn
Terminal
Copy
`- ``npm install vexo-analytics`
Terminal
Copy
`- ``yarn add vexo-analytics`
  4. Initialize Vexo: Add the following code in your app's entry file (for example, index.js, App.js, or app/_layout.tsx if using Expo Router):
app/_layout.tsx
Copy
```
import { vexo } from 'vexo-analytics';
// You may want to wrap this with `if (!__DEV__) { ... }` to only run Vexo in production.
vexo('YOUR_API_KEY');

```

  5. Rebuild and run your app: Since `vexo-analytics` includes native code, you need to rebuild your application.
  6. Verify integration: Go to your app's page on Vexo and you should see your first event!


## Compatibility
  * Expo: Vexo is compatible with [Development builds](https://docs.expo.dev/development/introduction) and does not require additional configuration plugins.
  * Expo Go: Not supported, as Vexo requires custom native code.


## Learn more about Vexo
To learn more about using Vexo with Expo, check out the [Vexo documentation](https://docs.vexo.co/).

