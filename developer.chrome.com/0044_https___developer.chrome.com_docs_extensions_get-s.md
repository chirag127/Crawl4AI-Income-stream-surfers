---
url: https://developer.chrome.com/docs/extensions/get-started?hl=ru
title: https://developer.chrome.com/docs/extensions/get-started?hl=ru
date: 2025-05-11T16:52:11.788838
depth: 1
---

[ Перейти к основному контенту ](https://developer.chrome.com/docs/extensions/get-started?hl=ru#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/extensions/get-started?hl=es-419)




Эта страница переведена с помощью [Cloud Translation API](https://cloud.google.com/translate/?hl=ru). 


###  Начать 
Добро пожаловать в разработку расширений Chrome. Узнайте все, что вам нужно, чтобы начать создавать и распространять свое первое расширение Chrome. 
[Создайте свое первое расширение](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world?hl=ru) [Посмотреть все руководства](https://developer.chrome.com/docs/extensions/get-started?hl=ru#tutorials)
###  Что такое расширения? 
Расширения Chrome улучшают работу в Интернете, настраивая пользовательский интерфейс, наблюдая за событиями браузера и изменяя Интернет. Посетите [Интернет-магазин Chrome,](https://chromewebstore.google.com/?hl=ru) чтобы узнать больше о возможностях расширений. ,Расширения Chrome улучшают работу в Интернете, настраивая пользовательский интерфейс, наблюдая за событиями браузера и изменяя Интернет. Посетите [Интернет-магазин Chrome,](https://chromewebstore.google.com/?hl=ru) чтобы узнать больше о возможностях расширений. 
###  Как они построены? 
Вы можете создавать расширения, используя те же веб-технологии, которые используются для создания веб-приложений: [HTML](https://web.dev/learn/html?hl=ru) , [CSS](https://web.dev/learn/css?hl=ru) и [JavaScript](https://developer.mozilla.org/docs/Learn/JavaScript) . 
###  Что они могут сделать? 
Помимо [веб-API](https://developer.mozilla.org/docs/Web/API) , расширения также имеют доступ к [API расширений Chrome](https://developer.chrome.com/docs/extensions/reference?hl=ru) для выполнения различных задач. Более подробный обзор можно найти в [руководстве по разработке](https://developer.chrome.com/docs/extensions/develop?hl=ru) . Помимо [веб-API](https://developer.mozilla.org/docs/Web/API) , расширения также имеют доступ к [API расширений Chrome](https://developer.chrome.com/docs/extensions/reference?hl=ru) для выполнения различных задач. Более подробный обзор можно найти в [руководстве по разработке](https://developer.chrome.com/docs/extensions/develop?hl=ru) . 
[ article  ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=ru)
###  [ Манифест ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=ru)
Манифест расширения — единственный обязательный файл, который должен иметь определенное имя файла: Manifest.json. Он также должен находиться в корневом каталоге расширения. Манифест записывает важные метаданные, определяет ресурсы, объявляет разрешения и определяет, какие файлы запускать в фоновом режиме и на странице. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=ru)
###  [ Работники сферы обслуживания ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=ru)
Сервис-воркер работает в фоновом режиме и обрабатывает события браузера, такие как удаление закладки или закрытие вкладки. У них нет доступа к DOM, но для этого варианта использования вы можете объединить его с закадровым документом. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=ru)
###  [ Скрипты контента ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=ru)
Сценарии содержимого запускают JavaScript в контексте веб-страницы. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=ru)
###  [ Действие панели инструментов ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=ru)
Выполнять код, когда пользователь нажимает значок расширения на панели инструментов, или отображать всплывающее окно с помощью Action API. ,Выполнять код, когда пользователь нажимает на значок расширения на панели инструментов или отображает всплывающее окно с помощью Action API. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=ru)
###  [ Боковая панель ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=ru)
Отображение пользовательского интерфейса на боковой панели браузера. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=ru)
###  [ ДекларативныйNetRequest ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=ru)
Перехватывайте, блокируйте или изменяйте сетевые запросы. 
palette 
###  Создайте качественное расширение 
Выбирая, какие функции поддерживать, убедитесь, что ваше расширение выполняет [единую цель](https://developer.chrome.com/docs/webstore/program-policies/quality-guidelines-faq?hl=ru) , которая четко определена и проста для понимания. ,Выбирая, какие функции поддерживать, убедитесь, что ваше расширение выполняет [единую цель](https://developer.chrome.com/docs/webstore/program-policies/quality-guidelines-faq?hl=ru) , которая четко определена и проста для понимания. 
build 
###  Ознакомьтесь с политикой 
Расширения, распространяемые в Интернет-магазине Chrome, должны соответствовать [правилам программы для разработчиков](https://developer.chrome.com/docs/webstore/program-policies?hl=ru) . Изучите эти правила, чтобы убедиться, что ваше расширение может быть размещено в Интернет-магазине Chrome. ,Расширения, распространяемые в Интернет-магазине Chrome, должны соответствовать [правилам программы для разработчиков](https://developer.chrome.com/docs/webstore/program-policies?hl=ru) . Изучите эти правила, чтобы убедиться, что ваше расширение может быть размещено в Интернет-магазине Chrome. 
cloud_off 
###  Включить всю логику расширения 
При написании кода имейте в виду, что вся логика должна быть включена в пакет расширения. Это означает, что во время выполнения нельзя загружать дополнительный код JavaScript. [Повышение безопасности расширений](https://developer.chrome.com/docs/extensions/migrating/improve-security?hl=ru) предоставляет альтернативу удаленному выполнению кода. 
code 
###  Ваше первое расширение 
Создайте свое первое расширение hello world, где вы познакомитесь с рабочим процессом разработки расширения. 
code 
###  Запуск скриптов на каждой странице 
Научитесь автоматически добавлять элементы на указанный сайт. 
code 
###  Внедрить скрипты в активную вкладку 
Узнайте, как упростить стиль текущей страницы, щелкнув значок на панели инструментов. 
code 
###  Создать менеджер вкладок 
Научитесь создавать всплывающее окно, которое управляет вашими вкладками. 
code 
###  Обработка событий с помощью сервисных работников 
Научитесь создавать и отлаживать работника службы расширений. 
code 
###  Отладка вашего расширения 
Научитесь находить журналы и сообщения об ошибках во время отладки. 

