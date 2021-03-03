import random
import math
import pandas as pd
class newrole:
    def __init__(self,name,sex):
        self.name = name
        self.career = 'Rookie'
        self.sex = sex
        self.mhp = random.randint(25,30)
        self.mmp = random.randint(5,10)
        self.hp = self.mhp
        self.mp = self.mmp
        self.lv = 1
        self.exp = 0
        self.str = 5
        self.int = 5
        self.vit = 5
        self.agi = 5
        self.luk = 5
        self.dex = 5
        self.attack = 1.5*self.str + self.dex/3 +self.agi/5 + random.uniform(0.2*math.sqrt(self.str),0.5*math.sqrt(self.str))
        self.defence = self.vit/2 + self.agi/3 + self.dex/5
        self.critical = (self.dex*0.5+self.luk*0.5)/(10*(self.dex+self.luk))
        self.avoid = (self.agi*1.5+self.luk*0.5)/(10*(self.agi+self.luk))
        self.skill = ''
        self.skillbase = []
        self.skillpower = []
        self.skillmp = []
        level = []
        for i in range(2,101):
            level.append(10+i**2*5*i)
        self.mexp = level
    def updatehp(self,maxornot,n):                #血量提升
        if maxornot == 1:
            self.mhp += n
        else:    
            if self.hp + n < self.mhp:
                self.hp += n
            else:
                self.hp = self.mhp
    def updatemp(self,maxornot,n):                #魔力提升
        if maxornot == 1:
            self.mmp += n
        else:    
            if self.mp + n < self.mmp:            
                self.mp += n 
            else:
                self.mp = self.mmp
    def skill(self):
        self.skillbase = ['二連擊','旋風斬','致命一擊','二連擊EX','旋風斬EX','致命一擊EX']
        self.skillmp = []
        self.skillpower = []
        for i in range(0,len(self.skillbase)):
            self.skillpower.append(self.attack*(i+2)+math.ceil(math.sqrt(10*(i+1))))
            self.skillmp.append(10*(i+1))
        return self.skillbase
    def lvup(self,that):                             #升級
        level = []
        for i in range(2,101):
            level.append(10+i**2*5*i)
        self.exp += that.exp
        while self.exp >= level[self.lv-1]:
            self.lv += 1
            lv = self.lv            
            self.mhp += math.ceil(self.vit/2) + random.randint(1,3)
            self.hp = self.mhp
            self.mmp += math.ceil(self.int/4) + random.randint(1,2)
            self.mp = self.mmp
            print(f'升到{lv}級了!獲得5點能力點!')
            if self.lv % 5 == 0:
                tmp = self.lv//5
                print(f'恭喜! 學會新技能{newrole.skill(self)[tmp-1]}')
                self.skill +=  newrole.skill(self)[tmp-1]
            point = 5
            while point != 0:
                print(f'請分配能力點 : 尚有{point}點')
                print(f'1 Str : {self.str}')
                print(f'2 Int : {self.int}')
                print(f'3 Vit : {self.vit}')
                print(f'4 Agi : {self.agi}')
                print(f'5 Luk : {self.luk}')
                print(f'6 Dex : {self.dex}')
                o = input('Option : ')
                if o == '1':
                    self.str += 1
                elif o == '2':
                    self.int += 1
                elif o == '3':    
                    self.vit += 1
                elif o == '4':    
                    self.agi += 1
                elif o == '5':
                    self.luk += 1
                elif o == '6':
                    self.dex += 1
                else:
                    print('無效的要求 請重新輸入!')
                    point += 1
                point -= 1    
                print('------------------------------')
        self.attack = 1.5*self.str + self.dex/3 +self.agi/5 + random.uniform(0.2*math.sqrt(self.str),0.5*math.sqrt(self.str))
        self.defence = self.vit/2 + self.agi/3 + self.dex/5
        self.critical = (self.dex*0.5+self.luk*0.5)/(10*(self.dex+self.luk))
        self.avoid = (self.agi*1.5+self.luk*0.5)/(10*(self.agi+self.luk))  
    def __str__(self):
        name = self.name
        career = self.career
        sex = self.sex
        mhp = self.mhp
        mmp = self.mmp
        hp = self.hp
        mp = self.mp
        LV = self.lv
        Exp = self.exp
        Str = self.str
        Int = self.int
        Vit = self.vit
        Agi = self.agi
        Luk = self.luk
        Dex = self.dex
        mexp = self.mexp[LV-1]
        Skill = self.skill
        return f'Lv : {LV}\nExp/mExp : {Exp}/{mexp}\n---------------\nName : {name}\nSex : {sex}\nCareer : {career}\nHp/mHP : {hp}/{mhp}\nMp/mMp : {mp}/{mmp}\nStr : {Str}\nInt : {Int}\nVit : {Vit}\nAgi : {Agi}\nLuk : {Luk}\nDex : {Dex}\nSkill : {Skill}\n---------------'
    def __repr__(self):
        return self.__str__()
class Sword(newrole):
    def __init__(self,name,sex,hp,mp):
        super().__init__(name,sex,hp,mp)
        self.career = 'Sword'
    def fight(self):
        print('揮劍攻擊')
class Mage(newrole):
    def __init__(self,name,sex,hp,mp):
        super().__init__(name,sex,hp,mp)
        self.career = 'Mage'
    def fight(self):
        print('魔法攻擊')
         

        