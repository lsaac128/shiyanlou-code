import sys
import csv

class Args:
    def __init__(self):
        self.c = sys.argv[sys.argv.index('-c')+1]
#        self.d = sys.argv[sys.argv.index('-d')+1]
#        self.o = sys.argv[sys.argv.index('-o')+1]

class UserData(Args):
    def huoqu(self):
        with open(self.c) as f:
           data = dict(list(csv.reader(f)))
        return data

    def jisuan(self):
        for line in self.huoqu():
            gz = int(self.huoqu()[line])
            yjssde = gz -gz*0.165 - 5000
            ns = yjssde*0.03
            print('ID:{},gz:{}, ns:{}'.format(line,self.huoqu()[line],ns))


age = UserData()
age.jisuan()
