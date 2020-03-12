# NBRP KOMUGI Toolbox

## アプリケーション
- FinDocs: ドキュメント管理データベースツール


## 経過メモ
1. プロジェクト立ち上げから設定ファイル作成
  - 参照: [DjangoアプリをHerokuにデプロイする方法](https://qiita.com/frosty/items/66f5dff8fc723387108c)
  - 
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
