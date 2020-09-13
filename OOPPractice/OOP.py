import random

name = input("Enter your name: ")
age = input("How old are you? ")


class Player:

    STATS_MAP = {
        "hp": random.randint(0, 255),
        "mp": random.randint(0, 255),
        "attack": random.randint(0, 50),
        "defense": random.randint(0, 50),
        "intell": random.randint(0, 50)
    }

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hp = self.STATS_MAP["hp"]
        self.mp = self.STATS_MAP["mp"]
        self.attack = self.STATS_MAP["attack"]
        self.defense = self.STATS_MAP["defense"]
        self.intell = self.STATS_MAP["intell"]

    def get_name(self):
        print("Name:", self.name)

    def get_age(self):
        print("Age:", self.age)

    def get_stats(self):
        print("Health:", self.hp)
        print("MP:", self.mp)
        print("Strength:", self.attack)
        print("Toughness:", self.defense)
        print("Intelligence:", self.intell)


char = Player(name, age)

print()
char.get_name()
char.get_age()
char.get_stats()
