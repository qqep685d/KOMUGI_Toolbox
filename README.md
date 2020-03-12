# NBRP KOMUGI Toolbox

## アプリケーション
- FinDocs: ドキュメント管理データベースツール
- account: ユーザー機能（メールアドレスでログイン）


## 経過メモ
1. プロジェクト立ち上げから設定ファイル作成
  - 基本的には「[『完全版』Djangoアプリをherokuにデプロイ！](http://digital-tree.xyz/blogs/1169)」に従った
  - データベースの設定は「[Django Girls Tutorial](https://tutorial-extensions.djangogirls.org/ja/heroku/)」に従った
  - HerokuへのSECRET_KEYの登録方法は[こちら](https://medium.com/@kjmczk/heroku-deploy-django-d2eab0a5e0ce)を参考にした
  - ここまでで、Herokuにエラーなしでデプロイされたことを確認した
2. ユーザー機能（メールアドレスでログイン）
  - 「[Djangoでメールアドレスとパスワードでログインしてみる](https://qiita.com/cortyuming/items/2167a29a90c94bb4b1bb)」の記述に従って実装した
  - ローカル: 「エラーなし」を確認
  - Heroku:
    - Herokuにて、`migrate`と`createsuperuser`を実行
    - `migrate`はOK
    - `createsuperuser`でwarningありを確認。ただし、ユーザー作成は完了
      - `pip install psycopg2-binary`を実行
      - `pip uninstall psycopg2`を実行
    - HerokuもOK
3. ログインページ、ログアウトページの実装
  - 参考: 「[Django2 でユーザー認証（ログイン認証）を実装するチュートリアル -1- 環境構築とアプリ雛形の作成](https://wonderwall.hatenablog.com/entry/2018/03/22/001500)」
  - 最低限のログイン・ログアウトページ実装は、上のサイトでできた
  - Herokuにデプロイ


- STATICFILES_DIRS、STATIC_ROOTについて
  - [違い説明](https://ja.stackoverflow.com/questions/38052/django%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8Bstatic-root-staticfiles-dirs-static-url%E3%81%AE%E9%81%95%E3%81%84%E3%81%A8%E3%81%AF)
  - [書き方例](https://medium.com/@kjmczk/django-settings-c29eb629223)
