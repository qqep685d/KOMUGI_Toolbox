# NBRP KOMUGI Toolbox

## アプリケーション
- FinDocs: ドキュメント管理データベースツール
- Accounts: ユーザー機能


## 参考
- [開発用と本番用にDjangoの設定ファイルを分割する](https://medium.com/@kjmczk/django-multiple-settings-2a4c15c7c7b0)
  - データベースについても各ファイルに記載: 「Herokuへのアップロード」を参考にした。
- [Herokuへのアップロード](https://tutorial-extensions.djangogirls.org/ja/heroku/)
  - migrate前までを参照した
  - 設定ファイルについては、上で設定した通りにした
  - つまづいた箇所
    - [whitenoise 4.0を使う場合の注意点](https://qiita.com/ymhr1121/items/344c4eb300ab9972d0c2)
    - [python manage.py collectstatic --noinput'のエラー](https://thinkami.hatenablog.com/entry/2017/01/13/053643)
    - [SECRET_KEYが設定されていないと言われるエラー](https://medium.com/@kjmczk/heroku-deploy-django-d2eab0a5e0ce)

- [ユーザー機能（ログイン、ログアウト）の実装](https://narito.ninja/blog/detail/39/)
