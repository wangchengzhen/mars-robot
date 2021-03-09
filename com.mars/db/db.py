#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import pymysql


def conn():
    return pymysql.connect(
        "localhost",
        "root",
        "pa$$w0rd",
        "mars-robot",
        charset='utf8'
    )


def query(sql):
    db = conn()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except ValueError:
        print("Error: unable to query data")

    db.commit()
    db.close


def insert(sql):
    db = conn()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
    except ValueError:
        print("Error: unable to insert data")
    db.commit()
    db.close


if __name__ == "__main__":
    insert(f"insert into t_article (id,reader,title,content,`like`) values (1601255821,15992,'中国哪个大学的伙食/食堂质量最好','中国哪个大学的伙食/食堂质量最好',888)")

