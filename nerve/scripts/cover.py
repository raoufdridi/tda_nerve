'''
cover

Created on Jan 28, 2015

@author: Raouf.
'''
from VR_graph import data_to_graph
from networkx import find_cliques
from numpy import array





def clique_cover(R, threshhold): 
	# - takes a numpy array and returns maximal cliques covering graph corresponding to R
	# - each clique is a set of column indices of R 
	# - for now it has covering in terms of maximal cliques. Min clique cover is coming soon
    G = data_to_graph(R, threshhold)
    return list(find_cliques(G)) 

def box_cover (R, threshhold):
	return "to be done"


def cover(R, threshhold, algo = clique_cover):
	# returns cover in terms of columns indices of R 
	return algo(R, threshhold)


if __name__ == '__main__':
	import matplotlib.pyplot as plt
	unit_square = array([[0, 0, 1, 1], [0, 1, 0, 1]])
	print "data", unit_square
	print "cover, [cover_set1, cover_set2, ...]", cover(unit_square, 1.1)



