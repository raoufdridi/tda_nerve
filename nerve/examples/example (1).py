'''
NKI complete data
Created on Jan 28, 2015

@author: Raouf.
'''

import os, sys
sys.path.insert(0, os.path.abspath("../scripts/"))

from pre_processing import *
from Nerve import nerve, get_node_elements
from numpy import array, mean
from filters import euclidean_distance
from nerve_to_json import showme

def laod_and_impute_NKI(numbers):
    #numbers = [1, 2, 3, 4, 5, 6]
    pieces = [] 
    for number in numbers:
        path = '../../data/NEJM_NKI/Table_NKI_295_%d.csv' % number
        if number <6:
        	frame = load_and_impute(path, tuple(5*i for i in range(0, 50))) 
        if number == 6:
        	frame = load_and_impute(path, tuple(5*i for i in range(0, 45))) 
        pieces += [frame.transpose()]
    return np.concatenate(pieces).transpose()  


# Loading data
data = laod_and_impute_NKI([1]) 
print "data loaded, data.shape ", data.shape
eventDeathData = np.genfromtxt('../../data/NEJM_NKI/EventDeath.csv', dtype=float, delimiter=',')

# filters
f= lambda x: euclidean_distance(x, data.transpose()[0]) #euclidean_distance from a survival
g= lambda x: euclidean_distance(x, data.transpose()[9]) #euclidean_distance from a patient who didnt survive

# survivors and non survivors data
my_list0 =[]
my_list1 =[]
for i in range(0, data.shape[1]):
	if eventDeathData[i, 1] == 0:
		my_list0 += [i]
	else:
		my_list1 += [i]


data0 = data.transpose()[my_list0].transpose()
data1 = data.transpose()[my_list1].transpose()   #not survival in data

# nerve
nerve0 = nerve(data=data0, filters = (f, g), threshhold =30, n_clusters=5)
#nerve1 = nerve(data=data1, filters = (f, g), threshhold =4.5, n_clusters=2)

#
def esr1_coloring(node):
	X = get_node_elements(node, data) 
	return mean(map(lambda x: 10**array(x)[18903], X.transpose()))
	
showme(nerve0, esr1_coloring)


