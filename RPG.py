import stage              #地圖
import createrole as cr   #角色
import option             #互動
import items              #道具
import battle             #戰鬥
import enemygenerate as eg#怪物生成
import save               #存檔
import load               #讀檔
import random
import os

#開始畫面
print('==============================')
print('          RPG GAME')
print('開始你的冒險ㄅ')
print('------------------------------')
print('1: New Game')
print('2: Load Game')
print('------------------------------')
print('==============================')

#創建腳色
tmp = 1
TheMap = stage.newmap('Black Island',60)
while tmp != 0:
    o = input('Option : ')
    if o == '1':                                 #新檔
        name = input('請輸入姓名')
        sex = input('請輸入性別')
        os.system('cls')
        TheRole = cr.newrole(name,sex)
        move = 0
        tmp = 0
        cr.newrole.skill(TheRole)
    elif o == '2':                               #讀檔
        sname = input('請輸入存檔名稱 : ')   
        TheRole = cr.newrole('1','2')
        move = load.load.load(TheRole,sname)
        TheMap.dmap[0] = '_'
        TheMap.dmap[move] = '*'
        tmp = 0
    else:
        print('無效的要求 請重新輸入')
        
#怪物生成
怪物 = eg.generate(100)
enemyprob_1 = [1,2]
enemyprob_2 = random.randint(0,1)
enemyprob = enemyprob_1[enemyprob_2]

#遊戲開始
while TheRole.hp > 0:
    怪物 = eg.generate(100)
    probofe_1 = [1,1,1,3,3]
    probofe_2 = random.randint(0,4)
    probofe = (probofe_1[probofe_2] == 1)
    print(TheMap,end = '')
    print(f'  ({move+1}/60)')
    de = option.option()
    if type(de) == int:                             #移動
        move += de
        if move < 0:
            move = 0
            print('無法後退')
        else:    
            TheMap.dmap[move] = '*'
            TheMap.dmap[move-de] = '_'
            if probofe == True or (move+1)%10 == 0:
                if (move+1)%10 == 0:
                    TheEnemy = 怪物[2][((move+1)//10)-1]
                    print(TheMap,end = '')
                    print(f'  ({move+1}/60)')
                    TheRole = battle.battle.fight(TheRole,TheEnemy)
                else:
                    if enemyprob == 1:
                        TheEnemy = 怪物[0][move]
                        print(TheMap,end = '')
                        print(f'  ({move+1}/60)')
                        TheRole = battle.battle.fight(TheRole,TheEnemy)
                    else:
                        TheEnemy = 怪物[1][move]
                        print(TheMap,end = '')
                        print(f'  ({move+1}/60)')
                        TheRole = battle.battle.fight(TheRole,TheEnemy)
          
    elif de == 'item':                               #使用物品
        di = option.itemact()
        if di == '1':
            cr.newrole.updatehp(TheRole,0,option.Health_potion.amount)
        elif di == '2':
            cr.newrole.updatemp(TheRole,0,option.Mana_potion.amount)
        elif di == '0':
            print('道具已耗盡')
        elif di =='q' or 'Q':
            continue
        else:
            print('無此道具')
    elif de == 'state':                              #查詢狀態
        print(TheRole)
    elif de == 'save':
        save.save.save(TheRole,move)
    elif de == 'quit': 
        pass