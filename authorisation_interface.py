import tkinter
import tkinter as tk
from tkinter import ttk, LEFT, END, PhotoImage

class LoginForm(tkinter.Tk):
    def __init__(self,Name,Label_text,Edit1_description_text,Edit2_description_text,Edit1_default_text,Edit2_default_text,Button1_caption,Button2_caption): #Инициализация объекта,Задание начальных данных
        super().__init__()
        self.FormCaption=Name
        self.title(self.FormCaption)
        # Выпадающий список таблиц

        self.inform_label = tk.Label(self, text=Label_text)
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

        self.Login_button = ttk.Button(self, text=Button1_caption, command=None)
        self.Login_button.pack()
        self.Restore_button = ttk.Button(self, text=Button2_caption, command=None)
        self.Restore_button.pack()

class WhereRestoreLoginForm(tkinter.Tk):
    def __init__(self,Name,Label_text,Edit1_description_text,Edit1_default_text,Button1_caption):#Инициализация объекта,Задание начальных данных
        super().__init__()
        self.FormCaption=Name
        self.title(self.FormCaption)
        # Выпадающий список таблиц

        self.inform_label = tk.Label(self, text=Label_text)
        self.inform_label.pack()

        self.frame_Edit1 = tk.Frame(self)
        self.frame_Edit1.pack()
        self.Edit1_lable = ttk.Label(self.frame_Edit1, text=Edit1_description_text)
        self.Edit1_lable.pack(side=LEFT)
        self.Edit1_textbox = ttk.Entry(self.frame_Edit1)
        self.Edit1_textbox.pack(side=LEFT)
        self.Edit1_textbox.delete(0, last=END)
        self.Edit1_textbox.insert(0, Edit1_default_text)

        self.Send_button = ttk.Button(self, text=Button1_caption, command=None)
        self.Send_button.pack()

class SetNewPasswordForm(tkinter.Tk):
    def __init__(self,Name,Label_text,Edit1_description_text,Edit2_description_text,Edit3_description_text,Edit1_default_text,Edit2_default_text,Edit3_default_text,Button1_caption):#Инициализация объекта,Задание начальных данных
        super().__init__()
        self.FormCaption=Name
        self.title(self.FormCaption)
        # Выпадающий список таблиц

        self.inform_label = tk.Label(self, text=Label_text)
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

        self.Restore_button = ttk.Button(self, text=Button1_caption, command=None)
        self.Restore_button.pack()