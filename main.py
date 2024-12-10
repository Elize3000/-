# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import work_with_database as db
from user_controller import UserController


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ApplicationName = 'Управление инвентарем'
    con = db.FireBirdDataBaseConnection('/OIIS_lab2/OMIS.FDB', 'SYSDBA', 'masterkey').connection
    CurrentUser = UserController(con, ApplicationName)
    CurrentUser.TakeUser()
    if CurrentUser.IsAdminSelect:
        CurrentUser.WorkAsAdmin()
    else:
        CurrentUser.WorkAsUser()
    con.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
