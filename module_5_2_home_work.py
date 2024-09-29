#--------------- H O M E  W O R K  (M O D U L E _ 5 _ 2) ---------------
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

    def __str__ (self):
        return f'{self.name}, {self.num_of_floor} эт.'

h1 = House('9-й микрорайон', 9)
h2 = House('Домик в деревне', 2)
h1.go_to(7)
h2.go_to(6)

print(str(h1))
print(str(h2))

print(len(h1))
print(len(h2))