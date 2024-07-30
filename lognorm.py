#lognorm.py
#Calculates key values and probability assuming a lognormal distribution.

import math
import numpy as np
from scipy.stats import lognorm

def cov(mean: float, stdev: float) -> float:
    '''Returns the coefficient of variation'''
    return stdev / mean

def sigmalnx(cv: float) -> float:
    '''Returns standard deviation value for lognorm'''
    return math.sqrt(math.log(cv ** 2 + 1))

def med(mean: float, sigma: float) -> float:
    '''Returns median for lognorm'''
    temp = (sigma ** 2) / 2
    return mean / (math.e ** temp)


def lognorm_dist(ref_point, point, median, sigma):
    '''Returns lognormal cumulative distribution function (cdf)'''
    interval = point - ref_point
    return lognorm.cdf(interval, s = sigma, scale = median)

def lognorm_diff(start, end):
    '''Returns difference between 2 cdf values adjusted for the start value'''
    return (end - start) / (1-start)

def probability(ref_point, start, end, mean, stdev):
    '''Returns probability'''
    cv = cov(mean, stdev)
    sigma = sigmalnx(cv)
    median = med(mean, sigma)
    start_prob = lognorm_dist(ref_point, start, median, sigma)
    end_prob = lognorm_dist(ref_point, end, median, sigma)
    difference = lognorm_diff(start_prob, end_prob)
    return difference
    
