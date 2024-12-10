from tkinter.messagebox import showinfo, showerror
from product_controller_interface import ReportSettingsForm, TableForm
from work_with_database import FireBirdDataBaseConnection

class ReportController():
 #Инициализация класса, задание начальных данных
    def __init__(self, DataBaseConnection, ReportTitleList, ReportQueryList, ApplicationName):
        self.ApplicationName = ApplicationName
        self.DataBaseConnection=DataBaseConnection # Соединение с базой данных
        self.ReportTitleList=ReportTitleList # Набор названий отчетов
        self.ReportQueryList=ReportQueryList # Набор запросов к базе данных для создания соответствующих отчетов
        self.CurrentReportID=0 # Текущий выбранный отчет

# Показ формы настроек и выбора отчетов
    def ShowSettingsForm(self, ApplicationName, Label1_text, Label2_text, combobox1_description_text, combobox1_Values, Calendar1_description_text, Calendar2_description_text, Button1_caption,
                     Button2_caption,Bt2_visible):  # Инициализация объекта,Задание начальных данных

 # Обработчик события показать отчет
        def WatchReport():
            self.CurrentReportID=RepSettings.combobox1_combobox.current()
            self.WatchReport()

 # Обработчик события показать отчет и отправить по почте
        def WatchAndSendReport():
            self.CurrentReportID=RepSettings.combobox1_combobox.current()
            self.WatchAndSendReport()

        RepSettings = ReportSettingsForm(ApplicationName, Label1_text, Label2_text, combobox1_description_text, combobox1_Values, Calendar1_description_text, Calendar2_description_text, Button1_caption,Button2_caption,Bt2_visible)
        RepSettings.Watch_button["command"] = WatchReport
        RepSettings.Watch_and_send_button["command"] = WatchAndSendReport
        RepSettings.wait_window()

 #Показ отчета в форме таблицы
    def WatchReport(self):
        print(self.CurrentReportID)
        RepTitle=self.ReportTitleList[self.CurrentReportID]
        RepQuery=self.ReportQueryList[self.CurrentReportID]
        TBRep=TableForm(self.ApplicationName, RepTitle, RepQuery, self.DataBaseConnection, 'Закрыть')
        TBRep.wait_window()
#Обработчик нажатия показать и отправить по почте
    def WatchAndSendReport(self):
        print(self.CurrentReportID)
        RepTitle=self.ReportTitleList[self.CurrentReportID]
        RepQuery=self.ReportQueryList[self.CurrentReportID]
        TBRep=TableForm(self.ApplicationName, RepTitle, RepQuery, self.DataBaseConnection, 'Закрыть')
        showinfo('Просмотр отчетов','Отчет отправлен на электронную почту')
        TBRep.wait_window()