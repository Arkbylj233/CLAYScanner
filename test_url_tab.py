import requests
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit


class TestUrlTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        url_label = QLabel("请输入要测试的URL:")
        self.url_entry = QLineEdit()
        test_button = QPushButton("测试")
        test_button.clicked.connect(self.test_url)
        self.result_text = QTextEdit()

        layout.addWidget(url_label)
        layout.addWidget(self.url_entry)
        layout.addWidget(test_button)
        layout.addWidget(self.result_text)

        self.setLayout(layout)

    def test_url(self):
        url = self.url_entry.text()
        if url:
            try:
                response = requests.get(url)
                self.result_text.setText(f"状态码：{response.status_code}\n响应内容：\n{response.text}")
            except requests.exceptions.RequestException as e:
                self.result_text.setText(f"发生错误：{e}")
