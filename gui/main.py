import sys

from Application import Application
from MainWindow import Ui
import qdarktheme

app = Application(sys.argv)
main_window = Ui()
main_window.show()

result = app.exec()
sys.exit(result)