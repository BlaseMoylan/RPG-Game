import random
import chapter1
import fighter_classes 
from player import Player
from battle import Battle
#next step is to 
class Game:
    """
    This class represents the main game engine for your RPG game.
    It manages the player character, storyline progression, battles, and user interactions.

    Attributes:
    - player (Player): The player character in the game.
    - warrior (Warrior): An AI-controlled warrior character.
    - battle (Battle): Manages battles between the player and AI characters.
    """

    def __init__(self):
        """
        Initializes a game instance by creating a player character, an AI warrior, and a battle instance.
        """
        self.player = Player()                # Create a player character instance
        self.warrior = fighter_classes.Warrior()  # Create an AI-controlled warrior instance
        self.battle = Battle(self.player, self.warrior)  # Create a battle instance for player vs. AI combat

    def run_Game(self):
        """
        Initiates the game by starting the story.
        """
        self.story()

    def story(self):
        """
        Presents the storyline and initiates the first battle.
        Manages user interactions and progression based on battle outcomes.

        This method sets the stage for the game, presenting the story and initiating the first battle.
        It handles user input to continue or exit the game, and the consequences of those choices.
        """
        print("It was a dark day that saw Our Great kingdom brought to its knees. Nature itself was revolting, \ncreatures out of nightmares began to appear upon our sacred land. \nI remember that day well, though thoughts of our great kingdom's demise never once crossed my mind. \nFor me, The Fall all began one early summer morning, the sun was just cresting the nearby hills \nwhen I woke to find a dagger attached to an ugly green arm, descending down upon me. \n(I must say this, impending death does wonders to get you out of bed in the morning). \nI quickly twisted the dagger out of the ugly arm's grip, and the fight of my life began... ")
        
        # Initiate the first battle with the player's attack options
        self.battle.attack(self.player.attacks)
        
        valid_input = False  # Flag to validate user input
        count = 1  # Tracks the number of invalid input attempts

        while not valid_input:
            if self.battle.player_state == 'dead':
                user_input = input('Do you wish to continue? (yes/no)')
                if user_input == 'yes':
                    # Call the Undead class for the next chapter
                    chapter1.Undead()
                    valid_input = True
                elif user_input == 'no':
                    valid_input = True
                else:
                    if count == 3:
                        print('Actions Have Consequences! \nYou did not enter one of the options for the 3rd time!\nYour progress is being erased...\nGame shutting down...\nGoodbye!')
                        valid_input = True
                    else:
                        count += 1
                        print('This is not one of the options')

            elif self.battle.player_state == 'alive':
                user_input = input('Do you wish to continue? (yes/no)')
                if user_input == 'yes':
                    # Call the Beginnings class for the next chapter
                    valid_input = True
                elif user_input == 'no':
                    valid_input = True
                else:
                    if count == 3:
                        print('Actions Have Consequences! \nYou did not enter one of the options for the 3rd time!\nYour progress is being erased...\nGame shutting down...\nGoodbye!')
                        valid_input = True
                    else:
                        count += 1
                        print('This is not one of the options')