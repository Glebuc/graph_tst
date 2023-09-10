import sys

from Application import Application
from MainWindow import Ui


app = Application(sys.argv)
main_window = Ui()
main_window.show()

result = app.exec()
sys.exit(result)