# ui/main_window.py
from automation.browser_manager import get_browser
from automation.login_handler import login_with_mfa
from automation.main_loop import run_all_checks
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel,
    QFileDialog, QProgressBar, QTextEdit
)
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авто-Проверка Сотрудников")
        self.setFixedSize(600, 400)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Загруженный файл: (не выбран)")
        self.layout.addWidget(self.label)

        self.button_load = QPushButton("Загрузить Excel")
        self.button_load.clicked.connect(self.load_excel)
        self.layout.addWidget(self.button_load)

        self.button_start = QPushButton("Начать проверку")
        self.button_start.clicked.connect(self.start_check)
        self.layout.addWidget(self.button_start)

        self.progress = QProgressBar()
        self.layout.addWidget(self.progress)

        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.layout.addWidget(self.log_output)

        self.excel_path = None

    def log(self, text):
        self.log_output.append(text)

    def load_excel(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выбери файл Excel", "", "Excel Files (*.xlsx *.xls)")
        if file_path:
            self.excel_path = file_path
            filename = os.path.basename(file_path)
            self.label.setText(f"Загруженный файл: {filename}")
            self.log(f"✅ Файл загружен: {filename}")

    def start_check(self):
        if not self.excel_path:
            self.log("❌ Сначала выбери файл Excel.")
            return
        try:
            self.driver = get_browser()
        except RuntimeError as e:
            self.log(str(e))
            return

        success = login_with_mfa(self.driver, self.log)
        if not success:
            return

        run_all_checks(self.driver, self.log, input_path=self.excel_path)