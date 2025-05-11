---
url: https://developer.chrome.com/docs/extensions/get-started?hl=ar
title: https://developer.chrome.com/docs/extensions/get-started?hl=ar
date: 2025-05-11T16:51:51.068215
depth: 1
---

[ التخطّي إلى المحتوى الرئيسي ](https://developer.chrome.com/docs/extensions/get-started?hl=ar#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/extensions/get-started?hl=es-419)




تمت ترجمة هذه الصفحة بواسطة [Cloud Translation API‏](https://cloud.google.com/translate/?hl=ar). 


###  البدء 
مرحبًا بك في تطوير إضافات Chrome. تعرَّف على كل ما تحتاجه لبدء إنشاء إضافة Chrome الأولى وتوزيعها. 
[إنشاء أول إضافة](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world?hl=ar) [الاطّلاع على جميع الأدلة التوجيهية](https://developer.chrome.com/docs/extensions/get-started?hl=ar#tutorials)
###  ما هي الإضافات؟ 
تعمل إضافات Chrome على تحسين تجربة التصفّح من خلال تخصيص واجهة المستخدم ومراقبة أحداث المتصفّح وتعديل الويب. يمكنك الانتقال إلى [سوق Chrome الإلكتروني](https://chromewebstore.google.com/?hl=ar) للاطّلاع على المزيد من الأمثلة على ما يمكن أن تُنجزه الإضافات. 
###  كيف يتم إنشاؤها؟ 
يمكنك إنشاء إضافات باستخدام تكنولوجيات الويب نفسها المستخدَمة لإنشاء تطبيقات الويب: [HTML](https://web.dev/learn/html?hl=ar) و[CSS](https://web.dev/learn/css?hl=ar) و[JavaScript](https://developer.mozilla.org/docs/Learn/JavaScript). 
###  ما هي الإجراءات التي يمكنهم اتّخاذها؟ 
بالإضافة إلى [Web APIs](https://developer.mozilla.org/docs/Web/API)، يمكن للإضافات أيضًا الوصول إلى [واجهات برمجة تطبيقات إضافات Chrome](https://developer.chrome.com/docs/extensions/reference?hl=ar) لتنفيذ مهام مختلفة. للحصول على نظرة عامة أكثر تفصيلاً، يمكنك الاطّلاع على [دليل التطوير](https://developer.chrome.com/docs/extensions/develop?hl=ar). 
[ article  ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=ar)
###  [ البيان ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=ar)
ملف بيان الإضافة هو الملف المطلوب الوحيد الذي يجب أن يتضمّن اسم ملف محدّدًا: manifest.json. ويجب أن يكون في دليل الجذر للإضافة أيضًا. يسجِّل البيان البيانات الوصفية المهمة ويحدِّد الموارد ويوضِّح الأذونات ويحدِّد الملفات التي سيتم تشغيلها في الخلفية وعلى الصفحة. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=ar)
###  [ مشغّلو الخدمات ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=ar)
يتم تشغيل مشغّل الخدمة في الخلفية ويعالج أحداث المتصفّح، مثل إزالة إشارة مرجعية أو إغلاق علامة تبويب. لا يمكنهم الوصول إلى DOM، ولكن يمكنك دمجه مع مستند خارج الشاشة لحالة الاستخدام هذه. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=ar)
###  [ النصوص البرمجية للمحتوى ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=ar)
تعمل نصوص برمجة المحتوى على تنفيذ JavaScript في سياق صفحة ويب. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=ar)
###  [ إجراء شريط الأدوات ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=ar)
تنفيذ الرمز البرمجي عندما ينقر المستخدم على رمز شريط أدوات الإضافة أو عرض نافذة منبثقة باستخدام واجهة برمجة التطبيقات Action API 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=ar)
###  [ اللوحة الجانبية ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=ar)
عرض واجهة مستخدم مخصّصة في اللوحة الجانبية للمتصفّح 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=ar)
###  [ DeclarativeNetRequest ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=ar)
اعتراض طلبات الشبكة أو حظرها أو تعديلها 
palette 
###  تصميم إضافة عالية الجودة 
عند اختيار الميزات التي تريد توفيرها، تأكَّد من أنّ إضافتك تحقّق [غرضًا واحدًا](https://developer.chrome.com/docs/webstore/program-policies/quality-guidelines-faq?hl=ar) محدّدًا وسهل الفهم. 
build 
###  التعرّف على السياسات 
يجب أن تكون الإضافات الموزَّعة على "سوق Chrome الإلكتروني" متوافقة مع [سياسات المطوّرين](https://developer.chrome.com/docs/webstore/program-policies?hl=ar). اطّلِع على هذه السياسات للتأكّد من إمكانية استضافة إضافتك في "سوق Chrome الإلكتروني". 
cloud_off 
###  تضمين كل منطق الإضافة 
عند كتابة الرمز البرمجي، يجب أن تضع في اعتبارك أنّه يجب تضمين كل العمليات المنطقية في حزمة الإضافة. وهذا يعني أنّه لا يمكن تنزيل أي رمز JavaScript إضافي أثناء التشغيل. [تحسين أمان الإضافات](https://developer.chrome.com/docs/extensions/migrating/improve-security?hl=ar): يقدّم هذا الخيار بدائل لتنفيذ الرموز البرمجية المستضافة عن بُعد. 
code 
###  إضافة البيانات الأولى 
أنشئ أول إضافة "مرحبًا"، حيث ستتعرّف على سير عمل تطوير الإضافات. 
code 
###  تشغيل النصوص البرمجية على كل صفحة 
تعرَّف على كيفية إضافة عناصر تلقائيًا إلى موقع إلكتروني محدّد. 
code 
###  إدراج نصوص برمجية في علامة التبويب النشطة 
تعرَّف على كيفية تبسيط أسلوب الصفحة الحالية من خلال النقر على رمز شريط الأدوات. 
code 
###  إنشاء أداة إدارة علامات التبويب 
تعرَّف على كيفية إنشاء نافذة منبثقة تدير علامات التبويب. 
code 
###  معالجة الأحداث باستخدام خدمات العمل 
تعرَّف على كيفية إنشاء عامل خدمة إضافة وتصحيح أخطاءه. 
code 
###  تصحيح أخطاء الإضافة 
تعرَّف على كيفية العثور على السجلات ورسائل الخطأ أثناء تصحيح الأخطاء. 
[بدء البرنامج التعليمي](https://developer.chrome.com/docs/extensions/get-started/tutorial/debug?hl=ar)

