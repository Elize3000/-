import tkinter
import tkinter as tk
from tkinter import ttk, LEFT, END, PhotoImage
from tkcalendar import Calendar
import work_with_database as db

class AddProductForm(tkinter.Tk):
    def __init__(self,Name,Label1_text,Label2_text,Edit1_description_text,Edit2_description_text,Edit3_description_text,combobox1_description_text,combobox1_Values,Edit4_description_text,Edit1_default_text,Edit2_default_text,Edit3_default_text,Edit4_default_text,Button1_caption):#Инициализация объекта,Задание начальных данных
        super().__init__()
        #self.ApplicationName = ApplicationName
        self.FormCaption=Name
        self.title(self.FormCaption)
        # Выпадающий список таблиц
        self.admin_label = tk.Label(self, text=Label1_text)
        self.admin_label.pack()
        self.inform_label = tk.Label(self, text=Label2_text)
        self.inform_label.pack()

        self.frame_Edit1 = tk.Frame(self)
        self.frame_Edit1.pack()
        self.Edit1_lable = ttk.Label(self.frame_Edit1, text=Edit1_description_text)
        self.Edit1_lable.pack(side=LEFT)
        self.Edit1_textbox = ttk.Entry(self.frame_Edit1)
        self.Edit1_textbox.pack(side=LEFT)
        self.Edit1_textbox.delete(0, last=END)
        self.Edit1_textbox.insert(0, Edit1_default_text)

        self.frame_Edit2 = tk.Frame(self)
        self.frame_Edit2.pack()
        self.Edit2_lable = ttk.Label(self.frame_Edit2, text=Edit2_description_text)
        self.Edit2_lable.pack(side=LEFT)
        self.Edit2_textbox = ttk.Entry(self.frame_Edit2)
        self.Edit2_textbox.pack(side=LEFT)
        self.Edit2_textbox.delete(0, last=END)
        self.Edit2_textbox.insert(0, Edit2_default_text)

        self.frame_Edit3 = tk.Frame(self)
        self.frame_Edit3.pack()
        self.Edit3_lable = ttk.Label(self.frame_Edit3, text=Edit3_description_text)
        self.Edit3_lable.pack(side=LEFT)
        self.Edit3_textbox = ttk.Entry(self.frame_Edit3)
        self.Edit3_textbox.pack(side=LEFT)
        self.Edit3_textbox.delete(0, last=END)
        self.Edit3_textbox.insert(0, Edit3_default_text)

        self.frame_combobox1 = tk.Frame(self)
        self.frame_combobox1.pack()
        self.combobox1_lable = tk.Label(self.frame_combobox1, text=combobox1_description_text)
        self.combobox1_lable.pack(side=LEFT)
        self.combobox1_combobox = ttk.Combobox(self.frame_combobox1)
        self.combobox1_combobox['values'] = combobox1_Values
        self.combobox1_combobox.pack(side=LEFT)

        self.frame_Edit4 = tk.Frame(self)
        self.frame_Edit4.pack()
        self.Edit4_lable = ttk.Label(self.frame_Edit4, text=Edit4_description_text)
        self.Edit4_lable.pack(side=LEFT)
        self.Edit4_textbox = ttk.Entry(self.frame_Edit4)
        self.Edit4_textbox.pack(side=LEFT)
        self.Edit4_textbox.delete(0, last=END)
        self.Edit4_textbox.insert(0, Edit4_default_text)

        self.Add_button = ttk.Button(self, text=Button1_caption, command=None)
        self.Add_button.pack()
