import enemy
def generate(n):
    哥布林 = []
    史萊姆 = []
    怪物 = []
    魔王 = []
    for i in range(1,n+1):     
        史萊姆.append(enemy.enemy('史萊姆','無',i))
        史萊姆.append(enemy.enemy('史萊姆','無',i)) 
        哥布林.append(enemy.enemy('哥布林','男',i))
        哥布林.append(enemy.enemy('哥布林','男',i))
    魔王.append(enemy.devil('L王','男',10))
    魔王.append(enemy.devil('O王','男',20))
    魔王.append(enemy.devil('S王','男',30))
    魔王.append(enemy.devil('E王','男',40))
    魔王.append(enemy.devil('R王','男',50))
    魔王.append(enemy.devil('LOSER王','男',60))
    en = [史萊姆,哥布林,魔王]
    return en
        