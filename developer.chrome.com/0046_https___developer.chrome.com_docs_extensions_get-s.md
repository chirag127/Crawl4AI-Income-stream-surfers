---
url: https://developer.chrome.com/docs/extensions/get-started?hl=tr
title: https://developer.chrome.com/docs/extensions/get-started?hl=tr
date: 2025-05-11T16:52:12.960118
depth: 1
---

[ Ana içeriğe atla ](https://developer.chrome.com/docs/extensions/get-started?hl=tr#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/extensions/get-started?hl=es-419)

Oturum aç


Bu sayfa, [Cloud Translation API](https://cloud.google.com/translate/?hl=tr) ile çevrilmiştir. 


###  Başlama 
Chrome uzantısı geliştirmeye hoş geldiniz. İlk Chrome uzantınızı oluşturmaya ve dağıtmaya başlamak için ihtiyacınız olan her şeyi keşfedin. 
[İlk uzantınızı oluşturma](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world?hl=tr) [Tüm eğiticileri göster](https://developer.chrome.com/docs/extensions/get-started?hl=tr#tutorials)
###  Uzantılar nedir? 
Chrome uzantıları, kullanıcı arayüzünü özelleştirerek, tarayıcı etkinliklerini gözlemleyerek ve web'i değiştirerek tarama deneyimini iyileştirir. Uzantıların neler yapabileceğiyle ilgili daha fazla örnek için [Chrome Web Mağazası](https://chromewebstore.google.com/?hl=tr)'nı ziyaret edin. 
###  Bu raporlar nasıl oluşturulur? 
Web uygulamaları oluşturmak için kullanılan web teknolojilerini ([HTML](https://web.dev/learn/html?hl=tr), [CSS](https://web.dev/learn/css?hl=tr) ve [JavaScript](https://developer.mozilla.org/docs/Learn/JavaScript)) kullanarak uzantı oluşturabilirsiniz. 
###  Bu kullanıcılar ne yapabilir? 
Uzantıların, farklı görevleri gerçekleştirmek için [Web API'lerine](https://developer.mozilla.org/docs/Web/API) ek olarak [Chrome Uzantısı API'lerine](https://developer.chrome.com/docs/extensions/reference?hl=tr) de erişimi vardır. Daha ayrıntılı bir genel bakış için [Geliştirme kılavuzuna](https://developer.chrome.com/docs/extensions/develop?hl=tr) göz atın. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=tr)
###  [ Manifest ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=tr)
Uzantı manifesti, belirli bir dosya adına (manifest.json) sahip olması gereken tek zorunlu dosyadır. Ayrıca, uzantının kök dizininde bulunmalıdır. Manifest, önemli meta verileri kaydeder, kaynakları tanımlar, izinleri belirtir ve arka planda ve sayfada hangi dosyaların çalışacağını belirler. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=tr)
###  [ Hizmet çalışanları ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=tr)
Hizmet çalışanları arka planda çalışır ve yer işareti kaldırma veya sekme kapatma gibi tarayıcı etkinliklerini yönetir. DOM'a erişimleri yoktur ancak bu kullanım alanı için DOM'u ekran dışı bir dokümanla birleştirebilirsiniz. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=tr)
###  [ İçerik komut dosyaları ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=tr)
İçerik komut dosyaları, JavaScript'i bir web sayfası bağlamında çalıştırır. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=tr)
###  [ Araç çubuğu işlemi ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=tr)
Kullanıcı uzantı araç çubuğu simgesini tıkladığında kod yürütme veya Action API'yi kullanarak pop-up gösterme. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=tr)
###  [ Yan Panel ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=tr)
Tarayıcının yan panelinde özel kullanıcı arayüzü görüntüleme 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=tr)
###  [ DeclarativeNetRequest ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=tr)
Ağ isteklerine müdahale etme, engelleme veya değiştirme 
palette 
###  Yüksek kaliteli uzantı tasarlama 
Hangi özellikleri destekleyeceğinizi seçerken uzantınızın, dar kapsamlı ve kolay anlaşılır [tek bir amaca](https://developer.chrome.com/docs/webstore/program-policies/quality-guidelines-faq?hl=tr) hizmet ettiğinden emin olun. 
build 
###  Politikaları öğrenin 
Chrome Web Mağazası'nda dağıtılan uzantılar [geliştirici programı politikalarına](https://developer.chrome.com/docs/webstore/program-policies?hl=tr) uygun olmalıdır. Uzantınızın Chrome Web Mağazası'nda barındırılabilmesi için bu politikaları inceleyin. 
cloud_off 
###  Tüm uzantı mantığını dahil edin 
Kodunuzu yazarken tüm mantığın uzantı paketine dahil edilmesi gerektiğini unutmayın. Bu, çalışma zamanında ek JavaScript kodu indirilemeyeceği anlamına gelir. [Uzantı güvenliğini artırma](https://developer.chrome.com/docs/extensions/migrating/improve-security?hl=tr), uzaktan barındırılan kodu çalıştırmaya alternatifler sunar. 
code 
###  İlk uzantınız 
Uzatma geliştirme iş akışıyla tanışacağınız ilk Merhaba Dünya uzantınızı oluşturun. 
code 
###  Her sayfada komut dosyası çalıştırma 
Belirli bir siteye otomatik olarak öğe eklemeyi öğrenin. 
code 
###  Etkin sekmeye komut dosyası yerleştirme 
Araç çubuğu simgesini tıklayarak mevcut sayfanın stilini basitleştirmeyi öğrenin. 
code 
###  Sekme yöneticisi oluşturma 
Sekmelerinizi yöneten bir pop-up oluşturmayı öğrenin. 
code 
###  Hizmet işçileriyle etkinlikleri işleme 
Uzatma hizmet çalışanı oluşturmayı ve hata ayıklamayı öğrenin. 
code 
###  Uzantınızda hata ayıklama 
Hata ayıklama sırasında günlükleri ve hata mesajlarını nasıl bulacağınızı öğrenin. 

