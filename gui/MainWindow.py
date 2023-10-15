
from PySide6.QtWidgets import *
from ui_functions import UIFunctions
from ui_mainwindow import Ui_MainWindow
from PySide6.QtGui import QIcon, QTransform
from PySide6.QtWidgets import (QAbstractItemView, QDataWidgetMapper,
    QHeaderView, QMainWindow, QMessageBox)
from PySide6.QtGui import QKeySequence
from PySide6.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlQuery
from PySide6.QtCore import Qt, Slot
import database.Model_result



import sys



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
        # self.model = Result.View()
        # self.ui.tableView.setModel(self.model)
        ## TOGGLE MENU
        self.ui.burger_btn.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        self.ui.burger_btn.clicked.connect(UIFunctions.toggle_text)


        # REPORT PAGE
        self.ui.report_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_report))

        # CHART PAGE
        self.ui.chart_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_chart))

        # RESULT PAGE
        self.ui.result_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_result))

        # SETTING PAGE
        self.ui.setting_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_setting))

        self.ui.btn_open_extension_search.clicked.connect(UIFunctions.open_dialog_search)

        self.ui.btn_check_conn_database.clicked.connect(UIFunctions.check_connection_database)

        database.Model_result.init_db()


        model = QSqlRelationalTableModel(self.ui.tableView)
        model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        model.setTable("tests")

        # filter_query = QSqlQuery()
        # filter_condition = "SELECT * FROM tests where test_name like 'HPCG'"
        # filter_query.exec(filter_condition)
        #
        # model.setQuery(filter_query)




        # Remember the indexes of the columns:
        # author_idx = model.fieldIndex("tests")
        # genre_idx = model.fieldIndex("users")
        #
        # # Set the relations to the other database tables:
        # model.setRelation(author_idx, QSqlRelation("authors", "id", "name"))
        # model.setRelation(genre_idx, QSqlRelation("genres", "id", "name"))

        # Set the localized header captions:
        # model.setHeaderData(author_idx, Qt.Horizontal, self.tr("Author Name"))
        # model.setHeaderData(genre_idx, Qt.Horizontal, self.tr("Genre"))


        model.setHeaderData(model.fieldIndex("test_name"), Qt.Horizontal, self.tr("Test Name"))
        model.setHeaderData(model.fieldIndex("test_param"), Qt.Horizontal, self.tr("Test Parametrs"))
        model.setHeaderData(model.fieldIndex("test_note"), Qt.Horizontal, self.tr("Note to the test"))
        model.setHeaderData(model.fieldIndex("test_id"), Qt.Horizontal, self.tr("ID Теста"))
        model.setHeaderData(model.fieldIndex("start_test"), Qt.Horizontal, self.tr("Test date"))
        model.setHeaderData(model.fieldIndex("time_test"), Qt.Horizontal, self.tr("Test execution time"))

        if not model.select():
            print(model.lastError())

        self.ui.tableView.setModel(model)
        self.ui.tableView.setColumnHidden(model.fieldIndex('test_id'), True)
        self.ui.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.header = self.ui.tableView.horizontalHeader()
        self.header.setSectionResizeMode(QHeaderView.Stretch)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec())