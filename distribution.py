#distribution.py
#Displays a density graph of the interval distribution.
#A lognorm distribution is an approximation, so the user should be able to see what the data really looks like.

import matplotlib.pyplot as plt
import seaborn as sns


def make_kde(data_pts: list) -> 'plot':
    '''Displays the graph using seaborn and matplotlib'''
    sns.kdeplot(data = data_pts, fill = True, color = 'blue')
    plt.show()



