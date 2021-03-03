import items
#創建道具
Health_potion = items.item('Health_potion',5,10)
Mana_potion = items.item('Mana_potion',5,3)

#互動
def option():  
    print('==============================')
    print('          Main Menu')
    print('------------------------------')
    print('d/D : Forward')
    print('a/A : Backward')
    print('i/I : Item')
    print('s/S : State')
    print('r/R : Save Game')
    print('q/Q : Quit')
    print('------------------------------')
    option_state = {'d':1,'D':1,'a':-1,'A':-1,'i':'item','I':'item','s':'state','S':'state','r':'save','R':'save','q':'quit','Q':'quit'}
    tmp = 0
    while tmp == 0: 
        o = input('Option : ')
        if option_state.get(o) != None:
            option_self = option_state.get(o)
            tmp = 1
        else:
            print('無效的要求 請重新輸入!')     
    return option_self
def itemact():
    print('請輸入選項來使用道具,離開請輸入 q/Q')
    print('============================')
    print(f'1 {Health_potion.name}   {Health_potion.num}個')
    print(f'2 {Mana_potion.name}     {Mana_potion.num}個') 
    print('----------------------------')
    o = input('Option : ')
    if o == '1':
        Health_potion.num -= 1
        if Health_potion == 0:
            o = '0'
    elif o == '2':
        Mana_potion.num -= 1
        if Mana_potion == 0:
            o = '0'
    elif o == 'q' or 'Q':
        o = o    
    else:
        print('無效的要求 請重新輸入')

    return o
    