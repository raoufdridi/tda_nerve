'''
filters (and distances)

Created on Jan 28, 2015

@author: Raouf.
'''
import numpy as np
import pandas
from math import sqrt
from pandas import DataFrame


def euclidean_distance(a,b):  
    res = np.array(a) - np.array(b)
    f = lambda x: x**2
    return sqrt(sum(map(f, res)))

def density(x, X, EPSILON, C, distance = euclidean_distance):
    return C * sum(math.exp(distance(x, y)**2/EPSILON) for y in X)

def eccentricity(x, X, p, distance = euclidean_distance):
    return (sum (distance(x, y)**p for y in X)/len(X))**(1/p)


def apply_filters(filters, data): 
    # return an np.array with same shape as data = columns vectors coords with filters values
    # filters = list/set/tuple of filters or just one filter  
    df = DataFrame(data)
    pieces =[]
    if type(filters) in {set, list, tuple}:
        myfilters = filters
    else:
        myfilters = [[filters][0]]
    for f in myfilters:
        frame = DataFrame(df.apply(f))    
        pieces += [frame.transpose()]
    res = pandas.concat(pieces)
    res = np.array(res)
    return res