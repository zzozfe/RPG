import createrole as cr
import csv
import option
import stage
class save(cr.newrole,stage.newmap):
    def save(self,situa):
        savename = input('請輸入存檔名稱 : ')
        savename += '.csv'
        with open(f'{savename}','w',newline = '\n',encoding = 'UTF-8') as s1:
            roledata = [[situa],[self.name],[self.career],[self.sex],[self.mhp],[self.hp],[self.mmp],[self.mp],[self.lv],[self.exp],[self.str],[self.int],[self.vit],[self.dex],[self.luk],[self.agi],[self.skill],self.skillbase,self.skillmp,self.skillpower,[option.Health_potion.name],[option.Health_potion.num],[option.Health_potion.amount],[option.Mana_potion.name],[option.Mana_potion.num],[option.Mana_potion.amount]]
            csv.writer(s1).writerows(roledata)