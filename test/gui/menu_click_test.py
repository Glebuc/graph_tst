import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtTest import QTest

def test_input_value():
    app = QApplication(sys.argv)
    window = QMainWindow()
    input_field = QLineEdit(window)

    QTest.keyClicks(input_field, "Initial value")
    assert input_field.text() == "Initial value"

    QTest.keyClicks(input_field, "New value")
    assert input_field.text() == "New value"

    app.exec()

test_input_value()