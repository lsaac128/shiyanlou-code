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
            yjssde = gz -sb1 -5000
            if gz <= 5000:
                ns = format(0,'.2f')
                shgz = format(gz - sb1,'.2f')
            elif yjssde <= 3000:
                ns = format(yjssde*0.03,'.2f')
                ns1 = float(ns)
                shgz = format(gz - sb1 -ns1,'.2f')
            elif yjssde >3000 and yjssde <= 12000:
                ns = format(yjssde*0.1,'.2f')
                ns1 = float(ns)
                shgz = format(gz - sb1 - ns1 - 210,'.2f')
            elif yjssde > 12000 and yjssde <= 25000:
                ns = format(yjssde*0.2,'.2f')
                ns1 = float(ns)
                shgz = format(gz - sb1 -ns1 -1410,'.2f')
            elif yjssde > 25000 and yjssde <= 35000:
                ns = format(yjssde*0.25,'.2f')
                ns1 = float(ns)
                shgz = format(gz - sb1 - ns1 - 2660,'.2f')
            elif yjssde > 35000 and yjssde <= 55000:
                ns = format(yjssde*0.3,'.2f')
                ns1 = float(ns)
                shgz = format(gz - sb1 - ns1 - 4410,'.2f')
            elif yjssde > 55000 and yjssde <= 80000:
                ns = format(yjssde*0.35,'.2f')
                ns1 = float(ns)
                shgz = format(gz - sb1 - ns1 - 7160,'.2f')
            elif yjssde > 80000:
                ns = format(yjssde*0.45,'.2f')
                ns1 = float(ns)
                shgz = format(gz - sb1 - ns1 - 15160,'.2f')
#            yjssde = gz - sb1  - 5000
#            ns = float(format(yjssde*0.03,'.2f'))
#            shgz = float(format(gz - sb1 - ns,'.2f'))

            print('{},{},{},{},{}'.format(line,kw[line],sb,ns,shgz))

age = UserData()
zidian = age.huoqu()
age.jisuan(zidian)
