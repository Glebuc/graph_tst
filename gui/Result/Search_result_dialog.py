from PySide6.QtWidgets import QDialog, QPushButton, QVBoxLayout


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Диалоговое окно")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.button = QPushButton("Закрыть диалог")
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.accept)
