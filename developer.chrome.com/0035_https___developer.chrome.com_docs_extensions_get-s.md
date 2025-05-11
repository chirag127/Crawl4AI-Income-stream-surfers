---
url: https://developer.chrome.com/docs/extensions/get-started?hl=id
title: https://developer.chrome.com/docs/extensions/get-started?hl=id
date: 2025-05-11T16:52:05.094089
depth: 1
---

[ Langsung ke konten utama ](https://developer.chrome.com/docs/extensions/get-started?hl=id#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/extensions/get-started?hl=es-419)




Halaman ini diterjemahkan oleh [Cloud Translation API](https://cloud.google.com/translate/?hl=id). 


###  Mulai 
Selamat datang di pengembangan Ekstensi Chrome. Temukan semua yang Anda perlukan untuk mulai mem-build dan mendistribusikan Ekstensi Chrome pertama Anda. 
[Mem-build ekstensi pertama Anda](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world?hl=id) [Lihat semua tutorial](https://developer.chrome.com/docs/extensions/get-started?hl=id#tutorials)
###  Apa yang dimaksud dengan ekstensi? 
Ekstensi Chrome meningkatkan pengalaman penjelajahan dengan menyesuaikan antarmuka pengguna, mengamati peristiwa browser, dan mengubah web. Kunjungi [Chrome Web Store](https://chromewebstore.google.com/?hl=id) untuk melihat contoh lain tentang kemampuan ekstensi. 
###  Bagaimana cara membuatnya? 
Anda dapat mem-build ekstensi menggunakan teknologi web yang sama dengan yang digunakan untuk membuat aplikasi web: [HTML](https://web.dev/learn/html?hl=id), [CSS](https://web.dev/learn/css?hl=id), dan [JavaScript](https://developer.mozilla.org/docs/Learn/JavaScript). 
###  Apa yang dapat mereka lakukan? 
Selain [Web API](https://developer.mozilla.org/docs/Web/API), ekstensi juga memiliki akses ke [Chrome Extension API](https://developer.chrome.com/docs/extensions/reference?hl=id) untuk menyelesaikan berbagai tugas. Untuk ringkasan yang lebih mendetail, lihat [Panduan pengembangan](https://developer.chrome.com/docs/extensions/develop?hl=id). 
[ article  ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=id)
###  [ Manifes ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=id)
Manifes ekstensi adalah satu-satunya file yang diperlukan yang harus memiliki nama file tertentu: manifest.json. File ini juga harus berada di direktori root ekstensi. Manifes mencatat metadata penting, menentukan resource, mendeklarasikan izin, dan mengidentifikasi file yang akan dijalankan di latar belakang dan di halaman. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=id)
###  [ Pekerja layanan ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=id)
Pekerja layanan berjalan di latar belakang dan menangani peristiwa browser, seperti menghapus bookmark, atau menutup tab. Fungsi ini tidak memiliki akses ke DOM, tetapi Anda dapat menggabungkannya dengan dokumen di balik layar untuk kasus penggunaan ini. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=id)
###  [ Skrip konten ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=id)
Skrip konten menjalankan JavaScript dalam konteks halaman web. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=id)
###  [ Tindakan toolbar ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=id)
Jalankan kode saat pengguna mengklik ikon toolbar ekstensi atau tampilkan pop-up menggunakan Action API. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=id)
###  [ Panel Samping ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=id)
Menampilkan UI kustom di panel samping browser. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=id)
###  [ DeclarativeNetRequest ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=id)
Mencegat, memblokir, atau mengubah permintaan jaringan. 
palette 
###  Mendesain ekstensi berkualitas tinggi 
Saat memilih fitur yang akan didukung, pastikan ekstensi Anda memenuhi [satu tujuan](https://developer.chrome.com/docs/webstore/program-policies/quality-guidelines-faq?hl=id) yang didefinisikan secara sempit dan mudah dipahami. 
[Pelajari lebih lanjut](https://developer.chrome.com/docs/webstore/best_practices?hl=id)
build 
###  Memahami kebijakan 
Ekstensi yang didistribusikan di Chrome Web Store harus mematuhi [kebijakan program developer](https://developer.chrome.com/docs/webstore/program-policies?hl=id). Pelajari kebijakan ini untuk memastikan ekstensi Anda dapat dihosting di Chrome Web Store. 
[Pelajari lebih lanjut](https://developer.chrome.com/docs/webstore/program-policies?hl=id)
cloud_off 
###  Menyertakan semua logika ekstensi 
Saat menulis kode, perhatikan bahwa semua logika harus disertakan dalam paket ekstensi. Artinya, tidak ada kode JavaScript tambahan yang dapat didownload saat runtime. [Meningkatkan keamanan ekstensi](https://developer.chrome.com/docs/extensions/migrating/improve-security?hl=id) menyediakan alternatif untuk menjalankan kode yang dihosting dari jarak jauh. 
[Pelajari lebih lanjut](https://developer.chrome.com/docs/extensions/migrating/improve-security?hl=id)
code 
###  Ekstensi pertama Anda 
Buat ekstensi hello world pertama Anda, tempat Anda akan memahami alur kerja pengembangan ekstensi. 
code 
###  Menjalankan skrip di setiap halaman 
Pelajari cara menambahkan elemen secara otomatis ke situs yang ditentukan. 
code 
###  Memasukkan skrip ke tab aktif 
Pelajari cara menyederhanakan gaya halaman saat ini dengan mengklik ikon toolbar. 
code 
###  Membuat pengelola tab 
Pelajari cara membuat pop-up yang mengelola tab Anda. 
code 
###  Menangani peristiwa dengan pekerja layanan 
Pelajari cara membuat dan men-debug pekerja layanan ekstensi. 
code 
###  Men-debug ekstensi 
Pelajari cara menemukan log dan pesan error selama proses debug. 

