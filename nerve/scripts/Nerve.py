
'''
nerve

Created on Jan 28, 2015

@author: Raouf.
'''

import time
from math import sqrt
from operator import itemgetter 
from inspect import getsourcelines, getsource
import numpy as np
import networkx as nx
from filters import apply_filters
from cover import cover, clique_cover
from cluster import cluster, kmeans


 
 
def pre_image(Bi, data):
    Xi = (data.transpose()[sorted(Bi)]).transpose()
    return Xi

def get_node_elements(node, data):
    # returns a numpy array 
    return (data.transpose()[sorted(node)]).transpose()

def find_idx (x, data):
    # returns col index of x in data/ x can be a list of xs
    ldata =  map(str, list(data.transpose()))
    if type(x) == list:
        return {ldata.index(y) for y in map(str, x)}
    return ldata.index(str(x))

def nerve (data = None, filters = None, threshhold = None, n_clusters = 8, cover_algo = clique_cover, cluster_algo = kmeans):
    # returns nerve graph and nodes components  
    R = apply_filters (filters, data)
    R_cover = cover(R, threshhold, algo = cover_algo)  

    print "clustering preimages, number of preimages =", len(R_cover)
    nodes_ = []
    for Bi in R_cover:
        Xi = pre_image(Bi, data)
        nodes_ += cluster(Xi, n_clusters, algo = cluster_algo).values() 

    nodes = []
    for node in nodes_:
        if not find_idx(node, data) in nodes:
            nodes += [find_idx(node, data)]      
    
    # edges are intersecting nodes 
    edges = [] 
    for i in range(0, len(nodes)-1):
        for j in range(i+1, len(nodes)):
            s = set(map(str, nodes[i])) # !! Casting: one needs to double check this, I convert to string to make the intersection possible as there is no way to cast a list arrays to set of arrays - the trick I use here is map str to the list of arrays and then cast to set
            t = set(map(str, nodes[j]))
            if not len(s.intersection(t))==0:
                edges += [(i, j)]          

    G = nx.Graph()
    G.add_nodes_from(range(0, len(nodes)))
    G.add_edges_from(edges)
    return G, nodes



if __name__ == '__main__':
    unit_square = np.array([[0, 0, 1, 1], [0, 1, 0, 1]])
    pr1 = lambda x: x[0]
    pr2 = lambda x: x[1]
    square_nerve = nerve (data = unit_square, filters = (pr1, pr2), threshhold=1.1, n_clusters=1)
    print square_nerve[0].edges()

