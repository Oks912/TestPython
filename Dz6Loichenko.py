# Task Напишіть програму яка перевіряє чи стрічка містить лише великі і малі літери, числа на нижнє підкреслення.
import re
pattern1 = re.compile("[\W]")
result = pattern1.findall("dsfs dgfrgG GGG JKJ DF 4548 +_)(*jj +_")
print("Стрічка містить ще: ", result)

# Напишіть програму, що видаляє область дужок в стрічці
pattern = re.compile('(\(\.com\)\",|\"|\(\.com\)")')
res = pattern.sub('', '"example (.com)", "github (.com)", "stackoverflow (.com)" ')
print(res)



