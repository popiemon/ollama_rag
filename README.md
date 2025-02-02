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

4. Ollamaのbase urlとモデルを設定します。
    run/conf/config.yamlの、ollama_baseurlにbase urlを、modelにollamaサーバにデプロイしたモデル名を設定します。

    テストは、localhostのサーバにphi3.5がデプロイされていることが前提となっています。

## 使用方法

1. PDFファイルをdataディレクトリに配置します。
2. 学習します。
    ```bash
    python3 run/learning.py
    ```
3. 推論します。
    ```bash
    python3 run/inference.py
    ```

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。
