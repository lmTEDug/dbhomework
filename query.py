import mysql.connector as sqlcnt


class JWXTStudent:
    def __init__(self, db_name, port=3306, host='localhost'):
        self.db_name = db_name
        self.port = port
        self.host = host
        self.__islogin = False
        self.username = None
        self.db_cnt = None
        self.db_cursor = None

    def __del__(self):
        if self.__islogin:
            self.db_cursor.close()
            self.db_cnt.close()

    def login(self, username, password):
        """登录数据库"""

        try:
            self.db_cnt = sqlcnt.connect(
                host=self.host,
                database=self.db_name,
                port=self.port,
                user=username,
                passwd=password,
            )
        except sqlcnt.Error as e:
            if e.errno == 1045:
                print("用户名或密码错误")
            else:
                raise
        else:
            self.db_cursor = self.db_cnt.cursor()
            self.username = username
            self.__islogin = True

    def selectCourse(self, course_ids):
        """
        学生选课

        参数:
            course_data: 要选的课的课程号, 用列表存储
        """

        if self.__islogin is False:
            print("请登录!")
            return
        else:
            sql = "INSERT INTO SC (sno, cno) VALUES (%s, %s)"
            val=[]
            for course_id in course_ids:
                val.append((self.username,course_id))
            self.db_cursor.executemany(sql, val)
            self.db_cursor.commit()   
            print("选课成功。")
            return True

    def withdrawCourse(self, course_ids):
        """
        学生撤课, 参数同选课参数
        """
        if self.__islogin is False:
            print("请登录!")
            return
        else:
            sql = "DELETE FROM SC WHERE sno = %s AND cno = %s"
            val=[]
            for course_id in course_ids:
                val.append((self.username,course_id))
            self.db_cursor.executemany(sql, val)
            self.db_cursor.commit()   
            print("撤课成功。")
            return True

    def queryCourseAvailable(self, params=None):
        """
        查询当前所有可选的课, 就是查询有哪些课
        """

        if self.__islogin is False:
            print("请登录!")
            return
        else:
            if params==None:
                sql="select * from TC"
                self.db_cursor.execute(sql)
                fet=self.db_cursor.fetchall()
                return fet
            else:
                sql="select * from TC WHERE"
                for param in params:
                    sql+=" AND "+str(param)+" = "+ str(params[param])
                self.db_cursor.executemany(sql)
                fet=self.db_cursor.fetchall()
                return fet

    def queryCourseTable(self, params=None):
        """
        查询学生课程表
        """

        if self.__islogin is False:
            print("请登录!")
            return
        else:
            if params==None:
                sql="select * from course_table WHERE sno = %s"
                val=(self.username,)
                self.db_cursor.execute(sql,val)
                fet=self.db_cursor.fetchall()
                return fet
            else:
                sql="select * from course_table WHERE sno = %s"
                for param in params:
                    sql+=" AND "+str(param)+" = "+ str(params[param])
                self.db_cursor.execute(sql)
                fet=self.db_cursor.fetchall()
                return fet

    def queryCourseGrade(self, params=None):
        """
        查询课程成绩
        """

        if self.__islogin is False:
            print("请登录!")
            return
        else:
            if params==None:
                sql="select * from course_grade WHERE sno = %s"
                val=(self.username,)
                self.db_cursor.execute(sql,val)
                fet=self.db_cursor.fetchall()
                return fet
            else:
                sql="select * from course_grade WHERE sno = %s"
                for param in params:
                    sql+=" AND "+str(param)+" = "+ str(params[param])
                self.db_cursor.execute(sql)
                fet=self.db_cursor.fetchall()
                return fet


class JWXTTeahcer:
    pass


class JWXTAdmin:
    pass
