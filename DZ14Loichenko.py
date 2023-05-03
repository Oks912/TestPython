class Train:
    def __init__(self, name):
        self.name = name
        self.stations = []
        self.cars = []

    def __len__(self):
        return len(self.cars) - 1  # Віднімаєм один вагон з локомативом

    def __getitem__(self, index):
        return self.cars[index]

    def add_car(self, car):
        self.cars.append(car)

    def add_station(self, stations):
        self.stations.append(stations)

    def __str__(self):
        return f"Train '{self.name}' has {len(self)} cars and is currently on station {self.stations[-1]}"

class TrainCar:
    def __init__(self, number, max_passengers):
        self.number = number
        self.passengers = []
        self.max_passengers = max_passengers

    def __len__(self):
        return len(self.passengers)

    def __getitem__(self, index):
        return self.passengers[index]

    def add_passenger(self, passenger):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(passenger)

    def __str__(self):
        return f"Train car {self.number} has {len(self)} passengers:\n" + \
               "\n".join([f"\t{name}: {destination}, place {place}" for name, destination, place in self.passengers])

class Passenger:
    def __init__(self, name, destination, place):
        self.name = name
        self.destination = destination
        self.place = place

    def __str__(self):
        return f"name: {self.name}, destination: {self.destination}, place: {self.place}"


train = Train("Express Харків Київ")

# Додаємо вагони до поїзда
train.add_car(TrainCar(0, 0)) #локоматив
train.add_car(TrainCar(1, 10))
train.add_car(TrainCar(2, 8))
train.add_car(TrainCar(3, 12))

# Додаємо стпнції до маршрута поїзда
train.add_station("Station 1")
train.add_station("Station 2")
train.add_station("Station 3")

# Додаємо пасажирів до поїзда
train[0].add_passenger(Passenger("Олег", "Харків", 12))
train[0].add_passenger(Passenger("Ганна", "Полтава", 47))
train[1].add_passenger(Passenger("Дмитро", "Харків", 54))
train[2].add_passenger(Passenger("Оксана", "Київ", 9))

# Вивод інформації про поїзд та вагони
print(f"Train '{train.name}' has {len(train)} cars:")
for car in train:
    print(f"Train car {car.number} has {len(car)} passengers:")
    for passenger in car:
        print(f"\t{passenger}")

print(f"\nTrain '{train.name}' is currently on station {train.stations[-1]}")