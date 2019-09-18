from datetime import date, timedelta, datetime
import datedelta
import locale

locale.setlocale(locale.LC_TIME, "ru_RU")

"""
Домашнее задание №2
Дата и время
* Напечатайте в консоль даты: вчера, сегодня, месяц назад
* Превратите строку "01/01/17 12:10:03.234567" в объект datetime
"""

def print_days():
    dt_now = datetime.now()
    dt_yesterday = dt_now - datedelta.DAY
    dt_month_ago = dt_now - datedelta.MONTH
    print(dt_yesterday.strftime('%d.%m.%Y'))
    print(dt_now.strftime('%d.%m.%Y'))
    print(dt_month_ago.strftime('%d.%m.%Y'))
    
def str_2_datetime(string):
    date_string = string
    date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return(date_dt)


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/17 12:10:03.234567"))