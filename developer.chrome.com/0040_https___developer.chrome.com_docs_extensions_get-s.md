---
url: https://developer.chrome.com/docs/extensions/get-started?hl=nl
title: https://developer.chrome.com/docs/extensions/get-started?hl=nl
date: 2025-05-11T16:52:08.704307
depth: 1
---

[ Skip to main content ](https://developer.chrome.com/docs/extensions/get-started?hl=nl#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/extensions/get-started?hl=es-419)




Deze pagina is vertaald door de [Cloud Translation API](https://cloud.google.com/translate/?hl=nl). 


###  Aan de slag 
Welkom bij de ontwikkeling van Chrome-extensies. Ontdek alles wat u nodig heeft om te beginnen met het bouwen en distribueren van uw eerste Chrome-extensie. 
[Bouw je eerste uitbreiding](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world?hl=nl) [Bekijk alle tutorials](https://developer.chrome.com/docs/extensions/get-started?hl=nl#tutorials)
###  Wat zijn extensies? 
Chrome-extensies verbeteren de browse-ervaring door de gebruikersinterface aan te passen, browsergebeurtenissen te observeren en het internet aan te passen. Bezoek de [Chrome Web Store](https://chromewebstore.google.com/?hl=nl) voor meer voorbeelden van wat extensies kunnen doen. 
###  Hoe zijn ze gebouwd? 
U kunt extensies bouwen met dezelfde webtechnologieën die worden gebruikt om webapplicaties te maken: [HTML](https://web.dev/learn/html?hl=nl) , [CSS](https://web.dev/learn/css?hl=nl) en [JavaScript](https://developer.mozilla.org/docs/Learn/JavaScript) . 
###  Wat kunnen ze doen? 
Naast [web-API's](https://developer.mozilla.org/docs/Web/API) hebben extensies ook toegang tot [Chrome Extension-API's](https://developer.chrome.com/docs/extensions/reference?hl=nl) om verschillende taken uit te voeren. Voor een gedetailleerder overzicht kunt u de [Ontwikkelgids](https://developer.chrome.com/docs/extensions/develop?hl=nl) raadplegen. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=nl)
###  [ Manifest ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=nl)
Het manifest van de extensie is het enige vereiste bestand dat een specifieke bestandsnaam moet hebben: manifest.json. Het moet zich ook in de hoofdmap van de extensie bevinden. Het manifest legt belangrijke metadata vast, definieert bronnen, declareert machtigingen en identificeert welke bestanden op de achtergrond en op de pagina moeten worden uitgevoerd. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=nl)
###  [ Servicemedewerkers ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=nl)
Een servicemedewerker draait op de achtergrond en handelt browsergebeurtenissen af, zoals het verwijderen van een bladwijzer of het sluiten van een tabblad. Ze hebben geen toegang tot de DOM, maar u kunt deze voor dit gebruik combineren met een offscreen-document. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=nl)
###  [ Inhoudsscripts ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=nl)
Inhoudsscripts voeren JavaScript uit in de context van een webpagina. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=nl)
###  [ Werkbalkactie ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=nl)
Voer code uit wanneer de gebruiker op het extensiewerkbalkpictogram klikt of toon een pop-up met behulp van de Action API. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=nl)
###  [ Zijpaneel ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=nl)
Geef de aangepaste gebruikersinterface weer in het zijpaneel van de browser. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=nl)
###  [ DeclaratieveNetRequest ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=nl)
Netwerkverzoeken onderscheppen, blokkeren of wijzigen. 
palette 
###  Ontwerp een hoogwaardige uitbreiding 
Wanneer u kiest welke functies u wilt ondersteunen, zorg er dan voor dat uw extensie één [enkel doel](https://developer.chrome.com/docs/webstore/program-policies/quality-guidelines-faq?hl=nl) vervult dat nauwkeurig gedefinieerd en gemakkelijk te begrijpen is. 
build 
###  Maak uzelf vertrouwd met het beleid 
Extensies die in de Chrome Web Store worden gedistribueerd, moeten voldoen aan het [programmabeleid voor ontwikkelaars](https://developer.chrome.com/docs/webstore/program-policies?hl=nl) . Bekijk dit beleid om ervoor te zorgen dat uw extensie kan worden gehost in de Chrome Web Store. 
cloud_off 
###  Neem alle extensielogica op 
Houd er bij het schrijven van uw code rekening mee dat alle logica in het uitbreidingspakket moet zijn opgenomen. Dit betekent dat er tijdens runtime geen extra JavaScript-code mag worden gedownload. [Verbetering van de extensiebeveiliging](https://developer.chrome.com/docs/extensions/migrating/improve-security?hl=nl) biedt alternatieven voor het uitvoeren van op afstand gehoste code. 
code 
###  Je eerste verlenging 
Creëer uw eerste hello world-extensie, waar u vertrouwd raakt met de workflow voor het ontwikkelen van extensies. 
code 
###  Voer scripts uit op elke pagina 
Leer hoe u automatisch elementen aan een opgegeven site kunt toevoegen. 
code 
###  Scripts in het actieve tabblad injecteren 
Leer hoe u de stijl van de huidige pagina kunt vereenvoudigen door op het werkbalkpictogram te klikken. 
code 
###  Maak een tabbladbeheerder 
Leer hoe u een pop-up maakt die uw tabbladen beheert. 
code 
###  Behandel evenementen met servicemedewerkers 
Leer hoe u een extensieservicemedewerker maakt en fouten oplost. 
code 
###  Debug uw extensie 
Leer hoe u logboeken en foutmeldingen kunt vinden tijdens het opsporen van fouten. 

