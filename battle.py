import random
# import fighter_classes 
# from player import Player
class Battle:
    def __init__(self,player,AI) -> None:
        self.player=player
        self.warrior=AI
        self.player_state=''
        pass
    def attack(self,attacks):
        fight_is_over=False
        list_of_attacks=attacks.keys()
        warrior_health=self.warrior.health
        while fight_is_over==False:
            warrior=self.warrior.normal_attack
            player_attack=input(f'choose attack option: {attacks}')
            num=random.randrange(100)
            num2=random.randrange(100)
            for item in list_of_attacks:
                if item==player_attack:
                    if self.player.crit(num)==True:
                        warrior_health=warrior_health-attacks[item]-self.player.crit_damage
                        print('crit')
                    elif self.player.attack(num)==True:
                        warrior_health=warrior_health-attacks[item]
                    elif self.player.block(num)==True:
                        print('got blocked')
                    elif self.player.attack_dodge(num)==True:
                        warrior_health=warrior_health-attacks[item]
                        print('dodged and returned attack!')
                    print(f'ugly health:{warrior_health}')
                    if warrior_health>0:               
                        if self.warrior.crit(num2)==True:
                            self.player.health=self.player.health-warrior-self.warrior.crit_damage
                            print('took a crit')
                        elif self.warrior.attack(num2)==True:
                            self.player.health=self.player.health-warrior
                        elif self.warrior.block(num2)==True:
                            print('blocked')
                        elif self.warrior.attack_dodge(num2)==True:
                            self.player.health=self.player.health-warrior
                            print('you missed and took a hit')
                    print(f'my health: {self.player.health}')          
                    
                    if self.player.health<1:
                        # need to send the results to the story line and have it continue on from there
                        #this is just a battle ground class not a storyline class
                        print("I saw it coming but I was helpless to stop it. And so I watched on in horror as the creature's claws tore into my chest, \nspilling the last of my life blood out onto the cold unforgiving floor. \nAnd thus my story ends, for I do not wish to speak of the horror that I have become.")
                        fight_is_over=True
                        self.player_state='dead'
                    elif warrior_health<1:
                        self.player.name=input('What is your name? ')
                        print(f"At last there it was! An opening in uglie's gaurd. Without any hesitaion I plunged that dagger into it's throat, \nand watched on as life left it's eyes. After the thrill of the fight left me, \nI stood there for who knows how long, looking down upon the pool of blood that had gathered at my feet, \nwith only one thing in my mind; a thought that still haunts me to this day, \n'What have I become; what will I become!'. For I had enjoyed it.\nI am {self.player.name} and this is my Tale of the Dark Days.\nAm I Infamous or Legendary maybe both or just another casulty, who knows?\n but come back to the tale I digress. ")
                        fight_is_over=True
                        self.player_state='alive'
