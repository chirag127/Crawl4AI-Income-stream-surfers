---
url: https://developer.chrome.com/docs/extensions/get-started?hl=he
title: https://developer.chrome.com/docs/extensions/get-started?hl=he
date: 2025-05-11T16:52:02.887067
depth: 1
---

[ דילוג לתוכן הראשי ](https://developer.chrome.com/docs/extensions/get-started?hl=he#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/extensions/get-started?hl=es-419)




דף זה תורגם על ידי [Cloud Translation API](https://cloud.google.com/translate/?hl=he). 


###  מתחילים 
אנחנו שמחים שהגעת לדף הזה בנושא פיתוח תוספים ל-Chrome. כאן תמצאו את כל מה שצריך כדי להתחיל לפתח ולהפיץ את תוסף Chrome הראשון שלכם. 
[פיתוח התוסף הראשון](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world?hl=he) [הצגת כל המדריכים](https://developer.chrome.com/docs/extensions/get-started?hl=he#tutorials)
###  מהם תוספים? 
תוספים ל-Chrome משפרים את חוויית הגלישה על ידי התאמה אישית של ממשק המשתמש, מעקב אחר אירועים בדפדפן ושינוי האינטרנט. ב[חנות האינטרנט של Chrome](https://chromewebstore.google.com/?hl=he) אפשר למצוא דוגמאות נוספות לדברים שאפשר לעשות עם תוספים. 
###  איך הם נוצרים? 
אפשר ליצור תוספים באמצעות אותן טכנולוגיות אינטרנט שמיועדות ליצירת אפליקציות אינטרנט: [HTML](https://web.dev/learn/html?hl=he),‏ [CSS](https://web.dev/learn/css?hl=he) ו-[JavaScript](https://developer.mozilla.org/docs/Learn/JavaScript). 
###  מה הם יכולים לעשות? 
בנוסף ל[ממשקי Web API](https://developer.mozilla.org/docs/Web/API), לתוספים יש גם גישה ל[ממשקי API של תוספים ל-Chrome](https://developer.chrome.com/docs/extensions/reference?hl=he) כדי לבצע משימות שונות. סקירה מפורטת יותר זמינה [במדריך למפתחים](https://developer.chrome.com/docs/extensions/develop?hl=he). 
[ article  ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=he)
###  [ מניפסט ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=he)
קובץ המניפסט של התוסף הוא הקובץ היחיד הנדרש, ושם הקובץ שלו חייב להיות ספציפי: manifest.json. הוא גם צריך להיות ממוקם בתיקיית השורש של התוסף. המניפסט מתעד מטא-נתונים חשובים, מגדיר משאבים, מצהיר על הרשאות ומזהה אילו קבצים צריך להריץ ברקע ובדף. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=he)
###  [ קובצי שירות (service worker) ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=he)
קובץ שירות פועל ברקע ומטפל באירועים בדפדפן, כמו הסרת סימנייה או סגירת כרטיסייה. אין להם גישה ל-DOM, אבל אפשר לשלב אותו עם מסמך מחוץ למסך בתרחיש לדוגמה הזה. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=he)
###  [ סקריפטים של תוכן ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=he)
סקריפטים של תוכן מפעילים JavaScript בהקשר של דף אינטרנט. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=he)
###  [ פעולה בסרגל הכלים ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=he)
להריץ קוד כשהמשתמש לוחץ על סמל סרגל הכלים של התוסף או להציג חלון קופץ באמצעות Action API. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=he)
###  [ חלונית צדדית ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=he)
הצגת ממשק משתמש מותאם אישית בחלונית הצדדית של הדפדפן. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=he)
###  [ DeclarativeNetRequest ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=he)
ליירט, לחסום או לשנות בקשות רשת. 
palette 
###  תכנון תוסף באיכות גבוהה 
כשאתם בוחרים אילו תכונות לתמוך בהן, חשוב לוודא שהתוסף משרת [מטרה יחידה](https://developer.chrome.com/docs/webstore/program-policies/quality-guidelines-faq?hl=he) שמוגדרת באופן מצומצם וקלה להבנה. 
build 
###  כדאי להכיר את כללי המדיניות 
תוספים שמופצים בחנות האינטרנט של Chrome חייבים לעמוד בדרישות של [מדיניות התוכנית למפתחים](https://developer.chrome.com/docs/webstore/program-policies?hl=he). כדאי לעיין בכללי המדיניות האלה כדי לוודא שהתוסף שלכם יכול להתארח בחנות האינטרנט של Chrome. 
cloud_off 
###  הכללת כל הלוגיקה של התוסף 
כשכותבים את הקוד, חשוב לזכור שכל הלוגיקה חייבת להיכלל בחבילת התוספים. המשמעות היא שלא ניתן להוריד קוד JavaScript נוסף בזמן הריצה. [שיפור אבטחת התוספים](https://developer.chrome.com/docs/extensions/migrating/improve-security?hl=he) – חלופות להרצת קוד שמתארח מרחוק. 
code 
###  התוסף הראשון 
יצירת התוסף הראשון של hello world, שבו תתרגלו את תהליך הפיתוח של תוספים. 
code 
###  הפעלת סקריפטים בכל דף 
איך מוסיפים רכיבים לאתר מסוים באופן אוטומטי 
code 
###  הוספת סקריפטים לכרטיסייה הפעילה 
לוחצים על סמל סרגל הכלים כדי לפשט את הסגנון של הדף הנוכחי. 
code 
###  יצירת מנהל כרטיסיות 
איך יוצרים חלון קופץ לניהול הכרטיסיות 
code 
###  טיפול באירועים באמצעות שירותי עבודה 
איך יוצרים תוסף של שירות עבודה (service worker) ומאתרים בו באגים 
code 
###  ניפוי באגים בתוסף 
איך למצוא יומנים והודעות שגיאה במהלך ניפוי הבאגים 

