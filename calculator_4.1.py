#!/usr/bin/env python3

import sys
import csv

class Args:
    def __init__(self):
        self.c = sys.argv[sys.argv.index('-c')+1]
        self.d = sys.argv[sys.argv.index('-d')+1]
#        self.o = sys.argv[sys.argv.index('-o')+1]


class UserData(Args):
    def huoqu(self):
        with open(self.c) as f:
           data = dict(list(csv.reader(f)))
        return data

    def test(self):
        l = []
        with open(self.d) as f:
            for line in f:
                name, rate = line.split(' = ')
                l.append((name, float(rate)))
        return dict(l)

    def jisuan(self, kw):
        sbbl = self.test()['YangLao'] + self.test()['YiLiao'] + \
                self.test()['GongShang'] + self.test()['ShengYu'] + \
                self.test()['GongJiJin'] + self.test()['ShiYe']
        for line in kw:
            gz = int(kw[line])
            sb = format(gz * sbbl,'.2f')
            sb1 = float(sb)
            ns = format(0, '.2f')
            ns1 = float(ns)
            yjssde = float(gz - sb1 - 5000)
            if gz <= 5000:
                yjssde = 0
                shgz = format(gz - sb1,'.2f')
            if gz < self.test()['JiShuL']:
                yjssde = 0
                sb = format(self.test()['JiShuL'] * sbbl, '.2f' )
                sb1 = float(sb)
                shgz = format(gz - sb1, '.2f')
            if gz > self.test()['JiShuH']:
                sb = format(self.test()['JiShuH'] * sbbl, '.2f')
                sb1 = float(sb)
            if yjssde <= 3000:
                ns = format(yjssde*0.03,'.2f')
                ns1 = float(ns)
                shgz = format(gz - sb1 -ns1,'.2f')
            elif 3000< yjssde <= 12000:
                ns = format(yjssde*0.1 - 210 ,'.2f')
                ns1 = float(ns)
                shgz = format(gz - sb1 - ns1,'.2f')
            elif 12000 < yjssde <= 25000:
                ns = format(yjssde*0.2 - 1410,'.2f')
                ns1 = float(ns)
                shgz = format(gz - sb1 -ns1,'.2f')
            elif 25000 < yjssde <= 35000:
                ns = format(yjssde*0.25 - 2660,'.2f')
                ns1 = float(ns)
                shgz = format(gz - sb1 - ns1,'.2f')
            elif 35000 < yjssde <= 55000:
                ns = format(yjssde*0.3 - 4410,'.2f')
                ns1 = float(ns)
                shgz = format(gz - sb1 - ns1,'.2f')
            elif 55000 < yjssde <= 80000:
                ns = format(yjssde*0.35 - 7160,'.2f')
                ns1 = float(ns)
                shgz = format(gz - sb1 - ns1,'.2f')
            elif yjssde > 80000:
                ns = format(yjssde*0.45 - 15160,'.2f')
                ns1 = float(ns)
                shgz = format(gz - sb1 - ns1,'.2f')

#            yjssde = gz - sb1  - 5000
#            ns = float(format(yjssde*0.03,'.2f'))
#            shgz = float(format(gz - sb1 - ns,'.2f'))
            print('{},{},{},{},{}'.format(line,kw[line],sb,ns,shgz))

age = UserData()
zidian = age.huoqu()
peizhi = age.test()
age.jisuan(zidian)
