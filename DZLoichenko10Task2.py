from random import randint

my_list = [randint(1, 10) for _ in range(100)]

for i in range(1, 11):
    count = my_list.count(i)
    print(f"{i}: {count}")