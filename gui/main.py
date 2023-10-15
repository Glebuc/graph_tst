import sys
import logging

from Application import Application
from MainWindow import Ui

logging.basicConfig(encoding='utf-8', level=logging.WARNING)

app = Application(sys.argv)
main_window = Ui()
main_window.show()

result = app.exec()
sys.exit(result)