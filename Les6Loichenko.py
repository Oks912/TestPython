while True:
    try:
        a = float(input("Enter length a: "))
        b = float(input("Enter length b: "))
        c = float(input("Enter length c: "))
        d = float(input("Enter length d: "))
        break
    except ValueError:
        print('Недопустимый ввод')


def priam(a, b, c, d):
    return (a ** 2 + b ** 2) == (c ** 2 + d ** 2)
    print("Це прямокутник")


def area(a, b):
   S = a * b
   return S


def squire(a, b, c, d):
    if a == b == d == c:
     return True
    return False


issqui = squire(a, b, c, d)
ispriam = priam(a,b,c,d)
if issqui:
    print("Це квадрат")
if ispriam:
    print("Площа прямокутника:", area(a,b))
else:
    print("Прямокутник не опуклий")



