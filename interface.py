import tkinter
import tkinter as tk
from tkinter import ttk, LEFT, END, PhotoImage

class MainForm(tkinter.Tk):
# Инициализация объекта,Задание начальных данных
# Создается форма с 2 кнопками
# Name -название формы
# Label_text - описание инструкция пользователю
# Button1_text-Button2_text Наименования соответствующих кнопок
    def __init__(self,Name,Label_text,Button1_text,Button2_text):
        super().__init__() #Инициализация объекта, как потомка от родительского класса
        self.FormName=Name  #Имя формы
        #self.MainWindow = tk.Tk()
        self.title(self.FormName)
        # Выпадающий список таблиц
        self.inform_label = tk.Label(self, text=Label_text)
        self.inform_label.pack()
        self.User_button = ttk.Button(self, text=Button1_text, command=None)
        self.User_button.pack()
        self.Admin_button = ttk.Button(self, text=Button2_text, command=None)
        self.Admin_button.pack()