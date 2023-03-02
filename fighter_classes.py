import random
from fighter import Fighter
#Here I am going to be storing the templates for different AI fighter classes
class Warrior(Fighter):
    def __init__(self):
        self.attacks={'slash':10,'stab':15,'shield bash':10,'armored kick':5}
        self.health=50
        self.crit_damage=10
        self.crit_chance=5
        self.block_chance=10
        self.dodge_chance=10
        self.dodge_attack=5
        self.name=' '
        self.normal_attack=self.random_attack()
    def random_attack(self):
        attacks=self.attacks.keys()
        attack=[]
        for item in attacks:
            attack.append(item)
        random_attack=random.choice(attack)
        normal_attack=self.attacks[random_attack]
        if self.name==' ':
            print(f"Unknown warrior {normal_attack}'s you!")
        else:
            print(f"{self.name} {normal_attack}'s you!")
        return normal_attack
class Militia(Fighter):
    def __init__(self):
        self.attacks={'slash':5,'stab':10,'kick':2,'punch':2}
        self.health=25
        self.crit_damage=10
        self.crit_chance=5
        self.block_chance=5
        self.dodge_chance=5
        self.dodge_attack=5
        self.name=''
        self.normal_attack=self.random_attack()
    def random_attack(self):
        attacks=self.attacks.keys()
        attack=[]
        for item in attacks:
            attack.append(item)
        random_attack=random.choice(attack)
        normal_attack=self.attacks[random_attack]
        if self.name==' ':
            print(f"Unknown warrior {normal_attack}'s you!")
        else:
            print(f"{self.name} {normal_attack}'s you!")
        return normal_attack