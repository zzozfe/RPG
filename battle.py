import createrole as cr
import random
import numpy as np 
import math
import enemy
import option
class battle(cr.newrole):
    def fight(self,that):
        probofc_1 = np.random.choice([1,2,3],size = 100, p =[self.critical,that.critical,1-self.critical-that.critical])
        probofc_2 = random.randint(0,99)
        probofc = probofc_1[probofc_2]
        probofav_1 = np.random.choice([1,2,3],size = 100, p =[self.avoid,that.avoid,1-self.avoid-that.avoid])
        probofav_2 = random.randint(0,99)
        probofav = probofav_1[probofav_2]
        while self.hp > 0 and that.hp > 0:
            probofc_2 = random.randint(0,99)
            probofc = probofc_1[probofc_2]
            probofav_2 = random.randint(0,99)
            probofav = probofav_1[probofav_2]
            tmp = 1
            print(f'====================       ====================')
            print(f'{self.name:23s}    {that.name:23s}')
            print(f'HP/mHP:  {self.hp}/{self.mhp}       HP/mHP:  {that.hp}/{that.mhp}')
            print(f'MP/mMP:  {self.mp}/{self.mmp}       MP/mMP:  {that.mp}/{that.mmp}')
            print('------------------------------------------------')
            print('1: Attack')
            print('2: Skill')
            print('3: Item')
            print('4: Escape')
            print('================================================')        
            if self.agi < that.agi:
                hploss1 = that.attack - self.defence                                              #敵人行動
                if hploss1 < 0:
                    hploss1 = 0
                hploss1 = round(hploss1)
                if probofav != 1 :
                    if probofc == 2:
                        hploss1 *= 2
                        print(f' 爆擊!! {that.name} attacks {self.name} with {hploss1} HP')
                    else:
                        print(f'{that.name} attacks {self.name} with {hploss1} HP')
                else:
                    print('敵人向你攻擊 你成功迴避!! 敵人未命中!!')
                    hploss1 = 0
                self.hp -= hploss1
                if self.hp <= 0:
                    print('you died!')
                    break
                ##########################################################################
                while tmp != 0:
                    o = input('Battle Option : ')
                    if o == '1':
                        hploss2 = self.attack - that.defence                                         #我方行動
                        if hploss2 < 0:
                            hploss2 = 0
                        hploss2 = round(hploss2)
                        if probofav != 2:
                            if probofc == 1:
                                hploss2 *= 2
                                print(f' 爆擊!! {self.name} attacks {that.name} with {hploss2} HP')
                            else:
                                print(f'{self.name} attacks {that.name} with {hploss2} HP')
                        else:
                            print('你向敵人攻擊 敵人成功迴避!! 你未命中!!')
                            hploss2 = 0
                        that.hp -= hploss2
                        tmp = 0
                    elif o == '2':                                                                      #技能
                        if self.skill == '':
                            print('尚未學會技能')
                        else:
                            print('技能列表 : ')
                            for i in range(0,self.lv//5):
                                print(f'{i+1}: {self.skillbase[i]}')
                            oskill = input('Select Skill : ')
                            oskill = int(oskill)
                            if oskill > self.lv//5 or oskill < 1 :
                                print('無效的要求 請重新輸入')
                                break
                            mploss = int(self.skillmp[oskill-1])      
                            if self.mp - mploss < 0:
                                print('魔力不足')
                                break
                            else:    
                                hploss = float(self.skillpower[oskill-1]) - that.defence
                                hploss = round(hploss)
                                if hploss < 0:
                                    hploss = 0 
                                that.hp -= hploss
                                self.mp -= mploss
                                print(f'{self.name} 使用{self.skillbase[oskill-1]}攻擊{that.name},造成{hploss}點傷害')
                            tmp = 0
                        
                    elif o == '3':                                                                      #道具
                        di = option.itemact()
                        if di == '1':
                            cr.newrole.updatehp(TheRole,0,optoin.Health_potion.amount)
                        elif di == '2':
                            cr.newrole.updatemp(TheRole,0,option.Mana_potion.amount)
                        elif di == '0':
                            print('道具已耗盡')
                        elif di == 'q' or 'Q':
                            break
                        else:
                            print('無此道具')
                        tmp = 0
                        
                    elif o == '4':                                                                      #逃跑
                        print('逃跑成功!')                        
                        tmp = 0
                        
                    else:
                        print('無效的要求 請重新輸入')
                        tmp = 1
                if o == 'Q' or o == 'q':
                    continue        
                if o == '4':
                    break
                if that.hp <= 0 :
                    enemy.enemy.drop(that)
                    print('enemy died!')
                    print(f'掉落物品 : {that.drop}')
                    if that.drop == 'Health_potion':
                        option.Health_potion.num += 1
                    elif that.drop == 'Mana_potion':
                        option.Mana_potion.num += 1    
                    print(f'獲得經驗值 : {that.exp}')
                    cr.newrole.lvup(self,that)
                    break
               ###################################################################################################                    
            else:                                                                                                       #我方行動
                while tmp != 0:
                    o = input('Battle Option : ')      
                    if o == '1':                                                                        #攻擊
                        hploss2 = self.attack - that.defence 
                        if hploss2 < 0:
                            hploss2 = 0
                        hploss2 = round(hploss2)
                        if probofav != 2:
                            if probofc == 1:
                                hploss2 *= 2
                                print(f' 爆擊!! {self.name} attacks {that.name} with {hploss2} HP')
                            else:
                                print(f'{self.name} attacks {that.name} with {hploss2} HP')
                        else:
                            print('你向敵人攻擊 敵人成功迴避!! 你未命中!!')
                            hploss2 = 0
                        that.hp -= hploss2
                        tmp = 0
                    elif o == '2':                                                                      #技能
                        if self.skill == '':
                            print('尚未學習技能')
                            continue
                        else:    
                            print('技能列表 : ')
                            for i in range(0,self.lv//5):
                                print(f'{i+1}: {self.skillbase[i]}')
                            oskill = input('Select Skill : ')
                            oskill = int(oskill)
                            if oskill > self.lv//5 or oskill < 1 :
                                print('無效的要求 請重新輸入')
                                break
                            mploss = int(self.skillmp[oskill-1])      
                            if self.mp - mploss < 0:
                                print('魔力不足')
                                break
                            else:    
                                hploss = float(self.skillpower[oskill-1]) - that.defence
                                hploss = round(hploss)
                                if hploss < 0:
                                    hploss = 0    
                                that.hp -= hploss
                                self.mp -= mploss
                                print(f'{self.name} 使用{self.skillbase[oskill-1]}攻擊{that.name},造成{hploss}點傷害')
                            tmp = 0

                    elif o == '3':                                                                      #道具
                        di = option.itemact()
                        if di == '1':
                            cr.newrole.updatehp(self,0,option.Health_potion.amount)
                        elif di == '2':
                            cr.newrole.updatemp(self,0,option.Mana_potion.amount)
                        elif di == '0':
                            print('道具已耗盡')   
                        elif di == 'q' or 'Q':
                            o = di
                            break
                        else:
                            print('無此道具')
                            tmp = 0
                        
                    elif o == '4':                                                                 #逃跑
                        print('逃跑成功')
                        tmp = 0
                        break
                    else:
                        print('無效的要求 請重新輸入')
                        tmp = 1
                if o == 'Q' or o == 'q':
                    continue
                if o =='4' :
                    break    
                if that.hp <= 0:
                    enemy.enemy.drop(that)
                    print('enemy died!')
                    print(f'掉落物品 : {that.drop}')
                    if that.drop == 'Health_potion':
                        option.Health_potion.num += 1
                    elif that.drop == 'Mana_potion':
                        option.Mana_potion.num += 1 
                    print(f'獲得經驗值 : {that.exp}')
                    cr.newrole.lvup(self,that)
                    break
                ############################################################################
                hploss1 = that.attack - self.defence                                              #敵人行動
                if hploss1 < 0:
                    hploss1 = 0
                hploss1 = round(hploss1)
                if probofav != 1 :
                    if probofc == 2:
                        hploss1 *= 2                           
                        print(f' 爆擊!! {that.name} attacks {self.name} with {hploss1} HP')
                    else:
                        print(f'{that.name} attacks {self.name} with {hploss1} HP')
                else:
                    print('敵人向你攻擊 你成功迴避!! 敵人未命中!!')
                    hploss1 = 0
                self.hp -= hploss1   
                if self.hp <= 0:
                    print('you died!')
                    break  
        return self