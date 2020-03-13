# NBRP KOMUGI Toolbox

## アプリケーション
- FinDocs: ドキュメント管理データベースツール
- account: アカウントログイン、ログアウト機能の実装（adminページも使用可能）


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
  - 参照: [Djangoのログイン処理を実装する方法①](https://intellectual-curiosity.tokyo/2018/11/13/django%E3%81%AE%E3%83%AD%E3%82%B0%E3%82%A4%E3%83%B3%E5%87%A6%E7%90%86%E3%82%92%E5%AE%9F%E8%A3%85%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95%E2%91%A0/)の前半（5.4まで）
  - ローカル: OK
  - Herokuにデプロイ: OK
  - Djangoのログイン処理を実装する方法①の後半
  - ローカル: OK
  - Herokuにデプロイ: OK
  - デプロイ時の`python manage.py collectstatic --noinput`は、以下の設定であれば問題なさそう。  
    共通のCSSやJSは作らないようにする。  
    ```
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_URL = '/static/'
    ```
4. FinDocsアプリの実装
  - 事前作成アプリをコピー
  - ローカル: OK
  - Herokuにデプロイ: 
