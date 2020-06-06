import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from query import JWXTStudent


class JWXT:
    def __init__(self):
        self.user_cnt = JWXTStudent('test')
        self.root = tk.Tk()
        self.root.title('教务系统')
        self.root.geometry('960x540')
        self.root.resizable(False, False)
        self.mainloop = self.root.mainloop

        # widgets for login ui
        self.login_ui = tk.Frame(self.root)  # , bg='lightgreen')

        # login button
        self.login_btn = tk.Button(self.login_ui)
        self.login_btn['text'] = '登录'
        self.login_btn['command'] = self.login_btn_cmd

        # username label
        self.login_usrn_label = tk.Label(self.login_ui)
        self.login_usrn_label['text'] = '用户名'

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
        self.login_ui.pack()

        # notebook frame for main ui
        self.main_ui = ttk.Notebook(self.root, height=540, width=960)

        self.course_table_ui = tk.Frame(self.main_ui, bg='lightyellow')
        self.main_ui.add(self.course_table_ui, text='课程表')
        self.course_available_ui = tk.Frame(self.main_ui, bg='lightblue')
        self.main_ui.add(self.course_available_ui, text='选课')
        self.course_grade_ui = tk.Frame(self.main_ui, bg='lightgreen')
        self.main_ui.add(self.course_grade_ui, text='成绩')

        # course table
        self.course_table_frame1 = tk.Frame(self.course_table_ui)
        self.course_table_tab = ttk.Treeview(self.course_table_frame1, show='headings', height=15)
        self.columns_course_table = ['c_id', 'c_name', 'c_type', 'c_school', 't_name', 'c_credit', 'c_period', 'c_time', 'c_site']
        self.columns_course_table_cn = ['课程号', '课程名', '课程类型', '院系', '授课老师', '学分', '学时', '上课时间', '上课地点']
        self.course_table_tab['columns'] = self.columns_course_table
        for i, j in zip(self.columns_course_table, self.columns_course_table_cn):
            self.course_table_tab.column(i, width='100')
            self.course_table_tab.heading(i, text=j)

        self.course_table_scroll = tk.Scrollbar(self.course_table_frame1, orient='vertical', command=self.course_table_tab.yview)
        self.course_table_tab['yscrollcommand'] = self.course_table_scroll.set

        # course table pack
        self.course_table_scroll.pack(side='right', fill='y')
        self.course_table_tab.pack(side='top', fill='x')
        self.course_table_frame1.pack(side='top', fill='x')

        # query frame
        self.course_table_frame2 = tk.Frame(self.course_table_ui)
        self.course_table_frame21 = tk.Frame(self.course_table_frame2)
        self.course_table_label = tk.Label(self.course_table_frame2, text='筛 选 条 件')
        self.course_table_labels = []
        self.course_table_entrys = []
        for i in self.columns_course_table_cn:
            self.course_table_labels.append(tk.Label(self.course_table_frame21, text='*'))
            self.course_table_entrys.append(tk.Entry(self.course_table_frame21, width=10))

        tmp = 0
        for i, j in zip(self.course_table_labels, self.course_table_entrys):
            i.grid(row=0, column=tmp, padx=5, pady=15)
            tmp += 1
            j.grid(row=0, column=tmp, padx=5, pady=15)
            tmp += 1

        self.course_table_btn = tk.Button(self.course_table_frame2, text='查 询')
        self.course_table_btn['command'] = self.course_table_btn_cmd

        self.course_table_label.grid(row=0, pady=10)
        self.course_table_frame21.grid(row=1, pady=15)
        self.course_table_btn.grid(row=2, pady=15)
        self.course_table_frame2.pack(side='top', fill='x')


        # course grade
        self.course_grade_frame1 = tk.Frame(self.course_grade_ui)
        self.course_grade_tab = ttk.Treeview(self.course_grade_frame1, show='headings', height=15)
        self.columns_course_grade = ['c_name', 'c_type', 'c_credit', 'c_school', 't_name', 'c_grade']
        self.columns_course_grade_cn = ['课程名', '课程类型', '学分', '院系', '授课老师', '成绩']
        self.course_grade_tab['columns'] = self.columns_course_grade
        for i, j in zip(self.columns_course_grade, self.columns_course_grade_cn):
            self.course_grade_tab.column(i, width='100')
            self.course_grade_tab.heading(i, text=j)

        self.course_grade_scroll = tk.Scrollbar(self.course_grade_frame1, orient='vertical', command=self.course_grade_tab.yview)
        self.course_grade_tab['yscrollcommand'] = self.course_grade_scroll.set

        # course grade pack
        self.course_grade_scroll.pack(side='right', fill='y')
        self.course_grade_tab.pack(side='top', fill='x')
        self.course_grade_frame1.pack(side='top', fill='x')

        # query frame
        self.course_grade_frame2 = tk.Frame(self.course_grade_ui)
        self.course_grade_frame21 = tk.Frame(self.course_grade_frame2)
        self.course_grade_label = tk.Label(self.course_grade_frame2, text='筛 选 条 件')
        self.course_grade_labels = []
        self.course_grade_entrys = []
        for i in self.columns_course_grade_cn:
            self.course_grade_labels.append(tk.Label(self.course_grade_frame21, text='*'))
            self.course_grade_entrys.append(tk.Entry(self.course_grade_frame21, width=10))

        tmp = 0
        for i, j in zip(self.course_grade_labels, self.course_grade_entrys):
            i.grid(row=0, column=tmp, padx=15, pady=15)
            tmp += 1
            j.grid(row=0, column=tmp, padx=15, pady=15)
            tmp += 1

        self.course_grade_btn = tk.Button(self.course_grade_frame2, text='查 询')
        self.course_grade_btn['command'] = self.course_grade_btn_cmd

        self.course_grade_label.grid(row=0, pady=10)
        self.course_grade_frame21.grid(row=1, pady=15)
        self.course_grade_btn.grid(row=2, pady=15)
        self.course_grade_frame2.pack(side='top', fill='x')

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
                params[i] = j
        result = self.user_cnt.queryCourseTable(params=params)

        # render
        tmp = self.course_table_tab.get_children()
        self.course_table_tab.delete(*tmp)
        for index, row_data in enumerate(result):
            self.course_table_tab.insert('', index, values=row_data)

    def course_grade_btn_cmd(self):
        # query
        params = {}
        for i, j in zip(self.columns_course_grade, self.course_grade_entrys):
            if j.get():
                params[i] = j
        result = self.user_cnt.queryCourseGrade(params=params)

        # render
        tmp = self.course_grade_tab.get_children()
        self.course_grade_tab.delete(*tmp)
        for index, row_data in enumerate(result):
            self.course_grade_tab.insert('', index, values=row_data)

a = JWXT()
a.mainloop()
