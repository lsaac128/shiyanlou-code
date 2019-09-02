#!/usr/bin/env python3
basic_salary = 1500
bonus_rate = 200
commission_rate = 0.02
numberofcamera = int(input('请输入数量：'))
price = float(input('请输入单价：'))
bonus = (bonus_rate * numberofcamera)
commission = (commission_rate * price * numberofcamera)
print('Bonus = {:6.2f}'.format(bonus))
print('Commission = {:6.2f}'.format(commission))
print('Gross salary = {:6.2f}'.format(basic_salary + bonus + commission))
