class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floors):
        for i in range(1, new_floors + 1):
            if i > self.number_of_floors or i < 1:
                print("Такого этажа не существует")
                break
            else:
                print(i)
h1 = House("ЖК Эльбрус", 30)
print(h1.name)
g = int(input("Введите этаж "))
h1.go_to(g)

