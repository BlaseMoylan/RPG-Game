import random
import chapter1
import fighter_classes 
from player import Player
from battle import Battle
#next step is to 
class Game:
    def __init__(self):
        self.player=Player()
        self.warrior=fighter_classes.Warrior()
        self.battle=Battle(self.player,self.warrior)
        pass
    def run_Game(self):
        self.story()
    def story(self):
        print("It was a dark day that saw Our Great kingdom brought to it's knees. Nature itself was revolting, \ncreatures out of nightmares began to appear upon our sacred land. \nI remember that day well, though thoughts of our great kingdom's demise never once crossed my mind. \nFor me The Fall all began one early summer morning, the sun was just cresting the nearby hills \nwhen I woke to find a dagger attached to an ugly green arm, desending down upon me. \n(I must say this, impending death does wonders to get you out of bed in the morning). \nI quickly twisted the dagger out of the ugly arm's grip, and the fight of my life began... ")
        self.battle.attack(self.player.attacks)
        valid_input=False
        count=1
        while valid_input==False:
            if self.battle.player_state=='dead':
                user_input=input('Do you wish to continue?(yes/no)')
                if user_input=='yes':
                    # chapter1 :undead class call
                    chapter1.Undead()
                    valid_input=True
                elif user_input=='no':
                    valid_input=True
                else:
                    if count==3:
                        print('Actions Have Consequences! \n You did not enter one of the options for the 3rd time!\nYour progress is being erased...\nGame shutting down...\nGoodbye!')
                        valid_input=True
                    else:
                        count+=1
                        print('this is not one of the options')


            elif self.battle.player_state=='alive':
                user_input=input('Do you wish to continue?(yes/no)')
                if user_input=='yes':
                    # chapter1 :Begginings class call
                    valid_input=True
                elif user_input=='no':
                    valid_input=True
                else:
                    if count==3:
                        print('Actions Have Consequences! \n You did not enter one of the options for the 3rd time!\nYour progress is being erased...\nGame shutting down...\nGoodbye!')
                        valid_input=True
                    else:
                        count+=1
                        print('this is not one of the options')


