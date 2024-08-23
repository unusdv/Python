class Player:
    # Attribute
    health = 100

    # Constructor 
    def __init__(self, name, w):
        self.name = name
        self.weapon = w

    # Method
    def shoot(self, player):
        if player.health <= 0:
            print(f"{self.name} -> {player.name}")
        player.health -= 20

    def salomlash(self):
        print(f"Hello! I'm {self.name}")

    def give_money(self):
        return 500


# Inheritance
class Terror (Player):
    def plant(self):
        print("The bomb has been planted")


class Counter (Player):
    def defuse(self):
        print("The bomb has been defused")

