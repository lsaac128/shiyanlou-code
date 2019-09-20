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

    def jisuan(self, kw):
        for line in kw:
            gz = int(kw[line])
            sb = format(gz * 0.165,'.2f')
            sb1 = float(format(gz * 0.165,'.2f'))
            yjssde = gz - sb1  - 5000
            ns = float(format(yjssde*0.03,'.2f'))
            shgz = float(format(gz - sb1 - ns,'.2f'))

            print('{},{},{},{},{}'.format(line,kw[line],sb,ns,shgz))

age = UserData()
zidian = age.huoqu()
age.jisuan(zidian)
