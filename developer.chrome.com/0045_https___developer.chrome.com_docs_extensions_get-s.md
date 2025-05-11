---
url: https://developer.chrome.com/docs/extensions/get-started?hl=zh-cn
title: https://developer.chrome.com/docs/extensions/get-started?hl=zh-cn
date: 2025-05-11T16:52:12.390238
depth: 1
---

[ 跳至主要内容 ](https://developer.chrome.com/docs/extensions/get-started?hl=zh-cn#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/extensions/get-started?hl=es-419)

登录


此页面由 [Cloud Translation API](https://cloud.google.com/translate/?hl=zh-cn) 翻译。 


###  开始使用 
欢迎开始学习 Chrome 扩展程序开发。了解开始构建和分发首个 Chrome 扩展程序所需的一切信息。 
###  什么是扩展程序？ 
Chrome 扩展程序可通过自定义界面、监控浏览器事件和修改网页来提升浏览体验。如需查看更多扩展程序功能示例，请访问 [Chrome 应用商店](https://chromewebstore.google.com/?hl=zh-cn)。 
###  它们是如何构建的？ 
您可以使用创建 Web 应用时所用的 Web 技术构建扩展程序：[HTML](https://web.dev/learn/html?hl=zh-cn)、[CSS](https://web.dev/learn/css?hl=zh-cn) 和 [JavaScript](https://developer.mozilla.org/docs/Learn/JavaScript)。 
###  他们可以做些什么？ 
除了 [Web API](https://developer.mozilla.org/docs/Web/API) 之外，扩展程序还可以使用 [Chrome 扩展程序 API](https://developer.chrome.com/docs/extensions/reference?hl=zh-cn) 来执行不同的任务。如需更加详细的信息，请参阅[开发指南](https://developer.chrome.com/docs/extensions/develop?hl=zh-cn)。 
[ article  ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=zh-cn)
扩展程序的清单是唯一必须具有特定文件名（即 manifest.json）的必需文件。它还必须位于扩展程序的根目录中。清单会记录重要元数据、定义资源、声明权限，并确定要在后台和网页上运行哪些文件。 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=zh-cn)
###  [ Service Worker ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=zh-cn)
服务工件在后台运行，并处理浏览器事件，例如移除书签或关闭标签页。它们无法访问 DOM，但您可以将其与屏幕外文档结合使用来实现此用例。 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=zh-cn)
内容脚本会在网页上下文中运行 JavaScript。 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=zh-cn)
###  [ 工具栏操作 ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=zh-cn)
在用户点击扩展程序工具栏图标时执行代码，或使用 Action API 显示弹出式窗口。 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=zh-cn)
在浏览器的侧边栏中显示自定义界面。 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=zh-cn)
###  [ DeclarativeNetRequest ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=zh-cn)
拦截、屏蔽或修改网络请求。 
palette 
###  设计高质量的扩展程序 
在选择要支持哪些功能时，请确保您的扩展程序具有明确定义且易于理解的[单一用途](https://developer.chrome.com/docs/webstore/program-policies/quality-guidelines-faq?hl=zh-cn)。 
build 
###  熟悉相关政策 
在 Chrome 网上应用店中分发的扩展程序必须遵守[开发者计划政策](https://developer.chrome.com/docs/webstore/program-policies?hl=zh-cn)。请查看以下政策，确保您的扩展程序可以托管在 Chrome 应用商店中。 
cloud_off 
###  包含所有扩展程序逻辑 
编写代码时，请注意扩展程序软件包中必须包含所有逻辑。这意味着，在运行时不得下载任何其他 JavaScript 代码。[提高扩展程序安全性](https://developer.chrome.com/docs/extensions/migrating/improve-security?hl=zh-cn)提供了执行远程托管代码的替代方案。 
code 
###  您的首个扩展程序 
创建您的第一个“Hello World”扩展程序，熟悉扩展程序开发工作流。 
code 
###  在每个网页上运行脚本 
了解如何自动向指定网站添加元素。 
code 
###  将脚本注入到当前活动的标签页中 
了解如何通过点击工具栏图标来简化当前网页的样式。 
code 
###  创建标签页管理器 
了解如何创建用于管理标签页的弹出式窗口。 
code 
###  使用 Service Worker 处理事件 
了解如何创建和调试扩展程序服务工作器。 
code 
###  调试扩展程序 
了解如何在调试期间查找日志和错误消息。 

