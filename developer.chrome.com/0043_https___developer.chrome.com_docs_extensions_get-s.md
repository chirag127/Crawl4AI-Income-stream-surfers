---
url: https://developer.chrome.com/docs/extensions/get-started?hl=th
title: https://developer.chrome.com/docs/extensions/get-started?hl=th
date: 2025-05-11T16:52:11.771780
depth: 1
---

[ ข้ามไปที่เนื้อหาหลัก ](https://developer.chrome.com/docs/extensions/get-started?hl=th#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/extensions/get-started?hl=es-419)




หน้านี้ได้รับการแปลโดย [Cloud Translation API](https://cloud.google.com/translate/?hl=th)


###  เริ่มใช้งาน 
ยินดีต้อนรับสู่การพัฒนาส่วนขยาย Chrome ดูข้อมูลทั้งหมดที่คุณต้องใช้ในการเริ่มสร้างและเผยแพร่ส่วนขยาย Chrome รายการแรก 
[สร้างชิ้นงานแรก](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world?hl=th) [ดูบทแนะนำทั้งหมด](https://developer.chrome.com/docs/extensions/get-started?hl=th#tutorials)
###  ส่วนขยายคืออะไร 
ส่วนขยาย Chrome ช่วยปรับปรุงประสบการณ์การท่องเว็บด้วยการปรับแต่งอินเทอร์เฟซผู้ใช้ สังเกตการณ์เหตุการณ์ของเบราว์เซอร์ และแก้ไขเว็บ ไปที่ [Chrome เว็บสโตร์](https://chromewebstore.google.com/?hl=th) เพื่อดูตัวอย่างเพิ่มเติมเกี่ยวกับสิ่งที่ส่วนขยายทำได้ 
###  สร้างขึ้นอย่างไร 
คุณสามารถสร้างส่วนขยายโดยใช้เทคโนโลยีเว็บเดียวกันกับที่ใช้สร้างเว็บแอปพลิเคชัน ได้แก่ [HTML](https://web.dev/learn/html?hl=th), [CSS](https://web.dev/learn/css?hl=th) และ [JavaScript](https://developer.mozilla.org/docs/Learn/JavaScript)
###  ผู้เข้าชมจะทำอะไรได้บ้าง 
นอกเหนือจาก [Web API](https://developer.mozilla.org/docs/Web/API) แล้ว ส่วนขยายยังมีสิทธิ์เข้าถึง [Chrome Extension API](https://developer.chrome.com/docs/extensions/reference?hl=th) เพื่อทำงานต่างๆ ด้วย ดูภาพรวมโดยละเอียดได้ที่[คู่มือการพัฒนา](https://developer.chrome.com/docs/extensions/develop?hl=th)
[ article  ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=th)
###  [ ไฟล์ Manifest ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=th)
ไฟล์ Manifest ของส่วนขยายเป็นไฟล์เดียวที่จำเป็นซึ่งต้องมีชื่อไฟล์ที่เฉพาะเจาะจง ซึ่งก็คือ manifest.json และจะต้องอยู่ในไดเรกทอรีรูทของส่วนขยายด้วย ไฟล์ Manifest จะบันทึกข้อมูลเมตาที่สําคัญ กําหนดทรัพยากร ประกาศสิทธิ์ และระบุไฟล์ที่จะทํางานในเบื้องหลังและในหน้าเว็บ 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=th)
###  [ Service Worker ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=th)
Service Worker จะทำงานในเบื้องหลังและจัดการเหตุการณ์ของเบราว์เซอร์ เช่น การนำบุ๊กมาร์กออกหรือปิดแท็บ ผู้ใช้จะไม่มีสิทธิ์เข้าถึง DOM แต่คุณสามารถรวมกับเอกสารที่อยู่นอกหน้าจอสำหรับกรณีการใช้งานนี้ได้ 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=th)
###  [ สคริปต์เนื้อหา ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=th)
สคริปต์เนื้อหาจะเรียกใช้ JavaScript ในบริบทของหน้าเว็บ 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=th)
###  [ การดำเนินการของแถบเครื่องมือ ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=th)
เรียกใช้โค้ดเมื่อผู้ใช้คลิกไอคอนแถบเครื่องมือส่วนขยายหรือแสดงป๊อปอัปโดยใช้ Action API 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=th)
###  [ แผงด้านข้าง ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=th)
แสดง UI ที่กําหนดเองในแผงด้านข้างของเบราว์เซอร์ 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=th)
###  [ DeclarativeNetRequest ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=th)
สกัดกั้น บล็อก หรือแก้ไขคำขอของเครือข่าย 
palette 
###  ออกแบบส่วนขยายที่มีคุณภาพสูง 
เมื่อเลือกฟีเจอร์ที่จะรองรับ ให้ตรวจสอบว่าส่วนขยายของคุณมี[วัตถุประสงค์เดียว](https://developer.chrome.com/docs/webstore/program-policies/quality-guidelines-faq?hl=th)ที่กําหนดไว้อย่างแคบๆ และเข้าใจง่าย 
build 
###  ทำความคุ้นเคยกับนโยบาย 
ส่วนขยายที่เผยแพร่ใน Chrome เว็บสโตร์ต้องเป็นไปตาม[นโยบายโปรแกรมสำหรับนักพัฒนาแอป](https://developer.chrome.com/docs/webstore/program-policies?hl=th) โปรดอ่านนโยบายเหล่านี้เพื่อให้มั่นใจว่าส่วนขยายของคุณจะโฮสต์ใน Chrome เว็บสโตร์ได้ 
cloud_off 
###  รวมตรรกะส่วนขยายทั้งหมด 
เมื่อเขียนโค้ด โปรดทราบว่าต้องรวมตรรกะทั้งหมดไว้ในแพ็กเกจส่วนขยาย ซึ่งหมายความว่าระบบจะไม่ดาวน์โหลดโค้ด JavaScript เพิ่มเติมเมื่อรันไทม์ [ปรับปรุงความปลอดภัยของส่วนขยาย](https://developer.chrome.com/docs/extensions/migrating/improve-security?hl=th)เป็นทางเลือกในการเรียกใช้โค้ดที่โฮสต์จากระยะไกล 
code 
###  ส่วนขยายแรก 
สร้างส่วนขยาย Hello World รายการแรก ซึ่งจะช่วยให้คุณคุ้นเคยกับเวิร์กโฟลว์การพัฒนาส่วนขยาย 
code 
###  เรียกใช้สคริปต์ในทุกหน้า 
ดูวิธีเพิ่มองค์ประกอบลงในเว็บไซต์ที่ระบุโดยอัตโนมัติ 
code 
###  แทรกสคริปต์ลงในแท็บที่ใช้งานอยู่ 
ดูวิธีลดความซับซ้อนของสไตล์ของหน้าปัจจุบันโดยคลิกไอคอนแถบเครื่องมือ 
code 
###  สร้างเครื่องมือจัดการแท็บ 
ดูวิธีสร้างป๊อปอัปที่จัดการแท็บ 
code 
###  จัดการเหตุการณ์ด้วย Service Worker 
ดูวิธีสร้างและแก้ไขข้อบกพร่องของ Wapper บริการของส่วนขยาย 
code 
###  แก้ไขข้อบกพร่องของส่วนขยาย 
ดูวิธีค้นหาบันทึกและข้อความแสดงข้อผิดพลาดระหว่างการแก้ไขข้อบกพร่อง 

