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
            # self.db_cursor.close()
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
                return False
            else:
                raise
        else:
            self.db_cursor = self.db_cnt.cursor()
            self.username = username
            self.__islogin = True
            return True

    def selectCourse(self, course_id):
        """
        学生选课

        参数:
            course_data: 要选的课的课程号, 用列表存储
        """

        if self.__islogin is False:
            print("请登录!")
            return False
        else:
            sql = f"select * from  course_available WHERE cno = {course_id}"
            self.db_cursor.execute(sql)
            fet = self.db_cursor.fetchall()
            if fet:
                sql = f"select restno from course_available WHERE cno = {course_id}"
                restno = (self.db_cursor.fetchall())[0]
                if restno > 0:
                    sql = f"update course_available set restno=restno-1 where cno = {course_id}"
                    self.db_cursor.execute(sql)
                    sql = f"INSERT INTO SC (sno, cno) VALUES ({self.username}, {course_id})"
                    self.db_cursor.execute(sql)
                    self.db_cnt.commit()
                    print("选课成功。")
                    return True
                else:
                    return False
            else:
                return False

    def withdrawCourse(self, course_id):
        """
        学生撤课, 参数同选课参数
        """
        if self.__islogin is False:
            print("请登录!")
            return False
        else:
            sql = f"select * from  SC WHERE sno = {self.username} and cno = {course_id}"
            self.db_cursor.execute(sql)
            fet = self.db_cursor.fetchall()
            if fet:
                sql = f"update course_available set restno=restno+1 where cno = {course_id}"
                self.db_cursor.execute(sql)
                sql = f"DELETE FROM SC WHERE sno = {self.username} AND cno = {course_id}"
                self.db_cursor.executemany(sql)
                self.db_cnt.commit()
                print("撤课成功。")
                return True
            else:
                return False

    def queryCourseAvailable(self, params=None):
        """
        查询当前所有可选的课, 就是查询有哪些课
        """

        if self.__islogin is False:
            print("请登录!")
            return False
        else:
            sql = "select * from course_available"
            if params:
                sql += " WHERE "
                index = 0
                for param in params:
                    if index:
                        sql += " AND "
                    else:
                        index = 1
                    sql += str(param)+" = '" + str(params[param])+"'"
            print("\n\n\n", sql, "\n\n\n")
            self.db_cursor.execute(sql)
            fet = self.db_cursor.fetchall()
            return fet

    def queryCourseTable(self, params=None):
        """
        查询学生课程表
        """

        if self.__islogin is False:
            print("请登录!")
            return False
        else:
            sql = f"select * from course_table WHERE sno = {self.username}"
            # val=(self.username,)
            if params:
                for param in params:
                    sql += " AND "+str(param)+" = '" + str(params[param])+"'"
            print("\n\n\n", sql, "\n\n\n")
            self.db_cursor.execute(sql)
            fet = self.db_cursor.fetchall()
            return fet

    def queryCourseGrade(self, params=None):
        """
        查询课程成绩
        """

        if self.__islogin is False:
            print("请登录!")
            return False
        else:
            sql = f"select * from course_grade WHERE sno = {self.username}"
            if params:
                for param in params:
                    sql += " AND "+str(param)+" = '" + str(params[param])+"'"
            print("\n\n\n", sql, "\n\n\n")
            self.db_cursor.execute(sql)
            fet = self.db_cursor.fetchall()
            return fet

    def queryStudentInfo(self):
        """
        查询当前登录学生信息

        返回:
            字典格式, 键对应列名, 值对应相应的值
        """
        dit = {}
        sql = f"select * from Student where sno = {self.username}"
        self.db_cursor.execute(sql)
        col_name = [tuple[0] for tuple in self.db_cursor.description]
        fet = self.db_cursor.fetchall()
        for i, j in zip(col_name, fet[0]):
            dit[i] = j
        return dit

    def updateStudentInfo(self, params):
        """
        更新当前登录学生信息

        参数: params字典格式, 更新后的值

        返回执行结果
        """
        if params:
            for param in params:
                sql = f"update Student set {param} = '{params[param]}' where sno = {self.username}"
                print(sql)
                self.db_cursor.execute(sql)
            self.db_cnt.commit()
        return True
