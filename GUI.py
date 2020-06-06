import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from query import JWXTStudent


class JWXT:
    def __init__(self):
        self.user_cnt = JWXTStudent('test')
        self.root = tk.Tk()
        self.root.title('教务系统')
        self.root.geometry('960x420')
        self.root.resizable(False, False)
        self.mainloop = self.root.mainloop

        # widgets for login ui
        self.login_ui = tk.Frame(self.root)  # , bg='lightgreen')
        self._init_login_ui(self.login_ui)
        self.login_ui.pack()

        self._init_main_ui()

        self._init_course_table()
        self._init_course_available()
        self._init_course_grade()

    def _init_login_ui(self, master):
        # login button
        self.login_btn = tk.Button(master)
        self.login_btn['text'] = '登录'
        self.login_btn['command'] = self.login_btn_cmd

        # username label
        self.login_usrn_label = tk.Label(master)
        self.login_usrn_label['text'] = '用户名'

        # username entry
        self.login_usrn_entry = tk.Entry(master)

        # password label
        self.login_pwd_label = tk.Label(master)
        self.login_pwd_label['text'] = '密码'

        # password entry
        self.login_pwd_entry = tk.Entry(master, show='*')

        # login widgets pack
        self.login_usrn_label.grid(row=0, column=0, padx=10, pady=10)
        self.login_usrn_entry.grid(row=0, column=1, padx=10, pady=10)
        self.login_pwd_label.grid(row=1, column=0, padx=10, pady=10)
        self.login_pwd_entry.grid(row=1, column=1, padx=10, pady=10)
        self.login_btn.grid(row=2, column=1, padx=10, pady=10)

    def _init_main_ui(self):
        # notebook frame for main ui
        self.main_ui = ttk.Notebook(self.root, height=540, width=960)
        self.course_table_ui = tk.Frame(self.main_ui)  # , bg='lightyellow')
        self.main_ui.add(self.course_table_ui, text='课程表')
        self.course_available_ui = tk.Frame(self.main_ui)  # , bg='lightblue')
        self.main_ui.add(self.course_available_ui, text='选课')
        self.course_grade_ui = tk.Frame(self.main_ui)  # , bg='lightgreen')
        self.main_ui.add(self.course_grade_ui, text='成绩')

    def _init_course_grade(self):
        # course grade
        self.course_grade_frame1 = tk.Frame(self.course_grade_ui)
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
        self.course_grade_frame2 = tk.Frame(self.course_grade_ui, bd=2, relief='groove')
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

    def _init_course_table(self):
        # course table
        self.course_table_frame1 = tk.Frame(self.course_table_ui)
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
        self.course_table_frame2 = tk.Frame(self.course_table_ui, bd=2, relief='groove')
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

    def _init_course_available(self):
        # course available
        self.course_available_frame1 = tk.Frame(self.course_available_ui)
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
        self.course_available_frame2 = tk.Frame(self.course_available_ui, bd=2, relief='groove')
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

    def login_btn_cmd(self):
        username = 'root'  # self.login_usrn_entry.get()
        password = '123456'  # self.login_pwd_entry.get()
        if not self.user_cnt.login(username, password):
            showinfo('登陆失败', '用户名或密码错误')
        else:
            self.login_ui.destroy()
            self.main_ui.pack(fill='both')

    def course_table_btn_cmd(self):
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
        course_id = self.course_table_entry2.get()  # type: str
        if course_id:
            if not course_id.isnumeric():
                showinfo('输入错误', '请输入合法的课程号')
            else:
                result = self.user_cnt.withdrawCourse(course_id)
                if result:
                    showinfo('提示信息', '提交成功, 请刷新课程表查看是否成功撤课')
                else:
                    showinfo('提示信息', '撤课失败')
        else:
            showinfo('提示信息', '请输入需撤课课程号')

    def course_available_btn2_cmd(self):
        course_id = self.course_table_entry2.get()  # type: str
        if course_id:
            if not course_id.isnumeric():
                showinfo('输入错误', '请输入合法的课程号')
            else:
                result = self.user_cnt.withdrawCourse(course_id)
                if result:
                    showinfo('提示信息', '提交成功, 请刷新课程表查看是否选课')
                else:
                    showinfo('提示信息', '撤课失败')
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

a = JWXT()
a.mainloop()
