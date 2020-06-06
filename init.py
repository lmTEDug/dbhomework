import mysql.connector
import os
import csv


def readSqlFile(filepath):
    with open(filepath, encoding='utf8') as f:
        tmp_commands = f.read().replace('\n', '').split(';')

    sql_commands = [i+';' for i in tmp_commands]
    print(sql_commands)
    return sql_commands


if __name__ == "__main__":
    # 连接数据库并且得到游标
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='123456',
        database='test'
    )
    db_cursor = mydb.cursor()
    db_cursor.execute('select sname from student;')
    # db_cursor.
    db_cursor.execute('select * from student;')
    # 建立表和建立视图直接用命令行跑算了

    # TODO: 导入csv数据
    # 这里就是用INSERT语句把数据批量导入, 当然也可以手动敲几条数据算了

    # 关闭连接
    db_cursor.close()
    mydb.close()