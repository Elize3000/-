import tkinter
import tkinter as tk
from tkinter import ttk, LEFT, END, PhotoImage

class AdminsWork(tkinter.Tk):
    def __init__(self,Name,Label1_text,Label2_text,Button1_text,Button2_text,Button3_text): #Инициализация объекта,Задание начальных данных
        super().__init__() #Инициализация объекта, как потомка от родительского класса
        self.FormName=Name  #Имя формы
        #self.MainWindow = tk.Tk()
        self.title(self.FormName)
        # Выпадающий список таблиц
        self.admin_label = tk.Label(self, text=Label1_text)
        self.admin_label.pack()
        self.inform_label = tk.Label(self, text=Label2_text)
        self.inform_label.pack()
        self.AddUser_button = ttk.Button(self, text=Button1_text, command=None)
        self.AddUser_button.pack()
        self.DeleteUser_button = ttk.Button(self, text=Button2_text, command=None)
        self.DeleteUser_button.pack()
        self.Report_button = ttk.Button(self, text=Button3_text, command=None)
        self.Report_button.pack()


class AddUserForm(tkinter.Tk):

    def __init__(self,Name,Label1_text,Label2_text,Edit1_description_text,Edit2_description_text,Edit3_description_text,Edit4_description_text,Edit5_description_text,Edit6_description_text,Edit1_default_text,Edit2_default_text,Edit3_default_text,Edit4_default_text,Edit5_default_text,Edit6_default_text,combobox1_description_text,combobox1_Values,combobox2_description_text,combobox2_Values,Avatar_label_caption,Avatar,Button1_caption,Button2_caption):#Инициализация объекта,Задание начальных данных
        super().__init__()
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

        self.frame_Edit4 = tk.Frame(self)
        self.frame_Edit4.pack()
        self.Edit4_lable = ttk.Label(self.frame_Edit4, text=Edit4_description_text)
        self.Edit4_lable.pack(side=LEFT)
        self.Edit4_textbox = ttk.Entry(self.frame_Edit4)
        self.Edit4_textbox.pack(side=LEFT)
        self.Edit4_textbox.delete(0, last=END)
        self.Edit4_textbox.insert(0, Edit4_default_text)

        self.frame_Edit5 = tk.Frame(self)
        self.frame_Edit5.pack()
        self.Edit5_lable = ttk.Label(self.frame_Edit5, text=Edit5_description_text)
        self.Edit5_lable.pack(side=LEFT)
        self.Edit5_textbox = ttk.Entry(self.frame_Edit5)
        self.Edit5_textbox.pack(side=LEFT)
        self.Edit5_textbox.delete(0, last=END)
        self.Edit5_textbox.insert(0, Edit5_default_text)

        self.frame_Edit6 = tk.Frame(self)
        self.frame_Edit6.pack()
        self.Edit6_lable = ttk.Label(self.frame_Edit6, text=Edit6_description_text)
        self.Edit6_lable.pack(side=LEFT)
        self.Edit6_textbox = ttk.Entry(self.frame_Edit6)
        self.Edit6_textbox.pack(side=LEFT)
        self.Edit6_textbox.delete(0, last=END)
        self.Edit6_textbox.insert(0, Edit6_default_text)
        self.frame_combobox1 = tk.Frame(self)
        self.frame_combobox1.pack()
        self.combobox1_lable = tk.Label(self.frame_combobox1, text=combobox1_description_text)
        self.combobox1_lable.pack(side=LEFT)
        self.combobox1_combobox = ttk.Combobox(self.frame_combobox1)
        self.combobox1_combobox['values'] = combobox1_Values
        self.combobox1_combobox.pack(side=LEFT)

        self.frame_combobox2 = tk.Frame(self)
        self.frame_combobox2.pack()
        self.combobox2_lable = tk.Label(self.frame_combobox2, text=combobox2_description_text)
        self.combobox2_lable.pack(side=LEFT)
        self.combobox2_combobox = ttk.Combobox(self.frame_combobox2)
        self.combobox2_combobox['values'] = combobox2_Values
        self.combobox2_combobox.pack(side=LEFT)

        self.Add_button = ttk.Button(self, text=Button1_caption, command=None)
        self.Add_button.pack()

        self.Back_button = ttk.Button(self, text=Button2_caption, command=None)
        self.Back_button.pack()

class DeleteRepeatUserForm(tkinter.Tk):

    def __init__(self,Name,Label1_text,Label2_text,Label3_text,Edit1_description_text,Edit2_description_text,Edit3_description_text,Edit1_default_text,Edit2_default_text,Edit3_default_text,Button1_caption,Button2_caption):#Инициализация объекта,Задание начальных данных
        super().__init__()
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


        self.Del_button = ttk.Button(self, text=Button1_caption, command=None)
        self.Del_button.pack()

        self.Back_button = ttk.Button(self, text=Button2_caption, command=None)
        self.Back_button.pack()

        self.Repeat_label = tk.Label(self, text=Label3_text)
        self.Repeat_label.pack()


