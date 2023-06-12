import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/photos')
photos = response.json()

for photo in photos:
    print(photo)


with open('response_data1.json', 'w') as file:
    json.dump(photos, file)
    print("JSON data saved to response_data.json")