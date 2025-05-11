---
url: https://developer.chrome.com/docs/extensions/get-started?hl=pt-br
title: https://developer.chrome.com/docs/extensions/get-started?hl=pt-br
date: 2025-05-11T16:52:10.207232
depth: 1
---

[ Ir para o conteúdo principal ](https://developer.chrome.com/docs/extensions/get-started?hl=pt-br#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/extensions/get-started?hl=es-419)




Esta página foi traduzida pela [API Cloud Translation](https://cloud.google.com/translate/?hl=pt-br). 


###  Começar 
Este é o desenvolvimento de extensões do Chrome. Descubra tudo o que você precisa para começar a criar e distribuir sua primeira extensão do Chrome. 
[Criar sua primeira extensão](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world?hl=pt-br) [Ver todos os tutoriais](https://developer.chrome.com/docs/extensions/get-started?hl=pt-br#tutorials)
###  O que são extensões? 
As extensões do Chrome melhoram a experiência de navegação ao personalizar a interface do usuário, observar eventos do navegador e modificar a Web. Acesse a [Chrome Web Store](https://chromewebstore.google.com/?hl=pt-br) para conferir mais exemplos do que as extensões podem fazer. 
###  Como elas são criadas? 
É possível criar extensões usando as mesmas tecnologias da Web usadas para criar aplicativos da Web: [HTML](https://web.dev/learn/html?hl=pt-br), [CSS](https://web.dev/learn/css?hl=pt-br) e [JavaScript](https://developer.mozilla.org/docs/Learn/JavaScript). 
###  O que ela pode fazer? 
Além das [APIs da Web](https://developer.mozilla.org/docs/Web/API), as extensões também têm acesso às [APIs de extensão do Chrome](https://developer.chrome.com/docs/extensions/reference?hl=pt-br) para realizar tarefas diferentes. Para uma visão geral mais detalhada, consulte o [guia de desenvolvimento](https://developer.chrome.com/docs/extensions/develop?hl=pt-br). 
[ article  ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=pt-br)
###  [ Manifesto ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=pt-br)
O manifesto da extensão é o único arquivo obrigatório que precisa ter um nome de arquivo específico: manifest.json. Ele também precisa estar localizado no diretório raiz da extensão. O manifesto registra metadados importantes, define recursos, declara permissões e identifica quais arquivos serão executados em segundo plano e na página. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=pt-br)
###  [ Service workers ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=pt-br)
Um worker de serviço é executado em segundo plano e processa eventos do navegador, como remover um marcador ou fechar uma guia. Eles não têm acesso ao DOM, mas você pode combiná-los com um documento fora da tela para esse caso de uso. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=pt-br)
###  [ Scripts de conteúdo ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=pt-br)
Os scripts de conteúdo executam JavaScript no contexto de uma página da Web. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=pt-br)
###  [ Ação da barra de ferramentas ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=pt-br)
Executar código quando o usuário clica no ícone da barra de ferramentas da extensão ou mostrar um pop-up usando a API Action. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=pt-br)
###  [ Painel lateral ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=pt-br)
Mostrar a interface personalizada no painel lateral do navegador. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=pt-br)
###  [ DeclarativeNetRequest ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=pt-br)
Interceptar, bloquear ou modificar solicitações de rede. 
palette 
###  Projetar uma extensão de alta qualidade 
Ao escolher os recursos que serão compatíveis, verifique se a extensão atende a um [único propósito](https://developer.chrome.com/docs/webstore/program-policies/quality-guidelines-faq?hl=pt-br) que seja bem definido e fácil de entender. 
build 
###  Conheça as políticas 
As extensões distribuídas na Chrome Web Store precisam obedecer às [políticas do programa para desenvolvedores](https://developer.chrome.com/docs/webstore/program-policies?hl=pt-br). Confira estas políticas para garantir que sua extensão possa ser hospedada na Chrome Web Store. 
cloud_off 
###  Incluir toda a lógica de extensão 
Ao escrever o código, lembre-se de que toda a lógica precisa ser incluída no pacote de extensão. Isso significa que nenhum código JavaScript adicional pode ser transferido por download no momento da execução. [Melhorar a segurança da extensão](https://developer.chrome.com/docs/extensions/migrating/improve-security?hl=pt-br) oferece alternativas para executar o código hospedado remotamente. 
code 
###  Sua primeira extensão 
Crie sua primeira extensão "hello world" para se familiarizar com o fluxo de trabalho de desenvolvimento de extensões. 
code 
###  Executar scripts em todas as páginas 
Aprenda a adicionar elementos automaticamente a um site específico. 
code 
###  Injete scripts na guia ativa 
Aprenda a simplificar o estilo da página atual clicando no ícone da barra de ferramentas. 
code 
###  Criar um gerenciador de guias 
Aprenda a criar um pop-up que gerencia suas guias. 
code 
###  Processar eventos com service workers 
Aprenda a criar e depurar um worker de serviço de extensão. 
code 
###  Depurar a extensão 
Aprenda a encontrar registros e mensagens de erro durante a depuração. 

