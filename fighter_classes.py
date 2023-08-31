import random
from fighter import Fighter
#Here I am going to be storing the templates for different AI fighter classes
class Warrior(Fighter):
    """
    This class represents a Warrior AI fighter. It inherits from the Fighter class.
    It defines attributes and methods for a Warrior fighter type.
    """
    def __init__(self):
        """
        Initializes a Warrior AI fighter instance with default attributes.
        """
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
        """
        Selects a random attack from available attacks and returns its damage value.
        """
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
    """
    This class represents a Militia AI fighter. It inherits from the Fighter class.
    It defines attributes and methods for a Militia fighter type.
    """

    def __init__(self):
        """
        Initializes a Militia AI fighter instance with default attributes.
        """
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
        """
        Selects a random attack from available attacks and returns its damage value.
        """
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