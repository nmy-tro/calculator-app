# 簡易電卓アプリ

このアプリは Flask で作成した簡易電卓アプリです。  ブラウザからアクセスして数式を入力し、計算結果を確認できます。

Docker と nginx を使ったこのアプリの構成と構築手順を以下に示します。

---

## 構成

```
リクエスト
   ↓
┌────────────┐      ┌────────────┐       ┌─────────────┐
│  browser   │ ---> │   nginx    │ --->  │   gunicorn  │
└────────────┘      └────────────┘       └─────────────┘
                                    ↑
                                  Flask

```

<!-- ```text
.
├── app/                  # Flask アプリ本体
│   ├── app.py
│   ├── templates/index.html
│   ├── requirements.txt
│   └── Dockerfile
├── nginx/                # nginx の設定ファイル
│   └── nginx.conf
└── docker-compose.yml    # コンテナ構成定義
```

--- -->

## 起動手順

1. このリポジトリをクローンまたはダウンロード。

    ```bash
    git clone https://github.com/nmy-tro/calculator-app.git
    cd calculator-app
    ```

2. コンテナをビルドしてバッググラウンドで起動。

    ```bash
    docker-compose up --build -d
    ```

3. ブラウザでアクセス。

    ```
    http://localhost:4000
    ```

---

## 使い方

1. ブラウザにアクセス
2. テキストボックスに式を入力（例：`3 + 5`, `sqrt 16` など）
3. [計算] ボタン押下 or Enter で結果が表示される

---

## 停止方法

```bash
docker-compose down
```

## 補足
- nginx はリバースプロキシとして動作し、Flask アプリ（web コンテナ）にリクエストを転送します。