import random
import math
class enemy:
    def __init__(self,name,sex,power):
        self.name = name
        self.sex = sex
        self.mhp = random.randint(25*power,30*power)
        self.mmp = random.randint(5*power,20*power)
        self.hp = self.mhp
        self.mp = self.mmp
        self.lv = power
        self.str = 5*math.sqrt(power)-power
        self.vit = 5*math.sqrt(power)-power
        self.agi = 5*math.sqrt(power)-power
        self.luk = 5*math.sqrt(power)-power
        self.dex = 5*math.sqrt(power)-power
        self.attack = self.str + self.dex/3 +self.agi/5
        self.defence = self.vit/2 + self.agi/3 + self.dex/5
        self.critical = (self.dex*0.5+self.luk*0.5)/600
        self.avoid = (self.agi*1.5+self.luk*0.5)/750
        self.skill = ''
        self.drop = ''
        self.exp = 10+6*power**2 + random.randint(power*10,power**2+power*10) 
    def drop(self):
        a = random.randint(1,10)
        if a == 1:
            self.drop = 'Health_potion'
        elif a == 2:
            self.drop = 'Mana_potion'
    def __str__(self):
        name = self.name
        sex = self.sex
        mhp = self.mhp
        mmp = self.mmp
        hp = self.hp
        mp = self.mp
        LV = self.lv
        Str = self.str
        Vit = self.vit
        Agi = self.agi
        Luk = self.luk
        Dex = self.dex
        Skill = self.skill
        return f'Lv : {LV}\n---------------\nName : {name}\nSex : {sex}\nHp/mHP : {hp}/{mhp}\nMp/mMp : {mp}/{mmp}\nStr : {Str}\nVit : {Vit}\nAgi : {Agi}\nLuk : {Luk}\nDex : {Dex}\nSkill : {Skill}\n---------------'
    def __repr__(self):
        return self.__str__()
class devil(enemy):
    def __init__(self,name,sex,power):
        super().__init__(name,sex,power)
        power = power*1.5
        self.lv = power/1.5
        if self.lv == 10:
            self.skill = 'L劍'
        elif self.lv == 20:
            self.skill = 'O劍'
        elif self.lv == 30:
            self.skill = 'S劍'
        elif self.lv == 40:
            self.skill = 'E劍'
        elif self.lv == 50:
            self.skill = 'R劍'
        elif self.lv == 60:
            self.skill = 'LOSER劍'