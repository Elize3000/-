from tkinter.messagebox import showinfo, showerror
from admin_interface import AdminsWork, AddUserForm, DeleteRepeatUserForm, DeleteUserForm, СreateBill, MakeInvForm, \
    UsersWork
from product_controller import ProductController
from report_controller import ReportController
import authorisation_interface as ai
import interface
import work_with_database as db

class UserController(db.fbDataSet):
# Инициализация класса, задание начальных данных
    def __init__(self,DataBaseConnection, ApplicationName):
        self.ApplicationName = ApplicationName
        #Задание основного запроса в базу для данного объекта
        self.SelectSQL= "Select ID, USERNAME, USER_PASSWORD, EMAIL, DATE_OF_BIRTH, AVATAR, USER_ROLE, IS_TWO_FACTOR_AUTENTIFICATION, FAMILIYA, IMYA, OTCHESTVO, DEPARTMENT_NAME, DOLGNOST From TB_USER"
        #Задание первичного ключа объекта
        self.KeyField = "ID"
        #Задание полей объекта
        self.FieldsList =["ID", "USERNAME", "USER_PASSWORD", "EMAIL", "DATE_OF_BIRTH", "AVATAR", "USER_ROLE",
                          "IS_TWO_FACTOR_AUTENTIFICATION","FAMILIYA","IMYA","OTCHESTVO","DEPARTMENT_NAME","DOLGNOST"]
        #Указание соединения с баой данных
        self.DataBaseConnection = DataBaseConnection
        #Указание наименования таблицы базы данных
        self.TableName = "TB_USER"
        #Указание является ли пользователь администратором
        self.IsAdminSelect=False
        #Текущий логин пользователя
        self.CurrentUserName=""
        #Текущий пароль пользователя
        self.CurrentUserPassword=""
        #Текущий идентификатор пользователя в базе данных
        self.CurrentUserID=-1
        #Указание был ли подтвержден код восстановления пароля
        self.RestoreKod=-1
        #Указатель куда отправлялся код восстановления пароля
        self.RestoreAdress=""
        #Указание были ли подтверждены данные пользователя для удаления
        self.IsRepeat=False
        #Инициализация объекта как потомка
        super().__init__(self.SelectSQL,self.TableName,self.FieldsList,self.KeyField,self.DataBaseConnection)

# Вспомогательный метод получения данных пользователя из базы по его логину
    def GetUserDataByUserName(self,FindingUserName): #Получить данные пользователя по его имени
        print(FindingUserName)
        columns, rows = self.GetSpecificRowFromDataBase("Where USERNAME="+"\'"+FindingUserName+"\'")
        if len(rows)==0:
            return None
        else:
            return rows[0]


#Метод получить пользователя (его идентификатор). Сначала выбирается роль пользователя,
#затем дается возможность залогиниться и найти его идентификатор
    def TakeUser(self):
        self.TakeUserRole()
        UserRoleRus=""
        if self.IsAdminSelect:
            UserRoleRus="Администратор"
        else:
            UserRoleRus = "Пользователь"
        self.TakeUserLogin(UserRoleRus)
#Метод для определения роли пользователя
    def TakeUserRole(self): #Получить роль пользователя(Администратор или Пользователь)
    #Обработчик события выбора входа как администратор
        def GetAdminLogin(): #Получать администратора
            self.IsAdminSelect = True
            Main_Window.destroy()
    #Обработчик события выбора входа как пользователь
        def GetUserLogin():#Получать пользователя
            self.IsAdminSelect = False
            Main_Window.destroy()

        Main_Window = interface.MainForm(self.ApplicationName, 'Сделайте выбор желаемой роли', 'Войти как пользователь',
                               'Войти как администратор')
        Main_Window.Admin_button["command"] = GetAdminLogin
        Main_Window.User_button["command"] = GetUserLogin
        Main_Window.wait_window()

