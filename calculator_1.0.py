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


age = UserData()
age_1 = age.huoqu()
for i in age_1:
    print(i,age_1[i])
