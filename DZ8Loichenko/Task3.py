import datetime

a = input('Дата (рррр-мм-дд): ')
b = input('Кідбкість днів: ')
c = input (str('Введіть + для додавання або - для віднімання'))
a = a.split('-')
aa = datetime.date(int(a[0]), int(a[1]), int(a[2]))
b = int(b)
bb = datetime.timedelta(days=b)
if c == "-" :
    Dif = aa - bb
    print(Dif)
else:
    Dif = aa + bb
    print(Dif)