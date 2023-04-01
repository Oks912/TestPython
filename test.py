import re

file = open("authors.txt")
values = file.read().split("\n")
data = []

for key in values:
    value = re.findall(r"[-+]?\d*\.\d+|\d+", key)

    if value != []:
        data.append(value)