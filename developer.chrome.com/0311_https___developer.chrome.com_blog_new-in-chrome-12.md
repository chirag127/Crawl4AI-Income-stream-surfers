---
url: https://developer.chrome.com/blog/new-in-chrome-124?hl=en
title: https://developer.chrome.com/blog/new-in-chrome-124?hl=en
date: 2025-05-11T16:57:21.670671
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-chrome-124?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-chrome-124?hl=es-419)




  * On this page
  * [Use declarative shadow DOM in JavaScript](https://developer.chrome.com/blog/new-in-chrome-124?hl=en#dsd)
  * [WebSocket Stream API](https://developer.chrome.com/blog/new-in-chrome-124?hl=en#streams-in-sockets)
  * [View transitions improvements](https://developer.chrome.com/blog/new-in-chrome-124?hl=en#view-transitions)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  New in Chrome 124 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Use declarative shadow DOM in JavaScript](https://developer.chrome.com/blog/new-in-chrome-124?hl=en#dsd)
  * [WebSocket Stream API](https://developer.chrome.com/blog/new-in-chrome-124?hl=en#streams-in-sockets)
  * [View transitions improvements](https://developer.chrome.com/blog/new-in-chrome-124?hl=en#view-transitions)


Pete LePage 
[ GitHub ](https://github.com/petele) [ Glitch ](https://glitch.com/@petele) [ Mastodon ](https://techhub.social/@petele) [ Homepage ](https://petelepage.com/)
Here are the highlights in Chrome 124:
  * There are two new APIs that allow the [declarative shadow DOM](https://developer.chrome.com/blog/new-in-chrome-124?hl=en#dsd) to be used from JavaScript.
  * You can use [streams in Web Sockets](https://developer.chrome.com/blog/new-in-chrome-124?hl=en#streams-in-sockets).
  * [View Transitions](https://developer.chrome.com/blog/new-in-chrome-124?hl=en#view-transitions) get a little better.
  * And there's plenty [more](https://developer.chrome.com/blog/new-in-chrome-124?hl=en#more).


Want the full run down? Check out the [Chrome 124 Release Notes](https://developer.chrome.com/release-notes/124).
## Use declarative shadow DOM in JavaScript
There are two new APIs that allow the declarative shadow DOM to be used from JavaScript.
`setHTMLUnsafe()` is similar to `innerHTML`, and lets you set the inner HTML of an element to the string provided. This helps when you have some HTML that includes a declarative shadow DOM, like this.
```
<my-custom-element>
 <template shadowrootmode="open">
  <style>
   :host {
    display: block;
    color: yellow;
   }
  </style>
  Hello, <slot></slot>
 </template>
</my-custom-element>

```

If you just use `innerHTML`, the browser won't parse it properly, and there's no shadow DOM. But with `setHTMLUnsafe()`, your shadow DOM is created, and the element is parsed as you'd expect.
```
constsection=document.createElement("section");
section.setHTMLUnsafe(`<my-custom-element>...</my-custom-element>`);

```

The other API is `parseHTMLUnsafe()`, and it works similarly to `DOMParser.parseFromString()`.
Both of these APIs are **unsafe** , which means they don't do any input sanitization. So you'll want to make sure that whatever you feed them, is safe. In an upcoming release, we expect see a version that does provide sanitization of the input.
Finally, both of these APIs are already supported in the latest version of Firefox and Safari!
## WebSocket Stream API
WebSockets are a great way to send data back and forth between the user's browser and the server without having to rely on polling. This is great for things like chat apps, where you want to deal with information as soon as it comes in.
But what if the data arrives faster than you can handle?
That's called back pressure, and can cause some serious headaches for you. Unfortunately, the WebSocket API doesn't have a nice way to deal with back pressure.
The [WebSocket Stream API](https://developer.chrome.com/docs/capabilities/web-apis/websocketstream) gives you the power of streams, and web sockets, which means back pressure can be applied without any extra cost.
Start by constructing a new `WebSocketStream` and passing it the URL of the WebSocket server.
```
constwss=newWebSocketStream(WSS_URL);
const{readable,writable}=awaitwss.opened;
constreader=readable.getReader();
constwriter=writable.getWriter();
while(true){
const{value,done}=awaitreader.read();
if(done){
break;
}
constresult=awaitprocess(value);
awaitwriter.write(result);
}

```

Next, you wait for the connection to be opened, which results in a `ReadableStream` and a `WritableStream`. By calling the `ReadableStream.getReader()` method, you get a `ReadableStreamDefaultReader` which you can then `read()` data from until the stream is done.
To write data, call the `WritableStream.getWriter()` method, which gives you a `WritableStreamDefaultWriter`, that you can then `write()` data to.
## View transitions improvements
I'm excited about the View Transitions features, and there are two new features in Chrome 124 designed to make view transitions easier.
The `pageswap` event is fired on a document's window object when a navigation will replace the document with a new document.
```
document.addEventListener("pageswap",event=>{
if(!event.viewTransition){
return;
}
});

```

And document render-blocking which lets you block rendering of a document until the critical content has been parsed, ensuring a consistent first paint across all browsers.
## And more!
Of course there's plenty more.
  * [`disallowReturnToOpener`](https://developer.chrome.com/docs/web-platform/document-picture-in-picture#hide_the_back_to_tab_button_of_the_picture-in-picture_window) hints to the browser that it shouldn't show a button in the picture-in-picture window that allows the user to go back to the opener tab.
  * [Keyboard-focusable scroll containers](https://developer.chrome.com/blog/keyboard-focusable-scrollers) improves accessibility by making scroll containers focusable using sequential focus navigation.
  * And universal install allows users to install any page, even those not meeting the [current PWA criteria](https://web.dev/articles/install-criteria).


## Further reading
This covers only some key highlights. Check the following links for additional changes in Chrome 124.
  * [Chrome 124 Release Notes](https://developer.chrome.com/release-notes/124)
  * [What's new in Chrome DevTools (124)](https://developer.chrome.com/blog/new-in-devtools-124)
  * [ChromeStatus.com updates for Chrome 124](https://chromestatus.com/features#milestone%3D124)
  * [Chromium source repository change list](https://chromium.googlesource.com/chromium/src/+log/123.0.6312.129..124.0.6367.66)
  * [Chrome release calendar](https://chromiumdash.appspot.com/schedule)


## Subscribe
To stay up to date, [subscribe](https://goo.gl/6FP1a5) to the [Chrome Developers YouTube channel](https://www.youtube.com/user/ChromeDevelopers/), and you'll get an email notification whenever we launch a new video.
I'm Pete LePage, and as soon as Chrome 125 is released, we'll be right here to tell you what's new in Chrome!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-04-16 UTC.

