import random
#Here I am going to be storing the templates for different AI fighter classes
class Worrior:
    def __init__(self,level):
        self.health=40*level
        self.crit_chance=5
        self.block_chance=10
        self.dodge_chance=10
        self.dodge_attack=5
        self.norm_attack=random.randrange(20)
    def attack(self,num):
        norm=False
        starting_num=self.dodge_attack+self.dodge_chance+self.block_chance
        ending_num=101-self.crit_chance
        if starting_num<num and num<ending_num:
            norm=True
            return norm
        return norm
    def crit(self,num):
        crit_hit=False
        self.crit_chance=100-self.crit_chance
        if num>self.crit_chance:
            crit_hit=True
            return crit_hit
        return crit_hit
    def block(self,num):
        block=False
        starting_num=self.dodge_attack+self.dodge_chance
        ending_num=starting_num+self.block_chance+1
        if starting_num<num and num<ending_num:
            block=True
            return block
        return block
    def dodge(self,num):
        dodge=False
        starting_num=self.dodge_attack
        ending_num=starting_num+self.dodge_chance+1
        if starting_num<num and num<ending_num:
            dodge=True
            return dodge
        return dodge
    def attack_dodge(self,num):
        attack=False
        if num<self.dodge_attack+1:
            attack=True
            return attack
        return attack