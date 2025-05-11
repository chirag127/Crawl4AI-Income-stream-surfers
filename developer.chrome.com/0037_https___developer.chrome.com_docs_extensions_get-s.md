---
url: https://developer.chrome.com/docs/extensions/get-started?hl=ko
title: https://developer.chrome.com/docs/extensions/get-started?hl=ko
date: 2025-05-11T16:52:07.105166
depth: 1
---

[ 기본 콘텐츠로 건너뛰기 ](https://developer.chrome.com/docs/extensions/get-started?hl=ko#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/extensions/get-started?hl=es-419)




이 페이지는 [Cloud Translation API](https://cloud.google.com/translate/?hl=ko)를 통해 번역되었습니다. 


###  시작하기 
Chrome 확장 프로그램 개발에 오신 것을 환영합니다. 첫 번째 Chrome 확장 프로그램을 빌드하고 배포하는 데 필요한 모든 것을 알아보세요. 
###  확장 프로그램이란 무엇인가요? 
Chrome 확장 프로그램은 사용자 인터페이스를 맞춤설정하고, 브라우저 이벤트를 관찰하고, 웹을 수정하여 탐색 환경을 개선합니다. 확장 프로그램이 할 수 있는 작업의 더 많은 예는 [Chrome 웹 스토어](https://chromewebstore.google.com/?hl=ko)를 참고하세요. 
###  어떻게 빌드되나요? 
웹 애플리케이션을 만드는 데 사용되는 것과 동일한 웹 기술([HTML](https://web.dev/learn/html?hl=ko), [CSS](https://web.dev/learn/css?hl=ko), [JavaScript](https://developer.mozilla.org/docs/Learn/JavaScript))을 사용하여 확장 프로그램을 빌드할 수 있습니다. 
###  어떤 조치를 취할 수 있을까요? 
확장 프로그램은 [웹 API](https://developer.mozilla.org/docs/Web/API) 외에도 [Chrome 확장 프로그램 API](https://developer.chrome.com/docs/extensions/reference?hl=ko)에 액세스하여 다양한 작업을 실행할 수 있습니다. 자세한 내용은 [개발 가이드](https://developer.chrome.com/docs/extensions/develop?hl=ko)를 참고하세요. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=ko)
###  [ 매니페스트 ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=ko)
확장 프로그램의 매니페스트는 특정 파일 이름(manifest.json)이 있어야 하는 유일한 필수 파일입니다. 또한 확장 프로그램의 루트 디렉터리에 있어야 합니다. 매니페스트는 중요한 메타데이터를 기록하고, 리소스를 정의하고, 권한을 선언하고, 백그라운드와 페이지에서 실행할 파일을 식별합니다. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=ko)
###  [ 서비스 워커 ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=ko)
서비스 워커는 백그라운드에서 실행되며 북마크 삭제 또는 탭 닫기와 같은 브라우저 이벤트를 처리합니다. DOM에 액세스할 수는 없지만 이 사용 사례에서는 오프스크린 문서와 결합할 수 있습니다. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=ko)
###  [ 콘텐츠 스크립트 ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=ko)
콘텐츠 스크립트는 웹페이지의 컨텍스트에서 JavaScript를 실행합니다. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=ko)
###  [ 툴바 작업 ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=ko)
사용자가 확장 프로그램 툴바 아이콘을 클릭할 때 코드를 실행하거나 Action API를 사용하여 팝업을 표시합니다. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=ko)
###  [ 측면 패널 ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=ko)
브라우저의 측면 패널에 맞춤 UI를 표시합니다. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=ko)
###  [ DeclarativeNetRequest ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=ko)
네트워크 요청을 가로채거나 차단하거나 수정합니다. 
palette 
###  고품질 확장 프로그램 설계 
지원할 기능을 선택할 때는 확장 프로그램이 좁게 정의되고 이해하기 쉬운 [단일 목적](https://developer.chrome.com/docs/webstore/program-policies/quality-guidelines-faq?hl=ko)을 충족하는지 확인하세요. 
build 
###  정책 숙지 
Chrome 웹 스토어에 배포되는 확장 프로그램은 [개발자 프로그램 정책](https://developer.chrome.com/docs/webstore/program-policies?hl=ko)을 준수해야 합니다. Chrome 웹 스토어에서 확장 프로그램을 호스팅할 수 있도록 하려면 다음 정책을 살펴보세요. 
cloud_off 
###  모든 확장 프로그램 로직 포함 
코드를 작성할 때는 모든 로직이 확장 프로그램 패키지에 포함되어야 한다는 점에 유의하세요. 즉, 런타임 시 추가 JavaScript 코드를 다운로드할 수 없습니다. [확장 프로그램 보안 개선](https://developer.chrome.com/docs/extensions/migrating/improve-security?hl=ko)은 원격 호스팅 코드 실행에 대한 대안을 제공합니다. 
code 
###  첫 번째 확장 프로그램 
첫 번째 Hello World 확장 프로그램을 만들어 확장 프로그램 개발 워크플로를 익힙니다. 
code 
###  모든 페이지에서 스크립트 실행 
지정된 사이트에 요소를 자동으로 추가하는 방법을 알아보세요. 
code 
###  활성 탭에 스크립트 삽입 
툴바 아이콘을 클릭하여 현재 페이지의 스타일을 간소화하는 방법을 알아봅니다. 
code 
###  탭 관리자 만들기 
탭을 관리하는 팝업을 만드는 방법을 알아봅니다. 
code 
###  서비스 워커로 이벤트 처리 
확장 프로그램 서비스 작업자를 만들고 디버그하는 방법을 알아봅니다. 
code 
###  확장 프로그램 디버그 
디버깅 중에 로그와 오류 메시지를 찾는 방법을 알아봅니다. 

