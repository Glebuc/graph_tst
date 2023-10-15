from PySide6.QtWidgets import QApplication
from PySide6.QtSql import QSqlDatabase
import config_db as dbc
import logging


LOG = logging.getLogger(__name__)
class Application(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        db = QSqlDatabase.addDatabase('QPSQL')
        db.setHostName(dbc.db_params['host'])
        db.setDatabaseName(dbc.db_params['database'])
        db.setPort(dbc.db_params['port'])
        db.setUserName(dbc.db_params['user'])
        db.setPassword(dbc.db_params['password'])
        ok = db.open()
        if ok:
            print('ok')
            LOG.info(f'Connected to database {dbc.db_params["database"]}')
        else:
            LOG.error('Connection FAILED')