class DeleteUserForm(DeleteRepeatUserForm):

    def __init__(self, Name, Label1_text, Label2_text, Label3_text, Edit1_description_text, Edit2_description_text,
                 Edit3_description_text, Edit1_default_text, Edit2_default_text, Edit3_default_text, Button1_caption,
                 Button2_caption,Button3_caption):  # Инициализация объекта,Задание начальных данных
        super().__init__( Name, Label1_text, Label2_text, Label3_text, Edit1_description_text, Edit2_description_text,
                 Edit3_description_text, Edit1_default_text, Edit2_default_text, Edit3_default_text, Button1_caption,
                 Button2_caption)

        self.Repeat_button = ttk.Button(self, text=Button3_caption, command=None)
        self.Repeat_button.pack()

class UsersWork(tkinter.Tk):
    def __init__(self,Name,Label1_text,Label2_text,Button1_text,Button2_text,Button3_text,Button4_text,Button5_text,Button6_text,Button7_text): #Инициализация объекта,Задание начальных данных
        super().__init__() #Инициализация объекта, как потомка от родительского класса
        self.FormName=Name  #Имя формы
        #self.MainWindow = tk.Tk()
        self.title(self.FormName)
        # Выпадающий список таблиц
        self.admin_label = tk.Label(self, text=Label1_text)
        self.admin_label.pack()
        self.inform_label = tk.Label(self, text=Label2_text)
        self.inform_label.pack()
        self.AddProduct_button = ttk.Button(self, text=Button1_text, command=None)
        self.AddProduct_button.pack()
        self.EditProduct_button = ttk.Button(self, text=Button2_text, command=None)
        self.EditProduct_button.pack()
        self.DeleteProduct_button = ttk.Button(self, text=Button3_text, command=None)
        self.DeleteProduct_button.pack()
        self.Inventarization_button = ttk.Button(self, text=Button4_text, command=None)
        self.Inventarization_button.pack()
        self.MakeBill_button = ttk.Button(self, text=Button5_text, command=None)
        self.MakeBill_button.pack()
        self.Report_button = ttk.Button(self, text=Button6_text, command=None)
        self.Report_button.pack()
        self.ShowInv_button = ttk.Button(self, text=Button7_text, command=None)
        self.ShowInv_button.pack()

class СreateBill(tkinter.Tk):
    def __init__(self,Name,Label1_text,Label2_text,Edit1_description_text,Edit2_description_text,Edit3_description_text,Edit4_description_text,Edit1_default_text,Edit2_default_text,Edit3_default_text,Edit4_default_text,Label_score1,Label_score2,Label_score3,Label_score4,Button1_caption,RadioButtonVars):#Инициализация объекта,Задание начальных данных
        super().__init__()
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

        self.frame_Edit4 = tk.Frame(self)
        self.frame_Edit4.pack()
        self.Edit4_lable = ttk.Label(self.frame_Edit4, text=Edit4_description_text)
        self.Edit4_lable.pack(side=LEFT)
        self.Edit4_textbox = ttk.Entry(self.frame_Edit4)
        self.Edit4_textbox.pack(side=LEFT)
        self.Edit4_textbox.delete(0, last=END)
        self.Edit4_textbox.insert(0, Edit4_default_text)

        self.frame_Radio = tk.Frame(self)
        self.frame_Radio.pack()

        # Tkinter string variable
        # able to store any string value
        v = tk.StringVar(self.frame_Radio, "1")

        # Dictionary to create multiple buttons
        values={}
        for k in range (0,len(RadioButtonVars)):
            values[RadioButtonVars[k]]=str(k+1)

        # Loop is used to create multiple Radiobuttons
        # rather than creating each button separately
        for (text, value) in values.items():
           tk.Radiobutton(self.frame_Radio, text=text, variable=v,
                        value=value).pack(side='top', ipady=5)
        self.score_number_label = tk.Label(self, text=Label_score1)
        self.score_number_label.pack()
        self.score_count_label = tk.Label(self, text=Label_score2)
        self.score_count_label.pack()
        self.score_transfer_label = tk.Label(self, text=Label_score3)
        self.score_transfer_label.pack()
        self.score_total_label = tk.Label(self, text=Label_score4)
        self.score_total_label.pack()


        self.Add_button = ttk.Button(self, text=Button1_caption, command=None)
        self.Add_button.pack()


class MakeInvForm(tkinter.Tk):
    def __init__(self,Name,Label1_text,Label2_text,Label3_text,Edit1_description_text,combobox1_description_text,combobox1_Values,Edit1_default_text,Button1_caption,Button2_caption):#Инициализация объекта,Задание начальных данных
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

        self.Ask_label = tk.Label(self, text=Label3_text)
        self.Ask_label.pack()
        self.Ask_button = ttk.Button(self, text=Button1_caption, command=None)
        self.Ask_button.pack()

        self.frame_Edit1 = tk.Frame(self)
        self.frame_Edit1.pack()
        self.Edit1_lable = ttk.Label(self.frame_Edit1, text=Edit1_description_text)
        self.Edit1_lable.pack(side=LEFT)
        self.Edit1_textbox = ttk.Entry(self.frame_Edit1)
        self.Edit1_textbox.pack(side=LEFT)
        self.Edit1_textbox.delete(0, last=END)
        self.Edit1_textbox.insert(0, Edit1_default_text)

        self.Inv_button = ttk.Button(self, text=Button2_caption, command=None)
        self.Inv_button.pack()