---
url: https://developer.chrome.com/docs/extensions/get-started?hl=de
title: https://developer.chrome.com/docs/extensions/get-started?hl=de
date: 2025-05-11T16:51:56.048422
depth: 1
---

[ Zum Hauptinhalt springen ](https://developer.chrome.com/docs/extensions/get-started?hl=de#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/extensions/get-started?hl=es-419)




Diese Seite wurde von der [Cloud Translation API](https://cloud.google.com/translate/?hl=de) übersetzt. 


###  Los gehts 
Willkommen bei der Entwicklung von Chrome-Erweiterungen. Hier finden Sie alles, was Sie zum Erstellen und Verteilen Ihrer ersten Chrome-Erweiterung benötigen. 
[Erste Erweiterung erstellen](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world?hl=de) [Alle Anleitungen ansehen](https://developer.chrome.com/docs/extensions/get-started?hl=de#tutorials)
###  Was sind Erweiterungen? 
Chrome-Erweiterungen verbessern die Browsernutzung, indem sie die Benutzeroberfläche anpassen, Browserereignisse beobachten und das Web ändern. Im [Chrome Web Store](https://chromewebstore.google.com/?hl=de) finden Sie weitere Beispiele für die Funktionen von Erweiterungen. 
###  Wie werden sie erstellt? 
Sie können Erweiterungen mit denselben Webtechnologien erstellen, die auch für Webanwendungen verwendet werden: [HTML](https://web.dev/learn/html?hl=de), [CSS](https://web.dev/learn/css?hl=de) und [JavaScript](https://developer.mozilla.org/docs/Learn/JavaScript). 
###  Was kann er tun? 
Neben [Web-APIs](https://developer.mozilla.org/docs/Web/API) haben Erweiterungen auch Zugriff auf [Chrome-Erweiterungs-APIs](https://developer.chrome.com/docs/extensions/reference?hl=de), um verschiedene Aufgaben auszuführen. Eine ausführlichere Übersicht finden Sie im [Entwicklerleitfaden](https://developer.chrome.com/docs/extensions/develop?hl=de). 
[ article  ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=de)
###  [ Manifest ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=de)
Das Manifest der Erweiterung ist die einzige erforderliche Datei, die einen bestimmten Dateinamen haben muss: manifest.json. Außerdem muss sie sich im Stammverzeichnis der Erweiterung befinden. Das Manifest enthält wichtige Metadaten, definiert Ressourcen, deklariert Berechtigungen und gibt an, welche Dateien im Hintergrund und auf der Seite ausgeführt werden sollen. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=de)
###  [ Dienstprogramme ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=de)
Ein Service Worker wird im Hintergrund ausgeführt und verarbeitet Browserereignisse wie das Entfernen eines Lesezeichens oder das Schließen eines Tabs. Sie haben keinen Zugriff auf das DOM, aber Sie können sie für diesen Anwendungsfall mit einem Offscreen-Dokument kombinieren. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=de)
###  [ Inhaltsscripts ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=de)
In Content-Scripts wird JavaScript im Kontext einer Webseite ausgeführt. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=de)
###  [ Symbolleistenaktion ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=de)
Code ausführen, wenn der Nutzer auf das Symbol in der Symbolleiste der Erweiterung klickt, oder ein Pop-up mit der Action API anzeigen 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=de)
###  [ Seitenleiste ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=de)
Benutzerdefinierte Benutzeroberfläche in der Seitenleiste des Browsers anzeigen 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=de)
###  [ DeclarativeNetRequest ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=de)
Netzwerkanfragen abfangen, blockieren oder ändern. 
palette 
###  Hochwertige Erweiterungen entwerfen 
Achten Sie bei der Auswahl der zu unterstützenden Funktionen darauf, dass Ihre Erweiterung [einem einzigen Zweck](https://developer.chrome.com/docs/webstore/program-policies/quality-guidelines-faq?hl=de) dient, der klar definiert und leicht verständlich ist. 
[Weitere Informationen](https://developer.chrome.com/docs/webstore/best_practices?hl=de)
build 
###  Machen Sie sich mit den Richtlinien vertraut. 
Im Chrome Web Store angebotene Erweiterungen müssen den [Programmrichtlinien für Entwickler](https://developer.chrome.com/docs/webstore/program-policies?hl=de) entsprechen. Lesen Sie sich diese Richtlinien durch, um sicherzustellen, dass Ihre Erweiterung im Chrome Web Store gehostet werden kann. 
[Weitere Informationen](https://developer.chrome.com/docs/webstore/program-policies?hl=de)
cloud_off 
###  Alle Erweiterungslogik einschließen 
Denken Sie beim Schreiben des Codes daran, dass die gesamte Logik im Erweiterungspaket enthalten sein muss. Das bedeutet, dass während der Laufzeit kein zusätzlicher JavaScript-Code heruntergeladen werden kann. [Verbesserte Sicherheit von Erweiterungen](https://developer.chrome.com/docs/extensions/migrating/improve-security?hl=de) bietet Alternativen zur Ausführung von remote gehostetem Code. 
[Weitere Informationen](https://developer.chrome.com/docs/extensions/migrating/improve-security?hl=de)
code 
###  Ihre erste Erweiterung 
Erstellen Sie Ihre erste „Hallo Welt“-Erweiterung, um sich mit dem Workflow zur Erweiterungsentwicklung vertraut zu machen. 
code 
###  Scripts auf jeder Seite ausführen 
Hier erfahren Sie, wie Sie einer bestimmten Website automatisch Elemente hinzufügen. 
code 
###  Skripte in den aktiven Tab einschleusen 
Klicken Sie auf das Symbol der Symbolleiste, um den Stil der aktuellen Seite zu vereinfachen. 
code 
###  Tabmanager erstellen 
Hier erfahren Sie, wie Sie ein Pop-up erstellen, mit dem Sie Ihre Tabs verwalten können. 
code 
###  Ereignisse mit Service Workern verarbeiten 
Informationen zum Erstellen und Entwickeln eines Erweiterungsdienst-Workers 
code 
###  Erweiterung debuggen 
Hier erfahren Sie, wie Sie während der Fehlerbehebung Protokolle und Fehlermeldungen finden. 

