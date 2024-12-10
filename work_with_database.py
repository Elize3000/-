import fdb

class FireBirdDataBaseConnection:
# Инициализация объекта,Задание начальных данных
    def __init__(self,path,user,password):
        self.path=path # Путь к базе данных
        self.user= user # Имя пользователя баы данных
        self.password = password # Пароль пользователя базы данных
        self.connection=fdb.connect(dsn=path,user=user,password=password) #Создание соединения с баззой данных

# Закрытие соединения с базой данных
    def close_connection(self):
        self.connection.close()

class fbExecuteSelectQuery:
# Инициализация объекта,Задание начальных данных
    def __init__(self,SelectSQL,DataBaseConnection):
        self.SelectSQL=SelectSQL #Запрос для выполнения
        self.DataBaseConnection=DataBaseConnection #Соединение с базой данных
# Получение данных из запроса
    def GetDataFromDataBase(self):
        cursor = self.DataBaseConnection.cursor()
        cursor.execute(self.SelectSQL)
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        return columns, rows

class fbDataSet:
# Инициализация объекта,Задание начальных данных
    def __init__(self,SelectSQL,TableName,FieldsList,KeyField,DataBaseConnection):
        self.SelectSQL=SelectSQL #Текст запроса на выборку данных
        self.TableName=TableName #Название таблицы в БД
        self.FieldsList=FieldsList  #Список полей таблицы БД
        self.KeyField=KeyField  #Ключевое поле таблицы БД
        self.DataBaseConnection=DataBaseConnection  #Соединение с базой данных

# Из массива полей формируем строку со списком полей
    def GetListOfFields(self):
        StringOfFields=""
        FieldsCount=len(self.FieldsList)
        StringOfFields=StringOfFields+self.FieldsList[0]
        if FieldsCount>1 :
            for i in range(1,FieldsCount-1):
                StringOfFields=StringOfFields+", "
                StringOfFields=StringOfFields+self.FieldsList[i]
        return StringOfFields

# Из массива значений полей таблицы формируем строку со списком значений не ключевого поля
# ValuesList - массив ззначений не ключевых полей
    def GetListOfNotKeyFieldsValues(self,ValuesList):
        StringOfValues=""
        ValuesCount= len(ValuesList)
        for i in range(0,ValuesCount-1):
            StringOfValues=StringOfValues+", "+ValuesList[i]
        return StringOfValues

# Из массива значений полей таблицы формируем строку ссопоставлением не ключевых полей и их значений
# ValuesList - массив ззначений не ключевых полей
    def GetEquationOfNotKeyFieldsAndValues(self,ValuesList):
        StringOfEquation=""
        EquationCount= len(ValuesList)
        print(EquationCount)
        for i in range(1,EquationCount):
            print (i)
            if i==(EquationCount-1):
                StringOfEquation = StringOfEquation + self.FieldsList[i] + "=" + ValuesList[i - 1]
            else:
                StringOfEquation=StringOfEquation+self.FieldsList[i]+"="+ValuesList[i-1]+", "
        return StringOfEquation

# Из массива значений ряда полей таблицы формируем строку ссопоставлением этих полей и их значений
# ValuesList - массив ззначений  полей
# FieldsList - массив полей
    def GetEquationOfSecificFieldsAndValues(self,FieldsList,ValuesList):
        StringOfEquation=""
        EquationCount= len(ValuesList)
        for i in range(0,EquationCount):
            if i==(EquationCount-1):
                StringOfEquation = StringOfEquation + FieldsList[i] + "=" + ValuesList[i]
            else:
                StringOfEquation=StringOfEquation+FieldsList[i]+"="+ValuesList[i]+", "
        return StringOfEquation

# Записать в базу данных новую строку со значениями полей равными FieldsValues
    def InsertRow(self,FieldsValues):
        cursor = self.DataBaseConnection.cursor()
        insstr = "insert into " + self.TableName+ " ( "+self.GetListOfFields()+" ) Values (gen_id(gen_"+self.TableName+"_"+self.KeyField+",1)"+self.GetListOfNotKeyFieldsValues(FieldsValues)+ ")"
        cursor.execute(insstr)
        self.DataBaseConnection.commit()

# Изменить значения неключевых полей в базе данных для записи со значением поля первичного ключа
# равным KeyFieldValue на значения, содержащиеся в FieldsValues
    def UpdateRow(self,KeyFieldValue,FieldsValues):
        cursor = self.DataBaseConnection.cursor()
        updstr = "update " + self.TableName+ " set  "+self.GetEquationOfNotKeyFieldsAndValues(FieldsValues)+ " where "+self.KeyField+"="+str(KeyFieldValue)
        print(updstr)
        cursor.execute(updstr)
        self.DataBaseConnection.commit()

# Изменить значения неключевых полей, содержащихся в FieldsList, в базе данных для записи
# со значением поля первичного ключа равным KeyFieldValue на значения, содержащиеся в FieldsValues
    def UpdateSpecificFieldsInRow(self,KeyFieldValue,FieldsList,FieldsValues):
        cursor = self.DataBaseConnection.cursor()
        updstr = "update " + self.TableName+ " set  "+self.GetEquationOfSecificFieldsAndValues(FieldsList,FieldsValues)+ " where "+self.KeyField+"="+str(KeyFieldValue)
        print(updstr)
        cursor.execute(updstr)
        self.DataBaseConnection.commit()

# Получить выборку данных по основному запросу
    def GetDataFromDataBase(self):
        cursor = self.DataBaseConnection.cursor()
        cursor.execute(self.SelectSQL)
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        return columns, rows

# Получить выборку данных по соответствующей строке ключевого поля по основному запросу
# KeyFieldValue-значение поля первичного ключа искомой записи
    def GetRowFromDataBase(self,KeyFieldValue):
        WhereStr=" where "+self.KeyField+"="+str(KeyFieldValue)
        return self.GetSpecificRowFromDataBase(WhereStr)

# Получить выборку данных согласно дополнительного условия к основному запросу
# WhereStr- Ограничение на основной запрос для отбора искомых записей
    def GetSpecificRowFromDataBase(self,WhereStr):
        cursor = self.DataBaseConnection.cursor()
        print(self.SelectSQL+" "+WhereStr)
        cursor.execute(self.SelectSQL+" "+WhereStr)
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        return columns, rows
# Удалить в базе данных строку со значение поля первичного ключа равным KeyFieldValue
    def DeleteRow(self,KeyFieldValue):
        cursor = self.DataBaseConnection.cursor()
        delstr = (f"DELETE FROM {self.TableName} "
                  f"where {self.KeyField} = {KeyFieldValue} ")
        print(delstr)
        cursor.execute(delstr)
        self.DataBaseConnection.commit()
        #update_table(table_name)

# Удалить в базе данных строки удовлетворяющие условию, содержащемуся в WhereFilter
    def DeleteSpecificRows(self, WhereFilter):
        cursor = self.DataBaseConnection.cursor()
        delstr = (f"DELETE FROM {self.TableName} "+" "+WhereFilter)
        print(delstr)
        cursor.execute(delstr)
        self.DataBaseConnection.commit()


