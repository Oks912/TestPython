mylist = []    #Створюємо пустий список
while True:    # Cтворюємо цикл в якому розмістимо блок команд
    element = input("Введіть ключове слово: add, earliest, latest, longest, shortest, exit: ")  # Присвоюемо змінній команду з консолі
    if element == 'add':                        # Додаемо нивий нотаток використовуючи метод append для додавання нового элемента у кінець списку
        mylist.append(input("Новий нотаток:"))
        print("Новий готаток додано: ", mylist[-1])
    elif element == "earliest":                 # Виводимо список у хронологічному порядку
        for element in mylist:
            print("Від найновішої до найпізнішої: ", element)
    elif element == "latest":                    #Виводимо список використовучи метод сортировки від найпізнішої до найновішої
        for element in sorted(mylist, reverse=True):
            print("Від найпізнішої до найновішої: ", element)
    elif element == "longest":                    #Виводимо список викурустовуючи сортировку по довжині элементів
        for element in sorted(mylist, key=len, reverse=True):
            print(element)
    elif element == "shortest":                   #Виводимо список викурустовуючи сортировку по довжині элементів
        for element in sorted(mylist, key=len, reverse=False):
            print(" Від найкоротшої до найдовшої: ", element)
    elif element == "exit":
        break
    else:
        print("Некоректний ввод. Введіть існуючу команду: add, earliest, latest, longest, shortest, exit:")


