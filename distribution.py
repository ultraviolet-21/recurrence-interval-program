#distribution.py

import matplotlib.pyplot as plt
import seaborn as sns
import random

data_pts = list(random.choices(range(100), k=30))

def make_kde(data_pts: list) -> 'plot':
    sns.kdeplot(data = data_pts, fill = True, color = 'blue')
    plt.show()


if __name__ == '__main__':
    make_kde(data_pts)

#use this for probability:
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.lognorm.html
