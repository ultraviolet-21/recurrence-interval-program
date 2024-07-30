#onevar_stats.py
#This contains the mean and standard deviation functions used for calculating the interval distribution.
#The user may also run this file separately.
#The other statistics calculations can be called in the console if the file is run separately.


import statistics as stats
import math

get_range = lambda data: max(data) - min(data)

mean = lambda data: sum(data)/len(data)

def median(data: list[int]) -> float:
    if len(data) % 2 == 1:
        midpoint = (len(data)-1)//2
        return data[midpoint]
    else:
        high = len(data)//2
        low = len(data)//2 - 1
        return (data[high] + data[low])/2

def stdev(data: list[int]) -> float:
    return stats.stdev(data)

def z_score(mean: float, stdev: float, x: float) -> float:
    return (x-mean)/stdev

def percent_error(expected: float, actual: float) -> str:
    return str(math.fabs(expected - actual)/expected) + '%'

