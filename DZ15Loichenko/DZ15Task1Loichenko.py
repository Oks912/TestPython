def singleton(cls):
    # Cловник для збеоеження класу
    instances = {}

    # Функція яка повертає єдиний клас
    def get_instance(*args, **kwargs):
        # Якщо клас ще не створений додаємо його в instances
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        # Повертаємо єдиний екземпляр
        return instances[cls]

    return get_instance

@singleton
class HandLuggage:
    def __init__(self, size, weight):
        self.size = size
        self.weight = weight

    def info(self):
        # Інформація про ручну кладь
        print(f"Розмір: {self.size} см")
        print(f"Вага: {self.weight} кг")


hand_luggage1 = HandLuggage('25x40x20', 7)
hand_luggage2 = HandLuggage('20x30x15', 5)

# Перевіряю що це один і той же об'єкт
print (id(hand_luggage1) == id(hand_luggage2))
print (id(hand_luggage1))
print (id(hand_luggage2))


hand_luggage1.info()
hand_luggage2.info()