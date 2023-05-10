import csv
import json


class JSONConverter:
    def __init__(self):
        self.__lines = []

    def read_file(self, filename: str):
        with open(filename, 'r') as json_file:
            lines = json.load(json_file)
            for line in lines:
                self.__lines.append(line)
            print(self.__lines)


    def writer_file(self, filename:str):
        with open (filename, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.__lines[0].keys())
            writer.writeheader()
            writer.writerows(self.__lines)
            self.cleanup()


    def cleanup(self):
        self.__lines=[]


converter = JSONConverter()
converter.read_file('dzexample.json')
converter.writer_file('dzexample.csv')
