---
url: https://developer.chrome.com/blog/how-photoshop-solved-working-with-files-larger-than-can-fit-into-memory?hl=en
title: https://developer.chrome.com/blog/how-photoshop-solved-working-with-files-larger-than-can-fit-into-memory?hl=en
date: 2025-05-11T16:56:25.834963
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/how-photoshop-solved-working-with-files-larger-than-can-fit-into-memory?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/how-photoshop-solved-working-with-files-larger-than-can-fit-into-memory?hl=es-419)




  * On this page
  * [Acknowledgements](https://developer.chrome.com/blog/how-photoshop-solved-working-with-files-larger-than-can-fit-into-memory?hl=en#acknowledgements)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  How Photoshop solved working with files larger than can fit into memory 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Acknowledgements](https://developer.chrome.com/blog/how-photoshop-solved-working-with-files-larger-than-can-fit-into-memory?hl=en#acknowledgements)


Learn how Adobe managed to let users edit even the biggest files on the web version of its iconic Photoshop app.
Nabeel Al-Shamma 
[ GitHub ](https://github.com/alshamma) [ LinkedIn ](https://www.linkedin.com/in/https://www.linkedin.com/in/alshamma/)
Thomas Steiner 
[ GitHub ](https://github.com/tomayac) [ Glitch ](https://glitch.com/@tomayac) [ LinkedIn ](https://www.linkedin.com/in/thomassteinerlinkedin) [ Mastodon ](https://toot.cafe/@tomayac) [ Bluesky ](https://bsky.app/profile/tomayac.com) [ Homepage ](https://blog.tomayac.com/)
## Introduction
(This article is also available in form of a video.)
In 2021, Adobe, together with Chrome engineering, [brought a version of Photoshop to the web](https://web.dev/articles/ps-on-the-web). The software makes innovative use of WebAssembly with features like [SIMD](https://v8.dev/features/simd), high performance storage in the [origin private file system](https://developer.chrome.com/articles/file-system-access#accessing-the-origin-private-file-system), the [P3 color space](https://developer.mozilla.org/docs/Web/API/HTMLCanvasElement/getContext#colorspace) for canvas, and Web Components with [Lit](https://lit.dev/). In this article, we want to focus on how Adobe Photoshop engineering solved working with files larger than can fit into memory. And, in the case of WebAssembly, how Photoshop works with files larger than the 32-bit address space of wasm32.
## The problem
Opening a file for editing requires a large amount of memory, significantly more than opening a file for viewing. The files edited in Photoshop often require more memory than a user has available on their device, due to the many features offered by the software, the types of digital design and editing it is used for, and the capabilities of user devices.
The [Photoshop file format](https://helpx.adobe.com/photoshop/using/file-formats.html#photoshop_format_psd) stores data with lossless compression. When a file or document is read, all of the image data is decompressed to allow for more efficient processing. As a result, the amount of memory required can be several times more than the amount of space a document uses on disk or in cloud storage.
Photoshop supports a very large undo history. Many operations in Photoshop are what we call destructive operations. That is, making an edit such as painting with a brush will result in new pixel data which can be just as large as the original pixel data. Making these edits in a long editing session yields large amounts of pixel data that must be kept around to support undo operations. Thus, the history can grow to several hundred megabytes or many gigabytes of data.
Devices and platforms, be they desktop machines, mobile devices or browsers, all manage memory. Some are more generous than others in how much memory they make available to applications. The amount of memory also varies from device to device, as you know when you order a new computer or device and specify the amount of [Random-Access Memory](https://en.wikipedia.org/wiki/Random-access_memory) (RAM) desired. Many of these platforms also support [virtual memory](https://en.wikipedia.org/wiki/Virtual_memory), which allows an application to use more memory than is physically available. This support varies by operating system and runtime, as in the case of WebAssembly, may not be readily accessible or usable by applications. On top of that, modern virtual systems have upper limits that are easily exceeded by Photoshop requirements.
Ideally, applications would use as much memory as they need. This generally allows them to provide the best performance to their users. However, if they use too much memory, they may be penalized by the runtime platform or may run out of memory, resulting in failures.
As a historical note, the original problem that Photoshop needed to solve was editing print resolution files on early versions of macOS, as low as 1 MB for the OS and all applications. A 300 dpi full page image in CMYK is approximately 32 MB uncompressed.
## The solution
To solve the problem of the app exceeding the available amount of RAM, Photoshop implemented a software virtual memory system (VM). Photoshop uses its VM to manage document data, especially image data, all of the undo history and state, as well as the working storage for the current command. It is also used for caching large blocks of data such as brush descriptions so that they only need to be serialized from disk once.
As an example of one of the aspects managed by the VM, image data is stored using a [mipmap](https://en.wikipedia.org/wiki/Mipmap) representation, which is a pyramidal set of tiles, providing image data at a range of low to high resolutions. This allows Photoshop to operate on the appropriate resolution data for quicker response when zoomed in or looking at a preview, versus zoomed out.
During application initialization, Photoshop determines how much RAM is available. It sets aside one portion for data to be stored in the VM. The remaining RAM is available for other application needs via the standard C++ runtime library. The VM memory is broken up into [pages](https://en.wikipedia.org/wiki/Page_\(computer_memory\)). Each page is typically a multiple of the hardware page size for the device. When used for image data, memory is referenced as tiles. A tile is a square area of pixels of a single layer including geometry bounds. A tile consumes one or more pages.
Photoshop creates one or more scratch files to provide disk-based backing for VM pages. These scratch files are stored in the [origin private file system](https://developer.chrome.com/articles/file-system-access#accessing-the-origin-private-file-system). The screenshot shows an exemplary file hierarchy of such a scratch file (highlighted in yellow) and other files during an image editing session. Each scratch file can contain many VM pages. When the VM needs more backing, it creates additional scratch files. As pages are freed, their space in a scratch file can be reused for new pages.
When processing image data, Photoshop iterates over tiles, performing pixel calculations. Each calculation can reference multiple tiles. The VM is responsible for ensuring that source and destination tiles for the current iteration are in memory, loading them from scratch files as required. At the same time, it can flush pages to the scratch files to make room in memory.
## Conclusions
While the concrete implementation details of the VM would go far beyond the scope of this document (and are also proprietary to Adobe), with the high-level description of the solution, we have put you in a position where you can understand how Photoshop can deal with large files. The origin private file system with its highly performant read and write access to files is a key component of the solution.
## Acknowledgements
This blog post was reviewed by Oliver Unter Ecker and Rachel Andrew. Special thanks to Russell Williams for his excellent documentation on the Photoshop VM.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2023-06-05 UTC.

