import random
from fighter import Fighter
#Here I am going to be storing the templates for different AI fighter classes
class Warrior(Fighter):
    def __init__(self):
        self.health=40
        self.crit_damage=10
        self.crit_chance=5
        self.block_chance=10
        self.dodge_chance=10
        self.dodge_attack=5
        self.normal_attack=random.randrange(20)
        self.name=''
        #need a list of attack to choose from automaticly
    