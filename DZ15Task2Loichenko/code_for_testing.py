import csv


class CsvEditor:

    def __init__(self, filename):
        self.filename = filename

    def add_row(self, row):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)

    def delete_row(self, row):
        with open(self.filename, 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for r in rows:
                if r != row:
                    writer.writerow(r)