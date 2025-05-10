---
url: https://expo.dev/blog/deploying-an-expo-app-to-web-with-eas-hosting
title: https://expo.dev/blog/deploying-an-expo-app-to-web-with-eas-hosting
date: 2025-04-30T17:18:15.274150
depth: 2
---

[All Posts](https://expo.dev/blog)
Share this post
# Deploy an Expo app to web in 2 commands with EAS Hosting
Users, Product, Development•April 15, 2025•5 minute read
Solarin Johnson
Guest Author
Learn how to deploy your Expo Web app with EAS Hosting in minutes—plus see a real-world animation demo using React Native and Reanimated.
_This is a guest post from Solarin Johnson - a 17-year-old developer building animated UIs with Expo. He's obsessed with clean motion and smooth user flows._
...
The Expo ecosystem keeps adding new features and capabilities, and their newest thing, [EAS Hosting](https://docs.expo.dev/eas/hosting/introduction/), makes it really easy to deploy React Native web apps. If you’ve ever deployed a Next.js app with Vercel, the experience will feel familiar. 
I experienced this myself recently when I saw a [cool prototype on **X (Twitter)**](https://x.com/raphaelsalaja/status/1897296203102216702) and wanted to **replicate it in React Native (Expo)**. The next thing I knew I was deploying with EAS Hosting!My original idea was simply to:
  * Experiment with **Reanimated for scroll-based animations.**
  * Show that **Expo can handle complex animations smoothly.**


[ Solarin](https://twitter.com/S0LARIN/status/1901478306215493644)
[@S0LARIN](https://twitter.com/S0LARIN/status/1901478306215493644)
Spotted a cool animation had to rebuild it ⚡️ Made this with [@expo](https://twitter.com/expo)[@swmansion](https://twitter.com/swmansion) Reanimated GitHub [github.com/Solarin-Johnso…](https://github.com/Solarin-Johnson/expo-blog)
Raphael Salaja
@raphaelsalaja
blogs should be joyful
[342](https://twitter.com/intent/like?tweet_id=1901478306215493644)[Reply](https://twitter.com/intent/tweet?in_reply_to=1901478306215493644)Copy link
The core features are powered by [**Reanimated**](https://docs.swmansion.com/react-native-reanimated/) and [**Expo Router**](https://docs.expo.dev/router/introduction/) (even though it’s a single page). Here’s a quick technical breakdown:
### [Scroll-Linked Progress Bar ](https://expo.dev/blog/deploying-an-expo-app-to-web-with-eas-hosting#scroll-linked-progress-bar)
There's a **bottom flow bar** that displays the title of the section the user is currently reading (based on scroll position).
  * It also functions as a **radial progress bar** , visually representing **reading progress**
  * The progress bar dynamically updates as the user scrolls through the content.


**Tracking Scroll Position**
Code
Copy
```

const scrollY =useSharedValue(0);
const totalHeight =useSharedValue(1);
const scrollHandler =useAnimatedScrollHandler({
onScroll:(event)=>{
   scrollY.value= event.contentOffset.y;
   totalHeight.value= event.contentSize.height- event.layoutMeasurement.height;
},
});
const progress =useDerivedValue(()=>
  totalHeight.value>0? scrollY.value/ totalHeight.value:0
);

```

### [Expanding and collapsing the flow bar ](https://expo.dev/blog/deploying-an-expo-app-to-web-with-eas-hosting#expanding-and-collapsing-the-flow-bar)
By default, the **bottom flow bar** is minimal, showing just the current section title and a radial progress. **Tapping it expands** the bar to display:
  * **Previous and next section titles**
  * **Time progress indicator** (like a media player progress bar)


**Toggling the Expanded State**
Code
Copy
```

const[isExpanded, setIsExpanded]=useState(false);
const animatedStyle =useAnimatedStyle(()=>({
	height:withTiming(isExpanded ?100:PEEK_VIEW_HEIGHT,TIMING_CONFIG),
}));
consttoggleExpand=()=>{
setIsExpanded((prev)=>!prev)
};

```

**Progress Bar Component**
Code
Copy
```

<View style={styles.progressBar}>
<Animated.View
		style={[
		 styles.progressLine,
useAnimatedStyle(()=>({
		  width:`${progress.value*100}%`,
})),
]}
/>
</View>

```

To see this code in action check out:
  * GitHub Repo: [GitHub](https://github.com/Solarin-Johnson/expo-blog).
  * Live Demo: [expo-blog.expo.app](https://expo-blog.expo.app/)


Now that you can see the animation demo is working, let’s talk about how I **deployed it online** using **EAS Hosting,** without any extra setup.
## [Why EAS Hosting? ](https://expo.dev/blog/deploying-an-expo-app-to-web-with-eas-hosting#why-eas-hosting)
With EAS Hosting, it's super easy. Only two commands in the Command Line Interface (CLI), and you can go live with your Expo Web app. No need to waste time uploading your app and configuring it manually. Just deploy, and you'll be given your URL right away. Here are some of the key benefits I observed from my experience deploying with EAS Hosting:
  * **Minimal Setup** – No need to configure servers or CDNs.
  * **Fast Deployments** – Your app goes live in seconds.
  * **Try It Out Free** –EAS Hosting is still in preview mode, so there's no need to spend money to deploy your app.

## [Deploying with EAS Hosting ](https://expo.dev/blog/deploying-an-expo-app-to-web-with-eas-hosting#deploying-with-eas-hosting)
The process couldn’t be easier. Here are the 4 steps:
### [1. Prepare Your App ](https://expo.dev/blog/deploying-an-expo-app-to-web-with-eas-hosting#1-prepare-your-app)
First, make sure your Expo Web app runs correctly on your local machine. If it works locally, it should work after deployment.
### [2. Export for Web ](https://expo.dev/blog/deploying-an-expo-app-to-web-with-eas-hosting#2-export-for-web)
Run the following command to generate the **static web build** :
Terminal
Copy
`npx expo export --platform web`
This creates a `dist` folder containing your optimized web output.
### [3. Deploy to EAS Hosting ](https://expo.dev/blog/deploying-an-expo-app-to-web-with-eas-hosting#3-deploy-to-eas-hosting)
Now, deploy your app:
Terminal
Copy
`eas deploy`
If you haven’t logged into EAS via CLI, it’ll prompt you to do so. Once authenticated, your app gets deployed, and you receive a URL where it’s hosted.
Want to deploy directly to production? Use:
Terminal
Copy
`eas deploy --prod`
By default, Expo auto-generates a **favicon** based on your `app.json`, so you don’t have to worry about it.
### [4. Monitor performance and requests ](https://expo.dev/blog/deploying-an-expo-app-to-web-with-eas-hosting#4-monitor-performance-and-requests)
Once your app is deployed, **EAS Hosting doesn’t just serve your app—it also helps you track its performance.** You can monitor:
  * **Incoming requests** – See how many users are accessing your site.
  * **Crashes & errors** – Identify unexpected issues that could affect user experience.
  * **Deployment history** – Keep track of when you deployed and what changed.

## [Optimizing an Expo web app for SEO and sharing ](https://expo.dev/blog/deploying-an-expo-app-to-web-with-eas-hosting#optimizing-an-expo-web-app-for-seo-and-sharing)
Now that your app is live, let’s talk about making it **search-friendly** and ensuring it looks great when shared.
By default, Expo Web exports don’t include much metadata. Without meta tags, your app might not show proper previews on **Google, Twitter, or WhatsApp**.
## [Adding Meta Tags in Expo Web ](https://expo.dev/blog/deploying-an-expo-app-to-web-with-eas-hosting#adding-meta-tags-in-expo-web)
Expo Router provides a built-in way to add meta tags using `expo-router/head`, similar to Next.js `<Head>` component.
Here’s an example:
Code
Copy
```

import{Stack}from"expo-router";
importHeadfrom"expo-router/head";
exportdefaultfunctionLayout(){
return(
<>
<Head>
<meta name="description" content="A smooth animation demo built with Expo and Reanimated."/>
<meta property="og:title" content="Expo Web Animations"/>
<meta property="og:image" content="https://your-app.com/preview.png"/>
<meta property="twitter:card" content="summary_large_image"/>
</Head>
<Stack/>
</>
);

```

Pro Tip: No need to add a `<link rel="icon" />` manually—Expo Web automatically generates a favicon when you export.
Also, if your app works locally, **EAS Hosting makes sure it works online** without any extra steps.
## [My reflections on EAS Hosting ](https://expo.dev/blog/deploying-an-expo-app-to-web-with-eas-hosting#my-reflections-on-eas-hosting)
  * **Deployment Speed** – Extremely fast; no unnecessary steps.
  * **Reliability** – No major errors during deployment.
  * **Ease of Use** – The CLI-based flow is intuitive, even for beginners.


EAS Hosting makes deploying Expo Web apps as simple as running two commands. If you’re already using Expo, it’s worth trying out—no extra setup, no hassle.
As Expo continues improving its ecosystem, EAS Hosting is shaping up to be the go-to deployment solution. Whether for quick prototypes or production-ready apps, **it just works**.
EAS Hosting
Expo Router
Reanimated
SEO
#### Table of Contents
[Scroll-Linked Progress Bar](https://expo.dev/blog/deploying-an-expo-app-to-web-with-eas-hosting#scroll-linked-progress-bar)[Expanding and collapsing the flow bar](https://expo.dev/blog/deploying-an-expo-app-to-web-with-eas-hosting#expanding-and-collapsing-the-flow-bar)[Why EAS Hosting?](https://expo.dev/blog/deploying-an-expo-app-to-web-with-eas-hosting#why-eas-hosting)[Deploying with EAS Hosting](https://expo.dev/blog/deploying-an-expo-app-to-web-with-eas-hosting#deploying-with-eas-hosting)[1. Prepare Your App](https://expo.dev/blog/deploying-an-expo-app-to-web-with-eas-hosting#1-prepare-your-app)[2. Export for Web](https://expo.dev/blog/deploying-an-expo-app-to-web-with-eas-hosting#2-export-for-web)[3. Deploy to EAS Hosting](https://expo.dev/blog/deploying-an-expo-app-to-web-with-eas-hosting#3-deploy-to-eas-hosting)[4. Monitor performance and requests](https://expo.dev/blog/deploying-an-expo-app-to-web-with-eas-hosting#4-monitor-performance-and-requests)[Optimizing an Expo web app for SEO and sharing](https://expo.dev/blog/deploying-an-expo-app-to-web-with-eas-hosting#optimizing-an-expo-web-app-for-seo-and-sharing)[Adding Meta Tags in Expo Web](https://expo.dev/blog/deploying-an-expo-app-to-web-with-eas-hosting#adding-meta-tags-in-expo-web)[My reflections on EAS Hosting](https://expo.dev/blog/deploying-an-expo-app-to-web-with-eas-hosting#my-reflections-on-eas-hosting)
#### Related Blog Posts
[React Native Hosting with EAS: Deploy your server-driven Expo apps to the cloud](https://expo.dev/blog/expo-announces-eas-hosting-service)[How to build beautiful React Native bottom tabs](https://expo.dev/blog/how-to-build-beautiful-react-native-bottom-tabs)[How to build a solid test harness for Expo apps](https://expo.dev/blog/how-to-build-a-solid-test-harness-for-expo-apps)
Share this post
### Sign up for the Expo Newsletter
Sign up to receive a summary of new features, capabilities, content, and news about Expo and the React Native community.
### Dive in, and create your first Expo project
[Learn More](https://docs.expo.dev)

