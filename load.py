import createrole as cr
import csv
import option
import random
import math
class load(cr.newrole):
    def load(self,savename):
        with open(f'{savename}.csv','r',newline = '\n',encoding = 'UTF-8') as s2:
            content = csv.reader(s2)
            roledata = []
            for row in content:
                roledata.append(row)
        move = int(roledata[0][0])
        self.name = roledata[1][0]
        self.career = roledata[2][0]
        self.sex = roledata[3][0]
        self.mhp = int(roledata[4][0])
        self.hp = int(roledata[5][0])
        self.mmp = int(roledata[6][0])
        self.mp = int(roledata[7][0])
        self.lv = int(roledata[8][0])
        self.exp = int(roledata[9][0])
        self.str = int(roledata[10][0])
        self.int = int(roledata[11][0])
        self.vit = int(roledata[12][0])
        self.dex = int(roledata[13][0])
        self.luk = int(roledata[14][0])
        self.agi = int(roledata[15][0])
        self.skill = roledata[16][0]
        self.skillbase = roledata[17]
        self.skillmp = roledata[18]
        self.skillpower = roledata[19]
        option.Health_potion.name = roledata[20][0]
        option.Health_potion.num = int(roledata[21][0])
        option.Health_potion.amount = int(roledata[22][0])
        option.Mana_potion.name = roledata[23][0]
        option.Mana_potion.num = int(roledata[24][0])
        option.Mana_potion.amount = int(roledata[25][0])
        self.attack = 1.5*self.str + self.dex/3 +self.agi/5 + random.uniform(0.2*math.sqrt(self.str),0.5*math.sqrt(self.str))
        self.defence = self.vit/2 + self.agi/3 + self.dex/5
        self.critical = (self.dex*0.5+self.luk*0.5)/(10*(self.dex+self.luk))
        self.avoid = (self.agi*1.5+self.luk*0.5)/(10*(self.agi+self.luk))
        return move            