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
    - `heroku ps:scale web=1`実施
    - `heroku run python manage.py migrate`実施

2. ユーザー機能（メールアドレスでログイン）
  - 参照: [Djangoでメールアドレスとパスワードでログインしてみる](https://qiita.com/cortyuming/items/2167a29a90c94bb4b1bb)
  - ローカル: 「エラーなし」を確認
  - Heroku:
    - Herokuにて、`migrate`と`createsuperuser`を実行
    - `migrate`はOK
    - `createsuperuser`でwarningありを確認。ただし、ユーザー作成は完了
      - `pip install psycopg2-binary`を実行
      - `pip uninstall psycopg2`を実行
    - HerokuもOK
