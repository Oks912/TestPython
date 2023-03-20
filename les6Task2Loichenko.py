# task 2
import random

names = ["king", "miller", "kean"]
domains = ["net.", "com.", "ua."]
word_list = "abcdefghijklmnopqrstuvwxyz"
k = random.randint(5, 7)
numb_list = [
    lambda x: (random.choice(names)),
    lambda i: ("."),
    lambda b: (str(random.randint(100, 999))),
    lambda c: ("@"),
    lambda d: (''.join(random.sample(word_list, k))),
    lambda j: ("."),
    lambda l: (random.choice(domains))
]

for el in numb_list:
    print(el(numb_list), end='')
