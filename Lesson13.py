import csv

# with open("group.txt", "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter= ',')
#     row_counter = 0
#     for row in csv_reader:
#         print(row)

a = []
b = {1:2}
with open("group.txt", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter= ',')
    row_counter = 0
    for row in csv_reader:
        a.append(row)
        b.update(row)
        print(row)
print(a)
print(b)

# with open("group_2.csv", mode='w', newline = '') as csv_file:
#     group_writer = csv .writer(csv_file, delimiter=':')
#     group_writer.writerow(['name', 'group', 'birthday'])
#     group_writer.writerow(['Maria', 'python','March'])
#     group_writer.writerow(['Oleksii', 'python', 'March'])


#
# with open("group_3.csv", mode='w') as csv_file:
#     field_names = ['name', 'group', 'birthday']
#     group_writer = csv.DictWriter(csv_file, fieldnames=field_names)
#     group_writer.writeheader()
#     group_writer.writerow({'name': 'Oleksii', 'group': 'python', 'birthday': 'March'})

# new_list = []
# with open("group_4.csv", 'r') as example:
#     reader_csv = csv.reader(example, delimiter=',')
#     for row in reader_csv:
#         new_list.append(row)
#
# print(new_list)
#
# new_list.append(['Oleksii', 'python', 'March'])
#
# print(new_list)
#
# with open("group_5.csv", 'w', newline='') as example_2:
#     writer_csv = csv.writer(example_2, delimiter=',')
#     #writer_csv.writerows(new_list)
#     for row in new_list:
#         writer_csv.writerow(row)


# def my_gen():
#     counter = 0
#     while True:
#         yield counter
#         counter +=1
# generator = my_gen()
# #print(my_gen())
# print(next(generator))
# print(next(generator))
# print(next(generator))
