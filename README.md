# 簡易電卓アプリ

このアプリは Flask で作成した簡易電卓アプリです。  ブラウザからアクセスして数式を入力し、計算結果を確認できます。

---

## 構成

```
┌────────────┐      ┌────────────┐       ┌─────────────┐
│  browser   │ <--> │   nginx    │ <-->  │  Gunicorn   │
└────────────┘      └────────────┘       └─────────────┘
                                               |
                                             Flask

```
---

## 動作環境
- Git
- Docker

--- 

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
    または
    ```
    http://[ホストのIPアドレス]:4000
    ```

---

## 使い方

1. ブラウザにアクセス。
2. テキストボックスに式を入力。例：`3 + 5`, `sqrt 16`
3. [計算] ボタン押下 または Enter で結果が表示される。

---

## 停止方法

```bash
docker-compose down
```