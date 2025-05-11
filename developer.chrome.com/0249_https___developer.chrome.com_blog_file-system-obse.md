---
url: https://developer.chrome.com/blog/file-system-observer?hl=en
title: https://developer.chrome.com/blog/file-system-observer?hl=en
date: 2025-05-11T16:56:02.799435
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/file-system-observer?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/file-system-observer?hl=es-419)




  * On this page
  * [How to use the File System Observer API](https://developer.chrome.com/blog/file-system-observer?hl=en#how_to_use_the_file_system_observer_api)
    * [Feature detection](https://developer.chrome.com/blog/file-system-observer?hl=en#feature_detection)
    * [Initialize a file system observer](https://developer.chrome.com/blog/file-system-observer?hl=en#initialize_a_file_system_observer)
    * [Start observing a file or directory](https://developer.chrome.com/blog/file-system-observer?hl=en#start_observing_a_file_or_directory)
    * [The callback function](https://developer.chrome.com/blog/file-system-observer?hl=en#the-callback-function)
    * [Stop observing a file or directory](https://developer.chrome.com/blog/file-system-observer?hl=en#stop_observing_a_file_or_directory)
    * [Stop observing the file system](https://developer.chrome.com/blog/file-system-observer?hl=en#stop-observing-the-file-system)
  * [Acknowledgements](https://developer.chrome.com/blog/file-system-observer?hl=en#acknowledgements)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  The File System Observer API origin trial 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [How to use the File System Observer API](https://developer.chrome.com/blog/file-system-observer?hl=en#how_to_use_the_file_system_observer_api)
    * [Feature detection](https://developer.chrome.com/blog/file-system-observer?hl=en#feature_detection)
    * [Initialize a file system observer](https://developer.chrome.com/blog/file-system-observer?hl=en#initialize_a_file_system_observer)
    * [Start observing a file or directory](https://developer.chrome.com/blog/file-system-observer?hl=en#start_observing_a_file_or_directory)
    * [The callback function](https://developer.chrome.com/blog/file-system-observer?hl=en#the-callback-function)
    * [Stop observing a file or directory](https://developer.chrome.com/blog/file-system-observer?hl=en#stop_observing_a_file_or_directory)
    * [Stop observing the file system](https://developer.chrome.com/blog/file-system-observer?hl=en#stop-observing-the-file-system)
  * [Acknowledgements](https://developer.chrome.com/blog/file-system-observer?hl=en#acknowledgements)


Thomas Steiner 
[ GitHub ](https://github.com/tomayac) [ Glitch ](https://glitch.com/@tomayac) [ LinkedIn ](https://www.linkedin.com/in/thomassteinerlinkedin) [ Mastodon ](https://toot.cafe/@tomayac) [ Bluesky ](https://bsky.app/profile/tomayac.com) [ Homepage ](https://blog.tomayac.com/)
The [File System Access API](https://developer.chrome.com/docs/capabilities/web-apis/file-system-access) and the [Origin Private File System API](https://web.dev/articles/origin-private-file-system) both allow developers to access files and directories on the user's device. The former lets developers read and write to the regular, user-visible file system, and the latter opens up a special, hidden from the user file system that is private to the [origin](https://developer.mozilla.org/docs/Glossary/Origin) of each site and that comes with certain performance advantages. The way developers interact with files and directories in both cases is through [`FileSystemHandle`](https://developer.mozilla.org/docs/Web/API/FileSystemHandle) objects, more concretely, [`FileSystemFileHandle`](https://developer.mozilla.org/docs/Web/API/FileSystemFileHandle) for files, and [`FileSystemDirectoryHandle`](https://developer.mozilla.org/docs/Web/API/FileSystemDirectoryHandle) for directories. Up until now, being informed of changes to a file or directory in either of the file systems required some form of polling and comparing the `lastModified` timestamp or even the file contents itself.
The File System Observer API, in origin trial from Chrome 129, changes that, and lets developers be alerted automatically when changes happen. This guide explains how it works and how to try the feature.
## Use cases
Use the File System Observer API in apps that need to be informed of possible file system changes as soon as they happen.
  * Web-based integrated development environments (IDEs) that show a representation of a project's file system tree.
  * Apps that synchronize file system changes with a server. For example, a SQLite database file.
  * Apps that need to notify the main thread of file system changes from a worker or another tab.
  * Apps that observe a directory of resources, for example, to automatically optimize images.
  * Experiences that profit from hot-reloading, like HTML-based slide decks where a reload gets triggered by a file change.


## How to use the File System Observer API
### Feature detection
To see if the File System Observer API is supported, run a feature test as in the following example.
```
if('FileSystemObserver'inself){
// The File System Observer API is supported.
}

```

### Initialize a file system observer
Initialize a File System Observer by calling `new FileSystemObserver()`, providing it a [`callback` function](https://developer.chrome.com/blog/file-system-observer?hl=en#the-callback-function) as an argument.
```
constobserver=newFileSystemObserver(callback);

```

### Start observing a file or directory
To begin observing a file or directory, call the asynchronous `observe()` method of the `FileSystemObserver` instance. Provide this method the `FileSystemHandle` of the selected file or directory as an argument. When observing a directory, there's an optional `options` argument that lets you choose if you want to be informed of changes to the directory recursively (that is, for the directory itself and _all_ contained subdirectories and files). The default option is to only observe the directory itself and the directly contained files.
```
// Observe a file.
awaitobserver.observe(fileHandle);
// Observe a directory.
awaitobserver.observe(directoryHandle);
// Observe a directory recursively.
awaitobserver.observe(directoryHandle,{recursive:true});

```

### The callback function
When changes to the file system happen, a callback function is called with the [file system change `records`](https://developer.chrome.com/blog/file-system-observer?hl=en#the-file-system-change-record) and the `observer` itself as its arguments. You can use the `observer` argument to, for example, disconnect the observer (see [Stop observing the file system](https://developer.chrome.com/blog/file-system-observer?hl=en#stop-observing-the-file-system)) when the files you're interested in are all deleted.
```
constcallback=(records,observer)=>{
for(constrecordofrecords){
console.log('Change detected',record);
}
};

```

#### The file system change record
Each file system change record has the following structure. All fields are read-only.
  * `root` (a `FileSystemHandle`): The handle passed to the `FileSystemObserver.observe()` function.
  * `changedHandle` (a `FileSystemHandle`): The handle affected by the file system change. This field will be `null` for `"errored"`, `"unknown"`, and `"disappeared"` type events. To see which file or directory has disappeared, use `relativePathComponents`.
  * `relativePathComponents` (an `Array`): The path of the `changedHandle` relative to the `root`.
  * `type` (a `String`): The type of the change. The following types are possible: 
    * `"appeared"`: The file or directory was created or got moved into the `root`.
    * `"disappeared"`: The file or directory was deleted or got moved out of the `root`.
    * `"modified"`: The file or directory was modified.
    * `"moved"`: The file or directory was moved within the `root`.
    * `"unknown"`: This indicates that zero or more events were missed. Developers should poll the watched directory in response to this.
    * `"errored"`: The observation is no longer valid. In this case, you may want to [stop observing the file system](https://developer.chrome.com/blog/file-system-observer?hl=en#stop-observing-the-file-system). This value will also be sent when the maximum limit of per-origin observations is reached. This limit is dependent on the operating system and not known beforehand. If this happens, the site may decide to retry, though there's no guarantee that the operating system has freed up enough resources. Another case for when this value will be sent is when the observed handle (that is, the root of the observation) is deleted or moved. In this case, first, the `"disappeared"` event is sent, followed by an `"errored"` event, indicating that the observation is no longer valid. Finally, this event is sent when permission to the directory or file handle is removed.
  * `relativePathMovedFrom` (an `Array`, optional): The former location of a moved handle. Available only when the `type` is `"moved"`.


### Stop observing a file or directory
To stop observing a `FileSystemHandle`, call the `unobserve()` method, passing it the handle as an argument.
```
observer.unobserve(fileHandle);

```

### Stop observing the file system
To stop observing the file system, disconnect the `FileSystemObserver` instance as follows.
```
observer.disconnect();

```

## Try the API
To test the File System Observer API locally, set the `#file-system-observer` flag in `about:flags`. To test the API with real users, [sign up](https://developer.chrome.com/origintrials#/view_trial/59109745109237761) for the origin trial and follow the instructions as per the guide [Chrome Origin Trials](https://developer.chrome.com/docs/web-platform/origin-trials). The origin trial will run from Chrome 129 (September 11, 2024) to Chrome 134 (February 26, 2025).
## Demo
You can see the File System Observer API in action in the embedded [demo](https://file-system-observer.glitch.me/). Check out the [source code](https://glitch.com/edit/#!/file-system-observer?path=observer.js) or remix the demo code on Glitch. The demo randomly creates, deletes, or modifies files in an observed directory and logs its activity in the upper part of the app window. It then logs the changes as they occur in the lower part of the app window. If you read this on a browser that doesn't support the File System Observer API, see a [screenshot](https://developer.chrome.com/static/blog/file-system-observer/fso.png) of the demo.
## Feedback
If you have feedback on the shape of the File System Observer API, comment on [Issue #123 in the WHATWG/fs](https://github.com/whatwg/fs/issues/123) repository.
## Relevant links
  * [Mozilla Standards Position](https://github.com/mozilla/standards-positions/issues/942)
  * [WebKit Standards Position](https://github.com/WebKit/standards-positions/issues/291)


## Acknowledgements
This document was reviewed by [Daseul Lee](https://www.linkedin.com/in/daseul-lee-8297314b/), [Nathan Memmott](https://www.linkedin.com/in/nathan-memmott), [Etienne Noël](https://www.linkedin.com/in/enoel19/), and [Rachel Andrew](https://rachelandrew.co.uk/).
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-08-20 UTC.

