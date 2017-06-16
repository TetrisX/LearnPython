#Напечатайте в консоль даты: вчера, сегодня, месяц назад

from datetime import datetime, timedelta


dt_now = datetime.now()
print(dt_now.strftime('%d.%m.%Y'))

period_1 = timedelta(days=1)
dt_yest = dt_now - period_1
print(dt_yest.strftime('%d.%m.%Y'))

period_2 = timedelta(days=30)
dt_month = dt_now - period_2

print(dt_month.strftime('%d.%m.%Y'))

# Превратите строку "01/01/17 12:10:03.234567" в объект datetime

strin = '01/01/17'
date_str = datetime.strptime(strin,'%d/%m/%Y')

print(date_str)