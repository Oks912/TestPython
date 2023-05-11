from abc import ABC, abstractmethod

class Art_gallery(ABC):  # Абстрактний клас Art_gallery
    def __init__(self):
        self.name = None
        self.artist = None
        self.size = None
        self.technique = None

    @abstractmethod
    def show(self):
        pass


class Renaissance(Art_gallery):  # Наслідуємо абстрактний клас Art_gallery
    def __init__(self):
        super().__init__()
        self.name = "Secret Supper"
        self.artist = 'Leonardo da Vinci'
        self.size = '460 см × 880 см'
        self.technique = 'tempers'


    def show(self):  #Поліморфізм
        print('We are goin to vizit in Santa Maria delle Grazie in Milan, Italy.')


class Realism(Art_gallery):

    def __init__(self):
        super().__init__()
        self.name = "Potato Pickers"
        self.artist = 'Jean-Francois'
        self.size = '83,8 см * 111,8 см.'
        self.technique = 'oil paints on canvas.'


    def show(self):  #Поліморфізм
        print('We are going to visit in Van Gogh Museum in Amsterdam, Netherlands')



class Modernism(Art_gallery):
    def __init__(self):
        super().__init__()
        self.name = "The Night"
        self.artist = 'Modigliani'
        self.size = '65.4 см x 81.3 см'
        self.technique = 'oil paints on canvas.'
        self.__ticket_count = 0


    def show(self):   #Поліморфізм
        self.__Buy_ticket()
        self.__Find_gallery()
        print('We are goin to vizit in Museum of Modern Art in New York')
        self.__ticket_count +=1  # інкапсуляція даних

    def __Buy_ticket(self):           # Скриття (encapsulation) - приватний метод
        print("We are buy ticket")

    def __Find_gallery(self):          # Скриття (encapsulation) - приватний метод
        print("The route is built")

    @property
    def ticket_count(self):
        return self.__ticket_count

    @ticket_count.setter
    def ticket_count(self, value):
        self.__ticket_count = value

    @property
    def discount(self):
        if self.ticket_count > 2:
            return "You have discount ticket"
        else:
            return "You haven't discount for next ticket"


picture = Modernism()
print(picture.ticket_count)
picture.show()
picture.show()
picture.show()
print(picture.ticket_count)
print(picture.discount)
