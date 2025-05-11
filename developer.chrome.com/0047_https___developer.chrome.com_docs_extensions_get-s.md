---
url: https://developer.chrome.com/docs/extensions/get-started?hl=vi
title: https://developer.chrome.com/docs/extensions/get-started?hl=vi
date: 2025-05-11T16:52:12.975240
depth: 1
---

[ Chuyển ngay đến nội dung chính ](https://developer.chrome.com/docs/extensions/get-started?hl=vi#main-content)
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Nederlands
  * Português – Brasil
  * Tiếng Việt
  * Русский
  * العربيّة
  * ภาษาไทย
  * 中文 – 简体
  * 中文 – 繁體

Đăng nhập


Trang này được dịch bởi [Cloud Translation API](https://cloud.google.com/translate/?hl=vi). 


Sử dụng bộ sưu tập để sắp xếp ngăn nắp các trang  Lưu và phân loại nội dung dựa trên lựa chọn ưu tiên của bạn. 
###  Bắt đầu 
Chào mừng bạn đến với phần phát triển Tiện ích Chrome. Khám phá mọi thứ bạn cần để bắt đầu xây dựng và phân phối Tiện ích Chrome đầu tiên. 
[Tạo tiện ích đầu tiên](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world?hl=vi) [Xem tất cả hướng dẫn](https://developer.chrome.com/docs/extensions/get-started?hl=vi#tutorials)
###  Tiện ích là gì? 
Tiện ích Chrome nâng cao trải nghiệm duyệt web bằng cách tuỳ chỉnh giao diện người dùng, quan sát các sự kiện của trình duyệt và sửa đổi web. Truy cập vào [Cửa hàng Chrome trực tuyến](https://chromewebstore.google.com/?hl=vi) để xem thêm ví dụ về những việc mà tiện ích có thể làm. 
###  Làm cách nào để tạo các mẫu này? 
Bạn có thể tạo tiện ích bằng các công nghệ web tương tự như dùng để tạo ứng dụng web: [HTML](https://web.dev/learn/html?hl=vi), [CSS](https://web.dev/learn/css?hl=vi) và [JavaScript](https://developer.mozilla.org/docs/Learn/JavaScript). 
###  Họ có thể làm gì? 
Ngoài [API web](https://developer.mozilla.org/docs/Web/API), tiện ích cũng có quyền truy cập vào [API tiện ích Chrome](https://developer.chrome.com/docs/extensions/reference?hl=vi) để thực hiện nhiều nhiệm vụ. Để biết thông tin tổng quan chi tiết hơn, hãy xem [Hướng dẫn phát triển](https://developer.chrome.com/docs/extensions/develop?hl=vi). 
[ article  ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=vi)
###  [ Tệp kê khai ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=vi)
Tệp kê khai của tiện ích là tệp bắt buộc duy nhất phải có tên tệp cụ thể: manifest.json. Tệp này cũng phải nằm trong thư mục gốc của tiện ích. Tệp kê khai ghi lại siêu dữ liệu quan trọng, xác định tài nguyên, khai báo quyền và xác định những tệp cần chạy ở chế độ nền và trên trang. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=vi)
###  [ Trình chạy dịch vụ ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=vi)
Trình chạy dịch vụ chạy ở chế độ nền và xử lý các sự kiện của trình duyệt, chẳng hạn như xoá dấu trang hoặc đóng thẻ. Các thành phần này không có quyền truy cập vào DOM, nhưng bạn có thể kết hợp thành phần này với một tài liệu ngoài màn hình cho trường hợp sử dụng này. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=vi)
###  [ Tập lệnh nội dung ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=vi)
Tập lệnh nội dung chạy JavaScript trong ngữ cảnh của một trang web. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=vi)
###  [ Thao tác trên thanh công cụ ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=vi)
Thực thi mã khi người dùng nhấp vào biểu tượng thanh công cụ tiện ích hoặc hiển thị một cửa sổ bật lên bằng Action API. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=vi)
###  [ Bảng điều khiển bên ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=vi)
Hiển thị giao diện người dùng tuỳ chỉnh trong bảng điều khiển bên của trình duyệt. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=vi)
###  [ DeclarativeNetRequest ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=vi)
Chặn, chặn hoặc sửa đổi các yêu cầu kết nối mạng. 
palette 
###  Thiết kế tiện ích chất lượng cao 
Khi chọn tính năng cần hỗ trợ, hãy đảm bảo tiện ích của bạn thực hiện [một mục đích duy nhất](https://developer.chrome.com/docs/webstore/program-policies/quality-guidelines-faq?hl=vi) được xác định rõ ràng và dễ hiểu. 
build 
###  Làm quen với các chính sách 
Các tiện ích được phân phối trên Cửa hàng Chrome trực tuyến phải tuân thủ [chính sách chương trình dành cho nhà phát triển](https://developer.chrome.com/docs/webstore/program-policies?hl=vi). Hãy tìm hiểu các chính sách này để đảm bảo tiện ích của bạn có thể được lưu trữ trong Cửa hàng Chrome trực tuyến. 
cloud_off 
###  Bao gồm tất cả logic của tiện ích 
Khi viết mã, hãy nhớ rằng tất cả logic phải có trong gói tiện ích. Điều này có nghĩa là không thể tải mã JavaScript bổ sung xuống trong thời gian chạy. [Nâng cao tính bảo mật của tiện ích](https://developer.chrome.com/docs/extensions/migrating/improve-security?hl=vi) cung cấp các giải pháp thay thế để thực thi mã được lưu trữ từ xa. 
code 
###  Tiện ích đầu tiên của bạn 
Tạo phần mở rộng hello world đầu tiên để làm quen với quy trình phát triển phần mở rộng. 
code 
###  Chạy tập lệnh trên mọi trang 
Tìm hiểu cách tự động thêm các phần tử vào một trang web cụ thể. 
code 
###  Chèn tập lệnh vào thẻ đang hoạt động 
Tìm hiểu cách đơn giản hoá kiểu của trang hiện tại bằng cách nhấp vào biểu tượng thanh công cụ. 
code 
###  Tạo trình quản lý thẻ 
Tìm hiểu cách tạo cửa sổ bật lên để quản lý các thẻ. 
code 
###  Xử lý sự kiện bằng worker dịch vụ 
Tìm hiểu cách tạo và gỡ lỗi trình chạy dịch vụ tiện ích. 
code 
###  Gỡ lỗi tiện ích 
Tìm hiểu cách tìm nhật ký và thông báo lỗi trong quá trình gỡ lỗi. 
[Bắt đầu xem hướng dẫn](https://developer.chrome.com/docs/extensions/get-started/tutorial/debug?hl=vi)

