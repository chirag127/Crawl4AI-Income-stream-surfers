---
url: https://developer.chrome.com/blog/maximum-idb-performance-with-storage-buckets?hl=en
title: https://developer.chrome.com/blog/maximum-idb-performance-with-storage-buckets?hl=en
date: 2025-05-11T16:56:43.175089
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/maximum-idb-performance-with-storage-buckets?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/maximum-idb-performance-with-storage-buckets?hl=es-419)

Sign in


  * On this page
  * [Acknowledgements](https://developer.chrome.com/blog/maximum-idb-performance-with-storage-buckets?hl=en#acknowledgements)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  Maximum IndexedDB performance with Storage Buckets 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Acknowledgements](https://developer.chrome.com/blog/maximum-idb-performance-with-storage-buckets?hl=en#acknowledgements)


Thomas Steiner 
[ GitHub ](https://github.com/tomayac) [ Glitch ](https://glitch.com/@tomayac) [ LinkedIn ](https://www.linkedin.com/in/thomassteinerlinkedin) [ Mastodon ](https://toot.cafe/@tomayac) [ Bluesky ](https://bsky.app/profile/tomayac.com) [ Homepage ](https://blog.tomayac.com/)
The Chrome team has made a number of performance-related improvements to the implementation of IndexedDB (IDB). One such improvement has been to move the backing store of each instance to a separate sequence (you can think of this roughly as a separate thread). What this means is that concurrent use of IDB is now faster, either from the same site, or from cross-site. This post gives all the details, and explains what you need to do to take advantage of this move, which is available from Chrome 126.
## Cross-site
If your use of IDB is cross-site, you don't need to do anything. Once this browser-level move has happened, and the backing store of each IDB instance is moved to a separate sequence, the performance win comes without you having to do anything.
## Same-site
To get this performance enhancement for same-site usage, you need to segregate your IDB usage into different instances, that is, [storage buckets](https://developer.chrome.com/docs/web-platform/storage-buckets). The following code sample shows how this can work:
```
constrequest=indexedDB.open('main',1);
request.onsuccess=(event)=>{
/* Do stuff with the main instance. */
};
// By default, just use the regular IDB instance.
letidb=indexedDB;
// Open a separate storage bucket if the API is supported.
if('storageBuckets'innavigator){
constbucket=awaitnavigator.storageBuckets.open('logs-bucket');
// Get access to the storage bucket's IDB instance.
idb=bucket.indexedDB;
}
constbucketRequest=idb.open('logs',1);
bucketRequest.onsuccess=(event)=>{
/* Do stuff with the separate instance. */
};

```

## Browser support
The performance gain mentioned in this post is a progressive enhancement that you can make use of when the Storage Buckets API is supported in your browser (from Chrome 122) and when the IDB instances are sharded, from Chrome 126.
## Demo
Check out the [demo](https://easy-surf-plot.glitch.me/) of this feature on Glitch. The [source code](https://glitch.com/edit/#!/easy-surf-plot) shows the concept from the previous code snippet in action. Be sure to carefully follow the instructions in the demo. If you inspect the IDB instances with Chrome DevTools, you can see the used storage bucket in the section **Bucket name** , highlighted with a red box in the following screenshot.
## Related links
  * [Not all storage is created equal: introducing Storage Buckets](https://developer.chrome.com/docs/web-platform/storage-buckets)
  * [Draft specification](https://wicg.github.io/storage-buckets/)


## Acknowledgements
This post was reviewed by [Evan Stade](https://www.linkedin.com/in/evan-stade-4585826) and [Rachel Andrew](https://rachelandrew.co.uk/).
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-06-13 UTC.

