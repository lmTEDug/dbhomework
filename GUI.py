import time
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from config import DATABASE

from query import JWXTStudent


class JWXT:
    def __init__(self):
        self.user_cnt = JWXTStudent(db_name=DATABASE)
        self.root = tk.Tk()
        self.root.title('教务系统(学生端)')
        self.root.geometry('960x440')
        self.root.iconbitmap('./img/jwxt.ico')
        self.root.resizable(False, False)
        self.mainloop = self.root.mainloop

        # login ui and main ui
        self._init_login_ui(self.root)
        self.login_ui.place(x=360, y=100)

        self._init_main_ui(self.root)

        self._init_course_grade(self.course_grade_ui)
        self._init_course_table(self.course_table_ui)
        self._init_course_available(self.course_available_ui)
        self._init_student_info(self.student_info_ui)

    def _init_login_ui(self, master):
        """初始化登录界面"""

        self.login_ui = tk.Frame(master)  # , bg='lightgreen')
        # login button
        self.login_btn = tk.Button(self.login_ui)
        self.login_btn['text'] = '登录'
        self.login_btn['command'] = self.login_btn_cmd

        # username label
        self.login_usrn_label = tk.Label(self.login_ui)
        self.login_usrn_label['text'] = '学号'

        # username entry
        self.login_usrn_entry = tk.Entry(self.login_ui)

        # password label
        self.login_pwd_label = tk.Label(self.login_ui)
        self.login_pwd_label['text'] = '密码'

        # password entry
        self.login_pwd_entry = tk.Entry(self.login_ui, show='*')

        # login widgets pack
        self.login_usrn_label.grid(row=0, column=0, padx=10, pady=10)
        self.login_usrn_entry.grid(row=0, column=1, padx=10, pady=10)
        self.login_pwd_label.grid(row=1, column=0, padx=10, pady=10)
        self.login_pwd_entry.grid(row=1, column=1, padx=10, pady=10)
        self.login_btn.grid(row=2, column=1, padx=10, pady=10)

    def _init_main_ui(self, master):
        """初始化主界面"""

        # notebook frame for main ui
        self.main_ui = tk.Frame(master)

        self.main_ui_notebook = ttk.Notebook(self.main_ui, height=385)
        self.course_table_ui = tk.Frame(self.main_ui_notebook)  # , bg='lightyellow')
        self.main_ui_notebook.add(self.course_table_ui, text='课程表')
        self.course_available_ui = tk.Frame(self.main_ui_notebook)  # , bg='lightblue')
        self.main_ui_notebook.add(self.course_available_ui, text='选课')
        self.course_grade_ui = tk.Frame(self.main_ui_notebook)  # , bg='lightgreen')
        self.main_ui_notebook.add(self.course_grade_ui, text='成绩')
        self.student_info_ui = tk.Frame(self.main_ui_notebook)  # , bg='lightblue')
        self.main_ui_notebook.add(self.student_info_ui, text='个人信息')
        self.main_ui_notebook.bind('<<NotebookTabChanged>>', self.main_ui_tab_change_cmd)
        self.main_ui_notebook.pack(side='top', fill='x')

        # logout btn
        self.logout_btn = tk.Button(self.main_ui, text='退出登录', bd=0)
        self.logout_btn['command'] = self.logout_btn_cmd
        self.logout_btn.pack(anchor='se')

    def _init_course_grade(self, master):
        """初始化成绩界面"""

        # course grade
        self.course_grade_frame1 = tk.Frame(master)
        self.course_grade_tab = ttk.Treeview(self.course_grade_frame1, show='headings', height=10)
        self.columns_course_grade = ['cno', 'cname', 'ctype', 'credit', 'dept', 'tname', 'cgrade']
        self.columns_course_grade_cn = ['课程号', '课程名', '课程类型', '学分', '院系', '授课老师', '成绩']
        self.course_grade_tab['columns'] = self.columns_course_grade
        for i, j in zip(self.columns_course_grade, self.columns_course_grade_cn):
            self.course_grade_tab.column(i, width='50')
            self.course_grade_tab.heading(i, text=j)

        self.course_grade_scroll = tk.Scrollbar(self.course_grade_frame1, orient='vertical', command=self.course_grade_tab.yview)
        self.course_grade_tab['yscrollcommand'] = self.course_grade_scroll.set

        # course grade pack
        self.course_grade_scroll.pack(side='right', fill='y')
        self.course_grade_tab.pack(side='top', fill='x')
        self.course_grade_frame1.pack(side='top', fill='x')

        # query frame
        self.course_grade_frame2 = tk.Frame(master, bd=2, relief='groove')
        self.course_grade_frame20 = tk.Frame(self.course_grade_frame2)
        self.course_grade_frame21 = tk.Frame(self.course_grade_frame2)
        self.course_grade_label = tk.Label(self.course_grade_frame20, text='筛 选 条 件')
        self.course_grade_labels = []
        self.course_grade_entrys = []
        for i in self.columns_course_grade_cn:
            self.course_grade_labels.append(tk.Label(self.course_grade_frame21, text='*'))
            self.course_grade_entrys.append(tk.Entry(self.course_grade_frame21, width=15))

        tmp = 0
        for i, j in zip(self.course_grade_labels, self.course_grade_entrys):
            # i.grid(row=0, column=tmp, padx=15, pady=15)
            # tmp += 1
            j.grid(row=0, column=tmp, padx=10, pady=15)
            tmp += 1

        self.course_grade_btn = tk.Button(self.course_grade_frame20, text='查 询')
        self.course_grade_btn['command'] = self.course_grade_btn_cmd
        self.course_grade_btn_cl = tk.Button(self.course_grade_frame20, text='清 除')
        self.course_grade_btn_cl['command'] = self.course_grade_btn_cl_cmd

        self.course_grade_label.grid(row=0, column=0, padx=10)
        self.course_grade_btn.grid(row=0, column=1, padx=10)
        self.course_grade_btn_cl.grid(row=0, column=2, padx=10)

        self.course_grade_frame20.grid(row=0)
        self.course_grade_frame21.grid(row=1, pady=5)
        self.course_grade_frame2.pack(side='top', fill='x')

    def _init_course_table(self, master):
        """初始化课表界面"""

        # course table
        self.course_table_frame1 = tk.Frame(master)
        self.course_table_tab = ttk.Treeview(self.course_table_frame1, show='headings', height=10)
        self.columns_course_table = ['cno', 'cname', 'ctype', 'dept', 'tname', 'credit', 'chour', 'ctime', 'cplace']
        self.columns_course_table_cn = ['课程号', '课程名', '课程类型', '院系', '授课老师', '学分', '学时', '上课时间', '上课地点']
        self.course_table_tab['columns'] = self.columns_course_table
        for i, j in zip(self.columns_course_table, self.columns_course_table_cn):
            self.course_table_tab.column(i, width='50')
            self.course_table_tab.heading(i, text=j)

        self.course_table_scroll = tk.Scrollbar(self.course_table_frame1, orient='vertical', command=self.course_table_tab.yview)
        self.course_table_tab['yscrollcommand'] = self.course_table_scroll.set

        # course table pack
        self.course_table_scroll.pack(side='right', fill='y')
        self.course_table_tab.pack(side='top', fill='x')
        self.course_table_frame1.pack(side='top', fill='x')

        # query frame
        self.course_table_frame2 = tk.Frame(master, bd=2, relief='groove')
        self.course_table_frame20 = tk.Frame(self.course_table_frame2)
        self.course_table_frame21 = tk.Frame(self.course_table_frame2)
        self.course_table_label = tk.Label(self.course_table_frame20, text='筛 选 条 件')
        self.course_table_labels = []
        self.course_table_entrys = []
        for i in self.columns_course_table_cn:
            self.course_table_labels.append(tk.Label(self.course_table_frame21, text='*'))
            self.course_table_entrys.append(tk.Entry(self.course_table_frame21, width=10))

        tmp = 0
        for i, j in zip(self.course_table_labels, self.course_table_entrys):
            # i.grid(row=0, column=tmp, padx=5, pady=15)
            # tmp += 1
            j.grid(row=0, column=tmp, padx=15, pady=15)
            tmp += 1

        self.course_table_btn = tk.Button(self.course_table_frame20, text='查 询')
        self.course_table_btn['command'] = self.course_table_btn_cmd
        self.course_table_btn_cl = tk.Button(self.course_table_frame20, text='清 除')
        self.course_table_btn_cl['command'] = self.course_table_btn_cl_cmd

        self.course_table_label.grid(row=0, column=0, padx=10)
        self.course_table_btn.grid(row=0, column=1, padx=10)
        self.course_table_btn_cl.grid(row=0, column=2, padx=10)
        self.course_table_frame20.grid(row=0)
        self.course_table_frame21.grid(row=1, pady=5)
        self.course_table_frame2.pack(side='top', fill='x')

        # withdraw course
        self.course_table_frame3 = tk.Frame(self.course_table_ui, bd=2, relief='groove')
        self.course_table_label2 = tk.Label(self.course_table_frame3, text='撤课(输入需撤课程号):')
        self.course_table_entry2 = tk.Entry(self.course_table_frame3, width=20)
        self.course_table_btn2 = tk.Button(self.course_table_frame3, text='提交')
        self.course_table_btn2['command'] = self.course_table_btn2_cmd

        self.course_table_label2.grid(row=0, column=0, padx=5, pady=20)
        self.course_table_entry2.grid(row=0, column=1, padx=5, pady=20)
        self.course_table_btn2.grid(row=0, column=2, padx=5, pady=20)
        self.course_table_frame3.pack(side='top', fill='x')

    def _init_course_available(self, master):
        """初始化选课界面"""

        # course available
        self.course_available_frame1 = tk.Frame(master)
        self.course_available_tab = ttk.Treeview(self.course_available_frame1, show='headings', height=10)
        self.columns_course_available = ['cno', 'cname', 'ctype', 'dept', 'tname', 'title', 'credit', 'chour', 'ctime', 'cplace', ' restno']
        self.columns_course_available_cn = ['课程号', '课程名', '课程类型', '院系', '授课老师', '职称', '学分', '学时', '上课时间', '上课地点', '剩余人数']
        self.course_available_tab['columns'] = self.columns_course_available
        for i, j in zip(self.columns_course_available, self.columns_course_available_cn):
            self.course_available_tab.column(i, width='50')
            self.course_available_tab.heading(i, text=j)

        self.course_available_scroll = tk.Scrollbar(self.course_available_frame1, orient='vertical', command=self.course_available_tab.yview)
        self.course_available_tab['yscrollcommand'] = self.course_available_scroll.set

        # course available pack
        self.course_available_scroll.pack(side='right', fill='y')
        self.course_available_tab.pack(side='top', fill='x')
        self.course_available_frame1.pack(side='top', fill='x')

        # query frame
        self.course_available_frame2 = tk.Frame(master, bd=2, relief='groove')
        self.course_available_frame20 = tk.Frame(self.course_available_frame2)
        self.course_available_frame21 = tk.Frame(self.course_available_frame2)
        self.course_available_label = tk.Label(self.course_available_frame20, text='筛 选 条 件')
        self.course_available_labels = []
        self.course_available_entrys = []
        for i in self.columns_course_available_cn:
            self.course_available_labels.append(tk.Label(self.course_available_frame21, text='*'))
            self.course_available_entrys.append(tk.Entry(self.course_available_frame21, width=10))

        tmp = 0
        for i, j in zip(self.course_available_labels, self.course_available_entrys):
            # i.grid(row=0, column=tmp, padx=0, pady=15)
            # tmp += 1
            j.grid(row=0, column=tmp, padx=5, pady=15)
            tmp += 1

        self.course_available_btn = tk.Button(self.course_available_frame20, text='查 询')
        self.course_available_btn['command'] = self.course_available_btn_cmd
        self.course_available_btn_cl = tk.Button(self.course_available_frame20, text='清 除')
        self.course_available_btn_cl['command'] = self.course_available_btn_cl_cmd

        self.course_available_label.grid(row=0, column=0, padx=10)
        self.course_available_btn.grid(row=0, column=1, padx=10)
        self.course_available_btn_cl.grid(row=0, column=2, padx=10)
        self.course_available_frame20.grid(row=0)
        self.course_available_frame21.grid(row=1, pady=5)
        self.course_available_frame2.pack(side='top', fill='x')

        self.course_available_frame3 = tk.Frame(self.course_available_ui, bd=2, relief='groove')

        # select course
        self.course_available_frame3 = tk.Frame(self.course_available_ui, bd=2, relief='groove')
        self.course_available_label2 = tk.Label(self.course_available_frame3, text='选课(输入需选课程号):')
        self.course_available_entry2 = tk.Entry(self.course_available_frame3, width=20)
        self.course_available_btn2 = tk.Button(self.course_available_frame3, text='提交')
        self.course_available_btn2['command'] = self.course_available_btn2_cmd

        self.course_available_label2.grid(row=0, column=0, padx=5, pady=20)
        self.course_available_entry2.grid(row=0, column=1, padx=5, pady=20)
        self.course_available_btn2.grid(row=0, column=2, padx=5, pady=20)
        self.course_available_frame3.pack(side='top', fill='x')

    def _init_student_info(self, master):
        """初始化学生信息界面"""

        self.student_info_frame1 = tk.Frame(master, bd=2, relief='groove')
        self.student_info_frame2 = tk.Frame(master)
        self.student_info_frame3 = tk.Frame(master)

        # info
        self.student_info_columns = ['sno', 'sname', 'sex', 'birthday', 'place', 'dept', 'major', 'sgrade']
        self.student_info_columns_cn = ['学号:', '姓名:', '性别:', '出生日期:', '籍贯:', '院系:', '专业:', '年级:']

        self.student_info_labels = []
        self.student_info_entrys = []

        for i in self.student_info_columns_cn:
            self.student_info_labels.append(tk.Label(self.student_info_frame1, text=i))
            self.student_info_entrys.append(tk.Entry(self.student_info_frame1, state='readonly', width=15))

        tmp1 = 0
        for i in range(0, 8, 2):
            tmp2 = 1
            self.student_info_labels[i].grid(row=tmp1, column=tmp2, padx=15, pady=10)
            tmp2 += 1
            self.student_info_entrys[i].grid(row=tmp1, column=tmp2, padx=15, pady=10)
            tmp2 += 1
            self.student_info_labels[i+1].grid(row=tmp1, column=tmp2, padx=15, pady=10)
            tmp2 += 1
            self.student_info_entrys[i+1].grid(row=tmp1, column=tmp2, padx=15, pady=10)
            tmp2 += 1
            tmp1 += 1

        # refresh and change btn
        self.student_info_btn1 = tk.Button(self.student_info_frame2, text='刷新')
        self.student_info_btn1['command'] = self.student_info_btn1_cmd
        self.student_info_btn2 = tk.Button(self.student_info_frame2, text='修改信息')
        self.student_info_btn2['command'] = self.student_info_btn2_cmd

        self.student_info_btn1.grid(row=0, column=0, padx=15, pady=15)
        self.student_info_btn2.grid(row=0, column=1, padx=15, pady=15)

        # ok and cancel btn
        self.student_info_btn3 = tk.Button(self.student_info_frame3, text='确认')
        self.student_info_btn3['command'] = self.student_info_btn3_cmd
        self.student_info_btn4 = tk.Button(self.student_info_frame3, text='取消')
        self.student_info_btn4['command'] = self.student_info_btn4_cmd

        self.student_info_btn3.grid(row=0, column=0, padx=15, pady=15)
        self.student_info_btn4.grid(row=0, column=1, padx=15, pady=15)

        self.student_info_frame1.pack(side='top')
        self.student_info_frame2.pack(side='top')

    def login_btn_cmd(self):
        """登录按钮"""

        username = self.login_usrn_entry.get()
        password = self.login_pwd_entry.get()

        if not username.isnumeric():
            showinfo('提示信息', '请输入正确的学号')
            return
        if not self.user_cnt.login(username, password):
            showinfo('登陆失败', '用户名或密码错误')
        else:
            self.login_pwd_entry.delete(0, 'end')
            self.login_ui.forget()
            self.main_ui.pack(fill='both')
            self.main_ui_tab_change_cmd()

    def logout_btn_cmd(self):
        """退出登录按钮"""

        self.user_cnt.logout()
        self.main_ui.forget()
        self.login_ui.pack()

    def course_table_btn_cmd(self):
        """课表查询按钮"""

        # query
        params = {}
        for i, j in zip(self.columns_course_table, self.course_table_entrys):
            if j.get():
                params[i] = j.get()
        if params:
            result = self.user_cnt.queryCourseTable(params=params)
        else:
            result = self.user_cnt.queryCourseTable()

        # render
        tmp = self.course_table_tab.get_children()
        self.course_table_tab.delete(*tmp)
        for index, row_data in enumerate(result):
            self.course_table_tab.insert('', index, values=row_data[1:])

    def course_available_btn_cmd(self):
        """选课查询按钮"""

        # query
        params = {}
        for i, j in zip(self.columns_course_available, self.course_available_entrys):
            if j.get():
                params[i] = j.get()
        if params:
            result = self.user_cnt.queryCourseAvailable(params=params)
        else:
            result = self.user_cnt.queryCourseAvailable()

        # render
        tmp = self.course_available_tab.get_children()
        self.course_available_tab.delete(*tmp)
        for index, row_data in enumerate(result):
            self.course_available_tab.insert('', index, values=row_data)

    def course_grade_btn_cmd(self):
        """成绩查询按钮"""

        # query
        params = {}
        for i, j in zip(self.columns_course_grade, self.course_grade_entrys):
            if j.get():
                params[i] = j.get()
        if params:
            result = self.user_cnt.queryCourseGrade(params=params)
        else:
            result = self.user_cnt.queryCourseGrade()

        # render
        tmp = self.course_grade_tab.get_children()
        self.course_grade_tab.delete(*tmp)
        for index, row_data in enumerate(result):
            self.course_grade_tab.insert('', index, values=row_data[1:])

    def course_table_btn2_cmd(self):
        """撤课按钮"""

        course_id = self.course_table_entry2.get()  # type: str
        if course_id:
            if not course_id.isnumeric():
                showinfo('输入错误', '请输入合法的课程号')
            else:
                result = self.user_cnt.withdrawCourse(course_id)
                if result:
                    self.course_table_btn_cmd()
                    showinfo('提示信息', '提交成功, 课表已更新')
                else:
                    showinfo('提示信息', '撤课失败')
        else:
            showinfo('提示信息', '请输入需撤课课程号')

    def course_available_btn2_cmd(self):
        """选课按钮"""

        course_id = self.course_available_entry2.get()  # type: str
        if course_id:
            if not course_id.isnumeric():
                showinfo('输入错误', '请输入合法的课程号')
            else:
                result = self.user_cnt.selectCourse(course_id)
                if result:
                    self.course_table_btn_cmd()
                    showinfo('提示信息', '提交成功, 课表已更新')
                else:
                    showinfo('提示信息', '选课失败')
        else:
            showinfo('提示信息', '请输入需选课课程号')

    def course_grade_btn_cl_cmd(self):
        for i in self.course_grade_entrys:
            i.delete(0, 'end')

    def course_available_btn_cl_cmd(self):
        for i in self.course_available_entrys:
            i.delete(0, 'end')

    def course_table_btn_cl_cmd(self):
        for i in self.course_table_entrys:
            i.delete(0, 'end')

    def student_info_btn1_cmd(self):
        """个人信息刷新按钮"""

        result = self.user_cnt.queryStudentInfo()
        # print(result)
        # result = {1: 2}
        if not result:
            showinfo('提示信息', '数据刷新失败')
        else:
            for i, j in zip(self.student_info_columns, self.student_info_entrys):
                j['state'] = 'normal'
                j.delete(0, 'end')
                j.insert(0, result[i])
                j['state'] = 'readonly'

    def student_info_btn2_cmd(self):
        """修改信息"""

        for i in self.student_info_entrys[2:5]:
            i['state'] = 'normal'

        self.student_info_btn1['state'] = 'disabled'
        self.student_info_btn2['state'] = 'disabled'
        self.student_info_frame3.pack(side='top')

    def student_info_btn3_cmd(self):
        """个人信息修改确认按钮"""

        new_info = {}
        for i in range(2, 5):
            new_info[self.student_info_columns[i]] = self.student_info_entrys[i].get()

        # check valid
        # print(new_info)
        if new_info['sex'] not in {'男', '女'}:
            showinfo('提示信息', '请输入合法的性别')
            return
        try:
            time.strptime(new_info['birthday'], '%Y-%m-%d')
        except ValueError:
            showinfo('提示信息', '请输入合法的日期\n格式: YYYY-MM-DD')
            return

        result = self.user_cnt.updateStudentInfo(new_info)

        if result:
            for i in self.student_info_entrys[2:5]:
                i['state'] = 'readonly'
            self.student_info_btn1['state'] = 'active'
            self.student_info_btn2['state'] = 'active'
            self.student_info_frame3.pack_forget()
            showinfo('提示信息', '提交成功, 个人信息已更新')
        else:
            showinfo('提示信息', '提交失败, 未知错误')

    def student_info_btn4_cmd(self):
        """个人信息修改取消按钮"""

        for i in self.student_info_entrys[2:5]:
            i['state'] = 'readonly'
        self.student_info_btn1['state'] = 'active'
        self.student_info_btn2['state'] = 'active'
        self.student_info_frame3.pack_forget()

        self.student_info_btn1_cmd()

    def main_ui_tab_change_cmd(self, *args):
        """切换标签事件"""

        events = [
            self.course_table_btn_cmd,
            self.course_available_btn_cmd,
            self.course_grade_btn_cmd,
            self.student_info_btn1_cmd
        ]
        if self.user_cnt.islogin:
            index = self.main_ui_notebook.index(self.main_ui_notebook.select())
            events[index]()
