#--------------- H O M E  W O R K  (M O D U L E _ 5 _ 3) ---------------
class House:
    def __init__ (self, name, num_of_floor):
        self.name = name
        self.num_of_floor = num_of_floor

    def go_to (self, new_floor):
        for i in range(1,new_floor+1):
            if new_floor <= self.num_of_floor:
                print(i)

        if new_floor > self.num_of_floor or new_floor < 1:
            print('Такого этажа не существует')

    def __len__ (self):
        return self.num_of_floor
    def __eq__ (self, other):
        return self.num_of_floor == other.num_of_floor      # ==
    def __lt__ (self, other):
        return self.num_of_floor < other.num_of_floor       # >
    def __le__ (self, other):
        return self.num_of_floor <= other.num_of_floor      # <=
    def __gt__ (self, other):
        return self.num_of_floor < other.num_of_floor       # <
    def __ge__ (self, other):
        return self.num_of_floor >= other.num_of_floor      # >=
    def __ne__ (self, other):
        return self.num_of_floor != other.num_of_floor      # !=
    def __str__ (self):
        return f'{self.name}, {self.num_of_floor} эт.'
    def __add__(self, other):
        if isinstance(other, House):
            return self.num_of_floor + other.num_of_floor
        return NotImplemented
    def __radd__(self, other):
        if isinstance(other, int):  # Если другой операнд - это целое число
            return self.num_of_floor + other
        return NotImplemented

h1 = House('9-й микрорайон', 9)
h2 = House('Домик в деревне', 2)
h1.go_to(4)
h2.go_to(89)

print(str(h1))
print(str(h2))
print(len(h1))
print(len(h2))

print(h1)
print(h1==h2)         # __eq__

print(type(h1.num_of_floor))

total_floor = h1 + h2   # Вызов метода __add__
print()      # Вывод: 11
print(h1==h2)

total_floor_int = 5 + h1   # Вызов метода __radd__
print(total_floor_int)     # Вывод: 14 (5 + 9)

print(h1<h2)          # __lt__
print(h1<=h2)         # __le__
print(h1>h2)          # __gt__
print(h1>=h2)         # __ge__
print(h1!=h2)         # __ne__



