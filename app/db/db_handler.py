import sqlite3
import datetime

conn = None
database = "app/web2.db"

sql_create_holder = "create table if not exists holder(id INTEGER PRIMARY KEY autoincrement, note TEXT, topic TEXT, url TEXT, published NUMERIC)"
sql_insert_holder = "insert into holder (note, topic, url, published) values (?, ?, ?, ?)"
sql_get_all = "select * from holder order by id desc"
sql_delete_id = "delete from holder where id = ?"


def init_holder():
    msg = None
    global conn
    try:
       
        conn = sqlite3.connect(database)
        with conn:
            cur = conn.cursor()
            global sql_create_logger
            cur.execute(sql_create_holder)
            conn.commit()
            row = cur.fetchone()
            if row == None:
                msg = " - - > Table exists holder"
            else:
                msg = " - - > Table created holder"
    except sqlite3.OperationalError as e:
        msg = str(e)
    return msg

def db_insert_note(note, topic, url):
    msg = None
    global conn
    try:
        conn = sqlite3.connect(database)
        with conn:
            cur = conn.cursor()
            t = datetime.datetime.now()
            global sql_insert_holder
            cur.execute(sql_insert_holder, (note, topic, url, t))
            conn.commit()
            msg = "added row"
    except Exception as e:
        msg = e
    return msg


def db_delete_note(note_id):
    msg = None
    global conn
    try:
        conn = sqlite3.connect(database)
        with conn:
            cur = conn.cursor()
            global sql_delete_id
            cur.execute(sql_delete_id, (note_id,))
            conn.commit()
            msg = "deleted " + format(note_id)
    except Exception as e:
        msg = e
    return msg

def db_all_note():
    msg = None
    global conn
    try:
        conn = sqlite3.connect(database)
        with conn:
            cur = conn.cursor()
            global sql_get_all
            cur.execute(sql_get_all)
            row = cur.fetchall()
            msg = row
    except Exception as e:
        msg = e
    return msg


