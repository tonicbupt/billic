#!/usr/bin/env python
#-*- coding:utf-8 -*-

from datastore import get_db
from datetime import datetime

class Bill(object):
    
    def __init__(self, id, time, cost, comment):
        self.id = id
        self.time = time
        self.cost = cost
        self.comment = comment

    def __repr__(self):
        return 'Bill <%s, %s, %s, %s>' % (self.id, self.time, self.cost, self.comment)

    @classmethod
    def get(cls, id):
        db = get_db()
        with db:
            rs = db.execute("select `id`, `time`, `cost`, `comment` from billdb where `id`= ?", (id,)).fetchone()
            return Bill(rs[0], rs[1], rs[2], rs[3]) if rs else None

    @classmethod
    def add(cls, cost, comment):
        db = get_db()
        with db:
            rs = db.execute("insert into billdb (time, cost, comment) values (?, ?, ?);", (datetime.now(), cost, comment))
            return rs.lastrowid if rs else None

    @classmethod
    def find(cls, beg, end):
        db = get_db()
        with db:
            rs = db.execute("select * from billdb where datetime(time) > ? and datetime(time) <= ?;", 
                    (datetime.strptime(beg, '%Y-%m-%d'), datetime.strptime(end, '%Y-%m-%d'))).fetchall()
            return [Bill(r[0], r[1], r[2], r[3]) for r in rs] if rs else []

def get(id):
    return Bill.get(id)

def add(cost, comment):
    return Bill.add(cost, comment)

def find(beg, end):
    return Bill.find(beg, end)


