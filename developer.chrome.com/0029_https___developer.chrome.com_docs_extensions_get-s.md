---
url: https://developer.chrome.com/docs/extensions/get-started?hl=bn
title: https://developer.chrome.com/docs/extensions/get-started?hl=bn
date: 2025-05-11T16:51:58.704346
depth: 1
---

[ সরাসরি আসল কন্টেন্টে যান ](https://developer.chrome.com/docs/extensions/get-started?hl=bn#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/extensions/get-started?hl=es-419)




এই পৃষ্ঠাটি [Cloud Translation API](https://cloud.google.com/translate/?hl=bn) অনুবাদ করেছে। 


###  শুরু করুন 
Chrome এক্সটেনশন ডেভেলপমেন্টে স্বাগতম। আপনার প্রথম ক্রোম এক্সটেনশন নির্মাণ এবং বিতরণ শুরু করার জন্য আপনার যা প্রয়োজন তা আবিষ্কার করুন। 
[আপনার প্রথম এক্সটেনশন তৈরি করুন](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world?hl=bn) [সব টিউটোরিয়াল দেখুন](https://developer.chrome.com/docs/extensions/get-started?hl=bn#tutorials)
###  এক্সটেনশন কি? 
ক্রোম এক্সটেনশনগুলি ব্যবহারকারীর ইন্টারফেস কাস্টমাইজ করে, ব্রাউজার ইভেন্টগুলি পর্যবেক্ষণ করে এবং ওয়েব পরিবর্তন করে ব্রাউজিং অভিজ্ঞতা উন্নত করে৷ এক্সটেনশনগুলি কী করতে পারে তার আরও উদাহরণের জন্য [Chrome ওয়েব দোকানে](https://chromewebstore.google.com/?hl=bn) যান৷ ,ক্রোম এক্সটেনশনগুলি ব্যবহারকারীর ইন্টারফেস কাস্টমাইজ করে, ব্রাউজার ইভেন্টগুলি পর্যবেক্ষণ করে এবং ওয়েব পরিবর্তন করে ব্রাউজিং অভিজ্ঞতা বাড়ায়৷ এক্সটেনশনগুলি কী করতে পারে তার আরও উদাহরণের জন্য [Chrome ওয়েব দোকানে](https://chromewebstore.google.com/?hl=bn) যান৷ 
###  তারা কিভাবে নির্মিত হয়? 
আপনি একই ওয়েব প্রযুক্তি ব্যবহার করে এক্সটেনশন তৈরি করতে পারেন যা ওয়েব অ্যাপ্লিকেশন তৈরি করতে ব্যবহৃত হয়: [HTML](https://web.dev/learn/html?hl=bn) , [CSS](https://web.dev/learn/css?hl=bn) , এবং [JavaScript](https://developer.mozilla.org/docs/Learn/JavaScript) ৷ 
###  তারা কি করতে পারে? 
[ওয়েব API](https://developer.mozilla.org/docs/Web/API) গুলি ছাড়াও, এক্সটেনশনগুলি বিভিন্ন কাজ সম্পাদন করার জন্য [Chrome এক্সটেনশন API-](https://developer.chrome.com/docs/extensions/reference?hl=bn) এ অ্যাক্সেস করে৷ আরও বিশদ ওভারভিউয়ের জন্য, [বিকাশ নির্দেশিকাটি](https://developer.chrome.com/docs/extensions/develop?hl=bn) দেখুন। , [ওয়েব এপিআই](https://developer.mozilla.org/docs/Web/API) ছাড়াও, এক্সটেনশনের বিভিন্ন কাজ সম্পন্ন করার জন্য [ক্রোম এক্সটেনশন এপিআই-এ](https://developer.chrome.com/docs/extensions/reference?hl=bn) অ্যাক্সেস রয়েছে। আরও বিশদ ওভারভিউয়ের জন্য, [বিকাশ নির্দেশিকাটি](https://developer.chrome.com/docs/extensions/develop?hl=bn) দেখুন। 
[ article  ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=bn)
###  [ উদ্ভাসিত ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=bn)
এক্সটেনশনের ম্যানিফেস্ট হল একমাত্র প্রয়োজনীয় ফাইল যার একটি নির্দিষ্ট ফাইলের নাম থাকতে হবে: manifest.json। এটি এক্সটেনশনের রুট ডিরেক্টরিতেও অবস্থিত হতে হবে। ম্যানিফেস্ট গুরুত্বপূর্ণ মেটাডেটা রেকর্ড করে, সংস্থানগুলি সংজ্ঞায়িত করে, অনুমতি ঘোষণা করে এবং পটভূমিতে এবং পৃষ্ঠায় কোন ফাইলগুলি চালাতে হবে তা চিহ্নিত করে৷ 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=bn)
###  [ সেবা কর্মীরা ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=bn)
একজন পরিষেবা কর্মী ব্যাকগ্রাউন্ডে চলে এবং ব্রাউজার ইভেন্টগুলি পরিচালনা করে, যেমন একটি বুকমার্ক সরানো, বা একটি ট্যাব বন্ধ করা। তাদের DOM-এ অ্যাক্সেস নেই, তবে আপনি এই ব্যবহারের ক্ষেত্রে একটি অফস্ক্রিন নথির সাথে এটি একত্রিত করতে পারেন। 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=bn)
###  [ বিষয়বস্তু স্ক্রিপ্ট ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=bn)
কন্টেন্ট স্ক্রিপ্ট একটি ওয়েব পৃষ্ঠার প্রসঙ্গে জাভাস্ক্রিপ্ট চালায়। 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=bn)
###  [ টুলবার অ্যাকশন ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=bn)
ব্যবহারকারী যখন এক্সটেনশন টুলবার আইকনে ক্লিক করেন বা অ্যাকশন API ব্যবহার করে একটি পপআপ দেখান তখন কোডটি চালান। ,যখন ব্যবহারকারী এক্সটেনশন টুলবার আইকনে ক্লিক করেন বা অ্যাকশন API ব্যবহার করে একটি পপআপ দেখান তখন কোড এক্সিকিউট করুন। 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=bn)
###  [ সাইড প্যানেল ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=bn)
ব্রাউজারের পাশের প্যানেলে কাস্টম UI প্রদর্শন করুন। 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=bn)
###  [ DeclarativeNetRequest ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=bn)
ইন্টারসেপ্ট, ব্লক, বা নেটওয়ার্ক অনুরোধ পরিবর্তন. 
palette 
###  একটি উচ্চ-মানের এক্সটেনশন ডিজাইন করুন 
কোন বৈশিষ্ট্যগুলিকে সমর্থন করতে হবে তা চয়ন করার সময়, নিশ্চিত করুন যে আপনার এক্সটেনশনটি একটি [একক উদ্দেশ্য](https://developer.chrome.com/docs/webstore/program-policies/quality-guidelines-faq?hl=bn) পূরণ করে যা সংক্ষিপ্তভাবে সংজ্ঞায়িত এবং বোঝা সহজ৷ ,কোন বৈশিষ্ট্যগুলিকে সমর্থন করতে হবে তা চয়ন করার সময়, নিশ্চিত করুন যে আপনার এক্সটেনশনটি একটি [একক উদ্দেশ্য](https://developer.chrome.com/docs/webstore/program-policies/quality-guidelines-faq?hl=bn) পূরণ করে যা সংকীর্ণভাবে সংজ্ঞায়িত এবং বোঝা সহজ৷ 
build 
###  নীতির সাথে পরিচিত হন 
Chrome ওয়েব স্টোরে বিতরণ করা এক্সটেনশনগুলিকে অবশ্যই [বিকাশকারী প্রোগ্রাম নীতিগুলি](https://developer.chrome.com/docs/webstore/program-policies?hl=bn) মেনে চলতে হবে৷ আপনার এক্সটেনশনটি Chrome ওয়েব স্টোরে হোস্ট করা যাবে তা নিশ্চিত করতে এই নীতিগুলি অন্বেষণ করুন৷ ,Chrome ওয়েব স্টোরে বিতরণ করা এক্সটেনশনগুলিকে অবশ্যই [বিকাশকারী প্রোগ্রাম নীতি](https://developer.chrome.com/docs/webstore/program-policies?hl=bn) মেনে চলতে হবে৷ আপনার এক্সটেনশনটি Chrome ওয়েব স্টোরে হোস্ট করা যাবে তা নিশ্চিত করতে এই নীতিগুলি অন্বেষণ করুন৷ 
cloud_off 
###  সমস্ত এক্সটেনশন যুক্তি অন্তর্ভুক্ত করুন, সমস্ত এক্সটেনশন যুক্তি অন্তর্ভুক্ত করুন 
আপনার কোড লেখার সময়, মনে রাখবেন যে সমস্ত যুক্তি অবশ্যই এক্সটেনশন প্যাকেজে অন্তর্ভুক্ত করা উচিত। এর মানে রানটাইমে কোনো অতিরিক্ত জাভাস্ক্রিপ্ট কোড ডাউনলোড করা যাবে না। [এক্সটেনশন নিরাপত্তা উন্নত করা](https://developer.chrome.com/docs/extensions/migrating/improve-security?hl=bn) দূরবর্তীভাবে হোস্ট করা কোড কার্যকর করার বিকল্প প্রদান করে। ,আপনার কোড লেখার সময়, মনে রাখবেন যে সমস্ত যুক্তি অবশ্যই এক্সটেনশন প্যাকেজে অন্তর্ভুক্ত করা উচিত। এর মানে রানটাইমে কোনো অতিরিক্ত জাভাস্ক্রিপ্ট কোড ডাউনলোড করা যাবে না। [এক্সটেনশন নিরাপত্তা উন্নত করা](https://developer.chrome.com/docs/extensions/migrating/improve-security?hl=bn) দূরবর্তীভাবে হোস্ট করা কোড কার্যকর করার বিকল্প প্রদান করে। 
code 
###  আপনার প্রথম এক্সটেনশন 
আপনার প্রথম হ্যালো ওয়ার্ল্ড এক্সটেনশন তৈরি করুন, যেখানে আপনি এক্সটেনশন উন্নয়ন কর্মপ্রবাহের সাথে পরিচিত হবেন। 
code 
###  প্রতিটি পৃষ্ঠায় স্ক্রিপ্ট চালান 
একটি নির্দিষ্ট সাইটে স্বয়ংক্রিয়ভাবে উপাদান যোগ করতে শিখুন. 
code 
###  সক্রিয় ট্যাবে স্ক্রিপ্ট ইনজেক্ট করুন 
টুলবার আইকনে ক্লিক করে বর্তমান পৃষ্ঠার শৈলী সহজ করতে শিখুন। 
code 
###  একটি ট্যাব ম্যানেজার তৈরি করুন 
আপনার ট্যাবগুলি পরিচালনা করে এমন একটি পপআপ তৈরি করতে শিখুন৷ 
code 
###  সেবা কর্মীদের সঙ্গে ঘটনা হ্যান্ডেল 
একটি এক্সটেনশন পরিষেবা কর্মী তৈরি এবং ডিবাগ করতে শিখুন৷ 
code 
###  আপনার এক্সটেনশন ডিবাগ করুন 
ডিবাগিংয়ের সময় লগ এবং ত্রুটি বার্তাগুলি খুঁজে পেতে শিখুন৷ 
[টিউটোরিয়াল শুরু করুন](https://developer.chrome.com/docs/extensions/get-started/tutorial/debug?hl=bn)

