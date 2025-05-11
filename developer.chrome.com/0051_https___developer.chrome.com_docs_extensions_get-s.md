---
url: https://developer.chrome.com/docs/extensions/get-started?hl=zh-tw
title: https://developer.chrome.com/docs/extensions/get-started?hl=zh-tw
date: 2025-05-11T16:52:19.760669
depth: 1
---

[ 跳至主要內容 ](https://developer.chrome.com/docs/extensions/get-started?hl=zh-tw#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/extensions/get-started?hl=es-419)




本頁面由 [Cloud Translation API](https://cloud.google.com/translate/?hl=zh-tw) 翻譯而成。 


###  開始使用 
歡迎使用 Chrome 擴充功能開發服務。瞭解建構及發布第一個 Chrome 擴充功能所需的一切。 
###  什麼是擴充功能？ 
Chrome 擴充功能可自訂使用者介面、觀察瀏覽器事件，以及修改網頁，進而提升瀏覽體驗。如要查看更多擴充功能的範例，請前往 [Chrome 線上應用程式商店](https://chromewebstore.google.com/?hl=zh-tw)。 
###  這些廣告單元是如何建立的？ 
您可以使用用於建立網頁應用程式的相同網頁技術來建構擴充功能，包括 [HTML](https://web.dev/learn/html?hl=zh-tw)、[CSS](https://web.dev/learn/css?hl=zh-tw) 和 [JavaScript](https://developer.mozilla.org/docs/Learn/JavaScript)。 
###  他們可以採取哪些行動？ 
除了[Web API](https://developer.mozilla.org/docs/Web/API)，擴充功能還可以存取 [Chrome 擴充功能 API](https://developer.chrome.com/docs/extensions/reference?hl=zh-tw)，以便執行各種工作。如需更詳細的概略說明，請參閱[開發指南](https://developer.chrome.com/docs/extensions/develop?hl=zh-tw)。 
[ article  ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=zh-tw)
擴充功能的資訊清單是唯一必須具備特定檔案名稱的必填檔案：manifest.json。且必須位於擴充功能的根目錄中。資訊清單會記錄重要中繼資料、定義資源、宣告權限，以及識別要在背景和頁面上執行的檔案。 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=zh-tw)
###  [ Service Worker ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=zh-tw)
Service Worker 會在背景執行，並處理瀏覽器事件，例如移除書籤或關閉分頁。這類應用程式無法存取 DOM，但您可以將 DOM 與螢幕外文件結合，以便用於此用途。 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=zh-tw)
###  [ 內容指令碼 ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=zh-tw)
內容指令碼會在網頁的環境中執行 JavaScript。 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=zh-tw)
###  [ 工具列動作 ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=zh-tw)
在使用者點選擴充功能工具列圖示或使用 Action API 顯示彈出式視窗時執行程式碼。 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=zh-tw)
在瀏覽器的側邊面板中顯示自訂 UI。 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=zh-tw)
###  [ DeclarativeNetRequest ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=zh-tw)
攔截、封鎖或修改網路要求。 
palette 
###  設計高品質的擴充功能 
選擇要支援的功能時，請確保擴充功能可滿足[單一用途](https://developer.chrome.com/docs/webstore/program-policies/quality-guidelines-faq?hl=zh-tw)，且該用途已明確定義且易於理解。 
build 
###  熟悉政策 
在 Chrome 線上應用程式商店發布的擴充功能必須遵守[開發人員計畫政策](https://developer.chrome.com/docs/webstore/program-policies?hl=zh-tw)。請詳閱這些政策，確保您的擴充功能可由 Chrome 線上應用程式商店代管。 
cloud_off 
###  納入所有擴充功能邏輯 
編寫程式碼時，請務必將所有邏輯納入擴充功能套件中。也就是說，執行階段不會下載任何額外的 JavaScript 程式碼。[改善擴充功能安全性](https://developer.chrome.com/docs/extensions/migrating/improve-security?hl=zh-tw)提供執行遠端代管程式的替代方案。 
code 
###  第一個擴充功能 
建立第一個 Hello World 擴充功能，熟悉擴充功能開發工作流程。 
code 
###  在每個網頁上執行指令碼 
瞭解如何自動將元素新增至指定網站。 
code 
###  將指令碼插入使用中的分頁 
瞭解如何按一下工具列圖示，簡化目前網頁的樣式。 
code 
###  建立分頁管理工具 
瞭解如何建立用於管理分頁的彈出式視窗。 
code 
###  使用服務工作程處理事件 
瞭解如何建立及偵錯擴充功能服務 worker。 
code 
###  對擴充功能進行偵錯 
瞭解如何在偵錯期間查看記錄和錯誤訊息。 

