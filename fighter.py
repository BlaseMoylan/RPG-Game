class Fighter:
    def __init__(self):
        # self.health=0
        # self.crit_damage=0
        # self.crit_chance=0
        # self.block_chance=0
        # self.dodge_chance=0
        # self.dodge_attack=0
        # self.name=''
        pass
    def attack(self,num):
        norm=False
        starting_num=self.dodge_attack+self.dodge_chance+self.block_chance
        ending_num=100-self.crit_chance
        if starting_num<num and num<ending_num:
            norm=True
            return norm
        return norm
    def crit(self,num):
        crit_hit=False
        crit_chance=100-self.crit_chance
        if num>crit_chance:
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
    