from fighter import Fighter
class Undead_Player(Fighter):
    def __init__(self) -> None:
        self.attacks={'slash':15,'bit':5,'Fiendish assalt':20,'stab':10}
        self.health=25
        self.crit_damage=10
        self.crit_chance=20
        self.block_chance=20
        self.dodge_chance=10
        self.dodge_attack=5
        self.will_power=1
        self.name=''