#Метод получения идентификатора пользователя по Логину и паролю пользователя
    def TakeUserLogin(self, UserRoleCaption):
        LoginWindow = ai.LoginForm(self.ApplicationName, 'Авторизация как ' + UserRoleCaption, 'Логин', 'Пароль',
                                'User3', '', 'Логин', 'Забыли пароль?')
     #Обработчик события проверить Логин и Пароль на наличие соответствующих данных и получить идентификатор пользователя
        def GetLogin():
            self.CurrentUserName = LoginWindow.Edit1_textbox.get()
            self.CurrentUserPassword = LoginWindow.Edit2_textbox.get()
            CheckUserSQL = "select IS_Login, User_ID from sp_check_login(" + "\'" + self.CurrentUserName + "\'" + " , " + "\'" + self.CurrentUserPassword + "\'" + ")"
            print(CheckUserSQL)
            columns, rows = db.fbExecuteSelectQuery(CheckUserSQL, self.DataBaseConnection).GetDataFromDataBase()
            if rows[0][0] == 1:
                showinfo('Авторизация пользователя', "Вы успешно авторизированы")
                self.CurrentUserID = rows[0][1]
                LoginWindow.destroy()
                return 0
            else:
                showinfo('Авторизация пользователя', "Не верно указаны логин или пароль")
                return -1
    #Обработчик события запроса восстановления пароля в форме логина пользователя
        def RestorePasswordOnLogin():
            CurUs = LoginWindow.Edit1_textbox.get()
            self.RestoreUserPassword(CurUs)

        LoginWindow.Login_button["command"] = GetLogin
        LoginWindow.Restore_button["command"] = RestorePasswordOnLogin
        LoginWindow.wait_window()


#Метод восстановить пароль
    def RestoreUserPassword(self,UserForRestore):
        FormRestore = ai.WhereRestoreLoginForm('Восстановление пароля', 'Восстановление пароля',
                                            'Введите номер телефона или Email', '', 'Получить код')
    #Обработчик события отправить код для восстановления пароля
        def sendNewPassword():
            self.RestoreAdress=FormRestore.Edit1_textbox.get()
            if '@' in FormRestore.Edit1_textbox.get():
                self.RestoreKod=777
                showinfo('Восстановление пароля',
                         message='Ваш код 777 для восстановления пароля отправлен на указанную электронную почту')
                FormRestore.destroy()
            else:
                self.RestoreKod=111
                showinfo('Восстановление пароля',
                         message='Ваш код 111 для восстановления пароля отправлен в SMS на указанный номер телефона')
                FormRestore.destroy()
            return 0
        FormRestore.Send_button["command"]=sendNewPassword
        FormRestore.wait_window()
    #Обработчик события проверки корректности данных для восстановления пароля и его замены в базе данных
        def CheckNewPasswordFormData():
            NewUserData=[]
            if str(UpdForm.Edit1_textbox.get())!=str(self.RestoreKod):
                showinfo('Ошибка восстановления пароля','Неверно указан код подтверждения пароля!')
            elif UpdForm.Edit2_textbox.get()!=UpdForm.Edit3_textbox.get():
                showinfo('Ошибка восстановления пароля','Указанные пароли не совпадают!')
            else :
                CurrentUserRow=self.GetUserDataByUserName(UserForRestore)
                if CurrentUserRow==None:
                    showinfo('Ошибка восстановления пароля','Указанного пользователя не обнаружено!')
                else:
                    CurrentUserKeyVal=CurrentUserRow[0]
                    NewUserData.insert(0,"\'"+UpdForm.Edit2_textbox.get()+"\'")
                    self.UpdateSpecificFieldsInRow(CurrentUserKeyVal,["USER_PASSWORD"],NewUserData)
                    showinfo('восстановление пароля', 'Пароль восстановлен!')
                UpdForm.destroy()

        if self.RestoreKod>0:
            UpdForm = ai.SetNewPasswordForm('Восстановление пароля', 'Восстановление пароля', 'Полученный код:',
                                         'Новый пароль', 'Подтвердите новый код', '', '', '', 'Восстановить')
            UpdForm.Restore_button["command"]=CheckNewPasswordFormData
            UpdForm.wait_window()

# Метод установки задач для пользователя как Администратора
    def WorkAsAdmin(self):
        AdminWorksForm = AdminsWork(self.ApplicationName, 'АДМИНИСТРАТОР','Выбор действия' ,'Добавить пользователя',
                               'Удалить пользователя','Отчетность')
        AdminWorksForm.AddUser_button["command"] = self.AddUser
        AdminWorksForm.DeleteUser_button["command"] = self.DeleteUser
        AdminWorksForm.Report_button["command"]=self.ShowReportForm
        AdminWorksForm.wait_window()

