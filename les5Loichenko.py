# Task2
students_score = {"Petro": 1, "Vasil": 2, "Katerina": 7, "Oksana": 10.5}

avarag = sum(students_score.values()) / len(students_score)

for student in students_score.keys():
    if students_score[student] > avarag:
        print(student)

# Task1 1.Дано два списки чисел. Знайдіть всі числа, що зустрічаються як в першому, так і другому списках, і надрукуйте їх у порядку зростання.
list1 = set([1, 7, 9, 10, 25, 100, 36, 0, 3.5, 45, 47.5])
list2 = set([2, 6, 99, 65, 36.6, 0, 45, 8, 1, 4, 100, 55, 66, 3.5])
list3 = list(list1 & list2)
print(sorted(list3))

# Task3 3. Даний список цілих чисел. Визначте кількість різних значень.
from collections import Counter
listik = [1, 7, 9, 10, 25, 100, 36, 0, 3, 45, 47, 1, 9]
print("Count of different numbers:", len(set(listik)))

# Task4.Дано два списки чисел. Виведіть всі числа, які входять як в перший, так і в другий список в порядку зростання. Вводяться два списки цілих чисел. Всі числа кожного списку знаходяться на окремому рядку.

firstlist = set([1, 3, 6, 5, 76, 87, 87,54,43, 66])
secondlist = set([3, 3,4,5,6,87,100,234,43,66,66,45])
thlist = firstlist & secondlist
th = sorted(list(thlist), reverse=False)
print("Перший список: ", firstlist)
print("Другий список: ", secondlist)
print("Всі числа, які входять як в перший, так і в другий список в порядку зростання:")
for element in th:
    print(element)
 # .Дано рядок тексту, в якому слова розділені пррпусками. Надрукуйте всі слова, які зустрічаються в тексті, та їхні частоти як у вихідних даних

text = 'one two three one four five seven ten seven one'
dict_1 = {}
for word in text.split():
    dict_1[word] = text.split().count(word)
for element in dict_1.items():
  print(element, end = '')
