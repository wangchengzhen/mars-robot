#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql


def getDB():
    return pymysql.connect(host="localhost", user="root", password="pa$$w0rd", database="mars",charset="utf8mb4")


def queryAll(sql):
    db = getDB()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except:
        print("Error: unable to queryAll data: " + sql)
    db.close()


def queryById(sql):
    db = getDB()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        return cursor.fetchone()
    except:
        print("Error: unable to queryById data: " + sql)
    db.close()


# 新增
def insert(sql):
    db = getDB()
    cursor = db.cursor()
    result = 0
    try:
        cursor.execute(sql)
        db.commit()
        result = 1
    except:
        print("Error: unable to insert data: " + sql)
        db.rollback()
        result = 0
    finally:
        db.close
        return result


# 新增
def update(sql):
    db = getDB()
    cursor = db.cursor()
    result = 0
    try:
        cursor.execute(sql)
        db.commit()
        result = 1
    except:
        print("Error: unable to insert data: " + sql)
        db.rollback()
        result = 0
    finally:
        db.close
        return result