# Метод добавить пользователя
    def AddUser(self):
    # Обработчик события отказа от добавления пользователя
        def btBackPress():
            AddUserFrm.destroy()
    # Обработчик события создания новой записи пользователя в базе данных
        def WriteNewUser():
            AddValueFieldsList = ["\'"+AddUserFrm.Edit5_textbox.get()+"\'","\'"+AddUserFrm.Edit6_textbox.get()+"\'","\'"+ ""+"\'", "\'"+AddUserFrm.Edit4_textbox.get()+"\'", "Null", "\'"+"User"+"\'",
                               "0", "\'"+AddUserFrm.Edit2_textbox.get()+"\'", "\'"+AddUserFrm.Edit1_textbox.get()+"\'", "\'"+AddUserFrm.Edit3_textbox.get()+"\'", "\'"+AddUserFrm.combobox1_combobox.get()+"\'",
                               "\'"+AddUserFrm.combobox2_combobox.get()+"\'"]
            self.InsertRow(AddValueFieldsList)
            showinfo('Добавление пользователя','Пользователь успешно добавлен')
            AddUserFrm.destroy()

        AddUserFrm=AddUserForm(self.ApplicationName,'АДМИНИСТРАТОР','Добавление пользователя в систему','Имя','Фамилия','Отчество','Возраст(дата рождения)','Логин','Пароль','Иван','Иванов','Иванович','31.01.2021','Login','Password','Отдел',['Администрация','Бухгалтерия','Магазин'],'Должность',['Администратор','Продавец','Директор','Товаровед','Бухгалтер'],'Личное фото','d:\\PBZ\\User.png','Подтвердить добавление','Вернуться назад')
        AddUserFrm.Back_button["command"]=btBackPress
        AddUserFrm.Add_button["command"]=WriteNewUser
        AddUserFrm.wait_window()


#Метод удаления пользователя из базы данных
    def DeleteUser(self):
        Family = ''  #Текущая фамилия удаляемого пользователя
        Imy = ''     #Текущее имя удаляемого пользователя
        Otchestvo= '' #Текущее отчество удаляемого пользователя
    #Обработчик события отказа от удаления пользователя
        def btBackPress():
            DelUserFrm.destroy()
    #Обработчик события удаления пользователя, включая проверку на прохождение повторного ввода данных
        def DelUser():
            if self.IsRepeat:
                columns, rows=self.GetSpecificRowFromDataBase("Where FAMILIYA="+"\'"+DelUserFrm.Edit2_textbox.get()+"\'"+ " and IMYA = "+"\'"+DelUserFrm.Edit1_textbox.get()+"\'"+" and OTCHESTVO="+"\'"+DelUserFrm.Edit3_textbox.get()+"\'")
                if len(rows)<1:
                    showinfo('Удаление пользователя','В базе данных не надено сведений о пользователе с такими данными')
                else:
                    print(rows[0][0])
                    self.DeleteRow(rows[0][0])
                    DelUserFrm.destroy()
                    showinfo('Удаление пользователя','Пользователь с указанными данными удален')
            else:
                showinfo('Удаление польователя','Сначало необходимо правильно повторить ввод данных пользователя. Нажмите кнопку [Подтвердить]"')


    #Обработчик события подтверждения данных для удаления пользователя
        def RepDelUser():

        #Обработчик события отказа от подтверждения данных удаляемого пользоватея
            def btBackRepPress():
                self.IsRepeat=False
                print(self.IsRepeat)
                RepDelUserFrm.destroy()
        #Обработчик события подтверждения данных удаляемого пользователя на форме подтверждения данных
            def RepitDelUserPress():
                if (RepDelUserFrm.Edit1_textbox.get()==Imy) and (RepDelUserFrm.Edit2_textbox.get()==Family) and (RepDelUserFrm.Edit3_textbox.get()==Otchestvo):
                    self.IsRepeat=True
                    print(self.IsRepeat)
                    RepDelUserFrm.destroy()
                else:
                    showinfo('Удаление пользователя','Введенные данные не совпадают с ранее указанными')

            Imy=DelUserFrm.Edit1_textbox.get()
            Family=DelUserFrm.Edit2_textbox.get()
            Otchestvo=DelUserFrm.Edit3_textbox.get()
            print(self.IsRepeat)
            IsRepeat=False
            print(Imy, Family, Otchestvo)
            RepDelUserFrm = DeleteRepeatUserForm(self.ApplicationName, 'АДМИНИСТРАТОР', 'Удаление пользователя из системы',
                                        'Нажмите подтвердить:', 'Введите Имя', 'Введите Фамилию', 'Введите Отчество',
                                        'Иван', 'Иванов', 'Иванович', 'Подтвердить удаление', 'Вернуться назад')
            RepDelUserFrm.Back_button["command"] = btBackRepPress
            RepDelUserFrm.Del_button["command"] = RepitDelUserPress
            RepDelUserFrm.wait_window()

        DelUserFrm=DeleteUserForm(self.ApplicationName,'АДМИНИСТРАТОР','Удаление пользователя из системы','Нажмите подтвердить:','Введите Имя','Введите Фамилию','Введите Отчество','Иван','Иванов','Иванович','Подтвердить удаление','Вернуться назад' ,' Подтвердить')
        DelUserFrm.Back_button["command"]=btBackPress
        DelUserFrm.Del_button["command"]=DelUser
        DelUserFrm.Repeat_button["command"]=RepDelUser
        DelUserFrm.wait_window()
