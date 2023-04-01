#1 Написати функцію, яка отримує у вигляді параметра ім'я файлу назви інтернет доменів (domains.txt) та повертає їх у вигляді списку рядків (назви повертати без крапки).

def reader(domains_file):
        domains = open(domains_file, "r")
        text = domains.read()
        name = text.replace(".", "")
        print(name)


reader("domains.txt")

#2 Написати функцію, яка отримує у вигляді параметра ім'я файлу (names.txt)
# і повертає список усіх прізвищ з нього. Кожен рядок файлу містить номер, прізвище, країну. Файл створити власноруч і запистаи туди дані

def reader2(names_file):
        names = open(names_file, "r")
        surnames = '\n'.join([line.split()[1] for line in names.readlines()])
        print(surnames)


reader2("names.txt")

#3 Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt)
# і повертає список словників виду {"date": date} у яких date - це дата з рядка (якщо є),
# Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]


def parse(file_name):
    file = open(file_name, "r")
    date = (line.split("-") for line in file.readlines())
    return {'date': date}


parse("authors.txt")
print(parse(file_name="authors.txt"))
#print(parse(file_name=[{'date': date }]))







