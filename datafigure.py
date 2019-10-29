import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def data_plot():
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    df = pd.read_json('/home/shiyanlou/Code/user_study.json')
    df1 = df[['user_id', 'minutes']].groupby('user_id').sum()

    ax.set_title('StudyData')
    ax.set_xlabel('User ID')
    ax.set_ylabel('Study Time')
    ax.plot(df1)
    #plt.savefig('/home/shiyankou/df1.jpg')
    #img = ply.imread('/home/shiyanlou/df1.jpg')
    #plt.imshow(img)
    fig.show()
    fig.canvas.start_event_loop(10)
    return ax


if __name__ == '__main__':
    data_plot()
