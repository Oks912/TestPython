import csv

new_list = [["Oksana","1500"],
            ["Igor","1000"],
            ["Roman","1000"]
            ]
with open("group_4.csv", 'w',newline='') as example:
    writer = csv.writer(example, delimiter=',')
    writer.writerows(new_list)

print(new_list)
new_list.append([['Oleksii', '2200'],
                 ["Viktoriar","1200"]])

print(new_list)

with open("group_5.csv", 'w', newline='') as example_2:
    writer_csv = csv.writer(example_2, delimiter=',')
    writer_csv.writerows(new_list)


