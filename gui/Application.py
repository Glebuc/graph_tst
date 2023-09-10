from PySide6.QtWidgets import QApplication
from PySide6.QtSql import QSqlDatabase


class Application(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        # db = QSqlDatabase.addDatabase("QPSQL")
        # db.setHostName(config_db.db_params["host"])
        # db.setDatabaseName(config_db)

