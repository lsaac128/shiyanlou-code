'''本挑战可以分解为四步

1、处理命令行参数
2、处理配置文件和员工数据文件
3、计算
4、将计算结果写入文件
'''

import sys
import json
import csv


class Args:
    '''处理命令行参数
    '''
    def __init__(self):
        self.c = sys.argv[sys.argv.index('-c')+1]
        self.d = sys.argv[sys.argv.index('-d')+1]
        self.o = sys.argv[sys.argv.index('-o')+1]


args = Args()
print('c:', args.c)
print('d:', args.d)
print('o:', args.o)


'''
#user_csv = sys.argv[4]
#test_cfg = sys.argv[2]
user_csv = '/home/shiyanlou/user.csv'
user_list = []
with open(user_csv, 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        user_list.append(line)
user_dict = tuple(user_list)
# class Config:
#     def __init__(self,configfile):
       # self._config = {}
#        pass
#
#    def get_config(self):
#        pass
#
#
#class UserData:
#    def __init__(self, userdatafile):
#        #self.userdata = {}
#        pass

#   def calculator(self):
#        pass

#    def dumptofile(self):
#        pass
'''
