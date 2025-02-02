# README

このプロジェクトは、LangChainを使用してPDFをRAG（Retrieval-Augmented Generation）するものです。Ollamaを利用し、Dockerとuvを使用しています。

## 必要条件

- Docker
- VScode

## セットアップ

1. リポジトリをクローンします。

    ```bash
    git clone <リポジトリURL>
    cd <リポジトリディレクトリ>
    ```

2. VScodeで、コンテナを再度開く、を選択します。

3. uvで環境を構築します。

    ```bash
    uv sync --all-extras
    ```

## 使用方法

1. PDFファイルをdataディレクトリに配置します。
2. アプリケーションを起動し、指定のエンドポイントにアクセスしてPDFをRAGします。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。
