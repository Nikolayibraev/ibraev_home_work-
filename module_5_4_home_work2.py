#--------------- H O M E  W O R K  (M O D U L E _ 5 _ 3) ---------------
class House:
    houses_history = []
    def __new__ (cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)                 # Выучить эту строку
    def __init__ (self, name, num_of_floor):
        self.name = name
        self.num_of_floor = num_of_floor
    def __del__(self):
       print(f'{self.name} остался в памяти')
    def go_to (self, new_floor):
        for i in range(1,new_floor+1):
            if new_floor <= self.num_of_floor:
                print(i)
        if new_floor > self.num_of_floor or new_floor < 1:
            print('Такого этажа не существует')
    def __len__ (self):
        return self.num_of_floor
    def __eq__ (self, other):
        if isinstance(other, House):
            return self.num_of_floor == other.num_of_floor      # ==
        elif isinstance(other, int):
            return self.number_of_floors == other
    def __lt__ (self, other):
        if isinstance(other, House):
            return self.num_of_floor < other.num_of_floor       # >
        elif isinstance(other, int):
            return self.number_of_floor < other
    def __le__ (self, other):
        return self.__eq__(other) or self.__lt__(other)    # <=
    def __gt__ (self, other):
        return not self.__le__(other)       # <
    def __ge__ (self, other):
        return not self.__le__(other)      # >=
    def __ne__ (self, other):
        return not self.__eq__(other)
#        return self.num_of_floor != other.num_of_floor      # !=
    def __str__ (self):
        return f'{self.name}, {self.num_of_floor} эт.'
    def __add__(self, other):
        if isinstance(other, House):
            return self.num_of_floor + other.num_of_floor
        return NotImplemented
    def __radd__(self, other):
        if isinstance(other, int):  # Если другой операнд - это целое число
            return self.num_of_floor + other
        return NotImplemente

h1 = House('9-й микрорайон', 9)
print(House.houses_history)
h2 = House('Домик в деревне', 2)
print(House.houses_history)
h3 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h4 = House('ЖК Акация', 20)
print(House.houses_history)

del h1
print(House.houses_history)
