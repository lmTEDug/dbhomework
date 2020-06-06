# 登录数据库
# 开启死循环
# 不断接收查询条件
# 返回查询结果
import mysql.connector as sqlcnt

try:
    mydb = sqlcnt.connect(
        host='localhost',
        user='root',
        passwd='123456',
        database='test2'
    )
except sqlcnt.ProgrammingError as e:
    print(e.errno)
    raise e

# mycursor = mydb.cursor(dictionary=True)

# mycursor.execute('SHOW TABLES;')

# print(mycursor.description)
