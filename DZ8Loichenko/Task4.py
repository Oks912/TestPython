import datetime

date1 = datetime.datetime.now()
date2 = datetime.datetime(year=1991, month=12, day=9)
if date1.month < date2.month or (date1.month < date2.month and date1.day > date2.day):
    vik2 = (date1.year - date2.year) -1
    print("Мій вік: ", vik2)
else:
    vik2 = date1.year - date2.year
    print("Мій вік: ",  vik2)
date4 = date1.timestamp() - date2.timestamp()
print("Мій вікж: ", date4)




