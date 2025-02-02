import os

import pytest

from ollama_rag.chatpdf import ChatPDF


@pytest.fixture
def sample_pdf():
    # テスト用のPDFファイルパスを返す
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(current_dir, "test_data", "sample.pdf")
    if not os.path.exists(pdf_path):
        pytest.skip("Test PDF file not found")
    return pdf_path


@pytest.fixture
def chat_pdf(tmp_path):
    return ChatPDF(
        model="phi4",
        base_url="http://host.docker.internal:11434",
        persist_directory=str(tmp_path / "test_db"),
    )


def test_learn_pdf(chat_pdf, sample_pdf):
    # PDFの学習をテスト
    chat_pdf.learn(sample_pdf)
    assert chat_pdf.db is not None


def test_ask_without_pdf(chat_pdf):
    # PDF追加前の質問テスト
    chat_pdf.clear()  # 既存のデータをクリア
    response = chat_pdf.ask("What is in the document?")
    assert "Please, add a PDF document first." in response


def test_ask_with_pdf(chat_pdf, sample_pdf):
    # PDF追加後の質問テスト
    chat_pdf.learn(sample_pdf)
    response = chat_pdf.ask("What is in the document?")
    assert isinstance(response, str)
    assert len(response) > 0


def test_clear(chat_pdf, sample_pdf):
    # クリア機能のテスト
    chat_pdf.learn(sample_pdf)
    chat_pdf.clear()
    assert chat_pdf.vector_store is None
    assert chat_pdf.retriever is None
    assert chat_pdf.chain is None