#Метод выбрать формы отчетности для администратора
    def ShowReportForm(self):
        AdminsReportsNames=['Отчет по пользователям','Отчет по товарам']
        AdminsReportsQuerys=['Select * from TB_USER','Select * from TB_Products']
        RepKontroller = ReportController(self.DataBaseConnection,AdminsReportsNames,AdminsReportsQuerys, self.ApplicationName )
        RepKontroller.ShowSettingsForm(self.ApplicationName,'АДМИНИСТРАТОР','Отчетность','Выбирите раздел',AdminsReportsNames,'Выбирите дату начала','Выбирите дату окончания','Просмотреть отчетность','Просмотреть отчетность и отправить на email',True )

# Метод установки задач для пользователя как Пользователя
    def WorkAsUser(self):
    #Обработчик выбора задачи добавить товар
        def AddProduct():
            prod.AddProduct()
    #Обработчик выбора задачи отредактировать товар
        def UpdProduct():
            prod.UpdProduct()
    #Обработчик выбора задачи удалить товар
        def DelProduct():
            prod.DelProduct()
    #Обработчик выбора задачи оформить счет
        def СreateBillForm():
        #Обработчик события согласия на оформление счета
            def AddBill():
                showinfo('Оформление заказа','Заказ успешно оформлен')
                BillForm.destroy()

            BillForm=СreateBill(self.ApplicationName, 'Пользователь','Оформление заказа','Введите название товара','Введите количество товара(-ов)','Введите ваше ФИО','Введите номер телефона','Товар','1','Иванов Иван Иванович','80297654321','Номер заказа №','Количество товаров, итого','Доставка','Итого','Оформить заказ',["Доставка курьером 25 р.", "Самовывоз 0 р."])
            BillForm.Add_button["command"]=AddBill
            BillForm.wait_window()
    #Обработчик события выбора задачи провести инвентаризацию
        def MakeInvFrm():
        #Обработчик события согласия с инвентариацией в задаче инвентаризации
            def Inved():
                showinfo('Инвентаризация товаров','Инвентаризация окончена')
                MkInvForm.destroy()
        #Обработчик события запроса данных при проведении инвентаризации
            def Asked():
                showinfo('Запрос учетных данных','По данным базы учета в данной категории 1234 товара')

            MkInvForm=MakeInvForm(self.ApplicationName, 'Пользователь','Инвентаризация','Запросить информацию из базы учета','Введите фактические данные','Выберите категорию товаров',['Системный блок', 'Монитор', 'Перефирия'],'1','Запросить','Провести инвентаризацию')
            MkInvForm.Inv_button["command"]=Inved
            MkInvForm.Ask_button["command"]=Asked
            MkInvForm.wait_window()


        UserWorksForm = UsersWork(self.ApplicationName, 'Пользователь','Выбор действия' ,'Добавить товар','Редактировать товар',
                               'Удалить товар','Провести инвентаризацию', 'Создать заказ', 'Сформировать Отчет','просмотреть инвентарь')
        prod=ProductController(self.DataBaseConnection, self.ApplicationName)
        UserWorksForm.AddProduct_button["command"] = AddProduct
        UserWorksForm.EditProduct_button["command"] = UpdProduct
        UserWorksForm.DeleteProduct_button["command"] = DelProduct
        UserWorksForm.Inventarization_button["command"] = MakeInvFrm
        UserWorksForm.MakeBill_button["command"] = СreateBillForm
        UserWorksForm.ShowInv_button["command"] = self.ShowInvForm
        UserWorksForm.Report_button["command"]=self.ShowUserReportForm
        UserWorksForm.wait_window()
#Метод выбрать формы отчетности для Пользователя
    def ShowUserReportForm(self):
        UsersReportsNames=['Отчет по пользователям','Отчет по товарам']
        UsersReportsQuerys=['Select * from TB_USER','Select * from TB_Products']
        RepKontroller = ReportController(self.DataBaseConnection,UsersReportsNames,UsersReportsQuerys, self.ApplicationName)
        RepKontroller.ShowSettingsForm(self.ApplicationName,'Пользователь','Формирование отчета','Выбирите раздел',UsersReportsNames,'Выбирите дату начала','Выбирите дату окончания','Вывести информацию','Просмотреть отчетность и отправить на email',False )
#Метод просмотреть инвентарь
    def ShowInvForm(self):
        UsersReportsNames=['Отчет по инвентарю']
        UsersReportsQuerys=['Select * from TB_Products']
        RepKontroller = ReportController(self.DataBaseConnection,UsersReportsNames,UsersReportsQuerys, self.ApplicationName)
        RepKontroller.CurrentReportID=0
        RepKontroller.WatchReport()