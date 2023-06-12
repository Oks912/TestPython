from xml.etree import ElementTree as et


class XML_manipulation:
    def __init__(self):
        self.root = None

    def xml_to_string(self, xml_data):
        self.root = et.fromstring(xml_data)
        return et.tostring(self.root, encoding='unicode')

    def string_to_xml(self, xml_string):
        self.root = et.fromstring(xml_string)

    def perform_xml_operations(self):
        food_elements = self.root.findall("food")
        print("Назви усіх їж на сніданок:")
        for food in food_elements:
            name = food.find("name").text
            print(name)


manipulator = XML_manipulation()


# Зчитування вмісту файлу XML
with open('D:/Python/L1Loichenko/DZ22Loichenko/my_example.xml', 'r') as file:
    xml_data = file.read()

# Перетворення XML в рядок
xml_string = manipulator.xml_to_string(xml_data)
print(xml_string)

# Декодування рядка в XML
manipulator.string_to_xml(xml_string)
print("Рядок XML:")
print(xml_string)

# Виконання операцій над XML
manipulator.perform_xml_operations()

