# Task1
import random

random_Val = random.randint(0, 59)
print('Random number: ', random_Val)

if random_Val >= 0 or random_Val <= 15:
    print('Число в першій четверті')
elif random_Val >= 16 or random_Val <= 30:
    print('Число в другій четверті')
elif random_Val >= 31 or random_Val <= 45:
    print('Число в третій четверті')
elif random_Val >= 46 or random_Val <= 59:
    print('Число в четвертій четверті')

# Tasdk3
n = random.randint(0, 2000)
print("Random: ", n)
cuma = 0
if n > 5:
    di = n % 10
    cuma = cuma + di
    n = n // 10
    if not cuma % 3:
        print("Число ділиться na 6")
    else:
        print("Число не ділиться  на 6")
else:
    print("Число не ділиться на 6")

# Task4
print("Введіть координати точки")
x = float(input("Введіть x: "))
y = float(input("Введіть y: "))

if x > 0 and y > 0:
    print('Точка у I чверті ')
elif x < 0 and y > 0:
    print('Точка у II чверті')
elif x < 0 and y < 0:
    print('Точка у III чверті')
elif x > 0 and y < 0:
    print('Точка у IV чверті')
elif x == 0 and y == 0:
    print("Точка в центрі координат")
elif x == 0:
    print("Точка на осі Y")
elif y == 0:
    print("Точка на осі X")

# Task2

while True:
    try:
        mis = int(input("Enter birthday month: "))
        if mis > 12:
            print('Невірний нормер місяця')
        if 0 < mis <= 12:
            zima_list = [12, 1, 2]
            vesna_list = [3, 4, 5]
            lito_list = [6, 7, 8]
            osin_list = [9, 10, 11]
            if mis in zima_list:
                print('Зима - За вікном падав сніг.')
            elif mis in vesna_list:
                print('Весна - Все довкола розцвітало.')
            elif mis in lito_list:
                print('Літо - Діти насолоджувались літніми канікулами.')
            elif mis in osin_list:
                print('Осінь - Все довкола загоралось яскравими фарбами.')
    except ValueError:
        print("Вы ввели не число")
        break
