from fighter import Fighter
class Player(Fighter):
    def __init__(self):
        self.health=25
        self.crit_damage=10
        self.crit_chance=20
        self.block_chance=20
        self.dodge_chance=10
        self.dodge_attack=5
        self.name=''