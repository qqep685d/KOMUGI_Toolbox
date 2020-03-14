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
  - Herokuにデプロイ: FinDocsページが`Server Error (500)`
  - CSS,JSをファイル読み込みからCDNに変更
  - Herokuにデプロイ: NG
  - `ALLOWED_HOSTS = ['*']`に変更
  - Herokuにデプロイ: NG
  - `{% loac i18n static %}` => `{% loac static %}`
  - Herokuにデプロイ: NG
  - psycopg2について、requrements.txt更新
  - Herokuアプリの削除:
    - `heroku destroy --app komugi-toolbox --confirm komugi-toolbox`
  - Herokuアプリ再作成:
    - `heroku create komugi-toolbox`
    - `heroku config:set SECRET_KEY=`
    - `heroku ps:scale web=1`
    - `heroku run python manage.py migrate`
    - `heroku run python manage.py createsuperuser`
  - Herokuにデプロイ: NG
  - 削除`STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'`
  - Herokuにデプロイ: NG
  - wsgiを編集:
    - `from dj_static import Cling`
    - `application = Cling(get_wsgi_application())`
  - Herokuにデプロイ: NG
    - `from dj_static import Cling` in wsgi.py
  - `pip install dj-static`
  - `pip freeze > requirements.txt`
  - asgi.pyの全コードをコメントアウト
  - Herokuにデプロイ: NG
  - [この](https://getbootstrap.jp/docs/4.3/getting-started/introduction/)説明に従って、<script>の位置を変更
  - Herokuにデプロイ: NG
  - ログイン画面に各種bootstrap用のCDNを入れてみてどうなるかみてみる
  - Herokuにデプロイ: NG
  - runtime.txtを変更: python-3.7.3 => python-3.7.6
  - Herokuにデプロイ: NG
  - ログイン画面に各種JSを入れてみてどうなるかみてみる
  - Herokuにデプロイ: NG
  - DEBAG=TRUEで試す
    - 詳細がはっきりわかるので、これでうまくいくように修正していく
    - django/template/backends/django.py in reraise, line 84
    - アプリ内のテンプレートの位置は階層的にすると、エラーが出るようだ
  - アプリ再構築
  - `heroku destroy --app komugi-toolbox --confirm komugi-toolbox`
  - `heroku create komugi-toolbox`
  - `heroku config:set SECRET_KEY=`
  - `heroku ps:scale web=1`
  - `heroku run python manage.py migrate`
  - `heroku run python manage.py createsuperuser`
  - Herokuにデプロイ: OK
