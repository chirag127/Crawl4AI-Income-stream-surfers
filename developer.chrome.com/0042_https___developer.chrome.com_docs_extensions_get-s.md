---
url: https://developer.chrome.com/docs/extensions/get-started?hl=pl
title: https://developer.chrome.com/docs/extensions/get-started?hl=pl
date: 2025-05-11T16:52:10.250252
depth: 1
---

[ Przejdź do głównej treści ](https://developer.chrome.com/docs/extensions/get-started?hl=pl#main-content)
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

Zaloguj się


Ta strona została przetłumaczona przez [Cloud Translation API](https://cloud.google.com/translate/?hl=pl). 


Zadbaj o dobrą organizację dzięki kolekcji  Zapisuj i kategoryzuj treści zgodnie ze swoimi preferencjami. 
###  Rozpocznij 
Witamy w rozwijaniu rozszerzeń do Chrome. Dowiedz się, co jest potrzebne, aby zacząć tworzyć i rozpowszechniać pierwsze rozszerzenie do Chrome. 
[Tworzenie pierwszego rozszerzenia](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world?hl=pl) [Zobacz wszystkie samouczki](https://developer.chrome.com/docs/extensions/get-started?hl=pl#tutorials)
###  Co to są rozszerzenia? 
Rozszerzenia Chrome ułatwiają przeglądanie dzięki dostosowywaniu interfejsu, obserwowaniu zdarzeń w przeglądarce i modyfikowaniu stron internetowych. Więcej przykładów możliwości rozszerzeń znajdziesz w [Chrome Web Store](https://chromewebstore.google.com/?hl=pl). 
###  Jak są budowane? 
Rozszerzenia możesz tworzyć za pomocą tych samych technologii internetowych, które są używane do tworzenia aplikacji internetowych: [HTML](https://web.dev/learn/html?hl=pl), [CSS](https://web.dev/learn/css?hl=pl) i [JavaScript](https://developer.mozilla.org/docs/Learn/JavaScript). 
###  Co mogą zrobić? 
Oprócz [interfejsów API sieciowych](https://developer.mozilla.org/docs/Web/API) mają one też dostęp do [interfejsów API rozszerzeń Chrome](https://developer.chrome.com/docs/extensions/reference?hl=pl), które umożliwiają wykonywanie różnych zadań. Bardziej szczegółowe informacje znajdziesz w [przewodniku dla programistów](https://developer.chrome.com/docs/extensions/develop?hl=pl). 
[ article  ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=pl)
###  [ Plik manifestu ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=pl)
Plik manifestu rozszerzenia to jedyny wymagany plik, który musi mieć określoną nazwę: manifest.json. Musi też znajdować się w katalogu głównym rozszerzenia. Plik manifestu zawiera ważne metadane, definiuje zasoby, deklaruje uprawnienia i określa, które pliki mają być uruchamiane w tle i na stronie. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=pl)
###  [ Skrypty service worker ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=pl)
Skrypt service worker działa w tle i obsługuje zdarzenia przeglądarki, takie jak usuwanie zakładki lub zamykanie karty. Nie mają dostępu do DOM, ale w tym przypadku możesz połączyć go z dokumentem poza ekranem. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=pl)
###  [ Skrypty dotyczące zawartości ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=pl)
Skrypty treści uruchamiają kod JavaScript w kontekście strony internetowej. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=pl)
###  [ Działanie na pasku narzędzi ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=pl)
Wykonywanie kodu, gdy użytkownik kliknie ikonę paska narzędzi rozszerzenia, lub wyświetlanie wyskakującego okienka za pomocą interfejsu Action API. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=pl)
###  [ Panel boczny ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=pl)
Wyświetlanie niestandardowego interfejsu użytkownika w panelu bocznym przeglądarki. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=pl)
###  [ DeclarativeNetRequest ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=pl)
przechwytywać, blokować lub modyfikować żądania sieciowe; 
palette 
###  Projektowanie wysokiej jakości rozszerzeń 
Wybierając funkcje, które chcesz obsługiwać, upewnij się, że rozszerzenie ma [jeden cel](https://developer.chrome.com/docs/webstore/program-policies/quality-guidelines-faq?hl=pl), który jest ściśle określony i łatwy do zrozumienia. 
build 
###  Zapoznaj się z zasadami 
Rozszerzenia rozpowszechniane w Chrome Web Store muszą być zgodne z [zasadami programu dla deweloperów](https://developer.chrome.com/docs/webstore/program-policies?hl=pl). Zapoznaj się z tymi zasadami, aby mieć pewność, że Twoje rozszerzenie może być hostowane w Chrome Web Store. 
cloud_off 
###  Uwzględnij całą logikę rozszerzenia 
Podczas pisania kodu pamiętaj, że wszystkie funkcje logiczne muszą znajdować się w pakiecie rozszerzeń. Oznacza to, że podczas wykonywania nie można pobrać dodatkowego kodu JavaScript. [Zwiększanie bezpieczeństwa rozszerzeń](https://developer.chrome.com/docs/extensions/migrating/improve-security?hl=pl) to alternatywa dla uruchamiania kodu hostowanego zdalnie. 
code 
###  Pierwsze rozszerzenie 
Utwórz swoje pierwsze rozszerzenie „hello world”, aby zapoznać się z procesem tworzenia rozszerzeń. 
code 
###  Uruchamianie skryptów na każdej stronie 
Dowiedz się, jak automatycznie dodawać elementy do określonej witryny. 
code 
###  Wstawianie skryptów na aktywnej karcie 
Dowiedz się, jak uprościć styl bieżącej strony, klikając ikonę na pasku narzędzi. 
code 
###  Tworzenie menedżera kart 
Dowiedz się, jak utworzyć wyskakujące okienko do zarządzania kartami. 
code 
###  Obsługa zdarzeń za pomocą usług workerów 
Dowiedz się, jak tworzyć i debugować rozszerzenie service worker. 
code 
###  Debugowanie rozszerzenia 
Dowiedz się, jak znajdować dzienniki i komunikaty o błędach podczas debugowania. 

