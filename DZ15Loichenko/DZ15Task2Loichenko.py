from abc import ABC, abstractmethod
from datetime import datetime

class Dish(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

class Risotto(Dish):
    def get_name(self):
        return "Risotto"

    def get_price(self):
        return 20.0

class Pasta(Dish):
    def get_name(self):
        return "Pasta"

    def get_price(self):
        return 15.5

class Pizza(Dish):
    def get_name(self):
        return "Pizza"

    def get_price(self):
        return 12.0

class Beverages(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

class Beer(Beverages):
    def get_name(self):
        return "Beer"

    def get_price(self):
        return 5.0

class Water(Beverages):
    def get_name(self):
        return "Water"

    def get_price(self):
        return 0

class Cola(Beverages):
    def get_name(self):
        return "Cola"

    def get_price(self):
        return 2.5

class OrderPart:
    def __init__(self):
        self.dishes = []
        self.beverages = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def add_beverages(self, beverage):
        self.beverages.append(beverage)

    def get_dishes(self):
        return self.dishes

    def get_beverages(self):
        return self.beverages

    def get_total_price(self):
        total = 0.0
        for dish in self.dishes:
            total += dish.get_price()
        for beverages in self.beverages:
            total += beverages.get_price()
        return total

class Order:
    def __init__(self):
        self.time = datetime.now()
        self.order_parts = []

    def add_order_part(self, order_part):
        self.order_parts.append(order_part)

    def get_time(self):
        return self.time

    def get_order_parts(self):
        return self.order_parts

    def get_total_price(self):
        total = 0.0
        for order_part in self.order_parts:
            total += order_part.get_total_price()
        return total


# Приклад створення замовлення
order = Order()

# Додаємо перше замовлення
order_part_1 = OrderPart()
order_part_1.add_dish(Risotto())
order_part_1.add_dish(Pasta())
order_part_1.add_beverages(Beer())
order.add_order_part(order_part_1)

# Додаємо друге замовлення
order_part_2 = OrderPart()
order_part_2.add_dish(Pizza())
order_part_2.add_beverages(Water())
order_part_2.add_beverages(Cola())
order.add_order_part(order_part_2)

# Отримуємо інформацію про замовлення
print("Order Time: {}".format(order.get_time()))
print("Order Total Price: {}".format(order.get_total_price()))

for i, order_part in enumerate(order.get_order_parts()):
    print("\nOrder Part {}:".format(i+1))
    for dish in order_part.get_dishes():
        print("- Dish: {} (Price: {})".format(dish.get_name(), dish.get_price()))
    for beverage in order_part.get_beverages():
        print("- Beverages: {} (Price: {})".format(beverage.get_name(), beverage.get_price()))

