#!/usr/bin/env python
#coding=utf-8

from os.path import expanduser
import sqlite3

DB = expanduser('~/.billdb')

def get_db(db_path = DB):
    db = sqlite3.connect(db_path, detect_types = sqlite3.PARSE_DECLTYPES)
    db.row_factory = sqlite3.Row
    db.text_factory = str
    if _is_new_db(db):
        _creat_new_db(db)
    return db

def _creat_new_db(db):
    db.execute("""
    create table billdb(
        id integer primary key not null,
        time timestamp not null,
        cost double not null,
        comment varchar(255)
    );
    """)

def _is_new_db(db):
    return db.execute(
            "select count(*) from sqlite_master where type = 'table';"
            ).fetchone()[0] == 0
