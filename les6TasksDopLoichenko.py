# Task: Напишіть програму на Python для знаходження перетину двох заданих масивів за допомогою лямбда.
arr1 = ['m', 'y', 't', 'h', '4', 'k', ' ', '=', '.', '0']
arr2 = ['k', 'y', '4', 'e', 'v', ' ', '2', '.', '0']
# Лямбда-функция с использованием filter() для поиска общих значений
out = list(filter(lambda it: it in arr1, arr2))
print("Отфильтрованный список:", out)

# Task: Напишіть програму на Python, щоб перевірити, чи є заданий рядок числом, за допомогою лямбда
arr3 = 'sdfsdfsdsg'
ch = lambda r: True if r.isdigit() else False
print(ch(arr3))

# Напишіть програму на Python, щоб знайти список із максимальною та мінімальною довжиною за допомогою лямбда
from functools import reduce

arr4_dict = ['m', 'y', 't', 'h', '4', 'k', ' ', '=', '.', '0']
arr6_dict = ['k', 'y', '4', 'e', 'v', '.', '0']

test_1 = lambda x: (x if (len(arr4_dict)) > (len(arr6_dict)) else print("Минимальная длинна у второго списка", (len(arr6_dict))))
print("Максимальная длинна у первого списка", test_1)



# Напишіть програму на Python для обчислення добутку заданого списку
my_numbers = [78, 3.6, 6, 45, 11]
print(reduce(lambda res, x: res * x, my_numbers, 1))
