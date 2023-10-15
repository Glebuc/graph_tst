import sys
import logging

from Application import Application
from MainWindow import Ui

<<<<<<< HEAD
logging.basicConfig(encoding='utf-8', level=logging.WARNING)
=======
>>>>>>> 44a8b5de9471abfcbb75ecf4669588d1052dbeda

app = Application(sys.argv)
main_window = Ui()
main_window.show()

result = app.exec()
sys.exit(result)