class UpdProductForm(tkinter.Tk):
    def __init__(self,Name,Label1_text,Label2_text,Edit5_description_text,Edit5_default_text,Edit1_description_text,Edit2_description_text,Edit3_description_text,combobox1_description_text,combobox1_Values,Edit4_description_text,Edit1_default_text,Edit2_default_text,Edit3_default_text,Edit4_default_text,Button1_caption):#Инициализация объекта,Задание начальных данных
        super().__init__()
        self.FormCaption=Name
        self.title(self.FormCaption)
        # Выпадающий список таблиц
        self.admin_label = tk.Label(self, text=Label1_text)
        self.admin_label.pack()
        self.inform_label = tk.Label(self, text=Label2_text)
        self.inform_label.pack()

        self.frame_Edit5 = tk.Frame(self)
        self.frame_Edit5.pack()
        self.Edit5_lable = ttk.Label(self.frame_Edit5, text=Edit5_description_text)
        self.Edit5_lable.pack(side=LEFT)
        self.Edit5_textbox = ttk.Entry(self.frame_Edit5)
        self.Edit5_textbox.pack(side=LEFT)
        self.Edit5_textbox.delete(0, last=END)
        self.Edit5_textbox.insert(0, Edit5_default_text)

        self.frame_Edit1 = tk.Frame(self)
        self.frame_Edit1.pack()
        self.Edit1_lable = ttk.Label(self.frame_Edit1, text=Edit1_description_text)
        self.Edit1_lable.pack(side=LEFT)
        self.Edit1_textbox = ttk.Entry(self.frame_Edit1)
        self.Edit1_textbox.pack(side=LEFT)
        self.Edit1_textbox.delete(0, last=END)
        self.Edit1_textbox.insert(0, Edit1_default_text)

        self.frame_Edit2 = tk.Frame(self)
        self.frame_Edit2.pack()
        self.Edit2_lable = ttk.Label(self.frame_Edit2, text=Edit2_description_text)
        self.Edit2_lable.pack(side=LEFT)
        self.Edit2_textbox = ttk.Entry(self.frame_Edit2)
        self.Edit2_textbox.pack(side=LEFT)
        self.Edit2_textbox.delete(0, last=END)
        self.Edit2_textbox.insert(0, Edit2_default_text)

        self.frame_Edit3 = tk.Frame(self)
        self.frame_Edit3.pack()
        self.Edit3_lable = ttk.Label(self.frame_Edit3, text=Edit3_description_text)
        self.Edit3_lable.pack(side=LEFT)
        self.Edit3_textbox = ttk.Entry(self.frame_Edit3)
        self.Edit3_textbox.pack(side=LEFT)
        self.Edit3_textbox.delete(0, last=END)
        self.Edit3_textbox.insert(0, Edit3_default_text)

        self.frame_combobox1 = tk.Frame(self)
        self.frame_combobox1.pack()
        self.combobox1_lable = tk.Label(self.frame_combobox1, text=combobox1_description_text)
        self.combobox1_lable.pack(side=LEFT)
        self.combobox1_combobox = ttk.Combobox(self.frame_combobox1)
        self.combobox1_combobox['values'] = combobox1_Values
        self.combobox1_combobox.pack(side=LEFT)

        self.frame_Edit4 = tk.Frame(self)
        self.frame_Edit4.pack()
        self.Edit4_lable = ttk.Label(self.frame_Edit4, text=Edit4_description_text)
        self.Edit4_lable.pack(side=LEFT)
        self.Edit4_textbox = ttk.Entry(self.frame_Edit4)
        self.Edit4_textbox.pack(side=LEFT)
        self.Edit4_textbox.delete(0, last=END)
        self.Edit4_textbox.insert(0, Edit4_default_text)

        self.Upd_button = ttk.Button(self, text=Button1_caption, command=None)
        self.Upd_button.pack()

class DelProductForm(tkinter.Tk):
    def __init__(self,Name,Label1_text,Label2_text,Edit1_description_text,Edit2_description_text,combobox1_description_text,combobox1_Values,Edit1_default_text,Edit2_default_text,Button1_caption):#Инициализация объекта,Задание начальных данных
        super().__init__()
        self.FormCaption=Name
        self.title(self.FormCaption)
        # Выпадающий список таблиц
        self.admin_label = tk.Label(self, text=Label1_text)
        self.admin_label.pack()
        self.inform_label = tk.Label(self, text=Label2_text)
        self.inform_label.pack()

        self.frame_combobox1 = tk.Frame(self)
        self.frame_combobox1.pack()
        self.combobox1_lable = tk.Label(self.frame_combobox1, text=combobox1_description_text)
        self.combobox1_lable.pack(side=LEFT)
        self.combobox1_combobox = ttk.Combobox(self.frame_combobox1)
        self.combobox1_combobox['values'] = combobox1_Values
        self.combobox1_combobox.pack(side=LEFT)

        self.frame_Edit1 = tk.Frame(self)
        self.frame_Edit1.pack()
        self.Edit1_lable = ttk.Label(self.frame_Edit1, text=Edit1_description_text)
        self.Edit1_lable.pack(side=LEFT)
        self.Edit1_textbox = ttk.Entry(self.frame_Edit1)
        self.Edit1_textbox.pack(side=LEFT)
        self.Edit1_textbox.delete(0, last=END)
        self.Edit1_textbox.insert(0, Edit1_default_text)

        self.frame_Edit2 = tk.Frame(self)
        self.frame_Edit2.pack()
        self.Edit2_lable = ttk.Label(self.frame_Edit2, text=Edit2_description_text)
        self.Edit2_lable.pack(side=LEFT)
        self.Edit2_textbox = ttk.Entry(self.frame_Edit2)
        self.Edit2_textbox.pack(side=LEFT)
        self.Edit2_textbox.delete(0, last=END)
        self.Edit2_textbox.insert(0, Edit2_default_text)


        self.Del_button = ttk.Button(self, text=Button1_caption, command=None)
        self.Del_button.pack()

