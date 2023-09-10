from fighter import Fighter
class Undead_Player(Fighter):
    """
    This class represents an Undead player character in your game.
    It inherits from the Fighter class and defines attributes and abilities specific to the Undead player.

    Attributes:
    - attacks (dict): A dictionary of available attack moves with corresponding damage values.
    - health (int): The current health points of the Undead player.
    - crit_damage (int): The bonus damage dealt on critical hits.
    - crit_chance (int): The chance of landing a critical hit, represented as a percentage (%).
    - block_chance (int): The chance of successfully blocking an incoming attack, represented as a percentage (%).
    - dodge_chance (int): The chance of successfully dodging an attack, represented as a percentage (%).
    - dodge_attack (int): The minimum value required for a successful dodge.
    - will_power (int): A special attribute representing the Undead player's unique willpower.
    - name (str): The name of the Undead player (if applicable).
    """

    def __init__(self):
        """
        Initializes an Undead player character with default attributes and abilities.
        """
        self.attacks = {'slash': 15, 'bit': 5, 'Fiendish assalt': 20, 'stab': 10}
        self.health = 25
        self.crit_damage = 10
        self.crit_chance = 20
        self.block_chance = 20
        self.dodge_chance = 10
        self.dodge_attack = 5
        self.will_power = 1
        self.name = ''