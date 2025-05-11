---
url: https://developer.chrome.com/docs/extensions/get-started?hl=it
title: https://developer.chrome.com/docs/extensions/get-started?hl=it
date: 2025-05-11T16:52:05.103133
depth: 1
---

[ Passa ai contenuti principali ](https://developer.chrome.com/docs/extensions/get-started?hl=it#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/extensions/get-started?hl=es-419)




Questa pagina è stata tradotta dall'[API Cloud Translation](https://cloud.google.com/translate/?hl=it). 


###  Per iniziare 
Ti diamo il benvenuto nello sviluppo di estensioni di Chrome. Scopri tutto ciò che ti serve per iniziare a creare e distribuire la tua prima estensione di Chrome. 
[Crea la tua prima estensione](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world?hl=it) [Vedi tutti i tutorial](https://developer.chrome.com/docs/extensions/get-started?hl=it#tutorials)
###  Che cosa sono le estensioni? 
Le estensioni di Chrome migliorano l'esperienza di navigazione personalizzando l'interfaccia utente, osservando gli eventi del browser e modificando il web. Visita il [Chrome Web Store](https://chromewebstore.google.com/?hl=it) per altri esempi di cosa possono fare le estensioni. 
###  Come vengono costruiti? 
Puoi creare estensioni utilizzando le stesse tecnologie web utilizzate per creare applicazioni web: [HTML](https://web.dev/learn/html?hl=it), [CSS](https://web.dev/learn/css?hl=it) e [JavaScript](https://developer.mozilla.org/docs/Learn/JavaScript). 
###  Che cosa possono fare? 
Oltre alle [API web](https://developer.mozilla.org/docs/Web/API), le estensioni hanno accesso anche alle [API di estensioni di Chrome](https://developer.chrome.com/docs/extensions/reference?hl=it) per svolgere diverse attività. Per una panoramica più dettagliata, consulta la [Guida per lo sviluppo](https://developer.chrome.com/docs/extensions/develop?hl=it). 
[ article  ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=it)
###  [ Manifest ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=it)
Il file manifest dell'estensione è l'unico file obbligatorio che deve avere un nome file specifico: manifest.json. Inoltre, deve trovarsi nella directory principale dell'estensione. Il manifest registra metadati importanti, definisce le risorse, dichiara le autorizzazioni e identifica i file da eseguire in background e nella pagina. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=it)
###  [ Service worker ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=it)
Un service worker viene eseguito in background e gestisce gli eventi del browser, ad esempio la rimozione di un preferito o la chiusura di una scheda. Non hanno accesso al DOM, ma puoi combinarli con un documento offscreen per questo caso d'uso. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=it)
###  [ Script di contenuti ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=it)
Gli script di contenuto eseguono JavaScript nel contesto di una pagina web. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=it)
###  [ Azione barra degli strumenti ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=it)
Esegui il codice quando l'utente fa clic sull'icona della barra degli strumenti dell'estensione o mostra un popup utilizzando l'API Action. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=it)
###  [ Riquadro laterale ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=it)
Mostrare l'interfaccia utente personalizzata nel riquadro laterale del browser. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=it)
###  [ DeclarativeNetRequest ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=it)
Intercettare, bloccare o modificare le richieste di rete. 
palette 
###  Progettare un'estensione di alta qualità 
Quando scegli le funzionalità da supportare, assicurati che l'estensione abbia un [unico scopo](https://developer.chrome.com/docs/webstore/program-policies/quality-guidelines-faq?hl=it), definito in modo preciso e facile da comprendere. 
build 
###  Acquisisci familiarità con le norme 
Le estensioni distribuite sul Chrome Web Store devono rispettare le [Norme del programma per gli sviluppatori](https://developer.chrome.com/docs/webstore/program-policies?hl=it). Consulta queste norme per assicurarti che la tua estensione possa essere ospitata nel Chrome Web Store. 
cloud_off 
###  Includi tutta la logica dell'estensione 
Quando scrivi il codice, tieni presente che tutta la logica deve essere inclusa nel pacchetto dell'estensione. Ciò significa che non è possibile scaricare altro codice JavaScript in fase di esecuzione. L'opzione [Migliora la sicurezza delle estensioni](https://developer.chrome.com/docs/extensions/migrating/improve-security?hl=it) offre alternative all'esecuzione di codice ospitato da remoto. 
code 
###  La tua prima estensione 
Crea la tua prima estensione "Hello World", per acquisire familiarità con il flusso di lavoro di sviluppo delle estensioni. 
code 
###  Esegui script su ogni pagina 
Scopri come aggiungere automaticamente elementi a un sito specificato. 
code 
###  Iniettare script nella scheda attiva 
Scopri come semplificare lo stile della pagina corrente facendo clic sull'icona della barra degli strumenti. 
code 
###  Creare un gestore delle schede 
Scopri come creare un popup che gestisce le tue schede. 
code 
###  Gestire gli eventi con i service worker 
Scopri come creare e eseguire il debug di un worker di servizio per le estensioni. 
code 
###  Eseguire il debug dell'estensione 
Scopri come trovare log e messaggi di errore durante il debug. 

