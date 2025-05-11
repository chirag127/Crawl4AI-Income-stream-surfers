---
url: https://developer.chrome.com/blog/how-construct3-uses-the-file-system-access-api?hl=en
title: https://developer.chrome.com/blog/how-construct3-uses-the-file-system-access-api?hl=en
date: 2025-05-11T16:56:14.910626
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/how-construct3-uses-the-file-system-access-api?hl=en#main-content)


  * On this page
  * [The File System Access API in Construct 3](https://developer.chrome.com/blog/how-construct3-uses-the-file-system-access-api?hl=en#the_file_system_access_api_in_construct_3)
    * [Working with large files and folders](https://developer.chrome.com/blog/how-construct3-uses-the-file-system-access-api?hl=en#working_with_large_files_and_folders)
    * [Continue where you left off](https://developer.chrome.com/blog/how-construct3-uses-the-file-system-access-api?hl=en#continue_where_you_left_off)
    * [Drag and drop integration](https://developer.chrome.com/blog/how-construct3-uses-the-file-system-access-api?hl=en#drag_and_drop_integration)
  * [Retired NW.js build](https://developer.chrome.com/blog/how-construct3-uses-the-file-system-access-api?hl=en#retired_nwjs_build)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  How the game editor Construct 3 uses the File System Access API to let users save their games 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [The File System Access API in Construct 3](https://developer.chrome.com/blog/how-construct3-uses-the-file-system-access-api?hl=en#the_file_system_access_api_in_construct_3)
    * [Working with large files and folders](https://developer.chrome.com/blog/how-construct3-uses-the-file-system-access-api?hl=en#working_with_large_files_and_folders)
    * [Continue where you left off](https://developer.chrome.com/blog/how-construct3-uses-the-file-system-access-api?hl=en#continue_where_you_left_off)
    * [Drag and drop integration](https://developer.chrome.com/blog/how-construct3-uses-the-file-system-access-api?hl=en#drag_and_drop_integration)
  * [Retired NW.js build](https://developer.chrome.com/blog/how-construct3-uses-the-file-system-access-api?hl=en#retired_nwjs_build)


The File System Access API allows read, write, and file management capabilities. Learn how Construct 3 makes use of this API.
Thomas Steiner 
[ GitHub ](https://github.com/tomayac) [ Glitch ](https://glitch.com/@tomayac) [ LinkedIn ](https://www.linkedin.com/in/thomassteinerlinkedin) [ Mastodon ](https://toot.cafe/@tomayac) [ Bluesky ](https://bsky.app/profile/tomayac.com) [ Homepage ](https://blog.tomayac.com/)
Ashley Gullen 
[ Mastodon ](https://mastodon.gamedev.place/@AshleyGullen)
## Introduction
(This article is also available in form of a video.)
[Construct 3](https://www.construct.net/en/make-games/free-trial) is a game editor developed by the brothers [Thomas and Ashley Gullen](https://www.starterstory.com/stories/we-created-a-100k-month-no-code-tool-for-video-game-developers). For the present third iteration of their game editor, the two fully _"[bet] on the browser being the new operating system"_ after building for Windows and [NW.js](https://nwjs.io/) before. You can get an impression of some games developed with the editor by exploring its [showcase](https://www.construct.net/en/make-games/showcase) or working through the [guided tour](https://editor.construct.net/?startTour). Thanks to the superpowers of the web, you can also just click through to any of the ["Get inspired" examples](https://www.construct.net/en/make-games/free-trial#:%7E:text=the%20Guided%20Tour-,Get%20inspired,-OPEN%20AND%20EDIT) and start editing immediately.
## The File System Access API in Construct 3
Construct provides the option of saving to local files with the [File System Access API](https://developer.mozilla.org/docs/Web/API/File_System_Access_API), as well as cloud save (Google Drive, OneDrive, Dropbox), and downloading of a copy of the project file. Stats the Construct developers have collected show that 65% of saves are done with the File System Access API, which demonstrates it's what most customers want to use.
For saving, the following snippet shows the original production code for obtaining a [`FileSystemFileHandle`](https://developer.mozilla.org/docs/Web/API/FileSystemFileHandle) from the [`showSaveFilePicker()`](https://developer.mozilla.org/docs/Web/API/Window/showSaveFilePicker) method, which then serves to save the actual data. Construct makes use of the `id` options parameter. The `id` field can be specified to suggest the directory in which the file picker opens. By specifying an `id`, the browser can remember different directories for different IDs, which serves to start the dialog consistently in the same directory depending on the ID. For example, level files could open in `Documents/levels/`, whereas texture files could open in `Images/textures/`. The `types` parameter is an array of supported file types with a localized user-visual `description` and an `accept` object that tells the operating system to initially only accept `.c3p` files with the MIME type `application/x-construct3-project`.
```
letfileHandle=null;
try{
fileHandle=awaitwindow["showSaveFilePicker"]({
id:"save-project-file",
types:[
{
description:lang("ui.project-file-picker.c3-single-file-project"),
accept:{
"application/x-construct3-project":[".c3p"],
},
},
],
});
}catch(err){
// Assume user cancelled, or permission otherwise denied.
return;
}

```

The Construct team have found working with files on the user's file system to be very intuitive. It works similarly to traditional desktop apps, and integrates conveniently with other software. For example, backup software that can make backups of users' files, or for easily sending work to other places, or editing files with external tools. They also use the File System Access API for various other use cases, such as selecting a backup folder or importing assets like animations.
### Working with large files and folders
Some of Construct's customers work with very large projects, in the hundreds of megabytes. Saving such a large amount of work to a single file is painfully slow, let alone uploading it to a cloud service. The File System Access API lets power users work with a local folder with all their assets in separate files. This allows for very fast saves, as only the changed files need to be updated.
### Continue where you left off
Both file and directory handles can be serialized to IndexedDB, allowing Construct to provide a recent projects list that is persisted across sessions, so users can access the same file or folder again, which is a great convenience to the user. In fact, about 30% of all projects opened in Construct are opened this way. The following screenshot shows two recent projects, `tetris.c3p` and `columns.c3p` and, in the DevTools window, the corresponding `FileSystemFileHandle` objects serialized in an IndexedDB table.
### Drag and drop integration
The File System Access API also integrates with the [Drag and Drop API](https://developer.mozilla.org/docs/Web/API/HTML_Drag_and_Drop_API), so the user can drag and drop `.c3p` files onto the application. Construct can then via the [`getAsFileSystemHandle()`](https://developer.mozilla.org/docs/Web/API/DataTransferItem/getAsFileSystemHandle) method on the `DataTransferItem` object obtain a [`FileSystemFileHandle`](https://developer.mozilla.org/docs/Web/API/FileSystemFileHandle), which means files opened this way can be edited and saved immediately, without having to go through a separate file save dialog.
## Retired NW.js build
Previously, the team had an [NW.js](https://nwjs.io/) build of Construct that needed maintaining and updating separately to access local files. After Chromium added support for the File System Access API in version 84, the Construct developers [implemented the API in 2020](https://www.construct.net/en/blogs/construct-official-blog-1/local-file-folder-saves-1555), and as a by-product were able to retire the NW.js build and use the browser exclusively on all platforms. This simplifies development and avoids the need to bundle the browser engine with the app.
## Conclusions
Construct makes heavy use of the three picker methods `showOpenFilePicker()`, `showSaveFilePicker()`, and `showOpenDirectoryPicker()` respectively to the benefit of their users who have learned to depend on this way of working with Construct. As an additional benefit, Construct also uses the [File Handling API](https://developer.chrome.com/articles/file-handling), which allows Construct 3 to register itself as a (default) file handler of `.c3p` files. This means that the user can doubleclick or right-click and open with Construct 3 their game files right from the file explorer of their operating system. Fully betting on the web, Construct uses loads of other modern browser APIs—like WebGL, Web Audio, Web Workers, WebAssembly, WebRTC for multiplayer games, Local Font Access, WebCodecs for their [new animation product](https://www.construct.net/en/animation-software), and even more. Their goal has always been to make full use of the web platform and show how great products can be built on top of it, so be sure to [try their guided tour](https://editor.construct.net/?startTour) and create your own games.
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2023-05-30 UTC.

