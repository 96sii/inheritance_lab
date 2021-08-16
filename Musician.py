class Musician:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Guitarist(Musician):
    def __init__(self, name, age, strings):
        super().__init__(name, age)
        self.strings = strings

guitarist_1 = Guitarist("Pablo", 16, 6)

print (guitarist_1.name)
