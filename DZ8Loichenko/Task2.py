# Task2 Створіть обробку одного будь-якого exception, який не використався як приклад на занятті. Виведіть результат в консоль
try:
    text = input('ВВедіть що небудь --> ')
except EOFError:
    print('Помилка EOF:') # CTRL + D
except KeyboardInterrupt:
    print('Ви відмінили операцію.') # CTRL+F2
else:
    print('Ви ввели {0}'.format(text))


