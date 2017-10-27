'''
VR graph

Created on Jan 28, 2015

@author: Raouf.
'''
import networkx as nx
import numpy as np
from filters import euclidean_distance

def data_to_graph(data, threshhold, distance = euclidean_distance):  
	# nodes are column-indices of data
    G = nx.Graph() 
    G.add_nodes_from(range(0, data.shape[1]))
    #print G.nodes()
    links = []
    for i in range(0, data.shape[1]-1):
        for j in range(i+1, data.shape[1]):
            #print "--------------"
            #print i, j
            #print data.transpose()[i], data.transpose()[j], distance(data.transpose()[i], data.transpose()[j])
            if distance(data.transpose()[i], data.transpose()[j]) < threshhold:
                links += [ (i, j)]
    G.add_edges_from(links)
    return G

if __name__ == '__main__':
	import matplotlib.pyplot as plt
	unit_square = np.array([[0, 0, 1, 1], [0, 1, 0, 1]])
	G = data_to_graph(unit_square, 1.1)
	print G.edges()
	

