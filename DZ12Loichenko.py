from abc import ABC, abstractmethod

class Plane(ABC):
    def __init__(self):
        self.type = None
        self.range = None
        self.airline = None
        self.speed = None
        self.fly = True
        self.height = None

    def arrive(self):
        print("The plane is arrived")


    def deppart(self):
        print("The plane is departing")


    @abstractmethod
    def airport(self):
        pass



class Boing(Plane):
    def __init__(self):
        super(Boing, self).__init__()
        self.type = "777"
        self.range = "16000"
        self.airline = "Canada air"
        self.speed = "900"
        self.height = "13000"

    def airport(self):
        print("from Toronto")



class Airbus(Plane):
    def __init__(self):
        super(Airbus, self).__init__()
        self.type = "A380"
        self.range = "15000"
        self.airline = "Emirates"
        self.speed = "945"
        self.height = "13100"

    def airport(self):
        print("from Dubai")





boing = Boing()
boing.airport()
print(boing.type)
airbus = Airbus()
airbus.airport()
print(airbus.type)

