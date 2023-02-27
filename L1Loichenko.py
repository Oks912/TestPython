#Task1
first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")
full_name = first_name + " " + last_name
print(full_name)
print(full_name.title())
print((first_name + " ") * 5)
new_full_name = "\t" + first_name + "\n " + last_name
print(new_full_name)
change_full_name1 = (new_full_name.replace("\n", ""))
change_full_name2 =(change_full_name1.split())
change_full_name2 = "".join(change_full_name2)
print(change_full_name2)

#Task2
from math import pi
radius = float(input("Please enter radius circle: "))
text = f" circle_length:  {pi * radius**2} and circle_area:{pi * radius * radius} "
print(text)

#Task3
import requests
from bs4 import BeautifulSoup

url = 'https://minfin.com.ua/currency/nbu/'
source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)
tr = soup.find('p', {'class': 'sc-1x32wa2-9 glerpA'})
tr = tr.text
tr = (tr.replace(",", "."))
tr = (tr[:5])
doll = "Сurrent dollar: " + str(tr)
print(doll)
doll = float(str(tr))
UAH = input("Enter the amount to exchange UAH:")
Total = int(UAH) / float(doll)
print(round(Total, 2))









