import mysql.connector as sqlcnt
import os
import csv
import json
from config import *


def readSqlFile(filepath):
    with open(filepath, encoding='utf8') as f:
        tmp_commands = f.read().replace('\n', '').strip(';').split(';')
    sql_commands = [i+';' for i in tmp_commands]
    return sql_commands


if __name__ == "__main__":
    # connect db
    mydb = sqlcnt.connect(
        host=HOST,
        port=PORT,
        user=SUPERUSERNAME,
        passwd=SUPERPASSWROD
    )
    db_cursor = mydb.cursor()

    # create database
    db_cursor.execute('SHOW DATABASES;')
    exist_db = db_cursor.fetchall()
    if (DATABASE,) in exist_db:
        choose = input(f"数据库'{DATABASE}'已经存在, 是否选择覆盖数据库?(Y/N)[Default:N]")
        if choose.lower() in ('y', 'yes'):
            print(f"覆盖原数据库'{DATABASE}'...")
            db_cursor.execute(f'DROP DATABASE {DATABASE};')
            db_cursor.execute(f"CREATE DATABASE {DATABASE};")
        else:
            print(f"保留原数据库'{DATABASE}'...")
    else:
        db_cursor.execute(f"CREATE DATABASE {DATABASE};")
    mydb.commit()
    db_cursor.execute(f"USE {DATABASE};")

    # create users
    with open('./data/user.csv', encoding='utf8') as f:
        csv_reader = csv.reader(f)
        for i in csv_reader:
            if csv_reader.line_num == 1:
                continue
            sql = f"CREATE USER '{i[0]}'@'{HOST}' IDENTIFIED BY '{i[1]}';"
            print(sql)
            try:
                db_cursor.execute(sql)
            except sqlcnt.Error as e:
                if e.errno == sqlcnt.errorcode.ER_CANNOT_USER:
                    pass
                else:
                    raise
            sql = f"GRANT SELECT, INSERT, UPDATE, DELETE ON {DATABASE}.* TO '{i[0]}'@'{HOST}';"
            print(sql)
            db_cursor.execute(sql)
            mydb.commit()

    # create table
    sql = readSqlFile('./sql/sql_table.sql')
    for i in sql:
        print(i)
        try:
            db_cursor.execute(i)
        except sqlcnt.Error as e:
            if e.errno == sqlcnt.errorcode.ER_TABLE_EXISTS_ERROR:
                continue
            else:
                raise

    # create view
    sql = readSqlFile('./sql/sql_view.sql')
    for i in sql:
        print(i)
        try:
            db_cursor.execute(i)
        except sqlcnt.Error as e:
            if e.errno == sqlcnt.errorcode.ER_TABLE_EXISTS_ERROR:
                continue
            else:
                raise

    # insert course data
    with open('./data/course.csv', encoding='utf8') as f:
        csv_reader = csv.reader(f)
        for i in csv_reader:
            if csv_reader.line_num == 1:
                continue
            sql = f"INSERT INTO course VALUES ('{i[0]}', '{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}')"
            print(sql)
            try:
                db_cursor.execute(sql)
            except sqlcnt.Error as e:
                if e.errno == sqlcnt.errorcode.ER_DUP_ENTRY:
                    continue
                else:
                    raise
            mydb.commit()

    # insert student data
    with open('./data/student.csv', encoding='utf8') as f:
        csv_reader = csv.reader(f)
        for i in csv_reader:
            if csv_reader.line_num == 1:
                continue
            sql = f"INSERT INTO student VALUES ('{i[0]}', '{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}')"
            print(sql)
            try:
                db_cursor.execute(sql)
            except sqlcnt.Error as e:
                if e.errno == sqlcnt.errorcode.ER_DUP_ENTRY:
                    continue
                else:
                    raise
            mydb.commit()

    # insert teacher data
    with open('./data/teacher.csv', encoding='utf8') as f:
        csv_reader = csv.reader(f)
        for i in csv_reader:
            if csv_reader.line_num == 1:
                continue
            sql = f"INSERT INTO teacher VALUES ('{i[0]}', '{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}')"
            print(sql)
            try:
                db_cursor.execute(sql)
            except sqlcnt.Error as e:
                if e.errno == sqlcnt.errorcode.ER_DUP_ENTRY:
                    continue
                else:
                    raise
            mydb.commit()

    # insert TC data
    with open('./data/TC.csv', encoding='utf8') as f1:
        csv_reader = csv.reader(f1)
        for i in csv_reader:
            if csv_reader.line_num == 1:
                continue
            sql = f"INSERT INTO TC VALUES ('{i[0]}', '{i[1]}')"
            print(sql)
            try:
                db_cursor.execute(sql)
            except sqlcnt.Error as e:
                if e.errno == sqlcnt.errorcode.ER_DUP_ENTRY:
                    continue
                else:
                    raise
            mydb.commit()

    # insert SC data
    with open('./data/SC.csv', encoding='utf8') as f1:
        csv_reader = csv.reader(f1)
        for i in csv_reader:
            if csv_reader.line_num == 1:
                continue
            sql = f"INSERT INTO SC VALUES ('{i[0]}', '{i[1]}', {i[2]})"
            print(sql)
            try:
                db_cursor.execute(sql)
            except sqlcnt.Error as e:
                if e.errno == sqlcnt.errorcode.ER_DUP_ENTRY:
                    continue
                else:
                    raise
            mydb.commit()
            sql = f"update course set restno=restno-1 where cno = {i[1]}"
            db_cursor.execute(sql)
            mydb.commit()

    # 关闭连接
    db_cursor.close()
    mydb.close()
