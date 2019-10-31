# -*- coding:utf-8 -*-

import pandas as pd


def quarter_volume():
    data = pd.read_csv('apple.csv', header=0)
    df = pd.Series(data.Volume.values, index=pd.to_datetime(data.Date))
    df1 = df.resample('q').sum()
    df1 = pd.DataFrame(df1,columns=['V'])
    second_volume = df1.sort_values('V', ascending=False).V[1]
    


    return second_volume


if __name__ == '__main__':
    print(quarter_volume())
