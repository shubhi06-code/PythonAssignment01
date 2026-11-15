class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def display(self):
        print("Name:", self.name)
        print("Health:", self.health)

    def attack(self):
        print(self.name, "attacks")

class Warrior(Character):
    def attack(self):
        print(self.name, "attacks with a sword")

class Mage(Character):
    def attack(self):
        print(self.name, "casts a magic spell")

class Archer(Character):
    def attack(self):
        print(self.name, "shoots an arrow")

warrior = Warrior("Thor", 100)
mage = Mage("Merlin", 80)
archer = Archer("Robin", 90)

for character in [warrior, mage, archer]:
    character.display()
    character.attack()
