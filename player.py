from fighter import Fighter
class Player(Fighter):
    """
    This class represents a player character in your game.
    It inherits from the Fighter class and defines attributes and abilities specific to the player character.

    Attributes:
    - attacks (dict): A dictionary of available attack moves with corresponding damage values.
    - health (int): The current health points of the player character.
    - crit_damage (int): The bonus damage dealt on critical hits.
    - crit_chance (int): The chance of landing a critical hit, represented as a percentage (%).
    - block_chance (int): The chance of successfully blocking an incoming attack, represented as a percentage (%).
    - dodge_chance (int): The chance of successfully dodging an attack, represented as a percentage (%).
    - dodge_attack (int): The minimum value required for a successful dodge.
    - name (str): The name of the player character (if applicable).
    """

    def __init__(self):
        """
        Initializes a player character with default attributes and abilities.
        """
        self.attacks = {'slash': 10, 'stab': 15, 'punch': 3, 'kick': 5}
        self.health = 25
        self.crit_damage = 10
        self.crit_chance = 20
        self.block_chance = 20
        self.dodge_chance = 10
        self.dodge_attack = 5
        self.name = ''  # Placeholder for the player character's name