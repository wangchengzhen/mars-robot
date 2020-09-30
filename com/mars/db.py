#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql


def getDB():
    return pymysql.connect(
        "localhost",
        "root",
        "pa$$w0rd",
        "mars-robot",
        charset='utf8'
    )


def queryAll(sql):
    db = getDB()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except:
        print("Error: unable to queryAll data")
    db.close()


def queryById(sql):
    db = getDB()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        return cursor.fetchone()
    except:
        print("Error: unable to queryById data")
    db.close()


def insert(sql):
    db = getDB()
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close
