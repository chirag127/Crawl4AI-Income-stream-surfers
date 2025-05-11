---
url: https://developer.chrome.com/blog/automatic-picture-in-picture-media-playback?hl=en
title: https://developer.chrome.com/blog/automatic-picture-in-picture-media-playback?hl=en
date: 2025-05-11T16:54:00.255016
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/automatic-picture-in-picture-media-playback?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/automatic-picture-in-picture-media-playback?hl=es-419)

Sign in


  * On this page
  * [Engage and share feedback](https://developer.chrome.com/blog/automatic-picture-in-picture-media-playback?hl=en#engage_and_share_feedback)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  Enter picture-in-picture automatically when playing media 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Engage and share feedback](https://developer.chrome.com/blog/automatic-picture-in-picture-media-playback?hl=en#engage_and_share_feedback)


François Beaufort 
[ GitHub ](https://github.com/beaufortfrancois)
Published: February 5, 2025 
From Chrome 120, video conferencing web apps can automatically open a picture-in-picture window when the user switches focus from their current tab. This is useful for presenters who want to see and interact with participants in real time while presenting a document or using other tabs or windows. See [Automatic picture-in-picture for video conferencing web apps](https://developer.chrome.com/blog/automatic-picture-in-picture) for details.
From Chrome 134, web apps that play audio or video can automatically enter picture-in-picture mode. This means that music and video players on the web can now seamlessly switch to a mini player window when the user switches tabs, eliminating the need for manual activation.
A picture-in-picture window opened and closed automatically when Spotify user switches tabs.
To support these media playback use cases, from Chrome 134 desktop web apps can automatically enter picture-in-picture, with a few restrictions to ensure a positive user experience. A web app is only eligible for automatic picture-in-picture for media playback if it meets all of the following conditions:
  * The top frame URL is safe according to the Safe Browsing service.
  * The media lives in the top frame.
  * The media has been audible within the last two seconds.
  * The media has audio focus.
  * The media is playing.
  * A [media session action](https://www.w3.org/TR/mediasession/#ref-for-enumdef-mediasessionaction) handler for the `"enterpictureinpicture"` action has been registered.
  * The user's [Media Engagement Index](https://developer.chrome.com/blog/autoplay#media_engagement_index) threshold has been exceeded, indicating that the user frequently consumes media in this web app. This applies if the user's browser setting is "Can ask to enter picture-in-picture". If the user explicitly allows the web app to enter picture-in-picture, this condition does not apply.

Automatic picture-in-picture setting in Chrome browser site information pane.
The [bug 386193409](https://issues.chromium.org/issues/386193409) tracks the implementation of surfacing conditions to make debugging and implementation easier.
Note that if another picture-in-picture window is already open, Chrome doesn't trigger automatic picture-in-picture. This rule doesn't apply if the existing picture-in-picture window was opened automatically and is about to close.
When a web app meets the requirements, switching focus to another tab triggers the media session action handler callback function for the `"enterpictureinpicture"` action. This lets the web app open a picture-in-picture window without a user gesture. The user may then be presented with a permission dialog, asking if they would like to allow the site to enter picture-in-picture automatically every time, only this time, or never.
User is asked whether entering picture-in-picture automatically is allowed.
You can either use the [Picture-in-Picture API for <video>](https://developer.chrome.com/blog/watch-video-using-picture-in-picture) to open a picture-in-picture window from an HTML `<video>` element, or the [Document Picture-in-Picture API](https://developer.chrome.com/docs/web-platform/document-picture-in-picture) to open an always-on-top window to populate with arbitrary HTML content. The picture-in-picture window is not focused when opened and automatically closed when the page becomes visible again.
The following example shows you how to play an HTML `<video>` element when a user clicks a button. Then, safely register a media session action handler for the `"enterpictureinpicture"` action with a callback function that opens a picture-in-picture window. This window contains the video with the Picture-in-Picture API for <video>.
```
constvideo=document.querySelector("video");
asyncfunctiononPlayButtonClick(){
// Play video.
awaitvideo.play();
}
try{
// Request video to automatically enter picture-in-picture when eligible.
navigator.mediaSession.setActionHandler("enterpictureinpicture",async()=>{
awaitvideo.requestPictureInPicture();
});
}catch(error){
console.log("The enterpictureinpicture action is not yet supported.");
}

```

Try the [VideoJS player demo](https://document-picture-in-picture-api.glitch.me/) which showcases the Document Picture-in-Picture API or play with the [Video Media Session](https://googlechrome.github.io/samples/media-session/video.html) and [Audio Media Session](https://googlechrome.github.io/samples/media-session/audio.html) samples.
## Engage and share feedback
If you have feedback or encounter any issues, you can share them at [crbug.com](https://issues.chromium.org/issues/new?noWizard=true&template=1942032&component=1456334&pli=1).
## Resources
  * [Spec changes](https://github.com/w3c/mediasession/pull/295)
  * [ChromeStatus entry](https://chromestatus.com/feature/6245717716238336)
  * [Intent to Ship](https://groups.google.com/a/chromium.org/g/blink-dev/c/BEhYD8v4zY0/m/ZcINHmMMBAAJ)
  * [Chromium issue](https://issues.chromium.org/issues/368058093)


## Acknowledgments
Thanks to Benjamin Keen and Frank Liberato for their reviews.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-02-05 UTC.

