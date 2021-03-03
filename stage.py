import numpy as np
class newmap:
    def __init__(self,name,num):
        self.name = name
        self.num = num
        dmap = np.arange(1,self.num+1,1)
        dmap = list(dmap)
        for i in range(0,60):
            dmap[i] = '_'
        dmap[0] = '*'
        dmap[9] = 'L'
        dmap[19] = 'O'
        dmap[29] = 'S'
        dmap[39] = 'E'
        dmap[49] = 'R'
        dmap[59] = 'LOSER'
        self.dmap = dmap
    def __str__(self):
        name = self.name
        road = ''
        for i in range(0,len(self.dmap)):
            road += self.dmap[i]
        return f'{name}\n{road}'