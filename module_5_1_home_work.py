class House:
    def __init__ (self, name, num_of_floor):
        self.name = name
        self.num_of_floor = num_of_floor

    def go_to (self, new_floor):
        for i in range(1,new_floor):
            print(i)

        if new_floor > self.num_of_floor or new_floor < 1:
            print('Такого этажа не сущесствует')

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(21)
h2.go_to(4)







