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

2. VScodeで、拡張機能のDev Containersをインストールし、コンテナを再度開く、を選択します。

3. Ollamaのbase urlとモデルを設定します。
    `run/conf/config.yaml`の、ollama_baseurlにbase urlを、modelにollamaサーバにデプロイしたモデル名を設定します。

    base_urlが空白の場合、localhost:11434が適用されます。

    テストは、localhostのサーバにphi3.5がデプロイされていることが前提となっています。

4. `run/conf/config.yaml`のpdf_dir, persist_directoryを設定する。
    ```yaml
    pdf_dir : pdfファイルのフォルダ。
    persist_directory : dbのフォルダ。
    ```

5. PDFファイルをpdf_dirディレクトリに配置します。


## 使用方法

1. 学習します。
    ```bash
    python3 run/learning.py
    ```
2. 推論します。
    ```bash
    python3 run/inference.py
    ```

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。
