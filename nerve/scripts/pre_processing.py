'''
pre_processing: for now it has only impute function

Created on Jan 28, 2015

@author: Raouf.

'''

import numpy as np
from pandas import DataFrame


def load_and_impute(fileName, _usecols=None, _skip_header=None): 
	# load and impute data: replace NaN by the mean of the row (thats why I do transpose, since apply is for col)
    data = np.genfromtxt(fileName, dtype=float, delimiter=',', usecols=_usecols, skip_header=_skip_header)
    df = DataFrame(data)  
    return np.array((df.transpose().apply(lambda x: x.fillna(x.mean())).transpose())) 

def load_and_impute(fileName, _usecols=None): 
	# load annd impute data: replace NaN by the mean of the row (thats why I do transpose, since apply is for col)
    data = np.genfromtxt(fileName, dtype=float, delimiter=',', usecols=_usecols)
    df = DataFrame(data)  
    return np.array((df.transpose().apply(lambda x: x.fillna(x.mean())).transpose())) 

 
