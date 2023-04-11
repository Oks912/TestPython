

import re

string = "ThisIsATestString"

string_spaces = re.sub(r"(\w)([A-Z])", r"\1 \2", string) #Ділимо на группи та ставимо пробіл між 1 та 2

print(string_spaces)