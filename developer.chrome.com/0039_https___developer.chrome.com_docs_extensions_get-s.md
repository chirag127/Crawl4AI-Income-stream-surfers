---
url: https://developer.chrome.com/docs/extensions/get-started?hl=ja
title: https://developer.chrome.com/docs/extensions/get-started?hl=ja
date: 2025-05-11T16:52:07.131269
depth: 1
---

[ メイン コンテンツにスキップ ](https://developer.chrome.com/docs/extensions/get-started?hl=ja#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/extensions/get-started?hl=es-419)




このページは [Cloud Translation API](https://cloud.google.com/translate/?hl=ja) によって翻訳されました。 


###  使ってみる 
Chrome 拡張機能の開発へようこそ。最初の Chrome 拡張機能の作成と配布を開始するために必要な情報をすべて確認できます。 
###  拡張機能とは 
Chrome 拡張機能は、ユーザー インターフェースのカスタマイズ、ブラウザ イベントの監視、ウェブの変更によってブラウジング エクスペリエンスを向上させます。拡張機能の機能の例については、[Chrome ウェブストア](https://chromewebstore.google.com/?hl=ja)をご覧ください。 
###  どのように構築されているか 
ウェブアプリの作成に使用されるウェブ技術（[HTML](https://web.dev/learn/html?hl=ja)、[CSS](https://web.dev/learn/css?hl=ja)、[JavaScript](https://developer.mozilla.org/docs/Learn/JavaScript)）を使用して拡張機能を作成できます。 
###  お客様はどのように対処できますか？ 
拡張機能は、[Web API](https://developer.mozilla.org/docs/Web/API) に加えて、[Chrome Extension API](https://developer.chrome.com/docs/extensions/reference?hl=ja) にもアクセスして、さまざまなタスクを実行できます。詳細については、[開発ガイド](https://developer.chrome.com/docs/extensions/develop?hl=ja)をご覧ください。 
[ article  ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=ja)
###  [ マニフェスト ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=ja)
拡張機能のマニフェストは、特定のファイル名（manifest.json）が必要な唯一の必須ファイルです。また、拡張機能のルート ディレクトリに配置する必要があります。マニフェストは、重要なメタデータを記録し、リソースを定義し、権限を宣言し、バックグラウンドとページで実行するファイルを識別します。 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=ja)
###  [ Service Worker ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=ja)
サービス ワーカーはバックグラウンドで実行され、ブックマークの削除やタブの閉じ方などのブラウザ イベントを処理します。これらの API は DOM にアクセスできませんが、このユースケースでは画面外ドキュメントと組み合わせることができます。 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=ja)
###  [ コンテンツ スクリプト ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=ja)
コンテンツ スクリプトは、ウェブページのコンテキストで JavaScript を実行します。 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=ja)
###  [ ツールバーのアクション ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=ja)
ユーザーが拡張機能のツールバー アイコンをクリックしたとき、または Action API を使用してポップアップを表示したときにコードを実行します。 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=ja)
###  [ サイドパネル ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=ja)
ブラウザのサイドパネルにカスタム UI を表示します。 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=ja)
###  [ DeclarativeNetRequest ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=ja)
ネットワーク リクエストをインターセプト、ブロック、変更する。 
palette 
###  高品質な拡張機能を設計する 
サポートする機能を選ぶ際は、拡張機能が、範囲を限定し、わかりやすい[単一の目的](https://developer.chrome.com/docs/webstore/program-policies/quality-guidelines-faq?hl=ja)を果たすようにしてください。 
build 
###  ポリシーを理解する 
Chrome ウェブストアで配布される拡張機能は、[デベロッパー プログラム ポリシー](https://developer.chrome.com/docs/webstore/program-policies?hl=ja)に準拠している必要があります。拡張機能を Chrome ウェブストアでホストできるようにするには、これらのポリシーを確認してください。 
cloud_off 
###  すべての拡張機能ロジックを含める 
コードを記述する際は、すべてのロジックを拡張機能のパッケージに含める必要があることに注意してください。つまり、ランタイム時に追加の JavaScript コードをダウンロードすることはできません。[拡張機能のセキュリティを強化する](https://developer.chrome.com/docs/extensions/migrating/improve-security?hl=ja)には、リモートでホストされるコードを実行する代替手段が用意されています。 
code 
###  最初の拡張機能 
最初の「Hello World」拡張機能を作成して、拡張機能の開発ワークフローに慣れましょう。 
code 
###  すべてのページでスクリプトを実行する 
指定したサイトに要素を自動的に追加する方法を学びます。 
code 
###  アクティブなタブにスクリプトを挿入する 
ツールバー アイコンをクリックして、現在のページのスタイルを簡素化する方法を学びます。 
code 
###  タブマネージャーを作成する 
タブを管理するポップアップを作成する方法を学びます。 
code 
###  Service Worker でイベントを処理する 
拡張機能サービス ワーカーの作成とデバッグについて学習する。 
code 
###  拡張機能をデバッグする 
デバッグ中にログとエラー メッセージを探す方法を学びます。 