class ReportSettingsForm(tkinter.Tk):

    def __init__(self,Name,Label1_text,Label2_text,combobox1_description_text,combobox1_Values,Calendar1_description_text,Calendar2_description_text,Button1_caption,Button2_caption,Bt2_visible):#Инициализация объекта,Задание начальных данных
        super().__init__()
        self.FormCaption=Name
        self.title(self.FormCaption)
        # Выпадающий список таблиц
        self.admin_label = tk.Label(self, text=Label1_text)
        self.admin_label.pack()
        self.inform_label = tk.Label(self, text=Label2_text)
        self.inform_label.pack()
        self.frame_combobox1 = tk.Frame(self)
        self.frame_combobox1.pack()
        self.combobox1_lable = tk.Label(self.frame_combobox1, text=combobox1_description_text)
        self.combobox1_lable.pack(side=LEFT)
        self.combobox1_combobox = ttk.Combobox(self.frame_combobox1)
        self.combobox1_combobox['values'] = combobox1_Values
        self.combobox1_combobox.pack(side=LEFT)

        self.frame_Calendar1 = tk.Frame(self)
        self.frame_Calendar1.pack()
        self.Calendar1_lable = ttk.Label(self.frame_Calendar1, text=Calendar1_description_text)
        self.Calendar1_lable.pack(side=LEFT)
        self.CalendarDate1 = Calendar(self.frame_Calendar1, selectmode = 'day', year = 2024, month = 12, day = 1)
        self.CalendarDate1.pack()

        self.frame_Calendar2 = tk.Frame(self)
        self.frame_Calendar2.pack()
        self.Calendar2_lable = ttk.Label(self.frame_Calendar2, text=Calendar2_description_text)
        self.Calendar2_lable.pack(side=LEFT)
        self.CalendarDate2 = Calendar(self.frame_Calendar2, selectmode = 'day', year = 2024, month = 12, day = 31)
        self.CalendarDate2.pack()

        self.Watch_button = ttk.Button(self, text=Button1_caption, command=None)
        self.Watch_button.pack()

        self.Watch_and_send_button = ttk.Button(self, text=Button2_caption, command=None)
        if Bt2_visible:
            self.Watch_and_send_button.pack()
        else:
            self.Watch_and_send_button.pack_forget()


class TableForm(tkinter.Tk):

    def __init__(self,Name,Label1_text,SelectQuery,DataBaseConnection,Button1_caption):#Инициализация объекта,Задание начальных данных
        super().__init__()
         #self.fbQ =fbExecuteSelectQuery(SelectQuery,DataBaseConnection).GetDataFromDataBase()
        self.FormCaption=Name
        self.title(Name)
        # Выпадающий список таблиц
        self.admin_label = tk.Label(self, text=Label1_text)
        self.admin_label.pack()
        self.columnsQ, self.rows=db.fbExecuteSelectQuery(SelectQuery,DataBaseConnection).GetDataFromDataBase()
        self.tree = ttk.Treeview(self, show='headings')
        self.tree.pack(fill='both', expand=True)
        self.scrollbarVert = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.scrollbarVert.pack(side='left', fill='y')
        self.tree.configure(yscroll=self.scrollbarVert.set)
        self.scrollbarHorizont = ttk.Scrollbar(self, orient="horizontal", command=self.tree.xview)
        self.scrollbarHorizont.pack(side='bottom', fill='x')
        self.tree.configure(xscroll=self.scrollbarHorizont.set, columns=self.columnsQ)
#        self.tree.["columns"] = self.columnsQ
        for col in self.columnsQ:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        # Заполняем данными
        for row in self.rows:
            self.tree.insert("", "end", values=row)
