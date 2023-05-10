import csv
from DZ15Task2Loichenko.code_for_testing import CsvEditor

# Перевірка додавання рядка
def test_add_row():
    editor = CsvEditor('test_data.csv')
    editor.add_row(['Alice', 28, 'Female'])

    with open('test_data.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    assert ['Alice', '28', 'Female'] in rows


# Перевірка видалення рядка
def test_delete_row():
    editor = CsvEditor('test_data.csv')
    editor.delete_row(['Mary', '30', 'Female'])

    with open('test_data.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    assert ['Mary', '30', 'Female'] not in rows