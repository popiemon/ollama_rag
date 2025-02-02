import os

import pytest
from reportlab.pdfgen import canvas


@pytest.fixture(autouse=True)
def setup_test_env(tmp_path):
    # テスト用のデータディレクトリを作成
    test_data_dir = os.path.join(os.path.dirname(__file__), "test_data")
    os.makedirs(test_data_dir, exist_ok=True)

    # テスト用のPDFファイルを作成
    pdf_path = os.path.join(test_data_dir, "sample.pdf")
    c = canvas.Canvas(pdf_path)
    c.drawString(100, 750, "This is a test PDF document.")
    c.drawString(100, 700, "It contains some sample text for testing.")
    c.save()

    yield

    # テスト後のクリーンアップ
    if os.path.exists(pdf_path):
        os.remove(pdf_path)
