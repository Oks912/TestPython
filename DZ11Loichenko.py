import random

class Elephants:

    def __init__(self, weight, age, breed, character):
        self.weight = weight
        self.age = age
        self.breed = breed
        self.character = character


    @staticmethod
    def generate_breakfast():
        foods = ["Carrot", "Сabbage", "Grass", "Fruits"]
        return "Breakfast fo elephants:" + random.choice(foods)


elephant_1 = Elephants(6000, 10, "Elephas", "playful")
elephant_2 = Elephants(6000, 10, "Loxodonta", "kindly")

random_name = Elephants.generate_breakfast()
print(random_name)
print(elephant_1.breed)
print(elephant_2.breed)

