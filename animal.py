# Parent class - Animal
class Animal:
    def __init__(self, name, breed, weight):
        self.name = name
        self.breed = breed
        self.weight = weight

    def eat_food(self):
        return "nom nom"

# Child class 1 - Cat
class Cat(Animal):
    def __init__(self, name, breed, weight, lives):
        super().__init__(name, breed, weight)
        self.lives = lives
    
    
    def meow(self):
        return "Meeeeooooww"

# Child class 2 - Chicken
class Chicken(Animal):
    def __init__(self, name, breed, weight, eggs):
        super().__init__(name, breed, weight)
        self.eggs = eggs

    def cluck(self):
        return "Cluck cluck"
    


cat_1 = Cat("Felix", "Sphynx", 5, 9)
print (cat_1.lives)
print(cat_1.eat_food())

chicken_1 = Chicken("Mary","Leghorn", 10, 5)
print(chicken_1.name)
print(chicken_1.eggs)
print (chicken_1.cluck())
print (chicken_1.eat_food())





    

