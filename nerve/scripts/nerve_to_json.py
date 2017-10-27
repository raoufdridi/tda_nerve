'''
nerve_to_json

Created on Jan 28, 2015

@author: Raouf.
'''

import json
import os
from subprocess import call
from numpy import array
from Nerve import *


def nerve_to_json(Nerve, file_name, color = lambda c: 1):
    # graph suitable for d3js
    [G, clusters] = Nerve
    nodesList_ = []
    for i in range(0, len(clusters)):
        nodesList_ += [dict({"name":i, "size":len(clusters[i]), "color": color(clusters[i])})]
    linksList_ = []
    for link in G.edges():
        #print link
        linksList_ += [dict({"source":link[0], "target":link[1]})]
    res = dict({"nodes":nodesList_, "links":linksList_, "nbrOfNodes":len(G.nodes()) , "nbrOfEdges":len(linksList_)})
    json_res = open(file_name, 'wb')
    json.dump(res,json_res)
    json_res.close()
    return res



def showme(Nerve, coloring = lambda c: 1):   
    new_file_name = "../html/graph/nerveGraph" + time.strftime("%Y-%m-%d-%H-%M-%S")
    call(["cp", "../html/graph/nerveGraph", "new_file_name"])
    nerve_to_json(Nerve, '../html/graph/nerveGraph', color = coloring)
    os.system("open -a /Applications/Safari.app ../html/index.html")
    return 0

if __name__ == '__main__':
    unit_square = array([[0, 0, 1, 1], [0, 1, 0, 1]])
    pr1 = lambda x: x[0]
    pr2 = lambda x: x[1]
    square_nerve = nerve (data = unit_square, filters = (pr1, pr2), threshhold=1.1, n_clusters=1)
    showme(square_nerve)
