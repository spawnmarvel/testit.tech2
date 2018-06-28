import sqlite3
import datetime

conn = None
database = "app/web2.db"

sql_create_logger = "create table if not exists logger (id INTEGER PRIMARY KEY autoincrement, logger_msg char(60) NOT NULL, logger_data char(60) NOT NULL, logger_time NUMERIC)"
sql_insert_logger = "insert into logger (logger_msg, logger_data, logger_time) values (?, ?, ?)"
sql_select_all = "select * from logger order by id desc"


def init_logger():
    msg = None
    global conn
    try:
       
        conn = sqlite3.connect(database)
        with conn:
            cur = conn.cursor()
            global sql_create_logger
            cur.execute(sql_create_logger)
            conn.commit()
            row = cur.fetchone()
            if row == None:
                msg = " - - > Table exists logger"
            else:
                msg = " - - > Table created logger"
    except sqlite3.OperationalError as e:
        msg = str(e)
    return msg

def db_logger_all():
    """___"""
    msg = ""
    global CONN
    try:
        conn = sqlite3.connect(database)
        with conn:
            cur = conn.cursor()
            global sql_select_all
            cur.execute(sql_select_all)
            row = cur.fetchall()
            msg = row
    except sqlite3.OperationalError as e:
        msg = e
    return msg


def db_logit(logger_msg, logger_data):
    """ doc """
    msg = None
    global conn
    try:
        conn = sqlite3.connect(database)
        with conn:
            cur = conn.cursor()
            timeNow = datetime.datetime.now()
            global sql_insert_logger
            cur.execute(sql_insert_logger, (format(logger_msg),format(logger_data), timeNow))
            conn.commit()
            msg = "added row"
    except sqlite3.OperationalError as e:
        msg = e
    return msg

def db_insert_note():
    pass
def db_delete_note():
    pass
def db_all_note():
    pass
