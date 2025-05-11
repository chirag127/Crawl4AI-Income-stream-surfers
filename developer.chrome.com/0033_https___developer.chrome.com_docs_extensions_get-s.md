---
url: https://developer.chrome.com/docs/extensions/get-started?hl=fr
title: https://developer.chrome.com/docs/extensions/get-started?hl=fr
date: 2025-05-11T16:52:01.700779
depth: 1
---

[ Passer au contenu principal ](https://developer.chrome.com/docs/extensions/get-started?hl=fr#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/extensions/get-started?hl=es-419)




Cette page a été traduite par l'[API Cloud Translation](https://cloud.google.com/translate/?hl=fr). 


###  Premiers pas 
Bienvenue dans le développement d'extensions Chrome. Découvrez tout ce dont vous avez besoin pour commencer à créer et à distribuer votre première extension Chrome. 
[Créer votre première extension](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world?hl=fr) [Voir tous les tutoriels](https://developer.chrome.com/docs/extensions/get-started?hl=fr#tutorials)
###  Que sont les extensions ? 
Les extensions Chrome améliorent l'expérience de navigation en personnalisant l'interface utilisateur, en observant les événements du navigateur et en modifiant le Web. Consultez le [Chrome Web Store](https://chromewebstore.google.com/?hl=fr) pour découvrir d'autres exemples de ce que les extensions peuvent faire. 
###  Comment sont-elles créées ? 
Vous pouvez créer des extensions à l'aide des mêmes technologies Web que celles utilisées pour créer des applications Web: [HTML](https://web.dev/learn/html?hl=fr), [CSS](https://web.dev/learn/css?hl=fr) et [JavaScript](https://developer.mozilla.org/docs/Learn/JavaScript). 
###  Que peut-il faire ? 
En plus des [API Web](https://developer.mozilla.org/docs/Web/API), les extensions ont également accès aux [API d'extension Chrome](https://developer.chrome.com/docs/extensions/reference?hl=fr) pour effectuer différentes tâches. Pour en savoir plus, consultez le [guide de développement](https://developer.chrome.com/docs/extensions/develop?hl=fr). 
[ article  ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=fr)
###  [ Fichier manifeste ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=fr)
Le fichier manifeste de l'extension est le seul fichier obligatoire qui doit porter un nom de fichier spécifique: manifest.json. Il doit également se trouver dans le répertoire racine de l'extension. Le fichier manifeste enregistre des métadonnées importantes, définit des ressources, déclare des autorisations et identifie les fichiers à exécuter en arrière-plan et sur la page. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=fr)
###  [ Service workers ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=fr)
Un service worker s'exécute en arrière-plan et gère les événements du navigateur, comme la suppression d'un favori ou la fermeture d'un onglet. Ils n'ont pas accès au DOM, mais vous pouvez les combiner à un document hors écran pour ce cas d'utilisation. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=fr)
###  [ Scripts de contenu ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=fr)
Les scripts de contenu exécutent JavaScript dans le contexte d'une page Web. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=fr)
###  [ Action de la barre d'outils ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=fr)
Exécutez du code lorsque l'utilisateur clique sur l'icône de la barre d'outils de l'extension ou affichez une fenêtre pop-up à l'aide de l'API Action. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=fr)
###  [ Panneau latéral ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=fr)
Affichez une UI personnalisée dans le panneau latéral du navigateur. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=fr)
###  [ DeclarativeNetRequest ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=fr)
Intercepter, bloquer ou modifier des requêtes réseau 
palette 
###  Concevoir une extension de haute qualité 
Lorsque vous choisissez les fonctionnalités à prendre en charge, assurez-vous que votre extension a un [seul objectif](https://developer.chrome.com/docs/webstore/program-policies/quality-guidelines-faq?hl=fr), qui est défini de manière précise et facile à comprendre. 
build 
###  Familiarisez-vous avec les règles 
Les extensions distribuées sur le Chrome Web Store doivent respecter le [Règlement du programme pour les développeurs](https://developer.chrome.com/docs/webstore/program-policies?hl=fr). Consultez ces règles pour vous assurer que votre extension peut être hébergée sur le Chrome Web Store. 
cloud_off 
###  Inclure toute la logique de l'extension 
Lorsque vous écrivez votre code, n'oubliez pas que toute logique doit être incluse dans le package d'extension. Cela signifie qu'aucun code JavaScript supplémentaire ne peut être téléchargé au moment de l'exécution. [Améliorer la sécurité des extensions](https://developer.chrome.com/docs/extensions/migrating/improve-security?hl=fr) propose des alternatives à l'exécution du code hébergé à distance. 
code 
###  Votre première extension 
Créez votre première extension "Hello World", qui vous permettra de vous familiariser avec le workflow de développement d'extensions. 
code 
###  Exécuter des scripts sur chaque page 
Découvrez comment ajouter automatiquement des éléments à un site spécifié. 
code 
###  Injecter des scripts dans l'onglet actif 
Découvrez comment simplifier le style de la page actuelle en cliquant sur l'icône de la barre d'outils. 
code 
###  Créer un gestionnaire d'onglets 
Découvrez comment créer une fenêtre pop-up qui gère vos onglets. 
code 
###  Gérer les événements avec des service workers 
Découvrez comment créer et déboguer un service worker d'extension. 
code 
###  Déboguer votre extension 
Découvrez comment trouver des journaux et des messages d'erreur pendant le débogage. 

