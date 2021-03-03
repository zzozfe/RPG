class item:
    def __init__(self,name,num,amount):
        self.name = name
        self.num = num
        self.amount = amount
    def __str__(self):
        name = self.name
        num = self.num
        amount = self.amount
        return f'item : {name}'
    def __repr__(self):
        return self.__str__()