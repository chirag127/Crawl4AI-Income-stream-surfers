---
url: https://developer.chrome.com/docs/extensions/get-started?hl=es-419
title: https://developer.chrome.com/docs/extensions/get-started?hl=es-419
date: 2025-05-11T16:52:01.674270
depth: 1
---

[ Ir al contenido principal ](https://developer.chrome.com/docs/extensions/get-started?hl=es-419#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/extensions/get-started?hl=es-419)




Se usó la [API de Cloud Translation](https://cloud.google.com/translate/?hl=es-419) para traducir esta página. 


###  Comenzar 
Te damos la bienvenida al desarrollo de extensiones de Chrome. Descubre todo lo que necesitas para comenzar a compilar y distribuir tu primera extensión de Chrome. 
[Compila tu primera extensión](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world?hl=es-419) [Ver todos los instructivos](https://developer.chrome.com/docs/extensions/get-started?hl=es-419#tutorials)
###  ¿Qué son las extensiones? 
Las extensiones de Chrome mejoran la experiencia de navegación personalizando la interfaz de usuario, observando eventos del navegador y modificando la Web. Visita [Chrome Web Store](https://chromewebstore.google.com/?hl=es-419) para ver más ejemplos de lo que pueden hacer las extensiones. 
###  ¿Cómo se construyen? 
Puedes compilar extensiones con las mismas tecnologías web que se usan para crear aplicaciones web: [HTML](https://web.dev/learn/html?hl=es-419), [CSS](https://web.dev/learn/css?hl=es-419) y [JavaScript](https://developer.mozilla.org/docs/Learn/JavaScript). 
###  ¿Qué pueden hacer? 
Además de las [APIs web](https://developer.mozilla.org/docs/Web/API), las extensiones también tienen acceso a las [APIs de extensiones de Chrome](https://developer.chrome.com/docs/extensions/reference?hl=es-419) para realizar diferentes tareas. Para obtener una descripción general más detallada, consulta la [guía de desarrollo](https://developer.chrome.com/docs/extensions/develop?hl=es-419). 
[ article  ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=es-419)
###  [ Manifiesto ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=es-419)
El manifiesto de la extensión es el único archivo obligatorio que debe tener un nombre de archivo específico: manifest.json. También debe estar ubicado en el directorio raíz de la extensión. El manifiesto registra metadatos importantes, define recursos, declara permisos y, además, identifica qué archivos se ejecutarán en segundo plano y en la página. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=es-419)
###  [ Service workers ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=es-419)
Un trabajador de servicio se ejecuta en segundo plano y controla los eventos del navegador, como quitar un favorito o cerrar una pestaña. No tienen acceso al DOM, pero puedes combinarlo con un documento fuera de pantalla para este caso de uso. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=es-419)
###  [ Secuencias de comandos de contenido ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=es-419)
Las secuencias de comandos de contenido ejecutan JavaScript en el contexto de una página web. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=es-419)
###  [ Acción de la barra de herramientas ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=es-419)
Ejecuta código cuando el usuario hace clic en el ícono de la barra de herramientas de la extensión o muestra una ventana emergente con la API de Action. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=es-419)
###  [ Panel lateral ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=es-419)
Muestra la IU personalizada en el panel lateral del navegador. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=es-419)
###  [ DeclarativeNetRequest ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=es-419)
Interceptar, bloquear o modificar solicitudes de red 
palette 
###  Diseña una extensión de alta calidad 
Cuando elijas qué funciones admitir, asegúrate de que tu extensión cumpla con un [propósito único](https://developer.chrome.com/docs/webstore/program-policies/quality-guidelines-faq?hl=es-419) que esté definido de forma clara y sea fácil de entender. 
build 
###  Familiarízate con las políticas 
Las extensiones que se distribuyen en Chrome Web Store deben cumplir con las [políticas del programa para desarrolladores](https://developer.chrome.com/docs/webstore/program-policies?hl=es-419). Explora estas políticas para asegurarte de que tu extensión se pueda alojar en Chrome Web Store. 
cloud_off 
###  Cómo incluir toda la lógica de la extensión 
Cuando escribas el código, ten en cuenta que toda la lógica debe incluirse en el paquete de extensiones. Esto significa que no se puede descargar código JavaScript adicional durante el tiempo de ejecución. [Mejorar la seguridad de las extensiones](https://developer.chrome.com/docs/extensions/migrating/improve-security?hl=es-419) proporciona alternativas para ejecutar código alojado de forma remota. 
code 
###  Tu primera extensión 
Crea tu primera extensión de Hola mundo, en la que te familiarizarás con el flujo de trabajo de desarrollo de extensiones. 
code 
###  Ejecuta secuencias de comandos en cada página 
Aprende a agregar elementos automáticamente a un sitio específico. 
code 
###  Cómo insertar secuencias de comandos en la pestaña activa 
Haz clic en el ícono de la barra de herramientas para aprender a simplificar el estilo de la página actual. 
code 
###  Cómo crear un administrador de pestañas 
Aprende a crear una ventana emergente que administre tus pestañas. 
code 
###  Controla eventos con service workers 
Aprende a crear y depurar un trabajador de servicio de extensión. 
code 
###  Cómo depurar tu extensión 
Aprende a encontrar registros y mensajes de error durante la depuración. 

