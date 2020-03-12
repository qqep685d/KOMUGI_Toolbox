# NBRP KOMUGI Toolbox

## アプリケーション
- FinDocs: ドキュメント管理データベースツール


## 経過メモ
1. プロジェクト立ち上げから設定ファイル作成
  - 参照: [DjangoアプリをHerokuにデプロイする方法](https://qiita.com/frosty/items/66f5dff8fc723387108c)
  - Herokuにデプロイ: エラー
    - `NameError: name 'dj_database_url' is not defined`
    - `import dj_database_url`を忘れていた
  - Herokuにデプロイ: エラー
    - `KeyError: 'SECRET_KEY'`
    - `heroku config:set SECRET_KEY='....'`を忘れていた
  - Herokuにデプロイ: OK
    - `python manage.py collectstatic --noinput`も正常に実行されていた
    - `heroku ps:scale web=1` ...OK
2. ユーザー機能（メールアドレスでログイン）
  - 参照: [Djangoでメールアドレスとパスワードでログインしてみる](https://qiita.com/cortyuming/items/2167a29a90c94bb4b1bb)
  - ローカル: OK
  - Herokuにデプロイ: OK
    - `heroku run python manage.py migrate` ...OK
    - `heroku run python manage.py createsuperuser` ...OK
3. ログイン、ログアウト機能
  - 参照: 
