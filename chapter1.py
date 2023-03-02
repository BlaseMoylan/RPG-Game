#for the undead class I will need to make a undead player instance.
#also need a militia class added to the AI fighter_classes 
from battle import Battle
from player_undead import Undead_Player
import fighter_classes
class Undead:
    def __init__(self) -> None:
        self.undead=Undead_Player()
        self.militia=fighter_classes.Militia()
        self.battle=Battle(self.undead,self.militia)
        self.chapter1()
    def chapter1(self):
        print('I awoke; or more acuratly, the thing that I had become awoke. An overwhelming need filled me and overcame what little of my soul was left in to animate this rotting corpse; A need to kill A need to serve!\nI stumbled to my feet a foreign will driving me on. I was on the outskirts of a forest, sometime deep into the night. A small peacefull village lay a few stone throws away, lay like a scene out of a fairy tale, spread out under the stary night sky. \nTwo words boomed like cannos in my mind: \nGo!\nKill\n And to my eternal shame I bounded foward, like a dog after a bone. And soon came across the first terrified villeger... ')
        self.battle.attack(self.undead.attacks)









class Begginings:
    pass