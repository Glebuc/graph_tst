from PySide6.QtSql import QSqlDatabase, QSqlQuery
from datetime import date
import config_db as dbc
import psycopg2

def add_book(q, title, year, authorId, genreId, rating):
    q.addBindValue(title)
    q.addBindValue(year)
    q.addBindValue(authorId)
    q.addBindValue(genreId)
    q.addBindValue(rating)
    q.exec()


def add_genre(q, name):
    q.addBindValue(name)
    q.exec()
    return q.lastInsertId()


def add_author(q, name, birthdate):
    q.addBindValue(name)
    q.addBindValue(str(birthdate))
    q.exec()
    return q.lastInsertId()


USERS_SQL = """
    CREATE TABLE IF NOT EXISTS users (
	user_id serial4 NOT NULL,
	user_name varchar NOT NULL,
	fio_user varchar NULL,
	email_user varchar NULL,
	password_user varchar NULL,
	CONSTRAINT users_pk PRIMARY KEY (user_id)
);
    """
TESTS_SQL = """
    CREATE TABLE IF NOT EXISTS tests (
	test_name varchar NOT NULL,
	test_param varchar NULL,
	test_note text NULL,
	test_id serial4 NOT NULL,
	id_user_fk int4 NULL,
	start_test timestamp NULL,
	time_test time NULL,
	CONSTRAINT tests_pk PRIMARY KEY (test_id),
	CONSTRAINT tests_fk FOREIGN KEY (id_user_fk) REFERENCES users(user_id)
);
    """
REPORT_SQL = """
    CREATE TABLE IF NOT EXISTS report (
	id_report serial4 NOT NULL,
	user_id_fk int4 NULL,
	forming_report timestamp NOT NULL,
	title_report varchar NOT NULL,
	CONSTRAINT report_pk PRIMARY KEY (id_report),
	CONSTRAINT report_fk FOREIGN KEY (user_id_fk) REFERENCES users(user_id)
);
    """
SETTING_SQL = """
CREATE TABLE IF NOT EXISTS settings (
	setting_id serial4 NOT NULL,
	theme varchar NOT NULL,
	"language" varchar NOT NULL,
	"scale" int4 NOT NULL DEFAULT 100,
	user_id_fk int4 NOT NULL,
	CONSTRAINT settings_pk PRIMARY KEY (setting_id),
	CONSTRAINT settings_fk FOREIGN KEY (user_id_fk) REFERENCES users(user_id)
);"""


# INSERT_AUTHOR_SQL = """
#     insert into authors(name, birthdate) values(?, ?)
#     """
# INSERT_GENRE_SQL = """
#     insert into genres(name) values(?)
#     """
# INSERT_BOOK_SQL = """
#     insert into books(title, year, author, genre, rating)
#                 values(?, ?, ?, ?, ?)
#     """


def init_db():
    """
    init_db()
    Initializes the database.
    If tables "books" and "authors" are already in the database, do nothing.
    Return value: None or raises ValueError
    The error value is the QtSql error instance.
    """

    db = QSqlDatabase.addDatabase('QPSQL')
    db.setHostName(dbc.db_params['host'])
    db.setDatabaseName(dbc.db_params['database'])
    db.setPort(dbc.db_params['port'])
    db.setUserName(dbc.db_params['user'])
    db.setPassword(dbc.db_params['password'])

    def check(func, *args):
        if not func(*args):
            raise ValueError(func.__self__.lastError())

    check(db.open)

    q = QSqlQuery()
    check(q.exec, USERS_SQL)
    check(q.exec, TESTS_SQL)
    check(q.exec, REPORT_SQL)
    check(q.exec, SETTING_SQL)
    check(q.exec, REPORT_SQL)

