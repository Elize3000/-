import work_with_database as db
from tkinter.messagebox import showinfo, showerror

from product_controller_interface import UpdProductForm, AddProductForm, DelProductForm


class ProductController(db.fbDataSet):
    # Инициализация класса, задание начальных данных
    def __init__(self,DataBaseConnection, ApplicationName):
        self.ApplicationName = ApplicationName
        #Задание основного запроса в базу для данного объекта
        self.SelectSQL= "Select ID, PRODUCT_NAME, PPRODUCT_DESCRIPTION, PRODUCT_COUNT, PRODUCT_CATEGORY, TEGS_AND_ATRIBUTES, PRODUCTS_IMMAGE From TB_PRODUCTS"
        #Задание первичного ключа объекта
        self.KeyField = "ID"
        #Задание полей объекта
        self.FieldsList =["ID", "PRODUCT_NAME", "PPRODUCT_DESCRIPTION", "PRODUCT_COUNT", "PRODUCT_CATEGORY", "TEGS_AND_ATRIBUTES", "PRODUCTS_IMMAGE"]
        #Указание соединения с баой данных
        self.DataBaseConnection = DataBaseConnection
        #Указание наименования таблицы базы данных
        self.TableName = "TB_PRODUCTS"
        #Задание текущего выбранного товара
        self.CurrentProductName=""
        #Наименование текущего выбранного товара
        self.CurrentProductID=-1
        #Инициализация объекта предка
        super().__init__(self.SelectSQL,self.TableName,self.FieldsList,self.KeyField,self.DataBaseConnection)

# Метод добавления товара в базу данных
    def AddProduct(self):
# Обработчик события добавить товар в базу данных
        def WriteNewProduct():
            AddValueFieldsList = ["\'" + AddProductFrm.Edit1_textbox.get() + "\'",
                                  "\'" + AddProductFrm.Edit2_textbox.get() + "\'",
                                  "\'" + AddProductFrm.Edit3_textbox.get() + "\'",
                                  "\'" + AddProductFrm.combobox1_combobox.get() + "\'",
                                   "\'" + AddProductFrm.Edit4_textbox.get() + "\'","Null"]
            self.InsertRow(AddValueFieldsList)
            showinfo('Добавление товара', 'Товар успешно добавлен')
            AddProductFrm.destroy()

        AddProductFrm = AddProductForm(self.ApplicationName, 'Пользователь', 'Добавление товара в систему', 'Добавить название товара', 'Добавить описание товара',
                                 'Указать количество товара (-ов)', 'Указать категорию товара',['Системный блок', 'Монитор', 'Перефирия'], 'Тэги и атрибуты','Товар' ,'Товарный','1','Товар','Подтвердить добавление')
        AddProductFrm.Add_button["command"] = WriteNewProduct
        AddProductFrm.wait_window()
#Метод для редактирования товара в базе данных
    def UpdProduct(self):
#Обработчик события для записи новых данных
        def WriteNewProduct():
            UpdValueFieldsList = ["\'" + UpdProductFrm.Edit1_textbox.get() + "\'",
                                  "\'" + UpdProductFrm.Edit2_textbox.get() + "\'",
                                  "\'" + UpdProductFrm.Edit3_textbox.get() + "\'",
                                  "\'" + UpdProductFrm.combobox1_combobox.get() + "\'",
                                   "\'" + UpdProductFrm.Edit4_textbox.get() + "\'","Null"]
            self.UpdateRow(UpdProductFrm.Edit5_textbox.get(),UpdValueFieldsList)
            showinfo('Редактирование товара', 'Товар успешно изменен')
            UpdProductFrm.destroy()

        UpdProductFrm = UpdProductForm(self.ApplicationName, 'Пользователь', 'Редактирование товара в системе', 'Введите идентификатор записи для редактирования','-1','Изменить название товара', 'Изменить описание товара',
                                 'Изменить количество товара (-ов)', 'Указать категорию товара',['Системный блок', 'Монитор', 'Перефирия'], 'Тэги и атрибуты','Товар' ,'Товарный','1','Товар','Подтвердить редактирование')
        UpdProductFrm.Upd_button["command"] = WriteNewProduct
        UpdProductFrm.wait_window()
#Метод для удаления товара из базы данных
    def DelProduct(self):
#Обработчик события удаления данных
        def DelProduct():
            self.DeleteSpecificRows("Where PRODUCT_CATEGORY="+"\'" + DelProductFrm.combobox1_combobox.get() + "\'"+" and PRODUCT_NAME="+"\'" + DelProductFrm.Edit1_textbox.get() + "\'"+" and PRODUCT_COUNT="+DelProductFrm.Edit2_textbox.get())
            showinfo('Удаление товара', 'Товар успешно удален')
            DelProductFrm.destroy()

        DelProductFrm = DelProductForm(self.ApplicationName, 'Пользователь', 'Удаление товара из системы', 'Введите название товара', 'Введите количество товара',
                                 'Введите категорию товара ', ['Системный блок', 'Монитор', 'Перефирия'], 'Товар','1' ,'Подтвердить удаление')
        DelProductFrm.Del_button["command"] = DelProduct
        DelProductFrm.wait_window()
