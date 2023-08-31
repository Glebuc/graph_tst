
from PySide6.QtWidgets import *
from ui_functions import *
import sys
import qdarktheme


class Ui(QMainWindow):
    """Основное окно и подгружаемый ui-файл Qt"""
    def __init__(self, parent=None):
        super(Ui, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.setWindowTitle("TsT Graph")
        self.setWindowIcon(QIcon('./static/main_icon.svg'))
        self.setMinimumSize(800,600)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_report)
        ## TOGGLE MENU
        self.ui.burger_btn.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))


        self.ui.burger_btn.clicked.connect(lambda: UIFunctions.toggle_text(self))

        self.ui.burger_btn.clicked.connect(lambda: UIFunctions.reset_style(self))

        # self.ui.home_btn.clicked.connect(UIFunctions.set_active_btn(self))

        # REPORT PAGE
        self.ui.report_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_report))

        # CHART PAGE
        self.ui.chart_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_chart))

        # RESULT PAGE
        self.ui.result_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_result))

        # SETTING PAGE
        self.ui.setting_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_setting))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec())